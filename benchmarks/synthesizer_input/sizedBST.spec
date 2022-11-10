qualifier tlen : tree :-> int;
qualifier sortedtree : tree :-> bool;
qualifier tmem : tree :-> int :-> bool;
qualifier rng : tree :-> int;
qualifier low : int :-> bool;
qualifier high : int :-> bool;




dummy : {v : unit | true};

bool_gen : (u:unit) -> {v : bool | [v=true] <=>[v=true] /\
                                    [v=false] <=> [v=false]};


lt_eq_one : (s : int) -> {v : bool | [v=true] <=> not [s > 1] /\ 
                            [v=false] <=> [s>1]};


decrement : (n : {v : int | true}) ->  {v : int | v == n -- 1};

int_range : (a : int) -> (b : int) -> {v : int | not [a > v] /\ not [v > b]};


increment : (n : {v : int | true}) ->  {v : int | v == n + 1};


Leaf : {v : tree | \(u : int).
                    rng (v) == 0 /\
                    tmem (v, u) = false /\ 
                    sortedtree (v) = true };



Node : 
    (root : { v : int | true}) -> 
    (ltree : {v : tree | \(u : int), (range1 : int).  
                    ( (tmem (v, u) = true /\ rng (v) == range1)  => 
                        ([root > u] /\ (u > root -- range1))
                    )/\ 
                    sortedtree (v) = true}
    ) -> 
    (rtree : {v : tree | \(u : int), (range2 : int).  
                    ( (tmem (v, u) = true /\ rng (v) == range2)  => 
                       ([u > root] /\ (root > u -- range2))
                    )/\ 
                    sortedtree (v) = true}
    ) -> 
        {v : tree | 
                    \(u : int), (range1:int), (range2: int). 
                (range1 == rng (ltree) /\ range2 == rng (rtree)) /\
                ((u == range1 + range2) => rng (v) == u) /\
                (tmem (v, u) = true => 
                        (u > (root -- range1) /\ 
                        root > (u -- range2))) 
                    /\ sortedtree (v) = true};    




goal : (d : {v : int | [v >0] \/ [v=0]}) -> 
        (s0 : {v : int | not [d > v]}) ->
        (lo : { v : int | true}) -> 
        (hi : { v : int | v == lo + d}) -> 
        {v : tree | \(u : int).
            (   hi == lo + d /\
                (tmem (v, u) = true => 
                ([u > lo] /\ [hi > u]) 
                ) /\
                sortedtree (v) = true /\
                rng (v) =  d
            )   
            };
