# DISM · T2.1 · Streaming multimedia

Elige una única respuesta por pregunta.

1. ¿Por qué resulta útil ubicar un OCA dentro de la red de un proveedor de Internet?

   A) Sustituye las cuentas y permisos por acceso anónimo a todo el catálogo
   B) Convierte cada película en un vídeo sin compresión
   C) Evita que el cliente necesite conexión a la red
   D) Acerca los archivos al usuario y reduce tráfico de tránsito externo

2. ¿Por qué una videoconferencia necesita cuidar especialmente el retardo además del caudal de datos?

   A) La ausencia de pérdidas garantiza por sí sola una conversación fluida
   B) El retraso excesivo dificulta la interacción aunque llegue todo el contenido
   C) Ancho de banda y latencia son dos nombres de la misma magnitud
   D) Aumentar la reserva de búfer elimina el retraso percibido

3. Una plataforma permite ver vídeos gratis e inserta anuncios para financiarlos. ¿Qué modelo representa?

   A) TVOD
   B) PPV
   C) AVOD
   D) SVOD

4. Antes de iniciar la reproducción, un cliente quiere acumular 12 Mbit y recibe a 6 Mbit/s constantes. Sin consumo durante esa espera, ¿cuánto tarda en reunir la reserva?

   A) 1 segundo
   B) 2 segundos
   C) 3 segundos
   D) 6 segundos

5. Un flujo multimedia recibe paquetes fuera de orden. ¿Para qué sirven los números de secuencia y marcas temporales de RTP?

   A) Eliminan la necesidad de interpretar el tiempo del contenido
   B) Sustituyen las órdenes de iniciar y pausar la sesión
   C) Garantizan que la red entregará todos los paquetes sin pérdidas
   D) Ayudan a reconstruir el orden y el tiempo de presentación del flujo

6. ¿Qué protocolo transporta audio y vídeo en tiempo real con números de secuencia y marcas temporales?

   A) HTTP como protocolo de control de sesiones RTSP
   B) RTSP
   C) RTP
   D) RTCP

7. ¿Qué es un OCA en Netflix Open Connect?

   A) Un códec que convierte cada vídeo en paquetes RTP
   B) Un reproductor instalado en el teléfono del espectador
   C) Un servidor que almacena y entrega contenido audiovisual al cliente
   D) Un servicio dedicado a facturar las suscripciones

8. ¿Qué caracteriza a una aplicación multimedia?

   A) Sustituye los datos digitales por señales analógicas independientes
   B) Utiliza exclusivamente vídeo, aunque disponga de texto o sonido
   C) Presenta cada medio en un equipo aislado, sin integración entre ellos
   D) Integra varios medios, como texto, audio e imagen, bajo control informático

9. Tres usuarios ven la misma película en puntos distintos y pueden pausar por separado. ¿Qué plantea eso para un único flujo multicast idéntico a todos?

   A) Los tres usuarios deben recibir necesariamente el mismo fotograma
   B) No basta para ofrecer por sí solo esas posiciones independientes
   C) Multicast convierte automáticamente cada posición en un archivo diferente
   D) Cada pausa individual se resuelve pausando ese flujo para todos

10. Un servicio cobra una cuota periódica que da acceso a un catálogo. ¿Qué modelo de vídeo bajo demanda utiliza?

   A) TVOD
   B) SVOD
   C) PPV por evento
   D) AVOD

11. El reproductor quiere finalizar una sesión RTSP y liberar su estado, en lugar de pausarla temporalmente. ¿Qué orden corresponde?

   A) SETUP
   B) PAUSE
   C) TEARDOWN
   D) PLAY

12. El receptor informa mediante RTCP de pérdidas y retardo variable. ¿Qué uso puede dar la aplicación a ese feedback?

   A) Enviar la orden de pausa como si RTCP fuera el mando RTSP
   B) Dar por recuperados automáticamente todos los paquetes perdidos
   C) Sustituir el audio y el vídeo por los informes de control
   D) Ajustar la transmisión según la calidad de recepción observada

13. Un museo ofrece fichas de obras enlazadas con vídeos y audios. El visitante elige qué enlaces seguir. ¿Qué rasgo aporta la hipermedia?

   A) Navegación entre contenidos de distintos medios
   B) Transmisión de un único directo a todos los visitantes
   C) Reproducción de todo el material en una secuencia obligatoria
   D) Duplicación del mismo vídeo en varios discos

