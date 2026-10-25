# From Watrous to exact Gibbs locality

[Repository overview](../README.md) · [Milestones](MILESTONES.md) · [Model](../science/model.md)

This bridge connects finite-dimensional quantum information to the question at the center of this project: when can an operation on part of a system preserve the **entire** Gibbs state? The route is through channels, fixed operators, and commutants. The textbook supplies the operator and channel language; the faithful-state criterion comes from primary research; the graph construction and genericity proof are developed in this repository.

## Source and reading route

The anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press (2018)**. The [author's book page](https://jhwatrous.github.io/books-and-courses.html) confirms publication in April 2018 and provides a manuscript and individual chapters. The locations below refer to the author-hosted standard-layout chapters. They are source links; the book is not redistributed here.

| Reading location | Tool needed for this project | First use below |
|---|---|---|
| [Chapter 1](https://jhwatrous.github.io/TQI.1.pdf), §§1.1.2–1.1.3: linear operators, decompositions, and norms | Positive operators, tensor products, operator bases, spectral calculus | [Notation](#notation), then [Gibbs states](#gibbs-states-and-commutants) |
| [Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), §§2.1.2–2.1.3: states and reductions | Density operators and the partial trace | [Local preservation](#local-preservation) |
| [Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), §§2.2.1–2.2.2: channels and their representations | Complete positivity, trace preservation, Kraus form; Corollary 2.27 | [Local preservation](#local-preservation), then [physical generators](#physical-generators) |
| [Chapter 4](https://jhwatrous.github.io/TQI.4.pdf), §4.1.1, Definition 4.4 and Example 4.5 | Pinching by projectors of arbitrary rank | [Preserving pinchings](#fixed-points-and-the-missing-implication) |
| [Chapter 4](https://jhwatrous.github.io/TQI.4.pdf), §4.2.2, “Fixed-points, spectra, and norms of unital channels” | Theorem 4.25: fixed operators of a unital channel commute with its Kraus operators | [Fixed points and the missing implication](#fixed-points-and-the-missing-implication) |

Chapter 1's spectral theorem is Theorem 1.3. In Chapter 2, Theorem 2.22 characterizes complete positivity, while Corollary 2.27 includes trace preservation and therefore characterizes channels. Keeping these two requirements separate is essential: a linear map that annihilates a Gibbs-state residual need not describe a physical operation.

The route does not require a complete reading of the book. The additional ingredients identified below have their own proofs and attribution on the canonical science pages.

## Notation

The book and this project use different symbols for several identical objects. In the table, $\mathcal X$ is a finite-dimensional space, $A$ is a set of sites, and $B=A^c$ is its complement.

| Watrous notation | Project notation | Meaning |
|---|---|---|
| $\mathcal X$ | $\mathcal H_A$ | Space of state vectors |
| $\mathrm L(\mathcal X)$ | $\mathcal B(\mathcal H_A)$ | All linear operators on that space |
| $\mathrm{Herm}(\mathcal X)$ | Hermitian operators on $A$ | Real vector space containing observables |
| $\mathrm D(\mathcal X)$ | Density operators $\rho_A$ | Positive semidefinite operators of trace one |
| $M^*$ | $M^\dagger$ | Adjoint of an operator |
| $1_{\mathcal X}$ | $I_A$ | Identity **operator** |
| $1_{\mathrm L(\mathcal X)}$ | $\mathrm{id}_A$ | Identity **map on operators** |
| $\Phi\in\mathrm C(\mathcal X)$ | CPTP map $\mathcal E_A$ | Channel with the same input and output space |

The distinction between the two identities prevents a common support error. A supported observable is $Q_A\otimes I_B$, whereas a supported channel is $\mathcal E_A\otimes\mathrm{id}_B$. The latter acts on a global density operator; it is not obtained by multiplying that density operator by $I_B$ on just one side.

“Faithful” means positive definite, $\rho>0$. Such a state has an inverse and a matrix logarithm on the whole space. A finite-dimensional Gibbs state at finite inverse temperature is faithful even when the Hamiltonian has degenerate energies.

## Local preservation

Suppose an operation changes only subsystem $A$. Two possible requirements are

$$
\mathcal E_A(\rho_A)=\rho_A,
\qquad
(\mathcal E_A\otimes\mathrm{id}_B)(\rho_{AB})=\rho_{AB}.
$$

The second implies the first by taking the partial trace over $B$. The first does not imply the second: it contains no condition on correlations.

### A faithful two-qubit example

Let

$$
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2},
\qquad
\rho_p=(1-p)\frac{I_4}{4}+p|\Phi^+\rangle\langle\Phi^+|,
\qquad 0<p<1.
$$

Its eigenvalues are $(1+3p)/4$ and $(1-p)/4$ with multiplicity three, so it is faithful. Both one-qubit marginals are $I_2/2$. Dephase the first qubit in the $Z$ basis:

$$
\mathcal D_Z(T)=\frac{T+ZTZ}{2}.
$$

The operators $I/\sqrt2$ and $Z/\sqrt2$ are Kraus operators and their squared sum is $I$, so this is CPTP. It leaves the first marginal unchanged. To see its effect on the joint state, write

$$
\rho_p=\frac14\bigl(I\otimes I+pX\otimes X-pY\otimes Y+pZ\otimes Z\bigr).
$$

Since $\mathcal D_Z(X)=\mathcal D_Z(Y)=0$ and $\mathcal D_Z(Z)=Z$,

$$
(\mathcal D_Z\otimes\mathrm{id})(\rho_p)
=\frac14\bigl(I\otimes I+pZ\otimes Z\bigr)\ne\rho_p.
$$

The removed off-diagonal block has eigenvalues $p/2$ and $-p/2$, so the trace norm of the disturbance is exactly $p$. Every local measurement statistic on either individual qubit remains the same, while joint correlations change.

The example also anticipates the project's criterion. If $Q_A\otimes I$ commutes with $\rho_p$, the linearly independent $X,Y,Z$ coefficients on the second qubit force $Q_A$ to commute with all three Pauli operators. Hence $Q_A$ is scalar. The faithful-state theorem below then rules out **every** nonidentity preserving channel on that qubit, not just the dephasing channel tested here.

### Why an operator basis is useful

Expand a general bipartite state as

$$
\rho_{AB}=\sum_\mu R_\mu\otimes F_\mu,
$$

where the $F_\mu$ are linearly independent operators on $B$. Global preservation is equivalent to

$$
\mathcal E_A(R_\mu)=R_\mu\quad\text{for every }\mu.
$$

A local preserver must therefore fix an entire collection of coefficient operators. Those coefficients need not be density operators. This is why the proof needs the fixed **linear space** of a channel, rather than just a list of its stationary density matrices.

## Fixed points and the missing implication

[Watrous, §4.2.2, Theorem 4.25](https://jhwatrous.github.io/TQI.4.pdf), gives a useful model case. If a channel is unital and

$$
\Phi(T)=\sum_\mu K_\mu T K_\mu^\dagger,
$$

then $\Phi(T)=T$ exactly when $T$ commutes with every $K_\mu$. Thus its fixed operators form an algebra. Both complete positivity and trace preservation are part of “channel”; unitality is the additional condition $\Phi(I)=I$.

The Gibbs question allows channels that are not unital. For example, choose a faithful state $\tau\ne I/d$ and define

$$
\mathcal R_\tau(T)=\mathrm{Tr}(T)\tau.
$$

This is a channel with $\mathcal R_\tau(\tau)=\tau$, but $\mathcal R_\tau(I)=d\tau\ne I$. Its fixed linear space is $\mathrm{span}\{\tau\}$, which is not an algebra under ordinary multiplication for a faithful nonuniform $\tau$. The unital theorem cannot simply be applied unchanged.

### The research input

The needed extension is the faithful fixed-space structure explained in [the channel-criterion proof](../science/channel-criterion.md#fixed-space-structure-used-in-the-proof), with its primary sources. A channel having a faithful fixed state admits a decomposition

$$
\mathcal H_A=\bigoplus_j(\mathcal H_{L_j}\otimes\mathcal H_{R_j}),
\qquad
\mathrm{Fix}(\mathcal E_A)
=\bigoplus_j\bigl[\mathcal B(\mathcal H_{L_j})\otimes\tau_{R_j}\bigr],
$$

where each $\tau_{R_j}>0$ is fixed. The $R_j$ factor stores a prescribed state, while arbitrary operators survive on $L_j$. The channel-criterion page attributes this structure to the established fixed-point literature, including [Johnson–Ticozzi–Viola](https://www.rintonpress.com/xxqic16/qic-16-78/0657-0699.pdf).

Apply this structure to the coefficients $R_\mu$ of a globally preserved state. There are three possibilities:

- Several direct-sum blocks give a nonscalar block projector commuting with the state.
- One block with $\dim\mathcal H_R>1$ gives a nonscalar operator commuting with $\tau_R$, and therefore with the state. If $\tau_R$ is scalar, any proper projector works.
- One block with $\dim\mathcal H_R=1$ means the whole operator space is fixed, so the channel is the identity.

Conversely, a nonscalar Hermitian $Q_A$ commuting with $\rho_{AB}$ yields a preserving pinching: if $Q_A=\sum_jq_jP_j$, then

$$
\mathcal P_A(T)=\sum_jP_jTP_j
$$

is CPTP, is nonidentity, and preserves the global state. This produces the equivalence

$$
\begin{aligned}
&\text{a nonidentity local preserving channel exists}\\
&\qquad\Longleftrightarrow
\text{a nonscalar local commuting observable exists}.
\end{aligned}
$$

The exact state-level equivalence is **Lie and Ng's Theorem 3**, [primary article](https://doi.org/10.1103/PhysRevA.108.012417), [author preprint](https://arxiv.org/html/2303.02376v1). It is an inherited research result, not a theorem attributed to Watrous and not the novel claim of this project. The repository supplies its faithful specialization in full.

## Gibbs states and commutants

For a Hamiltonian $H=H^\dagger$, define

$$
\rho_\beta=\frac{e^{-\beta H}}{Z_\beta},
\qquad Z_\beta=\mathrm{Tr}(e^{-\beta H}),
\qquad 0<|\beta|<\infty.
$$

Spectral calculus turns the state-preservation problem into a Hamiltonian problem. If $Q_A\otimes I_B$ commutes with $H$, it commutes with $e^{-\beta H}$ and hence with $\rho_\beta$. Conversely, commuting with the positive definite $\rho_\beta$ implies commuting with its logarithm, and

$$
\log\rho_\beta=-\beta H-\log Z_\beta\,I.
$$

Because $\beta\ne0$, this implies commutation with $H$. Thus the two local commutants coincide:

$$
\mathfrak C_A(\rho_\beta)=\mathfrak C_A(H),
\qquad
\mathfrak C_A(H)=
\{Q_A:[Q_A\otimes I_B,H]=0\}.
$$

Energy degeneracies do not invalidate this step. On distinct real energies, $E\mapsto e^{-\beta E}$ is injective for real $\beta\ne0$, so taking the exponential neither merges nor splits energy eigenspaces. No nondegeneracy assumption is needed.

The logical chain is now explicit: a scalar local commutant of $H$ gives a scalar local commutant of $\rho_\beta$; Lie–Ng then forces every preserving local channel to be the identity. This step works for all finite $\beta\ne0$ for the **same** Hamiltonian. Its detailed proof is [Corollary 2](../science/channel-criterion.md#3-gibbs-preservation-is-a-hamiltonian-condition).

What remains concerns the interaction graph: prove that a Hamiltonian with only allowed local interactions can have scalar local commutants on every proper subsystem. The textbook's channel results alone do not establish that fact.

## Boundary constraints and genericity

The [graph proof](../science/hamiltonian-rigidity.md) chooses

$$
H_* =\sum_{\{i,j\}\in E}w_{ij}(X_iX_j+Z_iZ_j),
$$

with nonzero weights whose squares are distinct on edges meeting at a vertex. These are interactions allowed by the model on any finite connected graph.

Fix a proper region $A$ and an exterior vertex $b$. Comparing coefficients of the exterior operators $X_b$ and $Z_b$ in $[Q_A\otimes I,H_*]=0$ gives commutation with

$$
S_x=\sum_{i\in N(b)\cap A}w_{ib}X_i,
\qquad
S_z=\sum_{i\in N(b)\cap A}w_{ib}Z_i.
$$

This is the same coefficient-comparison principle used in the two-qubit example. The new issue is separating several interior neighbors that appear in one weighted sum.

### A two-neighbor calculation

Suppose the two weights are $1$ and $2$. Then

$$
S_x=X_1+2X_2,
\qquad
T=\frac14[S_z,[S_z,S_x]]=X_1+8X_2.
$$

An operator commuting with $S_x,S_z$ also commutes with $T$. Solving these two linear equations gives

$$
X_1=\frac{4S_x-T}{3},
\qquad
X_2=\frac{T-S_x}{6}.
$$

Commutators with $S_z$ then isolate $Y_1,Y_2$, and further Pauli commutators give $Z_1,Z_2$. Commutation with the complete one-site matrix algebra forces $Q_A$ to act as identity on those sites.

With $d$ neighbors, the same calculation uses

$$
4^{-k}\mathrm{ad}_{S_z}^{2k}(S_x)
=\sum_{i=1}^{d}w_i^{2k+1}X_i,
\qquad k=0,\ldots,d-1.
$$

The coefficient matrix is a Vandermonde matrix in the distinct numbers $w_i^2$, times nonzero column factors $w_i$. It is invertible. After removing boundary sites from the possible support of $Q_A$, repeat on the smaller region. Connectedness guarantees another boundary until only a scalar remains. This argument includes disconnected regions and regions containing all but one site.

### Why one construction proves a generic statement

For the full allowed Hamiltonian family $H(\theta)$, represent the real linear map

$$
K_A(\theta):Q_A\longmapsto i[H(\theta),Q_A\otimes I]
$$

on traceless Hermitian operators in fixed Pauli bases. Its entries are linear in the Hamiltonian coefficients. The local commutant is scalar exactly when this map is injective, equivalently when

$$
p_A(\theta)=\det\bigl(K_A(\theta)^{\mathsf T}K_A(\theta)\bigr)>0.
$$

The explicit $H_*$ makes this polynomial nonzero for every proper $A$. At fixed graph size there are finitely many such subsets, so their product is a nonzero polynomial. Its zero set has measure zero and empty interior; the complement is open. This proves the advertised open, dense, full-measure conclusion in the specified coefficient space.

Boundary propagation, Vandermonde separation, and this polynomial argument are project-supplied material. They are not presented as results of Watrous's book. The full derivation, including the parameter space and every quantifier, is [Theorem 3](../science/hamiltonian-rigidity.md#1-hamiltonian-family-and-quantifiers).

## Physical generators

The [model page](../science/model.md#supported-operators-channels-and-generators) supplies the continuous-time framework. A GKSL generator $\ell_A$ generates CPTP maps $e^{t\ell_A}$ for every $t\geq0$. This semigroup input is additional to the selected textbook sections.

Suppose a generator supported on a proper region preserves the global Gibbs state individually:

$$
(\ell_A\otimes\mathrm{id}_B)(\rho_\beta)=0.
$$

The exponential series, or the constant solution of the evolution equation, gives

$$
(e^{t\ell_A}\otimes\mathrm{id}_B)(\rho_\beta)=\rho_\beta
\quad\text{for every }t\geq0.
$$

For a Hamiltonian satisfying the graph theorem, channel rigidity makes $e^{t\ell_A}=\mathrm{id}_A$ at every time. Differentiating at $t=0$ gives $\ell_A=0$. Identity at one isolated time would not suffice: a nonzero Hamiltonian generator can have periodic evolution.

For a frustration-free sum of physical generators, apply this reasoning to each term. The result requires every summand to be GKSL and to preserve the Gibbs state itself. Global stationarity alone allows cancellation: if $H=\sum_X h_X$, then $\sum_X-i[h_X,\rho_\beta]=0$ even when the separate commutators are nonzero.

Full support is sufficient as an existence statement. The global replacement channel $\mathcal T_\beta(T)=\mathrm{Tr}(T)\rho_\beta$ fixes the target, and

$$
e^{t(\mathcal T_\beta-\mathrm{id})}
=e^{-t}\mathrm{id}+(1-e^{-t})\mathcal T_\beta
$$

relaxes to it. This uses access to the target state; it is not an efficient preparation algorithm. The [local-update page](../science/local-updates.md) supplies the Kraus and GKSL checks and explains the support bound.

## Scope checks

The proof is complete only when its assumptions and exceptions remain visible.

| Check | Consequence |
|---|---|
| Set $\beta=0$. | The state becomes maximally mixed; every unital local channel preserves it. The logarithm cannot recover $H$. |
| Take $\beta\to\infty$. | The limiting state can lose rank. The faithful-state argument cannot be transferred to the limit without a separate proof. |
| Impose a special symmetry or commuting interaction family. | The full coefficient-space genericity theorem may not apply. The [examples](../science/examples.md) include explicit proper-support preservers. |
| Preserve only a marginal, or only the sum of generator terms. | The premise of individual global preservation has been weakened; the obstruction does not follow. |
| Allow small errors or spatially decaying nonzero tails. | Exact rigidity gives no uniform disturbance floor or lower bound on tail magnitude. Such updates can remain useful. |

The final result is therefore an exact support theorem for individually equilibrium-preserving physical operations. The [milestones](MILESTONES.md) organize the derivations, examples, and checks into a progression; the [science pages](../science/model.md) remain the authoritative statements and proofs.
