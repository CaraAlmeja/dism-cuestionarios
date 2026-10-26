# Solucionario: DISM · T2.1 · Streaming multimedia

## 1. D) Acerca los archivos al usuario y reduce tráfico de tránsito externo

La entrega localizada reduce la distancia de red y la dependencia de enlaces externos. No equivale a reproducir sin conexión ni a eliminar la autorización.

Fuente: Tema2-DISM-1.pdf, páginas PDF 57–59. Contraste: https://openconnect.netflix.com/en/

Distractores:

- A) Los controles de acceso siguen gestionándose aunque la caché sea cercana.
- B) La ubicación del servidor no elimina la codificación de los vídeos.
- C) El cliente sigue necesitando conectividad para solicitar y recibir contenido.

## 2. B) El retraso excesivo dificulta la interacción aunque llegue todo el contenido

En aplicaciones interactivas importa que la información llegue a tiempo. Una tasa suficiente o una entrega sin pérdidas no garantizan por sí mismas baja latencia.

Fuente: Tema2-DISM-1.pdf, páginas PDF 14–15.

Distractores:

- A) Una entrega perfecta pero muy tardía sigue perjudicando la conversación.
- C) Miden capacidad de transferencia y tiempo, respectivamente; hay que atender a ambas.
- D) Una reserva mayor puede mejorar estabilidad, pero añade espera y no elimina la latencia.

## 3. C) AVOD

AVOD significa Advertising Video on Demand: el ingreso principal del modelo descrito procede de la publicidad.

Fuente: Tema2-DISM-1.pdf, páginas PDF 29.

Distractores:

- A) TVOD se basa en pagar por contenido o evento seleccionado.
- B) PPV implica pagar por una visualización o evento, no acceso gratuito financiado con anuncios.
- D) SVOD se basa en una suscripción de acceso al servicio.

## 4. B) 2 segundos

El tiempo es reserva/tasa = 12/6 = 2 s. Aquí todavía no hay consumo de reproducción; no se resta una tasa de salida.

Fuente: Tema2-DISM-1.pdf, páginas PDF 52–53.

Distractores:

- A) En un segundo solo recibe 6 Mbit, la mitad de la reserva solicitada.
- C) Correspondería a recibir 18 Mbit con la tasa indicada.
- D) Confunde la tasa numérica con el tiempo que resulta de dividir reserva entre tasa.

## 5. D) Ayudan a reconstruir el orden y el tiempo de presentación del flujo

RTP incorpora información para ordenar y temporizar el contenido. No garantiza por sí mismo entregar perfectamente todos los paquetes ni controla todas las acciones de sesión.

Fuente: Tema2-DISM-1.pdf, páginas PDF 42–43.

Distractores:

- A) Las marcas temporales aportan precisamente información de tiempo para su tratamiento.
- B) El control de esas órdenes se asocia a RTSP, no a esos campos de RTP.
- C) Esos campos no convierten la red en un transporte sin pérdidas.

## 6. C) RTP

RTP lleva el contenido en tiempo real y aporta secuencias y tiempos para su reproducción. No garantiza por sí mismo recuperar todas las pérdidas.

Fuente: Tema2-DISM-1.pdf, páginas PDF 42–43.

Distractores:

- A) HTTP puede distribuir segmentos, pero no es el protocolo identificado por esa función de RTP.
- B) RTSP controla la sesión y sus órdenes de reproducción.
- D) RTCP informa sobre recepción y calidad, pero no transporta el flujo audiovisual principal.

## 7. C) Un servidor que almacena y entrega contenido audiovisual al cliente

Los Open Connect Appliances son servidores de caché y entrega situados cerca de los usuarios, por ejemplo dentro de ISP o en puntos de intercambio. El cliente recibe de ellos los bytes del vídeo.

Fuente: Tema2-DISM-1.pdf, páginas PDF 57–59, 64. Contraste: https://openconnect.netflix.com/en/

Distractores:

- A) OCA significa Open Connect Appliance; no es un algoritmo de compresión.
- B) El OCA es infraestructura de entrega, no el cliente de reproducción.
- D) La facturación pertenece a la lógica del backend, no a la misión del OCA.

## 8. D) Integra varios medios, como texto, audio e imagen, bajo control informático

