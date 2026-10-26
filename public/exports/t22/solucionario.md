# Solucionario: DISM · T2.2 · Almacenamiento y arquitecturas

## 1. B) CPU para lógica, NPU para IA y motor de vídeo para codificar

Un SoC puede combinar bloques y asignar tareas a los más adecuados: CPU general, NPU para redes neuronales y motor multimedia para códecs. Esto reduce trabajo y consumo en los bloques generales.

Fuente: Tema2-DISM-2.pdf, páginas PDF 47, 59–63.

Distractores:

- A) El motor de vídeo no es el bloque general de reglas de negocio.
- C) Una FPGA no es un requisito para ejecutar la app en un SoC.
- D) Invierte las especializaciones y obliga a la NPU a tareas generales.

## 2. A) Programable: cambia instrucciones; dedicada ASIC: circuito fijo; FPGA: lógica reconfigurable

El árbol de la página 47 distingue programables, dedicadas y reconfigurables. El programa adapta la secuencia de instrucciones; el ASIC dedica su circuito a una tarea; la FPGA permite reconfigurar su lógica.

Fuente: Tema2-DISM-2.pdf, páginas PDF 47, 61–63.

Distractores:

- B) Atribuye la reconfiguración al ASIC e impide a la FPGA adaptar la lógica.
- C) Intercambia las propiedades de ASIC y FPGA.
- D) Confunde el software programable, el circuito dedicado y el hardware reconfigurable.

## 3. D) Sustituir cadenas de símbolos por códigos de un diccionario

LZW mantiene una tabla de cadenas y puede sustituir una cadena por su código. El tema lo relaciona con GIF y lo distingue de los códigos de símbolos individuales.

Fuente: Tema2-DISM-2.pdf, páginas PDF 28, 34.

Distractores:

- A) El diccionario permite reutilizar códigos de cadenas; renunciar a ello no explica la compresión descrita.
- B) Eso describe pérdida de información, no la sustitución de cadenas de LZW.
- C) Esa descripción corresponde a la codificación simbólica de Huffman, no al diccionario de cadenas de LZW.

## 4. C) RAID 6 soporta dos discos fallidos y RAID 5 uno

RAID 5 utiliza una redundancia de paridad; RAID 6 añade una segunda. Por eso RAID 6 permite reconstruir ante dos discos fallidos.

Fuente: Tema2-DISM-2.pdf, páginas PDF 8, 14–15.

Distractores:

- A) La paridad también proporciona tolerancia a fallos; no se limita a los espejos.
- B) Invierte la tolerancia que proporciona la doble paridad.
- D) Una sola paridad de RAID 5 no permite resolver dos bloques perdidos de una franja.

## 5. B) No, porque se han perdido las dos copias de una misma pareja

La división se hace entre parejas reflejadas. Si desaparece una pareja completa, falta una parte de los datos aunque sobrevivan los discos de la otra.

Fuente: Tema2-DISM-2.pdf, páginas PDF 16.

Distractores:

- A) RAID 10 no utiliza la doble paridad propia de RAID 6.
- C) La tolerancia depende de qué discos fallen, no solo de su número.
- D) Las parejas contienen partes distintas del conjunto; cada una refleja sus propios datos.

## 6. C) SIMD: paralelismo de datos; VLIW: paralelismo de instrucciones

SIMD aplica operaciones a varios datos y VLIW explota paralelismo a nivel de instrucciones. El tema los presenta entre las técnicas para acelerar procesamiento multimedia.

Fuente: Tema2-DISM-2.pdf, páginas PDF 48, 56.

Distractores:

- A) SIMD se asocia al procesamiento paralelo de varios datos.
- B) VLIW se asocia al paralelismo a nivel de instrucciones.
- D) Invierte los tipos de paralelismo asociados a ambas técnicas.

## 7. A) 0010

1011 ⊕ 0101 = 1110; después 1110 ⊕ 1100 = 0010. XOR produce 1 cuando los bits comparados son diferentes.

Fuente: Tema2-DISM-2.pdf, páginas PDF 9, 13.

Distractores:

- B) Repite D2 sin combinar los otros bloques de datos.
- C) Es el XOR de D0 y D1, pero falta combinar D2.
- D) Se obtiene al usar OR en lugar de XOR con esos bloques.

## 8. D) Localidad temporal

