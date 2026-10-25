# Question, model, and results

## Why Gibbs-preserving updates are a locality question

A classical heatbath update resamples one spin conditioned on its neighbors and leaves the entire equilibrium distribution unchanged. Repeating such updates can produce a thermal sampler. For an interacting quantum system, preserving the reduced state of the updated spins is a much weaker requirement than preserving the global Gibbs state: an operation can keep the local density matrix while changing its correlations with the rest.

This project asks which physical operations confined to a proper subsystem can leave the **whole Gibbs state exactly unchanged**. The answer is governed by conserved observables confined to the same subsystem. For generic local qubit Hamiltonians on a connected graph, no such non-scalar observable exists on any proper subsystem.

The [channel criterion](channel-criterion.md) is inherited from the sensitivity theorem of Lie and Ng. The [Hamiltonian theorem](hamiltonian-rigidity.md) supplies the graph construction and genericity argument. Their combination yields the [local-update obstruction](local-updates.md).

## Finite graph and Hamiltonian family

Let $`G=(V,E)`$ be a fixed finite, connected, simple graph with $`n=|V|\geq2`$ qubits and Hilbert space $`\mathcal H_V=(\mathbb C^2)^{\otimes n}`$. Consider the full real coefficient family

$$
H(h,J)=
\sum_{i\in V}\sum_{a=x,y,z} h_i^a\,\sigma_i^a
+
\sum_{\{i,j\}\in E}\sum_{a,b=x,y,z}
J_{ij}^{ab}\,\sigma_i^a\sigma_j^b .
$$

An additive scalar has been omitted because it changes neither the Gibbs state nor commutators. The coefficient space is $`\mathbb R^{3n+9|E|}`$. No translation invariance, disorder distribution, spectral nondegeneracy, integrability, or mixing hypothesis is imposed.

For finite inverse temperature $`0<\beta<\infty`$, define

$$
\rho_\beta(H)=\frac{e^{-\beta H}}{\mathrm{Tr}(e^{-\beta H})}.
$$

This state is faithful: all its eigenvalues are positive. The algebraic statements also hold at finite negative $`\beta`$, but ordinary positive-temperature equilibrium is the physical setting used here. Infinite temperature, $`\beta=0`$, and the zero-temperature limit are separate cases.

## Supported operators, channels, and generators

An observable supported on $`A\subseteq V`$ has the form $`Q_A\otimes I_{A^c}`$. A channel supported on $`A`$ has the form $`\mathcal E_A\otimes\mathrm{id}_{A^c}`$, where $`\mathcal E_A`$ is completely positive and trace preserving (CPTP). The support can be disconnected and can contain $`n-1`$ sites.

Exact Gibbs preservation means

$$
(\mathcal E_A\otimes\mathrm{id}_{A^c})(\rho_\beta)=\rho_\beta.
$$

This is equality of the global state. Equality only of the marginal on $`A`$ does not satisfy the condition.

A local Lindblad generator is $`\mathcal L_A=\ell_A\otimes\mathrm{id}_{A^c}`$, with

$$
\ell_A(X)=-i[K_A,X]
+\sum_\mu\left(
V_\mu X V_\mu^\dagger
-\frac12\{V_\mu^\dagger V_\mu,X\}
\right).
$$

Thus $`e^{t\ell_A}`$ is CPTP for every $`t\geq0`$. Each term in a frustration-free decomposition is required to be a generator of this form, and the Gibbs state must be individually stationary under it:

$$
\mathcal L=\sum_\alpha\mathcal L_{A_\alpha},
\qquad
\mathcal L_{A_\alpha}(\rho_\beta)=0
\quad\text{for every }\alpha.
$$

The individual physicality and stationarity requirements are part of the model. A decomposition of a globally physical generator into arbitrary linear superoperators does not satisfy this definition automatically.

## Principal theorem

**Generic Gibbs rigidity.** For every graph above, there is a nonzero real polynomial $`F_G(h,J)`$ such that, whenever $`F_G(h,J)\neq0`$,

$$
(\mathcal E_A\otimes\mathrm{id}_{A^c})(\rho_\beta)=\rho_\beta
\quad\Longrightarrow\quad
\mathcal E_A=\mathrm{id}_A
$$

for **every** nonempty proper subset $`A\subsetneq V`$, **every** CPTP map $`\mathcal E_A`$, and **every** finite $`\beta\neq0`$, for the same Hamiltonian.

Consequently the rigid Hamiltonians form an open dense set of full Lebesgue measure in the stated coefficient space. Any absolutely continuous distribution on that full space assigns probability one to the conclusion. Genericity in a symmetry-restricted family requires a witness within that family.

The theorem is proved without sampling random Hamiltonians. An explicit bounded-coupling Hamiltonian has the required property on every connected graph; a finite product of commutator Gram determinants then establishes genericity.

## Consequences and explicit examples

| Result | Assumptions and meaning | Authoritative account |
|---|---|---|
| Gibbs/channel criterion | A nonidentity preserving channel exists exactly when a non-scalar local conserved observable exists. The state-level sensitivity theorem is known. | [Channel criterion](channel-criterion.md) |
| Generic graph theorem | Full one-site and edge two-site coefficient family; every proper support; the same generic Hamiltonian at all finite nonzero inverse temperatures. | [Hamiltonian rigidity](hamiltonian-rigidity.md) |
| Exact support requirement | Every nonzero, individually Gibbs-preserving local Lindblad term has full support. A global reset shows that the support requirement is attainable as an existence statement. | [Local updates](local-updates.md) |
| Open Ising chain | All nonzero fields and couplings imply rigidity on every proper contiguous interval. | [Examples](examples.md#open-ising-chain) |
| Four-spin Ising chain | For homogeneous nonzero field and coupling, rigidity holds on every proper subset, including disconnected triples. | [Four-spin proof](examples.md#four-spin-ising-chain) |
| Exceptional families | Classical commuting models, disconnected graphs, and certain spatial symmetries admit nontrivial proper-support preservers. | [Examples and exceptions](examples.md) |

## What the conclusion changes

For the stated class of exact physical updates, finite spatial support is not merely an implementation inconvenience: the nontrivial update itself does not exist. Even allowing an update to touch all but one site does not remove the generic obstruction.

The claim does not quantify how large the omitted tail of an approximate update must be. It also leaves room for local operations whose effects cancel, gates in a circuit that individually change the target state, and globally supported generators with rapidly decaying tails. These distinctions are developed with explicit examples in [Local updates](local-updates.md).

For attribution and the precise relation to prior Gibbs-sampler questions, see [Related work](../references/related-work.md). For finite exact calculations and their scope, see [Verification](../verification/README.md).

[Repository overview](../README.md)

