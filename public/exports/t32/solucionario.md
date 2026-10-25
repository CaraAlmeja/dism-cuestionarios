# Solucionario: DISM · T3.2 · Telefonía móvil

## 1. D) 2000 minutos de llamada y aproximadamente 11,11 erlangs

Volumen = 500×4 = 2000 minutos de llamada. Intensidad = 2000/(3×60) ≈ 11,11 erlangs. No se necesita aplicar la fórmula de Erlang B.

Fuente: Tema3-DISM-21.pdf, páginas PDF 51, 55.

Distractores:

- A) Intercambia las magnitudes y sus unidades.
- B) Divide el volumen entre 60 minutos en lugar de los 180 de observación.
- C) Omite la duración de cuatro minutos de cada llamada.

## 2. A) 165 canales

33 MHz = 33 000 kHz. Cada par dúplex ocupa 50 kHz: T = 33 000/50 = 660. Después K = 660/4 = 165.

Fuente: Tema3-DISM-21.pdf, páginas PDF 20.

Distractores:

- B) Olvida que cada canal dúplex utiliza dos canales simplex.
- C) Es el total de canales dúplex del sistema antes de repartir entre cuatro celdas.
- D) Cuenta canales simplex del sistema, sin formar pares ni dividir por N.

## 3. C) 7 celdas

N = 2² + 1² + 2×1 = 4 + 1 + 2 = 7. No cualquier entero es un tamaño geométricamente posible en este modelo.

Fuente: Tema3-DISM-21.pdf, páginas PDF 14–15.

Distractores:

- A) Suma i + j en lugar de aplicar la fórmula geométrica.
- B) Solo suma i² + j² y omite el producto i·j.
- D) Eleva (i + j) al cuadrado, duplicando el término cruzado.

## 4. B) 20 dB

Para una relación de potencias se utiliza 10 log₁₀(100) = 10×2 = 20 dB.

Fuente: Tema3-DISM-21.pdf, páginas PDF 24.

Distractores:

- A) Corresponde a una relación de potencia de 10, no de 100.
- C) Aplica 20 log₁₀ a una relación de potencias; aquí corresponde 10 log₁₀.
- D) Confunde directamente el cociente lineal con su representación logarítmica.

## 5. C) 73,5

S/I = 21²/6 = 441/6 = 73,5. Su equivalente en decibelios es 10 log₁₀(73,5) ≈ 18,66 dB.

Fuente: Tema3-DISM-21.pdf, páginas PDF 23–27.

Distractores:

- A) Divide 3N entre seis sin elevar a n/2.
- B) Es aproximadamente el resultado en dB, no la relación lineal pedida.
- D) Es (3N)²; falta dividir entre los seis interferentes.

## 6. B) 9,17 km

D = R√(3N) = 2√21 ≈ 2×4,5826 = 9,17 km. D/R no tiene unidades; D sí se mide en kilómetros.

Fuente: Tema3-DISM-21.pdf, páginas PDF 21, 25.

Distractores:

- A) Es el valor numérico de D/R; falta multiplicar por el radio de 2 km.
- C) Multiplica N por R sin aplicar √(3N).
- D) Usa 3N×R y omite la raíz cuadrada.

## 7. D) Establecer el enlace nuevo antes de soltar el anterior

Soft handover es make before break: durante la transición coexisten enlaces. Hard handover corta primero y establece después.

Fuente: Tema3-DISM-21.pdf, páginas PDF 42.

Distractores:

- A) Esa secuencia es hard handover, break before make.
- B) Eso no describe por sí solo un traspaso soft.
- C) Un traspaso busca conservar la llamada en curso, no iniciar una nueva.

## 8. A) 10 erlangs

El volumen es 600×3 = 1800 minutos de llamada. La intensidad es 1800/180 = 10 erlangs, equivalente a diez circuitos ocupados de media.

Fuente: Tema3-DISM-21.pdf, páginas PDF 49, 56.

Distractores:

- B) Divide por una hora cuando el intervalo observado son tres horas.
- C) Confunde el número de llamadas con la ocupación media de circuitos.
- D) Es el volumen en minutos de llamada, sin dividir entre los 180 minutos observados.

## 9. D) BSC

El Base Station Controller controla varias estaciones BTS. El MSC conecta y conmuta a un nivel superior. Este esquema se pregunta en su contexto GSM, no como arquitectura idéntica de 4G/5G.

Fuente: Tema3-DISM-21.pdf, páginas PDF 35–36.

Distractores:

- A) El MSC realiza conmutación y coordinación de mayor alcance; no es la estación radio.
- B) La BTS mantiene el enlace radio con los móviles de la celda.
- C) UE es el equipo del usuario, no el controlador de varias BTS.

## 10. D) Inter-celda, intra-BSC

Se cambia de celda dentro del mismo controlador, por lo que es un handover inter-celda e intra-BSC.