Hay localidad temporal cuando una posición referenciada tiene probabilidad de usarse de nuevo pronto. La caché puede aprovechar esa reutilización.

Fuente: Tema2-DISM-2.pdf, páginas PDF 45.

Distractores:

- A) La reutilización cercana en el tiempo es precisamente una forma de localidad.
- B) La espacial se refiere a posiciones próximas, no a repetir la misma.
- C) La repetición del mismo dato no es un recorrido sin reutilización.

## 9. C) El bloque de datos que cambia y la paridad de su franja

La actualización utiliza P nueva = P antigua XOR dato antiguo XOR dato nuevo. En ese procedimiento se leen dato y paridad antiguos y luego se escriben los nuevos.

Fuente: Tema2-DISM-2.pdf, páginas PDF 10–11.

Distractores:

- A) Para actualizar por XOR la paridad se necesitan las contribuciones antiguas.
- B) No puede deducirse en general el valor antiguo a partir del nuevo.
- D) El procedimiento no requiere releer todo el volumen.

## 10. D) Un ASIC dedicado a la tarea

El ASIC puede proporcionar gran eficiencia para una tarea fija, a costa de diseño costoso y poca flexibilidad. El volumen de fabricación ayuda a justificar ese coste.

Fuente: Tema2-DISM-2.pdf, páginas PDF 61, 63.

Distractores:

- A) La ventaja distintiva de una FPGA es precisamente su reconfigurabilidad.
- B) Ejecutar programas generales no elimina costes de cómputo ni consumo.
- C) La flexibilidad general no es la prioridad indicada en el caso.

## 11. C) UTF-8: 4 bytes; UTF-16: 4 bytes; UTF-32: 4 bytes

UTF-8 utiliza cuatro bytes para estos puntos de código; UTF-16 usa un par de unidades de 16 bits, también cuatro bytes; UTF-32 emplea cuatro bytes. Se pregunta por punto de código, no por carácter visual.

Fuente: Tema2-DISM-2.pdf, páginas PDF 23.

Distractores:

- A) UTF-16 necesita un par de unidades de 16 bits para ese punto de código.
- B) UTF-32 mantiene una unidad de 32 bits por punto de código, no dos.
- D) Los tamaños de uno y dos bytes no bastan para el punto suplementario especificado.

## 12. A) 0000

0001 XOR 0001 = 0000. Que la paridad no cambie no significa que los datos sean idénticos: la paridad no es una copia completa de ellos.

Fuente: Tema2-DISM-2.pdf, páginas PDF 9–11.

Distractores:

- B) Equivale a aplicar solo uno de los dos cambios; los dos bits a 1 se cancelan mediante XOR.
- C) Trata los cambios como una suma binaria con acarreo, no como XOR.
- D) Activa posiciones que no aparecen en el XOR de los datos nuevos.

## 13. A) RISC prioriza instrucciones simples; CISC dispone de un repertorio más complejo

Dentro de las programables de propósito general, RISC se asocia con instrucciones frecuentes y simples y CISC con un juego más rico y complejo. No son familias RAID ni sinónimos de FPGA.

Fuente: Tema2-DISM-2.pdf, páginas PDF 47, 49–50.

Distractores:

- B) Ambas familias pueden ejecutar programas compilados desde lenguajes de alto nivel.
- C) Invierte la distinción conceptual presentada en el tema.
- D) No corresponde a la caracterización del tema, que destaca la longitud variable en CISC.

## 14. B) UTF-32

UTF-32 representa cada punto de código Unicode en una unidad de 32 bits. Un carácter visual puede componerse de varios puntos de código; no hay que confundir ambas magnitudes.

Fuente: Tema2-DISM-2.pdf, páginas PDF 23.

Distractores:

- A) UTF-16 utiliza una o dos unidades de 16 bits, no cuatro bytes para todos los puntos de código.
- C) UTF-8 utiliza de uno a cuatro bytes, según el punto de código.
- D) ASCII tiene un repertorio limitado y no es una codificación de todo Unicode en cuatro bytes.

## 15. D) Usa entre uno y cuatro bytes y mantiene la codificación de ASCII

UTF-8 utiliza un byte para ASCII y secuencias más largas para otros caracteres Unicode, hasta cuatro bytes. «UTFS» en las indicaciones se interpreta aquí como UTF-8, presente en la página 23.

