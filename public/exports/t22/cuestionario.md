# DISM · T2.2 · Almacenamiento y arquitecturas

Elige una única respuesta por pregunta.

1. ¿Qué ocurre si falla un disco de un RAID 0 sin otra copia de los datos?

   A) El espejo conserva una copia completa
   B) El conjunto soporta hasta dos fallos simultáneos
   C) La paridad distribuida reconstruye el contenido
   D) El conjunto pierde la disponibilidad íntegra de sus datos

2. Se configura un espejo RAID 1 con dos discos de 2 TB. Sin contar metadatos, ¿qué capacidad útil ofrece?

   A) 1 TB
   B) 2 TB
   C) 3 TB
   D) 4 TB

3. Un RAID 5 usa cinco discos de 2 TB. Suponiendo discos iguales y sin metadatos, ¿cuánta capacidad útil tiene?

   A) 2 TB
   B) 6 TB
   C) 8 TB
   D) 10 TB

4. En RAID 5, ¿cómo se coloca la paridad entre las distintas franjas?

   A) Se guarda siempre en un único disco dedicado
   B) Se duplica cada bloque completo en todos los discos
   C) Se calcula sin guardar información redundante
   D) Va rotando entre los discos del conjunto

5. Una franja RAID 5 tiene D0 = 1011, D1 = 0101 y D2 = 1100. Si P = D0 ⊕ D1 ⊕ D2, ¿cuál es P?

   A) 0010
   B) 1100
   C) 1110
   D) 1111

6. Falta D1 en una franja con D0 = 1011, D2 = 1100 y P = 0010. ¿Qué bloque se recupera mediante P ⊕ D0 ⊕ D2?

   A) 0000
   B) 0101
   C) 0111
   D) 1001

7. En una escritura parcial RAID 5, P = 0010 y el dato D2 cambia de 1100 a 1000. ¿Qué nueva paridad resulta de P′ = P ⊕ D2viejo ⊕ D2nuevo?

   A) 0010
   B) 0100
   C) 0110
   D) 1010

8. Se actualiza un bloque de datos RAID 5 con Read-Modify-Write, sin caché previa. ¿Qué accesos lógicos a disco describe el tema?

   A) Tres lecturas y una escritura
   B) Cero lecturas y dos escrituras
   C) Una lectura y una escritura
   D) Dos lecturas y dos escrituras

9. Se escriben completos los tres bloques de datos nuevos de una franja RAID 5 de cuatro discos. Sin caché ni otras operaciones, ¿qué permite el full-stripe write?

   A) Leer siempre el dato antiguo y la paridad por cada bloque nuevo
   B) Evitar escribir el bloque de paridad
   C) Calcular la paridad nueva sin leer los datos antiguos de esa franja
   D) Convertir los cuatro discos en copias idénticas

10. ¿Qué diferencia de tolerancia a fallos distingue RAID 6 de RAID 5?

   A) RAID 6 soporta dos discos fallidos y RAID 5 uno
   B) Ninguno soporta fallos porque no utiliza espejos
   C) RAID 6 soporta uno y RAID 5 dos
   D) Ambos soportan dos discos fallidos por usar XOR

11. Se borra por error un archivo en un volumen RAID 1 y el borrado se refleja en ambos discos. ¿Qué medida habría permitido recuperar una versión anterior?

   A) Recalcular la paridad sobre el volumen ya modificado
   B) Cambiar a RAID 0 para repartir el archivo
   C) Añadir otro espejo que reproduzca el mismo borrado
   D) Una copia de seguridad anterior al borrado

12. ¿Qué propiedad describe correctamente UTF-8?

   A) Usa dos bytes para todo Unicode sin excepciones
   B) Usa entre uno y cuatro bytes y mantiene la codificación de ASCII
   C) Usa cuatro bytes para todos los caracteres
   D) Representa solo los 128 caracteres del repertorio ASCII

13. Una imagen de 512 × 512 píxeles usa 24 bits por píxel, sin compresión ni cabeceras. ¿Qué tamaño ocupa, tomando 1 MiB = 2²⁰ bytes?

   A) 0,25 MiB
   B) 0,75 MiB
   C) 2,25 MiB
   D) 6 MiB

14. Un archivo debe recuperar exactamente todos sus datos originales después de descomprimirlo. ¿Qué clase de compresión se requiere?

   A) Con pérdida seguida de ampliación de resolución
   B) Con pérdida y calidad visual alta
   C) Con pérdida (lossy)
   D) Sin pérdida (lossless)

15. ¿Qué pareja se corresponde con los modos de compresión descritos en el tema?

   A) GIF con pérdida y PNG con pérdida
   B) PNG sin pérdida y JPEG convencional con pérdida
   C) PNG con pérdida y JPEG convencional sin pérdida
   D) JPEG convencional sin pérdida y WebP solo con pérdida

16. Un algoritmo vuelve a leer la misma posición de memoria varias veces en un intervalo corto. ¿Qué propiedad manifiesta?

   A) Localidad temporal
   B) Localidad espacial
   C) Acceso secuencial sin reutilización
   D) Ausencia de localidad de memoria

17. Un filtro procesa píxeles consecutivos de cada fotograma y después pasa al siguiente sin volver a esos datos. ¿Qué patrón encaja con las MMA del tema?

   A) Alta localidad temporal y alta reutilización del mismo píxel
   B) Baja localidad espacial por acceder a píxeles vecinos
   C) Alta localidad espacial y baja localidad temporal de los datos
   D) Alta localidad temporal y baja localidad espacial

18. Se necesita modificar el circuito de procesamiento después de fabricar el dispositivo. ¿Qué opción lo permite según la clasificación del tema?

   A) Una FPGA reconfigurable
   B) Un ASIC de circuito fijo
   C) Un ASIC modular con más chips de la misma tarea
   D) Un ASIC monolítico con más frecuencia de reloj

19. ¿Qué operación básica acelerada por hardware destaca en un DSP para filtros y procesamiento repetitivo?

   A) Multiplicación y acumulación (MAC)
   B) Búsqueda y salto entre archivos del sistema
   C) Compresión y cifrado como una única operación MAC
   D) Conversión entre UTF-8 y UTF-32

20. Una videollamada ejecuta lógica de la app, un efecto de IA y codificación de vídeo. ¿Qué reparto se ajusta a la especialización descrita?

   A) Motor de vídeo para reglas de negocio y CPU solo para IA
   B) FPGA obligatoria para cualquier lógica de aplicación móvil
   C) CPU para lógica, NPU para IA y motor de vídeo para codificar
   D) NPU para toda la lógica y CPU exclusivamente para píxeles