Una aplicación multimedia combina información de distintos medios y fuentes, de forma coordinada por el sistema informático.

Fuente: Tema2-DISM-1.pdf, páginas PDF 2–3.

Distractores:

- A) El sistema del tema representa y procesa la información digitalmente.
- B) La multimedia integra diferentes medios; no exige limitarse al vídeo.
- C) La integración controlada es parte del concepto.

## 9. B) No basta para ofrecer por sí solo esas posiciones independientes

El VOD del tema mantiene flujos e interacciones individuales. Un único flujo compartido con el mismo contenido temporal no proporciona por sí solo controles independientes.

Fuente: Tema2-DISM-1.pdf, páginas PDF 25–26.

Distractores:

- A) Eso impediría las posiciones diferentes que requiere el servicio.
- C) La modalidad de envío no crea versiones temporales independientes.
- D) Pausarlo para todos no satisface la independencia pedida.

## 10. B) SVOD

SVOD es Subscription Video on Demand. El criterio aquí es la suscripción periódica, aunque en el mercado existan modelos combinados.

Fuente: Tema2-DISM-1.pdf, páginas PDF 30.

Distractores:

- A) En TVOD se paga una transacción por un contenido concreto.
- C) El pago por evento no describe acceso recurrente a un catálogo.
- D) En el modelo AVOD descrito el acceso se financia con anuncios, no con la cuota.

## 11. C) TEARDOWN

En el flujo del tema, TEARDOWN termina la sesión. Se diferencia de PAUSE, que permite conservarla para reanudar.

Fuente: Tema2-DISM-1.pdf, páginas PDF 46–47.

Distractores:

- A) SETUP prepara la sesión y sus recursos, no la finaliza.
- B) PAUSE detiene temporalmente la reproducción, conservando la sesión.
- D) PLAY inicia o reanuda la reproducción.

## 12. D) Ajustar la transmisión según la calidad de recepción observada

RTCP aporta estadísticas para que la aplicación tome decisiones de adaptación. Informar de una pérdida no equivale a corregirla automáticamente.

Fuente: Tema2-DISM-1.pdf, páginas PDF 43–44.

Distractores:

- A) Confunde supervisión de calidad con control de reproducción.
- B) El informe de pérdidas no reconstruye por sí solo los paquetes.
- C) RTCP complementa al transporte de medios; no convierte sus informes en el contenido.

## 13. A) Navegación entre contenidos de distintos medios

La hipermedia combina medios y un sistema de navegación que permite al usuario elegir su recorrido.

Fuente: Tema2-DISM-1.pdf, páginas PDF 4–5.

Distractores:

- B) La distribución simultánea no explica los enlaces elegidos individualmente.
- C) Una secuencia obligatoria se corresponde con multimedia lineal, sin la elección descrita.
- D) La redundancia de almacenamiento no define la navegación hipermedia.

## 14. C) Tiene retardo constante y no presenta jitter de llegada

La latencia es el tiempo de tránsito; el jitter es su variación. Puede existir latencia elevada con una llegada perfectamente regular.

Fuente: Tema2-DISM-1.pdf, páginas PDF 52–53.

Distractores:

- A) El jitter y el bitrate son magnitudes distintas.
- B) Un retardo grande pero constante no implica variación del retardo.
- D) La latencia sigue siendo 200 ms, aunque los intervalos sean regulares.

## 15. C) Que la solicitud esté autorizada por el plan y la licencia del contenido

El servicio comprueba que la petición sea válida para el contenido y el suscriptor antes de organizar su reproducción.

Fuente: Tema2-DISM-1.pdf, páginas PDF 62–64.

Distractores:

- A) La autorización no exige una representación idéntica para todos los clientes.
- B) La selección del OCA es un paso posterior a validar la petición en el flujo descrito.
- D) No se necesita replicar todo el catálogo en cada caché para autorizar una película.

## 16. D) Contenido por Internet sin exigir un servicio tradicional de TV de pago

OTT describe la vía de entrega a través de Internet. No equivale a un modelo concreto de ingresos ni a un único dispositivo de reproducción.

Fuente: Tema2-DISM-1.pdf, páginas PDF 27–28.

Distractores:

- A) OTT utiliza Internet y puede recibirse en distintos tipos de dispositivo.
- B) OTT no determina la financiación: puede haber AVOD, SVOD o TVOD.
- C) OTT puede ofrecer contenido bajo demanda además de directos.