Fuente: Tema2-DISM-2.pdf, páginas PDF 23, 25.

Distractores:

- A) El tamaño fijo de cuatro bytes corresponde a UTF-32.
- B) UTF-8 es variable; incluso UTF-16 necesita pares para caracteres complementarios.
- C) UTF-8 representa Unicode, no únicamente ASCII.

## 16. C) Dar códigos más cortos a los símbolos más frecuentes

La asignación de longitudes tiene en cuenta las frecuencias de los símbolos. La idea es reducir el coste medio conservando una representación decodificable.

Fuente: Tema2-DISM-2.pdf, páginas PDF 27.

Distractores:

- A) No aprovecha la distribución de probabilidad para variar el coste de cada símbolo.
- B) Eso aumenta el coste medio de los símbolos que más aparecen.
- D) Descartar símbolos perdería información; no es el mecanismo de Huffman.

## 17. D) Alta localidad espacial y baja localidad temporal de los datos

El acceso a píxeles vecinos aporta localidad espacial. Recorrer el flujo sin regresar a los datos reduce la localidad temporal, aunque el código del bucle sí pueda reutilizarse.

Fuente: Tema2-DISM-2.pdf, páginas PDF 45–46.

Distractores:

- A) El enunciado especifica que los datos no se vuelven a usar.
- B) Invierte el patrón: se visitan vecinos y apenas se reutilizan los datos.
- C) Acceder a posiciones contiguas favorece la localidad espacial.

## 18. A) Una copia de seguridad anterior al borrado

La redundancia RAID mejora disponibilidad ante fallos de discos, pero no sustituye copias con versiones anteriores. Un borrado válido puede propagarse a la información redundante.

Fuente: Tema2-DISM-2.pdf, páginas PDF 19.

Distractores:

- B) RAID 0 no mantiene versiones ni aporta recuperación de borrados.
- C) La paridad protege frente a determinados fallos físicos, no conserva por sí misma el archivo anterior.
- D) Otra copia sincronizada del volumen reproduce también el borrado.

## 19. B) 16 TB

La capacidad es (6 − 2)×4 TB = 16 TB. El equivalente de dos discos corresponde a la redundancia de RAID 6.

Fuente: Tema2-DISM-2.pdf, páginas PDF 14–15.

Distractores:

- A) Descuenta cuatro discos equivalentes, más redundancia de la indicada.
- C) Descuenta solo un disco, como en el cálculo de capacidad de RAID 5.
- D) Suma toda la capacidad física sin descontar la doble paridad.

## 20. D) Una arquitectura programable

El comportamiento se adapta mediante instrucciones sobre el hardware disponible. Esto se distingue de reconfigurar la lógica de una FPGA o de utilizar un circuito dedicado fijo.

Fuente: Tema2-DISM-2.pdf, páginas PDF 47–48, 63.

Distractores:

- A) Cargar otro programa no modifica físicamente un ASIC.
- B) No se ha descrito una reconfiguración de hardware ni un cambio por cada dato.
- C) Cambiar el programa del procesador no equivale a reorganizar discos.

## 21. D) Va rotando entre los discos del conjunto

La paridad es distribuida: su disco cambia de una franja a otra. Dentro de una franja, un bloque de paridad permite reconstruir un bloque de datos ausente.

Fuente: Tema2-DISM-2.pdf, páginas PDF 7–9.

Distractores:

- A) Eso describe un espejo, no paridad distribuida.
- B) RAID 5 almacena paridad para poder reconstruir un fallo.
- C) La paridad fija caracteriza a otros esquemas, como RAID 4, no a RAID 5.

## 22. B) UTF-16, con dos bytes por punto de código

Con las condiciones dadas, UTF-16 usa 2 bytes, UTF-8 usa 3 y UTF-32 usa 4. La ventaja de espacio de UTF-8 en textos ASCII no se generaliza a todos los repertorios.

Fuente: Tema2-DISM-2.pdf, páginas PDF 23, 25–26.

Distractores:

- A) Un byte en UTF-8 corresponde a ASCII, no a los ideogramas especificados.
- C) UTF-32 utiliza cuatro bytes, no uno.
- D) Unicode no obliga a que todas sus codificaciones tengan el mismo tamaño.

## 23. A) 2 TB

