
qualifier slen : list :-> int;
qualifier slist : list :-> bool;
qualifier shd : list :-> int;
qualifier sorder : list :-> int :-> int :-> bool;
qualifier smem : list :-> int :-> bool;


gt_eq_int_gen : (n3: int) -> {v : int | [v > n3] \/ [v=n3]}; 


subs : (n : {v : int | true}) ->  {v : int | v == n -- 1};

Nil : {v : list | \(u : int).
                    smem (v, u) = false /\ 
                    rng (v) == 0};
sizecheck : (s : int) -> 
        {v : bool | [v=true] <=> [s=0] /\ 
                    [v=false] <=> [s>0]};

Cons : (x : {v : int | [v>0] \/ [v=0]}) -> 
       (xs : {v : list | slist (v) = true}) -> 
                {v : list | 
                    \(u : int), (w : int). 
                        (smem (v, u) = true => (not [x > u])) /\
                        (shd (v) = u <=> [u = x]) /\
                        (shd (v) = u => smem (v, u) = true) /\
                        (sorder (v, u, w) => not [u > w]) /\
                        (slist (v) = true)
                         }; 

let[@library] cons =
  let (h : [%over: int]) = (true : [%v: int]) in
  let (s : [%over: int]) = (true : [%v: int]) in
  let (dummy : [%under: int list]) =
    (rng v s && fun (u : [%forall: int]) (w : [%forall: int]) ->
     implies (mem v u) (h <= u) && implies (ord v u w) (u <= w)
      : [%v: int list])
  in
  (fun (u : [%forall: int]) (w : [%forall: int]) ->
     implies (u == s + 1) (rng v u)
     && implies (mem v u) (h <= u)
     && implies (ord v u w) (u <= w)
    : [%v: int list])


goal : (size : { v : int | true}) -> 
                (x0 : {v : int | [v>0] \/ [v=0]}) -> 
                    {v : list | 
                    
                    
                            \(u : int), (w : int).
                            rng (v) = size /\
                            (smem (v, u) = true => not [x0 > u]) /\
                            (sorder (v, u, w) = true => not [u > w])};


let sorted_list_gen =
  let (s : [%over: int]) = (0 <= v : [%v: int]) in
  let (x : [%over: int]) = (true : [%v: int]) in
  (rng v s && fun (u : [%forall: int]) (w : [%forall: int]) ->
   implies (mem v u) (x <= u) && implies (ord v u w) (u <= w)
    : [%v: int list])
