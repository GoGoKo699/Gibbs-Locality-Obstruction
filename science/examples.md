# Explicit models and the boundary of the obstruction

The [generic graph theorem](hamiltonian-rigidity.md) concerns the full coefficient space. The examples here show an exactly solvable rigid family, a four-spin result relevant to an earlier stabilization claim, and several reasons a symmetry-restricted family can be exceptional.

## Open Ising chain

Consider an open transverse-field Ising chain,

```math
H=-\sum_{j=1}^{n-1}J_j Z_jZ_{j+1}
-\sum_{j=1}^n g_j X_j,
\qquad J_j\neq0,\quad g_j\neq0.
```

**Proposition.** Every observable supported on a nonempty proper contiguous interval and commuting with $`H`$ is scalar. Its Gibbs state therefore admits no nonidentity exactly preserving channel on any such interval, at every finite $`\beta\neq0`$.

**Proof.** Let $`A=[a,b]`$, and let $`e`$ be an endpoint adjacent to a site outside $`A`$. The coefficient of the exterior $`Z`$ operator in
$`[Q_A\otimes I,H]=0`$ gives $`[Q_A,Z_e]=0`$. The exterior identity coefficient gives $`[Q_A,H_A]=0`$, where $`H_A`$ contains the terms wholly inside the interval.

By the Jacobi identity, $`Q_A`$ commutes with $`[Z_e,H_A]`$, which is a nonzero multiple of $`Y_e`$. It therefore commutes with the full Pauli algebra at $`e`$, so

```math
Q_A=I_e\otimes Q_{A\setminus\{e\}}.
```

Substituting back into $`[Q_A,H_A]=0`$, the independent identity and $`Z_e`$ coefficients give commutation with the smaller interval Hamiltonian and its new boundary $`Z`$. Repeating removes one endpoint after another. Only a scalar remains. The Gibbs conclusion follows from the [channel criterion](channel-criterion.md). $`\square`$

Uniform nonzero $`J_j=J`$ and $`g_j=g`$ are included. Consequently the polynomial argument also establishes generic proper-interval rigidity within the full translation-invariant nearest-neighbor qubit family. It does not establish all-subset rigidity within that restricted family.

## Four-spin Ising chain

For the homogeneous open chain with $`n=4`$ and $`Jg\neq0`$, the stronger statement holds on **every proper subset**. It is enough to prove scalar commutants on the four three-site subsets, since every smaller support embeds in one of them.

The endpoint triples $`\{1,2,3\}`$ and $`\{2,3,4\}`$ are covered above. Consider $`A=\{1,3,4\}`$; the other disconnected triple follows by reflection. Removing an irrelevant overall sign, write

```math
H_A=g(X_1+X_3+X_4)+JZ_3Z_4.
```

The coefficient of the exterior $`Z_2`$ gives commutation with
$`S_z=Z_1+Z_3`$, while the exterior identity gives commutation with $`H_A`$. Let $`S_x=X_1+X_3`$ and $`S_y=Y_1+Y_3`$. For $`Jg\neq0`$, successive commutators isolate the following operators, up to nonzero scalar multiples:

```math
\begin{aligned}
[S_z,H_A]&\propto S_y,\\
[S_z,S_y]&\propto S_x,\\
[S_x,H_A]&\propto Y_3Z_4,\\
[S_z,Y_3Z_4]&\propto X_3Z_4,\\
[X_3Z_4,Y_3Z_4]&\propto Z_3.
\end{aligned}
```

Any $`Q_A`$ commuting with the initial pair commutes with this entire list. Combining $`Z_3`$ with $`S_x,S_y`$ gives $`X_3,Y_3`$; subtracting these from $`S_x,S_y`$ gives $`X_1,Y_1`$, and hence $`Z_1`$. Therefore

```math
Q_A=I_1\otimes I_3\otimes Q_4.
```

Now $`[Q_A,H_A]=0`$, separated into its identity and $`Z_3`$ coefficients, forces both $`[Q_4,X_4]=0`$ and $`[Q_4,Z_4]=0`$. Thus $`Q_4`$, and hence $`Q_A`$, is scalar. $`\square`$