El espejo conserva copias de los mismos datos. Su capacidad útil queda limitada por el menor disco: 2 TB.

Fuente: Tema2-DISM-2.pdf, páginas PDF 6.

Distractores:

- B) El disco menor no puede contener una copia completa de 3 TB.
- C) Duplicar la capacidad del disco menor cuenta dos veces los mismos datos.
- D) Suma las capacidades físicas como si los discos almacenaran datos distintos.

## 24. D) PNG sin pérdida y JPEG convencional con pérdida

El tema presenta PNG como lossless y JPEG convencional como lossy. JPEG 2000 y WebP permiten otros modos; por eso el enunciado acota el JPEG convencional.

Fuente: Tema2-DISM-2.pdf, páginas PDF 34–36.

Distractores:

- A) La compresión GIF mediante LZW y la de PNG son sin pérdida; limitar la paleta es otra operación.
- B) JPEG convencional es lossy y WebP admite modos lossy y lossless.
- C) Invierte los modos habituales descritos para ambos formatos.

## 25. B) Multiplicación y acumulación (MAC)

La operación MAC multiplica operandos y acumula el resultado. Es muy frecuente en filtros digitales y otros algoritmos numéricos de señal.

Fuente: Tema2-DISM-2.pdf, páginas PDF 52–53, 57.

Distractores:

- A) No es la operación aritmética característica que destaca el tema.
- C) La conversión de caracteres no define la unidad MAC de un DSP.
- D) MAC aquí significa multiply-accumulate, no compresión y cifrado.

## 26. B) 2 TB

Cada disco contiene la misma información. Un espejo de dos unidades iguales ofrece la capacidad de una: 2 TB.

Fuente: Tema2-DISM-2.pdf, páginas PDF 6.

Distractores:

- A) Divide otra vez la capacidad de un disco, aunque cada disco ya contiene la copia completa.
- C) Descuenta media unidad sin una regla de capacidad propia de un espejo.
- D) Suma la capacidad física sin descontar que el segundo disco duplica los datos.

## 27. C) Debe alimentar continuamente el procesamiento con muchos datos nuevos

Las MMA pueden reutilizar el código de sus bucles y, al mismo tiempo, consumir datos nuevos a gran ritmo. Eso exige memoria y E/S capaces de sostener el flujo.

Fuente: Tema2-DISM-2.pdf, páginas PDF 44–46.

Distractores:

- A) El cómputo necesita recibir los datos de entrada del flujo.
- B) La poca reutilización temporal reduce la ayuda de guardar copias para accesos repetidos.
- D) Aunque cada operando sea pequeño, se procesan muchos y con frecuencia.

## 28. A) Sin pérdida (lossless)

La propiedad definitoria de lossless es reconstruir exactamente la información original. La fidelidad perceptiva de un algoritmo lossy es una cuestión distinta.

Fuente: Tema2-DISM-2.pdf, páginas PDF 32.

Distractores:

- B) Lossy descarta información y no garantiza la reconstrucción exacta.
- C) Que la diferencia no se aprecie no implica igualdad exacta de datos.
- D) Ampliar la resolución no recupera la información descartada.

## 29. D) Dedicado y modular

Dedicado/reconfigurable/programable y monolítico/modular son clasificaciones diferentes. Varios chips de función fija forman una realización dedicada modular.

Fuente: Tema2-DISM-2.pdf, páginas PDF 47, 61–62.

Distractores:

- A) El caso especifica varios chips de función fija, no un único procesador general.
- B) Modular describe varios chips; no implica que su lógica sea reconfigurable.
- C) Ser ASIC no obliga a integrar todo el sistema en un único chip.

## 30. C) 1110

P = 0101 XOR 0011 XOR 1000 = 0110 XOR 1000 = 1110. Perder el bloque de paridad de una franja no obliga a perder los datos que siguen disponibles.

Fuente: Tema2-DISM-2.pdf, páginas PDF 9, 11.

Distractores:

- A) Es solo D0 XOR D1; falta incorporar el tercer bloque.
- B) Es D1 XOR D2, sin incorporar D0.
- D) Combina los bits mediante OR, en lugar de calcular el XOR de los tres bloques.

## 31. D) Calcular la paridad nueva sin leer los datos antiguos de esa franja

