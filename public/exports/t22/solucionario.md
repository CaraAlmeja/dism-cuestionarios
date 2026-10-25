# Solucionario: DISM · T2.2 · Almacenamiento y arquitecturas

## 1. D) El conjunto pierde la disponibilidad íntegra de sus datos

RAID 0 reparte datos entre discos para aumentar capacidad y rendimiento, pero no aporta redundancia. El fallo de uno compromete los datos del conjunto.

Fuente: Tema2-DISM-2.pdf, páginas PDF 5.

Distractores:

- A) RAID 0 no crea espejos; eso caracteriza a RAID 1.
- B) Esa tolerancia corresponde a RAID 6, no a RAID 0.
- C) RAID 0 no mantiene paridad.

## 2. B) 2 TB

Cada disco contiene la misma información. Un espejo de dos unidades iguales ofrece la capacidad de una: 2 TB.

Fuente: Tema2-DISM-2.pdf, páginas PDF 6.

Distractores:

- A) Divide otra vez la capacidad de un disco, aunque cada disco ya contiene la copia completa.
- C) Descuenta media unidad sin una regla de capacidad propia de un espejo.
- D) Suma la capacidad física sin descontar que el segundo disco duplica los datos.

## 3. C) 8 TB

RAID 5 utiliza el equivalente de un disco para paridad distribuida. La capacidad es (5 − 1) × 2 TB = 8 TB.

Fuente: Tema2-DISM-2.pdf, páginas PDF 7–9.

Distractores:

- A) Calcula como si todos los discos fueran copias de un único espejo.
- B) Resta dos discos equivalentes, como en RAID 6.
- D) Cuenta todos los discos como datos y omite la capacidad equivalente destinada a paridad.

## 4. D) Va rotando entre los discos del conjunto

La paridad es distribuida: su disco cambia de una franja a otra. Dentro de una franja, un bloque de paridad permite reconstruir un bloque de datos ausente.

Fuente: Tema2-DISM-2.pdf, páginas PDF 7–9.

Distractores:

- A) La paridad fija caracteriza a otros esquemas, como RAID 4, no a RAID 5.
- B) Eso describe un espejo, no paridad distribuida.
- C) RAID 5 almacena paridad para poder reconstruir un fallo.

## 5. A) 0010

1011 ⊕ 0101 = 1110; después 1110 ⊕ 1100 = 0010. XOR produce 1 cuando los bits comparados son diferentes.

Fuente: Tema2-DISM-2.pdf, páginas PDF 9, 13.

Distractores:

- B) Repite D2 sin combinar los otros bloques de datos.
- C) Es el XOR de D0 y D1, pero falta combinar D2.
- D) Se obtiene al usar OR en lugar de XOR con esos bloques.

## 6. B) 0101

0010 ⊕ 1011 = 1001 y 1001 ⊕ 1100 = 0101. El XOR permite despejar el único bloque ausente.

Fuente: Tema2-DISM-2.pdf, páginas PDF 9, 13.

Distractores:

- A) Sería cancelar cada bloque con una copia idéntica, que no es la operación pedida.
- C) Combina D0 y D2 pero omite la paridad P.
- D) Es el resultado parcial P ⊕ D0; falta aplicar XOR con D2.

## 7. C) 0110

0010 ⊕ 1100 = 1110; 1110 ⊕ 1000 = 0110. Hay que quitar la contribución antigua y añadir la nueva mediante XOR.

Fuente: Tema2-DISM-2.pdf, páginas PDF 10–13.

Distractores:

- A) Mantiene la paridad anterior pese a haber cambiado el dato.
- B) Es el XOR entre dato viejo y nuevo, pero falta combinar la paridad anterior.
- D) Combina P con el nuevo dato y omite retirar el efecto del dato viejo.

## 8. D) Dos lecturas y dos escrituras

Se leen el dato antiguo y la paridad antigua, se calcula la nueva paridad y se escriben dato y paridad nuevos: cuatro accesos lógicos.

Fuente: Tema2-DISM-2.pdf, páginas PDF 10–11.

Distractores:

- A) En el caso indicado se actualizan tanto el dato como la paridad.
- B) Sin caché se necesitan el dato viejo y la paridad vieja.
- C) Falta leer y escribir la paridad, además del dato.

## 9. C) Calcular la paridad nueva sin leer los datos antiguos de esa franja

Al disponer de todos los datos nuevos, la controladora calcula su XOR directamente. En el ejemplo se escriben tres bloques de datos y uno de paridad.

Fuente: Tema2-DISM-2.pdf, páginas PDF 10.

Distractores:

- A) Eso aplica el coste de pequeñas escrituras parciales al caso de franja completa.
- B) Aunque no se lean los datos viejos, hay que guardar la paridad nueva.
- D) Un full-stripe write no transforma RAID 5 en un espejo.

## 10. A) RAID 6 soporta dos discos fallidos y RAID 5 uno

RAID 5 utiliza una redundancia de paridad; RAID 6 añade una segunda. Por eso RAID 6 permite reconstruir ante dos discos fallidos.

Fuente: Tema2-DISM-2.pdf, páginas PDF 8, 14–15.

Distractores:

- B) La paridad también proporciona tolerancia a fallos; no se limita a los espejos.
- C) Invierte la tolerancia que proporciona la doble paridad.
- D) Una sola paridad de RAID 5 no permite resolver dos bloques perdidos de una franja.

## 11. D) Una copia de seguridad anterior al borrado

