# DISM · T2.2 · Almacenamiento y arquitecturas

Elige una única respuesta por pregunta.

1. Se actualiza un bloque de datos RAID 5 con Read-Modify-Write, sin caché previa. ¿Qué accesos lógicos a disco describe el tema?

   A) Una lectura y una escritura
   B) Tres lecturas y una escritura
   C) Dos lecturas y dos escrituras
   D) Cero lecturas y dos escrituras

2. Falta D1 en una franja con D0 = 1011, D2 = 1100 y P = 0010. ¿Qué bloque se recupera mediante P ⊕ D0 ⊕ D2?

   A) 0000
   B) 0101
   C) 0111
   D) 1001

3. Un RAID 10 tiene dos parejas espejo: discos A/B y discos C/D. Fallan A y C y sus compañeros siguen operativos. ¿Qué ocurre con los datos del conjunto?

   A) Se recuperan mediante la doble paridad de A y C
   B) Siguen accesibles porque queda una copia de cada pareja
   C) Solo queda accesible la mitad que estaba en B
   D) Se pierden porque RAID 10 solo tolera un fallo en todo el conjunto

4. Un texto contiene solo ideogramas del BMP que necesitan tres bytes en UTF-8 y una unidad en UTF-16. Sin cabeceras ni BOM, ¿qué representación usa menos espacio por esos puntos de código?

   A) UTF-8, con un byte por punto de código
   B) UTF-16, con dos bytes por punto de código
   C) Las tres ocupan lo mismo por tratarse de Unicode
   D) UTF-32, con un byte por punto de código

5. ¿Qué diferencia de tolerancia a fallos distingue RAID 6 de RAID 5?

   A) Ambos soportan dos discos fallidos por usar XOR
   B) RAID 6 soporta uno y RAID 5 dos
   C) RAID 6 soporta dos discos fallidos y RAID 5 uno
   D) Ninguno soporta fallos porque no utiliza espejos

6. ¿Qué forma de codificación Unicode emplea cuatro bytes por punto de código?

   A) UTF-16
   B) ASCII de 7 bits
   C) UTF-8
   D) UTF-32

7. Un archivo debe recuperar exactamente todos sus datos originales después de descomprimirlo. ¿Qué clase de compresión se requiere?

   A) Sin pérdida (lossless)
   B) Con pérdida seguida de ampliación de resolución
   C) Con pérdida (lossy)
   D) Con pérdida y calidad visual alta

8. Se borra por error un archivo en un volumen RAID 1 y el borrado se refleja en ambos discos. ¿Qué medida habría permitido recuperar una versión anterior?

   A) Recalcular la paridad sobre el volumen ya modificado
   B) Una copia de seguridad anterior al borrado
   C) Añadir otro espejo que reproduzca el mismo borrado
   D) Cambiar a RAID 0 para repartir el archivo

9. Un RAID 5 usa cinco discos de 2 TB. Suponiendo discos iguales y sin metadatos, ¿cuánta capacidad útil tiene?

   A) 2 TB
   B) 6 TB
   C) 8 TB
   D) 10 TB

10. Una franja RAID 5 tiene D0 = 1011, D1 = 0101 y D2 = 1100. Si P = D0 ⊕ D1 ⊕ D2, ¿cuál es P?

   A) 0010
   B) 1100
   C) 1110
   D) 1111

11. Una videollamada ejecuta lógica de la app, un efecto de IA y codificación de vídeo. ¿Qué reparto se ajusta a la especialización descrita?

   A) Motor de vídeo para reglas de negocio y CPU solo para IA
   B) FPGA obligatoria para cualquier lógica de aplicación móvil
   C) NPU para toda la lógica y CPU exclusivamente para píxeles
   D) CPU para lógica, NPU para IA y motor de vídeo para codificar

12. Un algoritmo vuelve a leer la misma posición de memoria varias veces en un intervalo corto. ¿Qué propiedad manifiesta?

   A) Ausencia de localidad de memoria
   B) Acceso secuencial sin reutilización
   C) Localidad temporal
   D) Localidad espacial

13. ¿Qué operación básica acelerada por hardware destaca en un DSP para filtros y procesamiento repetitivo?

   A) Búsqueda y salto entre archivos del sistema
   B) Conversión entre UTF-8 y UTF-32
   C) Compresión y cifrado como una única operación MAC
   D) Multiplicación y acumulación (MAC)

14. ¿Qué distingue una implementación monolítica de una modular en las arquitecturas del tema?

   A) La monolítica integra el sistema en un chip; la modular combina varios chips
   B) La monolítica ejecuta un único programa; la modular permite varios usuarios
   C) La monolítica carece de memoria; la modular tiene memoria externa
   D) La monolítica es siempre FPGA; la modular es siempre ASIC

15. ¿Qué diferencia conceptual entre RISC y CISC recoge el temario?

   A) CISC tiene instrucciones de longitud fija y RISC las tiene todas variables
   B) RISC usa el repertorio más complejo y CISC prioriza instrucciones simples
   C) Solo CISC permite compilar programas escritos en lenguajes de alto nivel
   D) RISC prioriza instrucciones simples; CISC dispone de un repertorio más complejo

16. Una imagen de 512 × 512 píxeles usa 24 bits por píxel, sin compresión ni cabeceras. ¿Qué tamaño ocupa, tomando 1 MiB = 2²⁰ bytes?

   A) 0,25 MiB
   B) 0,75 MiB
   C) 2,25 MiB
   D) 6 MiB

