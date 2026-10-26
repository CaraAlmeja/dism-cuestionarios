# Solucionario: DISM · T3.2 · Telefonía móvil

## 1. B) 9,17 km

D = R√(3N) = 2√21 ≈ 2×4,5826 = 9,17 km. D/R no tiene unidades; D sí se mide en kilómetros.

Fuente: Tema3-DISM-21.pdf, páginas PDF 21, 25.

Distractores:

- A) Es el valor numérico de D/R; falta multiplicar por el radio de 2 km.
- C) Multiplica N por R sin aplicar √(3N).
- D) Usa 3N×R y omite la raíz cuadrada.

## 2. D) Pérdida de la llamada en curso

El tema diferencia rechazar el inicio de una llamada nueva de cortar una llamada que ya existía. Por esa diferencia de impacto se puede dar prioridad a los traspasos.

Fuente: Tema3-DISM-21.pdf, páginas PDF 43.

Distractores:

- A) La necesidad de traspaso no crea por sí misma nuevos recursos.
- B) La comunicación del caso ya estaba establecida.
- C) Sin recursos ni alternativa no se garantiza la continuidad.

## 3. D) Aumentar la capacidad por unidad de superficie

Cell splitting facilita reutilizar recursos más veces en una zona, a costa de nuevos emplazamientos y mayor complejidad. No elimina interferencias ni movilidad.

Fuente: Tema3-DISM-21.pdf, páginas PDF 29.

Distractores:

- A) La división utiliza varias estaciones y radios menores, no una única antena más potente.
- B) La división requiere coordinar recursos y añade complejidad a la asignación.
- C) Las celdas menores pueden exigir más traspasos al desplazarse.

## 4. B) Se bloquea aunque haya canales de guarda libres

La reserva protege los traspasos y reduce cortes de llamadas existentes. Su coste es aumentar el bloqueo de nuevas llamadas al limitar sus canales disponibles.

Fuente: Tema3-DISM-21.pdf, páginas PDF 43–45.

Distractores:

- A) La política descrita no expulsa llamadas en curso.
- C) Los canales de guarda del caso son exclusivos para traspasos.
- D) Pedir una llamada nueva no la convierte en una comunicación ya en curso.

## 5. C) MCHO

MCHO es controlado por el móvil. No debe mezclarse el eje de quién decide con el de cómo se ejecuta la transición entre enlaces.

Fuente: Tema3-DISM-21.pdf, páginas PDF 41.

Distractores:

- A) Hard describe el orden de desconexión y conexión, no quién toma la decisión.
- B) En MAHO el móvil aporta medidas, pero decide la red.
- D) En NCHO la red realiza el control descrito.

## 6. C) Inter-celda, intra-BSC

Se cambia de celda dentro del mismo controlador, por lo que es un handover inter-celda e intra-BSC.

Fuente: Tema3-DISM-21.pdf, páginas PDF 36–40.

Distractores:

- A) Requeriría cambiar de BSC, que aquí se mantiene.
- B) En el intra-celda cambia el canal dentro de la misma celda, no la BTS.
- D) Requeriría cambiar de central MSC, no solo de BTS dentro de un BSC.

## 7. C) BSC

El Base Station Controller controla varias estaciones BTS. El MSC conecta y conmuta a un nivel superior. Este esquema se pregunta en su contexto GSM, no como arquitectura idéntica de 4G/5G.

Fuente: Tema3-DISM-21.pdf, páginas PDF 35–36.

Distractores:

- A) La BTS mantiene el enlace radio con los móviles de la celda.
- B) UE es el equipo del usuario, no el controlador de varias BTS.
- D) El MSC realiza conmutación y coordinación de mayor alcance; no es la estación radio.

## 8. D) 6 erlangs ofrecidos y 5,4 erlangs cursados

TO = 180×(2/60) = 6 E. TC = 6×(1−0,10) = 5,4 E. El tráfico perdido es 0,6 E. No se utiliza Erlang B.

Fuente: Tema3-DISM-21.pdf, páginas PDF 49–50, 54.

Distractores:

- A) Confunde el número de llamadas por hora con la ocupación media en erlangs.
- B) 0,6 es el tráfico perdido; el cursado es el 90 % del ofrecido.
- C) Introduce un factor dos adicional en el cálculo del tráfico.

