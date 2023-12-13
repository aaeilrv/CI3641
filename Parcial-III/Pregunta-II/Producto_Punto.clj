(defn producto-punto [vector1 vector2]
  (let [producto-parcial (pmap * vector1 vector2)]
    (reduce + producto-parcial)))

(def vector1 [1 2 3])
(def vector2 [4 -5 6])

(println "Producto Punto:" (producto-punto vector1 vector2))

(shutdown-agents)