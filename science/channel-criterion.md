# Local channels, fixed states, and the Hamiltonian commutant

[Repository overview](../README.md) · [Local Hamiltonian theorem](hamiltonian-rigidity.md)

An operation on one part of an interacting system must preserve its correlations with the rest if it is to leave the global equilibrium state unchanged. This page gives the exact algebraic criterion for that requirement. It then expresses the criterion directly in terms of the Hamiltonian, so that the temperature dependence of the Gibbs state does not need to be analyzed separately.

The state-level equivalence is an established result of [Lie and Ng, Theorem 3](https://arxiv.org/html/2303.02376v1). They call a state **totally quantum on a subsystem** when no nontrivial projective measurement on that subsystem preserves the global state, and prove that this is equivalent to sensitivity to every nonidentity local channel. The derivation below specializes that result to faithful states and makes its fixed-space mechanism explicit. The [Hamiltonian theorem](hamiltonian-rigidity.md) supplies the additional result for local interacting Hamiltonians.

## 1. Local preservation and local rigidity

Let the finite-dimensional Hilbert space be

$$
\mathcal H=\mathcal H_A\otimes\mathcal H_B,
$$

and let $\rho_{AB}>0$ be a density operator. The inequality means that the state is positive definite, also called faithful. Its reduced state $\rho_A=\operatorname{Tr}_B\rho_{AB}$ is then positive definite as well.

A local channel is a completely positive, trace-preserving linear map $\mathcal E_A$ from operators on $\mathcal H_A$ to operators on the same space. Its action on the joint state is $\mathcal E_A\otimes\operatorname{id}_B$. The local-preservation condition is

$$
(\mathcal E_A\otimes\operatorname{id}_B)(\rho_{AB})=\rho_{AB}.
\tag{1}
$$

Preserving only the marginal $\rho_A$ is a weaker condition. Equation (1) also preserves every correlation between $A$ and $B$.

We say that $\rho_{AB}$ is **locally rigid on $A$** if

$$
(\mathcal E_A\otimes\operatorname{id}_B)(\rho_{AB})=\rho_{AB}
\quad\Longrightarrow\quad
\mathcal E_A=\operatorname{id}_A
\tag{2}
$$

for every local channel. This is the channel-sensitivity property studied by Lie and Ng. The word “rigid” here specifies the exact condition (2); it does not assert a quantitative lower bound on the disturbance caused by an approximately preserving operation.

The relevant local commutant is

$$
\mathfrak C_A(\rho)
=\left\{Q_A\in\mathcal B(\mathcal H_A):
[Q_A\otimes I_B,\rho_{AB}]=0\right\}.
\tag{3}
$$

It is a unital algebra closed under adjoints. If it contains a nonscalar operator, it also contains a nonscalar Hermitian operator: take the Hermitian and anti-Hermitian parts and note that they cannot both be scalar unless the original operator is scalar.

## 2. The established channel criterion

**Theorem 1 — Local channel criterion.** For a faithful state $\rho_{AB}$, the following statements are equivalent:

1. The state is locally rigid on $A$.
2. Every projective pinching channel on $A$ that preserves $\rho_{AB}$ is the identity.
3. The local commutant is scalar:

$$
\mathfrak C_A(\rho)=\mathbb C I_A.
\tag{4}
$$

A projective pinching channel has the form

$$
\mathcal P_A(X)=\sum_j P_jXP_j,
\qquad
P_jP_k=\delta_{jk}P_j,
\qquad
\sum_jP_j=I_A.
\tag{5}
$$

The projectors may have arbitrary ranks. A pinching is nontrivial when there are at least two nonzero projectors. This distinction matters: sensitivity to rank-one measurements alone would not state the full criterion.

The equivalence of the first two statements is [Lie and Ng’s Theorem 3](https://arxiv.org/html/2303.02376v1). Their theorem applies more generally than the faithful case used here. The proof below exhibits the finite-dimensional structure on which the faithful specialization rests.

### Fixed-space structure used in the proof

Suppose a channel $\mathcal E_A$ has a faithful fixed state. The standard structure theorem for its fixed operators gives an orthogonal decomposition

$$
\mathcal H_A
=\bigoplus_j\left(\mathcal H_{L_j}\otimes\mathcal H_{R_j}\right)
\tag{6}
$$

in which

$$
\operatorname{Fix}(\mathcal E_A)
=\bigoplus_j\left[
\mathcal B(\mathcal H_{L_j})\otimes\tau_{R_j}
\right].
\tag{7}
$$

Each $\tau_{R_j}>0$ is a fixed density operator. The same $\tau_{R_j}$ occurs for every operator in the corresponding block of the fixed space. The faithful fixed state excludes a transient subspace outside these blocks.

Equation (7) is an inherited structural result. It is stated in [Johnson, Ticozzi, and Viola, Theorem 1 and Eq. (14)](https://arxiv.org/pdf/1506.07756), and the channel-sensitivity application is developed by Lie and Ng. It describes the fixed **linear space**, including nonpositive fixed operators, which is why it can be applied to the coefficient operators of a correlated state.

### Proof of Theorem 1

First suppose that a nonscalar Hermitian $Q_A$ belongs to $\mathfrak C_A(\rho)$. Write its spectral decomposition as

$$
Q_A=\sum_jq_jP_j,
\tag{8}
$$

where the $q_j$ are distinct. Commutation with $Q_A\otimes I_B$ implies commutation with every spectral projector $P_j\otimes I_B$. Consequently,

$$
\rho_{AB}
=\sum_j(P_j\otimes I_B)\rho_{AB}(P_j\otimes I_B).
\tag{9}
$$

There are at least two nonzero projectors, so (9) gives a nonidentity local preserving channel. Thus local rigidity implies a scalar local commutant.

Conversely, suppose that a nonidentity channel $\mathcal E_A$ satisfies (1). Taking the partial trace shows that $\rho_A$ is a faithful fixed state of $\mathcal E_A$, so the decomposition (6)–(7) applies.

Expand $\rho_{AB}$ in any operator basis on $B$:

$$
\rho_{AB}=\sum_\mu X_\mu\otimes F_\mu.
\tag{10}
$$

Linear independence of the $F_\mu$ and (1) imply $\mathcal E_A(X_\mu)=X_\mu$ for every $\mu$. Every coefficient therefore lies in (7), and the joint state has the form

$$
\rho_{AB}
=\bigoplus_j\left(
\omega_{L_jB}\otimes\tau_{R_j}
\right),
\tag{11}
$$

with the tensor factors ordered in the indicated block. The positive operators $\omega_{L_jB}$ may be unnormalized; their traces contain the block probabilities.

If there is more than one block, a projector onto one block of (6) is a nonscalar local Hermitian operator commuting with (11). If there is exactly one block and $\dim\mathcal H_R>1$, choose a nonscalar Hermitian operator $Q_R$ commuting with $\tau_R$. Such an operator always exists, including when $\tau_R$ is proportional to the identity. Then $I_L\otimes Q_R$ is a nonscalar element of $\mathfrak C_A(\rho)$.

The remaining possibility is one block with $\dim\mathcal H_R=1$. In that case (7) equals the entire operator algebra on $A$. The channel fixes every operator and hence is the identity, contrary to the assumption. We have therefore shown that any nonidentity local preserving channel produces a nonscalar local commutant.

Finally, a preserving pinching (5) makes $\rho_{AB}$ block diagonal in the $P_j$, so every $P_j\otimes I_B$ commutes with it. A nontrivial pinching therefore yields a nonscalar element of (3). Together with (8)–(9), this proves all three equivalences. $\square$

## 3. Gibbs preservation is a Hamiltonian condition

Let $H=H^\dagger$ be a finite-dimensional Hamiltonian and let

$$
\rho_\beta(H)
=\frac{e^{-\beta H}}{Z_\beta(H)},
\qquad
Z_\beta(H)=\operatorname{Tr}e^{-\beta H},
\qquad
0<|\beta|<\infty.
\tag{12}
$$

Positive inverse temperatures are the main application. The finite-dimensional statements also hold for negative inverse temperatures. The state in (12) is faithful, whether or not the Hamiltonian has degenerate eigenvalues.

Define the local Hamiltonian commutant

$$
\mathfrak C_A(H)
=\left\{Q_A\in\mathcal B(\mathcal H_A):
[Q_A\otimes I_B,H]=0\right\}.
\tag{13}
$$

**Corollary 2 — Exact Gibbs criterion.** At every finite $\beta\neq0$,

$$
\rho_\beta(H)\text{ is locally rigid on }A
\quad\Longleftrightarrow\quad
\mathfrak C_A(H)=\mathbb C I_A.
\tag{14}
$$

**Proof.** Commutation with $H$ implies commutation with every function of $H$, including $\rho_\beta(H)$. In the other direction, faithfulness permits the matrix logarithm, and

$$
\log\rho_\beta(H)
=-\beta H-\log Z_\beta(H)\,I.
\tag{15}
$$

An operator commuting with $\rho_\beta(H)$ also commutes with its logarithm. Since $\beta\neq0$, (15) gives commutation with $H$. Thus

$$
\mathfrak C_A\bigl(\rho_\beta(H)\bigr)
=\mathfrak C_A(H),
\tag{16}
$$

and Theorem 1 proves (14). $\square$

The criterion is independent of temperature throughout the finite nonzero-temperature domain. Once $\mathfrak C_A(H)$ is scalar, the conclusion holds for every finite $\beta\neq0$ for that same Hamiltonian. There is no interchange of “almost every Hamiltonian” and “every temperature” in this step.

At $\beta=0$, the Gibbs state is maximally mixed. Every unital local channel preserves it, and local rigidity fails when $\dim\mathcal H_A>1$. The zero-temperature limit can produce a nonfaithful state; neither the logarithm argument nor the faithful-state proof above asserts that the limiting ground-state projector has the same rigidity property.

## 4. What is transferred to the many-body theorem

The channel criterion reduces exact local Gibbs preservation to a question about ordinary operators: does the Hamiltonian have a nonscalar conserved operator supported entirely inside $A$? The [next page](hamiltonian-rigidity.md) constructs edge-local Hamiltonians for which the answer is no for every proper subsystem, and then proves that this property holds generically in the full local-interaction parameter space.

The state-level sensitivity theorem, the fixed-space structure, and the functional-calculus step are explicitly attributed ingredients. The locality-constrained Hamiltonian construction and its simultaneous genericity statement are the additional mathematical content developed in this repository.

## Sources for this page

- S. H. Lie and N. H. Y. Ng, *Catalysis always degrades external quantum correlations*, Physical Review A **108**, 012417 (2023), [doi:10.1103/PhysRevA.108.012417](https://doi.org/10.1103/PhysRevA.108.012417), [arXiv:2303.02376](https://arxiv.org/abs/2303.02376). Theorem 3 proves the equivalence between total quantumness and sensitivity to all nonidentity local channels.
- P. D. Johnson, F. Ticozzi, and L. Viola, *General fixed points of quasi-local frustration-free quantum semigroups: from invariance to stabilization*, Quantum Information and Computation **16**, 657–699 (2016), [arXiv:1506.07756](https://arxiv.org/abs/1506.07756), [published full text](https://www.rintonpress.com/xxqic16/qic-16-78/0657-0699.pdf). Theorem 1 and Eq. (14) give the faithful fixed-space structure used above.
