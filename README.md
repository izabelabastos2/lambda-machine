Simple lambda calculator


# Untyped syntax

* Atoms: `true, false, nil, 1i32, 42u, -1, 3.14, 3.14f32, "foo"`
* Lambdas: `ꟛ x: y` e `ꟛ x y: z` => `ꟛ x: ꟛ y: z`
* Apply: `f x` or `x | f`
* Let: `x = y; expr`
* Holes: `...`
* Ref: `$native`
* Pair: `x, y`
* First/Second: `x.0, x.1` (`x.2` => `x.1.1` and so on)
* First/Second selectors: `.0` or `.1`
* Record: `{ foo: 42, bar: 10 }` or `{} |+ foo 42 |+ bar 10`
* Record/add: `r |+ foo 42` or `+ foo`
* Record/remove: `r |- foo` or `- foo`
* Record/select: `r . foo` or `.foo r` or `r |. foo`
* Cons: `x : xs`
* List: `[a, b, c]` => `a : b : c : []`


```
fat = ꟛ n:
    aux = ꟛ(m, acc):
        match :is m {
            :is 0 -> acc;
            :is n -> aux(i32.sub(m, 1), m * acc);
        };
    aux(n, 1)
```