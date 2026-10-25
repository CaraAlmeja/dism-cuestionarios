# Solucionario: DISM · T2.2 · Almacenamiento y arquitecturas

## 1. C) Dos lecturas y dos escrituras

Se leen el dato antiguo y la paridad antigua, se calcula la nueva paridad y se escriben dato y paridad nuevos: cuatro accesos lógicos.

Fuente: Tema2-DISM-2.pdf, páginas PDF 10–11.

Distractores:

- A) Falta leer y escribir la paridad, además del dato.
- B) En el caso indicado se actualizan tanto el dato como la paridad.
- D) Sin caché se necesitan el dato viejo y la paridad vieja.

## 2. B) 0101

0010 ⊕ 1011 = 1001 y 1001 ⊕ 1100 = 0101. El XOR permite despejar el único bloque ausente.

Fuente: Tema2-DISM-2.pdf, páginas PDF 9, 13.

Distractores:

- A) Sería cancelar cada bloque con una copia idéntica, que no es la operación pedida.
- C) Combina D0 y D2 pero omite la paridad P.
- D) Es el resultado parcial P ⊕ D0; falta aplicar XOR con D2.

## 3. B) Siguen accesibles porque queda una copia de cada pareja

La tolerancia depende de qué discos fallen. A y C pertenecen a parejas distintas y B/D conservan sus datos. Perder A y B sí eliminaría una pareja completa.

Fuente: Tema2-DISM-2.pdf, páginas PDF 16.

Distractores:

- A) RAID 10 utiliza espejos y división de datos, no doble paridad.
- C) D conserva la copia de C; no se pierde esa mitad de los datos.
- D) Puede tolerar más de un fallo si no se pierden todas las copias de una pareja.

## 4. B) UTF-16, con dos bytes por punto de código

Con las condiciones dadas, UTF-16 usa 2 bytes, UTF-8 usa 3 y UTF-32 usa 4. La ventaja de espacio de UTF-8 en textos ASCII no se generaliza a todos los repertorios.

Fuente: Tema2-DISM-2.pdf, páginas PDF 23, 25–26.

Distractores:

- A) Un byte en UTF-8 corresponde a ASCII, no a los ideogramas especificados.
- C) Unicode no obliga a que todas sus codificaciones tengan el mismo tamaño.
- D) UTF-32 utiliza cuatro bytes, no uno.

## 5. C) RAID 6 soporta dos discos fallidos y RAID 5 uno

RAID 5 utiliza una redundancia de paridad; RAID 6 añade una segunda. Por eso RAID 6 permite reconstruir ante dos discos fallidos.

Fuente: Tema2-DISM-2.pdf, páginas PDF 8, 14–15.

Distractores:

- A) Una sola paridad de RAID 5 no permite resolver dos bloques perdidos de una franja.
- B) Invierte la tolerancia que proporciona la doble paridad.
- D) La paridad también proporciona tolerancia a fallos; no se limita a los espejos.

## 6. D) UTF-32

UTF-32 representa cada punto de código Unicode en una unidad de 32 bits. Un carácter visual puede componerse de varios puntos de código; no hay que confundir ambas magnitudes.

Fuente: Tema2-DISM-2.pdf, páginas PDF 23.

Distractores:

- A) UTF-16 utiliza una o dos unidades de 16 bits, no cuatro bytes para todos los puntos de código.
- B) ASCII tiene un repertorio limitado y no es una codificación de todo Unicode en cuatro bytes.
- C) UTF-8 utiliza de uno a cuatro bytes, según el punto de código.

## 7. A) Sin pérdida (lossless)

La propiedad definitoria de lossless es reconstruir exactamente la información original. La fidelidad perceptiva de un algoritmo lossy es una cuestión distinta.

Fuente: Tema2-DISM-2.pdf, páginas PDF 32.

Distractores:

- B) Ampliar la resolución no recupera la información descartada.
- C) Lossy descarta información y no garantiza la reconstrucción exacta.
- D) Que la diferencia no se aprecie no implica igualdad exacta de datos.

## 8. B) Una copia de seguridad anterior al borrado

La redundancia RAID mejora disponibilidad ante fallos de discos, pero no sustituye copias con versiones anteriores. Un borrado válido puede propagarse a la información redundante.

Fuente: Tema2-DISM-2.pdf, páginas PDF 19.

Distractores:

- A) La paridad protege frente a determinados fallos físicos, no conserva por sí misma el archivo anterior.
- C) Otra copia sincronizada del volumen reproduce también el borrado.
- D) RAID 0 no mantiene versiones ni aporta recuperación de borrados.

## 9. C) 8 TB

RAID 5 utiliza el equivalente de un disco para paridad distribuida. La capacidad es (5 − 1) × 2 TB = 8 TB.

Fuente: Tema2-DISM-2.pdf, páginas PDF 7–9.

Distractores:

- A) Calcula como si todos los discos fueran copias de un único espejo.
- B) Resta dos discos equivalentes, como en RAID 6.
- D) Cuenta todos los discos como datos y omite la capacidad equivalente destinada a paridad.

## 10. A) 0010

1011 ⊕ 0101 = 1110; después 1110 ⊕ 1100 = 0010. XOR produce 1 cuando los bits comparados son diferentes.

Fuente: Tema2-DISM-2.pdf, páginas PDF 9, 13.

Distractores:

- B) Repite D2 sin combinar los otros bloques de datos.
- C) Es el XOR de D0 y D1, pero falta combinar D2.
- D) Se obtiene al usar OR en lugar de XOR con esos bloques.

## 11. D) CPU para lógica, NPU para IA y motor de vídeo para codificar

Un SoC puede combinar bloques y asignar tareas a los más adecuados: CPU general, NPU para redes neuronales y motor multimedia para códecs. Esto reduce trabajo y consumo en los bloques generales.

Fuente: Tema2-DISM-2.pdf, páginas PDF 47, 59–63.

Distractores:

- A) El motor de vídeo no es el bloque general de reglas de negocio.
- B) Una FPGA no es un requisito para ejecutar la app en un SoC.
- C) Invierte las especializaciones y obliga a la NPU a tareas generales.

## 12. C) Localidad temporal

Hay localidad temporal cuando una posición referenciada tiene probabilidad de usarse de nuevo pronto. La caché puede aprovechar esa reutilización.

Fuente: Tema2-DISM-2.pdf, páginas PDF 45.

Distractores:

- A) La reutilización cercana en el tiempo es precisamente una forma de localidad.
- B) La repetición del mismo dato no es un recorrido sin reutilización.
- D) La espacial se refiere a posiciones próximas, no a repetir la misma.

## 13. D) Multiplicación y acumulación (MAC)

La operación MAC multiplica operandos y acumula el resultado. Es muy frecuente en filtros digitales y otros algoritmos numéricos de señal.

Fuente: Tema2-DISM-2.pdf, páginas PDF 52–53, 57.

Distractores:

- A) No es la operación aritmética característica que destaca el tema.
- B) La conversión de caracteres no define la unidad MAC de un DSP.
- C) MAC aquí significa multiply-accumulate, no compresión y cifrado.

## 14. A) La monolítica integra el sistema en un chip; la modular combina varios chips

La distinción monolítica/modular describe la integración física. Es un eje diferente de programable, dedicado o reconfigurable.

Fuente: Tema2-DISM-2.pdf, páginas PDF 47, 61–62.

Distractores:

- B) Monolítico/modular se refiere aquí a la implementación física, no al número de programas o usuarios.
- C) El número de chips no impone esa ausencia de memoria.
- D) La distinción de uno o varios chips puede aplicarse a diferentes familias.

## 15. D) RISC prioriza instrucciones simples; CISC dispone de un repertorio más complejo

Dentro de las programables de propósito general, RISC se asocia con instrucciones frecuentes y simples y CISC con un juego más rico y complejo. No son familias RAID ni sinónimos de FPGA.

Fuente: Tema2-DISM-2.pdf, páginas PDF 47, 49–50.

Distractores:

- A) No corresponde a la caracterización del tema, que destaca la longitud variable en CISC.
- B) Invierte la distinción conceptual presentada en el tema.
- C) Ambas familias pueden ejecutar programas compilados desde lenguajes de alto nivel.

## 16. B) 0,75 MiB

512 × 512 × 24 / 8 = 786 432 bytes. Al dividir entre 1 048 576 bytes/MiB se obtiene 0,75 MiB.

Fuente: Tema2-DISM-2.pdf, páginas PDF 30.

Distractores:

- A) Equivale a contar un byte por píxel en lugar de tres.
- C) Aplica de nuevo el factor de tres después de haberlo incluido.
- D) Es el número de mebibits; falta dividir entre ocho para pasarlo a bytes.

