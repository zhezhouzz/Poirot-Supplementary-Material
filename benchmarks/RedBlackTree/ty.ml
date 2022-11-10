let[@library] int_gen =
  let (dummy : [%over: unit]) = (true : [%v: unit]) in
  (true : [%v: int])

let[@library] bool_gen =
  let (dummy : [%over: unit]) = (true : [%v: unit]) in
  (true : [%v: bool])

let rbtree_gen =
  let (inv : [%over: int]) = (v >= 0 : [%v: int]) in
  let (c : [%over: bool]) = (true : [%v: bool]) in
  let (height : [%over: int]) =
    (v >= 0 && implies c (v + v == inv) && implies (not c) (v + v + 1 == inv)
      : [%v: int])
  in
  (numblack v height && noredred v
   && fun (u : [%forall: int]) ->
   (c && not (hdcolor v true))
   ||
   ((not c) && implies (height == 0) (hdcolor v true))
    : [%v: int rbtree])
