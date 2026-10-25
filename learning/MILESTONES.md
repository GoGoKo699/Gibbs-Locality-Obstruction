# Thirty milestones for Gibbs Locality Obstruction

[Repository overview](../README.md) · [Watrous bridge](WATROUS_BRIDGE.md) · [Scientific model](../science/model.md)

This map gives thirty project-defined understanding targets for any reader. The sole educational anchor is John Watrous, *The Theory of Quantum Information* (2018), available through the [author’s book page](https://jhwatrous.github.io/books-and-courses.html). The [bridge](WATROUS_BRIDGE.md) identifies the relevant sections, translates notation, and supplies the steps from channel theory to this project. Primary research sources provide attribution for inherited theorems; they do not form a second textbook route.

The allocation is **12 milestones for background and preliminaries, followed by 18 for the narrative and innovation**. The first phase builds from states and individual operations to the full equilibrium-preservation question. The second reconstructs the mechanism from one local preserving channel and one boundary interaction to the generic graph theorem, its dynamical consequence, and its limits. This allocation reflects the project’s combination of channel structure and an operator argument on a graph.

| Phase | Milestones | Integrating endpoint |
|---|---|---|
| Background and preliminaries | M01–M12 | State the complete physical model and identify the ingredients needed to analyze it. |
| Narrative and innovation | M13–M30 | Explain the theorem, proof mechanism, consequences, examples, attribution, and exact scope as one connected account. |

The map covers the project’s central understanding targets. Detailed algebra, source comparisons, and reproduction instructions remain in their canonical scientific pages.

## Background and preliminaries

### M01 — States, observables, and spectra

**Central question.** What information do a density operator and a Hermitian observable describe?

**Understanding target.** Relate positivity and unit trace to a quantum state, interpret an observable through its spectral projectors, and recognize that a faithful state has no zero eigenvalues.

**Dependencies and story role.** No earlier milestone is required. This establishes the individual operators used throughout the argument.

**Conceptual connection.** Faithfulness later permits a matrix logarithm; spectral projectors later turn conserved observables into preserving measurements.

**Sources.** Watrous §§1.1.2–1.1.3 and §2.1.2; [bridge notation](WATROUS_BRIDGE.md#notation); [local-preservation definitions](../science/channel-criterion.md#1-local-preservation-and-local-rigidity).

### M02 — A joint state contains more than its marginals

**Central question.** How can an operation preserve a subsystem’s state while changing the whole system?

**Understanding target.** Explain tensor-product registers, partial traces, and correlations, and distinguish equality of a reduced density operator from equality of the joint state.

**Dependencies and story role.** Depends on M01. It enlarges the setting from one register to a subsystem and its surroundings.

**Conceptual connection.** The obstruction requires preservation of the global Gibbs state, including correlations across the chosen boundary.

**Sources.** Watrous §§2.1.2–2.1.3; [bridge local preservation](WATROUS_BRIDGE.md#local-preservation); [scientific question](../science/model.md#why-gibbs-preserving-updates-are-a-locality-question).

### M03 — Physical channels and their representations

**Central question.** Which linear maps describe deterministic physical operations on a quantum state?

**Understanding target.** Explain complete positivity and trace preservation, and use a Kraus representation to identify a channel, including the completeness relation on its Kraus operators.

**Dependencies and story role.** Depends on M01–M02. It identifies the physical class of maps to which the result applies.

**Conceptual connection.** Complete positivity is essential when the operated register remains correlated with another register; a merely linear map need not be an allowed update.

**Sources.** Watrous §§2.2.1–2.2.2, especially Corollary 2.27; [bridge notation](WATROUS_BRIDGE.md#notation); [supported maps](../science/model.md#supported-operators-channels-and-generators).

### M04 — Exact tensor support

**Central question.** What does it mean for an operation to act only on a subset of sites?

**Understanding target.** Interpret a supported channel as a channel on the chosen subset tensored with the identity map on its complement. Recognize that a proper subset can be disconnected or contain all but one site.

**Dependencies and story role.** Depends on M02–M03. It gives the precise spatial constraint before any impossibility statement is considered.

**Conceptual connection.** The theorem constrains the induced system channel’s tensor support; later comparisons with local gates and bath couplings depend on this definition.

**Sources.** Watrous §2.2.1 for channel notation; [bridge local preservation](WATROUS_BRIDGE.md#local-preservation); [support convention](../science/model.md#supported-operators-channels-and-generators).

### M05 — Fixed states, identity maps, and relaxation

**Central question.** What can be inferred when a channel leaves one state unchanged?

**Understanding target.** Distinguish having a fixed state, fixing every state, and converging to a unique fixed state. Understand that the identity channel preserves every state but performs no relaxation.

**Dependencies and story role.** Depends on M03–M04. It separates the different dynamical claims used in the main result and its consequences.

**Conceptual connection.** Local rigidity says that exact preservation of this particular correlated state forces the entire local channel to be the identity.

**Sources.** Watrous §4.2.2 for unital-channel fixed points and spectra; [rigidity definition](../science/channel-criterion.md#1-local-preservation-and-local-rigidity); [global reset example](../science/local-updates.md#the-spatial-support-bound-is-attainable).

### M06 — Preserving projective measurements

**Central question.** When does an unread projective measurement leave a joint state unchanged?

**Understanding target.** Explain pinching into orthogonal blocks and why preservation is equivalent to block diagonality in the measured projectors. Allow projectors of arbitrary rank.

**Dependencies and story role.** Depends on M01, M04, and M05. It supplies a concrete preserving operation from which the general channel criterion can be understood.

**Conceptual connection.** A nonscalar commuting observable gives a nontrivial preserving pinching through its spectral projectors.

**Sources.** Watrous §4.1.1, Definition 4.4 and Example 4.5, for arbitrary-rank pinching; §2.2.3 for dephasing examples; [projective pinching and Theorem 1](../science/channel-criterion.md#2-the-established-channel-criterion); [bridge fixed points](WATROUS_BRIDGE.md#fixed-points-and-the-missing-implication).

### M07 — Commutants and a full one-qubit algebra

**Central question.** How does commutation constrain the possible action of an operator?

**Understanding target.** Define a commutant, distinguish scalar from nonscalar commuting operators, and explain why an operator commuting with all Pauli operators on one site acts as identity on that site.

**Dependencies and story role.** Depends on M01 and M06. It provides the algebraic language that connects local invariance to the graph proof.

**Conceptual connection.** The boundary argument will force commutation with the full local Pauli algebra and thereby remove sites from the possible support of a conserved observable.

**Sources.** Watrous §1.1.2 and §4.2.2, with Theorem 4.25 restricted to its unital setting; [local commutant](../science/channel-criterion.md#1-local-preservation-and-local-rigidity); [boundary conclusion](../science/hamiltonian-rigidity.md#3-resolving-the-boundary-sites).

### M08 — The structure of a faithful fixed space

**Central question.** What structure must the fixed operators of a channel share when a faithful fixed state exists?

**Understanding target.** Interpret the direct sum of tensor blocks in which one factor can vary and the other has a fixed density operator. Identify how the several-block and fixed-factor possibilities can reveal a preserving local observable.

**Dependencies and story role.** Depends on M02, M05, and M07. It combines operator algebra with correlated-state structure.

**Conceptual connection.** This is the structural input behind the established implication from a nonidentity preserving channel to a nontrivial preserving measurement. Watrous’s unital fixed-point theorem alone does not state the full faithful, potentially nonunital result.

**Sources.** Watrous §4.2.2 for the unital foundation; [attributed faithful fixed-space structure](../science/channel-criterion.md#fixed-space-structure-used-in-the-proof); [bridge missing implication](WATROUS_BRIDGE.md#fixed-points-and-the-missing-implication).

### M09 — Gibbs states and the matrix logarithm

**Central question.** Why does a finite-temperature Gibbs state retain the Hamiltonian’s commutation relations?

**Understanding target.** Explain the normalized exponential defining the Gibbs state and use its logarithm to recover the Hamiltonian up to a scale and an additive scalar, at finite nonzero inverse temperature.

**Dependencies and story role.** Depends on M01 and M07. It connects equilibrium physics to the operator criterion.

**Conceptual connection.** The commutant equality will make the rigidity question independent of temperature throughout the stated finite nonzero-temperature domain.

**Sources.** Watrous §1.1.3 for spectral decomposition; [Gibbs criterion](../science/channel-criterion.md#3-gibbs-preservation-is-a-hamiltonian-condition); [bridge Gibbs states](WATROUS_BRIDGE.md#gibbs-states-and-commutants).

### M10 — Physical generators and termwise stationarity

**Central question.** What extra conditions are imposed when equilibrium-preserving operations form a continuous-time sampler?

**Understanding target.** Explain a GKSL generator and its CPTP semigroup, then distinguish stationarity under each physical term from stationarity under their sum. Recognize the project’s precise frustration-free requirement.

**Dependencies and story role.** Depends on M03–M05. It introduces the dynamical application while keeping each allowed update physical.

**Conceptual connection.** A channel obstruction can be applied to every semigroup time of an individually stationary local generator. The generator discussion is supplied by the project rather than attributed to an unverified section of the anchor.

**Sources.** [Model of supported generators](../science/model.md#supported-operators-channels-and-generators); [bridge physical generators](WATROUS_BRIDGE.md#physical-generators); [semigroup consequence](../science/local-updates.md#from-channels-to-lindblad-generators).

### M11 — Rank conditions and the meaning of genericity

**Central question.** How can one explicit example imply a statement about almost every member of a continuous Hamiltonian family?

**Understanding target.** Relate injectivity of a finite matrix to its Gram determinant, and understand why a determinant polynomial that is nonzero at one point has a zero set of measure zero and empty interior. Keep the specified parameter space explicit.

**Dependencies and story role.** Depends on M01 and M07. It introduces the mathematical bridge from a construction to a family-wide result.

**Conceptual connection.** The new graph witness will certify that the commutator-rank polynomial is not identically zero; numerical sampling is not needed for genericity.

**Sources.** Watrous §§1.1.2–1.1.3 for matrix and operator foundations; [polynomial argument](../science/hamiltonian-rigidity.md#5-from-one-construction-to-a-generic-theorem); [bridge boundary constraints and genericity](WATROUS_BRIDGE.md#boundary-constraints-and-genericity).

### M12 — The complete equilibrium-preservation question

**Central question.** What must be specified before the locality obstruction has a definite physical meaning?

**Understanding target.** State the finite connected graph, qubit interaction family, proper subsystem, physical channel or generator, global exact-preservation requirement, and finite nonzero inverse-temperature domain together.

**Dependencies and story role.** Integrates M02, M04, and M08–M11. It completes the background phase by assembling the full problem and the tools needed to address it.

**Conceptual connection.** The route is now visible: local channel structure leads to a Hamiltonian commutant, graph interactions constrain that commutant, and the result limits exact termwise-preserving dynamics.

**Sources.** [Question, model, and results](../science/model.md); [bridge reading route](WATROUS_BRIDGE.md#source-and-reading-route); [scope checks](WATROUS_BRIDGE.md#scope-checks).

## Narrative and innovation

### M13 — From an arbitrary preserving channel to an observable

**Central question.** Why does any nonidentity preserving local channel imply a nonscalar local observable that commutes with the global state?

**Understanding target.** Follow the faithful fixed-space argument through its alternatives: multiple invariant blocks yield a block projector, and a nontrivial fixed tensor factor yields a commuting observable. Explain why the remaining case is the identity channel.

**Dependencies and story role.** Depends on M06–M08 and M12. It begins the narrative with the local-channel implication on which the physical obstruction rests.

**Conceptual connection.** This is the established Lie–Ng ingredient. The project’s Hamiltonian contribution uses it rather than claiming the channel characterization as new.

**Sources.** [Theorem 1 and its proof](../science/channel-criterion.md#2-the-established-channel-criterion); [bridge fixed points](WATROUS_BRIDGE.md#fixed-points-and-the-missing-implication); [attribution](../references/related-work.md#contribution-and-inherited-ingredients).

### M14 — Removing temperature from the local rigidity question

**Central question.** How does the state-level criterion become an exact statement about one local Hamiltonian commutant?

**Understanding target.** Combine the channel criterion with the Gibbs logarithm and explain both directions of the equivalence. Identify precisely why the same Hamiltonian conclusion applies at every finite nonzero inverse temperature.

**Dependencies and story role.** Depends on M09 and M13. It reduces the scientific question to the operator problem that the construction will solve.

**Conceptual connection.** The proof can work directly with local interactions; it does not need to diagonalize thermal density matrices or prove a separate result at each temperature.

**Sources.** [Corollary 2](../science/channel-criterion.md#3-gibbs-preservation-is-a-hamiltonian-condition); [bridge Gibbs states and commutants](WATROUS_BRIDGE.md#gibbs-states-and-commutants).

### M15 — Constructing the weighted interaction Hamiltonian

**Central question.** Which local couplings provide enough independent boundary information to constrain a conserved observable?

**Understanding target.** Explain the choice of two Pauli coupling directions on each edge, the need for nonzero weights with distinct squared incident values, and the bounded rational example satisfying these conditions on any finite graph.

**Dependencies and story role.** Depends on M04, M07, M11, and M14. It introduces the concrete local mechanism carrying the new Hamiltonian result.

**Conceptual connection.** The construction remains inside the one-site and edge two-site coefficient family; no long-range interaction is inserted to create the obstruction.

**Sources.** [Hamiltonian family](../science/hamiltonian-rigidity.md#1-hamiltonian-family-and-quantifiers); [bounded-coupling construction](../science/hamiltonian-rigidity.md#2-a-bounded-coupling-construction); [bridge graph argument](WATROUS_BRIDGE.md#boundary-constraints-and-genericity).

### M16 — Reading the exterior Pauli coefficients

**Central question.** What does global commutation reveal at one vertex outside the proposed support?

**Understanding target.** Separate internal, external, and crossing interactions, and explain why linear independence of the exterior Pauli operators forces commutation with two weighted sums on the inside boundary.

**Dependencies and story role.** Depends on M07 and M15. It extracts the first local constraints from the global conserved-operator equation.

**Conceptual connection.** The outside system provides independent operator labels. This coefficient argument works even when the chosen subsystem is disconnected.

**Sources.** [Boundary coefficient argument](../science/hamiltonian-rigidity.md#3-resolving-the-boundary-sites), Eqs. (11)–(15); [bridge boundary constraints](WATROUS_BRIDGE.md#boundary-constraints-and-genericity).

### M17 — Generating distinguishable powers of the edge weights

**Central question.** How do repeated commutators turn two collective boundary constraints into several independent ones?

**Understanding target.** Explain why cross-site commutators vanish and why each double commutator adds a squared edge-weight factor to the corresponding site term. Use the Jacobi identity to transfer these constraints to the conserved observable.

**Dependencies and story role.** Depends on M07 and M16. It identifies the mechanism that separates several neighbors of the same exterior vertex.

**Conceptual connection.** Noncommuting Pauli directions create a sequence of weighted sums whose coefficients encode the individual incident edges.

**Sources.** [Nested-commutator calculation](../science/hamiltonian-rigidity.md#3-resolving-the-boundary-sites), Eqs. (16)–(17); [bridge graph argument](WATROUS_BRIDGE.md#boundary-constraints-and-genericity).

### M18 — Separating individual boundary sites

**Central question.** Why do distinct squared weights allow the collective constraints to determine each site separately?

**Understanding target.** Interpret the resulting coefficient matrix as a weighted Vandermonde matrix, identify its nonzero determinant factors, and explain how invertibility isolates each boundary Pauli operator.

**Dependencies and story role.** Depends on M11 and M17. It converts the generated constraints into independently resolved boundary sites.

**Conceptual connection.** The weight condition is a sufficient device for this construction. Equal weights can retain permutation symmetries, but the condition is not a classification of all rigid Hamiltonians.

**Sources.** [Vandermonde separation](../science/hamiltonian-rigidity.md#3-resolving-the-boundary-sites), Eqs. (18)–(21); [equal-weight star example](../science/examples.md#why-distinct-boundary-weights-matter).

### M19 — Removing the resolved sites from the conserved operator

**Central question.** What follows once the candidate conserved operator commutes with both Pauli directions at a boundary site?

**Understanding target.** Complete the local Pauli algebra using commutators and infer that the conserved operator factors as identity on each resolved boundary site.

**Dependencies and story role.** Depends on M07 and M18. It turns algebraic constraints into a strict reduction of the possible support.

**Conceptual connection.** “Commutation with the full site algebra” is stronger than commutation with one local observable; it removes all dependence on that site.

**Sources.** [Boundary factorization](../science/hamiltonian-rigidity.md#3-resolving-the-boundary-sites), Eqs. (20)–(23); [bridge boundary constraints](WATROUS_BRIDGE.md#boundary-constraints-and-genericity).

### M20 — Propagating the constraint through the whole graph

**Central question.** Why can no nontrivial part of the conserved operator remain hidden deeper inside the subsystem?

**Understanding target.** Reapply the boundary argument after each removal and explain why graph connectedness guarantees progress until the remaining operator is scalar. Include subsets with only one omitted vertex.

**Dependencies and story role.** Depends on M16 and M19. It completes the graph construction by carrying a local boundary mechanism to every proper subsystem.

**Conceptual connection.** The original commutator equation is retained at every step; the proof changes the active support rather than the Hamiltonian.

**Sources.** [Connected-graph propagation proof](../science/hamiltonian-rigidity.md#4-propagating-the-constraint-through-a-connected-graph); [graph-connectedness qualification](../science/hamiltonian-rigidity.md#6-meaning-and-scope-of-the-generic-statement).

### M21 — Certifying a scalar commutant by a polynomial

**Central question.** How is the operator statement for one subsystem encoded as a condition on Hamiltonian coefficients?

**Understanding target.** Form the commutator map on traceless Hermitian operators, relate a scalar commutant to injectivity, and explain why its Gram determinant is a polynomial that is positive at the constructed Hamiltonian.

**Dependencies and story role.** Depends on M11, M14, and M20. It transfers the explicit example to the full continuous family of allowed interactions.

**Conceptual connection.** Removing the scalar operator before taking the rank is essential: the identity always commutes and must not create an unavoidable zero determinant.

**Sources.** [Commutator map and Gram determinant](../science/hamiltonian-rigidity.md#5-from-one-construction-to-a-generic-theorem), Eqs. (25)–(26); [bridge genericity](WATROUS_BRIDGE.md#boundary-constraints-and-genericity).

### M22 — The simultaneous generic Gibbs theorem

**Central question.** How do the individual subsystem conditions become one result covering every proper support and every finite nonzero temperature?

**Understanding target.** Explain the finite product over subsystem polynomials, the resulting proper algebraic exceptional set, and the separate Hamiltonian-to-Gibbs step that supplies all temperatures for the same Hamiltonian.

**Dependencies and story role.** Integrates M14 and M20–M21. It assembles the principal theorem from the local mechanism and the genericity argument.

**Conceptual connection.** Full measure, openness, and density refer to the specified full coefficient space. They do not automatically transfer to a symmetry-restricted subfamily.

**Sources.** [Theorem 3 and its quantifiers](../science/hamiltonian-rigidity.md#1-hamiltonian-family-and-quantifiers); [finite-product argument](../science/hamiltonian-rigidity.md#5-from-one-construction-to-a-generic-theorem); [genericity scope](../science/hamiltonian-rigidity.md#6-meaning-and-scope-of-the-generic-statement).

### M23 — Explicit Ising conclusions beyond a generic assertion

**Central question.** What can be established directly for a specified familiar Hamiltonian family?

**Understanding target.** Explain endpoint removal for the open transverse-field Ising chain and the additional commutators needed for the disconnected triple in the homogeneous four-spin chain. Distinguish the interval result from the four-spin all-subset result.

**Dependencies and story role.** Depends on M07, M14, M20, and M22. It connects the abstract graph statement to exact, parameter-explicit examples.

**Conceptual connection.** These proofs establish conclusions within specified restricted families instead of assuming that genericity in the larger space already covers them.

**Sources.** [Open Ising proof](../science/examples.md#open-ising-chain); [four-spin proof](../science/examples.md#four-spin-ising-chain); [exact finite checks](../verification/README.md).

### M24 — Understanding the exceptional families

**Central question.** Which assumptions permit nontrivial local preserving operations to reappear?

**Understanding target.** Explain the roles of reflection symmetry, equal-weight leaf permutations, diagonal classical heatbath updates, disconnected components, and infinite temperature. Identify the conserved local observable or preserving channel in each case.

**Dependencies and story role.** Depends on M06 and M22–M23. It places the theorem inside a larger physical picture with explicit exceptions.

**Conceptual connection.** Noncommuting interactions alone do not imply rigidity. The exact criterion is the local commutant within the stated Hamiltonian family.

**Sources.** [Examples and exceptions](../science/examples.md); [genericity boundaries](../science/hamiltonian-rigidity.md#6-meaning-and-scope-of-the-generic-statement); [bridge scope checks](WATROUS_BRIDGE.md#scope-checks).

### M25 — From channel rigidity to the generator obstruction

**Central question.** Why must an individually physical, individually stationary generator with proper support vanish?

**Understanding target.** Apply channel rigidity at every semigroup time and differentiate at zero. Derive the full-support necessity for every nonzero term in the project’s exact frustration-free Gibbs generator.

**Dependencies and story role.** Depends on M10, M14, and M22. It converts the principal theorem into the central dynamical consequence.

**Conceptual connection.** Complete positivity of each semigroup and stationarity of each term are load-bearing hypotheses; no detailed-balance or mixing-rate assumption is used.

**Sources.** [Generator proof and corollary](../science/local-updates.md#from-channels-to-lindblad-generators); [physical-summand model](../science/model.md#supported-operators-channels-and-generators); [bridge physical generators](WATROUS_BRIDGE.md#physical-generators).

### M26 — Attaining the support bound with a global reset

**Central question.** Is full system support sufficient once it is allowed?

**Understanding target.** Explain the replacement channel, its Kraus representation, and the relaxing generator obtained by subtracting the identity map. Recognize exactly which preparation resource the construction assumes.

**Dependencies and story role.** Depends on M03, M05, and M25. It establishes that the spatial support requirement is tight as an existence statement.

**Conceptual connection.** Support attainability and efficient state preparation are different claims. The construction proves the former without supplying a free target state or a gate-complexity bound.

**Sources.** Watrous §2.2.2 for Kraus representations; [global reset and semigroup](../science/local-updates.md#the-spatial-support-bound-is-attainable); [bridge physical generators](WATROUS_BRIDGE.md#physical-generators).

### M27 — Recognizing dynamics outside termwise preservation

**Central question.** Why can local dynamics preserve equilibrium globally without contradicting this result?

**Understanding target.** Explain cancellation among local Hamiltonian generators whose sum is generated by the full Hamiltonian. Distinguish strict channel support from microscopic bath locality and from locality of circuit gates that move the target during intermediate steps.

**Dependencies and story role.** Depends on M10, M12, and M25. It separates the exact dynamical conclusion from broader thermalization questions.

**Conceptual connection.** The condition imposed on each update determines the reach of the obstruction. Global stationarity cannot be substituted for individual stationarity.

**Sources.** [Cancellation example](../science/local-updates.md#why-stationarity-of-the-sum-is-insufficient); [tails, bath coupling, and circuit locality](../science/local-updates.md#strict-support-decaying-tails-and-circuit-locality); [related-work comparisons](../references/related-work.md).

### M28 — Exact impossibility and small approximate disturbance

**Central question.** How can a fixed nonidentity local operation become almost Gibbs-preserving while exact preservation remains forbidden?

**Understanding target.** Follow the high-temperature trace-norm bound for a unital local channel and explain why its disturbance tends to zero for fixed finite Hamiltonian as inverse temperature tends to zero. Keep exact nonzero disturbance distinct from a uniform detectable lower bound.

**Dependencies and story role.** Depends on M03, M09, M22, and M27. It gives the quantitative limiting example needed to interpret the exact theorem responsibly.

**Conceptual connection.** Exact support necessity is compatible with small quasilocal tails and useful approximate truncations; the project proves no error-versus-range law.

**Sources.** [High-temperature approximation bound](../science/local-updates.md#exact-rigidity-can-coexist-with-very-accurate-local-updates); [bridge scope checks](WATROUS_BRIDGE.md#scope-checks); [meaning of exact rigidity](../science/channel-criterion.md#1-local-preservation-and-local-rigidity).

### M29 — Attribution, exact evidence, and the earlier Ising claim

**Central question.** Which conclusions rest on inherited theorems, new proofs, and finite verification?

**Understanding target.** Attribute the channel-sensitivity theorem and fixed-space structure correctly, identify the graph and genericity contribution, and explain the role of exact finite commutator checks. State the precise incompatibility with the earlier four-spin numerical stabilization claim without inferring its computational cause.

**Dependencies and story role.** Depends on M13, M22–M23, and M28. It integrates the scientific argument with its source and verification boundaries.

**Conceptual connection.** A finite rank certificate supports its specified example. The written graph proof supplies the arbitrary-graph result, while the source comparison determines what is additional to prior work.

**Sources.** [Related work](../references/related-work.md); [verification scope and commands](../verification/README.md); [four-spin analytical proof](../science/examples.md#four-spin-ising-chain).

### M30 — The complete physical and mathematical account

**Central question.** What does Gibbs Locality Obstruction establish, and how does each part of the argument support that conclusion?

**Understanding target.** Give a connected account from exact global preservation and the known channel criterion through the weighted boundary mechanism, graph propagation, and polynomial genericity to the tight full-support requirement. Include the explicit examples, relevant exceptions, preparation-resource qualification, and approximation boundary.

**Dependencies and story role.** Integrates M22 and M24–M29, drawing on the whole map. It completes the narrative phase with the contribution, mechanism, evidence, and scope together.

**Conceptual connection.** Generic two-body interactions can make every proper subsystem sensitive to any nonidentity physical update, even at finite high temperature. The resulting obstruction concerns exact individually preserving operations and leaves the stated broader thermalization mechanisms available.

**Sources.** [Repository overview](../README.md); [model and principal theorem](../science/model.md); [Hamiltonian proof](../science/hamiltonian-rigidity.md); [dynamical interpretation](../science/local-updates.md); [source comparison](../references/related-work.md); [Watrous bridge](WATROUS_BRIDGE.md).