La redundancia RAID mejora disponibilidad ante fallos de discos, pero no sustituye copias con versiones anteriores. Un borrado válido puede propagarse a la información redundante.

Fuente: Tema2-DISM-2.pdf, páginas PDF 19.

Distractores:

- A) La paridad protege frente a determinados fallos físicos, no conserva por sí misma el archivo anterior.
- B) RAID 0 no mantiene versiones ni aporta recuperación de borrados.
- C) Otra copia sincronizada del volumen reproduce también el borrado.

## 12. B) Usa entre uno y cuatro bytes y mantiene la codificación de ASCII

UTF-8 utiliza un byte para ASCII y secuencias más largas para otros caracteres Unicode, hasta cuatro bytes. «UTFS» en las indicaciones se interpreta aquí como UTF-8, presente en la página 23.

Fuente: Tema2-DISM-2.pdf, páginas PDF 23, 25.

Distractores:

- A) UTF-8 es variable; incluso UTF-16 necesita pares para caracteres complementarios.
- C) El tamaño fijo de cuatro bytes corresponde a UTF-32.
- D) UTF-8 representa Unicode, no únicamente ASCII.

## 13. B) 0,75 MiB

512 × 512 × 24 / 8 = 786 432 bytes. Al dividir entre 1 048 576 bytes/MiB se obtiene 0,75 MiB.

Fuente: Tema2-DISM-2.pdf, páginas PDF 30.

Distractores:

- A) Equivale a contar un byte por píxel en lugar de tres.
- C) Aplica de nuevo el factor de tres después de haberlo incluido.
- D) Es el número de mebibits; falta dividir entre ocho para pasarlo a bytes.

## 14. D) Sin pérdida (lossless)

La propiedad definitoria de lossless es reconstruir exactamente la información original. La fidelidad perceptiva de un algoritmo lossy es una cuestión distinta.

Fuente: Tema2-DISM-2.pdf, páginas PDF 32.

Distractores:

- A) Ampliar la resolución no recupera la información descartada.
- B) Que la diferencia no se aprecie no implica igualdad exacta de datos.
- C) Lossy descarta información y no garantiza la reconstrucción exacta.

## 15. B) PNG sin pérdida y JPEG convencional con pérdida

El tema presenta PNG como lossless y JPEG convencional como lossy. JPEG 2000 y WebP permiten otros modos; por eso el enunciado acota el JPEG convencional.

Fuente: Tema2-DISM-2.pdf, páginas PDF 34–36.

Distractores:

- A) La compresión GIF mediante LZW y la de PNG son sin pérdida; limitar la paleta es otra operación.
- C) Invierte los modos habituales descritos para ambos formatos.
- D) JPEG convencional es lossy y WebP admite modos lossy y lossless.

## 16. A) Localidad temporal

Hay localidad temporal cuando una posición referenciada tiene probabilidad de usarse de nuevo pronto. La caché puede aprovechar esa reutilización.

Fuente: Tema2-DISM-2.pdf, páginas PDF 45.

Distractores:

- B) La espacial se refiere a posiciones próximas, no a repetir la misma.
- C) La repetición del mismo dato no es un recorrido sin reutilización.
- D) La reutilización cercana en el tiempo es precisamente una forma de localidad.

## 17. C) Alta localidad espacial y baja localidad temporal de los datos

El acceso a píxeles vecinos aporta localidad espacial. Recorrer el flujo sin regresar a los datos reduce la localidad temporal, aunque el código del bucle sí pueda reutilizarse.

Fuente: Tema2-DISM-2.pdf, páginas PDF 45–46.

Distractores:

- A) El enunciado especifica que los datos no se vuelven a usar.
- B) Acceder a posiciones contiguas favorece la localidad espacial.
- D) Invierte el patrón: se visitan vecinos y apenas se reutilizan los datos.

## 18. A) Una FPGA reconfigurable

La FPGA ofrece bloques lógicos e interconexiones programables. El ASIC dedica su circuito a una tarea y prioriza eficiencia frente a flexibilidad.

Fuente: Tema2-DISM-2.pdf, páginas PDF 61–63.

Distractores:

- B) El ASIC dedicado no cambia su circuito tras fabricarse.
- C) Añadir chips fijos no proporciona la reconfiguración lógica solicitada.
- D) Cambiar la frecuencia no modifica el circuito fijo del ASIC.

## 19. A) Multiplicación y acumulación (MAC)

La operación MAC multiplica operandos y acumula el resultado. Es muy frecuente en filtros digitales y otros algoritmos numéricos de señal.

Fuente: Tema2-DISM-2.pdf, páginas PDF 52–53, 57.

Distractores:

- B) No es la operación aritmética característica que destaca el tema.
- C) MAC aquí significa multiply-accumulate, no compresión y cifrado.
- D) La conversión de caracteres no define la unidad MAC de un DSP.

## 20. C) CPU para lógica, NPU para IA y motor de vídeo para codificar

Un SoC puede combinar bloques y asignar tareas a los más adecuados: CPU general, NPU para redes neuronales y motor multimedia para códecs. Esto reduce trabajo y consumo en los bloques generales.

Fuente: Tema2-DISM-2.pdf, páginas PDF 47, 59–63.

Distractores:

- A) El motor de vídeo no es el bloque general de reglas de negocio.
- B) Una FPGA no es un requisito para ejecutar la app en un SoC.
- D) Invierte las especializaciones y obliga a la NPU a tareas generales.