14. Todos los paquetes tardan 200 ms y llegan separados exactamente por los mismos intervalos con los que se enviaron. ¿Qué describe mejor ese enlace idealizado?

   A) Tiene jitter igual al bitrate del vídeo
   B) Tiene mucho jitter porque el retardo no es cero
   C) Tiene retardo constante y no presenta jitter de llegada
   D) No tiene latencia porque conserva los intervalos

15. Un cliente solicita reproducir una película. Según el flujo del PDF, ¿qué debe comprobar el servicio de reproducción antes de facilitar el acceso?

   A) Que todos los espectadores utilicen la misma calidad de vídeo
   B) Que el cliente haya elegido ya el OCA de menor latencia
   C) Que la solicitud esté autorizada por el plan y la licencia del contenido
   D) Que todos los OCA contengan la totalidad del catálogo

16. ¿Qué describe la entrega de contenido OTT?

   A) Contenido limitado al decodificador de televisión por cable
   B) Contenido que se financia necesariamente con publicidad
   C) Contenido que solo puede verse en emisión simultánea
   D) Contenido por Internet sin exigir un servicio tradicional de TV de pago

17. En la arquitectura de streaming del tema, el cliente envía PAUSE y el servidor confirma la orden. ¿Qué canal permite ese intercambio?

   A) El canal de control bidireccional
   B) El búfer local, que envía por sí mismo todas las respuestas del servidor
   C) El canal unidireccional que transporta el vídeo al cliente
   D) El archivo comprimido del vídeo, que contiene las órdenes del usuario

18. Un equipo ejecuta su aplicación en distintas situaciones y contrasta el resultado con las especificaciones. ¿Cuál es el propósito de esa etapa?

   A) Producir todos los audios y vídeos que aún faltan
   B) Comprobar si el sistema cumple los requisitos definidos
   C) Definir por primera vez qué producto se quiere construir
   D) Limitarse a empaquetar la aplicación para su distribución

19. Un reproductor guarda una reserva de 8 Mbit. Consume a 4 Mbit/s y recibe de forma constante 2 Mbit/s. Sin adaptación de calidad, ¿cuánto tarda en agotar esa reserva?

   A) 2 segundos
   B) 4 segundos
   C) 8 segundos
   D) 16 segundos

20. Varios clientes solicitan de nuevo segmentos que un proxy VOD acaba de guardar. ¿Qué puede hacer ese proxy?

   A) Volver a solicitarlos siempre al origen aunque sean reutilizables
   B) Obligar a todos los clientes a compartir los mismos controles de reproducción
   C) Servir los segmentos desde su caché si siguen disponibles
   D) Cambiar la codificación del contenido a Unicode antes de enviarlo

21. Antes de producir los materiales se estiman personas, equipos, costes y tiempo, y se redactan los requisitos. ¿A qué etapa corresponde?

   A) Distribución y promoción del producto
   B) Pruebas de conformidad del sistema terminado
   C) Diseño y producción de materiales
   D) Planificación y evaluación de costes

22. Un servidor emite a una hora fija un vídeo grabado y todos los espectadores siguen el mismo instante del programa. ¿Qué describe mejor el servicio?

   A) Vídeo bajo demanda porque el material fue grabado antes
   B) Descarga completa previa porque todos ven el mismo contenido
   C) Una emisión en directo con contenido previamente almacenado
   D) Un servicio que no puede utilizar streaming por no proceder de una cámara

23. El cliente consume todos los datos almacenados y todavía no ha recibido los siguientes. ¿Qué sucede normalmente?

   A) La reproducción se detiene hasta recuperar una reserva suficiente
   B) La reproducción continúa indefinidamente con calidad original
   C) La sesión cambia obligatoriamente al protocolo RTCP
   D) El reproductor inventa los segmentos que faltan en el servidor

24. Una aplicación reproduce vídeo en tiempo real, pero su sistema de archivos entrega datos de forma irregular y demasiado lenta. ¿Qué requisito necesita reforzar directamente?

   A) La rapidez con que aparece el menú inicial de la aplicación
   B) La potencia gráfica, manteniendo el mismo suministro insuficiente de datos
   C) La capacidad total de almacenamiento, aunque la lectura siga igual
   D) La eficiencia y rapidez de entrada/salida de los datos

