# DISM · T2.2 · Almacenamiento y arquitecturas

Elige una única respuesta por pregunta.

1. Una videollamada ejecuta lógica de la app, un efecto de IA y codificación de vídeo. ¿Qué reparto se ajusta a la especialización descrita?

   A) Motor de vídeo para reglas de negocio y CPU solo para IA
   B) CPU para lógica, NPU para IA y motor de vídeo para codificar
   C) FPGA obligatoria para cualquier lógica de aplicación móvil
   D) NPU para toda la lógica y CPU exclusivamente para píxeles

2. En la clasificación del tema, ¿qué asociación entre familia y forma de adaptación es correcta?

   A) Programable: cambia instrucciones; dedicada ASIC: circuito fijo; FPGA: lógica reconfigurable
   B) Programable: circuito fijo sin instrucciones; ASIC: cambia su lógica; FPGA: solo cambia datos
   C) Programable: cambia instrucciones; ASIC: lógica reconfigurable; FPGA: circuito fijo
   D) Programable: cambia conexiones físicas; ASIC: ejecuta cualquier software; FPGA: solo almacena

3. ¿Qué mecanismo caracteriza a LZW en el temario?

   A) Crear un código nuevo para cada aparición sin reutilizar entradas
   B) Descartar píxeles de color para que la imagen sea más pequeña
   C) Asignar a cada símbolo un código según un árbol de probabilidades
   D) Sustituir cadenas de símbolos por códigos de un diccionario

4. ¿Qué diferencia de tolerancia a fallos distingue RAID 6 de RAID 5?

   A) Ninguno soporta fallos porque no utiliza espejos
   B) RAID 6 soporta uno y RAID 5 dos
   C) RAID 6 soporta dos discos fallidos y RAID 5 uno
   D) Ambos soportan dos discos fallidos por usar XOR

5. Un RAID 10 se forma con parejas espejo A/B y C/D. Fallan A y B; C y D siguen operativos. ¿Puede el conjunto conservar todos sus datos?

   A) Sí, porque se reconstruye A/B con la paridad doble de C/D
   B) No, porque se han perdido las dos copias de una misma pareja
   C) Sí, porque RAID 10 soporta cualquier combinación de dos fallos
   D) Sí, porque la pareja C/D contiene también un espejo completo de A/B

6. ¿Qué asociación de tipos de paralelismo recoge el temario?

   A) SIMD y VLIW: únicamente paralelismo de instrucciones
   B) SIMD y VLIW: únicamente paralelismo sobre los datos
   C) SIMD: paralelismo de datos; VLIW: paralelismo de instrucciones
   D) SIMD: paralelismo de instrucciones; VLIW: paralelismo de datos

7. Una franja RAID 5 tiene D0 = 1011, D1 = 0101 y D2 = 1100. Si P = D0 ⊕ D1 ⊕ D2, ¿cuál es P?

   A) 0010
   B) 1100
   C) 1110
   D) 1111

8. Un algoritmo vuelve a leer la misma posición de memoria varias veces en un intervalo corto. ¿Qué propiedad manifiesta?

   A) Ausencia de localidad de memoria
   B) Localidad espacial
   C) Acceso secuencial sin reutilización
   D) Localidad temporal

9. Para cambiar un único bloque mediante Read-Modify-Write en RAID 5, sin caché previa, ¿qué información antigua se lee?

   A) Solo el bloque nuevo, porque la paridad anterior no interviene
   B) Solo la paridad, porque el dato antiguo se deduce del dato nuevo
   C) El bloque de datos que cambia y la paridad de su franja
   D) Todos los bloques de todas las franjas del conjunto

10. Se fabricarán muchas unidades para una tarea estable y se priorizan rendimiento y bajo consumo frente a flexibilidad. ¿Qué opción destaca el tema?

   A) Una FPGA elegida porque su principal ventaja es un circuito que nunca se puede cambiar
   B) Un procesador de propósito general por eliminar todo coste de ejecución
   C) Una CPU elegida únicamente por poder ejecutar cualquier programa
   D) Un ASIC dedicado a la tarea

