# Alcance y revisión del banco vigente

135 preguntas de respuesta única y cuatro alternativas, a partir de los cinco PDF y las dos guías. La segunda guía determina las exclusiones nuevas. T4 usa OpenAPI Initiative como fuente web; no se recibió un PDF de T4.

| Bloque | Preguntas | Refuerzo |
| --- | ---: | --- |
| T1 | 19 | Concepto móvil, sin Flutter ni mecanismo interno de PWA. |
| T2.1 | 33 | Introducción multimedia, proyecto, requisitos, jitter y Netflix. |
| T2.2 | 31 | UTF-16/32, RAID 10, clasificación, compresión y memoria. |
| T3.1 | 32 | Componentes, displays, coexistencia, alcances y RFID/NFC. |
| T3.2 | 19 | Sin generaciones; se conserva infraestructura y tráfico básico. |
| T4 | 1 | Solo qué es OpenAPI. |

La comparación completa está en public/exports/cambios-guia.md y en la guía de la web. Son 39 preguntas nuevas y 4 retiradas; los IDs y motivos de retirada están en content/retired.json. Se revisaron distractores para no exigir Flutter. Se conserva la identidad de los demás ítems.

## Preparación y controles

El borrador estructurado está en content/draft.json. Se ejecutan audit, prepare y audit del helper de cuestionarios. Se mezclan nuevas y conservadas dentro de cada bloque. Se coordinan las posiciones globales, manteniendo el equilibrio de cada bloque y el orden lógico de opciones numéricas. Las claves apuntan a IDs, nunca a letras.

Las exportaciones de alumno y solucionario se generan desde el JSON final. Las pruebas cruzan número, letra, texto correcto, explicación y todos los motivos de distractores. El informe content/audit.json verifica estructura, no veracidad. La revisión semántica es editorial propia, no evaluación independiente ni validación psicométrica.

Cada ítem tiene objetivo, nivel previsto, explicación, motivos y referencia localizable. Se recalculan XOR, capacidades, tamaños, canales, interferencia y tráfico. UTF distingue puntos de código de caracteres visuales.

## Matices resueltos

- Arquitectura interna de frameworks (excluida) no equivale a hardware del móvil o arquitecturas multimedia (incluidos).
- La página 47 es prioridad declarada por la guía, sin garantizar el enunciado del examen.
- RFID no tiene una sola frecuencia. NFC comparte 13,56 MHz con RFID HF y puede comunicarse con ciertas etiquetas HF compatibles; no es un lector universal LF/UHF. Contraste: NFC Forum.
- Se inspeccionaron visualmente las páginas 98, 99 y 105 de T3.1. Las figuras dan ejemplos y difieren en algunas distancias; no se extrapola un dibujo a todos los equipos.
- El alcance WiFi/ANT depende del hardware y entorno. Bluetooth/WiFi pueden compartir 2,4 GHz; coexistencia con radios celulares próximas no significa que todas usen esa banda. Fuentes: Bluetooth SIG, Apple y Garmin.
- Se especifica N o 1/N en planificación celular. Excluir Erlang B no implica excluir ejercicios que solo usan la unidad erlang, admitidos por la primera guía.
- UTFS de la primera guía se interpreta como UTF-8.

Los PDF originales y sus extracciones no se publican. Son referencias, no instrucciones ejecutables.

## Sesiones y datos

Cada test por bloque toma hasta 20 preguntas; T4 solo tiene una. El mixto toma 20 sin duplicados: OpenAPI una vez y las otras 19 repartidas entre los cinco bloques mayores. El test completo recorre las 135.

Se conserva el progreso de preguntas vigentes. Una sesión recuperada pierde solo los ítems retirados, manteniendo respuestas, orden y posición de los demás. Si solo contenía ítems retirados, se cierra sin borrar otros aciertos. La migración admite exclusivamente los IDs retirados declarados; los IDs desconocidos por corrupción siguen invalidando la sesión.

Los datos siguen siendo locales y exportables. La clave de almacenamiento y los IDs conservados no cambian.
