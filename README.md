# Gibbs Locality Obstruction

**Can a physical operation confined to part of an interacting quantum system preserve its entire Gibbs state exactly?**

For generic two-body qubit Hamiltonians on any fixed finite connected graph, the answer is **only if the operation is the identity**. This holds on every proper subsystem, including disconnected subsets and regions containing all but one site, at every finite nonzero inverse temperature.

$$
(\mathcal E_A\otimes\operatorname{id}_{A^c})(\rho_\beta)=\rho_\beta
\quad\Longrightarrow\quad
\mathcal E_A=\operatorname{id}_A,
\qquad
\rho_\beta=\frac{e^{-\beta H}}{\operatorname{Tr}(e^{-\beta H})}.
$$

Here “generic” means an open dense set of full measure in the real coefficient space of all allowed one-site and edge two-site interactions. The exceptional Hamiltonians form a proper algebraic set. The same generic Hamiltonian satisfies the conclusion for all finite nonzero inverse temperatures.

## Principal results

| Result | Meaning |
|---|---|
| Exact Gibbs/channel criterion | A nonidentity preserving local channel exists exactly when a non-scalar conserved observable exists on that subsystem. The state-level channel theorem is due to Lie and Ng. |
| Constructive connected-graph theorem | Weighted $`XX+ZZ`$ interactions with nonzero weights and distinct squared incident weights have no non-scalar conserved observable on any proper subset. A polynomial argument gives genericity. |
| Tight support requirement | Every nonzero physical update in an exact frustration-free Gibbs sampler must have full support. A global reset attains that support as an existence construction. |
| Explicit Ising family | Every open transverse-field Ising chain with nonzero fields and couplings is rigid on proper intervals. The homogeneous four-spin chain is rigid on every proper subset. |

The state-level characterization is [established prior work](references/related-work.md). The [graph construction and genericity proof](science/hamiltonian-rigidity.md) supply the local-Hamiltonian result.

## Read the science

Start with the [question, model, and exact statements](science/model.md), then follow the [channel criterion](science/channel-criterion.md), [Hamiltonian proof](science/hamiltonian-rigidity.md), and [consequences for Gibbs dynamics](science/local-updates.md).

| To inspect | Read |
|---|---|
| Allowed Hamiltonians, channels, supports, and temperatures | [Model and results](science/model.md) |
| Why a preserving channel implies a conserved local observable | [Channel criterion](science/channel-criterion.md) |
| Boundary separation, Vandermonde inversion, and genericity | [Hamiltonian rigidity](science/hamiltonian-rigidity.md) |
| Exact support bound, global reset, cancellation, and approximate updates | [Local updates](science/local-updates.md) |
| Ising proofs, classical heatbath updates, and symmetry exceptions | [Examples](science/examples.md) |
| Established ingredients and comparisons with thermalization results | [Related work](references/related-work.md) and [bibliography](references/references.bib) |
| Exact finite checks and their interpretation | [Verification](verification/README.md) |

The [LLM reading guide](llms.txt) maps scientific questions to the authoritative files.

## Reproduce the finite checks

From the repository root:

~~~bash
python -m pip install -r verification/requirements.txt
python verification/verify.py
~~~

The suite uses exact rational Pauli commutator matrices and checks weighted path, star, and cycle examples, the four-spin Ising chain, and explicit exceptions. A separate dense-matrix calculation checks phases and tensor ordering. No floating-point rank threshold or thermal matrix exponential is used.

These calculations validate finite examples and the implementation. The arbitrary-graph theorem and its genericity follow from the written proof.

## Scope and interpretation

Every update in the obstruction must be physical in its own right and preserve the global Gibbs state exactly. For continuous time, each summand must itself be a Lindblad generator. Global stationarity alone does not imply these conditions.

The result allows approximate updates, generators with decaying but nonzero tails, and local circuit steps that do not individually preserve the target. It gives no uniform lower bound on disturbance or tail strength. The global reset establishes attainability of the spatial support bound and assumes the resources needed to prepare the target state; it is not an efficient Gibbs-preparation algorithm.

The [four-spin Ising proof](science/examples.md#four-spin-ising-chain) also gives a precise mathematical comparison with an earlier numerical stabilization claim. The [related-work account](references/related-work.md) states the incompatibility and the limits of what can be inferred about that computation.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