11. Para un punto de código Unicode suplementario, fuera del BMP, ¿qué tamaños indica el tema para UTF-8, UTF-16 y UTF-32?

   A) UTF-8: 4 bytes; UTF-16: 2 bytes; UTF-32: 4 bytes
   B) UTF-8: 4 bytes; UTF-16: 4 bytes; UTF-32: 8 bytes
   C) UTF-8: 4 bytes; UTF-16: 4 bytes; UTF-32: 4 bytes
   D) UTF-8: 1 byte; UTF-16: 2 bytes; UTF-32: 4 bytes

12. Una franja tiene D0 = 0000 y D1 = 0000, con P = 0000. Ambos datos cambian a 0001. ¿Cuál es la nueva paridad XOR?

   A) 0000
   B) 0001
   C) 0010
   D) 0011

13. ¿Qué diferencia conceptual entre RISC y CISC recoge el temario?

   A) RISC prioriza instrucciones simples; CISC dispone de un repertorio más complejo
   B) Solo CISC permite compilar programas escritos en lenguajes de alto nivel
   C) RISC usa el repertorio más complejo y CISC prioriza instrucciones simples
   D) CISC tiene instrucciones de longitud fija y RISC las tiene todas variables

14. ¿Qué forma de codificación Unicode emplea cuatro bytes por punto de código?

   A) UTF-16
   B) UTF-32
   C) UTF-8
   D) ASCII de 7 bits

15. ¿Qué propiedad describe correctamente UTF-8?

   A) Usa cuatro bytes para todos los caracteres
   B) Usa dos bytes para todo Unicode sin excepciones
   C) Representa solo los 128 caracteres del repertorio ASCII
   D) Usa entre uno y cuatro bytes y mantiene la codificación de ASCII

16. ¿Qué idea utiliza Huffman para reducir la longitud media de una representación simbólica?

   A) Usar una longitud fija para todos sin considerar sus frecuencias
   B) Dar los códigos más largos a los símbolos más frecuentes
   C) Dar códigos más cortos a los símbolos más frecuentes
   D) Eliminar los símbolos menos frecuentes de la reconstrucción

17. Un filtro procesa píxeles consecutivos de cada fotograma y después pasa al siguiente sin volver a esos datos. ¿Qué patrón encaja con las MMA del tema?

   A) Alta localidad temporal y alta reutilización del mismo píxel
   B) Alta localidad temporal y baja localidad espacial
   C) Baja localidad espacial por acceder a píxeles vecinos
   D) Alta localidad espacial y baja localidad temporal de los datos

18. Se borra por error un archivo en un volumen RAID 1 y el borrado se refleja en ambos discos. ¿Qué medida habría permitido recuperar una versión anterior?

   A) Una copia de seguridad anterior al borrado
   B) Cambiar a RAID 0 para repartir el archivo
   C) Recalcular la paridad sobre el volumen ya modificado
   D) Añadir otro espejo que reproduzca el mismo borrado

19. Un RAID 6 utiliza seis discos iguales de 4 TB. Sin contar metadatos, ¿qué capacidad útil queda al reservar el equivalente de dos discos para redundancia?

   A) 8 TB
   B) 16 TB
   C) 20 TB
   D) 24 TB

20. Un procesador conserva sus circuitos y cambia de algoritmo ejecutando otro programa. ¿Qué familia describe esa forma de adaptación?

   A) Un circuito ASIC que cambia físicamente al cargar cada archivo
   B) Una FPGA que necesariamente cambia sus interconexiones con cada dato
   C) Un sistema de almacenamiento que alterna el nivel RAID
   D) Una arquitectura programable

21. En RAID 5, ¿cómo se coloca la paridad entre las distintas franjas?

   A) Se duplica cada bloque completo en todos los discos
   B) Se calcula sin guardar información redundante
   C) Se guarda siempre en un único disco dedicado
   D) Va rotando entre los discos del conjunto

