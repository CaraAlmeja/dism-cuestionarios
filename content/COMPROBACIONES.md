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
