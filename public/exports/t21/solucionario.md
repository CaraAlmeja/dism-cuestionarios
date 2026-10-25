# Solucionario: DISM · T2.1 · Streaming multimedia

## 1. A) La reproducción se detiene hasta recuperar una reserva suficiente

Cuando el búfer queda vacío aparece un corte o rebuffering. Para continuar, el cliente necesita recibir más datos y puede reducir la calidad si el servicio permite adaptación.

Fuente: Tema2-DISM-1.pdf, páginas PDF 52.

Distractores:

- B) El almacenamiento temporal no crea el contenido que falta.
- C) RTCP supervisa; no sustituye el contenido que falta.
- D) No se puede seguir mostrando contenido nuevo sin recibir sus datos.

## 2. A) Más tolerancia a retrasos y mayor espera inicial

El búfer cambia latencia por estabilidad: reserva más datos para amortiguar retrasos, a costa de mayor retardo de arranque. Una reserva finita no resuelve una conexión insuficiente de manera indefinida.

Fuente: Tema2-DISM-1.pdf, páginas PDF 52–53.

Distractores:

- B) Crear una reserva mayor requiere esperar más datos, no menos.
- C) El búfer no aumenta la capacidad física de la red.
- D) El búfer no garantiza recuperar paquetes perdidos ni una espera invariable.

## 3. A) Vídeo bajo demanda (VOD)

VOD permite solicitar contenidos en el momento elegido y controlar la reproducción. La forma de distribución y el modelo de pago son dimensiones diferentes.

Fuente: Tema2-DISM-1.pdf, páginas PDF 21–27.

Distractores:

- B) Un flujo simultáneo compartido no describe los puntos de reproducción individuales.
- C) Broadcast describe distribución y no garantiza la elección individual indicada.
- D) En ese modelo el usuario sigue la señal que se emite, no elige libremente el punto.

## 4. C) RTCP

RTCP comunica estadísticas de recepción y calidad para ayudar a controlar la transmisión. Complementa a RTP.

Fuente: Tema2-DISM-1.pdf, páginas PDF 43–44.

Distractores:

- A) RTMP se asocia en el tema al envío del directo al servidor.
- B) RTSP sirve para gestionar la sesión, no es el protocolo de informes de recepción de RTP.
- D) HLS distribuye segmentos HTTP y no es el protocolo de supervisión complementario a RTP.

## 5. A) Integra varios medios, como texto, audio e imagen, bajo control informático

Una aplicación multimedia combina información de distintos medios y fuentes, de forma coordinada por el sistema informático.

Fuente: Tema2-DISM-1.pdf, páginas PDF 2–3.

Distractores:

- B) El sistema del tema representa y procesa la información digitalmente.
- C) La multimedia integra diferentes medios; no exige limitarse al vídeo.
- D) La integración controlada es parte del concepto.

## 6. D) HLS con M3U8 y MPEG-DASH con MPD

HLS emplea listas M3U8 y DASH usa Media Presentation Description (MPD). Ambos pueden describir segmentos y calidades disponibles.

Fuente: Tema2-DISM-1.pdf, páginas PDF 48–49.

Distractores:

- A) Los manifiestos corresponden a streaming HTTP, no a esos protocolos RTP/RTCP.
- B) Intercambia los manifiestos de ambas tecnologías.
- C) Asigna a RTSP y RTMP los manifiestos de DASH y HLS.

## 7. C) Navegación entre contenidos de distintos medios

La hipermedia combina medios y un sistema de navegación que permite al usuario elegir su recorrido.

Fuente: Tema2-DISM-1.pdf, páginas PDF 4–5.

Distractores:

- A) La distribución simultánea no explica los enlaces elegidos individualmente.
- B) La redundancia de almacenamiento no define la navegación hipermedia.
- D) Una secuencia obligatoria se corresponde con multimedia lineal, sin la elección descrita.

## 8. B) Comprobar si el sistema cumple los requisitos definidos

Las pruebas evalúan si el sistema funciona de acuerdo con sus requisitos en diferentes situaciones de uso.

Fuente: Tema2-DISM-1.pdf, páginas PDF 13.

Distractores:

- A) La producción genera recursos; aquí se está evaluando el sistema.
- C) Empaquetar y distribuir no verifica por sí mismo los requisitos.
- D) Los requisitos se establecen durante la planificación y sirven de criterio a las pruebas.