This proof covers every nonzero homogeneous field and coupling, not only one numerical point. It implies that no exact frustration-free stabilization by physical three-body generators is possible for this four-spin Gibbs state at finite $`\beta\neq0`$. The precise comparison with Johnson–Ticozzi–Viola is given in [Related work](../references/related-work.md).

The [exact verification suite](../verification/README.md) independently checks the commutator ranks at $`J=g=1`$; these finite ranks illustrate the analytical result rather than establish its parameter-uniform form.

## Reflection symmetry on an odd chain

The interval result cannot be upgraded to every disconnected support for all uniform chains. On a homogeneous five-spin open chain, spatial reflection is

```math
R=\mathrm{SWAP}_{1,5}\mathrm{SWAP}_{2,4}\otimes I_3.
```

It permutes the fields and bonds, so $`[R,H]=0`$. It is non-scalar and is supported on the proper subset $`\{1,2,4,5\}`$. Consequently the nonidentity channel
$`X\mapsto RXR^\dagger`$ preserves the Gibbs state at every temperature.

The Hamiltonian has noncommuting terms, yet fails all-subset rigidity because of this spatial symmetry. Reflection-symmetric coefficients lie in a lower-dimensional restricted family, consistent with the full-space generic theorem.

## Why distinct boundary weights matter

For a star centered at $`0`$, equal edge weights in

```math
H=\sum_{j=1}^{m}w(X_0X_j+Z_0Z_j)
```

make a swap of any two leaves a conserved proper-support observable. Distinct squared edge weights remove this permutation symmetry in the [graph witness](hamiltonian-rigidity.md): the Vandermonde system separates the individual leaf Pauli operators.

The distinct-weight condition is a sufficient condition for this witness. It is not asserted to characterize every rigid Hamiltonian.

## Classical commuting heatbath updates

For a diagonal Ising Hamiltonian and an interior spin $`i`$, write the neighboring spin values as $`\ell,r\in\{-1,+1\}`$. Its classical Gibbs conditional probability is

```math
p(s\mid\ell,r)=
\frac{\exp\{\beta s(J_{i-1}\ell+J_i r+h_i)\}}
{2\cosh\{\beta(J_{i-1}\ell+J_i r+h_i)\}}.
```

A three-site CPTP channel can retain the neighbor values and resample the center according to this conditional distribution. With $`P_\ell=|\ell\rangle\langle\ell|`$ and $`P_r=|r\rangle\langle r|`$, use the Kraus operators

```math
K_{\ell,r;s,t}=
\sqrt{p(s\mid\ell,r)}
\,P_\ell\otimes |s\rangle\langle t|\otimes P_r.
```

Summing $`K^\dagger K`$ over $`\ell,r,s,t`$ gives the identity, because the conditional probabilities sum to one. The Gibbs state is diagonal, and its conditional distribution of the center given all other spins depends only on these neighbors. Resampling that conditional therefore leaves the global Gibbs state unchanged.

For a chain of at least four sites this is a proper-support, nonidentity preserving update. Each $`Z_i`$ also commutes with the Hamiltonian. Thus both the channel construction and the conserved-observable criterion identify this as an exceptional family.

## Disconnected graphs and infinite temperature

If the interaction graph has several components, the Gibbs state factors across them. Resetting one component to its own Gibbs state preserves the full state and acts on a proper subset. Connectedness is therefore essential for the stated generic theorem.

At $`\beta=0`$, every Hamiltonian gives $`I/2^n`$, and any unital local channel preserves it. The finite nonzero inverse-temperature condition is essential. At zero temperature, the limiting state need not be faithful, and taking its logarithm no longer recovers the Hamiltonian on the whole Hilbert space.

These examples also explain why a claim based only on “noncommuting Hamiltonian” would be too broad. The exact criterion is the local commutant, with genericity established in a specified coefficient family.

[Question and model](model.md) · [Local updates](local-updates.md) · [Repository overview](../README.md)