Al disponer de todos los datos nuevos, la controladora calcula su XOR directamente. En el ejemplo se escriben tres bloques de datos y uno de paridad.

Fuente: Tema2-DISM-2.pdf, páginas PDF 10.

Distractores:

- A) Eso aplica el coste de pequeñas escrituras parciales al caso de franja completa.
- B) Un full-stripe write no transforma RAID 5 en un espejo.
- C) Aunque no se lean los datos viejos, hay que guardar la paridad nueva.

## 32. A) La monolítica integra el sistema en un chip; la modular combina varios chips

La distinción monolítica/modular describe la integración física. Es un eje diferente de programable, dedicado o reconfigurable.

Fuente: Tema2-DISM-2.pdf, páginas PDF 47, 61–62.

Distractores:

- B) La distinción de uno o varios chips puede aplicarse a diferentes familias.
- C) Monolítico/modular se refiere aquí a la implementación física, no al número de programas o usuarios.
- D) El número de chips no impone esa ausencia de memoria.

## 33. B) 0101

0010 ⊕ 1011 = 1001 y 1001 ⊕ 1100 = 0101. El XOR permite despejar el único bloque ausente.

Fuente: Tema2-DISM-2.pdf, páginas PDF 9, 13.

Distractores:

- A) Sería cancelar cada bloque con una copia idéntica, que no es la operación pedida.
- C) Combina D0 y D2 pero omite la paridad P.
- D) Es el resultado parcial P ⊕ D0; falta aplicar XOR con D2.

## 34. A) En las programables específicas, optimizadas para procesamiento de señal

En la clasificación, ser específico indica optimización para una clase de tareas. Un DSP puede seguir siendo programable; no debe confundirse esa especialización con la rama de ASIC dedicados.

Fuente: Tema2-DISM-2.pdf, páginas PDF 47, 51–53, 63.

Distractores:

- B) Cambiar el programa de un DSP no equivale a reconfigurar bloques e interconexiones de una FPGA.
- C) El DSP del caso está optimizado para algoritmos de señal y se sitúa entre las programables específicas.
- D) Un DSP programable permite cambiar instrucciones; especialización no significa circuito ASIC fijo.

## 35. B) Siguen accesibles porque queda una copia de cada pareja

La tolerancia depende de qué discos fallen. A y C pertenecen a parejas distintas y B/D conservan sus datos. Perder A y B sí eliminaría una pareja completa.

Fuente: Tema2-DISM-2.pdf, páginas PDF 16.

Distractores:

- A) Puede tolerar más de un fallo si no se pierden todas las copias de una pareja.
- C) RAID 10 utiliza espejos y división de datos, no doble paridad.
- D) D conserva la copia de C; no se pierde esa mitad de los datos.

## 36. A) 100 bytes

Cada punto de código ASCII ocupa un byte en UTF-8: 100×1 = 100 bytes. En las condiciones del enunciado serían 200 en UTF-16 y 400 en UTF-32.

Fuente: Tema2-DISM-2.pdf, páginas PDF 23, 25.

Distractores:

- B) Cuenta dos bytes por punto de código como en UTF-16 para este repertorio.
- C) Aplica el tamaño fijo de UTF-32 en lugar de UTF-8.
- D) Confunde bits y bytes o multiplica por ocho una cantidad que ya está en bytes.

## 37. A) Una FPGA reconfigurable

La FPGA ofrece bloques lógicos e interconexiones programables. El ASIC dedica su circuito a una tarea y prioriza eficiencia frente a flexibilidad.

Fuente: Tema2-DISM-2.pdf, páginas PDF 61–63.

Distractores:

- B) Cambiar la frecuencia no modifica el circuito fijo del ASIC.
- C) El ASIC dedicado no cambia su circuito tras fabricarse.
- D) Añadir chips fijos no proporciona la reconfiguración lógica solicitada.

## 38. B) 0,75 MiB

512 × 512 × 24 / 8 = 786 432 bytes. Al dividir entre 1 048 576 bytes/MiB se obtiene 0,75 MiB.

Fuente: Tema2-DISM-2.pdf, páginas PDF 30.

Distractores:

- A) Equivale a contar un byte por píxel en lugar de tres.
- C) Aplica de nuevo el factor de tres después de haberlo incluido.
- D) Es el número de mebibits; falta dividir entre ocho para pasarlo a bytes.

