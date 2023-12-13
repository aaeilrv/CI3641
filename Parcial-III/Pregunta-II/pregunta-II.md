
# Clojure
Uno de los objetivos de diseño de Clojure es la programación concurrente.
La decisión clave de diseño fue hacer que las estructuras de datos de Clojure fueran inmutables (persistentes) y separar los conceptos de identidad y valor. Los valores inmutables pueden compartirse de manera segura entre hilos y eliminan peligros de concurrencia.
La separación entre identidad y valor hace que las mutaciones de estado sean posibles de maneras que tienen garantías conocidas con respecto a la concurrencia. Esto elimina la necesidad de utilizar explícitamente bloqueos, que son posibles en Clojure pero generalmente no son necesarios. 

1. Diga si su lenguaje provee capacidades nativas para concurrencia, usa librerías o depende de herramientas externas.

Clojure proporciona un conjunto completo de características de concurrencia propias (se explican más a profundidad en la próxima pregunta), pero en ciertos casos es mejor usar una clase existente de java.util.concurrent (j.u.c) -grupo de herramientas de concurrencia en el Java Development Kit- o construir una nueva abstracción sobre los bloques de construcción de j.u.c.

También utiliza la librería `core.async` que provee facilidades para la programación asíncrona y la comunicación a través de canales.

2. Explique la creación/manejo de tareas concurrentes, así como el control de la memoria compartida y/o pasaje de mensajes.

En Clojure se puede obtener concurrencia colocando las tareas en diferentes hilos de la JVM.

**Futuros**: los _futuros_ se usan para definir una tarea y colocarla en otro hilo sin requerir dicho resultado de forma inmediata. Los futuros se crean con el macro `futuro`

```Clojure
(future (Thread/sleep 4000) ; Hilo
        (println "Voy a imprimir después de 4s"))
(println "Imprimo inmediatamente")
```

`Thread/sleep` dice cuándo el hilo actual debe esperar y no hacer nada por un tiempo en milisegundos. Normalmente, si se evalua `Thread/sleep` en el REPL, no sería posible evaluar otras instrucciones hasta que el REPL termine de _dormir_, ya que el hilo ejecutando el REPL estará bloqueado. Sin embargo, `future` crea un nuevo hilo y lo coloca en cada expresión que se le pase en el nuevo hilo, incluyendo `Thread/sleep`, permitiendole al REPL continuar ejecutándose.

**Demoras**: las _demoras_ permiten definir una tarea sin tener que ejecutarla o requerir su resultado inmediatamente. Se crean con `delay`

```Clojure
(def jackson-5-delay
  (delay (let [message "Llámame y ahí estaré"] ; Delay
           (println "Primera ref:" message) ; Desfererencia
           message)))
```

En este caso nada se imprime, debido a que no hemos pedido que se evalúe  el `let`. Se puede evaluar una demora y obtener su resultado al desreferenciarlo o usando `force`. Esta palabra clave funciona igual que `deref`, de la forma que se comunica más claramente de que está haciéndose que una tarea inicie en vez de esperar a que finalice.

```Clojure
(force jackson-5-delay)
```

**Promesas**: las _promesas_ permiten expresar que se espera un resultado sin tener que definir la tarea que debería producirlo o cuándo la tarea debería ejecutarse. Se pueden crear promesas usando `promise` y entregar el resultado con `deliver`. Los output se obtienen al desreferenciar.

```Clojure
(def my-promise (promise)) ; Crear la promesa
(deliver my-promise (+ 1 2)) ;; Entrega de los valores
@my-promise -- ; Desreferencia 
; => 3
```
En este caso, se crea una promesa y luego se entrega un valor a ésta. Finalmente, el valor se obtiene luego de desreferenciarla. Al hacer una desreferenica se expresa que se quiere el resultado. También se puede hacer la desreferencia sin haber pasado un valor pero esto ocasionaría que el programa se bloquee hasta que la promesa sea entregada, igual que las _demoras_ y los _futuros_, eso sí, sólo se puede entregar un resultado a una promesa una vez.

Para el pasaje de mensajes, Clojure utiliza canales -por medio de la librería `core.async`- que son creados con la función `chan`. Tú puedes poner y tomar mensajes de un canal.
Los procesos esperan por la completación de poner-tomar. Es decir: 1) Cuando intentan poner o tomar un mensaje de un canal, esperan y no hacen nada hasta que la acción es exitosa. 2) Cuando la acción es exitosa, continúa ejecutándose.


3. Describa el mecanismo de sincronización que utiliza el lenguaje.
La sincronización se puede lograr a través de promesas, canales, `countdownwatch` de Java, `Phaser` de Java, entre otros.


(perdone el mal resumen, la información de clojure -y la sintaxis- es agobiante djasd :c)