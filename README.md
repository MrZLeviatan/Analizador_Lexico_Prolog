![Tablero en blanco (9)](https://github.com/user-attachments/assets/f07a7cfd-b4b6-4f97-96de-75817aac1497)# Analizador Léxico para Prolog: Reconocimiento de Tokens mediante Autómatas Finitos Deterministas

## 📝 Introducción

Este repositorio contiene el diseño y la documentación detallada de un analizador léxico para el lenguaje de programación **Prolog**. El objetivo principal de este proyecto es demostrar cómo los **Autómatas Finitos Deterministas (AFD)** pueden ser empleados eficazmente para reconocer y clasificar los distintos tipos de tokens léxicos que componen el código fuente de Prolog.

Cada sección de este documento describe un token específico, incluyendo su definición formal, ejemplos válidos, los símbolos utilizados en su AFD correspondiente, una explicación del funcionamiento del autómata, y observaciones relevantes sobre su comportamiento y diseño.

**Nota Importante:** Para optimizar la claridad visual de los diagramas y cumplir con las métricas del proyecto, **los estados sumidero (o estados trampa) han sido omitidos en las representaciones gráficas de los AFD.** La ausencia de una transición explícita para un determinado símbolo de entrada desde un estado particular implica que la cadena de entrada conduciría implícitamente a un estado sumidero, resultando en el rechazo de dicha cadena.

## 📦 Estructura del Repositorio

* `README.md`: Este documento principal que describe el proyecto.
* `docs/`: (Opcional) Carpeta que contendría la versión formal de este documento en un formato como PDF o DOCX.
* `img/`: Carpeta que contendrá todos los diagramas de los AFDs correspondientes a cada token. Asegúrate de que los nombres de archivo coincidan con los que se usan en las referencias de este README.
* `src/`: (Opcional) Carpeta donde se ubicará el código fuente de tu analizador léxico en Python.

## ✨ Tokens Reconocidos y su Diseño mediante AFD

---

### 1. Token: Números Naturales

**Descripción:**
Los números naturales en Prolog están formados únicamente por dígitos del 0 al 9. El autómata diseñado para este token es capaz de reconocer secuencias de uno o más dígitos.

**Ejemplos válidos:** `0`, `7`, `123`, `999`

**Símbolos utilizados:**
* `D`: representa cualquier dígito del 0 al 9 (es decir: `0|1|2|3|4|5|6|7|8|9`).

**Explicación del AFD:**
El autómata comienza su procesamiento en el estado inicial.
1.  Si se recibe un dígito (`D`), transita inmediatamente a un estado de aceptación.
2.  Desde este estado de aceptación, existe un bucle sobre el símbolo `D` que permite al autómata seguir leyendo más dígitos consecutivos.
Este diseño permite aceptar tanto un único dígito (como `7`) como secuencias numéricas extensas (como `123456`).

**Observaciones:**
* No se permite el signo `+` o `-` al inicio de los números naturales.
* No se aceptan decimales ni letras ni cualquier otro tipo de caracteres.

**AFD Números Naturales:**
![AFD Números Naturales](https://github.com/user-attachments/assets/4beb52dc-4dd8-4ae0-bda4-4c0934061261))

---

### 2. Token: Números Reales

**Descripción:**
Los números reales en Prolog están formados por una parte entera (secuencia de dígitos), seguida obligatoriamente de un punto decimal, y finalmente una parte decimal (también una secuencia de dígitos). Es indispensable que ambos lados del punto contengan al menos un dígito.

**Ejemplos válidos:** `3.14`, `0.5`, `12.0`

**Símbolos utilizados:**
* `D`: representa cualquier dígito del 0 al 9.
* `.`: representa el punto decimal obligatorio.

**Explicación del AFD:**
El autómata inicia leyendo un dígito (`D`) y permite una o más repeticiones para formar la parte entera del número.
1.  Luego, al recibir el punto (`.`), cambia a un nuevo estado intermedio.
2.  Después del punto, es obligatorio que lea al menos un dígito (`D`) para formar la parte decimal, transitando a un estado de aceptación.
3.  Desde este estado de aceptación, un bucle sobre `D` permite la lectura de más dígitos decimales.

**Observaciones:**
* El número real debe tener sí o sí una parte decimal; no se aceptan entradas como `3.` o `12.`.
* No se acepta el uso de coma `,` como separador decimal.
* No se permiten signos (`+` o `-`) ni notación exponencial (`E`, `e`, etc.).

**AFD Números Reales:**
![AFD Números Reales](https://github.com/user-attachments/assets/6f346b4d-ac3b-4721-9278-1e8af9eb949c)
 )

---

### 3. Token: Identificadores (Variables y Átomos en Prolog)

**Descripción general:**
En el lenguaje Prolog, los identificadores se clasifican en dos categorías principales: **átomos** y **variables**, cada una con sus propias reglas de escritura. Ambos tipos de identificadores comparten la restricción de una longitud máxima de 10 caracteres y solo pueden contener letras, dígitos o guiones bajos (`_`). La distinción fundamental radica en el primer carácter permitido.

#### 3.1 Variables

**Descripción:** Las variables en Prolog inician su nombre con una letra mayúscula (A-Z) o con el guión bajo (`_`). Pueden estar seguidas por cualquier combinación de letras (A-Z, a-z), dígitos (0-9) o más guiones bajos. Es crucial que la longitud total del identificador no exceda los 10 caracteres.

**Ejemplos válidos:** `X`, `Persona1`, `_temp`

**Símbolos Utilizados en el AFD:**
* `Lmay`: Letra mayúscula (A-Z)
* `D`: Dígito decimal (0-9)
* `_`: Guión bajo
* `L`: Cualquier letra (mayúscula o minúscula)

**Explicación del AFD:**
El autómata para variables está diseñado para:
1.  Comenzar reconociendo una letra mayúscula (`Lmay`) o un guión bajo (`_`).
2.  Posteriormente, acepta hasta 9 caracteres adicionales que pueden ser letras (`L`), dígitos (`D`) o guiones bajos (`_`), mediante transiciones secuenciales que garantizan el límite de longitud.
El AFD se detiene al alcanzar el décimo carácter, asegurando que la longitud máxima no sea excedida.

**AFD Variables:**
![AFD Variables](https://github.com/user-attachments/assets/9b8b70a1-f264-4b7b-a5a4-f89a99c27224)


#### 3.2 Átomos

**Descripción:** Los átomos en Prolog inician con una letra minúscula (a-z), y pueden estar seguidos por cualquier combinación de letras, dígitos o guiones bajos (`_`). Al igual que las variables, el identificador de un átomo debe tener un máximo de 10 caracteres.

**Ejemplos válidos:** `persona`, `dato_1`, `colorRojo`

**Símbolos Utilizados en el AFD:**
* `Lmin`: Letra minúscula (a-z)
* `D`: Dígito decimal (0-9)
* `_`: Guión bajo
* `L`: Cualquier letra (mayúscula o minúscula)

**Explicación del AFD:**
El autómata para átomos está diseñado para:
1.  Comenzar reconociendo una letra minúscula (`Lmin`).
2.  Luego, acepta hasta 9 caracteres adicionales que pueden ser letras (`L`), dígitos (`D`) o guiones bajos (`_`), con transiciones que limitan la longitud total.
El AFD considera transiciones entre estados que garantizan que el límite de 10 caracteres no sea excedido, aceptando el átomo al llegar a cualquier estado final dentro de ese límite.

**AFD Átomos:**
![AFD Átomos](https://github.com/user-attachments/assets/7ab58363-3abb-42fc-8bfc-5c796157bff6)


**Observaciones:**
* Ambos tipos de identificadores (variables y átomos) no deben superar los 10 caracteres de longitud.
* La diferencia más importante en su reconocimiento radica en el primer carácter: mayúscula o guión bajo para variables, y minúscula para átomos.
* Este diseño de AFD permite una validación estricta de los tokens de identificadores en compiladores o analizadores léxicos para Prolog.
* Los múltiples caminos alternativos en los AFDs demuestran que no hay un único recorrido válido, sino diversas combinaciones de caracteres que pueden formar un identificador válido.

---

### 4. Token: Palabras Reservadas

**Descripción:** En Prolog, existen ciertas palabras que tienen un significado especial y predefinido dentro del lenguaje, lo que impide que sean utilizadas como identificadores (nombres de variables o átomos). Estas **palabras reservadas** se reconocen como tokens únicos y fijos. Debido a su secuencia fija de caracteres, cada una puede representarse eficientemente mediante su propio Autómata Finito Determinista (AFD).

**Palabras reservadas reconocidas por el lenguaje:**
* `is`
* `not`
* `fail`
* `true`
* `false`
* `assert`

#### 4.1 AFD Individual por Palabra

Cada palabra reservada se representa por un AFD lineal que valida una secuencia específica de letras, carácter por carácter.
El AFD para cada palabra reservada se compone de transiciones secuenciales que siguen el orden exacto de las letras que la forman. Si en cualquier punto de la secuencia se presenta un carácter incorrecto, un carácter adicional, o la secuencia no se completa, el token no es reconocido como una palabra reservada.

**Ejemplos inválidos (por contener errores o cambios):**
* `Is` (no es válida, inicia con mayúscula)
* `not_` (no es válida, contiene un carácter adicional)
* `faill` (no es válida, contiene una letra de más)

**Explicación del AFD general:**
Cada palabra reservada tiene un AFD que es una cadena lineal de estados, donde cada transición corresponde a una letra específica de la palabra en su orden exacto. El reconocimiento exitoso de la palabra reservada termina en un estado final una vez que se han recorrido todas sus letras correctamente y no hay más caracteres a continuación.
Estos autómatas son inherentemente simples, ya que no permiten repeticiones, bucles, ni la presencia de caracteres adicionales que alteren la secuencia. Su principal utilidad es asegurar que el token reconocido sea exactamente idéntico a la palabra clave predefinida.

**Observaciones:**
* Las palabras reservadas son elementos inmutables del lenguaje y no se pueden redefinir ni usar como nombres de variables o átomos definidos por el usuario en Prolog.
* Al no aceptar variaciones ni sufijos, su detección debe ser exacta y sin ambigüedad por parte del analizador léxico.
* Son esenciales para el funcionamiento del lenguaje y, por lo tanto, deben tener prioridad en el proceso de análisis léxico sobre otros posibles tokens como los identificadores.

**AFD Palabras Reservadas:**
*(Aquí deberías insertar los diagramas de los AFDs para cada palabra reservada. Ejemplos de nombres de archivo sugeridos: `img/afd_is.png`, `img/afd_not.png`, `img/afd_fail.png`, etc.)*
![AFD Palabras Reservadas](https://github.com/user-attachments/assets/68a9a658-a6ee-4942-a51d-438aba54f256)


---

### 5. Token: Operadores Aritméticos

**Descripción:**
En Prolog, los operadores aritméticos se utilizan para realizar cálculos matemáticos. La mayoría de estos operadores son símbolos de un solo carácter (`+`, `-`, `*`, `/`), con la notable excepción de `mod`, que es una palabra reservada compuesta por tres letras.
Durante la fase de análisis léxico, estos operadores se reconocen como tokens individuales, asegurando su correcta separación de operandos o variables.

**Operadores reconocidos:**
* `+` (suma)
* `-` (resta o negación)
* `*` (multiplicación)
* `/` (división)
* `mod` (módulo)

**AFD simplificado para los operadores de un solo carácter:**
Para `+`, `-`, `*`, `/`:
Estos operadores se reconocen directamente desde el estado inicial con una sola transición, llevando a un estado de aceptación que significa el reconocimiento inmediato del token tras leer el símbolo.

**AFD para `mod`:**
Dado que `mod` es una palabra de tres caracteres, requiere su propio AFD secuencial que verifica cada letra. Este autómata reconoce únicamente la secuencia exacta "m" → "o" → "d". Si se presenta alguna letra incorrecta o extra, la secuencia no se acepta como el operador `mod`.

**Ejemplos válidos:** `X + Y`, `5 * 3`, `mod(10, 3)`, `Z / 2`, `-7`

**Ejemplos inválidos:** `++` (no es un operador definido), `mo_d` (no válido como operador, podría confundirse con un átomo), `mod1` (no se reconoce como operador aritmético).

**Explicación del AFD:**
Los operadores de un solo carácter (`+`, `-`, `*`, `/`) son reconocidos de forma instantánea al leer el símbolo correspondiente desde el estado inicial.
El operador `mod`, al ser una palabra, requiere un AFD que verifica letra por letra de manera secuencial. Solo si se reconoce la secuencia exacta "m" → "o" → "d" se llega al estado de aceptación para este token.

**Observaciones:**
* El operador `mod` es tratado como una palabra reservada especial dentro de la categoría de operadores aritméticos.
* Estos operadores pueden aparecer tanto de forma aislada como integrados en expresiones aritméticas complejas, por lo que su correcta y clara separación en la fase de análisis léxico es fundamental.

**AFD Operador Aritmético MOD:**
![AFD Operador Aritmético MOD](https://github.com/user-attachments/assets/aa01c371-a730-476d-ab13-5618d0f8e257)


**AFD Operadores Aritméticos (Simples):**
![AFD Operadores Aritméticos](https://github.com/user-attachments/assets/3800cf0c-0326-4803-b64c-7cad58904183)
 

---

### 6. Token: Operadores de Comparación

**Descripción:**
En Prolog, los operadores de comparación permiten establecer y verificar relaciones entre términos o valores. Estos se clasifican en operadores de igualdad estructural (`==`, `\==`), relacionales (`<`, `>`, `=<`, `>=`), y aritméticos (`=:=`, `=\=`). Son símbolos que pueden consistir en una combinación de uno, dos o tres caracteres, utilizando símbolos como `=`, `<`, `>`, `-`, `:`, `/`.

**Lista de operadores válidos considerados:**
* `==` → Igualdad estructural (unificación estricta)
* `\==` → No igualdad estructural (no unificación estricta)
* `<` → Menor que
* `>` → Mayor que
* `=<` → Menor o igual
* `>=` → Mayor o igual
* `=:=` → Igualdad aritmética (evalúa y compara valores)
* `=\=` → Desigualdad aritmética (evalúa y compara valores)

**Ejemplos válidos:** `X == Y`, `A \== B`, `Valor < 10`, `Edad >= 18`, `5 =:= 2+3`, `10 =\= 2*5+1`

**Explicación del AFD:**
El autómata para los operadores de comparación parte de un estado inicial y se bifurca inteligentemente según el primer símbolo leído, para manejar las posibles secuencias:
* Si se lee un `=`, puede continuar con otro `=` (`==`), con `:` seguido de `=` (`=:=`), o con `/` seguido de `=` (`=\=`).
* Si el primer símbolo es `<` o `>`, el autómata puede aceptar directamente como operador simple (si no hay más caracteres), o si va seguido de `=`, se reconocen como `=<` o `>=` respectivamente.
* Si el primer símbolo es `-`, seguido de `==`, se acepta el operador `-==` (no estándar en Prolog, pero incluido en este conjunto).
Cada combinación de símbolos que forma un operador válido lleva a un estado final de aceptación. Las secuencias de caracteres que no corresponden a ningún operador válido no alcanzan un estado final, lo que garantiza una validación estricta.

**Observaciones:**
* Los operadores de comparación en este conjunto pueden tener hasta 3 caracteres, lo que requiere que el analizador léxico procese secuencias de esa longitud para su correcta identificación.
* El operador `-==` (No igualdad estructural) se ha incluido como parte del lenguaje reconocido, aunque es importante notar que no forma parte del estándar ISO Prolog.
* El autómata fue diseñado para permitir un reconocimiento eficiente y sin ambigüedades, estructurándose lógicamente a partir de los símbolos iniciales esperados (`=`, `<`, `>`, `-`).

**AFD Operadores de Comparación:**
![AFD Operadores de Comparación](https://github.com/user-attachments/assets/92d6a9a1-2fae-4065-8c1c-67207b7fe630)
 

---

### 7. Token: Operadores Lógicos

**Descripción:**
En Prolog, los operadores lógicos son fundamentales para construir expresiones complejas y definir las condiciones en las reglas. Permiten establecer relaciones entre diferentes condiciones o metas. Los principales operadores lógicos considerados en este proyecto son:

* `,` → Conjunción (AND lógico, "y")
* `;` → Disyunción (OR lógico, "o")
* `not` → Negación (como predicado o operador de prefijo)
* `->` → Implicación (análogo a "si-entonces")

**Ejemplos válidos:** `a, b` (a y b), `a ; b` (a o b), `not(X > 5)` (no es cierto que X sea mayor que 5), `condición -> acción` (si condición, entonces acción).

**Explicación del AFD:**
El AFD para operadores lógicos está diseñado para reconocer los distintos patrones:
* Los operadores de un solo carácter como `,` y `;` se reconocen directamente desde el estado inicial con una única transición a un estado final de aceptación.
* El operador `->` requiere una secuencia específica de dos símbolos: primero lee el guión (`-`) y luego el signo mayor (`>`), siguiendo una transición secuencial de dos estados hasta el estado final.
* El operador `not` es una palabra reservada, por lo tanto, su AFD lee secuencialmente la `n`, luego la `o` y finalmente la `t`, alcanzando un estado final solo si la secuencia completa `not` es reconocida exactamente.

**Observaciones:**
* Aunque `not` es un operador lógico, se comporta como un predicado en Prolog y su reconocimiento léxico comparte la estructura de los AFDs de palabras reservadas.
* Los operadores de un solo símbolo (`,` y `;`) y el operador `->` pueden ser agrupados lógicamente en un mismo AFD debido a sus patrones de reconocimiento simples y directos, que se distinguen por el carácter inicial.

**AFD Operadores Lógicos (General):**
![AFD Operadores Lógicos](https://github.com/user-attachments/assets/1a378fff-8d8b-4f42-9d30-879bf50b6c4a)


**AFD Operador Lógico “not”:**
![AFD Operador Lógico not](https://github.com/user-attachments/assets/b937bad9-ef56-4bd1-879b-da06f678a1da)




---

### 8. Token: Operadores de Asignación

**Descripción:**
En Prolog, el principal operador utilizado para la "asignación" (más precisamente, la evaluación aritmética y unificación de un resultado con una variable) es `is`. Es un operador clave que distingue a Prolog de otros lenguajes imperativos en la forma de manejar valores.

**Ejemplos válidos:** `X is 5 + 2.`, `Resultado is A + B.`

**Explicación del AFD:**
El operador `is` se trata como una palabra clave y, por lo tanto, necesita un AFD secuencial específico para su reconocimiento:
1.  El autómata comienza en un estado inicial.
2.  Acepta una `i` como primer carácter y transita a un segundo estado.
3.  Desde este segundo estado, transiciona a un tercer estado de aceptación si se reconoce la letra `s`.
Solo si la secuencia completa `i` → `s` es detectada, se alcanza el estado final de aceptación, reconociendo el token `is`.
Este AFD es muy similar en estructura a los AFDs de otras palabras reservadas como `mod` o `not`, ya que se basa en la validación exacta de una cadena específica de caracteres.

**Observaciones:**
* A diferencia de los operadores simbólicos de un solo carácter, `is` no puede agruparse directamente con ellos, ya que requiere un AFD secuencial con validación exacta de caracteres.
* Es fundamental no confundir el operador `is` con los operadores de comparación de igualdad (`=`, `==`, `=:=`), ya que su comportamiento y propósito en Prolog son fundamentalmente diferentes: `is` evalúa una expresión aritmética y unifica el resultado, mientras que los operadores de comparación verifican relaciones entre términos o valores.

**AFD Operadores de Asignación (is):**
![AFD Operador de Asignación (is)](https://github.com/user-attachments/assets/8735b4fc-7ba9-460d-9663-d54754ef4082)


---

### 9. Token: Operadores de Incremento/Decremento

**Descripción:**
A diferencia de lenguajes de programación imperativos como C, Java o Python, Prolog **no posee operadores de incremento (`++`) ni de decremento (`--`)** predefinidos. La naturaleza declarativa y lógica de Prolog, donde las variables representan valores unificados que no "cambian" en el sentido imperativo, hace que este tipo de operación no aplique directamente a su paradigma.

**Ejemplos inválidos:** `X++.`, `--Y.`
(Estos ejemplos no son válidos en Prolog y, si se intentan usar, generarán errores de sintaxis o de predicado no definido.)

**Explicación del AFD:**
Dado que los operadores de incremento y decremento (`++`, `--`) no forman parte del lenguaje estándar de Prolog, **no se diseña un AFD específico para su reconocimiento como tokens válidos**. Cualquier secuencia de caracteres que se asemeje a estos operadores debe ser considerada como un token inválido o un error léxico dentro del analizador, lo que llevaría al analizador a un estado sumidero implícito.

---

### 10. Token: Paréntesis

**Descripción:**
En Prolog, los paréntesis (`(` y `)`) son símbolos esenciales que cumplen múltiples funciones sintácticas: agrupar expresiones (tanto aritméticas como lógicas) para controlar la precedencia, y delimitar los argumentos de predicados compuestos o funciones.

**Los símbolos reconocidos son:**
* `(` → paréntesis de apertura
* `)` → paréntesis de cierre

**Ejemplos válidos:**
* `(3 + 2) * 5`
* `padre(juan, (hijo(maria)))`
* `not((X =:= Y))`

**Explicación del AFD:**
El reconocimiento de los paréntesis en la fase léxica es directo y sencillo:
1.  Desde el estado inicial, si se recibe el símbolo `(`, se transita inmediatamente a un estado de aceptación.
2.  De manera análoga, si desde el estado inicial se recibe el símbolo `)`, también se transita directamente a un estado de aceptación.
Ambos paréntesis se reconocen como tokens individuales y atómicos, sin requerir secuencias múltiples de transiciones como en el caso de palabras clave o identificadores. Por lo tanto, cada uno tiene su propio camino simple y directo en el AFD desde el estado inicial (`q0`) hacia un estado de aceptación.

**Observaciones:**
* Aunque los paréntesis no tienen un significado matemático intrínseco o de acción por sí mismos, su uso es crucial en Prolog para establecer la precedencia de operadores y la estructura lógica de los términos y expresiones.
* Es responsabilidad de la siguiente fase del compilador, el analizador sintáctico, asegurar el balanceo correcto de los paréntesis (que cada paréntesis de apertura tenga su correspondiente cierre). El analizador léxico solo se encarga de reconocer los tokens individuales.

**AFD Paréntesis:**
![AFD Paréntesis](https://github.com/user-attachments/assets/9a548ba2-9738-4d3a-a21d-3c4c9af04daa)


---

### 11. Token: Llaves

**Descripción:**
En Prolog, las llaves (`{` y `}`) se utilizan en contextos específicos, aunque su frecuencia de uso no es tan alta como la de los paréntesis. Sirven para delimitar ciertos objetos de evaluación o bloques de código dentro de construcciones más avanzadas o definidas por el usuario. Forman parte del conjunto de símbolos válidos en la sintaxis de Prolog.

**Los símbolos reconocidos son:**
* `{` → llave de apertura
* `}` → llave de cierre

**Ejemplos válidos:**
* `{X = 5}` (común en SWI-Prolog para evaluar metas)
* `predicado({a, b, c})`

**Explicación del AFD:**
El análisis léxico de las llaves es directo y sencillo, similar al de los paréntesis:
1.  Desde el estado inicial, si se recibe el carácter `{`, el autómata transita inmediatamente a un estado de aceptación.
2.  De la misma manera, si se recibe el carácter `}`, se transita directamente a un estado de aceptación.
Ambos son reconocidos como tokens individuales. El AFD no requiere múltiples estados ni validaciones complejas para su identificación.

**Observaciones:**
* A diferencia de otros lenguajes (como C o Java), las llaves en Prolog no representan estructuras de control de flujo (como bucles o condicionales), pero su uso es válido en ciertas construcciones o extensiones definidas por el programador o por algunas bibliotecas del lenguaje.
* Al igual que con los paréntesis, es responsabilidad del analizador sintáctico validar que las llaves están correctamente balanceadas en el código fuente.

**AFD Llaves:**
![AFD Llaves](https://github.com/user-attachments/assets/98ad26da-1ed5-47c3-877c-97fa9d726455)


---

### 12. Token: Terminal (fin de sentencia)

**Descripción:**
En Prolog, cada sentencia o cláusula lógica (ya sea un hecho, una regla o una consulta) debe finalizar con un punto (`.`). Este símbolo es crucial porque indica al intérprete que una instrucción completa ha terminado y que puede proceder a su evaluación. Es un elemento obligatorio y fundamental de la sintaxis básica del lenguaje.

**Ejemplos válidos:**
* `padre(juan, maria).`
* `X is 5.`
* `true.`

**Explicación del AFD:**
El AFD para reconocer el token de terminal (`.`) es sumamente simple:
Desde el estado inicial, si se recibe el carácter `.` (punto), el autómata transita inmediatamente a un estado de aceptación.
Este AFD no requiere estados adicionales ni transiciones complejas, ya que el punto es un símbolo único que se reconoce de forma directa como un token finalizador de sentencia.

**Observaciones:**
* La omisión del punto al final de una sentencia es un error de sintaxis común en Prolog; si no se coloca, el intérprete esperará que el usuario complete la instrucción.
* Es una buena práctica de programación y puede ayudar al analizador léxico a evitar ambigüedades, si se usa un espacio o un salto de línea después del punto que finaliza una sentencia.

**AFD Terminal (fin de sentencia):**
![AFD Terminal (fin de sentencia)](https://github.com/user-attachments/assets/23f7f036-0a9f-44ba-b1ef-aa92772057ab)


---

### 13. Token: Separador (Coma)

**Descripción:**
En Prolog, la coma (`,`) es un símbolo versátil que actúa como separador en diversos contextos sintácticos del lenguaje. Su función es crucial para estructurar elementos en diferentes construcciones:
* **Separar elementos en una lista:** Por ejemplo, `[a, b, c]`.
* **Separar argumentos en predicados:** Por ejemplo, `padre(juan, maria)`.
* **Expresar conjunciones en reglas y consultas:** Por ejemplo, `hombre(X), humano(X)`.

**Ejemplos válidos:**
* `padre(juan, maria).`
* `lista([1, 2, 3]).`
* `hombre(X), humano(X).`

**Explicación del AFD:**
El autómata para reconocer el token coma es extremadamente simple:
Desde el estado inicial `q0`, si se detecta el carácter `,` (coma), el autómata transita directamente a un estado de aceptación.
No requiere más transiciones ni condiciones adicionales, ya que la coma es un símbolo único y directamente reconocible.

**Observaciones:**
* Aunque la coma también aparece en contextos de conjunciones lógicas, su tratamiento léxico no cambia; sigue siendo el mismo símbolo que se tokeniza como tal.
* El significado semántico y el rol de la coma (si es un separador de argumentos o un operador de conjunción) se interpretan en la fase de análisis sintáctico (parsing), dependiendo del contexto gramatical en el que aparezca.

**AFD Separador (Coma):**
![AFD Separador (Coma)](https://github.com/user-attachments/assets/79b9a9ac-c47e-4371-ad2b-893aa94880cc)


---

### 14. Token: Cadenas de Caracteres

**Descripción:**
En Prolog, las cadenas de caracteres son secuencias de símbolos encerradas entre comillas dobles (`"`). Estas cadenas pueden contener una amplia variedad de caracteres ASCII estándar, así como secuencias de escape especiales iniciadas por una barra invertida (`\`) para representar caracteres que no pueden ser escritos directamente (como nuevas líneas o las propias comillas dobles).

**Las secuencias de escape válidas consideradas son:**
* `\n` (nueva línea)
* `\t` (tabulador)
* `\\` (barra invertida literal)
* `\"` (comillas dobles literal)

**Ejemplos válidos:**
* `"hola mundo"`
* `"linea\nnueva"` (contiene un salto de línea)
* `"Ruta: C:\\Archivos\\"`
* `"Contenido con \"comillas\""`

**Símbolos utilizados:**
* `ASCII`: representa cualquier carácter del conjunto estándar de códigos ASCII, es decir, cualquier símbolo válido que pueda ser procesado por el autómata, como letras, números, signos de puntuación y caracteres especiales (excluyendo la comilla doble `"` y la barra invertida `\` cuando no es el inicio de una secuencia de escape).
* `C`: representa un carácter de secuencia de escape válido (es decir, `n`, `t`, `\`, `"`).

**Explicación del AFD:**
El AFD para cadenas de caracteres está diseñado para:
1.  Comenzar en el estado inicial, esperando la comilla doble (`"`) de apertura.
2.  Una vez abierta la cadena, transita a un estado de lectura general que acepta cualquier carácter `ASCII` válido. Este estado tiene un bucle de auto-transición para permitir múltiples caracteres en la cadena.
3.  Si se encuentra una barra invertida (`\`), transita a un estado intermedio que espera una secuencia de escape válida (`C`) (como `n`, `t`, `\`, `"`).
4.  Tras reconocer un carácter de secuencia de escape válido, el autómata regresa al estado de lectura general para continuar procesando el resto de la cadena.
5.  Finalmente, si se encuentra otra comilla doble (`"`), el autómata transita al estado de aceptación, indicando que la cadena ha finalizado correctamente.

**Observaciones:**
* Si una cadena no cierra con la comilla doble (`"`) de cierre, o si se detecta una secuencia de escape no válida, la cadena no será aceptada como un token.
* Las cadenas de caracteres, encerradas entre comillas dobles, son léxicamente distintas de los átomos que a veces se escriben entre comillas simples (`'texto'`), aunque visualmente puedan parecer similares.
* La fase léxica es la encargada de distinguir correctamente las cadenas de caracteres gracias a la comilla doble inicial y su manejo de las secuencias de escape.

**AFD Cadenas de Caracteres:**
![AFD Cadenas de Caracteres](https://github.com/user-attachments/assets/8444abce-cb1f-4f76-8145-c1313cffcf4b)


---

### 15. Token: Comentarios

**Descripción general:**
En el lenguaje Prolog, los comentarios son porciones de texto completamente ignoradas por el intérprete durante el procesamiento del código. Su principal función es mejorar la legibilidad y la documentación del programa, permitiendo a los programadores añadir explicaciones, notas o deshabilitar temporalmente secciones de código. Prolog soporta dos tipos principales de comentarios: de línea y de bloque.

#### 15.1 Tipos de Comentarios

#### 15.1.1 Comentarios de Línea (`%`)

**Descripción:** Los comentarios de línea comienzan con el símbolo de porcentaje (`%`) y se extienden hasta el final de la línea actual. Cualquier texto que se encuentre después del `%` en esa misma línea será considerado un comentario y no será procesado por el analizador.

**Ejemplos válidos:**
* `% Esto es un comentario que ocupa una línea completa.`
* `mi_hecho. % Comentario al final de una línea de código.`
* `%_variable_temporal = 10.`

**Símbolos utilizados:**
* `%`: Carácter que marca el inicio del comentario de línea.
* `ASCII`: Representa cualquier carácter válido dentro del conjunto ASCII (incluyendo letras, números, símbolos y espacios), excepto el carácter de nueva línea (`\n`).
* `\n`: Carácter de nueva línea (salto de línea), que indica el fin del comentario de línea.

**Explicación del AFD:**
El Autómata Finito Determinista (AFD) para reconocer comentarios de línea opera de la siguiente manera:
1.  Inicia en un estado inicial.
2.  Al leer el carácter `%`, transita a un estado intermedio.
3.  Desde este estado intermedio, el AFD puede consumir cero o más caracteres `ASCII` (lo que permite el cuerpo del comentario), representado por un bucle de auto-transición etiquetado como `ASCII`.
4.  Finalmente, para alcanzar el estado de aceptación, el AFD debe leer el carácter de nueva línea (`\n`), lo que señala el final del comentario de línea.

**AFD Comentario de Línea:**
![AFD Comentario de Línea](https://github.com/user-attachments/assets/f1f68aa3-8e65-4bf4-8784-6edffbf0b7e0)


#### 15.1.2 Comentarios de Bloque (`/* ... */`)

**Descripción:** Los comentarios de bloque, también conocidos como comentarios multi-línea, se utilizan para comentar secciones de código que abarcan una o más líneas. Comienzan con la secuencia de caracteres `/*` y terminan con la secuencia `*/`. Todo el texto encerrado entre estos delimitadores es ignorado por el analizador.

**Ejemplos válidos:**
* `/* Este es un comentario`
    `   que se extiende por varias líneas.`
    `   Puede incluir símbolos y espacios. */`
* `otra_clausula. /* Comentario corto */`

**Símbolos utilizados:**
* `/`: Carácter utilizado en la secuencia de apertura y cierre del comentario de bloque.
* `*`: Carácter utilizado en la secuencia de apertura y cierre del comentario de bloque.
* `ASCII`: Representa cualquier carácter válido dentro del conjunto ASCII que forma el contenido del comentario, incluyendo el carácter `*` si no es parte de la secuencia de cierre `*/`.

**Explicación del AFD:**
El AFD para reconocer comentarios de bloque funciona de la siguiente manera:
1.  Comienza en un estado inicial.
2.  Transita a un segundo estado al leer el carácter `/`.
3.  Desde el segundo estado, transita a un tercer estado al leer el carácter `*`, completando así la secuencia de apertura `/*`.
4.  Este tercer estado representa el cuerpo del comentario y tiene una auto-transición etiquetada como `ASCII`, lo que permite consumir cualquier carácter dentro del bloque de comentario.
5.  Desde este tercer estado, debe leer un `*` para transitar a un cuarto estado (que es un estado potencial de cierre).
6.  Finalmente, desde este cuarto estado, debe leer un `/` para alcanzar el estado final de aceptación (doble círculo), cerrando la secuencia `*/`.

**AFD Comentario de Bloque:**
![AFD Comentario de Bloque](https://github.com/user-attachments/assets/964ca6b3-c056-4e76-926e-010c5333299b)


**Observaciones:**
* Ambos tipos de comentarios son cruciales para la documentación y organización del código fuente, haciendo que el programa sea más comprensible para los desarrolladores sin afectar su ejecución.
* Los AFDs ilustran cómo un analizador léxico identifica las secuencias de inicio y fin de los comentarios para poder ignorar el texto intermedio durante el procesamiento.
* Es importante destacar que en la mayoría de las implementaciones estándar de Prolog, los comentarios de bloque (`/* ... */`) **no permiten anidamiento**. Esto significa que si un `/*` aparece dentro de un comentario de bloque ya abierto, será tratado como parte del contenido del comentario hasta que se encuentre el primer `*/` de cierre. El AFD presentado refleja este comportamiento al no tener una lógica que permita el anidamiento recursivo.

---