## 17. D) Una FPGA reconfigurable

La FPGA ofrece bloques lógicos e interconexiones programables. El ASIC dedica su circuito a una tarea y prioriza eficiencia frente a flexibilidad.

Fuente: Tema2-DISM-2.pdf, páginas PDF 61–63.

Distractores:

- A) Añadir chips fijos no proporciona la reconfiguración lógica solicitada.
- B) El ASIC dedicado no cambia su circuito tras fabricarse.
- C) Cambiar la frecuencia no modifica el circuito fijo del ASIC.

## 18. C) Usa entre uno y cuatro bytes y mantiene la codificación de ASCII

UTF-8 utiliza un byte para ASCII y secuencias más largas para otros caracteres Unicode, hasta cuatro bytes. «UTFS» en las indicaciones se interpreta aquí como UTF-8, presente en la página 23.

Fuente: Tema2-DISM-2.pdf, páginas PDF 23, 25.

Distractores:

- A) UTF-8 representa Unicode, no únicamente ASCII.
- B) El tamaño fijo de cuatro bytes corresponde a UTF-32.
- D) UTF-8 es variable; incluso UTF-16 necesita pares para caracteres complementarios.

## 19. C) Calcular la paridad nueva sin leer los datos antiguos de esa franja

Al disponer de todos los datos nuevos, la controladora calcula su XOR directamente. En el ejemplo se escriben tres bloques de datos y uno de paridad.

Fuente: Tema2-DISM-2.pdf, páginas PDF 10.

Distractores:

- A) Un full-stripe write no transforma RAID 5 en un espejo.
- B) Eso aplica el coste de pequeñas escrituras parciales al caso de franja completa.
- D) Aunque no se lean los datos viejos, hay que guardar la paridad nueva.

## 20. C) 0110

0010 ⊕ 1100 = 1110; 1110 ⊕ 1000 = 0110. Hay que quitar la contribución antigua y añadir la nueva mediante XOR.

Fuente: Tema2-DISM-2.pdf, páginas PDF 10–13.

Distractores:

- A) Mantiene la paridad anterior pese a haber cambiado el dato.
- B) Es el XOR entre dato viejo y nuevo, pero falta combinar la paridad anterior.
- D) Combina P con el nuevo dato y omite retirar el efecto del dato viejo.

## 21. D) La mayor sensibilidad a variaciones de luminancia que de crominancia

La visión no responde por igual al brillo y al color ni a todas las variaciones espaciales. Esa diferencia permite reducir información perceptivamente menos relevante.

Fuente: Tema2-DISM-2.pdf, páginas PDF 35.

Distractores:

- A) La compresión perceptiva aprovecha precisamente sensibilidades diferentes.
- B) Invierte la relación perceptiva que presenta el tema.
- C) El tema indica que pequeñas variaciones de brillo se perciben con facilidad en zonas homogéneas.

## 22. A) Debe alimentar continuamente el procesamiento con muchos datos nuevos

Las MMA pueden reutilizar el código de sus bucles y, al mismo tiempo, consumir datos nuevos a gran ritmo. Eso exige memoria y E/S capaces de sostener el flujo.

Fuente: Tema2-DISM-2.pdf, páginas PDF 44–46.

Distractores:

- B) La poca reutilización temporal reduce la ayuda de guardar copias para accesos repetidos.
- C) El cómputo necesita recibir los datos de entrada del flujo.
- D) Aunque cada operando sea pequeño, se procesan muchos y con frecuencia.

## 23. B) 2 TB

Cada disco contiene la misma información. Un espejo de dos unidades iguales ofrece la capacidad de una: 2 TB.

Fuente: Tema2-DISM-2.pdf, páginas PDF 6.

Distractores:

- A) Divide otra vez la capacidad de un disco, aunque cada disco ya contiene la copia completa.
- C) Descuenta media unidad sin una regla de capacidad propia de un espejo.
- D) Suma la capacidad física sin descontar que el segundo disco duplica los datos.

## 24. A) En las programables específicas, optimizadas para procesamiento de señal

En la clasificación, ser específico indica optimización para una clase de tareas. Un DSP puede seguir siendo programable; no debe confundirse esa especialización con la rama de ASIC dedicados.

Fuente: Tema2-DISM-2.pdf, páginas PDF 47, 51–53, 63.

