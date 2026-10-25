#!/usr/bin/env python3
"""Exact finite checks of local commutant rigidity and its scope.

All Hamiltonian coefficients and rank computations use rational arithmetic.
No thermal matrix exponential, floating-point rank tolerance, or random draw
is used. See README.md for the distinction between these checks and the proof.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
from pathlib import Path
from time import perf_counter

import sympy as sp
from sympy.polys.domains import QQ
from sympy.polys.matrices import DomainMatrix


ALPHABET = "IXYZ"
PAULI = {
    "I": sp.eye(2),
    "X": sp.Matrix([[0, 1], [1, 0]]),
    "Y": sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    "Z": sp.diag(1, -1),
}
# An entry (letter, exponent) represents i**exponent times that Pauli matrix.
PRODUCT = {(a, "I"): (a, 0) for a in ALPHABET}
PRODUCT.update({("I", a): (a, 0) for a in ALPHABET})
PRODUCT.update({(a, a): ("I", 0) for a in "XYZ"})
for a, b, c in ("XYZ", "YZX", "ZXY"):
    PRODUCT[a, b] = (c, 1)
    PRODUCT[b, a] = (c, 3)


def require(condition: bool, message: str) -> None:
    """Checks remain active when Python is invoked with -O."""
    if not condition:
        raise RuntimeError(message)


def word(n: int, entries: dict[int, str]) -> str:
    letters = ["I"] * n
    for site, letter in entries.items():
        require(0 <= site < n and letter in ALPHABET, "Invalid Pauli entry")
        letters[site] = letter
    return "".join(letters)


def add_term(terms: dict[str, sp.Rational], p: str, coefficient) -> None:
    coefficient = sp.sympify(coefficient)
    require(coefficient.is_Rational is True, "Only exact rational coefficients are accepted")
    terms[p] = terms.get(p, sp.S.Zero) + coefficient
    if terms[p] == 0:
        del terms[p]


def weighted_graph(n: int, edges) -> dict[str, sp.Rational]:
    terms: dict[str, sp.Rational] = {}
    for i, j, weight in edges:
        require(i != j, "Self-loops are not graph edges")
        for letter in "XZ":
            add_term(terms, word(n, {i: letter, j: letter}), weight)
    return terms


def tfim(n: int, field=1) -> dict[str, sp.Rational]:
    terms: dict[str, sp.Rational] = {}
    for i in range(n - 1):
        add_term(terms, word(n, {i: "Z", i + 1: "Z"}), -1)
    for i in range(n):
        add_term(terms, word(n, {i: "X"}), -sp.sympify(field))
    return terms


def multiply(p: str, q: str) -> tuple[str, int]:
    require(len(p) == len(q), "Pauli words must have equal lengths")
    letters, exponent = [], 0
    for a, b in zip(p, q):
        c, power = PRODUCT[a, b]
        letters.append(c)
        exponent += power
    return "".join(letters), exponent % 4


def row_index(p: str) -> int:
    index = 0
    for letter in p:
        index = 4 * index + ALPHABET.index(letter)
    return index


def local_basis(n: int, support: tuple[int, ...]) -> list[str]:
    require(tuple(sorted(set(support))) == support, "Support must be sorted and distinct")
    require(all(0 <= site < n for site in support), "Support outside the system")
    return [
        word(n, dict(zip(support, letters)))
        for letters in itertools.product(ALPHABET, repeat=len(support))
        if any(letter != "I" for letter in letters)
    ]


def commutator_matrix(n: int, terms, support: tuple[int, ...]):
    """Matrix of Q -> [Q tensor I, H]/(2i) in unnormalized Pauli bases.

    The columns omit the scalar identity. Since Pauli words are Hermitian,
    a product phase +/-1 means the words commute, while +/-i gives the
    corresponding coefficient +/-1 after division by 2i.
    """
    columns = local_basis(n, support)
    entries = {}
    for column, p in enumerate(columns):
        for q, coefficient in terms.items():
            r, phase = multiply(p, q)
            if phase in (1, 3):
                key = row_index(r), column
                sign = 1 if phase == 1 else -1
                entries[key] = entries.get(key, sp.S.Zero) + sign * coefficient
    entries = {key: value for key, value in entries.items() if value != 0}
    return sp.SparseMatrix(4**n, len(columns), entries), columns


def exact_rank(matrix) -> int:
    rational_matrix = DomainMatrix.from_Matrix(matrix).convert_to(QQ)
    _, pivots = rational_matrix.rref()
    return len(pivots)


def rank_record(n: int, terms, support: tuple[int, ...], expected: int) -> dict:
    matrix, _ = commutator_matrix(n, terms, support)
    rank = exact_rank(matrix)
    require(rank == expected, f"Unexpected rank on support {support}: {rank} != {expected}")
    return {
        "support_zero_based": list(support),
        "matrix_shape": list(matrix.shape),
        "matrix_nonzero_entries": matrix.nnz(),
        "rank_over_Q": rank,
        "expected_rank": expected,
        "traceless_kernel_dimension": matrix.cols - rank,
        "commutant_dimension_including_identity": 1 + matrix.cols - rank,
        "passed": True,
    }


def dense_pauli(p: str):
    return sp.kronecker_product(*(PAULI[letter] for letter in p))


def dense_hamiltonian(n: int, terms):
    result = sp.zeros(2**n)
    for p, coefficient in terms.items():
        result += coefficient * dense_pauli(p)
    return result


def swap_matrix(n: int, i: int, j: int):
    """Independent computational-basis permutation, with site 0 leftmost."""
    result = sp.zeros(2**n)
    for source in range(2**n):
        bits = list(f"{source:0{n}b}")
        bits[i], bits[j] = bits[j], bits[i]
        result[int("".join(bits), 2), source] = 1
    return result


def conserved_observable_record(n: int, terms, observable, description: str, support) -> dict:
    hamiltonian = dense_hamiltonian(n, terms)
    scalar_part = sp.trace(observable) * sp.eye(2**n) / 2**n
    require(observable == observable.H, "Conserved observable is not Hermitian")
    require(observable != scalar_part, "Conserved observable is scalar")
    require(observable * hamiltonian == hamiltonian * observable,
            f"Observable does not commute with H: {description}")
    return {"observable": description, "support_zero_based": list(support),
            "nonscalar_Hermitian": True, "commutator_is_exactly_zero": True}


def independent_dense_crosscheck() -> dict:
    # Nonadjacent support exercises the tensor ordering; all 15 columns include
    # both real and imaginary Pauli factors. Dense products use a separate
    # representation from PRODUCT and row_index.
    n, support = 3, (0, 2)
    terms = weighted_graph(n, [(0, 1, 1), (1, 2, sp.Rational(3, 2))])
    matrix, columns = commutator_matrix(n, terms, support)
    hamiltonian = dense_hamiltonian(n, terms)
    rows = ["".join(p) for p in itertools.product(ALPHABET, repeat=n)]
    for column, p in enumerate(columns):
        reconstructed = sp.zeros(2**n)
        for row in range(matrix.rows):
            if matrix[row, column] != 0:
                reconstructed += matrix[row, column] * dense_pauli(rows[row])
        observable = dense_pauli(p)
        direct = (observable * hamiltonian - hamiltonian * observable) / (2 * sp.I)
        require(reconstructed == direct, f"Dense crosscheck failed for {p}")
    return {"n": n, "support_zero_based": list(support),
            "columns_checked": len(columns), "all_exactly_equal": True}


def terms_record(terms) -> dict[str, str]:
    return {p: str(coefficient) for p, coefficient in sorted(terms.items())}


def run_suite() -> dict:
    dense_check = independent_dense_crosscheck()
    n = 4
    positive_cases = []
    witnesses = [
        ("weighted_path_4", weighted_graph(n, [
            (0, 1, 1), (1, 2, sp.Rational(5, 4)), (2, 3, sp.Rational(3, 2))])),
        ("weighted_star_4", weighted_graph(n, [
            (0, 1, 1), (0, 2, sp.Rational(5, 4)), (0, 3, sp.Rational(3, 2))])),
        ("weighted_cycle_4", weighted_graph(n, [
            (0, 1, 1), (1, 2, sp.Rational(5, 4)),
            (2, 3, sp.Rational(3, 2)), (3, 0, sp.Rational(7, 4))])),
        ("homogeneous_tfim_4", tfim(n)),
    ]
    for name, terms in witnesses:
        supports = []
        for omitted in range(n):
            support = tuple(site for site in range(n) if site != omitted)
            record = rank_record(n, terms, support, expected=4**(n - 1) - 1)
            record["omitted_vertex_zero_based"] = omitted
            supports.append(record)
        positive_cases.append({"name": name, "n": n,
                               "hamiltonian_pauli_coefficients": terms_record(terms),
                               "maximal_proper_support_checks": supports})

    # Repeated boundary weights prevent individual-spin isolation. On the
    # three star leaves, the collective-spin commutant has dimension 5.
    equal_star = weighted_graph(4, [(0, 1, 1), (0, 2, 1), (0, 3, 1)])
    equal_star_record = {
        "name": "equal_weight_star_boundary_separation_exception",
        "n": 4,
        "hamiltonian_pauli_coefficients": terms_record(equal_star),
        "rank_check": rank_record(4, equal_star, (1, 2, 3), expected=59),
        "conserved_observable": conserved_observable_record(
            4, equal_star, swap_matrix(4, 1, 2), "SWAP(1,2)", (1, 2)),
    }

    ising = tfim(4, field=0)
    ising_record = {
        "name": "commuting_ising_exception", "n": 4,
        "hamiltonian_pauli_coefficients": terms_record(ising),
        "rank_check": rank_record(4, ising, (0,), expected=2),
        "conserved_observable": conserved_observable_record(
            4, ising, dense_pauli("ZIII"), "Z_0", (0,)),
    }

    odd_tfim = tfim(3)
    reflection_record = {
        "name": "odd_homogeneous_tfim_reflection_exception", "n": 3,
        "hamiltonian_pauli_coefficients": terms_record(odd_tfim),
        "rank_check": rank_record(3, odd_tfim, (0, 2), expected=14),
        "conserved_observable": conserved_observable_record(
            3, odd_tfim, swap_matrix(3, 0, 2), "reflection = SWAP(0,2)", (0, 2)),
    }

    # At beta=0, local dephasing fixes I/d for every Hamiltonian. It is a
    # nonidentity CPTP map: a mixture of conjugations by I and Z_0.
    dimension = 2**4
    maximally_mixed = sp.eye(dimension) / dimension
    z0, x0 = dense_pauli("ZIII"), dense_pauli("XIII")
    dephase = lambda matrix: (matrix + z0 * matrix * z0) / 2
    probe_state = (sp.eye(dimension) + x0) / dimension
    require(dephase(maximally_mixed) == maximally_mixed, "beta=0 stationarity failed")
    require(dephase(probe_state) != probe_state, "Dephasing should change the probe state")
    require(dephase(x0) == sp.zeros(dimension), "Dephasing should erase X_0")
    beta_zero_record = {
        "name": "beta_zero_channel_exception", "n": 4, "beta": "0",
        "channel": "E(M) = (M + Z_0 M Z_0)/2",
        "support_zero_based": [0],
        "CPTP_reason": "equal mixture of two unitary conjugations",
        "fixes_I_over_16_exactly": True,
        "changes_probe_state_(I+X_0)_over_16": True,
        "maps_X_0_to_zero_exactly": True,
    }

    return {
        "schema_version": 1,
        "environment": {"python": platform.python_version(), "sympy": sp.__version__},
        "method": {
            "field": "QQ (exact rationals)",
            "linear_map": "Q_A -> [Q_A tensor I, H]/(2i)",
            "basis": "unnormalized Pauli words; scalar identity excluded from domain",
            "rank_algorithm": "SymPy DomainMatrix.rref after explicit conversion to QQ",
            "floating_point_rank_tolerance": None,
            "tensor_order": "site 0 is the leftmost tensor factor",
        },
        "independent_dense_crosscheck": dense_check,
        "positive_cases": positive_cases,
        "exceptions": [equal_star_record, ising_record, reflection_record, beta_zero_record],
        "summary": {
            "positive_support_rank_checks": 16,
            "exception_rank_checks": 3,
            "independent_dense_columns_checked": dense_check["columns_checked"],
            "all_checks_passed": True,
            "scope": "finite exact checks; the arbitrary-graph and genericity claims require proof",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().with_name("results.json"))
    args = parser.parse_args()
    start = perf_counter()
    results = run_suite()
    args.output.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS: 16 rigidity ranks, 3 exception ranks, 15 dense crosschecks, and beta=0 channel.")
    print(f"Exact results: {args.output}")
    print(f"Elapsed: {perf_counter() - start:.3f} seconds")


if __name__ == "__main__":
    main()