## 9. A) 1/7

La fracción es 1/N = 1/7. El PDF también llama «factor» a N en otra diapositiva; aquí se explicita la definición para evitar ambigüedad.

Fuente: Tema3-DISM-21.pdf, páginas PDF 13, 16.

Distractores:

- B) Resta una celda sin que exista esa resta en el modelo.
- C) Es el complemento de 1/7 y corresponde a los canales que no recibe esa celda.
- D) Es el tamaño N del clúster, no la fracción 1/N solicitada.

## 10. B) 60 canales

K = T/N = 420/7 = 60 canales por celda. T ya está expresado en canales dúplex, por lo que no hay que dividir de nuevo entre dos.

Fuente: Tema3-DISM-21.pdf, páginas PDF 16–17.

Distractores:

- A) Divide entre 12, que no es el tamaño N indicado.
- C) Asigna el total del clúster a cada celda y omite el reparto.
- D) Multiplica T por N en lugar de dividirlo.

## 11. A) 165 canales

33 MHz = 33 000 kHz. Cada par dúplex ocupa 50 kHz: T = 33 000/50 = 660. Después K = 660/4 = 165.

Fuente: Tema3-DISM-21.pdf, páginas PDF 20.

Distractores:

- B) Olvida que cada canal dúplex utiliza dos canales simplex.
- C) Es el total de canales dúplex del sistema antes de repartir entre cuatro celdas.
- D) Cuenta canales simplex del sistema, sin formar pares ni dividir por N.

## 12. D) Hay nueve circuitos ocupados de media en ese intervalo

El tráfico cursado representa ocupación media de recursos. Puede superar un erlang en un grupo de varios circuitos, aunque un recurso individual no pueda estar ocupado más del 100 % del tiempo.

Fuente: Tema3-DISM-21.pdf, páginas PDF 49–51.

Distractores:

- A) La intensidad no es el número total de llamadas.
- B) Un circuito individual no atiende nueve llamadas simultáneas; el valor se refiere al grupo.
- C) El valor no es una tasa de llegadas; también depende de la duración.

## 13. B) Más canales por celda y más interferencia cocanal

K = T/N aumenta si baja N, pero D/R = √(3N) disminuye. Las celdas que reutilizan los canales quedan más cerca y la relación S/I empeora.

Fuente: Tema3-DISM-21.pdf, páginas PDF 21, 27–28.

Distractores:

- A) Eso describe el efecto de aumentar N.
- C) Ambos efectos están invertidos respecto a reducir N.
- D) Disminuir N acerca las celdas cocanal y empeora la interferencia.

## 14. A) Mide el móvil y decide la red

MAHO significa Mobile Assisted Handover: el móvil aporta medidas y la red decide. No debe confundirse asistencia con control completo por el terminal.

Fuente: Tema3-DISM-21.pdf, páginas PDF 41.

Distractores:

- B) Ese reparto corresponde al MCHO descrito.
- C) Invierte los papeles del esquema MAHO.
- D) Ese reparto corresponde al NCHO descrito.

## 15. A) 10 erlangs

El volumen es 600×3 = 1800 minutos de llamada. La intensidad es 1800/180 = 10 erlangs, equivalente a diez circuitos ocupados de media.

Fuente: Tema3-DISM-21.pdf, páginas PDF 49, 56.

Distractores:

- B) Divide por una hora cuando el intervalo observado son tres horas.
- C) Confunde el número de llamadas con la ocupación media de circuitos.
- D) Es el volumen en minutos de llamada, sin dividir entre los 180 minutos observados.

## 16. B) 12

(D/R)² = 3N. Por tanto N = 6²/3 = 36/3 = 12.

Fuente: Tema3-DISM-21.pdf, páginas PDF 21, 25.

Distractores:

- A) Repite D/R sin despejar N.
- C) Divide 6² entre dos en lugar de entre tres.
- D) Eleva al cuadrado D/R, pero omite dividir entre tres.

## 17. B) 4

El área de cada celda queda en (1/2)² = 1/4. Para cubrir el mismo territorio hacen falta cuatro veces más celdas.

Fuente: Tema3-DISM-21.pdf, páginas PDF 29.

Distractores:

- A) El área cambia con el cuadrado de la escala lineal, no solo con el radio.
- C) Introduce un factor cúbico que no corresponde a una superficie.
- D) Confunde la relación de áreas con otro posible escalado, como el de potencia con exponente cuatro.

