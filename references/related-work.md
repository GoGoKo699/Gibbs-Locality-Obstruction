# Related work and scope of the contribution

[Repository overview](../README.md) · [Bibliography](references.bib) · [Channel criterion](../science/channel-criterion.md) · [Hamiltonian theorem](../science/hamiltonian-rigidity.md)

## Contribution and inherited ingredients

The contribution developed here is a statement about the restricted family of **local Hamiltonians**. On each fixed finite connected graph of qubits, a generic Hamiltonian with arbitrary one-site and edge-supported two-site interactions has no nonscalar conserved operator supported on any proper subsystem. The [Hamiltonian theorem](../science/hamiltonian-rigidity.md) gives an explicit interaction Hamiltonian with this property and proves that the exceptions form a proper algebraic subset of the full coefficient space. One Hamiltonian therefore satisfies the conclusion simultaneously for every proper subsystem and every finite nonzero inverse temperature.

The channel-theoretic ingredient is established prior work. [Lie and Ng, Theorem 3](https://arxiv.org/html/2303.02376v1), prove that a bipartite state admits a nonidentity preserving channel on one subsystem if and only if it admits a nontrivial preserving projective pinching there. In commutant language, for the faithful states needed here,

```math
\exists\,\mathcal E_A\ne\mathrm{id}_A:
(\mathcal E_A\otimes\mathrm{id}_{A^c})(\rho)=\rho
\quad\Longleftrightarrow\quad
\exists\,Q_A=Q_A^\dagger\notin\mathbb RI_A:
[Q_A\otimes I_{A^c},\rho]=0.
```

This equivalence is not claimed as new. Its structural background includes [Koashi and Imoto's decomposition of state-preserving operations](https://doi.org/10.1103/PhysRevA.66.022318) and the faithful fixed-space structure used in [Johnson, Ticozzi, and Viola, Theorem 1 and Eq. (14)](https://www.rintonpress.com/xxqic16/qic-16-78/0657-0699.pdf). The [channel-criterion page](../science/channel-criterion.md) gives the faithful specialization with explicit attribution. Lie and Ng's result is more general than this specialization.

For a finite-dimensional Gibbs state, the elementary identity

```math
\log\rho_\beta=-\beta H-\log Z_\beta\,I
```

equates its local commutant with that of $`H`$ whenever $`0<|\beta|<\infty`$. Combining this observation with the established channel criterion gives the dynamical consequence of the Hamiltonian theorem: every exactly Gibbs-preserving CPTP map on a proper subsystem is the identity. The restriction to Hamiltonians with prescribed interaction locality is substantive. A generic-state assertion by itself does not prove a generic assertion inside this much smaller Gibbs family.

## Comparison at a glance

| Work | Relevant result or setting | Relation to this project |
|---|---|---|
| [Koashi–Imoto (2002)](https://doi.org/10.1103/PhysRevA.66.022318); [Lie–Ng (2023)](https://doi.org/10.1103/PhysRevA.108.012417) | Structure and sensitivity of state-preserving operations | Inherited state-level ingredients; the locality-constrained Hamiltonian theorem is additional. |
| [Johnson–Ticozzi–Viola (2016)](https://doi.org/10.26421/QIC16.7-8-5) | Fixed spaces and exact neighborhood stabilization | Established framework; a specific four-spin numerical example conflicts with the exact calculation below. |
| [Kastoryano–Brandão (2016)](https://doi.org/10.1007/s00220-016-2641-8) | Gibbs samplers for commuting interactions | Demonstrates the importance of the Hamiltonian-family hypotheses. |
| [Chen–Kastoryano–Gilyén (2023; revised 2025)](https://arxiv.org/abs/2311.09207) | Exact noncommutative Gibbs sampler with spatially decaying tails | Compatible construction; exact strict support is the obstruction studied here. |
| [Ma–Khemani–Sang (2026)](https://doi.org/10.1103/sh48-wmy4) | Thermal phases, memory, and frustration-free Gibbs dynamics | Explicitly raises the strict-local existence question; the answer here assumes physical GKSL summands. |
| [Tupkary et al. (2023)](https://doi.org/10.1103/PhysRevA.107.062216); [Sarma et al. (2026)](https://doi.org/10.1103/jyck-mvlg) | Local master equations constrained by microscopic weak-coupling accuracy | Different stationarity requirements and different no-go conclusions. |
| [Guo et al. (2025)](https://doi.org/10.22331/q-2025-01-28-1612); [Arad–Firanko–Gurevich (2024; revised 2025)](https://arxiv.org/abs/2408.08672) | Inverse design and effective Gibbs descriptions of local dynamics | Compatible settings that do not impose all the hypotheses of the present obstruction. |

## Strict support, spatial tails, and the recent Gibbs question

The published [Ma–Khemani–Sang article](https://journals.aps.org/prxquantum/pdf/10.1103/sh48-wmy4), Eq. (26) and endnote [51], distinguishes quasi-local Gibbs-preserving dynamics from the unresolved strict-local case for generic noncommuting Hamiltonians. The question appears as footnote 3 in [arXiv v3](https://arxiv.org/html/2509.15204v3). Their decomposition assumes $`\mathcal L_X(\rho_\beta)=0`$ for each term, with exponentially accurate finite-diameter approximations. The paragraph explicitly calls the sum a Lindbladian and the individual terms superoperators; it does not separately stipulate there that every summand is GKSL.

The present result has an explicit physical-summand hypothesis. If

```math
\mathcal L=\sum_X\mathcal L_X,
\qquad
\mathcal L_X=\mathcal L_{A_X}\otimes\mathrm{id}_{A_X^c},
\qquad
\mathcal L_X(\rho_\beta)=0,
```

where each $`\mathcal L_{A_X}`$ is a GKSL generator and $`A_X\subsetneq V`$, then each semigroup $`e^{t\mathcal L_{A_X}}`$ is a preserving CPTP map. The generic theorem forces it to be the identity for every $`t\geq0`$, and hence $`\mathcal L_X=0`$. This rules out exact frustration-free relaxation assembled from physical updates on proper subsystems. It requires neither detailed balance nor primitivity. It does not establish the same statement for arbitrary linear summands that fail to generate completely positive semigroups.

The exact sampler of [Chen, Kastoryano, and Gilyén](https://arxiv.org/html/2311.09207v2) uses filtered Heisenberg-evolved seed operators and a coherent correction to enforce exact detailed balance. Its seed collection is closed under adjoints; Eqs. (5)–(12) describe the generator, and Eq. (23) describes its spatially decaying decomposition. For Hermitian local seeds, the construction can be applied seed by seed; for non-Hermitian seeds, an adjoint-closed pair can be grouped. Each such group is itself a GKSL generator with exact Gibbs stationarity. This grouping follows by applying their construction to that group alone. It does not assert stationarity of an isolated frequency-resolved jump.

These generators are compatible with the obstruction because their exact terms have tails. For a generic Hamiltonian in the theorem's family, a nonzero exactly stationary physical term cannot be replaced by any generator on a proper subsystem while retaining exact stationarity. This establishes an exact support requirement. It supplies no lower bound on the magnitude of the tails, no lower bound on the error of an approximate truncation, and no mixing-time obstruction.

For comparison, [Kastoryano and Brandão](https://arxiv.org/abs/1409.3435) develop local Gibbs samplers and their mixing properties for commuting interaction Hamiltonians. Such structured families are not covered merely by invoking genericity in the larger noncommuting coefficient space.

## The four-spin Ising statement in Johnson–Ticozzi–Viola

The [published article](https://www.rintonpress.com/xxqic16/qic-16-78/0657-0699.pdf), §5.4.2, p. 688, considers

```math
H=-\sum_{j=1}^{n-1}Z_jZ_{j+1}-g\sum_{j=1}^{n}X_j,
\qquad n\geq4,\quad g>0,
```

and finite-temperature Gibbs states defined by its Eq. (43). It reports numerical FFQLS for four spins with three-body neighborhoods. The section does not specify numerical values of $`g`$ or $`\beta`$. Its definitions resolve the relevant interpretation: neighborhoods are arbitrary subsets (§2.3); Definition 2 uses neighborhood generators; Definitions 4–5 require neighborhood-wise invariance and global stabilization. These are exact conditions, with no restriction to contiguous neighborhoods.

The [four-spin Ising calculation](../science/examples.md#four-spin-ising-chain) proves a stronger parameter statement directly. For

```math
H=-J(Z_1Z_2+Z_2Z_3+Z_3Z_4)-g(X_1+X_2+X_3+X_4),
\qquad Jg\ne0,
```

the local commutant is scalar on **every proper support**, including disconnected three-site subsets. The conclusion holds for every finite $`\beta\ne0`$. The proof uses exact Pauli commutators; it does not depend on a numerical rank tolerance, a thermal matrix exponential, or a special choice such as $`g=1`$.

Consequently, every exactly Gibbs-preserving neighborhood generator on at most three spins must vanish. Their sum cannot globally stabilize the Gibbs state. This contradicts the four-spin Gibbs FFQLS statement under the article's own exact definitions. The conclusion is independent of which three-body neighborhoods were used and of the unspecified positive field and temperature. It concerns that particular numerical statement, not the general fixed-space or stabilization theorems. The calculation does not reproduce the original numerical implementation or identify the cause of the discrepancy. It also makes no claim about the separately discussed states obtained after a quench.

## Local thermalization under microscopic constraints

[Tupkary, Dhar, Kulkarni, and Purkayastha](https://arxiv.org/html/2301.02146v2) study a finite system weakly coupled to a thermal bath on a subsystem. Their Theorem 2 shows that complete positivity together with local conservation laws forces the dissipative and Lamb-shift terms onto the bath-coupled subsystem. Their thermalization condition, Eq. (36), takes the long-time limit followed by the weak-coupling limit. Accordingly, Eq. (37) constrains the energy-diagonal part of $`\mathcal L_2(\rho_\beta)`$:

```math
\langle E_i|\mathcal L_2(\rho_\beta)|E_i\rangle=0.
```

It does not require the entire operator $`\mathcal L_2(\rho_\beta)`$ to vanish. Their semidefinite program and few-spin XXZ examples address feasibility under that weaker, perturbative thermalization condition. The present theorem assumes full exact stationarity and imposes no microscopic bath or local-current accuracy condition; it therefore addresses a different question. In particular, feasibility with a two-spin bath contact in their examples does not contradict exact local rigidity.

[Sarma, Kulkarni, Purkayastha, and Tupkary](https://arxiv.org/html/2602.01794v2) extend this approach to matching populations and coherences at the relevant orders in the system–bath coupling. Their Eq. (38) compares a candidate Lindblad correction with the Redfield correction acting on the leading steady state. This requires matching a generally nonzero operator, rather than annihilating the bare Gibbs state term by term. Their semidefinite analysis of few-spin XXZ systems concerns compatibility of complete positivity, microscopic accuracy, and conservation laws. It supplies neither the all-proper-subsystems Hamiltonian statement nor an exact frustration-free Gibbs-preservation theorem. Conversely, the obstruction here does not settle those perturbative master-equation questions.

## Other compatible constructions

[Guo, Hart, Chen, Friedman, and Lucas](https://quantum-journal.org/papers/q-2025-01-28-1612/) give an inverse-design framework for prescribed stationary mixed states. Their explicit local Gibbs constructions focus on stabilizer Hamiltonians. The absence of proper-support conserved operators is a hypothesis to be proved in a specified Hamiltonian family; it cannot be presumed for these structured targets.

[Arad, Firanko, and Gurevich](https://arxiv.org/abs/2408.08672) start with local channels and study the effective Hamiltonian $`-\log\rho`$ of their joint stationary state perturbatively. That Hamiltonian has interactions of increasing range. Their stationary-state condition concerns the combined dynamics and does not require each local component to preserve the state. Thus the construction changes both the target-Hamiltonian class and the individual-update condition relevant here.

## Priority and mathematical limits

Among the primary works compared above, the exact state-level criterion is already explicit, while the graph-local Hamiltonian construction, its simultaneous algebraic genericity, and the resulting all-temperature proper-support obstruction are additional results developed here. This comparison supports that precise contribution; it is not a claim of an exhaustive priority search across every equivalent formulation.

“Generic” refers to the full finite-dimensional coefficient space specified in the [theorem](../science/hamiltonian-rigidity.md#1-hamiltonian-family-and-quantifiers). A symmetry-restricted or translation-invariant subfamily needs a separate argument. The result concerns exact individual preservation at finite $`\beta\ne0`$. It does not exclude approximate local updates, local terms whose disturbances cancel in the total generator, quasi-local dynamics, or protocols whose intermediate steps move away from equilibrium. It also does not assert a uniform estimate in system size or an obstruction to thermalization in general.