Fuente: Tema3-DISM-21.pdf, páginas PDF 36–40.

Distractores:

- A) Requeriría cambiar de BSC, que aquí se mantiene.
- B) Requeriría cambiar de central MSC, no solo de BTS dentro de un BSC.
- C) En el intra-celda cambia el canal dentro de la misma celda, no la BTS.

## 11. C) 5040 canales

Hay M = 84/7 = 12 clústeres. La capacidad es M×T = 12×420 = 5040 canales, equivalente a 84×60.

Fuente: Tema3-DISM-21.pdf, páginas PDF 16–17.

Distractores:

- A) Ese es el número de clústeres, no el número de canales disponibles.
- B) Cuenta un único clúster y omite su repetición por la red.
- D) Multiplica por cada celda en lugar de por el número de clústeres.

## 12. B) 60 canales

K = T/N = 420/7 = 60 canales por celda. T ya está expresado en canales dúplex, por lo que no hay que dividir de nuevo entre dos.

Fuente: Tema3-DISM-21.pdf, páginas PDF 16–17.

Distractores:

- A) Divide entre 12, que no es el tamaño N indicado.
- C) Asigna el total del clúster a cada celda y omite el reparto.
- D) Multiplica T por N en lugar de dividirlo.

## 13. C) Se bloquea aunque haya canales de guarda libres

La reserva protege los traspasos y reduce cortes de llamadas existentes. Su coste es aumentar el bloqueo de nuevas llamadas al limitar sus canales disponibles.

Fuente: Tema3-DISM-21.pdf, páginas PDF 43–45.

Distractores:

- A) La política descrita no expulsa llamadas en curso.
- B) Los canales de guarda del caso son exclusivos para traspasos.
- D) Pedir una llamada nueva no la convierte en una comunicación ya en curso.

## 14. D) Más canales por celda y más interferencia cocanal

K = T/N aumenta si baja N, pero D/R = √(3N) disminuye. Las celdas que reutilizan los canales quedan más cerca y la relación S/I empeora.

Fuente: Tema3-DISM-21.pdf, páginas PDF 21, 27–28.

Distractores:

- A) Disminuir N acerca las celdas cocanal y empeora la interferencia.
- B) Eso describe el efecto de aumentar N.
- C) Ambos efectos están invertidos respecto a reducir N.

## 15. B) Aumentar la capacidad por unidad de superficie

Cell splitting facilita reutilizar recursos más veces en una zona, a costa de nuevos emplazamientos y mayor complejidad. No elimina interferencias ni movilidad.

Fuente: Tema3-DISM-21.pdf, páginas PDF 29.

Distractores:

- A) Las celdas menores pueden exigir más traspasos al desplazarse.
- C) La división requiere coordinar recursos y añade complejidad a la asignación.
- D) La división utiliza varias estaciones y radios menores, no una única antena más potente.

## 16. A) Asignar un canal disponible mientras dura su uso y liberarlo después

El trunking permite compartir un conjunto de recursos: se ocupa un canal disponible para la comunicación y se devuelve al conjunto al finalizar.

Fuente: Tema3-DISM-21.pdf, páginas PDF 9–10.

Distractores:

- B) Eso introduce interferencia y no define el trunking.
- C) El trunking comparte un conjunto, no consume el conjunto entero por llamada.
- D) Eso desperdicia el recurso cuando el usuario no lo utiliza.

## 17. C) Mide el móvil y decide la red

MAHO significa Mobile Assisted Handover: el móvil aporta medidas y la red decide. No debe confundirse asistencia con control completo por el terminal.

Fuente: Tema3-DISM-21.pdf, páginas PDF 41.

Distractores:

- A) Ese reparto corresponde al MCHO descrito.
- B) Invierte los papeles del esquema MAHO.
- D) Ese reparto corresponde al NCHO descrito.

## 18. B) 40 %

El tráfico perdido es 25 − 15 = 10 erlangs. GoS = 10/25 = 0,4 = 40 %. En esta definición un porcentaje de pérdidas menor indica mejor servicio.

Fuente: Tema3-DISM-21.pdf, páginas PDF 50, 52, 57.

Distractores:

- A) La diferencia es 10 erlangs, que no equivale directamente a un porcentaje.
- C) Es la fracción de tráfico cursado 15/25, no la de tráfico perdido.
- D) Divide el tráfico perdido entre el cursado en lugar de entre el ofrecido.

## 19. A) 1/7

La fracción es 1/N = 1/7. El PDF también llama «factor» a N en otra diapositiva; aquí se explicita la definición para evitar ambigüedad.

Fuente: Tema3-DISM-21.pdf, páginas PDF 13, 16.

Distractores:

- B) Resta una celda sin que exista esa resta en el modelo.
- C) Es el complemento de 1/7 y corresponde a los canales que no recibe esa celda.
- D) Es el tamaño N del clúster, no la fracción 1/N solicitada.
