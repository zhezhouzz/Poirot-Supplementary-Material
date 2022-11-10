# Proof Readme #

## Build ##

- Coq version: `8.13.2`.
- The project is organized by the coq make file `_CoqProject` in this folder.
- Build command.

```
# make
```

## File Structures ##

The files are structured as the following:
+ The parts that are independent of our coverage type system.
  - `Maps.v`: The definitions and notations of state, as in Software Foundations.
  - `CoreLang.v`: The definitions and notations of the syntax and operational semantics of our core language `λTG`.
  - `NormalTypeSystem.v`: The definitions and notations of the basic type system.
  - `Ax.v`: Axioms and facts about the operational semantics.
+ The development of our coverage type system.
  - `LinearContext.v`: The definitions and notations of a polymorphic context, implemented as a list.
  - `RfTypeDef.v`: The definitions and notations of coverage types.
  - `NoDup.v`: Some tactics handling duplicate naming.
  - `TypeClosed.v`: The definitions and notations the coverage types that is closed under context.
  - `Denotation.v`: The definitions and notations the type denotation.
  - `WellFormed.v`: The definitions and notations of our well-formedness rules.
  - `CtxErase.v`: Some tactics transfer the coverage types to basic types.
  - `TermMeet.v`: Auxiliary definitions, The meet (intersection) of terms
  - `DenotationAux.v`: Some tactics for the type denotations.
  - `TypeDisj.v`: The definitions and notations of disjunction typing rules.
  - `DenotationSpecs.v`: Tactics for working with type denotations.
  - `WellFormedSpecs.v`: Tactics for working with well-formedness facts.
  - `Subtyping.v`: The definitions and notations of the subtyping rules.
  - `TypingRules.v`: The definitions and notations of the typing rules.
  - `Soundness.v`: Our key soundness theorem and its corollary.

## Paper-to-artifact Correspondence ##


| Definition/Theorems  | Paper | Definition | Notation |
| ------------- | ------------- | ------------- | ------------- |
| Syntax | Figure 3  | mutual recursive defined as `value` and `tm` in file `CoreLang.v` |  |
| Operational semantics | Figure 11 (supplementary materials)  | `step`in file `CoreLang.v` | `e --> v` |
| Basic typing rules | Figure 12 (supplementary materials)  | mutual recursive defined as `has_type` and `value_hsa_type` in file `NormalTypeSystem.v` | `Gamma \N- t \vin T` and `Gamma \N- t \Tin T` |
| Well-formedness rules | Figure 4  | `well_formed` in file `WellFormed.v`  | |
| Subtyping rules | Figure 4  | `is_subtype` in file `Subtyping.v`  | `Gamma \C- t1 \<: t2` |
| Disjunction rules | Figure 4  | `disjunct` in file `TypeDisj.v` | `Gamma \C- t1 \tyor t2 \tyeq t3` |
| Selected typing rules | Figure 5 (Figure 13 in supplementary materials shows full set of rules) | given by the mutually inductive types `value_under_type_check` and `term_under_type_check` in file `TypingRules.v` | `Gamma \C- t \Vin T` and `Gamma \C- t \Tin T`|
| Type denotation (under context) | At the beginning of Section 4.1 | `tmR_aux` (`tmR_in_ctx_aux` under context) in file `Definition.v` | |
| Subset relation of type denotation under context | Section D (supplementary materials) | `tmR_sub_in_ctx_aux` in file `Subtyping.v` |
| Soundness theorem | Theorem 4.2 | `soundness` in file `Soundness.v`  | |

## Differences Between Paper and Artifact ##

- Our formalization only has two base types: nat and bool,
- Our formalization only have four operators: `+`, `==`, `<`,
  `nat_gen`. Other operators shown in the paper can be implemented in
  terms of these four, for example, the minus operator can be defined as the function:

```
let minus (x: nat) (y: nat) =
    let (diff: nat) = nat_gen () in
    if x + diff == y then diff else err
```

In addition, to simplify the syntax, all operators take two arguments as input, the random nat generator takes two arbitrary numbers as input.
- In the formalization, to simplify the syntax, we only implement pattern matching over booleans. The pattern matching over natural number

```
match n with
| 0 -> f 0
| S n' -> g n'
```

can be implemented as the following

```
if n == 0 then f 0
else g (n - 1)
```

- In the formalization, we assume all programs are converted to  alpha-equivalent versions in which no variables with the same name.
- In the formalization, the substitution of refinement types are formalized into a state. It can help as to get rid of termination check of the fixpoint function in Coq when we define the logic relation.
- In the formalization, our coverage typing rules additionally require the all branches of pattern matching expression are type safe in the basic type system (they may not consistent with the coverage type we want to check). This guarantees program with coverage types can also be assigned a basic type.

## Axioms ##

Our formalization assumes the functional and propositional extensionality axioms (`FunctionalExtensionality` and `PropExtensionality`) in order to reason about equality of refinement types (we encode qualifiers as Coq propositions `Prop`). We also rely on the following assumptions, all of which are axioms in the file `Ax.v`.
- The renaming assumptions (e.g., there exists a variable name that is not free in a term), there is no duplicate bindings in a state.
- Well-typed programs are terminating. We assume there exists a well-founded relation over all constants, used for the check of decrease in the typing rule of the fix-point function; if a term can reduce to a value, then they have the same basic type (it can be implied by the preservation property if the programs always halt).
- Some syntax equivalence fact of our core language, for example `let x = e_x in x` is equal to `e_x`.
