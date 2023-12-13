**a.i. Orden de evaluación normal**
```
misteriosa "abc" (gen 1)
< Def. misteriosa >
foldr what (const []) "abc" (gen 1)
< Def. foldr >
what "a" $ foldr what (const []) "bc" (gen 1)
< Def. gen >
what "a" $ foldr what (const []) "bc" (1:gen 2)
< Def. what >
("a",1) : foldr what (const []) "bc" (gen 2)
< Def. foldr >
("a",1) : what "b" $ foldr what (const []) "c" (gen 2)
< Def. gen  >
("a",1) : what "b" $ foldr what (const []) "c" (2:gen 3)
< Def. what >
("a", 1) : ("b", 2) : foldr what (const []) "c" (gen 3)
< Def. foldr >
("a", 1) : ("b", 2) : what "c" $ foldr what (const []) [] (gen 3)
< Def. gen >
("a", 1) : ("b", 2) : what "c" $ foldr what (const []) [] (3:gen 4)
< Def. what >
("a", 1) : ("b", 2) : ("c", 3) : foldr what (const []) [] (gen 4)
< Def. foldr >
("a", 1) : ("b", 2) : ("c", 3) : (const []) (gen 4)
< Def. const >
("a", 1) : ("b", 2) : ("c", 3) : []
< evaluación >
[("a", 1), ("b", 2), ("c", 3)]
```

**a.ii. Orden de evaluación aplicativo** 
```
misteriosa "abc" (gen 1)
< Def. gen >
misteriosa "abc" (1: gen 2)
< Def. gen >
misteriosa "abc" (1: 2: gen 3)
(...)
Entra en loop infinito.
```

**b**
```
data Arbol a = Hoja | Rama a (Arbol a) (Arbol a)

foldA :: (a -> b -> b -> b) -> b -> Arbol a -> b
foldA _ acc Hoja = acc
foldA f acc (Rama x izquierda derecha) = f x (foldA f acc izquierda) (foldA f acc derecha)
```

**c.i Orden de evaluación normal**
```
sospechosa arbolito (genA 1)
< Def de sospechosa >
foldA whatTF (const Hoja) arbolito (genA 1)
< Def de arbolito >
foldA whatTF (const Hoja) (Rama 'a' (Rama 'b' Hoja (Rama 'c' Hoja Hoja)) Hoja) (genA 1)
< Def de foldA >
whatTF 'a' (foldA whatTF (const Hoja) (Rama 'b' Hoja (Rama 'c' Hoja Hoja))) (foldA whatTF (const Hoja) Hoja) (genA 1)
< Def genA >
whatTF 'a' (foldA whatTF (const Hoja) (Rama 'b' Hoja (Rama 'c' Hoja Hoja))) (foldA whatTF (const Hoja) Hoja) (Rama 1 (genA 2)(genA 3))
< Def whatTF >
Rama ('a',1) ((foldA whatTF (const Hoja) (Rama 'b' Hoja (Rama 'c' Hoja Hoja))) (genA 2)) ((foldA whatTF (const Hoja) Hoja) (genA 3))
< Def foldA >
Rama ('a',1) ((whatTF 'b' (foldA whatTF (const Hoja) Hoja) (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)))) (genA 2)) ((foldA whatTF (const Hoja) Hoja) (genA 3))
< Def genA >
Rama ('a',1) ((whatTF 'b' (foldA whatTF (const Hoja) Hoja) (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)))) (Rama 2 (genA 3)(genA 4))) ((foldA whatTF (const Hoja) Hoja) (genA 3))
< Def whatTF >
Rama ('a',1) ((Rama ('b',2) ((foldA whatTF (const Hoja) Hoja) (genA 3) ) ((foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)) (genA 4)))) ((foldA whatTF (const Hoja) Hoja) (genA 3))
< Def foldA >
Rama ('a',1) ((Rama ('b',2) (const Hoja (genA 3) ) ((foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)) (genA 4)))) ((foldA whatTF (const Hoja) Hoja) (genA 3))
< Def const >
Rama ('a',1) ((Rama ('b',2) Hoja ((foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)) (genA 4)))) ((foldA whatTF (const Hoja) Hoja) (genA 3))
< Def foldA >
Rama ('a',1) ((Rama ('b',2) Hoja (whatTF 'c' (foldA whatTF (const Hoja) Hoja) (foldA whatTF (const Hoja) Hoja) (genA 4)))) ((foldA whatTF (const Hoja) Hoja) (genA 3))
< Def genA >
Rama ('a',1) ((Rama ('b',2) Hoja (whatTF 'c' (foldA whatTF (const Hoja) Hoja) (foldA whatTF (const Hoja) Hoja) (Rama 4 (genA 5) (genA 6))))) ((foldA whatTF (const Hoja) Hoja) (genA 3))
< Def whatTF >
Rama ('a',1) ((Rama ('b',2) Hoja (Rama ('c',4) ((foldA whatTF (const Hoja) Hoja) (genA 5)) ((foldA whatTF (const Hoja) Hoja) (genA 6)) ))) ((foldA whatTF (const Hoja) Hoja) (genA 3))
< Def foldA >
Rama ('a',1) ((Rama ('b',2) Hoja (Rama ('c',4) (const Hoja (genA 5)) ((foldA whatTF (const Hoja) Hoja) (genA 6)) ))) ((foldA whatTF (const Hoja) Hoja) (genA 3))
< Def const >
Rama ('a',1) ((Rama ('b',2) Hoja (Rama ('c',4) Hoja ((foldA whatTF (const Hoja) Hoja) (genA 6)) ))) ((foldA whatTF (const Hoja) Hoja) (genA 3))
< Def foldA >
Rama ('a',1) ((Rama ('b',2) Hoja (Rama ('c',4) Hoja (const Hoja (genA 6)) ))) ((foldA whatTF (const Hoja) Hoja) (genA 3))
< Def const >
Rama ('a',1) ((Rama ('b',2) Hoja (Rama ('c',4) Hoja Hoja ))) ((foldA whatTF (const Hoja) Hoja) (genA 3))
< Def foldA >
Rama ('a',1) ((Rama ('b',2) Hoja (Rama ('c',4) Hoja Hoja ))) (const Hoja (genA 3))
< Def const >
Rama ('a',1) (Rama ('b',2) Hoja (Rama ('c',4) Hoja Hoja )) Hoja
```

**c.ii Orden de evaluación aplicativo**
```
sospechosa arbolito (genA 1)
< Def. genA >
sospechosa arbolito Rama 1 (genA 2) (genA 2)
< Def. genA >
sospechosa arbolito Rama 1 (Rama 2) (Rama 2 (genA 3) (genA 4))
(...)
Entra en loop infinito.
```