## 9. D) El retraso excesivo dificulta la interacción aunque llegue todo el contenido

En aplicaciones interactivas importa que la información llegue a tiempo. Una tasa suficiente o una entrega sin pérdidas no garantizan por sí mismas baja latencia.

Fuente: Tema2-DISM-1.pdf, páginas PDF 14–15.

Distractores:

- A) Miden capacidad de transferencia y tiempo, respectivamente; hay que atender a ambas.
- B) Una reserva mayor puede mejorar estabilidad, pero añade espera y no elimina la latencia.
- C) Una entrega perfecta pero muy tardía sigue perjudicando la conversación.

## 10. B) RTMP

RTMP se usa para transportar la señal desde el codificador al servidor. El formato de entrega al espectador puede ser otro, como HLS o DASH.

Fuente: Tema2-DISM-1.pdf, páginas PDF 45.

Distractores:

- A) RTSP controla sesiones y tampoco se define por informar de pérdidas.
- C) RTCP informa de la calidad de un flujo RTP, no es la ingestión descrita.
- D) M3U8 es un formato de lista de reproducción usado por HLS, no ese protocolo de ingestión.

## 11. B) Planificación y evaluación de costes

La planificación concreta necesidades, costes y especificaciones. Sirve de referencia para producir y evaluar el sistema.

Fuente: Tema2-DISM-1.pdf, páginas PDF 13.

Distractores:

- A) La distribución prepara y entrega el producto al final del proceso.
- C) Las pruebas contrastan el sistema con requisitos ya definidos.
- D) Esa etapa desarrolla los recursos y el código a partir de la planificación.

## 12. C) Los espectadores también pueden reenviar fragmentos a otros peers

Los peers descargan y comparten chunks. El tracker coordina y el seed aporta contenido inicial. Esto reduce carga del origen, aunque añade dependencia de los peers.

Fuente: Tema2-DISM-1.pdf, páginas PDF 54–55.

Distractores:

- A) El seed posee contenido y puede iniciar su distribución.
- B) El tracker coordina peers; no tiene que servir todo el vídeo.
- D) En el esquema descrito se intercambian fragmentos durante la reproducción.

## 13. B) 4 segundos

La reserva disminuye a 4 − 2 = 2 Mbit/s. Por tanto, tarda 8/2 = 4 s en vaciarse. Un búfer finito no compensa indefinidamente un caudal inferior al consumo.

Fuente: Tema2-DISM-1.pdf, páginas PDF 52–53.

Distractores:

- A) Divide la reserva por el consumo, pero omite los datos que siguen llegando.
- C) No divide por el déficit neto de 2 Mbit/s.
- D) Multiplica por el déficit en lugar de dividir la reserva entre ese déficit.

## 14. D) Acerca los archivos al usuario y reduce tráfico de tránsito externo

La entrega localizada reduce la distancia de red y la dependencia de enlaces externos. No equivale a reproducir sin conexión ni a eliminar la autorización.

Fuente: Tema2-DISM-1.pdf, páginas PDF 57–59. Contraste: https://openconnect.netflix.com/en/

Distractores:

- A) La ubicación del servidor no elimina la codificación de los vídeos.
- B) El cliente sigue necesitando conectividad para solicitar y recibir contenido.
- C) Los controles de acceso siguen gestionándose aunque la caché sea cercana.

## 15. A) RTSP

RTSP gestiona la sesión como un mando de reproducción. El audio y el vídeo pueden viajar por RTP en otro canal.

Fuente: Tema2-DISM-1.pdf, páginas PDF 46–47.

Distractores:

- B) RTP transporta datos multimedia; no es el protocolo de esas órdenes.
- C) RTCP supervisa calidad y recepción; no ejecuta esas órdenes de sesión.
- D) DASH describe streaming adaptativo HTTP, no ese control de sesión.

## 16. B) TVOD

TVOD es el modelo transaccional: se paga por la pieza o evento elegido. El alquiler digital es un ejemplo.

Fuente: Tema2-DISM-1.pdf, páginas PDF 31.

Distractores:

- A) No hay cuota de catálogo ni anuncios en las condiciones del caso.
- C) El contenido aquí se paga directamente y no se ofrece gratis por anuncios.
- D) La suscripción da acceso periódico al catálogo, no describe este alquiler individual.

## 17. C) Tiene retardo constante y no presenta jitter de llegada