Distractores:

- B) Cambiar el programa de un DSP no equivale a reconfigurar bloques e interconexiones de una FPGA.
- C) El DSP del caso está optimizado para algoritmos de señal y se sitúa entre las programables específicas.
- D) Un DSP programable permite cambiar instrucciones; especialización no significa circuito ASIC fijo.

## 25. A) PNG sin pérdida y JPEG convencional con pérdida

El tema presenta PNG como lossless y JPEG convencional como lossy. JPEG 2000 y WebP permiten otros modos; por eso el enunciado acota el JPEG convencional.

Fuente: Tema2-DISM-2.pdf, páginas PDF 34–36.

Distractores:

- B) Invierte los modos habituales descritos para ambos formatos.
- C) JPEG convencional es lossy y WebP admite modos lossy y lossless.
- D) La compresión GIF mediante LZW y la de PNG son sin pérdida; limitar la paleta es otra operación.

## 26. D) Programable: cambia instrucciones; dedicada ASIC: circuito fijo; FPGA: lógica reconfigurable

El árbol de la página 47 distingue programables, dedicadas y reconfigurables. El programa adapta la secuencia de instrucciones; el ASIC dedica su circuito a una tarea; la FPGA permite reconfigurar su lógica.

Fuente: Tema2-DISM-2.pdf, páginas PDF 47, 61–63.

Distractores:

- A) Confunde el software programable, el circuito dedicado y el hardware reconfigurable.
- B) Atribuye la reconfiguración al ASIC e impide a la FPGA adaptar la lógica.
- C) Intercambia las propiedades de ASIC y FPGA.

## 27. C) Alta localidad espacial y baja localidad temporal de los datos

El acceso a píxeles vecinos aporta localidad espacial. Recorrer el flujo sin regresar a los datos reduce la localidad temporal, aunque el código del bucle sí pueda reutilizarse.

Fuente: Tema2-DISM-2.pdf, páginas PDF 45–46.

Distractores:

- A) El enunciado especifica que los datos no se vuelven a usar.
- B) Invierte el patrón: se visitan vecinos y apenas se reutilizan los datos.
- D) Acceder a posiciones contiguas favorece la localidad espacial.

## 28. A) 100 bytes

Cada punto de código ASCII ocupa un byte en UTF-8: 100×1 = 100 bytes. En las condiciones del enunciado serían 200 en UTF-16 y 400 en UTF-32.

Fuente: Tema2-DISM-2.pdf, páginas PDF 23, 25.

Distractores:

- B) Cuenta dos bytes por punto de código como en UTF-16 para este repertorio.
- C) Aplica el tamaño fijo de UTF-32 en lugar de UTF-8.
- D) Confunde bits y bytes o multiplica por ocho una cantidad que ya está en bytes.

## 29. A) El conjunto pierde la disponibilidad íntegra de sus datos

RAID 0 reparte datos entre discos para aumentar capacidad y rendimiento, pero no aporta redundancia. El fallo de uno compromete los datos del conjunto.

Fuente: Tema2-DISM-2.pdf, páginas PDF 5.

Distractores:

- B) RAID 0 no mantiene paridad.
- C) RAID 0 no crea espejos; eso caracteriza a RAID 1.
- D) Esa tolerancia corresponde a RAID 6, no a RAID 0.

## 30. D) Reducir el tamaño frente a introducir pérdida de detalle y artefactos

La compresión con pérdida descarta información. Una reducción de tamaño mayor puede hacer visibles errores de reconstrucción; ampliar después el archivo no recupera los datos originales.

Fuente: Tema2-DISM-2.pdf, páginas PDF 32, 34–35.

Distractores:

- A) JPEG convencional es con pérdida; esa igualdad exacta no está garantizada.
- B) Descartar información no crea detalle original nuevo.
- C) La información codificada necesita decodificarse para reconstruir la imagen.

## 31. B) Va rotando entre los discos del conjunto

La paridad es distribuida: su disco cambia de una franja a otra. Dentro de una franja, un bloque de paridad permite reconstruir un bloque de datos ausente.

Fuente: Tema2-DISM-2.pdf, páginas PDF 7–9.

Distractores:

- A) Eso describe un espejo, no paridad distribuida.
- C) La paridad fija caracteriza a otros esquemas, como RAID 4, no a RAID 5.
- D) RAID 5 almacena paridad para poder reconstruir un fallo.