22. Un texto contiene solo ideogramas del BMP que necesitan tres bytes en UTF-8 y una unidad en UTF-16. Sin cabeceras ni BOM, ¿qué representación usa menos espacio por esos puntos de código?

   A) UTF-8, con un byte por punto de código
   B) UTF-16, con dos bytes por punto de código
   C) UTF-32, con un byte por punto de código
   D) Las tres ocupan lo mismo por tratarse de Unicode

23. Se crea un RAID 1 con un disco de 2 TB y otro de 3 TB. Sin metadatos ni configuraciones especiales, ¿qué capacidad de datos ofrece el espejo?

   A) 2 TB
   B) 3 TB
   C) 4 TB
   D) 5 TB

24. ¿Qué pareja se corresponde con los modos de compresión descritos en el tema?

   A) GIF con pérdida y PNG con pérdida
   B) JPEG convencional sin pérdida y WebP solo con pérdida
   C) PNG con pérdida y JPEG convencional sin pérdida
   D) PNG sin pérdida y JPEG convencional con pérdida

25. ¿Qué operación básica acelerada por hardware destaca en un DSP para filtros y procesamiento repetitivo?

   A) Búsqueda y salto entre archivos del sistema
   B) Multiplicación y acumulación (MAC)
   C) Conversión entre UTF-8 y UTF-32
   D) Compresión y cifrado como una única operación MAC

26. Se configura un espejo RAID 1 con dos discos de 2 TB. Sin contar metadatos, ¿qué capacidad útil ofrece?

   A) 1 TB
   B) 2 TB
   C) 3 TB
   D) 4 TB

27. Una MMA recorre grandes flujos de datos con poca reutilización temporal. ¿Por qué sigue necesitando gran ancho de banda de memoria?

   A) El procesador puede reconstruir todos los datos sin leer memoria
   B) La baja reutilización garantiza que todos los datos estarán siempre en caché
   C) Debe alimentar continuamente el procesamiento con muchos datos nuevos
   D) Los operandos pequeños hacen innecesaria la transferencia de datos

28. Un archivo debe recuperar exactamente todos sus datos originales después de descomprimirlo. ¿Qué clase de compresión se requiere?

   A) Sin pérdida (lossless)
   B) Con pérdida (lossy)
   C) Con pérdida y calidad visual alta
   D) Con pérdida seguida de ampliación de resolución

29. Un sistema combina varios chips ASIC de función fija. ¿Qué clasificación encaja con los dos ejes usados en el tema?

   A) Programable de propósito general y monolítico
   B) Reconfigurable y modular por el hecho de tener varios chips
   C) Dedicado y monolítico por tratarse de ASIC
   D) Dedicado y modular

30. En una franja RAID 5 sobreviven D0 = 0101, D1 = 0011 y D2 = 1000. Falta el bloque de paridad P. ¿Qué valor se reconstruye?

   A) 0110
   B) 1011
   C) 1110
   D) 1111

31. Se escriben completos los tres bloques de datos nuevos de una franja RAID 5 de cuatro discos. Sin caché ni otras operaciones, ¿qué permite el full-stripe write?

   A) Leer siempre el dato antiguo y la paridad por cada bloque nuevo
   B) Convertir los cuatro discos en copias idénticas
   C) Evitar escribir el bloque de paridad
   D) Calcular la paridad nueva sin leer los datos antiguos de esa franja

32. ¿Qué distingue una implementación monolítica de una modular en las arquitecturas del tema?

   A) La monolítica integra el sistema en un chip; la modular combina varios chips
   B) La monolítica es siempre FPGA; la modular es siempre ASIC
   C) La monolítica ejecuta un único programa; la modular permite varios usuarios
   D) La monolítica carece de memoria; la modular tiene memoria externa

33. Falta D1 en una franja con D0 = 1011, D2 = 1100 y P = 0010. ¿Qué bloque se recupera mediante P ⊕ D0 ⊕ D2?

   A) 0000
   B) 0101
   C) 0111
   D) 1001

34. ¿Dónde se sitúa un DSP programable en el árbol de arquitecturas del tema?

   A) En las programables específicas, optimizadas para procesamiento de señal
   B) En las reconfigurables FPGA, porque ejecutar un filtro cambia sus conexiones
   C) En las programables de propósito general, sin especialización para señal
   D) En las dedicadas ASIC, porque ningún DSP admite cambiar su programa

