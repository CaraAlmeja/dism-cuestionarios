# Comprobaciones realizadas

Fecha: 25 de octubre de 2026.

## Pruebas automatizadas

`npm test`: 12 pruebas satisfactorias. Cubren estructura y claves del banco, selección mixta sin duplicados, relación clave/ID tras barajado, orden y exclusividad numérica, altas y bajas de fallos, persistencia de sesión, validación de importación, separación de blancos en examen, cálculos y correspondencia de las dos exportaciones con el JSON final.

`npm run build`: salida estática generada correctamente. `node --check` en los módulos de la web: sin errores de sintaxis.

## Comprobación en navegador

Se recorrieron los siguientes flujos en el navegador de la app:

- Inicio → cuestionario por bloque → elegir una respuesta incorrecta → Comprobar: aparecen el motivo específico, la explicación general y las páginas de referencia; el fallo entra en la lista.
- Recargar con una respuesta ya corregida: conserva selección, explicación y sesión.
- Terminar un test incompleto: solicita confirmación y separa los blancos de los errores.
- Mis fallos → reintentar una pregunta → acertar: se retira de la lista y conserva el historial acumulado.
- Modo examen → elegir → avanzar → volver a la anterior: conserva la selección sin mostrar la solución. Al finalizar, corrige y separa los blancos.
- El historial muestra los intentos realizados y los porcentajes acumulados.
- Vista móvil a 390 × 844: se corrigió un desbordamiento inicial de las tarjetas de estadísticas. Inicio y cuestionario quedaron sin desbordamiento horizontal. Se restableció después el tamaño normal del navegador.
- Consola del navegador: sin errores ni avisos de la aplicación durante estos recorridos.

No se afirma que el banco esté validado psicométricamente. La revisión de contenido es editorial propia, con referencias y recálculo, documentada en `REVISION.md`.

## Actualización: tema oscuro, móvil y teclado

- Se añadieron nueve pruebas específicas de teclado, para un total de 21 pruebas satisfactorias. Cubren Espacio/Enter mantenidos, cambio de foco entre Comprobar y Siguiente, consumo del keyup, preguntas sin respuesta, modo examen, selección nativa con Tab, formularios/diálogos y liberación al perder el foco.
- Prueba real en navegador: mantener Espacio durante 1,5 segundos corrigió una sola pregunta y dejó visible la explicación; otra pulsación avanzó exactamente una pregunta. En examen, mantener Espacio avanzó una pregunta sin mostrar la corrección.
- Selector claro/oscuro comprobado en ambos sentidos. La elección se mantiene tras recargar; utiliza una clave independiente del progreso (`dism-lab:theme`).
- Cuestionario revisado a 320×568, 375×812, 430×932, 667×375 y 768×1024: sin desbordamiento horizontal. En móvil los controles de respuesta quedan encima de la navegación inferior y el mapa se presenta plegado.
- Guía, progreso y tarjetas revisados a 375 píxeles de ancho. Los nombres largos de los PDF ajustan su línea y las tarjetas se muestran en una columna en teléfonos pequeños.

## Corrección del desbordamiento del mapa

El mapa de 20 preguntas desbordaba internamente: con una tarjeta de 215 px, la cuadrícula disponía de 173 px pero ocupaba 198 px. La combinación de columnas `1fr`, proporción cuadrada y altura mínima de los botones imponía un ancho mínimo que no cabía. Se cambió a columnas `minmax(0,1fr)`, se eliminó esa transferencia de tamaño mediante `aspect-ratio: auto` y se ajustó el padding de los botones. El mapa largo tiene desplazamiento vertical dentro de su recuadro. La comprobación incluye los límites de la tarjeta, no solo el ancho total de la página.

## Pruebas de usuario con dos subagentes Luna (razonamiento máximo)

Se usaron puertos locales separados (4174 y 4175) para aislar los datos de prueba. Ambos revisores actuaron con la interfaz y no modificaron código. Sus vistas fueron de escritorio; las pruebas de siete anchuras del mapa las realizó el agente principal.