17. Se necesita modificar el circuito de procesamiento después de fabricar el dispositivo. ¿Qué opción lo permite según la clasificación del tema?

   A) Un ASIC modular con más chips de la misma tarea
   B) Un ASIC de circuito fijo
   C) Un ASIC monolítico con más frecuencia de reloj
   D) Una FPGA reconfigurable

18. ¿Qué propiedad describe correctamente UTF-8?

   A) Representa solo los 128 caracteres del repertorio ASCII
   B) Usa cuatro bytes para todos los caracteres
   C) Usa entre uno y cuatro bytes y mantiene la codificación de ASCII
   D) Usa dos bytes para todo Unicode sin excepciones

19. Se escriben completos los tres bloques de datos nuevos de una franja RAID 5 de cuatro discos. Sin caché ni otras operaciones, ¿qué permite el full-stripe write?

   A) Convertir los cuatro discos en copias idénticas
   B) Leer siempre el dato antiguo y la paridad por cada bloque nuevo
   C) Calcular la paridad nueva sin leer los datos antiguos de esa franja
   D) Evitar escribir el bloque de paridad

20. En una escritura parcial RAID 5, P = 0010 y el dato D2 cambia de 1100 a 1000. ¿Qué nueva paridad resulta de P′ = P ⊕ D2viejo ⊕ D2nuevo?

   A) 0010
   B) 0100
   C) 0110
   D) 1010

21. ¿Qué propiedad de la visión humana aprovecha la compresión JPEG descrita en el tema?

   A) La percepción idéntica de todas las frecuencias y componentes de la imagen
   B) La mayor sensibilidad a cambios de color que a cambios de brillo
   C) La incapacidad de percibir detalles en cualquier zona uniforme
   D) La mayor sensibilidad a variaciones de luminancia que de crominancia

22. Una MMA recorre grandes flujos de datos con poca reutilización temporal. ¿Por qué sigue necesitando gran ancho de banda de memoria?

   A) Debe alimentar continuamente el procesamiento con muchos datos nuevos
   B) La baja reutilización garantiza que todos los datos estarán siempre en caché
   C) El procesador puede reconstruir todos los datos sin leer memoria
   D) Los operandos pequeños hacen innecesaria la transferencia de datos

23. Se configura un espejo RAID 1 con dos discos de 2 TB. Sin contar metadatos, ¿qué capacidad útil ofrece?

   A) 1 TB
   B) 2 TB
   C) 3 TB
   D) 4 TB

24. ¿Dónde se sitúa un DSP programable en el árbol de arquitecturas del tema?

   A) En las programables específicas, optimizadas para procesamiento de señal
   B) En las reconfigurables FPGA, porque ejecutar un filtro cambia sus conexiones
   C) En las programables de propósito general, sin especialización para señal
   D) En las dedicadas ASIC, porque ningún DSP admite cambiar su programa

25. ¿Qué pareja se corresponde con los modos de compresión descritos en el tema?

   A) PNG sin pérdida y JPEG convencional con pérdida
   B) PNG con pérdida y JPEG convencional sin pérdida
   C) JPEG convencional sin pérdida y WebP solo con pérdida
   D) GIF con pérdida y PNG con pérdida

26. En la clasificación del tema, ¿qué asociación entre familia y forma de adaptación es correcta?

   A) Programable: cambia conexiones físicas; ASIC: ejecuta cualquier software; FPGA: solo almacena
   B) Programable: circuito fijo sin instrucciones; ASIC: cambia su lógica; FPGA: solo cambia datos
   C) Programable: cambia instrucciones; ASIC: lógica reconfigurable; FPGA: circuito fijo
   D) Programable: cambia instrucciones; dedicada ASIC: circuito fijo; FPGA: lógica reconfigurable

27. Un filtro procesa píxeles consecutivos de cada fotograma y después pasa al siguiente sin volver a esos datos. ¿Qué patrón encaja con las MMA del tema?

   A) Alta localidad temporal y alta reutilización del mismo píxel
   B) Alta localidad temporal y baja localidad espacial
   C) Alta localidad espacial y baja localidad temporal de los datos
   D) Baja localidad espacial por acceder a píxeles vecinos

28. Se guardan 100 puntos de código del repertorio ASCII, sin BOM ni cabeceras. ¿Cuántos bytes necesita UTF-8?

   A) 100 bytes
   B) 200 bytes
   C) 400 bytes
   D) 800 bytes

29. ¿Qué ocurre si falla un disco de un RAID 0 sin otra copia de los datos?

   A) El conjunto pierde la disponibilidad íntegra de sus datos
   B) La paridad distribuida reconstruye el contenido
   C) El espejo conserva una copia completa
   D) El conjunto soporta hasta dos fallos simultáneos

30. Se comprime una fotografía con JPEG convencional usando una compresión cada vez más agresiva. ¿Qué compromiso debe evaluarse?

   A) Reducir el tamaño manteniendo igualdad exacta de todos los píxeles
   B) Aumentar la calidad original eliminando información de forma irreversible
   C) Evitar la descompresión porque los píxeles comprimidos se muestran directamente
   D) Reducir el tamaño frente a introducir pérdida de detalle y artefactos

31. En RAID 5, ¿cómo se coloca la paridad entre las distintas franjas?

   A) Se duplica cada bloque completo en todos los discos
   B) Va rotando entre los discos del conjunto
   C) Se guarda siempre en un único disco dedicado
   D) Se calcula sin guardar información redundante