## 39. D) Alta reutilización temporal del código y baja de los datos del flujo

Hay que distinguir qué se reutiliza. El código puede ejecutarse repetidamente y tener alta localidad temporal, mientras los datos entran como un flujo con poca reutilización.

Fuente: Tema2-DISM-2.pdf, páginas PDF 44–46.

Distractores:

- A) Un código pequeño y repetido puede beneficiarse de permanecer accesible en memoria rápida.
- B) Que cambien los datos no impide repetir las mismas instrucciones del bucle.
- C) Repetir instrucciones no significa volver a usar los mismos datos.

## 40. C) 0110

0010 ⊕ 1100 = 1110; 1110 ⊕ 1000 = 0110. Hay que quitar la contribución antigua y añadir la nueva mediante XOR.

Fuente: Tema2-DISM-2.pdf, páginas PDF 10–13.

Distractores:

- A) Mantiene la paridad anterior pese a haber cambiado el dato.
- B) Es el XOR entre dato viejo y nuevo, pero falta combinar la paridad anterior.
- D) Combina P con el nuevo dato y omite retirar el efecto del dato viejo.

## 41. C) 8 TB

RAID 5 utiliza el equivalente de un disco para paridad distribuida. La capacidad es (5 − 1) × 2 TB = 8 TB.

Fuente: Tema2-DISM-2.pdf, páginas PDF 7–9.

Distractores:

- A) Calcula como si todos los discos fueran copias de un único espejo.
- B) Resta dos discos equivalentes, como en RAID 6.
- D) Cuenta todos los discos como datos y omite la capacidad equivalente destinada a paridad.

## 42. C) La mayor sensibilidad a variaciones de luminancia que de crominancia

La visión no responde por igual al brillo y al color ni a todas las variaciones espaciales. Esa diferencia permite reducir información perceptivamente menos relevante.

Fuente: Tema2-DISM-2.pdf, páginas PDF 35.

Distractores:

- A) El tema indica que pequeñas variaciones de brillo se perciben con facilidad en zonas homogéneas.
- B) Invierte la relación perceptiva que presenta el tema.
- D) La compresión perceptiva aprovecha precisamente sensibilidades diferentes.

## 43. C) Reducir el tamaño frente a introducir pérdida de detalle y artefactos

La compresión con pérdida descarta información. Una reducción de tamaño mayor puede hacer visibles errores de reconstrucción; ampliar después el archivo no recupera los datos originales.

Fuente: Tema2-DISM-2.pdf, páginas PDF 32, 34–35.

Distractores:

- A) JPEG convencional es con pérdida; esa igualdad exacta no está garantizada.
- B) La información codificada necesita decodificarse para reconstruir la imagen.
- D) Descartar información no crea detalle original nuevo.

## 44. B) 3 discos

RAID 5 necesita como mínimo tres discos para distribuir datos y paridad. El número del nivel no indica cuántos discos deben instalarse.

Fuente: Tema2-DISM-2.pdf, páginas PDF 7–9.

Distractores:

- A) Dos unidades permiten otros esquemas, pero RAID 5 requiere al menos tres.
- C) Cuatro es un tamaño posible, pero no el mínimo de RAID 5.
- D) El número 5 designa el nivel RAID, no la cantidad mínima de discos.

## 45. A) El conjunto pierde la disponibilidad íntegra de sus datos

RAID 0 reparte datos entre discos para aumentar capacidad y rendimiento, pero no aporta redundancia. El fallo de uno compromete los datos del conjunto.

Fuente: Tema2-DISM-2.pdf, páginas PDF 5.

Distractores:

- B) RAID 0 no crea espejos; eso caracteriza a RAID 1.
- C) Esa tolerancia corresponde a RAID 6, no a RAID 0.
- D) RAID 0 no mantiene paridad.

## 46. C) Dos lecturas y dos escrituras

Se leen el dato antiguo y la paridad antigua, se calcula la nueva paridad y se escriben dato y paridad nuevos: cuatro accesos lógicos.

Fuente: Tema2-DISM-2.pdf, páginas PDF 10–11.

Distractores:

- A) Sin caché se necesitan el dato viejo y la paridad vieja.
- B) Falta leer y escribir la paridad, además del dato.
- D) En el caso indicado se actualizan tanto el dato como la paridad.