## 17. A) El canal de control bidireccional

El canal de control recibe interacciones y devuelve respuestas. El esquema lo distingue del canal de transporte de datos multimedia hacia el cliente.

Fuente: Tema2-DISM-1.pdf, páginas PDF 36.

Distractores:

- B) El búfer almacena datos; no sustituye la comunicación de control.
- C) El envío de medios hacia el cliente no es el intercambio de orden y respuesta.
- D) Las interacciones se envían durante la sesión, no se introducen en el archivo del vídeo.

## 18. B) Comprobar si el sistema cumple los requisitos definidos

Las pruebas evalúan si el sistema funciona de acuerdo con sus requisitos en diferentes situaciones de uso.

Fuente: Tema2-DISM-1.pdf, páginas PDF 13.

Distractores:

- A) La producción genera recursos; aquí se está evaluando el sistema.
- C) Los requisitos se establecen durante la planificación y sirven de criterio a las pruebas.
- D) Empaquetar y distribuir no verifica por sí mismo los requisitos.

## 19. B) 4 segundos

La reserva disminuye a 4 − 2 = 2 Mbit/s. Por tanto, tarda 8/2 = 4 s en vaciarse. Un búfer finito no compensa indefinidamente un caudal inferior al consumo.

Fuente: Tema2-DISM-1.pdf, páginas PDF 52–53.

Distractores:

- A) Divide la reserva por el consumo, pero omite los datos que siguen llegando.
- C) No divide por el déficit neto de 2 Mbit/s.
- D) Multiplica por el déficit en lugar de dividir la reserva entre ese déficit.

## 20. C) Servir los segmentos desde su caché si siguen disponibles

En VOD, el proxy puede almacenar información recientemente utilizada y reutilizarla en peticiones posteriores. Así evita volver a traer esos mismos datos del origen.

Fuente: Tema2-DISM-1.pdf, páginas PDF 40.

Distractores:

- A) Desaprovecha la función de caché descrita.
- B) Reutilizar segmentos no exige sincronizar todas las sesiones.
- D) Unicode representa texto; no es la operación que permite reutilizar vídeo en caché.

## 21. D) Planificación y evaluación de costes

La planificación concreta necesidades, costes y especificaciones. Sirve de referencia para producir y evaluar el sistema.

Fuente: Tema2-DISM-1.pdf, páginas PDF 13.

Distractores:

- A) La distribución prepara y entrega el producto al final del proceso.
- B) Las pruebas contrastan el sistema con requisitos ya definidos.
- C) Esa etapa desarrolla los recursos y el código a partir de la planificación.

## 22. C) Una emisión en directo con contenido previamente almacenado

El tipo de servicio depende del control temporal que tiene el usuario, no solo de cuándo se capturó el contenido. El tema distingue emisiones live con información en vivo o almacenada.

Fuente: Tema2-DISM-1.pdf, páginas PDF 21–24.

Distractores:

- A) Que el material esté grabado no implica que cada usuario elija el inicio.
- B) Una programación común no exige descargar el archivo entero antes de reproducir.
- D) El streaming también distribuye información previamente almacenada.

## 23. A) La reproducción se detiene hasta recuperar una reserva suficiente

Cuando el búfer queda vacío aparece un corte o rebuffering. Para continuar, el cliente necesita recibir más datos y puede reducir la calidad si el servicio permite adaptación.

Fuente: Tema2-DISM-1.pdf, páginas PDF 52.

Distractores:

- B) No se puede seguir mostrando contenido nuevo sin recibir sus datos.
- C) RTCP supervisa; no sustituye el contenido que falta.
- D) El almacenamiento temporal no crea el contenido que falta.

## 24. D) La eficiencia y rapidez de entrada/salida de los datos

La captura y reproducción en tiempo real necesitan E/S suficiente y regular. Más capacidad de almacenamiento no implica por sí sola más rapidez de acceso.

Fuente: Tema2-DISM-1.pdf, páginas PDF 14–15.

Distractores:

- A) Una interfaz que abre antes no garantiza el caudal de datos durante el vídeo.
- B) El cuello de botella descrito es entregar datos, no procesarlos una vez recibidos.
- C) Más capacidad no resuelve por sí misma la velocidad o regularidad de lectura.

