# Consequences for exact Gibbs-preserving dynamics

This page derives the dynamical consequences of the [generic graph theorem](hamiltonian-rigidity.md). The [model](model.md) fixes the support convention and requires every local update to be physical in its own right.

## From channels to Lindblad generators

Let $`H`$ have scalar local commutant on every proper subset, and fix a finite $`\beta\neq0`$. Suppose a proper-support GKSL generator satisfies

```math
\mathcal L_A(\rho_\beta)=0.
```

Its semigroup obeys

```math
e^{t\mathcal L_A}(\rho_\beta)=\rho_\beta
\qquad\text{for every }t\geq0.
```

Every $`e^{t\mathcal L_A}`$ is a CPTP channel supported on $`A`$. The channel theorem therefore makes every such map the identity. Differentiating at $`t=0`$ gives

```math
\mathcal L_A=0.
```

This uses preservation at all semigroup times. Identity of a channel at one isolated time alone would not force its generator to vanish.

**Corollary.** In a frustration-free decomposition into individually physical, individually Gibbs-preserving terms, every nonzero term has full support $`V`$. If every allowed support is proper, the entire generator is zero and cannot prepare a unique Gibbs steady state.

No detailed-balance assumption, convergence rate, dissipative gap, or uniqueness assumption is needed for the obstruction. The same conclusion holds for a family of discrete CPTP updates, each of which fixes the target state exactly: every proper-support update is the identity.

An operation implemented with independent ancillas, measurement, internal classical feedback, and discarding of local ancillas still defines a CPTP map on its chosen subsystem. Such an implementation is covered when its induced system channel has proper support.

## The spatial support bound is attainable

For any faithful target state $`\rho_\beta`$, the global replacement channel

```math
\mathcal T_\beta(X)=\mathrm{Tr}(X)\rho_\beta
```

is CPTP and fixes the target. If
$`\rho_\beta=\sum_i p_i|i\rangle\langle i|`$, a Kraus representation is

```math
K_{ij}=\sqrt{p_i}\,|i\rangle\langle j|,
\qquad
\sum_{i,j}K_{ij}^\dagger K_{ij}=I.
```

Since $`\mathcal T_\beta^2=\mathcal T_\beta`$, the generator

```math
\mathcal L_{\mathrm{reset}}=\mathcal T_\beta-\mathrm{id}
```

has the CPTP semigroup

```math
e^{t\mathcal L_{\mathrm{reset}}}
=e^{-t}\mathrm{id}+(1-e^{-t})\mathcal T_\beta.
```

Its unique stationary density matrix is $`\rho_\beta`$. The same Kraus operators give its GKSL form directly, because their squared sum is the identity.

For generic $`H`$, the minimum possible support of a nonidentity exactly Gibbs-preserving channel is therefore exactly $`n`$ sites. The same support is sufficient for an exact relaxing generator.

This construction is an existence witness for the spatial statement. Implementing it requires access to the target state, or to equivalent global preparation information. It supplies no efficient preparation algorithm, gate-count bound, or free state-loading assumption.

## Why stationarity of the sum is insufficient

For a local Hamiltonian $`H=\sum_X h_X`$, consider

```math
\mathcal L_X=-i[h_X,\,\cdot\,].
```

Each term is a local physical Hamiltonian generator. Their sum preserves the Gibbs state:

```math
\sum_X\mathcal L_X(\rho_\beta)
=-i[H,\rho_\beta]=0.
```

For a generic interacting Hamiltonian, the individual terms do not preserve it. Their nonzero disturbances cancel. This example has no relaxation to a unique equilibrium, but it shows why global stationarity cannot be substituted for termwise stationarity in the proof.

Likewise, the present theorem does not decide whether a genuinely dissipative local generator with such cancellations can have the exact Gibbs state as its unique stationary state. That is a different question.

## Strict support, decaying tails, and circuit locality

A term can be centered near one vertex and have small operator tails reaching distant vertices while still having full support. The theorem allows that behavior. The exact Gibbs constructions discussed in [Related work](../references/related-work.md) use quasi-local physical generators, and their nonzero tails are compatible with the full-support necessity.

Strict support of a system channel is also different from locality of its microscopic coupling to a bath. Evolution under an interacting system Hamiltonian can spread the action of a locally coupled bath. The resulting system channel need not be of the form $`\mathcal E_A\otimes\mathrm{id}_{A^c}`$.

Similarly, a circuit of local gates can implement a global channel. Requiring every gate to preserve the target separately is an additional condition, absent from a general preparation circuit.

## Exact rigidity can coexist with very accurate local updates

There is no temperature-independent disturbance floor in the theorem. Let $`\mathcal D_A`$ be a nonidentity unital local channel, for example dephasing one spin, and write $`D=2^n`$. At infinite temperature,

```math
(\mathcal D_A\otimes\mathrm{id})(I/D)=I/D.
```

For finite $`\beta`$, trace-norm contraction on Hermitian operators and the triangle inequality give

```math
\begin{aligned}
\|(\mathcal D_A\otimes\mathrm{id})(\rho_\beta)-\rho_\beta\|_1
&\leq
2\|\rho_\beta-I/D\|_1 .
\end{aligned}
```

For any fixed finite Hamiltonian, the right-hand side tends to zero as $`\beta\to0`$, even though the left-hand side is strictly positive at every nonzero $`\beta`$ when the rigidity theorem applies. Analyticity of the finite-dimensional Gibbs state makes this bound $`O(|\beta|)`$ for a fixed $`H`$; no size-uniform constant is asserted.

This explains the compatibility between an exact obstruction and accurate truncated or approximate updates. The proof gives neither a useful lower bound on tail strength nor an approximation-error versus range law.

## Physical interpretation

The decisive property is the absence of a non-scalar local observable commuting with the Hamiltonian. A local operation cannot preserve the full equilibrium state unless such a locally nondisturbing observable exists. The graph construction shows that generic two-body interactions remove this possibility on every proper subsystem.

No entanglement assumption enters the result. Nor is the result a statement about the cost of observing an arbitrarily small disturbance: detecting the difference can be ill-conditioned. The distinction is exact existence of a preserving physical map.

[Question and model](model.md) · [Examples](examples.md) · [Repository overview](../README.md)

