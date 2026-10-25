# Alcance y revisión del banco

Se redactaron 100 preguntas originales, 20 para cada uno de los cinco bloques de los PDF entregados. Cada pregunta tiene cuatro alternativas, una solución por ID estable, explicación general, motivo de cada distractor y referencia localizable.

La guía facilitada por el estudiante fija el alcance. Los PDF se tratan como material de referencia, no como instrucciones ejecutables. Las páginas citadas son las del archivo, contando desde la primera.

## Distribución

| Bloque | Objetivos priorizados | Preguntas |
| --- | --- | --- |
| T1 | Definiciones y elección de frameworks, nativo/híbrido, PWA | 20 |
| T2.1 | 2 introductorias; servicios, protocolos, búfer, jitter, P2P y OCA | 20 |
| T2.2 | 11 de RAID; formatos, compresión, localidad y arquitecturas | 20 |
| T3.1 | Wearables/textiles, táctil/display y conectividad | 20 |
| T3.2 | Modelo celular, capacidad/interferencia, traspasos y tráfico | 20 |

Se excluye la arquitectura interna de MAUI, los anchos de banda de WiFi y el desarrollo en profundidad de Erlang B. Se incluyen ejercicios de intensidad de tráfico en erlangs. La dificultad prevista combina comprensión, aplicación y cálculo; no hay métricas observadas de estudiantes.

## Comprobaciones

- Extracción de los cinco PDF locales mediante pypdf, con texto y páginas en `work/sources/` (ignorado por Git).
- Comprobación de las soluciones con las secciones indicadas. Los ejercicios XOR, capacidades, imagen sin comprimir, distancias, cocientes de interferencia y tráfico se recalculan también en pruebas automatizadas.
- Borrador estructurado en `content/draft.json`. Se ejecutaron `audit`, `prepare` y `audit` del helper de la skill cuestionarios. Exportaciones de alumno y solucionario generadas desde el mismo JSON final, por bloque.
- Distribución de claves de la exportación: 5 por posición y bloque; 25 por posición en el banco completo. Los ejercicios numéricos mantienen orden ascendente (`shuffle_options: false`). Las demás opciones se barajan por ID, repartiendo posiciones sin ciclos prefijados y compensando las posiciones fijas cuando es posible. Un repaso parcial puede tener restricciones que impidan un reparto exacto.
- La única alerta final del helper es una racha de cuatro C entre preguntas consecutivas del banco. Se conserva: las preguntas evalúan objetivos distintos, las explicaciones corresponden a sus claves y una racha aleatoria no es un error. No se ha impuesto una alternancia artificial.
- Revisión editorial propia del resultado: definición única bajo las condiciones del enunciado, referencias, razones de distractores y ausencia de soluciones visibles en la copia del alumno. No se acredita validación psicométrica ni evaluación independiente.

## Matices resueltos

- «UTFS (23)» se interpreta como UTF-8, presente en la página PDF 23 de T2.2.
- En T3.2, página 13 se llama factor de reutilización a N, y página 16 a 1/N. Se pregunta por tamaño N o fracción 1/N de forma expresa.
- No se pregunta si WiFi 1 supera siempre a WiFi 7 en alcance. Se compara 2,4 GHz con 6 GHz bajo condiciones comparables, aclarando que WiFi 7 también admite 2,4 GHz.
- No se repiten afirmaciones absolutas de las transparencias sobre PNG sin animación, uniformidad de alcance RFID ni generalización de disponibilidad y soporte de frameworks. Xamarin se pregunta en contexto histórico.
- Las frecuencias y perfiles de conectividad y la misión del OCA se contrastaron con fuentes primarias: Netflix Open Connect, Bluetooth SIG, Garmin ANT/ANT+ y NFC Forum. Los enlaces están en los ítems correspondientes y en la guía.
- No se publican los PDF originales ni sus extracciones. La web publica preguntas originales con referencias a archivos que conserva el estudiante.

## Datos y puntuación

El progreso se guarda en localStorage por navegador. Mis fallos contiene preguntas con último intento incorrecto. Un acierto posterior las retira, manteniendo el historial de intentos. Cada estudiante tiene su propio progreso; no hay repositorio común de errores de alumnos. Exportación/importación permiten trasladar estadísticas, pero no fusionan copias ni sincronizan dispositivos. El modo examen registra correcciones al finalizar. Las preguntas en blanco se muestran por separado, sin tratarlas como intentos erróneos guardados. El porcentaje es de aciertos sin penalización; no equivale a la nota oficial.