La latencia es el tiempo de tránsito; el jitter es su variación. Puede existir latencia elevada con una llegada perfectamente regular.

Fuente: Tema2-DISM-1.pdf, páginas PDF 52–53.

Distractores:

- A) La latencia sigue siendo 200 ms, aunque los intervalos sean regulares.
- B) El jitter y el bitrate son magnitudes distintas.
- D) Un retardo grande pero constante no implica variación del retardo.

## 18. A) Se reproduce el contenido mientras siguen llegando sus datos

En streaming la recepción y el consumo se solapan. No hay que esperar al archivo completo, aunque suele existir una espera inicial de almacenamiento en búfer.

Fuente: Tema2-DISM-1.pdf, páginas PDF 16–18.

Distractores:

- B) El streaming también puede ser bajo demanda.
- C) El cliente utiliza un búfer para sostener la reproducción.
- D) Esa espera caracteriza la descarga completa previa.

## 19. B) Unicast: 800 Mbit/s; multicast: 8 Mbit/s

Unicast envía 100 flujos: 100×8 = 800 Mbit/s. Multicast emite un flujo de 8 Mbit/s en el origen y la red lo replica donde corresponde.

Fuente: Tema2-DISM-1.pdf, páginas PDF 25.

Distractores:

- A) Omite las cien copias individuales que debe enviar ese origen en unicast.
- C) Cuenta una copia por usuario también en el origen multicast.
- D) Invierte el flujo individual de unicast y el flujo compartido de multicast.

## 20. D) Multimedia lineal

La multimedia lineal mantiene un orden predeterminado sin que el usuario controle los contenidos o su secuencia. La hipermedia incorpora navegación.

Fuente: Tema2-DISM-1.pdf, páginas PDF 4–5.

Distractores:

- A) Los saltos libres contradicen la secuencia que el usuario no puede modificar.
- B) Ese control está expresamente ausente en el caso.
- C) La navegación permitiría elegir el recorrido, que aquí está fijado.

## 21. B) El backend gestiona identidad y catálogo; Open Connect entrega el vídeo

La arquitectura distingue el plano de control (identidad, catálogo y decisiones) de la entrega audiovisual desde Open Connect.

Fuente: Tema2-DISM-1.pdf, páginas PDF 57–59, 67.

Distractores:

- A) Intercambia la función de entrega del OCA con la lógica de servicio del backend.
- C) Reduce el backend a almacenamiento y atribuye al OCA una función de identidad que no le corresponde.
- D) El cliente reproduce y los OCA entregan; la personalización pertenece al backend.

## 22. C) Solicitar segmentos de una representación de menor bitrate

El cliente puede elegir una representación con menor tasa para ajustarse a la red y sostener la reproducción. La decisión combina estimaciones de capacidad y estado del búfer.

Fuente: Tema2-DISM-1.pdf, páginas PDF 39, 48–49.

Distractores:

- A) La financiación no ajusta la tasa de los segmentos.
- B) El manifiesto describe recursos; no contiene por sí mismo el vídeo a reproducir.
- D) Ignora la adaptación y aumenta el riesgo de cortes.

## 23. A) Contenido por Internet sin exigir un servicio tradicional de TV de pago

OTT describe la vía de entrega a través de Internet. No equivale a un modelo concreto de ingresos ni a un único dispositivo de reproducción.

Fuente: Tema2-DISM-1.pdf, páginas PDF 27–28.

Distractores:

- B) OTT puede ofrecer contenido bajo demanda además de directos.
- C) OTT no determina la financiación: puede haber AVOD, SVOD o TVOD.
- D) OTT utiliza Internet y puede recibirse en distintos tipos de dispositivo.

## 24. B) Que la solicitud esté autorizada por el plan y la licencia del contenido

El servicio comprueba que la petición sea válida para el contenido y el suscriptor antes de organizar su reproducción.

Fuente: Tema2-DISM-1.pdf, páginas PDF 62–64.

Distractores:

- A) La autorización no exige una representación idéntica para todos los clientes.
- C) No se necesita replicar todo el catálogo en cada caché para autorizar una película.
- D) La selección del OCA es un paso posterior a validar la petición en el flujo descrito.

## 25. D) RTP

RTP lleva el contenido en tiempo real y aporta secuencias y tiempos para su reproducción. No garantiza por sí mismo recuperar todas las pérdidas.

Fuente: Tema2-DISM-1.pdf, páginas PDF 42–43.

Distractores:

- A) HTTP puede distribuir segmentos, pero no es el protocolo identificado por esa función de RTP.
- B) RTSP controla la sesión y sus órdenes de reproducción.
- C) RTCP informa sobre recepción y calidad, pero no transporta el flujo audiovisual principal.

## 26. D) La eficiencia y rapidez de entrada/salida de los datos

La captura y reproducción en tiempo real necesitan E/S suficiente y regular. Más capacidad de almacenamiento no implica por sí sola más rapidez de acceso.

Fuente: Tema2-DISM-1.pdf, páginas PDF 14–15.

Distractores:

- A) Una interfaz que abre antes no garantiza el caudal de datos durante el vídeo.
- B) Más capacidad no resuelve por sí misma la velocidad o regularidad de lectura.
- C) El cuello de botella descrito es entregar datos, no procesarlos una vez recibidos.

## 27. D) AVOD

AVOD significa Advertising Video on Demand: el ingreso principal del modelo descrito procede de la publicidad.

Fuente: Tema2-DISM-1.pdf, páginas PDF 29.

Distractores:

- A) PPV implica pagar por una visualización o evento, no acceso gratuito financiado con anuncios.
- B) TVOD se basa en pagar por contenido o evento seleccionado.
- C) SVOD se basa en una suscripción de acceso al servicio.

## 28. C) Mantener las relaciones temporales entre medios

El sistema debe conservar las relaciones temporales entre flujos. Las marcas de tiempo ayudan a presentar audio y vídeo en el momento que corresponde.

Fuente: Tema2-DISM-1.pdf, páginas PDF 14.

Distractores:

- A) La codificación de caracteres no corrige el desfase audiovisual.
- B) Tener más espacio no mantiene por sí solo las relaciones de tiempo.
- D) La profundidad de color no determina la sincronización de audio y vídeo.

## 29. C) SVOD

SVOD es Subscription Video on Demand. El criterio aquí es la suscripción periódica, aunque en el mercado existan modelos combinados.

Fuente: Tema2-DISM-1.pdf, páginas PDF 30.

Distractores:

- A) El pago por evento no describe acceso recurrente a un catálogo.
- B) En el modelo AVOD descrito el acceso se financia con anuncios, no con la cuota.
- D) En TVOD se paga una transacción por un contenido concreto.

## 30. C) Un servidor que almacena y entrega contenido audiovisual al cliente

Los Open Connect Appliances son servidores de caché y entrega situados cerca de los usuarios, por ejemplo dentro de ISP o en puntos de intercambio. El cliente recibe de ellos los bytes del vídeo.

Fuente: Tema2-DISM-1.pdf, páginas PDF 57–59, 64. Contraste: https://openconnect.netflix.com/en/

Distractores:

- A) OCA significa Open Connect Appliance; no es un algoritmo de compresión.
- B) La facturación pertenece a la lógica del backend, no a la misión del OCA.
- D) El OCA es infraestructura de entrega, no el cliente de reproducción.

## 31. A) Jitter

Jitter es la variación del retardo o de los instantes de llegada. Un búfer de reproducción puede absorber parte de esa irregularidad.

Fuente: Tema2-DISM-1.pdf, páginas PDF 53.

Distractores:

- B) La profundidad de color describe la representación de píxeles, no la llegada de paquetes.
- C) Una latencia fija desplaza todos los paquetes por igual, sin variar los intervalos.
- D) El bitrate mide cantidad de datos por unidad de tiempo, no la variación de retardo.

## 32. A) Multicast

Multicast dirige el flujo a un grupo de receptores. Unicast sirve individualmente y broadcast difunde a los receptores del ámbito de difusión.

Fuente: Tema2-DISM-1.pdf, páginas PDF 25.

Distractores:

- B) No es una modalidad de transmisión a un grupo por la red.
- C) Unicast establece un flujo por destinatario.
- D) Broadcast difunde sin seleccionar ese grupo específico.

## 33. D) Representar digitalmente la información bajo control del computador

La integración requiere representaciones digitales manejables por el sistema. No significa que todos los medios usen un mismo formato o tamaño.

Fuente: Tema2-DISM-1.pdf, páginas PDF 6.

Distractores:

- A) Texto, audio e imagen tienen representaciones y necesidades diferentes; igualar tamaños no los integra.
- B) No permite el procesamiento digital integrado descrito.
- C) La ausencia de integración contradice el sistema multimedia del tema.