- Estudio: corrección de aciertos y fallos, explicación y referencias, resultado con pendientes, filtro de errores, nuevo intento acertado y retirada del fallo. Se navegó también a la pregunta 100 y por el mapa largo.
- Examen: cambio de respuesta, avanzar y volver, finalización con blancos, guardado y reanudación, recarga, tema claro/oscuro y exportación/importación de una copia de prueba. La importación se completó por el control accesible con Enter; la captura del evento de clic del selector de archivos tuvo una limitación en la herramienta y no se atribuyó al producto.
- Hallazgo corregido: en estudio se distingue ahora una opción «seleccionada, pendiente de comprobar» de una «corregida». El contador indica «comprobadas» y el texto explica cuándo cuenta una selección.
- Hallazgo corregido: el grupo de respuesta única tiene semántica `radiogroup`/`radio`, un punto de entrada con Tab y cambio de selección mediante flechas. La comprobación en navegador confirmó que se anuncia como radio y que solo una opción permanece marcada.
- Revisión adicional de teclado: «Dejar para después» respeta su acción al pulsar Espacio/Enter, sin forzar la corrección ni exigir una respuesta. Se añadieron tres pruebas de regresión; el total es de 24 pruebas automatizadas.

## Actualización con la segunda guía

- Banco de 135 preguntas: 39 añadidas y 4 retiradas. Se conserva la clave por ID de los 96 ítems vigentes de la primera versión y se mezclan los nuevos dentro de sus bloques.
- Audit del JSON final y de los seis bloques: sin errores ni alertas automáticas. La revisión semántica propia incluyó soluciones, distractores, cálculos y contradicciones de las guías; el script no acredita esa parte.
- 27 pruebas automatizadas satisfactorias. Las nuevas comprueban exclusiones, OpenAPI único, reparto mixto con T4 una sola vez y migración de sesiones con preguntas retiradas.
- Recálculo de los ejercicios nuevos: reserva de búfer 8/(4−2)=4 s; unicast 100×8=800 Mbit/s frente a multicast 8 Mbit/s en el origen; texto ASCII de 100 puntos de código en UTF-8: 100 bytes.
- Prueba en navegador: las tarjetas muestran bancos de 19, 33, 31, 32, 19 y 1 preguntas. T4 se completa con una única respuesta y muestra fuente web, resultado de 1/1 y progreso del 100 %. La guía presenta doce descargas de cuestionario/solucionario y la comparación de alcance.
- La guía nueva se revisó a 390 px sin desbordamiento horizontal. Los controles existentes de teclado y mapa siguen pasando sus pruebas.

## Ampliación de práctica del 26 de octubre de 2026

- Se hizo pull fast-forward del commit 85a3e2f del usuario: ocultar etiquetas antes de corregir y explicar todas las alternativas. Su implementación y estilos se conservan; solo se actualizan las referencias de caché y el título de una prueba para que no fije el total anterior.
- Banco ampliado de 135 a 200: T1 24 (+5), T2.1 48 (+15), T2.2 46 (+15), T3.1 47 (+15), T3.2 34 (+15), T4 1. Ninguna pregunta anterior se retira en esta ampliación.
- Baseline de 135 IDs y soluciones comprobado automáticamente. Los ítems nuevos tienen IDs posteriores a los existentes, sin reutilizar los retirados, y conservan las explicaciones de sus tres distractores.
- Audit/prepare/audit y exportaciones de alumno y solucionario regeneradas. No hay errores estructurales ni avisos de longitud; se revisaron y documentaron dos rachas legítimas de cuatro claves iguales. No se fuerza alternancia de letras.
- 34 pruebas satisfactorias, incluidas las seis pruebas nuevas de interfaz que incorporó el usuario. Comprueban ocultación de etiquetas y explicaciones completas para el banco entero, además de claves, exportaciones, límites de alcance y persistencia.
- Se recalcularon los ejercicios añadidos: XOR de datos 0101/0011/1000 = 1110, cancelación 0001 XOR 0001 = 0000, RAID 6 (6−2)×4 = 16 TB, búfer inicial 12/6 = 2 s, reparto (420−70)/7 = 50, N(2,2)=12, radio a la mitad implica cuatro veces más celdas, N=6²/3=12, potencia a doble distancia con n=4 queda en 1/16 y tráfico ofrecido/cursado 6/5,4 E. Las pruebas recalculan estos resultados.
- Navegador: tarjetas con los seis tamaños correctos; test de tema de 20 preguntas con etiqueta oculta antes de corregir; al corregir aparecen las tres razones de las alternativas. El test completo permite abrir la pregunta 200 y sus 200 botones no exceden horizontalmente la tarjeta. Consola sin errores durante el recorrido.
- La guía explica expresamente el muestreo aleatorio: no se repiten preguntas dentro de una sesión, pero sí pueden reaparecer en tests distintos. El mixto mantiene 20 y el recorrido completo contiene 200.
