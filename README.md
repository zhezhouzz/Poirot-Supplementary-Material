# PLDI 23 Supplementary Material

## Results

The Coq formalization of our core language and the soundness theorem are shown folder "proof".

## Benchmarks

There are details of `14` benchmarks which are shown in folders with the same name of the benchmark under "benchmarks" folder.
Each benchmark has a file `prog.ml` which presents the source code of input test genarator and a file `ty.ml` present the coverage types, which include the coverage type we want to check against (having the same name of the input test geneartor) and the coverage types of the libary functions (notated with `[@library]`). For example, there are three types in `RedBlackTree\ty.ml`: two types that have name `int_gen` and `bool_gen` which are the types of the library functions, one type has name `rbtree_gen` which is the type we want to check with the `rbtree_gen` program in `RedBlackTree\prog.ml`.