## 18. A) Establecer el enlace nuevo antes de soltar el anterior

Soft handover es make before break: durante la transición coexisten enlaces. Hard handover corta primero y establece después.

Fuente: Tema3-DISM-21.pdf, páginas PDF 42.

Distractores:

- B) Esa secuencia es hard handover, break before make.
- C) Eso no describe por sí solo un traspaso soft.
- D) Un traspaso busca conservar la llamada en curso, no iniciar una nueva.

## 19. C) 12 celdas

N = 2² + 2² + 2×2 = 4 + 4 + 4 = 12. El producto cruzado aparece una vez.

Fuente: Tema3-DISM-21.pdf, páginas PDF 14–15.

Distractores:

- A) Suma i+j en vez de aplicar la fórmula.
- B) Suma los dos cuadrados, pero omite i·j.
- D) Calcula (i+j)² e incluye dos veces el término cruzado.

## 20. D) Se mantiene, porque señal e interferencia se multiplican por el mismo factor

La relación se mantiene: 2S/(2I) = S/I. La mejora debe buscarse en factores como separación y planificación, no en subir igual la potencia de todos.

Fuente: Tema3-DISM-21.pdf, páginas PDF 21, 25.

Distractores:

- A) La interferencia también aumenta en las condiciones dadas.
- B) Subir todas las potencias no elimina que las celdas reutilicen los mismos canales.
- C) El mismo factor aparece tanto en numerador como en denominador y se cancela.

## 21. D) 2000 minutos de llamada y aproximadamente 11,11 erlangs

Volumen = 500×4 = 2000 minutos de llamada. Intensidad = 2000/(3×60) ≈ 11,11 erlangs. No se necesita aplicar la fórmula de Erlang B.

Fuente: Tema3-DISM-21.pdf, páginas PDF 51, 55.

Distractores:

- A) Intercambia las magnitudes y sus unidades.
- B) Omite la duración de cuatro minutos de cada llamada.
- C) Divide el volumen entre 60 minutos en lugar de los 180 de observación.

## 22. A) 1/16

La nueva potencia es proporcional a 1/(2d)⁴ = 1/(16d⁴). Se recibe una dieciseisava parte.

Fuente: Tema3-DISM-21.pdf, páginas PDF 23.

Distractores:

- B) Aplica un exponente tres en lugar de cuatro.
- C) Aplica un exponente dos en lugar de cuatro.
- D) Trata la caída como inversamente proporcional solo a la distancia.

## 23. B) 40 %

El tráfico perdido es 25 − 15 = 10 erlangs. GoS = 10/25 = 0,4 = 40 %. En esta definición un porcentaje de pérdidas menor indica mejor servicio.

Fuente: Tema3-DISM-21.pdf, páginas PDF 50, 52, 57.

Distractores:

- A) La diferencia es 10 erlangs, que no equivale directamente a un porcentaje.
- C) Es la fracción de tráfico cursado 15/25, no la de tráfico perdido.
- D) Divide el tráfico perdido entre el cursado en lugar de entre el ofrecido.

## 24. D) Inter-BSC, intra-MSC

Cambia el controlador BSC pero se conserva la central MSC. El temario sitúa la gestión de este alcance en el MSC.

Fuente: Tema3-DISM-21.pdf, páginas PDF 36, 39.

Distractores:

- A) Se cambia de estación y de controlador, no solo de canal en la misma celda.
- B) Las dos estaciones no comparten BSC en este caso.
- C) El enunciado mantiene el mismo MSC para los dos controladores.

## 25. A) Cola de traspasos

La cola aprovecha el intervalo en que el móvil aún puede conservar su enlace anterior. Si la espera se agota, el traspaso puede fallar y la llamada perderse.

Fuente: Tema3-DISM-21.pdf, páginas PDF 43–44.

Distractores:

- B) El caso permite esperar en vez de rechazar inmediatamente.
- C) No se ha descrito interrumpir otra llamada, sino esperar un recurso.
- D) La reserva separa recursos; el caso describe además una espera temporal de la petición.

## 26. C) Intra-celda

Handover no significa necesariamente desplazarse a otra celda. El traspaso intra-celda cambia recursos del enlace dentro de la misma.