35. Un RAID 10 tiene dos parejas espejo: discos A/B y discos C/D. Fallan A y C y sus compañeros siguen operativos. ¿Qué ocurre con los datos del conjunto?

   A) Se pierden porque RAID 10 solo tolera un fallo en todo el conjunto
   B) Siguen accesibles porque queda una copia de cada pareja
   C) Se recuperan mediante la doble paridad de A y C
   D) Solo queda accesible la mitad que estaba en B

36. Se guardan 100 puntos de código del repertorio ASCII, sin BOM ni cabeceras. ¿Cuántos bytes necesita UTF-8?

   A) 100 bytes
   B) 200 bytes
   C) 400 bytes
   D) 800 bytes

37. Se necesita modificar el circuito de procesamiento después de fabricar el dispositivo. ¿Qué opción lo permite según la clasificación del tema?

   A) Una FPGA reconfigurable
   B) Un ASIC monolítico con más frecuencia de reloj
   C) Un ASIC de circuito fijo
   D) Un ASIC modular con más chips de la misma tarea

38. Una imagen de 512 × 512 píxeles usa 24 bits por píxel, sin compresión ni cabeceras. ¿Qué tamaño ocupa, tomando 1 MiB = 2²⁰ bytes?

   A) 0,25 MiB
   B) 0,75 MiB
   C) 2,25 MiB
   D) 6 MiB

39. Un bucle pequeño se ejecuta miles de veces mientras procesa datos nuevos que apenas relee. ¿Qué combinación es coherente?

   A) Imposibilidad de aprovechar caché para las instrucciones del bucle
   B) Baja reutilización del código porque cada dato de entrada es nuevo
   C) Alta reutilización temporal de todos los datos porque se repite el bucle
   D) Alta reutilización temporal del código y baja de los datos del flujo

40. En una escritura parcial RAID 5, P = 0010 y el dato D2 cambia de 1100 a 1000. ¿Qué nueva paridad resulta de P′ = P ⊕ D2viejo ⊕ D2nuevo?

   A) 0010
   B) 0100
   C) 0110
   D) 1010

41. Un RAID 5 usa cinco discos de 2 TB. Suponiendo discos iguales y sin metadatos, ¿cuánta capacidad útil tiene?

   A) 2 TB
   B) 6 TB
   C) 8 TB
   D) 10 TB

42. ¿Qué propiedad de la visión humana aprovecha la compresión JPEG descrita en el tema?

   A) La incapacidad de percibir detalles en cualquier zona uniforme
   B) La mayor sensibilidad a cambios de color que a cambios de brillo
   C) La mayor sensibilidad a variaciones de luminancia que de crominancia
   D) La percepción idéntica de todas las frecuencias y componentes de la imagen

43. Se comprime una fotografía con JPEG convencional usando una compresión cada vez más agresiva. ¿Qué compromiso debe evaluarse?

   A) Reducir el tamaño manteniendo igualdad exacta de todos los píxeles
   B) Evitar la descompresión porque los píxeles comprimidos se muestran directamente
   C) Reducir el tamaño frente a introducir pérdida de detalle y artefactos
   D) Aumentar la calidad original eliminando información de forma irreversible

44. ¿Cuál es el mínimo de discos que necesita un RAID 5 según el temario?

   A) 2 discos
   B) 3 discos
   C) 4 discos
   D) 5 discos

45. ¿Qué ocurre si falla un disco de un RAID 0 sin otra copia de los datos?

   A) El conjunto pierde la disponibilidad íntegra de sus datos
   B) El espejo conserva una copia completa
   C) El conjunto soporta hasta dos fallos simultáneos
   D) La paridad distribuida reconstruye el contenido

46. Se actualiza un bloque de datos RAID 5 con Read-Modify-Write, sin caché previa. ¿Qué accesos lógicos a disco describe el tema?

   A) Cero lecturas y dos escrituras
   B) Una lectura y una escritura
   C) Dos lecturas y dos escrituras
   D) Tres lecturas y una escritura
