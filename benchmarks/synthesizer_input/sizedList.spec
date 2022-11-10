
qualifier slen : list :-> int;
qualifier slist : list :-> bool;
qualifier shd : list :-> int;
qualifier sorder : list :-> int :-> int :-> bool;
qualifier smem : list :-> int :-> bool;


un : unit;

subs : (n : {v : int | true}) ->  {v : int | v == n -- 1};


gt_eq_int_gen : (n3: int) -> {v : int | [v > n3] \/ [v = n3]}; 

bool_gen : (u : unit) -> {v : bool | [v=true] <=>[v=true] /\
                                    [v=false] <=> [v=false]};

Nil : {v : list | slen (v) == 0};
sizecheck : (s : int) -> 
        {v : bool | [v=true] <=> [s=0] /\ 
                    [v=false] <=> [s>0]};

Cons : (x : {v : int | true}) -> 
       (xs : {v : list | true}) -> 
                {v : list | 
                    \(u : int). 
                        ((u == slen (xs) + 1) => slen (v) == u)
                         }; 




goal : (size : { v : int | true}) -> 
                    {v : list | \(u : int). 
            (slen (v) == u => ( ([u > 0] \/ [u = 0]) /\ 
                              not [u > size]))};
