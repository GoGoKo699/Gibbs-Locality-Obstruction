# Generic local Hamiltonians have rigid Gibbs states

[Repository overview](../README.md) · [Channel criterion and attribution](channel-criterion.md)

This page proves that exact local rigidity is generic among Hamiltonians with one-site and edge-supported two-site interactions on any finite connected graph of qubits. A bounded-coupling example establishes the result for every proper subsystem. A polynomial argument then gives an open, dense, full-measure set of Hamiltonians with the same property.

The [channel criterion](channel-criterion.md#3-gibbs-preservation-is-a-hamiltonian-condition) converts the operator statement into a conclusion about every completely positive, trace-preserving update. That criterion is inherited from Lie and Ng’s channel-sensitivity theorem. The proof here concerns the additional restrictions imposed by a local Hamiltonian.

## 1. Hamiltonian family and quantifiers

Let $G=(V,E)$ be a finite connected simple undirected graph, with $n=|V|\geq2$. Each vertex carries a qubit, so

$$
\mathcal H_V=\bigotimes_{i\in V}\mathbb C^2.
\qquad\text{(1)}
$$

Choose an ordering of the vertices. Write $\sigma^1=X$, $\sigma^2=Y$, and $\sigma^3=Z$. The real parameter space is

$$
\Theta_G=\mathbb R^{3n+9|E|},
\qquad\text{(2)}
$$

with Hamiltonians

$$
H(\theta)
=\sum_{i\in V}\sum_{a=1}^3 h_{i,a}\sigma_i^a
+\sum_{\substack{\{i,j\}\in E\\i<j}}
\sum_{a,b=1}^3J_{ij}^{ab}\sigma_i^a\sigma_j^b.
\qquad\text{(3)}
$$

The displayed Pauli strings form a linearly independent basis of the allowed interaction space. A scalar multiple of the identity is omitted because it affects neither Gibbs states nor commutants. The graph specifies which edge terms are allowed; individual coefficients in (3) may vanish.

For a nonempty proper subset $A\subsetneq V$, define

$$
\mathfrak C_A(H)
=\left\{Q_A\in\mathcal B(\mathcal H_A):
[Q_A\otimes I_{A^c},H]=0\right\}.
\qquad\text{(4)}
$$

The subset $A$ need not be connected. The statement below therefore covers every channel with proper tensor support, including channels acting on most of the system or on disconnected groups of sites.

**Theorem 3 — Generic rigidity for local interacting Hamiltonians.** There is a nonzero real polynomial $p_G$ on $\Theta_G$ such that, for every $\theta$ with $p_G(\theta)\neq0$,

$$
\mathfrak C_A\bigl(H(\theta)\bigr)=\mathbb C I_A
\qquad
\text{for every }\varnothing\neq A\subsetneq V.
\qquad\text{(5)}
$$

Consequently, for that same Hamiltonian, every finite $\beta\neq0$ and every proper nonempty $A$ obey

$$
(\mathcal E_A\otimes\mathrm{id}_{A^c})
\bigl(\rho_\beta(H(\theta))\bigr)
=\rho_\beta(H(\theta))
\quad\Longrightarrow\quad
\mathcal E_A=\mathrm{id}_A.
\qquad\text{(6)}
$$

The set of parameters satisfying (5) is open, dense, and of full Lebesgue measure. The exceptional set is a proper algebraic subset of $\Theta_G$.

The proof consists of the explicit construction in Sections 2–4 and the genericity argument in Section 5. Equation (6) then follows from [Corollary 2](channel-criterion.md#3-gibbs-preservation-is-a-hamiltonian-condition). The proof establishes all proper subsets and all finite nonzero inverse temperatures simultaneously; it does not select a different Hamiltonian for each temperature.

## 2. A bounded-coupling construction

Assign each edge a real weight $w_e$ satisfying

$$
w_e\neq0,
\qquad
w_e^2\neq w_f^2
\quad\text{whenever distinct edges }e,f\text{ meet at a vertex}.
\qquad\text{(7)}
$$

Consider

$$
H_*
=\sum_{\{i,j\}\in E}w_{ij}
\left(X_iX_j+Z_iZ_j\right).
\qquad\text{(8)}
$$

Condition (7) can be met with uniformly bounded rational couplings. For example, enumerate the $m=|E|$ edges and take

$$
w_{e_k}=1+\frac{k}{m+1},
\qquad k=1,\ldots,m.
\qquad\text{(9)}
$$

Every weight then lies strictly between $1$ and $2$, and all squared weights are distinct. The construction uses only two-body edge interactions from (3); it requires no additional sites or interactions beyond the specified graph.

We will prove

$$
\mathfrak C_A(H_*)=\mathbb C I_A
\qquad
\text{for every }\varnothing\neq A\subsetneq V.
\qquad\text{(10)}
$$

The mechanism is propagation of operator constraints from the boundary of $A$ into its interior. Two independent Pauli couplings allow boundary constraints to resolve individual sites, even when one exterior vertex has several neighbors inside $A$.

## 3. Resolving the boundary sites

Fix a nonempty proper $A$ and put $B=A^c$. Suppose

$$
[Q_A\otimes I_B,H_*]=0.
\qquad\text{(11)}
$$

For an exterior vertex $b\in B$, let $N_A(b)=N(b)\cap A$ and define operators on $A$ by

$$
S_x^{(b)}=\sum_{i\in N_A(b)}w_{ib}X_i,
\qquad
S_z^{(b)}=\sum_{i\in N_A(b)}w_{ib}Z_i.
\qquad\text{(12)}
$$

The crossing interactions of $H_*$ are exactly

$$
\sum_{b\in B}\left(
S_x^{(b)}\otimes X_b+S_z^{(b)}\otimes Z_b
\right),
\qquad\text{(13)}
$$

with identities on the remaining exterior sites. Terms supported entirely in $B$ commute with $Q_A\otimes I_B$ and make no contribution to (11). Terms supported entirely in $A$ have the exterior factor $I_B$. The operators

$$
I_B,\quad X_b,\quad Z_b\quad(b\in B)
\qquad\text{(14)}
$$

are linearly independent. Comparing their coefficients in (11) gives

$$
[Q_A,S_x^{(b)}]=[Q_A,S_z^{(b)}]=0
\qquad(b\in B).
\qquad\text{(15)}
$$

This comparison does not require $A$ or $B$ to be connected.

Now fix an exterior vertex with $d=|N_A(b)|>0$, abbreviate $S_x=S_x^{(b)}$, $S_z=S_z^{(b)}$, and write its crossing weights as $w_1,\ldots,w_d$. With $\mathrm{ad}_S(T)=[S,T]$, the Pauli relations and commutativity of operators on distinct sites imply

$$
\mathrm{ad}_{S_z}^{2k}(S_x)
=4^k\sum_{i=1}^{d}w_i^{2k+1}X_i,
\qquad k\geq0.
\qquad\text{(16)}
$$

For completeness, one double commutator gives

$$
[S_z,[S_z,S_x]]
=4\sum_{i=1}^dw_i^3X_i,
\qquad\text{(17)}
$$

because $[Z,[Z,X]]=4X$ and all cross-site commutators vanish. Repeating this step multiplies the coefficient at site $i$ by $4w_i^2$, proving (16).

An operator commuting with $S_x$ and $S_z$ also commutes with every nested commutator in (16), by the Jacobi identity. Use the first $d$ equations, with $k=0,\ldots,d-1$. Their coefficient matrix, after removing the nonzero row factors $4^k$, is

$$
V_{ki}=w_i(w_i^2)^k.
\qquad\text{(18)}
$$

Its determinant is, up to the chosen column ordering,

$$
\det V
=\left(\prod_{i=1}^dw_i\right)
\prod_{1\leq i<j\leq d}(w_j^2-w_i^2),
\qquad\text{(19)}
$$

which is nonzero by (7). Linear combinations of the nested commutators therefore isolate each $X_i$. Equation (15) implies

$$
[Q_A,X_i]=0
\qquad(i\in N_A(b)).
\qquad\text{(20)}
$$

For such a site,

$$
[X_i,S_z]=-2i w_iY_i.
\qquad\text{(21)}
$$

The coefficient is nonzero. Equations (15), (20), and the Jacobi identity give $[Q_A,Y_i]=0$. Commutation with $[X_i,Y_i]=2iZ_i$ then gives $[Q_A,Z_i]=0$ as well.

We have proved that $Q_A$ commutes with the full one-qubit operator algebra on every vertex of $A$ adjacent to $B$. Hence it acts as identity on those vertices. Explicitly, if

$$
\partial_B A=\{i\in A:N(i)\cap B\neq\varnothing\},
\qquad\text{(22)}
$$

then there is an operator $Q_{A\setminus\partial_B A}$ such that

$$
Q_A
=I_{\partial_B A}\otimes Q_{A\setminus\partial_B A},
\qquad\text{(23)}
$$

with the tensor factors placed in their original site order. Equation (23) follows directly from the commutant of a full one-site matrix algebra, applied to each boundary site.

## 4. Propagating the constraint through a connected graph

The boundary argument can be repeated without changing the Hamiltonian. Set $A_0=A$. Having shown that the original operator acts as identity outside a remaining set $A_s$, apply Section 3 with $A_s$ as the active region and $V\setminus A_s$ as its complement. It gives

$$
A_{s+1}
=A_s\setminus\partial_{V\setminus A_s}A_s
\qquad\text{(24)}
$$

and forces identity on the newly removed sites.

Whenever $A_s$ is nonempty, it is still a proper subset because the original $A$ was proper. Connectedness of $G$ guarantees an edge from $A_s$ to its complement, so at least one site is removed. After at most $|A|$ steps no active sites remain. The original $Q_A$ is therefore scalar.

This proves (10). In particular, it applies to a region containing $n-1$ sites: the initially omitted site supplies boundary constraints that propagate through the entire connected graph.

The argument works for arbitrary operators $Q_A$. Equivalently, it suffices to prove it for Hermitian operators because the local commutant is closed under taking Hermitian and anti-Hermitian parts.

## 5. From one construction to a generic theorem

The construction proves that the local commutants can be scalar within the restricted Hamiltonian family (3). The next step shows that failure of this property occupies a proper algebraic subset of that family.

Fix a nonempty proper $A$. Let $\mathrm{Herm}_0(\mathcal H_A)$ denote the real vector space of traceless Hermitian operators on $A$, of dimension $4^{|A|}-1$. Define the real linear map

$$
K_A(\theta):\mathrm{Herm}_0(\mathcal H_A)
\longrightarrow\mathrm{Herm}(\mathcal H_V),
\qquad
K_A(\theta)(Q_A)=i[H(\theta),Q_A\otimes I_{A^c}].
\qquad\text{(25)}
$$

Choose fixed orthonormal Hermitian Pauli bases in its domain and codomain. The matrix entries of $K_A(\theta)$ are real and linear in $\theta$. The local commutant is scalar exactly when $K_A(\theta)$ is injective: subtracting the trace removes the scalar part of any Hermitian commuting operator.

Define

$$
p_A(\theta)
=\det\left(K_A(\theta)^{\mathsf T}K_A(\theta)\right).
\qquad\text{(26)}
$$

This is a real polynomial, is nonnegative, and is positive precisely when $K_A(\theta)$ is injective. The particular parameters $\theta_*$ giving (8) satisfy $p_A(\theta_*)>0$ for every proper nonempty $A$, by Sections 3–4. Therefore none of these polynomials vanishes identically.

There are only finitely many proper subsets at fixed graph size. Set

$$
p_G(\theta)
=\prod_{\varnothing\neq A\subsetneq V}p_A(\theta).
\qquad\text{(27)}
$$

The same construction witnesses $p_G(\theta_*)>0$. Consequently $p_G$ is a nonzero polynomial, and

$$
p_G(\theta)\neq0
\quad\Longleftrightarrow\quad
\mathfrak C_A(H(\theta))=\mathbb C I_A
\text{ for every proper nonempty }A.
\qquad\text{(28)}
$$

The zero set of a nonzero real polynomial has Lebesgue measure zero and empty interior. It is closed, so its complement is open and dense. This proves the parameter-space claim in Theorem 3.

Finally, (28) is a property of $H$ alone. The [exact Gibbs criterion](channel-criterion.md#3-gibbs-preservation-is-a-hamiltonian-condition) transfers it to every finite $\beta\neq0$ and every local channel, proving (6). $\square$

## 6. Meaning and scope of the generic statement

**Bounded interactions.** The full-measure conclusion also holds inside any nonempty open bounded region of $\Theta_G$. A nonzero polynomial cannot vanish throughout such a region. The explicit construction (9) also uses bounded edge weights. Neither statement supplies a uniform quantitative estimate for approximate Gibbs preservation.

**Symmetry constraints.** Genericity is with respect to the coefficient space (2). A lower-dimensional family with imposed symmetries, commuting terms, or repeated coefficients may lie partly or wholly in the exceptional set. The theorem does not remove such constraints by describing them as atypical. A claim restricted to one of those families needs its own argument.

**Graph connectedness.** If the graph is disconnected, a nontrivial operation on one complete connected component can preserve a product Gibbs state of the components. Connectedness is therefore a substantive hypothesis of the full-support statement.

**Finite systems and exact preservation.** Theorem 3 concerns each fixed finite graph and equality of states. It is consistent with accurate finite-range approximations, quasilocal generators whose tails reach the whole graph, and constructions that preserve the Gibbs state only after several non-preserving operations are combined. The polynomial argument does not give a computationally efficient test for every subsystem of a large graph, and no such efficiency claim is required by the theorem.

**Temperature.** The same generic Hamiltonian works at every finite nonzero inverse temperature. At exactly $\beta=0$, the maximally mixed state has many nonidentity local preserving channels. The zero-temperature limit is outside the faithful Gibbs argument.

The result identifies the exact support required by an individual equilibrium-preserving operation. Its implications for frustration-free Gibbs generators follow by applying the channel statement to the semigroup generated by each term.

## Attribution and proof dependencies

The state-level channel-sensitivity equivalence is due to [Lie and Ng](https://doi.org/10.1103/PhysRevA.108.012417), with the faithful fixed-space derivation and its sources given on the [preceding page](channel-criterion.md). The graph construction (8), the boundary-resolution argument (12)–(24), and the simultaneous genericity result (25)–(28) are proved here. The genericity step uses only the elementary measure-zero property of the zero set of a nonzero real polynomial; numerical rank checks are not used in this proof.
