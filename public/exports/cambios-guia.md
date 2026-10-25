# Comparación de las dos guías de examen

La segunda guía amplía y precisa el alcance de la primera. Se han añadido 39 preguntas, retirado 4 y revisado alternativas conservadas para no exigir contenidos excluidos. El banco activo pasa de 100 a 135 preguntas.

| Bloque | Antes | Ahora | Cambio principal |
| --- | ---: | ---: | --- |
| T1 | 20 | 19 | Se retiran Flutter y el mecanismo interno de la PWA; se añade concepto de desarrollo móvil. |
| T2.1 | 20 | 33 | Más introducción multimedia, proyecto, requisitos, jitter y Netflix. |
| T2.2 | 20 | 31 | UTF-16/32, RAID 10, clasificación de arquitecturas, compresión perceptiva y memoria. |
| T3.1 | 20 | 32 | Componentes del móvil, displays, coexistencia radio, alcances y RFID/NFC; se retira la pregunta de generaciones WiFi. |
| T3.2 | 20 | 19 | Se retira la pregunta de generaciones móviles. Se mantiene la infraestructura celular y el tráfico básico. |
| T4 | 0 | 1 | Únicamente «¿Qué es OpenAPI?». |

Las preguntas nuevas están intercaladas con las conservadas en cada bloque. Los tests por bloque toman hasta 20 preguntas sin repetir dentro de la sesión; el test completo utiliza las 135. El mixto tiene 20 preguntas y cubre los seis bloques: OpenAPI aparece una vez y el resto se reparte entre los cinco bancos mayores.

## Cambios de alcance

- **T1:** la primera guía pedía qué es cada framework, sin arquitectura MAUI. La segunda excluye Flutter y todo funcionamiento interno o arquitectura detallada de apps/frameworks. Se conservan definiciones, elecciones y diferencias nativo/híbrido. También se revisaron distractores para no depender de conocer Flutter.
- **T2.1:** «las 15 primeras páginas tal vez algo» pasa a «entra todo hasta streaming». Se añaden preguntas de integración digital, hipermedia, planificación, pruebas y requisitos; se refuerzan jitter, búfer y el reparto backend/OCA de Netflix. Unicast/multicast, AVOD y RTSP ya estaban cubiertos.
- **T2.2:** RAID 5, XOR, recuperación y escritura parcial ya tenían preguntas. Se incorpora RAID 10 y se amplía la comparación de UTF-8/16/32. La clasificación de la página 47 se refuerza con las familias programables, dedicadas y reconfigurables, programables específicas, integración monolítica/modular y RISC/CISC. Se incorporan costes perceptivos de compresión y necesidades de memoria de las MMA. La prioridad atribuida a la página 47 procede de la guía, no de una verificación del examen oficial.
- **T3.1:** se añade hardware interno del móvil (SoC, RAM/flash y NPU), ventajas de LCD frente a AMOLED para imágenes estáticas, interferencias/coexistencia Bluetooth, comparación de uso de WiFi/ANT, criterios de alcance y compatibilidad RFID/NFC. No se preguntan versiones Bluetooth ni generaciones de conectividad, y tampoco tasas o anchos de canal memorizados.
- **T3.2:** la segunda guía excluye versiones de redes móviles y Erlang B. No excluye expresamente planificación celular, traspasos ni intensidad de tráfico en erlangs, que la primera guía sí incluía; se mantienen. La unidad erlang no es la fórmula de Erlang B.
- **T4:** es nuevo respecto a la primera guía. Se añade una pregunta conceptual con referencia a la OpenAPI Initiative, sin inventar un PDF ni introducir el resto de ese tema.

## Dos contradicciones de RFID/NFC

La segunda guía dice «tienen la misma frecuencia» y «un lector NFC no puede leer una etiqueta RFID». No son reglas universales correctas:

- NFC usa **13,56 MHz**, también utilizada por RFID **HF**. RFID incluye además LF, UHF y otras familias; los propios esquemas de las páginas 98 y 105 del PDF muestran distintas bandas.
- Un lector NFC no es un lector RFID universal: no lee una etiqueta UHF mediante su radio HF. Sí puede comunicarse con ciertas etiquetas RFID HF si el protocolo y las condiciones de acceso son compatibles. El [NFC Forum](https://nfc-forum.org/learn/nfc-technology/) enumera los protocolos admitidos.

Las preguntas concretan las condiciones y las explicaciones hacen visible el matiz. Se recomienda contrastar con el profesor qué familia o lector pretendía describir esa frase de la guía.

Las ilustraciones de alcance de las páginas 98 y 105 tampoco son límites universales: presentan valores distintos para algunos sistemas. No se ha convertido una distancia de un dibujo en garantía para cualquier equipo. Se pregunta por bandas, usos, proximidad y condiciones de alcance.

## Bluetooth e interferencias

Se distingue la banda compartida por Bluetooth y WiFi en 2,4 GHz de la coexistencia de radios celulares próximas en un móvil. No se afirma que toda red celular emita en 2,4 GHz ni que siempre interfiera. Referencias: [Apple, interferencias inalámbricas](https://support.apple.com/en-us/102319) y [Bluetooth SIG, mecanismos de coexistencia](https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-62/out/en/architecture%2C-change-history%2C-and-conventions/architecture.html).

## Fuentes y revisión

Se utilizan los cinco PDF originales, las dos guías aportadas y fuentes primarias de contraste. La definición de OpenAPI procede de [OpenAPI Initiative](https://www.openapis.org/what-is-openapi). Las referencias se guardan por pregunta, con explicación y motivo específico de cada distractor. Hay copias separadas de alumno y solucionario.

La revisión es editorial propia. Los controles automáticos comprueban estructura, claves y exportaciones; no prueban que estas sean las preguntas que pondrá el profesor ni constituyen validación psicométrica.