## 25. D) RTCP

RTCP comunica estadísticas de recepción y calidad para ayudar a controlar la transmisión. Complementa a RTP.

Fuente: Tema2-DISM-1.pdf, páginas PDF 43–44.

Distractores:

- A) RTMP se asocia en el tema al envío del directo al servidor.
- B) RTSP sirve para gestionar la sesión, no es el protocolo de informes de recepción de RTP.
- C) HLS distribuye segmentos HTTP y no es el protocolo de supervisión complementario a RTP.

## 26. A) Vídeo bajo demanda (VOD)

VOD permite solicitar contenidos en el momento elegido y controlar la reproducción. La forma de distribución y el modelo de pago son dimensiones diferentes.

Fuente: Tema2-DISM-1.pdf, páginas PDF 21–27.

Distractores:

- B) Un flujo simultáneo compartido no describe los puntos de reproducción individuales.
- C) Broadcast describe distribución y no garantiza la elección individual indicada.
- D) En ese modelo el usuario sigue la señal que se emite, no elige libremente el punto.

## 27. D) Multimedia lineal

La multimedia lineal mantiene un orden predeterminado sin que el usuario controle los contenidos o su secuencia. La hipermedia incorpora navegación.

Fuente: Tema2-DISM-1.pdf, páginas PDF 4–5.

Distractores:

- A) Los saltos libres contradicen la secuencia que el usuario no puede modificar.
- B) La navegación permitiría elegir el recorrido, que aquí está fijado.
- C) Ese control está expresamente ausente en el caso.

## 28. A) Lo que se está emitiendo en ese momento

En el live clásico descrito, al reanudar se vuelve a la señal actual. El enunciado excluye DVR porque existen servicios reales de directo con otras funciones.

Fuente: Tema2-DISM-1.pdf, páginas PDF 21–22.

Distractores:

- B) El modelo no incorpora una recuperación acelerada del intervalo perdido.
- C) El modelo descrito no ofrece inicio individual bajo demanda.
- D) Ese comportamiento exigiría una función de retardo o recuperación que el caso excluye.

## 29. A) Presentación

El cliente distingue recepción, presentación y búfer. Presentación reproduce la información de forma temporizada y ofrece la interacción al usuario.

Fuente: Tema2-DISM-1.pdf, páginas PDF 51.

Distractores:

- B) Mantiene una reserva temporal; la presentación se encarga de reproducirla según su temporización.
- C) Se encarga de recibir la información solicitada, no de su presentación temporizada.
- D) Conserva contenido en el origen; no presenta el vídeo en el dispositivo del usuario.

## 30. A) Para que el control conozca el estado y contenido de los servidores de entrega

Los informes permiten conocer disponibilidad de contenidos, carga y condiciones relevantes de los OCA. Esa información ayuda a organizar la entrega.

Fuente: Tema2-DISM-1.pdf, páginas PDF 61.

Distractores:

- B) La facturación pertenece al backend de servicio, no a esos informes.
- C) Los informes describen estado; no sustituyen la entrega audiovisual al cliente.
- D) Informar sobre el OCA no cambia el papel del reproductor del usuario.

## 31. A) Permite preparar representaciones que el cliente puede elegir según sus condiciones

El backend prepara contenido y Open Connect entrega archivos codificados en distintas calidades. Esa variedad hace posible adaptar la reproducción; no reemplaza la autorización.

Fuente: Tema2-DISM-1.pdf, páginas PDF 57–58, 67.

Distractores:

- B) La transcodificación no recupera información que ya se descartó de forma irreversible.
- C) Ofrecer varias calidades permite adaptar la entrega a clientes y conexiones distintos.
- D) Preparar vídeo y comprobar permisos son responsabilidades distintas.

## 32. C) Más tolerancia a retrasos y mayor espera inicial

El búfer cambia latencia por estabilidad: reserva más datos para amortiguar retrasos, a costa de mayor retardo de arranque. Una reserva finita no resuelve una conexión insuficiente de manera indefinida.

Fuente: Tema2-DISM-1.pdf, páginas PDF 52–53.

Distractores:

- A) El búfer no aumenta la capacidad física de la red.
- B) El búfer no garantiza recuperar paquetes perdidos ni una espera invariable.
- D) Crear una reserva mayor requiere esperar más datos, no menos.

