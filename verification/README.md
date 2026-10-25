# Exact verification

This suite checks the finite-dimensional algebra underlying local Gibbs rigidity. It uses exact rational arithmetic throughout the commutator and rank calculations. It does not evaluate a thermal matrix exponential or use a numerical rank threshold.

## Run

Python 3.10 or newer is required. From the repository root:

```sh
python -m pip install -r verification/requirements.txt
python verification/verify.py
```

The script writes `verification/results.json` and exits unsuccessfully if an expected rank, conserved observable, or channel property fails. It accepts an optional `--output PATH`. The output records the Python and SymPy versions; no random seed is needed.

## What is computed

For a support $A$, expand a traceless Hermitian observable in the Pauli basis and form the real linear map

$$
K_A(H):Q_A\longmapsto\frac{[Q_A\otimes I_{A^c},H]}{2i}.
$$

The matrix has $4^n$ rows and $4^{|A|}-1$ columns. Its coefficients are rational for all Hamiltonians in this suite. `SymPy DomainMatrix.rref`, explicitly over the field `QQ`, gives the rank. The full local commutant has dimension

$$
1+\bigl(4^{|A|}-1-\mathrm{rank}K_A(H)\bigr).
$$

The added one is the identity, which is excluded from the input basis. Site labels start at zero, with site 0 the leftmost tensor factor. The result file lists every Hamiltonian as a Pauli coefficient dictionary.

An independent check reconstructs all 15 commutator columns on the disconnected support $A=\{0,2\}$ of a three-qubit weighted path. It compares the Pauli implementation against direct dense Kronecker products. This checks phases, normalization, and tensor ordering using a separate matrix representation.

## Expected results

For the graph witnesses,

$$
H_G=\sum_{\{i,j\}\in E}w_{ij}(X_iX_j+Z_iZ_j).
$$

The path uses weights $1,5/4,3/2$; the star uses the same weights on the three edges incident on its center; the cycle uses $1,5/4,3/2,7/4$. These are bounded, positive rational weights with distinct squared weights at each vertex.

| Case | Support checked | Expected rank | Full commutant dimension |
|---|---|---:|---:|
| Weighted path, $n=4$ | Each of the four three-site subsets | 63 | 1 |
| Weighted star, $n=4$ | Each of the four three-site subsets | 63 | 1 |
| Weighted cycle, $n=4$ | Each of the four three-site subsets | 63 | 1 |
| Homogeneous open TFIM, $n=4$, $J=g=1$ | Each of the four three-site subsets | 63 | 1 |
| Equal-weight star, $n=4$ | Its three leaves | 59 | 5 |
| Commuting open Ising chain, $n=4$, $g=0$ | Site 0 | 2 | 2 |
| Homogeneous open TFIM, $n=3$, $J=g=1$ | Disconnected endpoints $\{0,2\}$ | 14 | 2 |

Here the transverse-field Ising convention is

$$
H_{\rm TFIM}=-\sum_{j=0}^{n-2}Z_jZ_{j+1}-g\sum_{j=0}^{n-1}X_j.
$$

Checking every support of size $n-1$ covers every smaller proper support for that same Hamiltonian: any smaller-support commuting operator can be extended by identities to an $n-1$-site support. A nonzero traceless observable remains nonzero and traceless under this extension. Thus the 16 positive rank checks establish scalar commutants for every proper subset of each of these four explicit four-qubit Hamiltonians.

### Why the exceptions are included

- **Repeated boundary weights:** the equal-weight star preserves permutations of its leaves. The script constructs `SWAP(1,2)` as a computational-basis permutation and verifies its commutator exactly. The three-leaf collective-spin commutant has dimension $1^2+2^2=5$, explaining rank 59. This checks the failure of individual-spin separation when the Vandermonde nodes coincide. Distinct squared weights are a sufficient witness condition, not a claimed necessary condition for every rigid Hamiltonian.
- **Commuting interactions:** at $g=0$, the Ising chain commutes with $Z_0$. Local dephasing in the $Z_0$ basis therefore preserves its Gibbs state at every temperature. The script verifies the conserved observable directly.
- **Symmetry-restricted families:** for the odd three-site homogeneous TFIM, reflection is `SWAP(0,2)` and acts trivially on the central site. It is a nonscalar conserved operator with proper disconnected support. Thus all-subset genericity in the full interaction space cannot simply be transferred to the homogeneous reflection-symmetric family. This exception does not concern the theorem for proper contiguous intervals.
- **Infinite temperature:** at $\beta=0$, every Hamiltonian has Gibbs state $I/16$ in the four-site example. The nonidentity local CPTP channel $\mathcal E(M)=(M+Z_0MZ_0)/2$ fixes that state exactly. It changes the valid probe state $(I+X_0)/16$ and sends $X_0$ to zero. This verifies why the finite-temperature rigidity statement excludes $\beta=0$.

## What these checks do and do not establish

These are exact finite checks of representative graph geometries, the disconnected-support issue, and explicit scope boundaries. They are not a proof of the arbitrary-size theorem or an estimate of how often a randomly chosen Hamiltonian is rigid. The general proof must establish boundary coefficient isolation, Vandermonde separation, iterative removal of boundary sites, and the nonzero-polynomial genericity argument.

The passage from scalar local commutants to channel rigidity uses the known characterization of sensitivity to nonidentity local channels, together with

$$
[Q_A\otimes I,e^{-\beta H}]=0\quad\Longleftrightarrow\quad[Q_A\otimes I,H]=0
\qquad(0<|\beta|<\infty).
$$

The channel characterization is due to Lie and Ng, *Physical Review A* **108**, 012417 (2023), Theorem 3: [arXiv:2303.02376](https://arxiv.org/abs/2303.02376). The suite does not independently prove that characterization. Its Lindbladian consequence concerns individually valid GKSL terms that each annihilate the Gibbs state. It gives no quantitative disturbance bound, approximate-sampling lower bound, or claim about cancellations between local terms.

## Cost and limits

For a Hamiltonian with $T$ Pauli terms, assembling a support matrix takes $O(nT4^{|A|})$ elementary Pauli operations. Exact Gaussian elimination is exponential in the support size; a dense arithmetic-operation bound is $O(4^n(4^{|A|})^2)$, with additional rational bit growth. The largest matrix used here is $256\times63$; there are 19 rank computations in total. This is a small-system verification tool, not a many-body scalability benchmark. Runtime is printed by the script, while the JSON omits timing so its scientific content remains reproducible.
