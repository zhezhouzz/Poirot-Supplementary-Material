# Proof Readme #

## Build ##

- Coq version: `8.13.2`.
- The project is orgnized by the coq make file `_CoqProject` under this folder.
- Build command.

```
# make
```

## File Structures ##

The files are structured as follows:
+ Definitions and proofs that are independent of Poirot's type system.
  - `Maps.v`: Definitions and notations of program state.
  - `CoreLang.v`: Definitions and notations relevant to the syntax and operational semantics of our core language `λTG`.
  - `NormalTypeSystem.v`: Definitions and notations for a basic type system.
  - `Ax.v`: The axioms and facts relevant to the operational semantics.
+ Definitions and proofs for Poirot's type system.
  - `LinearContext.v`: Definitions and notations for reasoning about polymorphic contexts.
  - `RfTypeDef.v`: Definitions and notations of coverage types.
  - `NoDup.v`: Some tactics to handle duplicate naming.
  - `TypeClosed.v`: Definitions and notations for coverage types that are closed under a given context.
  - `Denotation.v`: Definitions and notations for type denotations.
  - `WellFormed.v`: Definitions and notations of well-formed typing rules.
  - `CtxErase.v`: Some tactics to transfer coverage types to basic types.
  - `TermMeet.v`: Various auxiliary definitions.
  - `DenotationAux.v`: Some tactics for reasoning about type denotations.
  - `TypeDisj.v`: Definitions and notations of disjunction typing rules.
  - `DenotationSpecs.v`: Tactics for type denotations.
  - `WellFormedSpecs.v`: Tactics for reasoning about well-formed typing rules.
  - `Subtyping.v`: Definitions and notations relevant to subtyping.
  - `TypingRules.v`: Definitions and notations used in the  typing rules.
  - `Soundness.v`: Statement and proof of the soundness theorem and related corollaries.

## Paper-to-artifact Correspondence ##


| Definition/Theorems  | Paper | Definitoin | Notation |
| ------------- | ------------- | ------------- | ------------- |
| Syntax | Figure 3  | mutual recursive defined as `value` and `tm` in file `CoreLang.v` |  |
| Operaional semantcis | Figure 11 (supplementary materials)  | `step`in file `CoreLang.v` | `e --> v` |
| Basic typing rules | Figure 12 (supplementary materials)  | mutual recursive definition of `has_type` and `value_hsa_type` in file `NormalTypeSystem.v` | `Gamma \N- t \vin T` and `Gamma \N- t \Tin T` |
| Well-formedness typing rules | Figure 4  | `well_formed` in file `WellFormed.v`  | |
| Subtyping rules | Figure 4  | `is_subtype` in file `Subtyping.v`  | `Gamma \C- t1 \<: t2` |
| Disjunction typing rules | Figure 4  | `disjunct` in file `TypeDisj.v` | `Gamma \C- t1 \tyor t2 \tyeq t3` |
| Selected typing rules | Figure 5 (Figure 13 in supplementary materials shows full set of rules) | mutual recursive defined as `value_under_type_check` and `term_under_type_check` in file `TypingRules.v` | `Gamma \C- t \Vin T` and `Gamma \C- t \Tin T`|
| Type denotation (under context) | At the beginning of Section 4.1 | `tmR_aux` (`tmR_in_ctx_aux` under context) in file `Definition.v` | |
| Subset relation of type denotation under context | Section D (supplementary material) | `tmR_sub_in_ctx_aux` in file `Subtyping.v` |
| Soundness theorem | Theorem 4.2 | `soundness` in file `Soundness.v`  | |

## Differences Between Paper and Artifact ##

- The formalization considers only two base types: nat and bool.
- The formalization considers only four primitive operators: `+`, `==`, `<`, `nat_gen`. Other operators can be defined in terms of these. E.g.,

```
let minus (x: nat) (y: nat) =
    let (diff: nat) = nat_gen () in
    if x + diff == y then diff else err
```

In addition, to simplify the syntax, all operators take two input arguments; e.g., the random nat generator takes two arbitray numbers as input.
- In the formalization, to simplify the syntax, pattern-matching can only pattern match against Boolean variables. Pattern matching over natural numbers

```
match n with
| 0 -> f 0
| S n' -> g n' 
```

is implemented as follows:

```
if n == 0 then f 0
else g (n - 1)
```

- We assume all input programs are alpha-converted, such that all variables have unique names.
- The substitution of refinement types are formalized into a state, helping to eliminate terminattion checks of the fixpoint function in Coq when we define the logical relation.
- In the formalization, our coverage typing rules additionally require that the all branches of a pattern matching expression are type safe in the basic type system (they may not be consistent with the coverage type we want to check).  This restriction helps guarantee that a program with coverage types is type safe under a basic type system.

## Axioms ##

Our formalization relies on `FunctionalExtensionality` and `PropExtensionality` axioms since we need to reason over the equality of refinement types that have qualifiers (deeply embeded as Coq propositions (`Prop`)). We also rely on various other assumptions listed in the file `Ax.v`:
- Renaming assumptions related to binding and duplication.
- Programs always halt. We assume there exists a well-founded relation over all constants, used in the `decreases` check of the typing rule of the fix-point function; if a term can reduce to a value, then they have the same basic type (this is implied by the perservation property for halting programs)
- Some syntactic equivalence facts of our core language, for example `let x = e_x in x` is equal to `e_x`.  