25. Una aplicación necesita informes de pérdidas y variación del retardo de un flujo RTP. ¿Qué protocolo aporta esa supervisión?

   A) RTMP
   B) RTSP
   C) HLS
   D) RTCP

26. Un usuario elige una película del catálogo y decide cuándo empezar y a qué punto saltar. ¿Qué tipo de servicio describe?

   A) Vídeo bajo demanda (VOD)
   B) Multicast de un único evento en el mismo instante
   C) Difusión broadcast de una programación fija
   D) Emisión live sin retroceso

27. Una presentación reproduce sus contenidos en un orden fijo que el usuario no puede cambiar. ¿A qué categoría pertenece?

   A) Contenido bajo demanda con saltos libres
   B) Hipermedia navegable
   C) Hipermedia interactiva con control de secuencia
   D) Multimedia lineal

28. En el modelo live del temario, sin DVR ni retroceso, un usuario pausa durante un minuto y después reanuda. ¿Qué ve?

   A) Lo que se está emitiendo en ese momento
   B) El minuto perdido acelerado antes de volver al directo
   C) El programa desde el comienzo del archivo
   D) El punto exacto que pausó, con un minuto de retraso

29. Ya han llegado los datos al cliente y deben mostrarse respetando su temporización. ¿Qué componente del esquema se encarga de reproducirlos?

   A) Presentación
   B) Búfer
   C) Recepción
   D) Sistema de almacenamiento del servidor

30. Según el flujo Netflix del PDF, ¿para qué comunican los OCA su carga y los vídeos disponibles al servicio de control de caché?

   A) Para que el control conozca el estado y contenido de los servidores de entrega
   B) Para que el OCA cobre directamente el plan de cada espectador
   C) Para enviar cada película entera dentro de los informes de salud
   D) Para convertir al cliente en un servidor OCA de la misma red

31. ¿Qué relación tiene la transcodificación con ofrecer un vídeo de Netflix en varias calidades?

   A) Permite preparar representaciones que el cliente puede elegir según sus condiciones
   B) Convierte un vídeo con pérdida en una copia idéntica de todo detalle original
   C) Obliga a todos los clientes a reproducir siempre la misma representación
   D) Sustituye el servicio de identidad y autorización de la cuenta

32. Si se aumenta la reserva de reproducción antes de empezar, ¿qué compromiso se espera, en igualdad de las demás condiciones?

   A) Menos tolerancia a retrasos y mayor capacidad de la red
   B) La misma espera inicial y eliminación de todas las pérdidas
   C) Más tolerancia a retrasos y mayor espera inicial
   D) Más tolerancia a retrasos y menor espera inicial

33. ¿Qué pareja de tecnología y manifiesto está correctamente asociada?

   A) HLS con M3U8 y MPEG-DASH con MPD
   B) RTSP con MPD y RTMP con M3U8
   C) HLS con MPD y MPEG-DASH con M3U8
   D) RTP con M3U8 y RTCP con MPD

34. El cliente recibe una lista de OCA apropiados para un vídeo. En el esquema del PDF, ¿qué criterio utiliza después para elegir uno?

   A) Selecciona solo por la resolución de pantalla, ignorando la conexión
   B) Prueba las conexiones y elige una entrega rápida y fiable
   C) Elige siempre el geográficamente más cercano sin medir la conexión
   D) Descarta los OCA y descarga obligatoriamente del servicio de identidad

35. Un usuario paga una cantidad para alquilar una película concreta, sin contratar una cuota de catálogo. ¿Qué modelo utiliza?

   A) AVOD
   B) SVOD
   C) TVOD
   D) Modelo híbrido de cuota y publicidad

36. Un vídeo reproduce la imagen y el audio de forma descoordinada. ¿Qué requisito del sistema está fallando directamente?

   A) Aumentar el número de colores de la imagen
   B) Mantener las relaciones temporales entre medios
   C) Incrementar el espacio libre del archivo final
   D) Convertir el texto a una codificación Unicode