## 33. A) HLS con M3U8 y MPEG-DASH con MPD

HLS emplea listas M3U8 y DASH usa Media Presentation Description (MPD). Ambos pueden describir segmentos y calidades disponibles.

Fuente: Tema2-DISM-1.pdf, páginas PDF 48–49.

Distractores:

- B) Asigna a RTSP y RTMP los manifiestos de DASH y HLS.
- C) Intercambia los manifiestos de ambas tecnologías.
- D) Los manifiestos corresponden a streaming HTTP, no a esos protocolos RTP/RTCP.

## 34. B) Prueba las conexiones y elige una entrega rápida y fiable

Tras obtener candidatos, el cliente prueba las conexiones y escoge un OCA adecuado para solicitar el vídeo. La cercanía geográfica o la pantalla por sí solas no sustituyen esa evaluación.

Fuente: Tema2-DISM-1.pdf, páginas PDF 64–66.

Distractores:

- A) Las condiciones del enlace también importan para escoger una entrega adecuada.
- C) La distancia geográfica no basta para medir el comportamiento de la ruta de red.
- D) El flujo del tema entrega el vídeo desde un OCA, no desde el servicio de identidad.

## 35. C) TVOD

TVOD es el modelo transaccional: se paga por la pieza o evento elegido. El alquiler digital es un ejemplo.

Fuente: Tema2-DISM-1.pdf, páginas PDF 31.

Distractores:

- A) El contenido aquí se paga directamente y no se ofrece gratis por anuncios.
- B) La suscripción da acceso periódico al catálogo, no describe este alquiler individual.
- D) No hay cuota de catálogo ni anuncios en las condiciones del caso.

## 36. B) Mantener las relaciones temporales entre medios

El sistema debe conservar las relaciones temporales entre flujos. Las marcas de tiempo ayudan a presentar audio y vídeo en el momento que corresponde.

Fuente: Tema2-DISM-1.pdf, páginas PDF 14.

Distractores:

- A) La profundidad de color no determina la sincronización de audio y vídeo.
- C) Tener más espacio no mantiene por sí solo las relaciones de tiempo.
- D) La codificación de caracteres no corrige el desfase audiovisual.

## 37. D) Solicitar segmentos de una representación de menor bitrate

El cliente puede elegir una representación con menor tasa para ajustarse a la red y sostener la reproducción. La decisión combina estimaciones de capacidad y estado del búfer.

Fuente: Tema2-DISM-1.pdf, páginas PDF 39, 48–49.

Distractores:

- A) El manifiesto describe recursos; no contiene por sí mismo el vídeo a reproducir.
- B) La financiación no ajusta la tasa de los segmentos.
- C) Ignora la adaptación y aumenta el riesgo de cortes.

## 38. A) El backend gestiona identidad y catálogo; Open Connect entrega el vídeo

La arquitectura distingue el plano de control (identidad, catálogo y decisiones) de la entrega audiovisual desde Open Connect.

Fuente: Tema2-DISM-1.pdf, páginas PDF 57–59, 67.

Distractores:

- B) El cliente reproduce y los OCA entregan; la personalización pertenece al backend.
- C) Intercambia la función de entrega del OCA con la lógica de servicio del backend.
- D) Reduce el backend a almacenamiento y atribuye al OCA una función de identidad que no le corresponde.

## 39. B) RTSP

RTSP gestiona la sesión como un mando de reproducción. El audio y el vídeo pueden viajar por RTP en otro canal.

Fuente: Tema2-DISM-1.pdf, páginas PDF 46–47.

Distractores:

- A) RTCP supervisa calidad y recepción; no ejecuta esas órdenes de sesión.
- C) RTP transporta datos multimedia; no es el protocolo de esas órdenes.
- D) DASH describe streaming adaptativo HTTP, no ese control de sesión.

## 40. A) Entregar todos los datos no basta si llegan fuera del plazo útil

Los sistemas multimedia temporizados deben atender a cuándo llegan los datos, además de a su integridad. En servicios interactivos, esperar indefinidamente también perjudica la calidad.

Fuente: Tema2-DISM-1.pdf, páginas PDF 14, 42, 53.

Distractores:

- B) La capacidad de transferencia y el tiempo de entrega son aspectos distintos.
- C) La información correcta puede resultar demasiado tardía para una interacción fluida.
- D) Aumentar la reserva puede mejorar estabilidad, pero no elimina el retraso y puede añadir espera.

## 41. B) Los espectadores también pueden reenviar fragmentos a otros peers

Los peers descargan y comparten chunks. El tracker coordina y el seed aporta contenido inicial. Esto reduce carga del origen, aunque añade dependencia de los peers.

Fuente: Tema2-DISM-1.pdf, páginas PDF 54–55.

Distractores:

- A) El seed posee contenido y puede iniciar su distribución.
- C) El tracker coordina peers; no tiene que servir todo el vídeo.
- D) En el esquema descrito se intercambian fragmentos durante la reproducción.

## 42. D) RTMP

RTMP se usa para transportar la señal desde el codificador al servidor. El formato de entrega al espectador puede ser otro, como HLS o DASH.

Fuente: Tema2-DISM-1.pdf, páginas PDF 45.

Distractores:

- A) M3U8 es un formato de lista de reproducción usado por HLS, no ese protocolo de ingestión.
- B) RTCP informa de la calidad de un flujo RTP, no es la ingestión descrita.
- C) RTSP controla sesiones y tampoco se define por informar de pérdidas.

## 43. D) Se reproduce el contenido mientras siguen llegando sus datos

En streaming la recepción y el consumo se solapan. No hay que esperar al archivo completo, aunque suele existir una espera inicial de almacenamiento en búfer.

Fuente: Tema2-DISM-1.pdf, páginas PDF 16–18.

Distractores:

- A) El cliente utiliza un búfer para sostener la reproducción.
- B) El streaming también puede ser bajo demanda.
- C) Esa espera caracteriza la descarga completa previa.

## 44. C) Jitter

Jitter es la variación del retardo o de los instantes de llegada. Un búfer de reproducción puede absorber parte de esa irregularidad.

Fuente: Tema2-DISM-1.pdf, páginas PDF 53.

Distractores:

- A) Una latencia fija desplaza todos los paquetes por igual, sin variar los intervalos.
- B) La profundidad de color describe la representación de píxeles, no la llegada de paquetes.
- D) El bitrate mide cantidad de datos por unidad de tiempo, no la variación de retardo.

## 45. A) Reduce los flujos que deben salir del servidor de origen

El origen puede enviar una sola copia al punto de distribución. La carga de atender las entregas posteriores se desplaza hacia el proxy; no desaparece el tráfico de los clientes.

Fuente: Tema2-DISM-1.pdf, páginas PDF 40.

Distractores:

- B) Cada espectador sigue necesitando los datos para reproducir.
- C) Redistribuir el flujo no añade por sí solo funciones de VOD.
- D) El proxy todavía tiene que entregar el directo a sus clientes.

## 46. B) Unicast: 800 Mbit/s; multicast: 8 Mbit/s

Unicast envía 100 flujos: 100×8 = 800 Mbit/s. Multicast emite un flujo de 8 Mbit/s en el origen y la red lo replica donde corresponde.

Fuente: Tema2-DISM-1.pdf, páginas PDF 25.

Distractores:

- A) Invierte el flujo individual de unicast y el flujo compartido de multicast.
- C) Omite las cien copias individuales que debe enviar ese origen en unicast.
- D) Cuenta una copia por usuario también en el origen multicast.

## 47. C) Multicast

Multicast dirige el flujo a un grupo de receptores. Unicast sirve individualmente y broadcast difunde a los receptores del ámbito de difusión.

Fuente: Tema2-DISM-1.pdf, páginas PDF 25.

Distractores:

- A) Unicast establece un flujo por destinatario.
- B) No es una modalidad de transmisión a un grupo por la red.
- D) Broadcast difunde sin seleccionar ese grupo específico.

## 48. B) Representar digitalmente la información bajo control del computador

La integración requiere representaciones digitales manejables por el sistema. No significa que todos los medios usen un mismo formato o tamaño.

Fuente: Tema2-DISM-1.pdf, páginas PDF 6.

Distractores:

- A) Texto, audio e imagen tienen representaciones y necesidades diferentes; igualar tamaños no los integra.
- C) No permite el procesamiento digital integrado descrito.
- D) La ausencia de integración contradice el sistema multimedia del tema.
