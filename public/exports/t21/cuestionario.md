# DISM · T2.1 · Streaming multimedia

Elige una única respuesta por pregunta.

1. El cliente consume todos los datos almacenados y todavía no ha recibido los siguientes. ¿Qué sucede normalmente?

   A) La reproducción se detiene hasta recuperar una reserva suficiente
   B) El reproductor inventa los segmentos que faltan en el servidor
   C) La sesión cambia obligatoriamente al protocolo RTCP
   D) La reproducción continúa indefinidamente con calidad original

2. Si se aumenta la reserva de reproducción antes de empezar, ¿qué compromiso se espera, en igualdad de las demás condiciones?

   A) Más tolerancia a retrasos y mayor espera inicial
   B) Más tolerancia a retrasos y menor espera inicial
   C) Menos tolerancia a retrasos y mayor capacidad de la red
   D) La misma espera inicial y eliminación de todas las pérdidas

3. Un usuario elige una película del catálogo y decide cuándo empezar y a qué punto saltar. ¿Qué tipo de servicio describe?

   A) Vídeo bajo demanda (VOD)
   B) Multicast de un único evento en el mismo instante
   C) Difusión broadcast de una programación fija
   D) Emisión live sin retroceso

4. Una aplicación necesita informes de pérdidas y variación del retardo de un flujo RTP. ¿Qué protocolo aporta esa supervisión?

   A) RTMP
   B) RTSP
   C) RTCP
   D) HLS

5. ¿Qué caracteriza a una aplicación multimedia?

   A) Integra varios medios, como texto, audio e imagen, bajo control informático
   B) Sustituye los datos digitales por señales analógicas independientes
   C) Utiliza exclusivamente vídeo, aunque disponga de texto o sonido
   D) Presenta cada medio en un equipo aislado, sin integración entre ellos

6. ¿Qué pareja de tecnología y manifiesto está correctamente asociada?

   A) RTP con M3U8 y RTCP con MPD
   B) HLS con MPD y MPEG-DASH con M3U8
   C) RTSP con MPD y RTMP con M3U8
   D) HLS con M3U8 y MPEG-DASH con MPD

7. Un museo ofrece fichas de obras enlazadas con vídeos y audios. El visitante elige qué enlaces seguir. ¿Qué rasgo aporta la hipermedia?

   A) Transmisión de un único directo a todos los visitantes
   B) Duplicación del mismo vídeo en varios discos
   C) Navegación entre contenidos de distintos medios
   D) Reproducción de todo el material en una secuencia obligatoria

8. Un equipo ejecuta su aplicación en distintas situaciones y contrasta el resultado con las especificaciones. ¿Cuál es el propósito de esa etapa?

   A) Producir todos los audios y vídeos que aún faltan
   B) Comprobar si el sistema cumple los requisitos definidos
   C) Limitarse a empaquetar la aplicación para su distribución
   D) Definir por primera vez qué producto se quiere construir

9. ¿Por qué una videoconferencia necesita cuidar especialmente el retardo además del caudal de datos?

   A) Ancho de banda y latencia son dos nombres de la misma magnitud
   B) Aumentar la reserva de búfer elimina el retraso percibido
   C) La ausencia de pérdidas garantiza por sí sola una conversación fluida
   D) El retraso excesivo dificulta la interacción aunque llegue todo el contenido

10. Un codificador envía una señal en directo a la plataforma antes de que esta la distribuya a espectadores. ¿Qué protocolo asocia el tema a esa ingestión?

   A) RTSP como informe de pérdidas
   B) RTMP
   C) RTCP
   D) M3U8 como protocolo de subida

11. Antes de producir los materiales se estiman personas, equipos, costes y tiempo, y se redactan los requisitos. ¿A qué etapa corresponde?

   A) Distribución y promoción del producto
   B) Planificación y evaluación de costes
   C) Pruebas de conformidad del sistema terminado
   D) Diseño y producción de materiales

12. ¿Qué distingue al streaming P2P del esquema cliente-servidor descrito en el tema?

   A) El seed solo controla el pago y nunca aporta fragmentos
   B) Cada espectador recibe todo el vídeo únicamente del tracker
   C) Los espectadores también pueden reenviar fragmentos a otros peers
   D) Cada cliente necesita haber descargado todo antes de compartir

13. Un reproductor guarda una reserva de 8 Mbit. Consume a 4 Mbit/s y recibe de forma constante 2 Mbit/s. Sin adaptación de calidad, ¿cuánto tarda en agotar esa reserva?

   A) 2 segundos
   B) 4 segundos
   C) 8 segundos
   D) 16 segundos

14. ¿Por qué resulta útil ubicar un OCA dentro de la red de un proveedor de Internet?

   A) Convierte cada película en un vídeo sin compresión
   B) Evita que el cliente necesite conexión a la red
   C) Sustituye las cuentas y permisos por acceso anónimo a todo el catálogo
   D) Acerca los archivos al usuario y reduce tráfico de tránsito externo

15. ¿Qué protocolo corresponde a órdenes de sesión como SETUP, PLAY y PAUSE?

   A) RTSP
   B) RTP
   C) RTCP
   D) MPEG-DASH

16. Un usuario paga una cantidad para alquilar una película concreta, sin contratar una cuota de catálogo. ¿Qué modelo utiliza?

   A) Modelo híbrido de cuota y publicidad
   B) TVOD
   C) AVOD
   D) SVOD