Fuente: Tema3-DISM-21.pdf, páginas PDF 36–37.

Distractores:

- A) Implicaría cambiar de controlador, no solo de canal dentro de la celda.
- B) Implicaría un cambio de central de un alcance mucho mayor.
- D) Implicaría cambiar de celda, que el caso descarta.

## 27. B) 20 dB

Para una relación de potencias se utiliza 10 log₁₀(100) = 10×2 = 20 dB.

Fuente: Tema3-DISM-21.pdf, páginas PDF 24.

Distractores:

- A) Corresponde a una relación de potencia de 10, no de 100.
- C) Aplica 20 log₁₀ a una relación de potencias; aquí corresponde 10 log₁₀.
- D) Confunde directamente el cociente lineal con su representación logarítmica.

## 28. C) 73,5

S/I = 21²/6 = 441/6 = 73,5. Su equivalente en decibelios es 10 log₁₀(73,5) ≈ 18,66 dB.

Fuente: Tema3-DISM-21.pdf, páginas PDF 23–27.

Distractores:

- A) Divide 3N entre seis sin elevar a n/2.
- B) Es aproximadamente el resultado en dB, no la relación lineal pedida.
- D) Es (3N)²; falta dividir entre los seis interferentes.

## 29. C) 7 celdas

N = 2² + 1² + 2×1 = 4 + 1 + 2 = 7. No cualquier entero es un tamaño geométricamente posible en este modelo.

Fuente: Tema3-DISM-21.pdf, páginas PDF 14–15.

Distractores:

- A) Suma i + j en lugar de aplicar la fórmula geométrica.
- B) Solo suma i² + j² y omite el producto i·j.
- D) Eleva (i + j) al cuadrado, duplicando el término cruzado.

## 30. B) MSC, central de conmutación móvil

El esquema clásico distingue terminales, estaciones base, controladores y central MSC. El MSC conmuta y conecta con otras redes; no se pregunta por generaciones.

Fuente: Tema3-DISM-21.pdf, páginas PDF 7, 35.

Distractores:

- A) El BSC controla BTS y traspasos de su dominio; la conmutación y conexión de nivel superior corresponden al MSC.
- C) El terminal no realiza la conmutación central de toda la red.
- D) La BTS proporciona el enlace radio con los terminales, no la función central de conmutación del caso.

## 31. A) 50 canales

Quedan 420 − 70 = 350 canales de tráfico. Al dividirlos entre siete celdas se obtienen 50 por celda.

Fuente: Tema3-DISM-21.pdf, páginas PDF 16, 20.

Distractores:

- B) Divide 420 entre siete sin descontar los reservados para control.
- C) Confunde la reserva total de control con los canales de tráfico por celda.
- D) Es el total de tráfico del clúster, antes de repartirlo entre celdas.

## 32. D) Asignar un canal disponible mientras dura su uso y liberarlo después

El trunking permite compartir un conjunto de recursos: se ocupa un canal disponible para la comunicación y se devuelve al conjunto al finalizar.

Fuente: Tema3-DISM-21.pdf, páginas PDF 9–10.

Distractores:

- A) Eso desperdicia el recurso cuando el usuario no lo utiliza.
- B) Eso introduce interferencia y no define el trunking.
- C) El trunking comparte un conjunto, no consume el conjunto entero por llamada.

## 33. A) Multiplicarse aproximadamente por 2

10 log₁₀(2) ≈ 3,01 dB. Por eso una mejora de unos 3 dB equivale aproximadamente a duplicar la relación lineal.

Fuente: Tema3-DISM-21.pdf, páginas PDF 24.

Distractores:

- B) El número de dB no se utiliza directamente como factor lineal.
- C) Dividir entre dos supone una caída cercana a 3 dB, no una mejora.
- D) Un factor diez corresponde a 10 dB, no a 3 dB.

## 34. C) 5040 canales

Hay M = 84/7 = 12 clústeres. La capacidad es M×T = 12×420 = 5040 canales, equivalente a 84×60.

Fuente: Tema3-DISM-21.pdf, páginas PDF 16–17.

Distractores:

- A) Ese es el número de clústeres, no el número de canales disponibles.
- B) Cuenta un único clúster y omite su repetición por la red.
- D) Multiplica por cada celda en lugar de por el número de clústeres.
