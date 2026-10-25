# Solucionario: DISM · T2.1 · Streaming multimedia

## 1. B) Multimedia lineal

La multimedia lineal mantiene un orden predeterminado sin que el usuario controle los contenidos o su secuencia. La hipermedia incorpora navegación.

Fuente: Tema2-DISM-1.pdf, páginas PDF 4–5.

Distractores:

- A) Los saltos libres contradicen la secuencia que el usuario no puede modificar.
- C) La navegación permitiría elegir el recorrido, que aquí está fijado.
- D) Ese control está expresamente ausente en el caso.

## 2. D) Mantener las relaciones temporales entre medios

El sistema debe conservar las relaciones temporales entre flujos. Las marcas de tiempo ayudan a presentar audio y vídeo en el momento que corresponde.

Fuente: Tema2-DISM-1.pdf, páginas PDF 14.

Distractores:

- A) La codificación de caracteres no corrige el desfase audiovisual.
- B) Tener más espacio no mantiene por sí solo las relaciones de tiempo.
- C) La profundidad de color no determina la sincronización de audio y vídeo.

## 3. A) Se reproduce el contenido mientras siguen llegando sus datos

En streaming la recepción y el consumo se solapan. No hay que esperar al archivo completo, aunque suele existir una espera inicial de almacenamiento en búfer.

Fuente: Tema2-DISM-1.pdf, páginas PDF 16–18.

Distractores:

- B) El streaming también puede ser bajo demanda.
- C) El cliente utiliza un búfer para sostener la reproducción.
- D) Esa espera caracteriza la descarga completa previa.

## 4. B) Vídeo bajo demanda (VOD)

VOD permite solicitar contenidos en el momento elegido y controlar la reproducción. La forma de distribución y el modelo de pago son dimensiones diferentes.

Fuente: Tema2-DISM-1.pdf, páginas PDF 21–27.

Distractores:

- A) En ese modelo el usuario sigue la señal que se emite, no elige libremente el punto.
- C) Broadcast describe distribución y no garantiza la elección individual indicada.
- D) Un flujo simultáneo compartido no describe los puntos de reproducción individuales.

## 5. D) Multicast

Multicast dirige el flujo a un grupo de receptores. Unicast sirve individualmente y broadcast difunde a los receptores del ámbito de difusión.

Fuente: Tema2-DISM-1.pdf, páginas PDF 25.

Distractores:

- A) No es una modalidad de transmisión a un grupo por la red.
- B) Unicast establece un flujo por destinatario.
- C) Broadcast difunde sin seleccionar ese grupo específico.

## 6. B) Contenido por Internet sin exigir un servicio tradicional de TV de pago

OTT describe la vía de entrega a través de Internet. No equivale a un modelo concreto de ingresos ni a un único dispositivo de reproducción.

Fuente: Tema2-DISM-1.pdf, páginas PDF 27–28.

Distractores:

- A) OTT puede ofrecer contenido bajo demanda además de directos.
- C) OTT utiliza Internet y puede recibirse en distintos tipos de dispositivo.
- D) OTT no determina la financiación: puede haber AVOD, SVOD o TVOD.

## 7. A) AVOD

AVOD significa Advertising Video on Demand: el ingreso principal del modelo descrito procede de la publicidad.

Fuente: Tema2-DISM-1.pdf, páginas PDF 29.

Distractores:

- B) PPV implica pagar por una visualización o evento, no acceso gratuito financiado con anuncios.
- C) TVOD se basa en pagar por contenido o evento seleccionado.
- D) SVOD se basa en una suscripción de acceso al servicio.

## 8. A) SVOD

SVOD es Subscription Video on Demand. El criterio aquí es la suscripción periódica, aunque en el mercado existan modelos combinados.

Fuente: Tema2-DISM-1.pdf, páginas PDF 30.

Distractores:

- B) En TVOD se paga una transacción por un contenido concreto.
- C) En el modelo AVOD descrito el acceso se financia con anuncios, no con la cuota.
- D) El pago por evento no describe acceso recurrente a un catálogo.

## 9. D) TVOD

TVOD es el modelo transaccional: se paga por la pieza o evento elegido. El alquiler digital es un ejemplo.

Fuente: Tema2-DISM-1.pdf, páginas PDF 31.

Distractores:

- A) El contenido aquí se paga directamente y no se ofrece gratis por anuncios.
- B) La suscripción da acceso periódico al catálogo, no describe este alquiler individual.
- C) No hay cuota de catálogo ni anuncios en las condiciones del caso.

## 10. A) RTP

RTP lleva el contenido en tiempo real y aporta secuencias y tiempos para su reproducción. No garantiza por sí mismo recuperar todas las pérdidas.

Fuente: Tema2-DISM-1.pdf, páginas PDF 42–43.

Distractores:

- B) RTCP informa sobre recepción y calidad, pero no transporta el flujo audiovisual principal.
- C) RTSP controla la sesión y sus órdenes de reproducción.
- D) HTTP puede distribuir segmentos, pero no es el protocolo identificado por esa función de RTP.

## 11. C) RTCP

RTCP comunica estadísticas de recepción y calidad para ayudar a controlar la transmisión. Complementa a RTP.

Fuente: Tema2-DISM-1.pdf, páginas PDF 43–44.