17. Todos los paquetes tardan 200 ms y llegan separados exactamente por los mismos intervalos con los que se enviaron. ¿Qué describe mejor ese enlace idealizado?

   A) No tiene latencia porque conserva los intervalos
   B) Tiene jitter igual al bitrate del vídeo
   C) Tiene retardo constante y no presenta jitter de llegada
   D) Tiene mucho jitter porque el retardo no es cero

18. ¿Qué distingue al streaming frente a esperar a descargar por completo un archivo antes de reproducirlo?

   A) Se reproduce el contenido mientras siguen llegando sus datos
   B) Se reproduce únicamente contenido capturado en directo
   C) Se elimina cualquier almacenamiento temporal del cliente
   D) Se necesita tener todo el archivo antes del primer fotograma

19. Desde una misma interfaz de origen se envía un directo de 8 Mbit/s a 100 usuarios. Sin sobrecarga y suponiendo multicast admitido por la red, ¿qué tráfico sale del origen en cada caso?

   A) Unicast: 8 Mbit/s; multicast: 8 Mbit/s
   B) Unicast: 800 Mbit/s; multicast: 8 Mbit/s
   C) Unicast: 800 Mbit/s; multicast: 800 Mbit/s
   D) Unicast: 8 Mbit/s; multicast: 800 Mbit/s

20. Una presentación reproduce sus contenidos en un orden fijo que el usuario no puede cambiar. ¿A qué categoría pertenece?

   A) Contenido bajo demanda con saltos libres
   B) Hipermedia interactiva con control de secuencia
   C) Hipermedia navegable
   D) Multimedia lineal

21. En el esquema simplificado de Netflix del tema, ¿qué reparto de responsabilidades es correcto?

   A) El OCA factura las suscripciones y el backend sirve todos los bytes de vídeo
   B) El backend gestiona identidad y catálogo; Open Connect entrega el vídeo
   C) El backend solo guarda fotogramas y Open Connect ejecuta el inicio de sesión
   D) El cliente administra los servidores y el OCA decide las recomendaciones

22. La conexión de un espectador pierde capacidad durante la reproducción. ¿Qué puede hacer un cliente de streaming adaptativo?

   A) Cambiar el modelo de pago de SVOD a AVOD
   B) Reproducir el manifiesto como si fuese un segmento de vídeo
   C) Solicitar segmentos de una representación de menor bitrate
   D) Mantener siempre la máxima calidad aunque se vacíe el búfer

23. ¿Qué describe la entrega de contenido OTT?

   A) Contenido por Internet sin exigir un servicio tradicional de TV de pago
   B) Contenido que solo puede verse en emisión simultánea
   C) Contenido que se financia necesariamente con publicidad
   D) Contenido limitado al decodificador de televisión por cable

24. Un cliente solicita reproducir una película. Según el flujo del PDF, ¿qué debe comprobar el servicio de reproducción antes de facilitar el acceso?

   A) Que todos los espectadores utilicen la misma calidad de vídeo
   B) Que la solicitud esté autorizada por el plan y la licencia del contenido
   C) Que todos los OCA contengan la totalidad del catálogo
   D) Que el cliente haya elegido ya el OCA de menor latencia

25. ¿Qué protocolo transporta audio y vídeo en tiempo real con números de secuencia y marcas temporales?

   A) HTTP como protocolo de control de sesiones RTSP
   B) RTSP
   C) RTCP
   D) RTP

26. Una aplicación reproduce vídeo en tiempo real, pero su sistema de archivos entrega datos de forma irregular y demasiado lenta. ¿Qué requisito necesita reforzar directamente?

   A) La rapidez con que aparece el menú inicial de la aplicación
   B) La capacidad total de almacenamiento, aunque la lectura siga igual
   C) La potencia gráfica, manteniendo el mismo suministro insuficiente de datos
   D) La eficiencia y rapidez de entrada/salida de los datos

27. Una plataforma permite ver vídeos gratis e inserta anuncios para financiarlos. ¿Qué modelo representa?

   A) PPV
   B) TVOD
   C) SVOD
   D) AVOD

28. Un vídeo reproduce la imagen y el audio de forma descoordinada. ¿Qué requisito del sistema está fallando directamente?

   A) Convertir el texto a una codificación Unicode
   B) Incrementar el espacio libre del archivo final
   C) Mantener las relaciones temporales entre medios
   D) Aumentar el número de colores de la imagen

29. Un servicio cobra una cuota periódica que da acceso a un catálogo. ¿Qué modelo de vídeo bajo demanda utiliza?

   A) PPV por evento
   B) AVOD
   C) SVOD
   D) TVOD

30. ¿Qué es un OCA en Netflix Open Connect?

   A) Un códec que convierte cada vídeo en paquetes RTP
   B) Un servicio dedicado a facturar las suscripciones
   C) Un servidor que almacena y entrega contenido audiovisual al cliente
   D) Un reproductor instalado en el teléfono del espectador

31. Los paquetes llegan con intervalos variables aunque se enviaran regularmente. ¿Qué fenómeno describe esa variación?

   A) Jitter
   B) Profundidad de color
   C) Latencia constante
   D) Bitrate del códec

32. ¿Qué modalidad de transmisión envía un flujo destinado a un grupo específico de receptores?

   A) Multicast
   B) Descarga local sin red
   C) Unicast
   D) Broadcast

33. ¿Qué requisito permite a un sistema multimedia almacenar y procesar de forma integrada información de medios distintos?

   A) Asignar el mismo tamaño de archivo a todos los medios
   B) Mantener los medios como señales analógicas sin conversión
   C) Utilizar un programa sin relación para cada medio y no intercambiar datos
   D) Representar digitalmente la información bajo control del computador