37. La conexión de un espectador pierde capacidad durante la reproducción. ¿Qué puede hacer un cliente de streaming adaptativo?

   A) Reproducir el manifiesto como si fuese un segmento de vídeo
   B) Cambiar el modelo de pago de SVOD a AVOD
   C) Mantener siempre la máxima calidad aunque se vacíe el búfer
   D) Solicitar segmentos de una representación de menor bitrate

38. En el esquema simplificado de Netflix del tema, ¿qué reparto de responsabilidades es correcto?

   A) El backend gestiona identidad y catálogo; Open Connect entrega el vídeo
   B) El cliente administra los servidores y el OCA decide las recomendaciones
   C) El OCA factura las suscripciones y el backend sirve todos los bytes de vídeo
   D) El backend solo guarda fotogramas y Open Connect ejecuta el inicio de sesión

39. ¿Qué protocolo corresponde a órdenes de sesión como SETUP, PLAY y PAUSE?

   A) RTCP
   B) RTSP
   C) RTP
   D) MPEG-DASH

40. En una comunicación audiovisual interactiva, un paquete llega íntegro después del instante en que debía reproducirse. ¿Qué limitación ilustra?

   A) Entregar todos los datos no basta si llegan fuera del plazo útil
   B) Basta aumentar el caudal máximo anunciado sin atender al retardo real
   C) La ausencia de errores de bits garantiza que el retardo deja de importar
   D) Un búfer más grande garantiza que el retardo percibido sea cero

41. ¿Qué distingue al streaming P2P del esquema cliente-servidor descrito en el tema?

   A) El seed solo controla el pago y nunca aporta fragmentos
   B) Los espectadores también pueden reenviar fragmentos a otros peers
   C) Cada espectador recibe todo el vídeo únicamente del tracker
   D) Cada cliente necesita haber descargado todo antes de compartir

42. Un codificador envía una señal en directo a la plataforma antes de que esta la distribuya a espectadores. ¿Qué protocolo asocia el tema a esa ingestión?

   A) M3U8 como protocolo de subida
   B) RTCP
   C) RTSP como informe de pérdidas
   D) RTMP

43. ¿Qué distingue al streaming frente a esperar a descargar por completo un archivo antes de reproducirlo?

   A) Se elimina cualquier almacenamiento temporal del cliente
   B) Se reproduce únicamente contenido capturado en directo
   C) Se necesita tener todo el archivo antes del primer fotograma
   D) Se reproduce el contenido mientras siguen llegando sus datos

44. Los paquetes llegan con intervalos variables aunque se enviaran regularmente. ¿Qué fenómeno describe esa variación?

   A) Latencia constante
   B) Profundidad de color
   C) Jitter
   D) Bitrate del códec

45. Un servidor envía una copia de un directo a un proxy, que lo distribuye a muchos clientes. ¿Qué ventaja aporta respecto a enviar desde el origen una copia por cliente?

   A) Reduce los flujos que deben salir del servidor de origen
   B) Evita que los clientes necesiten recibir los datos del vídeo
   C) Convierte el directo en un servicio con inicio libre para cada usuario
   D) Elimina el tráfico entre el proxy y los espectadores

46. Desde una misma interfaz de origen se envía un directo de 8 Mbit/s a 100 usuarios. Sin sobrecarga y suponiendo multicast admitido por la red, ¿qué tráfico sale del origen en cada caso?

   A) Unicast: 8 Mbit/s; multicast: 800 Mbit/s
   B) Unicast: 800 Mbit/s; multicast: 8 Mbit/s
   C) Unicast: 8 Mbit/s; multicast: 8 Mbit/s
   D) Unicast: 800 Mbit/s; multicast: 800 Mbit/s

47. ¿Qué modalidad de transmisión envía un flujo destinado a un grupo específico de receptores?

   A) Unicast
   B) Descarga local sin red
   C) Multicast
   D) Broadcast

48. ¿Qué requisito permite a un sistema multimedia almacenar y procesar de forma integrada información de medios distintos?

   A) Asignar el mismo tamaño de archivo a todos los medios
   B) Representar digitalmente la información bajo control del computador
   C) Mantener los medios como señales analógicas sin conversión
   D) Utilizar un programa sin relación para cada medio y no intercambiar datos