Distractores:

- A) HLS distribuye segmentos HTTP y no es el protocolo de supervisión complementario a RTP.
- B) RTMP se asocia en el tema al envío del directo al servidor.
- D) RTSP sirve para gestionar la sesión, no es el protocolo de informes de recepción de RTP.

## 12. D) RTSP

RTSP gestiona la sesión como un mando de reproducción. El audio y el vídeo pueden viajar por RTP en otro canal.

Fuente: Tema2-DISM-1.pdf, páginas PDF 46–47.

Distractores:

- A) RTCP supervisa calidad y recepción; no ejecuta esas órdenes de sesión.
- B) RTP transporta datos multimedia; no es el protocolo de esas órdenes.
- C) DASH describe streaming adaptativo HTTP, no ese control de sesión.

## 13. A) RTMP

RTMP se usa para transportar la señal desde el codificador al servidor. El formato de entrega al espectador puede ser otro, como HLS o DASH.

Fuente: Tema2-DISM-1.pdf, páginas PDF 45.

Distractores:

- B) M3U8 es un formato de lista de reproducción usado por HLS, no ese protocolo de ingestión.
- C) RTCP informa de la calidad de un flujo RTP, no es la ingestión descrita.
- D) RTSP controla sesiones y tampoco se define por informar de pérdidas.

## 14. C) HLS con M3U8 y MPEG-DASH con MPD

HLS emplea listas M3U8 y DASH usa Media Presentation Description (MPD). Ambos pueden describir segmentos y calidades disponibles.

Fuente: Tema2-DISM-1.pdf, páginas PDF 48–49.

Distractores:

- A) Los manifiestos corresponden a streaming HTTP, no a esos protocolos RTP/RTCP.
- B) Intercambia los manifiestos de ambas tecnologías.
- D) Asigna a RTSP y RTMP los manifiestos de DASH y HLS.

## 15. C) Solicitar segmentos de una representación de menor bitrate

El cliente puede elegir una representación con menor tasa para ajustarse a la red y sostener la reproducción. La decisión combina estimaciones de capacidad y estado del búfer.

Fuente: Tema2-DISM-1.pdf, páginas PDF 39, 48–49.

Distractores:

- A) El manifiesto describe recursos; no contiene por sí mismo el vídeo a reproducir.
- B) La financiación no ajusta la tasa de los segmentos.
- D) Ignora la adaptación y aumenta el riesgo de cortes.

## 16. B) Jitter

Jitter es la variación del retardo o de los instantes de llegada. Un búfer de reproducción puede absorber parte de esa irregularidad.

Fuente: Tema2-DISM-1.pdf, páginas PDF 53.

Distractores:

- A) La profundidad de color describe la representación de píxeles, no la llegada de paquetes.
- C) El bitrate mide cantidad de datos por unidad de tiempo, no la variación de retardo.
- D) Una latencia fija desplaza todos los paquetes por igual, sin variar los intervalos.

## 17. C) Más tolerancia a retrasos y mayor espera inicial

El búfer cambia latencia por estabilidad: reserva más datos para amortiguar retrasos, a costa de mayor retardo de arranque. Una reserva finita no resuelve una conexión insuficiente de manera indefinida.

Fuente: Tema2-DISM-1.pdf, páginas PDF 52–53.

Distractores:

- A) El búfer no garantiza recuperar paquetes perdidos ni una espera invariable.
- B) El búfer no aumenta la capacidad física de la red.
- D) Crear una reserva mayor requiere esperar más datos, no menos.

## 18. B) La reproducción se detiene hasta recuperar una reserva suficiente

Cuando el búfer queda vacío aparece un corte o rebuffering. Para continuar, el cliente necesita recibir más datos y puede reducir la calidad si el servicio permite adaptación.

Fuente: Tema2-DISM-1.pdf, páginas PDF 52.

Distractores:

- A) No se puede seguir mostrando contenido nuevo sin recibir sus datos.
- C) El almacenamiento temporal no crea el contenido que falta.
- D) RTCP supervisa; no sustituye el contenido que falta.

## 19. C) Los espectadores también pueden reenviar fragmentos a otros peers

Los peers descargan y comparten chunks. El tracker coordina y el seed aporta contenido inicial. Esto reduce carga del origen, aunque añade dependencia de los peers.

Fuente: Tema2-DISM-1.pdf, páginas PDF 54–55.

Distractores:

- A) En el esquema descrito se intercambian fragmentos durante la reproducción.
- B) El seed posee contenido y puede iniciar su distribución.
- D) El tracker coordina peers; no tiene que servir todo el vídeo.

## 20. D) Un servidor que almacena y entrega contenido audiovisual al cliente

Los Open Connect Appliances son servidores de caché y entrega situados cerca de los usuarios, por ejemplo dentro de ISP o en puntos de intercambio. El cliente recibe de ellos los bytes del vídeo.

Fuente: Tema2-DISM-1.pdf, páginas PDF 57–59, 64. Contraste: https://openconnect.netflix.com/en/

Distractores:

- A) El OCA es infraestructura de entrega, no el cliente de reproducción.
- B) La facturación pertenece a la lógica del backend, no a la misión del OCA.
- C) OCA significa Open Connect Appliance; no es un algoritmo de compresión.
