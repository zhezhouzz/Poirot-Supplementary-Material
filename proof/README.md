# Proof Readme #

## Build ##

- Coq version: `8.13.2`.
- The project is orgnized by the coq make file `_CoqProject` under this folder.
- Build command.

```
# make
```

## File Structures ##

The files are strcutured as the following:
+ The parts that are indepdent from our coverage type system.
  - `Maps.v`: The definitions and notations of the state, like Software Foundations.
  - `CoreLang.v`: The definitions and notations of the syntax and operational semantcis of our core language `λTG`.
  - `NormalTypeSystem.v`: The definitions and notations of the basic type system.
  - `Ax.v`: The axioms and fact of the operational semantcis.
+ The defintion of our coverage type system.
  - `LinearContext.v`: The definitions and notations of a polymorphic context, impelemenetd as a list.
  - `RfTypeDef.v`: The definitions and notations of coverage types.
  - `NoDup.v`: Some tactics handling duplicate naming.
  - `TypeClosed.v`: The definitions and notations the coverage types that is closed under context.
  - `Denotation.v`: The definitions and notations the type denotation.
  - `WellFormed.v`: The definitions and notations of well formedness typing rules.
  - `CtxErase.v`: Some tactics transfer the coverage types to basic types.
  - `TermMeet.v`: Auxlirary definitions, The meet (intersection) of terms
  - `DenotationAux.v`: Some tactics for the type denotations.
  - `TypeDisj.v`: The definitions and notations of disjunction typing rules.
  - `DenotationSpecs.v`: Some tactics for the type denotations.
  - `WellFormedSpecs.v`: Some tactics for the well formedness typing rules.
  - `Subtyping.v`: The definitions and notations of the subtyping typing rules.
  - `TypingRules.v`: The definitions and notations of the typing rules.
  - `Soundness.v`: The proof the soundness theorem and corollary.

## Paper-to-artifact Correspondence ##


| Definition/Theorems  | Paper | Definitoin | Notation |
| ------------- | ------------- | ------------- | ------------- |
| Syntax | Figure 3  | mutual recursive defined as `value` and `tm` in file `CoreLang.v` |  |
| Operaional semantcis | Figure 11 (supplementary materials)  | `step`in file `CoreLang.v` | `e --> v` |
| Basic typing rules | Figure 12 (supplementary materials)  | mutual recursive defined as `has_type` and `value_hsa_type` in file `NormalTypeSystem.v` | `Gamma \N- t \vin T` and `Gamma \N- t \Tin T` |
| Well fromedness typing rules | Figure 4  | `well_formed` in file `WellFormed.v`  | |
| Subtyping typing rules | Figure 4  | `is_subtype` in file `Subtyping.v`  | `Gamma \C- t1 \<: t2` |
| Disjunction typing rules | Figure 4  | `disjunct` in file `TypeDisj.v` | `Gamma \C- t1 \tyor t2 \tyeq t3` |
| Selected typing rules | Figure 5 (Figure 13 in supplementary materials shows full set of rules) | mutual recursive defined as `value_under_type_check` and `term_under_type_check` in file `TypingRules.v` | `Gamma \C- t \Vin T` and `Gamma \C- t \Tin T`|
| Type denotation (under context) | At the begining of Section 4.1 | `tmR_aux` (`tmR_in_ctx_aux` under context) in file `Definition.v` | |
| Subset relation of type denotation under context | Section D (supplementary materials) | `tmR_sub_in_ctx_aux` in file `Subtyping.v` |
| Soundness theorem | Theorem 4.2 | `soundness` in file `Soundness.v`  | |

## Differences Between Paper and Artifact ##

- In the formalization, we only have two base types: nat and bool, 
- In the formalization, we only have four operators: `+`, `==`, `<`, `nat_gen`. Other operators shown in the paper can be impelemenetd with them, for example, the minus operator can be defined as the funtion:

```
let minus (x: nat) (y: nat) =
    let (diff: nat) = nat_gen () in
    if x + diff == y then diff else err
```

In addition, to simplify the syntax, all of them are unified to take two arguments as input, the random nat generator takes two arbitray numbers as input.
- In the formalization, to simplify the syntax, the patterm match can only pattern match the bool variables. The pattern matching over natural number

```
match n with
| 0 -> f 0
| S n' -> f n' 
```

can be implemted the following

```
if n == 0 then f 0
else f (n - 1)
```

- In the formalization, we assume all program we checked are alpha-converted, which has no variables with the same name.
- In the formalization, the substitution of refinement types are formalized into a state. It can help as to get rid of terminattion check of the fixpoint function in Coq when we define the logic relation.
- In the formalization, our coverage typing rules addtionally requires the all branches of pattern matching expression are type safe in the basic type system (they may not consistent with the coverage type we want to check). It can help to gurantees the coverage typed program are also basic type safed.

## Axioms ##

Our formalization relies on the axiom of excluded middle (`FunctionalExtensionality` and `PropExtensionality`) since we need to reasoning the equalty of refinement types that has qualifiers (deep embeded as Coq `Prop`). We also rely on the following assumptions, all of them are axioms we listed in the file `Ax.v`.
- The renaming assumptions (e.g., there exists a variable name that is not free in a term), there is no duplicate bindinsg in a state.
- The programs we type check always halt. We assume there exists a well-founded relation over all constants, used for the decreasing check of the typing rule of the fix-point function; if a term can reduce to a value, then they have the same basic type (it can be implied by the perservation property if the programs always halt).
- Some syntax equivelence fact of our core language, for example `let x = e_x in x` is equal to `e_x`.  
