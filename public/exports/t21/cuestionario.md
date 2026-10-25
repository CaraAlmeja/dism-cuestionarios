# DISM · T2.1 · Streaming multimedia

Elige una única respuesta por pregunta.

1. Una presentación reproduce sus contenidos en un orden fijo que el usuario no puede cambiar. ¿A qué categoría pertenece?

   A) Contenido bajo demanda con saltos libres
   B) Multimedia lineal
   C) Hipermedia navegable
   D) Hipermedia interactiva con control de secuencia

2. Un vídeo reproduce la imagen y el audio de forma descoordinada. ¿Qué requisito del sistema está fallando directamente?

   A) Convertir el texto a una codificación Unicode
   B) Incrementar el espacio libre del archivo final
   C) Aumentar el número de colores de la imagen
   D) Mantener las relaciones temporales entre medios

3. ¿Qué distingue al streaming frente a esperar a descargar por completo un archivo antes de reproducirlo?

   A) Se reproduce el contenido mientras siguen llegando sus datos
   B) Se reproduce únicamente contenido capturado en directo
   C) Se elimina cualquier almacenamiento temporal del cliente
   D) Se necesita tener todo el archivo antes del primer fotograma

4. Un usuario elige una película del catálogo y decide cuándo empezar y a qué punto saltar. ¿Qué tipo de servicio describe?

   A) Emisión live sin retroceso
   B) Vídeo bajo demanda (VOD)
   C) Difusión broadcast de una programación fija
   D) Multicast de un único evento en el mismo instante

5. ¿Qué modalidad de transmisión envía un flujo destinado a un grupo específico de receptores?

   A) Descarga local sin red
   B) Unicast
   C) Broadcast
   D) Multicast

6. ¿Qué describe la entrega de contenido OTT?

   A) Contenido que solo puede verse en emisión simultánea
   B) Contenido por Internet sin exigir un servicio tradicional de TV de pago
   C) Contenido limitado al decodificador de televisión por cable
   D) Contenido que se financia necesariamente con publicidad

7. Una plataforma permite ver vídeos gratis e inserta anuncios para financiarlos. ¿Qué modelo representa?

   A) AVOD
   B) PPV
   C) TVOD
   D) SVOD

8. Un servicio cobra una cuota periódica que da acceso a un catálogo. ¿Qué modelo de vídeo bajo demanda utiliza?

   A) SVOD
   B) TVOD
   C) AVOD
   D) PPV por evento

9. Un usuario paga una cantidad para alquilar una película concreta, sin contratar una cuota de catálogo. ¿Qué modelo utiliza?

   A) AVOD
   B) SVOD
   C) Modelo híbrido de cuota y publicidad
   D) TVOD

10. ¿Qué protocolo transporta audio y vídeo en tiempo real con números de secuencia y marcas temporales?

   A) RTP
   B) RTCP
   C) RTSP
   D) HTTP como protocolo de control de sesiones RTSP

11. Una aplicación necesita informes de pérdidas y variación del retardo de un flujo RTP. ¿Qué protocolo aporta esa supervisión?

   A) HLS
   B) RTMP
   C) RTCP
   D) RTSP

12. ¿Qué protocolo corresponde a órdenes de sesión como SETUP, PLAY y PAUSE?

   A) RTCP
   B) RTP
   C) MPEG-DASH
   D) RTSP

13. Un codificador envía una señal en directo a la plataforma antes de que esta la distribuya a espectadores. ¿Qué protocolo asocia el tema a esa ingestión?

   A) RTMP
   B) M3U8 como protocolo de subida
   C) RTCP
   D) RTSP como informe de pérdidas

14. ¿Qué pareja de tecnología y manifiesto está correctamente asociada?

   A) RTP con M3U8 y RTCP con MPD
   B) HLS con MPD y MPEG-DASH con M3U8
   C) HLS con M3U8 y MPEG-DASH con MPD
   D) RTSP con MPD y RTMP con M3U8

15. La conexión de un espectador pierde capacidad durante la reproducción. ¿Qué puede hacer un cliente de streaming adaptativo?

   A) Reproducir el manifiesto como si fuese un segmento de vídeo
   B) Cambiar el modelo de pago de SVOD a AVOD
   C) Solicitar segmentos de una representación de menor bitrate
   D) Mantener siempre la máxima calidad aunque se vacíe el búfer

16. Los paquetes llegan con intervalos variables aunque se enviaran regularmente. ¿Qué fenómeno describe esa variación?

   A) Profundidad de color
   B) Jitter
   C) Bitrate del códec
   D) Latencia constante

17. Si se aumenta la reserva de reproducción antes de empezar, ¿qué compromiso se espera, en igualdad de las demás condiciones?

   A) La misma espera inicial y eliminación de todas las pérdidas
   B) Menos tolerancia a retrasos y mayor capacidad de la red
   C) Más tolerancia a retrasos y mayor espera inicial
   D) Más tolerancia a retrasos y menor espera inicial

18. El cliente consume todos los datos almacenados y todavía no ha recibido los siguientes. ¿Qué sucede normalmente?

   A) La reproducción continúa indefinidamente con calidad original
   B) La reproducción se detiene hasta recuperar una reserva suficiente
   C) El reproductor inventa los segmentos que faltan en el servidor
   D) La sesión cambia obligatoriamente al protocolo RTCP

19. ¿Qué distingue al streaming P2P del esquema cliente-servidor descrito en el tema?

   A) Cada cliente necesita haber descargado todo antes de compartir
   B) El seed solo controla el pago y nunca aporta fragmentos
   C) Los espectadores también pueden reenviar fragmentos a otros peers
   D) Cada espectador recibe todo el vídeo únicamente del tracker

20. ¿Qué es un OCA en Netflix Open Connect?

   A) Un reproductor instalado en el teléfono del espectador
   B) Un servicio dedicado a facturar las suscripciones
   C) Un códec que convierte cada vídeo en paquetes RTP
   D) Un servidor que almacena y entrega contenido audiovisual al cliente
