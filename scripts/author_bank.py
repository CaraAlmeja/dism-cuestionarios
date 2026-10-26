"""Banco original, redactado a partir de los materiales de DISM y el alcance indicado."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
BLOCKS = [
    {'id':'t1','code':'T1','title':'Aplicaciones multiplataforma','subtitle':'Nativo, híbrido y frameworks','icon':'layers','color':'purple'},
    {'id':'t21','code':'T2.1','title':'Streaming multimedia','subtitle':'Servicios, protocolos y distribución','icon':'play','color':'blue'},
    {'id':'t22','code':'T2.2','title':'Almacenamiento y arquitecturas','subtitle':'RAID, formatos y procesamiento','icon':'database','color':'orange'},
    {'id':'t31','code':'T3.1','title':'Dispositivos y conectividad','subtitle':'Wearables, pantallas y redes','icon':'watch','color':'pink'},
    {'id':'t32','code':'T3.2','title':'Telefonía móvil','subtitle':'Celdas, traspasos y tráfico','icon':'signal','color':'green'},
]
FILES = {
    't1':'Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf',
    't21':'Tema2-DISM-1.pdf','t22':'Tema2-DISM-2.pdf',
    't31':'Tema3-DISM-1.pdf','t32':'Tema3-DISM-21.pdf',
    't4':'OpenAPI Initiative · What is OpenAPI?',
}
questions=[]
def q(block, tag, pages, stem, correct, wrong, explanation, level='Comprensión', url=None):
    idx = max((int(x['id'].rsplit('-',1)[1]) for x in questions if x['block']==block),default=0)+1
    opts=[{'id':'o1','text':correct}]+[{'id':f'o{i+2}','text':t} for i,(t,r) in enumerate(wrong)]
    source=f'{FILES[block]}, páginas PDF {pages}.' if block!='t4' else f'{FILES[block]} · {pages}.'
    if url: source += ' Contraste: '+url
    questions.append({'id':f'{block}-{idx:02}','block':block,'tag':tag,'objective':tag,
        'level':level,'stem':stem,'options':opts,'correct_option_id':'o1',
        'explanation':explanation,'distractor_rationales':{f'o{i+2}':r for i,(t,r) in enumerate(wrong)},
        'source':source,'source_file':FILES[block],'source_pages':pages,'source_type':'web' if block=='t4' else 'pdf','reference_url':url,'shuffle_options':True})
    return questions[-1]

# T1: identificación de herramientas y decisiones; se excluye arquitectura interna.
q('t1','Híbrido frente a nativo','13–16',
  'Una app móvil muestra HTML, CSS y JavaScript dentro de una WebView instalada con la app. ¿Qué enfoque utiliza?',
  'Desarrollo híbrido', [('Desarrollo nativo con Swift','Swift no describe una interfaz HTML ejecutada en una WebView.'),('Desarrollo nativo con Kotlin','El lenguaje de Android no convierte una interfaz web en controles nativos.'),('Desarrollo con controles nativos de MAUI','MAUI usa controles de plataforma en el enfoque nativo descrito, no esta interfaz web.')],
  'El rasgo decisivo es la interfaz web ejecutada en una WebView dentro de la aplicación. Instalarla desde una tienda no cambia su naturaleza híbrida.')
q('t1','Criterio de clasificación','16, 57',
  'Un equipo utiliza JavaScript con React Native y componentes de interfaz nativos. ¿Cómo se clasifica este enfoque en el tema?',
  'Multiplataforma con interfaz nativa', [('Híbrido por utilizar JavaScript','El lenguaje por sí solo no determina que exista una interfaz híbrida.'),('Web tradicional por utilizar React','React Native no presenta la app como una página HTML tradicional.'),('PWA por compartir el código','Compartir código no implica distribución como aplicación web progresiva.')],
  'React Native permite construir una interfaz con componentes nativos utilizando JavaScript o TypeScript. La clasificación depende de cómo se ejecuta y presenta la app, no solo de su lenguaje.')
q('t1','Ventajas del enfoque híbrido','13–14',
  'Un equipo domina HTML, CSS y JavaScript y quiere una app sencilla para iOS y Android con una base compartida. ¿Qué ventaja le aporta el enfoque híbrido?',
  'Reutilizar conocimientos web y reducir duplicación de desarrollo', [('Mantener dos bases de código independientes con el mismo lenguaje','El ahorro destacado se obtiene compartiendo código, no manteniendo dos implementaciones independientes.'),('Compilar el HTML en controles UIKit y Android Views','El enfoque híbrido descrito mantiene la interfaz en una WebView.'),('Sustituir las pruebas de dispositivo por pruebas de navegador','La base compartida sigue necesitando pruebas en los dispositivos objetivo.')],
  'La reutilización de código y de las competencias web puede reducir tiempo y coste. El ahorro no elimina las pruebas específicas ni las diferencias entre plataformas.', 'Aplicación')
q('t1','Limitaciones del enfoque híbrido','15, 41',
  'Una app híbrida necesita un sensor nuevo que todavía no dispone de integración. ¿Qué dependencia puede retrasar su implementación?',
  'La disponibilidad o creación de un plugin para ese sensor', [('La necesidad de convertir todo el código a HTML estático','El acceso al sensor requiere integración nativa, no eliminar la lógica.'),('La imposibilidad de instalar apps híbridas desde tiendas','Las apps híbridas pueden empaquetarse y distribuirse en tiendas.'),('La obligación de sustituir CSS por XAML','XAML pertenece a otro ecosistema y no resuelve por sí mismo ese acceso.')],
  'El código web accede a muchas funciones del dispositivo a través de plugins. Si falta el del sensor, hay que implementarlo o esperar a que exista.', 'Aplicación')
q('t1','Desarrollo específico','8, 12',
  '¿Qué pareja de lenguaje y entorno corresponde al desarrollo específico de aplicaciones iOS descrito en el tema?',
  'Swift y Xcode', [('Kotlin y Android Studio','Esta pareja corresponde a Android.'),('Dart y Android Studio como SDK exclusivo de Apple','Dart se asocia con Flutter; no es el lenguaje específico de iOS.'),('C# y una WebView de Cordova','Cordova usa tecnologías web y C# se asocia con el ecosistema .NET.')],
  'Para iOS, el tema sitúa Swift (y el histórico Objective-C) junto a Xcode. Para Android, sitúa Kotlin y Android Studio.')
q('t1','Xamarin','18–19, 24',
  'En el contexto histórico del temario, ¿qué describe mejor a Xamarin?',
  'Una herramienta para crear apps nativas compartiendo código C#', [('Un framework web basado exclusivamente en HTML y CSS','Xamarin pertenece a .NET y utiliza C#, no solo tecnologías web.'),('Un SDK de Google cuyo lenguaje principal es Dart','Esta descripción corresponde a Flutter.'),('Una tecnología de JetBrains centrada en compartir código Kotlin','Esta descripción corresponde a Kotlin Multiplatform.')],
  'Xamarin permitió reutilizar C# en aplicaciones móviles nativas. El material lo presenta como antecedente histórico de .NET MAUI, no como una recomendación de soporte actual.')
q('t1','Apache Cordova','26–30',
  '¿Para qué se utiliza Apache Cordova en el modelo de desarrollo del tema?',
  'Empaquetar apps web móviles y acceder al dispositivo mediante plugins', [('Compilar Dart para dibujar interfaces con widgets','Esta función corresponde al enfoque de Flutter.'),('Compartir lógica Kotlin conservando interfaces por plataforma','Ese objetivo se asocia con Kotlin Multiplatform.'),('Crear interfaces nativas usando C# y XAML','Esa combinación se asocia con MAUI o Xamarin.Forms.')],
  'Cordova permite usar HTML, CSS y JavaScript en una app empaquetada y ofrece plugins para cámara, GPS y otras capacidades. La interfaz continúa siendo web.')
q('t1','Ionic','33, 37, 39',
  '¿Qué es Ionic según el temario?',
  'Un framework de interfaces y apps multiplataforma con tecnologías web', [('Un lenguaje que sustituye a JavaScript en el navegador','Ionic es un framework; no un nuevo lenguaje de programación.'),('Un SDK que obliga a escribir todas las vistas en Dart','Dart es el lenguaje de Flutter, no un requisito de Ionic.'),('Una herramienta de Apple exclusiva para apps iOS','Ionic permite distintos destinos y no es una herramienta exclusiva de Apple.')],
  'Ionic facilita aplicaciones con tecnologías web y componentes adaptados visualmente a cada plataforma. Puede trabajar con Angular, React o Vue.')
q('t1','Capacitor','34–37',
  'En una app Ionic, ¿qué papel cumple Capacitor cuando se necesita usar la cámara?',
  'Ofrecer integración con funciones nativas mediante plugins', [('Sustituir JavaScript por el lenguaje Dart','Capacitor no convierte la app en Flutter.'),('Transformar toda la interfaz en controles XAML','XAML pertenece a .NET y no es la función de Capacitor.'),('Servir exclusivamente como sistema de estilos CSS','El sistema de estilos no proporciona la integración nativa que necesita la cámara.')],
  'Capacitor conecta el código web con capacidades del dispositivo mediante plugins. La apariencia similar a la del sistema no implica que la interfaz deje de ser web.')
q('t1','TypeScript','38',
  '¿Qué relación mantiene TypeScript con JavaScript?',
  'Añade capacidades como tipos y se transpila a JavaScript', [('Es un subconjunto que elimina las funciones de JavaScript','TypeScript amplía JavaScript; no se define por eliminar sus funciones.'),('Es un lenguaje exclusivo de bases de datos relacionales','No es un lenguaje de consulta de bases de datos.'),('Es código máquina que ejecuta directamente la GPU','Su resultado habitual para la web es JavaScript, no instrucciones de GPU.')],
  'TypeScript incorpora un sistema de tipos y otras herramientas para el desarrollo. El código se transforma a JavaScript para ejecutarse en el entorno web.')
q('t1','PWA','42–44',
  '¿Qué caracteriza a una Progressive Web App (PWA)?',
  'Una app web con capacidades como instalación y funcionamiento sin conexión', [('Una app que solo puede obtenerse desde una tienda móvil','Una PWA puede descubrirse y compartirse mediante una URL.'),('Un ejecutable de escritorio escrito obligatoriamente en Rust','Rust y los ejecutables de escritorio no definen una PWA.'),('Una interfaz que exige controles nativos de UIKit','La base de la PWA son tecnologías web, no UIKit.')],
  'Una PWA parte de una aplicación web e incorpora capacidades de experiencia de app. El funcionamiento sin conexión depende de lo que se implemente y almacene, no significa que todos sus servicios funcionen sin red.')
q('t1','Funcionamiento sin conexión','43–44',
  'Una PWA quiere abrir los recursos de estudio ya descargados cuando no hay conexión. ¿Qué mecanismo del tema lo hace posible?',
  'Un service worker con una estrategia de caché', [('Un manifiesto que convierte automáticamente la web en código Swift','El manifiesto describe la app; no compila Swift ni guarda por sí solo los recursos.'),('Una suscripción a la tienda de aplicaciones','La suscripción no proporciona el almacenamiento de recursos web.'),('Una hoja de estilos con diseño adaptable','CSS adapta la presentación; no intercepta peticiones ni proporciona caché programable.')],
  'El service worker permite gestionar peticiones y recursos en caché. Para abrir contenido sin conexión, ese contenido debe haberse guardado previamente.', 'Aplicación')
q('t1','.NET MAUI','48–49',
  '¿Qué es .NET MAUI?',
  'Un framework para apps nativas móviles y de escritorio con C# y XAML', [('Un reproductor de streaming adaptativo para navegadores','MAUI es una herramienta de desarrollo de aplicaciones, no un protocolo o reproductor.'),('Un framework híbrido que exige HTML para todas las interfaces','El enfoque nativo de MAUI utiliza C# y XAML; HTML no es obligatorio.'),('Un compilador de Dart mantenido por Google','Esa asociación corresponde al ecosistema Flutter, no a MAUI.')],
  '.NET Multi-platform App UI permite compartir una base de código C# y XAML para Android, iOS, macOS y Windows. Aquí se evalúa qué es, sin preguntar su arquitectura interna.')
q('t1','Flutter','53–54',
  '¿Qué combinación identifica a Flutter en el temario?',
  'SDK de Google y lenguaje Dart', [('Framework de Microsoft y lenguaje C#','Esta combinación se relaciona con .NET MAUI.'),('Tecnología de JetBrains y lenguaje Kotlin','Esta combinación se relaciona con Kotlin Multiplatform.'),('Framework de Meta y lenguaje JavaScript','Esta combinación se relaciona con React Native.')],
  'Flutter es el SDK multiplataforma de Google cuyo lenguaje de desarrollo es Dart. Permite crear apps para móvil, web y escritorio.')
q('t1','React Native','57',
  'Un equipo domina React y quiere crear apps iOS y Android con interfaz nativa usando JavaScript o TypeScript. ¿Qué herramienta encaja directamente?',
  'React Native', [('Apache Cordova','Cordova ofrece el enfoque de app web empaquetada, no la interfaz nativa solicitada.'),('Flutter','Flutter utiliza Dart; no es la opción que reutiliza directamente React.'),('.NET MAUI','MAUI se centra en C# y XAML, no en React con JS/TS.')],
  'React Native combina el modelo de React con componentes nativos para las plataformas móviles. Es la opción alineada con el conocimiento y el resultado solicitados.', 'Aplicación')
q('t1','Kotlin Multiplatform','60–61',
  'Un equipo quiere compartir reglas de negocio en Kotlin y conservar una interfaz diferente para iOS y Android. ¿Qué tecnología se ajusta a ese objetivo?',
  'Kotlin Multiplatform', [('Ionic con una interfaz HTML compartida','Ionic prioriza la interfaz web; no el objetivo de lógica común en Kotlin indicado.'),('Cordova con plugins JavaScript','Cordova no es la tecnología de compartición de lógica Kotlin descrita.'),('Flutter con widgets Dart','Flutter propone Dart y una interfaz con sus widgets, que no es el requisito dado.')],
  'KMP permite compartir lógica y conservar interfaces específicas. Compartir UI es una posibilidad adicional con Compose Multiplatform, no una obligación.', 'Aplicación')
q('t1','Tauri','64',
  '¿Qué herramienta del temario combina una interfaz de tecnologías web con un núcleo en Rust para crear apps ligeras?',
  'Tauri', [('Flutter','Flutter utiliza Dart y su propio sistema de interfaz.'),('Xamarin','Xamarin utiliza C# y el ecosistema .NET.'),('Kotlin Multiplatform','KMP comparte código Kotlin; no se define por un núcleo Rust.')],
  'Tauri utiliza tecnologías web para la interfaz y Rust para el núcleo nativo. El tema destaca que aprovecha la WebView del sistema en lugar de empaquetar un navegador completo.')
q('t1','Uno Platform','52, 69',
  'Un equipo de C# y XAML necesita llevar la misma app también al navegador mediante WebAssembly. ¿Qué alternativa destaca el tema?',
  'Uno Platform', [('.NET MAUI como destino web integrado del tema','El material diferencia Uno por incluir WebAssembly entre sus destinos.'),('React Native como framework de XAML','React Native usa JS/TS con React; no se define por XAML.'),('Apache Cordova como compilador de C# a WebAssembly','Cordova empaqueta tecnologías web, no ofrece ese modelo C#/XAML.')],
  'Uno Platform es una alternativa del ecosistema .NET con soporte de WebAssembly y Linux, además de destinos móviles y de escritorio.', 'Aplicación')
q('t1','Elección de enfoque','3, 11–15',
  'Una app necesita aprovechar funciones muy específicas del dispositivo y prioriza la integración con su plataforma. ¿Qué enfoque del tema ofrece el acceso más directo?',
  'Desarrollo específico con las herramientas nativas de la plataforma', [('Desarrollo híbrido con plugins para sus capacidades de hardware','Los plugins pueden ofrecer acceso, pero añaden una integración intermedia respecto a las APIs nativas.'),('Una PWA mediante las APIs compatibles del navegador','Las capacidades dependen de las APIs y permisos expuestos por el navegador.'),('Una interfaz web dentro de un contenedor multiplataforma','El contenedor requiere integración adicional para acceder a las funciones del dispositivo.')],
  'El desarrollo específico utiliza las herramientas y APIs de la plataforma. Puede exigir más esfuerzo al mantener versiones distintas, pero facilita aprovechar sus particularidades.', 'Aplicación')
q('t1','Multiplataforma y pruebas','11–12, 70',
  'Después de compartir código con un framework multiplataforma, ¿qué tarea sigue siendo necesaria?',
  'Probar y ajustar el comportamiento en cada plataforma objetivo', [('Comprobar solo la lógica común en el equipo de desarrollo','No cubre diferencias de interfaz, permisos o integración del dispositivo.'),('Probar una única plataforma y extrapolar los resultados al resto','Compartir código no garantiza el mismo resultado visual y funcional en todas.'),('Verificar solo la compilación para cada sistema operativo','Compilar sin errores no comprueba el comportamiento durante la ejecución.')],
  'El código compartido reduce duplicación, pero el material recuerda la puesta a punto por sistema operativo y la elección según los requisitos del proyecto.', 'Aplicación')

# T2.1: dos preguntas introductorias y prioridad a servicios y streaming.
q('t21','Multimedia lineal','4–5',
  'Una presentación reproduce sus contenidos en un orden fijo que el usuario no puede cambiar. ¿A qué categoría pertenece?',
  'Multimedia lineal', [('Hipermedia navegable','La navegación permitiría elegir el recorrido, que aquí está fijado.'),('Hipermedia interactiva con control de secuencia','Ese control está expresamente ausente en el caso.'),('Contenido bajo demanda con saltos libres','Los saltos libres contradicen la secuencia que el usuario no puede modificar.')],
  'La multimedia lineal mantiene un orden predeterminado sin que el usuario controle los contenidos o su secuencia. La hipermedia incorpora navegación.')
q('t21','Sincronización multimedia','14',
  'Un vídeo reproduce la imagen y el audio de forma descoordinada. ¿Qué requisito del sistema está fallando directamente?',
  'Mantener las relaciones temporales entre medios', [('Aumentar el número de colores de la imagen','La profundidad de color no determina la sincronización de audio y vídeo.'),('Convertir el texto a una codificación Unicode','La codificación de caracteres no corrige el desfase audiovisual.'),('Incrementar el espacio libre del archivo final','Tener más espacio no mantiene por sí solo las relaciones de tiempo.')],
  'El sistema debe conservar las relaciones temporales entre flujos. Las marcas de tiempo ayudan a presentar audio y vídeo en el momento que corresponde.', 'Aplicación')
q('t21','Concepto de streaming','16–18',
  '¿Qué distingue al streaming frente a esperar a descargar por completo un archivo antes de reproducirlo?',
  'Se reproduce el contenido mientras siguen llegando sus datos', [('Se necesita tener todo el archivo antes del primer fotograma','Esa espera caracteriza la descarga completa previa.'),('Se reproduce únicamente contenido capturado en directo','El streaming también puede ser bajo demanda.'),('Se elimina cualquier almacenamiento temporal del cliente','El cliente utiliza un búfer para sostener la reproducción.')],
  'En streaming la recepción y el consumo se solapan. No hay que esperar al archivo completo, aunque suele existir una espera inicial de almacenamiento en búfer.')
q('t21','Servicios live y VOD','21–27',
  'Un usuario elige una película del catálogo y decide cuándo empezar y a qué punto saltar. ¿Qué tipo de servicio describe?',
  'Vídeo bajo demanda (VOD)', [('Emisión live sin retroceso','En ese modelo el usuario sigue la señal que se emite, no elige libremente el punto.'),('Difusión broadcast de una programación fija','Broadcast describe distribución y no garantiza la elección individual indicada.'),('Multicast de un único evento en el mismo instante','Un flujo simultáneo compartido no describe los puntos de reproducción individuales.')],
  'VOD permite solicitar contenidos en el momento elegido y controlar la reproducción. La forma de distribución y el modelo de pago son dimensiones diferentes.', 'Aplicación')
q('t21','Distribución multicast','25',
  '¿Qué modalidad de transmisión envía un flujo destinado a un grupo específico de receptores?',
  'Multicast', [('Unicast','Unicast establece un flujo por destinatario.'),('Broadcast','Broadcast difunde sin seleccionar ese grupo específico.'),('Descarga local sin red','No es una modalidad de transmisión a un grupo por la red.')],
  'Multicast dirige el flujo a un grupo de receptores. Unicast sirve individualmente y broadcast difunde a los receptores del ámbito de difusión.')
q('t21','OTT','27–28',
  '¿Qué describe la entrega de contenido OTT?',
  'Contenido por Internet sin exigir un servicio tradicional de TV de pago', [('Contenido limitado al decodificador de televisión por cable','OTT utiliza Internet y puede recibirse en distintos tipos de dispositivo.'),('Contenido que se financia necesariamente con publicidad','OTT no determina la financiación: puede haber AVOD, SVOD o TVOD.'),('Contenido que solo puede verse en emisión simultánea','OTT puede ofrecer contenido bajo demanda además de directos.')],
  'OTT describe la vía de entrega a través de Internet. No equivale a un modelo concreto de ingresos ni a un único dispositivo de reproducción.')
q('t21','AVOD','29',
  'Una plataforma permite ver vídeos gratis e inserta anuncios para financiarlos. ¿Qué modelo representa?',
  'AVOD', [('SVOD','SVOD se basa en una suscripción de acceso al servicio.'),('TVOD','TVOD se basa en pagar por contenido o evento seleccionado.'),('PPV','PPV implica pagar por una visualización o evento, no acceso gratuito financiado con anuncios.')],
  'AVOD significa Advertising Video on Demand: el ingreso principal del modelo descrito procede de la publicidad.')
q('t21','SVOD','30',
  'Un servicio cobra una cuota periódica que da acceso a un catálogo. ¿Qué modelo de vídeo bajo demanda utiliza?',
  'SVOD', [('AVOD','En el modelo AVOD descrito el acceso se financia con anuncios, no con la cuota.'),('TVOD','En TVOD se paga una transacción por un contenido concreto.'),('PPV por evento','El pago por evento no describe acceso recurrente a un catálogo.')],
  'SVOD es Subscription Video on Demand. El criterio aquí es la suscripción periódica, aunque en el mercado existan modelos combinados.')
q('t21','TVOD','31',
  'Un usuario paga una cantidad para alquilar una película concreta, sin contratar una cuota de catálogo. ¿Qué modelo utiliza?',
  'TVOD', [('SVOD','La suscripción da acceso periódico al catálogo, no describe este alquiler individual.'),('AVOD','El contenido aquí se paga directamente y no se ofrece gratis por anuncios.'),('Modelo híbrido de cuota y publicidad','No hay cuota de catálogo ni anuncios en las condiciones del caso.')],
  'TVOD es el modelo transaccional: se paga por la pieza o evento elegido. El alquiler digital es un ejemplo.', 'Aplicación')
q('t21','RTP','42–43',
  '¿Qué protocolo transporta audio y vídeo en tiempo real con números de secuencia y marcas temporales?',
  'RTP', [('RTCP','RTCP informa sobre recepción y calidad, pero no transporta el flujo audiovisual principal.'),('RTSP','RTSP controla la sesión y sus órdenes de reproducción.'),('HTTP como protocolo de control de sesiones RTSP','HTTP puede distribuir segmentos, pero no es el protocolo identificado por esa función de RTP.')],
  'RTP lleva el contenido en tiempo real y aporta secuencias y tiempos para su reproducción. No garantiza por sí mismo recuperar todas las pérdidas.')
q('t21','RTCP','43–44',
  'Una aplicación necesita informes de pérdidas y variación del retardo de un flujo RTP. ¿Qué protocolo aporta esa supervisión?',
  'RTCP', [('RTSP','RTSP sirve para gestionar la sesión, no es el protocolo de informes de recepción de RTP.'),('RTMP','RTMP se asocia en el tema al envío del directo al servidor.'),('HLS','HLS distribuye segmentos HTTP y no es el protocolo de supervisión complementario a RTP.')],
  'RTCP comunica estadísticas de recepción y calidad para ayudar a controlar la transmisión. Complementa a RTP.', 'Aplicación')
q('t21','RTSP','46–47',
  '¿Qué protocolo corresponde a órdenes de sesión como SETUP, PLAY y PAUSE?',
  'RTSP', [('RTP','RTP transporta datos multimedia; no es el protocolo de esas órdenes.'),('RTCP','RTCP supervisa calidad y recepción; no ejecuta esas órdenes de sesión.'),('MPEG-DASH','DASH describe streaming adaptativo HTTP, no ese control de sesión.')],
  'RTSP gestiona la sesión como un mando de reproducción. El audio y el vídeo pueden viajar por RTP en otro canal.')
q('t21','RTMP','45',
  'Un codificador envía una señal en directo a la plataforma antes de que esta la distribuya a espectadores. ¿Qué protocolo asocia el tema a esa ingestión?',
  'RTMP', [('RTCP','RTCP informa de la calidad de un flujo RTP, no es la ingestión descrita.'),('RTSP como informe de pérdidas','RTSP controla sesiones y tampoco se define por informar de pérdidas.'),('M3U8 como protocolo de subida','M3U8 es un formato de lista de reproducción usado por HLS, no ese protocolo de ingestión.')],
  'RTMP se usa para transportar la señal desde el codificador al servidor. El formato de entrega al espectador puede ser otro, como HLS o DASH.')
q('t21','HLS y DASH','48–49',
  '¿Qué pareja de tecnología y manifiesto está correctamente asociada?',
  'HLS con M3U8 y MPEG-DASH con MPD', [('HLS con MPD y MPEG-DASH con M3U8','Intercambia los manifiestos de ambas tecnologías.'),('RTP con M3U8 y RTCP con MPD','Los manifiestos corresponden a streaming HTTP, no a esos protocolos RTP/RTCP.'),('RTSP con MPD y RTMP con M3U8','Asigna a RTSP y RTMP los manifiestos de DASH y HLS.')],
  'HLS emplea listas M3U8 y DASH usa Media Presentation Description (MPD). Ambos pueden describir segmentos y calidades disponibles.')
q('t21','Streaming adaptativo','39, 48–49',
  'La conexión de un espectador pierde capacidad durante la reproducción. ¿Qué puede hacer un cliente de streaming adaptativo?',
  'Solicitar segmentos de una representación de menor bitrate', [('Mantener siempre la máxima calidad aunque se vacíe el búfer','Ignora la adaptación y aumenta el riesgo de cortes.'),('Cambiar el modelo de pago de SVOD a AVOD','La financiación no ajusta la tasa de los segmentos.'),('Reproducir el manifiesto como si fuese un segmento de vídeo','El manifiesto describe recursos; no contiene por sí mismo el vídeo a reproducir.')],
  'El cliente puede elegir una representación con menor tasa para ajustarse a la red y sostener la reproducción. La decisión combina estimaciones de capacidad y estado del búfer.', 'Aplicación')
q('t21','Jitter','53',
  'Los paquetes llegan con intervalos variables aunque se enviaran regularmente. ¿Qué fenómeno describe esa variación?',
  'Jitter', [('Latencia constante','Una latencia fija desplaza todos los paquetes por igual, sin variar los intervalos.'),('Bitrate del códec','El bitrate mide cantidad de datos por unidad de tiempo, no la variación de retardo.'),('Profundidad de color','La profundidad de color describe la representación de píxeles, no la llegada de paquetes.')],
  'Jitter es la variación del retardo o de los instantes de llegada. Un búfer de reproducción puede absorber parte de esa irregularidad.')
q('t21','Compromiso del búfer','52–53',
  'Si se aumenta la reserva de reproducción antes de empezar, ¿qué compromiso se espera, en igualdad de las demás condiciones?',
  'Más tolerancia a retrasos y mayor espera inicial', [('Más tolerancia a retrasos y menor espera inicial','Crear una reserva mayor requiere esperar más datos, no menos.'),('Menos tolerancia a retrasos y mayor capacidad de la red','El búfer no aumenta la capacidad física de la red.'),('La misma espera inicial y eliminación de todas las pérdidas','El búfer no garantiza recuperar paquetes perdidos ni una espera invariable.')],
  'El búfer cambia latencia por estabilidad: reserva más datos para amortiguar retrasos, a costa de mayor retardo de arranque. Una reserva finita no resuelve una conexión insuficiente de manera indefinida.', 'Aplicación')
q('t21','Agotamiento del búfer','52',
  'El cliente consume todos los datos almacenados y todavía no ha recibido los siguientes. ¿Qué sucede normalmente?',
  'La reproducción se detiene hasta recuperar una reserva suficiente', [('El reproductor inventa los segmentos que faltan en el servidor','El almacenamiento temporal no crea el contenido que falta.'),('La reproducción continúa indefinidamente con calidad original','No se puede seguir mostrando contenido nuevo sin recibir sus datos.'),('La sesión cambia obligatoriamente al protocolo RTCP','RTCP supervisa; no sustituye el contenido que falta.')],
  'Cuando el búfer queda vacío aparece un corte o rebuffering. Para continuar, el cliente necesita recibir más datos y puede reducir la calidad si el servicio permite adaptación.', 'Aplicación')
q('t21','Streaming P2P','54–55',
  '¿Qué distingue al streaming P2P del esquema cliente-servidor descrito en el tema?',
  'Los espectadores también pueden reenviar fragmentos a otros peers', [('Cada espectador recibe todo el vídeo únicamente del tracker','El tracker coordina peers; no tiene que servir todo el vídeo.'),('El seed solo controla el pago y nunca aporta fragmentos','El seed posee contenido y puede iniciar su distribución.'),('Cada cliente necesita haber descargado todo antes de compartir','En el esquema descrito se intercambian fragmentos durante la reproducción.')],
  'Los peers descargan y comparten chunks. El tracker coordina y el seed aporta contenido inicial. Esto reduce carga del origen, aunque añade dependencia de los peers.')
q('t21','Netflix y OCA','57–59, 64',
  '¿Qué es un OCA en Netflix Open Connect?',
  'Un servidor que almacena y entrega contenido audiovisual al cliente', [('Un servicio dedicado a facturar las suscripciones','La facturación pertenece a la lógica del backend, no a la misión del OCA.'),('Un reproductor instalado en el teléfono del espectador','El OCA es infraestructura de entrega, no el cliente de reproducción.'),('Un códec que convierte cada vídeo en paquetes RTP','OCA significa Open Connect Appliance; no es un algoritmo de compresión.')],
  'Los Open Connect Appliances son servidores de caché y entrega situados cerca de los usuarios, por ejemplo dentro de ISP o en puntos de intercambio. El cliente recibe de ellos los bytes del vídeo.', url='https://openconnect.netflix.com/en/')

# T2.2: cálculos RAID y propiedades de formatos y arquitecturas.
q('t22','RAID 0','5',
  '¿Qué ocurre si falla un disco de un RAID 0 sin otra copia de los datos?',
  'El conjunto pierde la disponibilidad íntegra de sus datos', [('La paridad distribuida reconstruye el contenido','RAID 0 no mantiene paridad.'),('El espejo conserva una copia completa','RAID 0 no crea espejos; eso caracteriza a RAID 1.'),('El conjunto soporta hasta dos fallos simultáneos','Esa tolerancia corresponde a RAID 6, no a RAID 0.')],
  'RAID 0 reparte datos entre discos para aumentar capacidad y rendimiento, pero no aporta redundancia. El fallo de uno compromete los datos del conjunto.')
q('t22','RAID 1','6',
  'Se configura un espejo RAID 1 con dos discos de 2 TB. Sin contar metadatos, ¿qué capacidad útil ofrece?',
  '2 TB', [('4 TB','Suma la capacidad física sin descontar que el segundo disco duplica los datos.'),('1 TB','Divide otra vez la capacidad de un disco, aunque cada disco ya contiene la copia completa.'),('3 TB','Descuenta media unidad sin una regla de capacidad propia de un espejo.')],
  'Cada disco contiene la misma información. Un espejo de dos unidades iguales ofrece la capacidad de una: 2 TB.', 'Cálculo')
q('t22','Capacidad RAID 5','7–9',
  'Un RAID 5 usa cinco discos de 2 TB. Suponiendo discos iguales y sin metadatos, ¿cuánta capacidad útil tiene?',
  '8 TB', [('10 TB','Cuenta todos los discos como datos y omite la capacidad equivalente destinada a paridad.'),('6 TB','Resta dos discos equivalentes, como en RAID 6.'),('2 TB','Calcula como si todos los discos fueran copias de un único espejo.')],
  'RAID 5 utiliza el equivalente de un disco para paridad distribuida. La capacidad es (5 − 1) × 2 TB = 8 TB.', 'Cálculo')
q('t22','Paridad distribuida','7–9',
  'En RAID 5, ¿cómo se coloca la paridad entre las distintas franjas?',
  'Va rotando entre los discos del conjunto', [('Se guarda siempre en un único disco dedicado','La paridad fija caracteriza a otros esquemas, como RAID 4, no a RAID 5.'),('Se duplica cada bloque completo en todos los discos','Eso describe un espejo, no paridad distribuida.'),('Se calcula sin guardar información redundante','RAID 5 almacena paridad para poder reconstruir un fallo.')],
  'La paridad es distribuida: su disco cambia de una franja a otra. Dentro de una franja, un bloque de paridad permite reconstruir un bloque de datos ausente.')
q('t22','Cálculo de paridad XOR','9, 13',
  'Una franja RAID 5 tiene D0 = 1011, D1 = 0101 y D2 = 1100. Si P = D0 ⊕ D1 ⊕ D2, ¿cuál es P?',
  '0010', [('1110','Es el XOR de D0 y D1, pero falta combinar D2.'),('1111','Se obtiene al usar OR en lugar de XOR con esos bloques.'),('1100','Repite D2 sin combinar los otros bloques de datos.')],
  '1011 ⊕ 0101 = 1110; después 1110 ⊕ 1100 = 0010. XOR produce 1 cuando los bits comparados son diferentes.', 'Cálculo')
q('t22','Reconstrucción RAID 5','9, 13',
  'Falta D1 en una franja con D0 = 1011, D2 = 1100 y P = 0010. ¿Qué bloque se recupera mediante P ⊕ D0 ⊕ D2?',
  '0101', [('1001','Es el resultado parcial P ⊕ D0; falta aplicar XOR con D2.'),('0111','Combina D0 y D2 pero omite la paridad P.'),('0000','Sería cancelar cada bloque con una copia idéntica, que no es la operación pedida.')],
  '0010 ⊕ 1011 = 1001 y 1001 ⊕ 1100 = 0101. El XOR permite despejar el único bloque ausente.', 'Cálculo')
q('t22','Actualización de paridad','10–13',
  'En una escritura parcial RAID 5, P = 0010 y el dato D2 cambia de 1100 a 1000. ¿Qué nueva paridad resulta de P′ = P ⊕ D2viejo ⊕ D2nuevo?',
  '0110', [('0010','Mantiene la paridad anterior pese a haber cambiado el dato.'),('0100','Es el XOR entre dato viejo y nuevo, pero falta combinar la paridad anterior.'),('1010','Combina P con el nuevo dato y omite retirar el efecto del dato viejo.')],
  '0010 ⊕ 1100 = 1110; 1110 ⊕ 1000 = 0110. Hay que quitar la contribución antigua y añadir la nueva mediante XOR.', 'Cálculo')
q('t22','Read-Modify-Write','10–11',
  'Se actualiza un bloque de datos RAID 5 con Read-Modify-Write, sin caché previa. ¿Qué accesos lógicos a disco describe el tema?',
  'Dos lecturas y dos escrituras', [('Una lectura y una escritura','Falta leer y escribir la paridad, además del dato.'),('Tres lecturas y una escritura','En el caso indicado se actualizan tanto el dato como la paridad.'),('Cero lecturas y dos escrituras','Sin caché se necesitan el dato viejo y la paridad vieja.')],
  'Se leen el dato antiguo y la paridad antigua, se calcula la nueva paridad y se escriben dato y paridad nuevos: cuatro accesos lógicos.', 'Aplicación')
q('t22','Full-stripe write','10',
  'Se escriben completos los tres bloques de datos nuevos de una franja RAID 5 de cuatro discos. Sin caché ni otras operaciones, ¿qué permite el full-stripe write?',
  'Calcular la paridad nueva sin leer los datos antiguos de esa franja', [('Evitar escribir el bloque de paridad','Aunque no se lean los datos viejos, hay que guardar la paridad nueva.'),('Leer siempre el dato antiguo y la paridad por cada bloque nuevo','Eso aplica el coste de pequeñas escrituras parciales al caso de franja completa.'),('Convertir los cuatro discos en copias idénticas','Un full-stripe write no transforma RAID 5 en un espejo.')],
  'Al disponer de todos los datos nuevos, la controladora calcula su XOR directamente. En el ejemplo se escriben tres bloques de datos y uno de paridad.', 'Aplicación')
q('t22','Tolerancia a fallos','8, 14–15',
  '¿Qué diferencia de tolerancia a fallos distingue RAID 6 de RAID 5?',
  'RAID 6 soporta dos discos fallidos y RAID 5 uno', [('RAID 6 soporta uno y RAID 5 dos','Invierte la tolerancia que proporciona la doble paridad.'),('Ambos soportan dos discos fallidos por usar XOR','Una sola paridad de RAID 5 no permite resolver dos bloques perdidos de una franja.'),('Ninguno soporta fallos porque no utiliza espejos','La paridad también proporciona tolerancia a fallos; no se limita a los espejos.')],
  'RAID 5 utiliza una redundancia de paridad; RAID 6 añade una segunda. Por eso RAID 6 permite reconstruir ante dos discos fallidos.')
q('t22','RAID y copias de seguridad','19',
  'Se borra por error un archivo en un volumen RAID 1 y el borrado se refleja en ambos discos. ¿Qué medida habría permitido recuperar una versión anterior?',
  'Una copia de seguridad anterior al borrado', [('Añadir otro espejo que reproduzca el mismo borrado','Otra copia sincronizada del volumen reproduce también el borrado.'),('Cambiar a RAID 0 para repartir el archivo','RAID 0 no mantiene versiones ni aporta recuperación de borrados.'),('Recalcular la paridad sobre el volumen ya modificado','La paridad protege frente a determinados fallos físicos, no conserva por sí misma el archivo anterior.')],
  'La redundancia RAID mejora disponibilidad ante fallos de discos, pero no sustituye copias con versiones anteriores. Un borrado válido puede propagarse a la información redundante.', 'Aplicación')
q('t22','UTF-8','23, 25',
  '¿Qué propiedad describe correctamente UTF-8?',
  'Usa entre uno y cuatro bytes y mantiene la codificación de ASCII', [('Usa cuatro bytes para todos los caracteres','El tamaño fijo de cuatro bytes corresponde a UTF-32.'),('Usa dos bytes para todo Unicode sin excepciones','UTF-8 es variable; incluso UTF-16 necesita pares para caracteres complementarios.'),('Representa solo los 128 caracteres del repertorio ASCII','UTF-8 representa Unicode, no únicamente ASCII.')],
  'UTF-8 utiliza un byte para ASCII y secuencias más largas para otros caracteres Unicode, hasta cuatro bytes. «UTFS» en las indicaciones se interpreta aquí como UTF-8, presente en la página 23.')
q('t22','Tamaño de imagen','30',
  'Una imagen de 512 × 512 píxeles usa 24 bits por píxel, sin compresión ni cabeceras. ¿Qué tamaño ocupa, tomando 1 MiB = 2²⁰ bytes?',
  '0,75 MiB', [('0,25 MiB','Equivale a contar un byte por píxel en lugar de tres.'),('6 MiB','Es el número de mebibits; falta dividir entre ocho para pasarlo a bytes.'),('2,25 MiB','Aplica de nuevo el factor de tres después de haberlo incluido.')],
  '512 × 512 × 24 / 8 = 786 432 bytes. Al dividir entre 1 048 576 bytes/MiB se obtiene 0,75 MiB.', 'Cálculo')
q('t22','Compresión sin pérdida','32',
  'Un archivo debe recuperar exactamente todos sus datos originales después de descomprimirlo. ¿Qué clase de compresión se requiere?',
  'Sin pérdida (lossless)', [('Con pérdida (lossy)','Lossy descarta información y no garantiza la reconstrucción exacta.'),('Con pérdida y calidad visual alta','Que la diferencia no se aprecie no implica igualdad exacta de datos.'),('Con pérdida seguida de ampliación de resolución','Ampliar la resolución no recupera la información descartada.')],
  'La propiedad definitoria de lossless es reconstruir exactamente la información original. La fidelidad perceptiva de un algoritmo lossy es una cuestión distinta.')
q('t22','Formatos de imagen','34–36',
  '¿Qué pareja se corresponde con los modos de compresión descritos en el tema?',
  'PNG sin pérdida y JPEG convencional con pérdida', [('PNG con pérdida y JPEG convencional sin pérdida','Invierte los modos habituales descritos para ambos formatos.'),('GIF con pérdida y PNG con pérdida','La compresión GIF mediante LZW y la de PNG son sin pérdida; limitar la paleta es otra operación.'),('JPEG convencional sin pérdida y WebP solo con pérdida','JPEG convencional es lossy y WebP admite modos lossy y lossless.')],
  'El tema presenta PNG como lossless y JPEG convencional como lossy. JPEG 2000 y WebP permiten otros modos; por eso el enunciado acota el JPEG convencional.')
q('t22','Localidad temporal','45',
  'Un algoritmo vuelve a leer la misma posición de memoria varias veces en un intervalo corto. ¿Qué propiedad manifiesta?',
  'Localidad temporal', [('Localidad espacial','La espacial se refiere a posiciones próximas, no a repetir la misma.'),('Acceso secuencial sin reutilización','La repetición del mismo dato no es un recorrido sin reutilización.'),('Ausencia de localidad de memoria','La reutilización cercana en el tiempo es precisamente una forma de localidad.')],
  'Hay localidad temporal cuando una posición referenciada tiene probabilidad de usarse de nuevo pronto. La caché puede aprovechar esa reutilización.')
q('t22','Localidad en MMA','45–46',
  'Un filtro procesa píxeles consecutivos de cada fotograma y después pasa al siguiente sin volver a esos datos. ¿Qué patrón encaja con las MMA del tema?',
  'Alta localidad espacial y baja localidad temporal de los datos', [('Alta localidad temporal y baja localidad espacial','Invierte el patrón: se visitan vecinos y apenas se reutilizan los datos.'),('Alta localidad temporal y alta reutilización del mismo píxel','El enunciado especifica que los datos no se vuelven a usar.'),('Baja localidad espacial por acceder a píxeles vecinos','Acceder a posiciones contiguas favorece la localidad espacial.')],
  'El acceso a píxeles vecinos aporta localidad espacial. Recorrer el flujo sin regresar a los datos reduce la localidad temporal, aunque el código del bucle sí pueda reutilizarse.', 'Aplicación')
q('t22','Arquitecturas dedicadas y reconfigurables','61–63',
  'Se necesita modificar el circuito de procesamiento después de fabricar el dispositivo. ¿Qué opción lo permite según la clasificación del tema?',
  'Una FPGA reconfigurable', [('Un ASIC de circuito fijo','El ASIC dedicado no cambia su circuito tras fabricarse.'),('Un ASIC monolítico con más frecuencia de reloj','Cambiar la frecuencia no modifica el circuito fijo del ASIC.'),('Un ASIC modular con más chips de la misma tarea','Añadir chips fijos no proporciona la reconfiguración lógica solicitada.')],
  'La FPGA ofrece bloques lógicos e interconexiones programables. El ASIC dedica su circuito a una tarea y prioriza eficiencia frente a flexibilidad.', 'Aplicación')
q('t22','DSP y MAC','52–53, 57',
  '¿Qué operación básica acelerada por hardware destaca en un DSP para filtros y procesamiento repetitivo?',
  'Multiplicación y acumulación (MAC)', [('Compresión y cifrado como una única operación MAC','MAC aquí significa multiply-accumulate, no compresión y cifrado.'),('Búsqueda y salto entre archivos del sistema','No es la operación aritmética característica que destaca el tema.'),('Conversión entre UTF-8 y UTF-32','La conversión de caracteres no define la unidad MAC de un DSP.')],
  'La operación MAC multiplica operandos y acumula el resultado. Es muy frecuente en filtros digitales y otros algoritmos numéricos de señal.')
q('t22','Propósito general y especialización','47, 59–63',
  'Una videollamada ejecuta lógica de la app, un efecto de IA y codificación de vídeo. ¿Qué reparto se ajusta a la especialización descrita?',
  'CPU para lógica, NPU para IA y motor de vídeo para codificar', [('NPU para toda la lógica y CPU exclusivamente para píxeles','Invierte las especializaciones y obliga a la NPU a tareas generales.'),('Motor de vídeo para reglas de negocio y CPU solo para IA','El motor de vídeo no es el bloque general de reglas de negocio.'),('FPGA obligatoria para cualquier lógica de aplicación móvil','Una FPGA no es un requisito para ejecutar la app en un SoC.')],
  'Un SoC puede combinar bloques y asignar tareas a los más adecuados: CPU general, NPU para redes neuronales y motor multimedia para códecs. Esto reduce trabajo y consumo en los bloques generales.', 'Aplicación')

# T3.1: wearables, textiles, pantallas y conectividad sin tasas WiFi.
q('t31','Wearables','23–26',
  '¿Qué rasgo define a un wearable en el contexto del tema?',
  'Se lleva puesto en el cuerpo y registra, procesa o transmite información', [('Se transporta en una bolsa y requiere una mesa para utilizarse','La portabilidad no implica que el dispositivo sea vestible.'),('Se instala como equipo fijo para dar cobertura a una habitación','Eso describe infraestructura fija, no un dispositivo que se lleva puesto.'),('Se identifica únicamente por tener una pantalla de gran tamaño','La pantalla grande no define a un wearable y muchos ni siquiera tienen pantalla.')],
  'La tecnología vestible se integra en objetos o prendas que se llevan sobre el cuerpo. Puede incluir sensores, procesamiento y comunicación con otros equipos.')
q('t31','Taxonomía de wearables','36–37',
  'Una etiqueta NFC sin batería integrada en una pulsera obtiene energía del lector. Según el criterio activo/pasivo del tema, ¿cómo se clasifica?',
  'Pasiva', [('Activa por responder al lector','Responder no implica disponer de alimentación propia; la etiqueta obtiene la energía del lector.'),('Invasiva por estar en una pulsera','Llevarla en la muñeca no la convierte en un implante o dispositivo invasivo.'),('Monofuncional como alternativa a activa o pasiva','La funcionalidad es otro criterio; no responde a la clasificación energética solicitada.')],
  'El ejemplo de wearable pasivo del tema es una etiqueta NFC sin batería. Activo/pasivo, invasivo/no invasivo y funcionalidad son ejes distintos.', 'Aplicación')
q('t31','Pantallas en wearables','26, 67, 71',
  'Un wearable muestra texto casi estático y prioriza lectura por reflexión de luz ambiental y mínimo consumo al mantener la imagen. No necesita vídeo fluido. ¿Qué tecnología encaja mejor?',
  'Tinta electrónica', [('LCD IPS','Modula una retroiluminación: no es la lectura reflectante de bajo consumo solicitada.'),('OLED','Sus píxeles deben emitir luz mientras muestran la imagen; no usa el principio reflectante pedido.'),('MicroLED','Es una tecnología emisiva, no el display reflectante para imagen estática descrito.')],
  'La tinta electrónica forma imágenes reflectantes aprovechando la luz ambiental y resulta adecuada para información poco cambiante. OLED encaja mejor cuando se buscan color y respuesta rápida.', 'Aplicación')
q('t31','Textillography','42–44',
  '¿Qué objetivo caracteriza a Textillography en el material de la asignatura?',
  'Automatizar las interconexiones electrónicas al fabricar la tela', [('Colocar módulos en un bolsillo sin conectarlos al tejido','Eso es electrónica añadida, no automatización de interconexiones en la fabricación.'),('Sustituir los sensores textiles por una pantalla externa','El objetivo no consiste en eliminar la red de sensores de la prenda.'),('Confeccionar primero la tela y realizar todas las uniones a mano','Ese procedimiento es precisamente el que pretende automatizar.')],
  'Textillography integra las conexiones durante la producción del tejido. El meta-wearable distribuye sensores y procesamiento por la prenda.')
q('t31','Materiales de e-textiles','45–48',
  'Un hilo conductor de una camiseta inteligente pierde continuidad tras varios lavados. ¿Qué requisito de diseño está incumpliendo?',
  'Mantener su conductividad durante el uso y los lavados', [('Incrementar su resistencia eléctrica hasta interrumpir la señal','Interrumpir la señal no es el requisito; es el fallo que se desea evitar.'),('Sustituir el tejido flexible por una batería rígida','No resuelve la degradación de la interconexión conductora.'),('Aumentar la resolución del panel de visualización','La resolución del panel no determina la durabilidad del hilo.')],
  'Los conductores textiles deben combinar propiedades eléctricas y textiles con durabilidad. Una prenda se dobla, se usa y se lava: la conexión debe sobrevivir a esas condiciones.', 'Aplicación')
q('t31','Pantallas SAW','55–56',
  'Una pantalla detecta el toque porque el dedo absorbe parte de unas ondas de ultrasonido sobre su superficie. ¿Qué tecnología es?',
  'SAW', [('Infrarroja','La infrarroja detecta interrupciones de haces luminosos, no absorción de ultrasonidos.'),('Resistiva','La resistiva localiza el contacto entre capas conductoras al presionarlas.'),('Capacitiva proyectada','La capacitiva detecta cambios de capacitancia, no ondas acústicas.')],
  'SAW utiliza ondas acústicas superficiales. El dedo modifica su propagación y el controlador localiza el toque.')
q('t31','Pantallas ópticas e infrarrojas','55, 57–58',
  'Una pantalla usa cámaras en las esquinas para triangular la sombra producida por un dedo. ¿Qué tecnología describe?',
  'Imagen óptica', [('Matriz de infrarrojos sin cámaras','La matriz detecta qué haces se interrumpen; aquí la localización se obtiene con cámaras.'),('Capacitiva de superficie','La capacitiva de superficie mide una alteración eléctrica, no una sombra.'),('Resistiva de dos capas','La resistiva detecta contacto entre capas al ejercer presión.')],
  'La imagen óptica usa sensores o cámaras para localizar la sombra del contacto. Se diferencia del marco infrarrojo que localiza el cruce de haces interrumpidos.')
q('t31','Pantallas resistivas','59–60',
  '¿Qué mecanismo permite usar una pantalla resistiva con un guante o un lápiz no conductor?',
  'La presión pone en contacto dos capas conductoras', [('El guante aporta obligatoriamente la capacitancia del dedo','No necesita la conductividad del objeto como una capacitiva convencional.'),('El lápiz debe emitir ultrasonidos hacia el cristal','El objeto no necesita emitir señales para presionar una pantalla resistiva.'),('La pantalla reconoce el objeto mediante una cámara de color','El mecanismo descrito es eléctrico por presión, no reconocimiento visual.')],
  'La resistiva responde al contacto físico entre sus capas. Por ello puede activarse con diversos objetos que ejerzan suficiente presión.')
q('t31','Capacitiva proyectada','61–63',
  '¿Qué característica distingue a la capacitiva proyectada (PCAP) descrita frente a la capacitiva de superficie?',
  'Detección multitáctil mediante una rejilla de electrodos', [('Dos capas que deben tocarse al ejercer presión','Ese mecanismo corresponde a una pantalla resistiva.'),('Una red de haces ópticos que el dedo interrumpe','Ese mecanismo corresponde a una pantalla infrarroja.'),('Ondas acústicas que se absorben en el cristal','Ese mecanismo corresponde a SAW.')],
  'PCAP mide capacitancia en una rejilla de filas y columnas bajo el cristal. Esa distribución permite localizar múltiples contactos.')
q('t31','LCD e IPS','67–68',
  '¿Qué describe correctamente un display LCD IPS?',
  'Cristal líquido con retroiluminación y buenos ángulos de visión', [('Diodos orgánicos que emiten luz propia en cada píxel','Eso describe OLED, no LCD.'),('Partículas que reflejan luz y mantienen texto con refresco lento','Eso describe tinta electrónica, no IPS.'),('Una matriz de LED microscópicos autoemisivos por píxel','Eso describe MicroLED, no un panel LCD IPS.')],
  'LCD modula la luz de una retroiluminación mediante cristal líquido. IPS es una variante LCD que destaca por ángulos de visión y reproducción del color.')
q('t31','OLED y AMOLED','71–72',
  '¿Por qué una pantalla OLED puede mostrar un negro más profundo que un LCD retroiluminado?',
  'Puede apagar los píxeles negros sin una retroiluminación común', [('Bloquea una retroiluminación que siempre ilumina el negro','Ese es el principio del LCD, con posibles fugas de luz.'),('Reduce todos los colores a una paleta fija de 256 tonos','La limitación de paleta no explica los píxeles autoemisivos ni el negro.'),('Refleja exclusivamente la luz ambiental como la tinta electrónica','OLED emite luz propia; no es una tecnología reflectante.')],
  'En OLED los píxeles emiten luz y pueden apagarse al representar negro. AMOLED añade una matriz activa de transistores para su control.')
q('t31','Retina','69–70',
  '¿Qué significa Retina en el contexto de los displays del tema?',
  'Una denominación de Apple asociada a alta densidad de píxeles', [('Un tipo de cristal líquido incompatible con OLED','Retina puede aplicarse tanto a pantallas LCD como OLED.'),('Una rejilla capacitiva que mide los puntos de toque','Eso pertenece al sistema táctil, no a la denominación de densidad.'),('Un sistema de iluminación con LED de tamaño microscópico','Esa descripción se relaciona con tecnologías de iluminación o MicroLED.')],
  'Retina es una marca comercial, no un mecanismo físico de display. La densidad y la distancia de observación determinan si se distinguen los píxeles.')
q('t31','Bluetooth frente a IrDA','76–77',
  '¿Qué diferencia explica que Bluetooth pueda comunicar equipos sin alinearlos ópticamente, a diferencia de un enlace infrarrojo?',
  'Utiliza radiofrecuencia en la banda ISM de 2,4 GHz', [('Utiliza luz infrarroja de mayor brillo','Bluetooth no es un enlace óptico infrarrojo.'),('Necesita unir los equipos mediante una antena cableada','La comunicación entre dispositivos es inalámbrica.'),('Usa el campo cercano de 13,56 MHz de NFC','Esa frecuencia y mecanismo corresponden a NFC.')],
  'Bluetooth usa radio en 2,4 GHz y no exige alinear emisor y receptor como un enlace óptico. El alcance y la propagación siguen dependiendo del entorno.', url='https://www.bluetooth.com/learn-about-bluetooth/tech-overview/')
q('t31','ANT y ANT+','83–85',
  'Dos sensores transmiten mediante ANT, pero el receptor interpreta sus datos de forma distinta. ¿Qué añade ANT+ para resolver esa interoperabilidad?',
  'Perfiles que definen cómo interpretar los datos', [('Más potencia de emisión para reducir los errores de bits','La cuestión es interpretar datos ya recibidos, no mejorar la cobertura del enlace.'),('Un códec común para comprimir cualquier medida biométrica','Los perfiles definen significado y formato; no se reducen a un compresor universal.'),('Un emparejamiento que asigna direcciones IP a los sensores','ANT+ no resuelve la interpretación asignando direcciones de una red IP.')],
  'ANT ofrece la comunicación de bajo consumo; ANT+ añade perfiles como el de frecuencia cardíaca para que dispositivos compatibles entiendan los mismos datos.', 'Aplicación', url='https://developer.garmin.com/ant-program/ant-ant-plus/')
q('t31','Zigbee','86',
  'Una red de domótica necesita enviar pequeñas medidas de sensores durante mucho tiempo con batería. ¿Qué tecnología del tema está orientada a ese caso?',
  'Zigbee sobre IEEE 802.15.4', [('WiFi elegido por una tasa máxima de transferencia elevada','La prioridad son pequeños mensajes y autonomía, no el mayor caudal.'),('NFC usado como red permanente entre habitaciones','NFC está pensado para interacciones a centímetros, no para esa cobertura.'),('IrDA con emisores que deben mantenerse alineados','La dependencia de un trayecto óptico dificulta esa red de sensores distribuida.')],
  'Zigbee se orienta a comunicaciones de baja tasa y bajo consumo, habituales en domótica. Está basado en IEEE 802.15.4.', 'Aplicación')
q('t31','WiFi y bandas','89–91',
  'Se compara WiFi 1 (802.11b) en 2,4 GHz con un enlace WiFi 7 en 6 GHz, con potencia, antenas y entorno comparables. ¿Qué banda tiende a ofrecer mayor alcance y penetración en interiores?',
  '2,4 GHz, por su menor frecuencia', [('6 GHz, porque una generación más reciente garantiza más alcance','La generación no elimina la mayor atenuación asociada a frecuencias altas.'),('Las dos siempre ofrecen exactamente el mismo alcance','La banda y la propagación influyen incluso si el resto de condiciones es comparable.'),('No influye la frecuencia, únicamente el nombre comercial','La frecuencia es uno de los factores relevantes en la propagación.')],
  'En condiciones comparables, 2,4 GHz tiende a llegar más lejos y atravesar obstáculos mejor. WiFi 7 también puede usar 2,4 GHz: no es correcto concluir que WiFi 1 siempre llega más lejos que WiFi 7.', 'Aplicación')
q('t31','Generaciones WiFi','90–91',
  '¿Qué asociación entre estándar y generación WiFi coincide con el temario?',
  '802.11ax con WiFi 6 y 802.11be con WiFi 7', [('802.11ax con WiFi 7 y 802.11be con WiFi 6','Intercambia las dos generaciones.'),('802.11ac con WiFi 6 y 802.11ax con WiFi 5','802.11ac corresponde a WiFi 5; 802.11ax a WiFi 6.'),('802.11b con WiFi 7 y 802.11be con WiFi 1','Invierte un estándar inicial y uno de los más recientes del material.')],
  'El tema asocia 802.11ax con WiFi 6 y 802.11be con WiFi 7. La pregunta identifica generaciones y evita memorizar sus anchos de banda.')
q('t31','RFID y frecuencias','95, 104–105',
  '¿Qué afirmación distingue correctamente la frecuencia de NFC de las familias de RFID?',
  'NFC usa 13,56 MHz; RFID incluye bandas como LF, HF y UHF', [('NFC usa 2,4 GHz y RFID solo 13,56 MHz','Confunde NFC con otras tecnologías y limita indebidamente RFID a una frecuencia.'),('NFC usa la banda UHF y RFID se limita a LF','NFC trabaja en HF a 13,56 MHz; RFID también incluye UHF.'),('NFC y cualquier RFID usan obligatoriamente la misma banda','RFID es una familia amplia con distintas bandas y alcances.')],
  'NFC trabaja en 13,56 MHz, dentro de HF. RFID abarca diferentes bandas y sistemas; no todos los RFID tienen el mismo alcance ni frecuencia.', url='https://nfc-forum.org/learn/nfc-technology/')
q('t31','Etiqueta RFID pasiva','95, 105',
  '¿Cómo obtiene energía una etiqueta RFID pasiva sin batería?',
  'Del campo generado por el lector', [('De una batería interna que se recarga en cada lectura','La condición dada es que no lleva batería.'),('De una conexión WiFi que transporta sus mensajes IP','No necesita convertirse en un dispositivo WiFi para responder.'),('Del GPS que incorpora cada etiqueta de identificación','Las etiquetas pasivas no requieren receptor GPS ni obtienen así su alimentación.')],
  'El lector aporta el campo que permite alimentar la etiqueta pasiva y obtener su respuesta. Las etiquetas activas incorporan su propia fuente de energía.')
q('t31','NFC y modos','100–102',
  'Un móvil se presenta ante el terminal de acceso como una tarjeta sin contacto. ¿Qué modo NFC utiliza?',
  'Emulación de tarjeta', [('Lectura/escritura de una etiqueta','En ese modo el móvil actúa como lector o escritor, no como tarjeta.'),('Intercambio punto a punto entre dos equipos','La emulación ante un lector no es el modo de intercambio entre pares.'),('Difusión WiFi a los terminales cercanos','WiFi es otra tecnología y no describe un modo NFC.')],
  'En emulación de tarjeta el dispositivo actúa como una tarjeta contactless ante el lector. El tema también distingue lectura/escritura y punto a punto.', 'Aplicación')

# T3.2: modelo celular clásico y cálculos; sin desarrollo de Erlang B.
q('t32','Generaciones móviles','5',
  '¿Qué transición introdujo GSM y la voz digital con SMS según la evolución del tema?',
  'El paso de 1G a 2G', [('El paso de 2G a 3G','3G se asocia con UMTS/HSPA y acceso a Internet móvil, no con la introducción de GSM.'),('El paso de 3G a 4G','4G se asocia con LTE y banda ancha móvil.'),('El paso de 4G a 5G','5G se asocia con NR; GSM ya pertenecía a 2G.')],
  '1G era analógico y orientado a voz. La segunda generación incorporó GSM, voz digital y SMS. La pregunta no depende de fechas de apagado de operadores.')
q('t32','Trunking','9–10',
  '¿Qué principio describe el trunking de canales?',
  'Asignar un canal disponible mientras dura su uso y liberarlo después', [('Reservar un canal exclusivo de por vida para cada usuario','Eso desperdicia el recurso cuando el usuario no lo utiliza.'),('Asignar todos los canales del sistema a cada llamada a la vez','El trunking comparte un conjunto, no consume el conjunto entero por llamada.'),('Reutilizar el mismo canal en cada celda adyacente sin coordinación','Eso introduce interferencia y no define el trunking.')],
  'El trunking permite compartir un conjunto de recursos: se ocupa un canal disponible para la comunicación y se devuelve al conjunto al finalizar.')
q('t32','Tamaño del clúster','14–15',
  'En el modelo hexagonal, i = 2 y j = 1. ¿Cuántas celdas contiene el clúster si N = i² + j² + i·j?',
  '7 celdas', [('5 celdas','Solo suma i² + j² y omite el producto i·j.'),('9 celdas','Eleva (i + j) al cuadrado, duplicando el término cruzado.'),('3 celdas','Suma i + j en lugar de aplicar la fórmula geométrica.')],
  'N = 2² + 1² + 2×1 = 4 + 1 + 2 = 7. No cualquier entero es un tamaño geométricamente posible en este modelo.', 'Cálculo')
q('t32','Fracción de reutilización','13, 16',
  'Un clúster tiene N = 7 celdas. Usando la fracción de reutilización definida como 1/N en la página 16, ¿qué fracción del conjunto total de canales recibe cada celda?',
  '1/7', [('7','Es el tamaño N del clúster, no la fracción 1/N solicitada.'),('1/6','Resta una celda sin que exista esa resta en el modelo.'),('6/7','Es el complemento de 1/7 y corresponde a los canales que no recibe esa celda.')],
  'La fracción es 1/N = 1/7. El PDF también llama «factor» a N en otra diapositiva; aquí se explicita la definición para evitar ambigüedad.', 'Cálculo')
q('t32','Canales por celda','16–17',
  'Un sistema dispone de T = 420 canales dúplex y utiliza clústeres de N = 7 celdas con reparto uniforme. ¿Cuántos canales corresponden a cada celda?',
  '60 canales', [('2940 canales','Multiplica T por N en lugar de dividirlo.'),('420 canales','Asigna el total del clúster a cada celda y omite el reparto.'),('35 canales','Divide entre 12, que no es el tamaño N indicado.')],
  'K = T/N = 420/7 = 60 canales por celda. T ya está expresado en canales dúplex, por lo que no hay que dividir de nuevo entre dos.', 'Cálculo')
q('t32','Capacidad de la red','16–17',
  'Una red tiene 84 celdas, clústeres de N = 7 y T = 420 canales dúplex por clúster. Si todos los canales se reutilizan en cada clúster, ¿cuál es la capacidad simultánea total?',
  '5040 canales', [('420 canales','Cuenta un único clúster y omite su repetición por la red.'),('35 280 canales','Multiplica por cada celda en lugar de por el número de clústeres.'),('12 canales','Ese es el número de clústeres, no el número de canales disponibles.')],
  'Hay M = 84/7 = 12 clústeres. La capacidad es M×T = 12×420 = 5040 canales, equivalente a 84×60.', 'Cálculo')
q('t32','Simplex y dúplex','20',
  'Se asignan 33 MHz en total. Cada canal de voz full dúplex ocupa dos canales simplex de 25 kHz. Sin reservar canales de control y con N = 4, ¿cuántos canales dúplex corresponden a cada celda?',
  '165 canales', [('330 canales','Olvida que cada canal dúplex utiliza dos canales simplex.'),('660 canales','Es el total de canales dúplex del sistema antes de repartir entre cuatro celdas.'),('1320 canales','Cuenta canales simplex del sistema, sin formar pares ni dividir por N.')],
  '33 MHz = 33 000 kHz. Cada par dúplex ocupa 50 kHz: T = 33 000/50 = 660. Después K = 660/4 = 165.', 'Cálculo')
q('t32','Distancia cocanal','21, 25',
  'Con N = 7 y un radio de celda R = 2 km, ¿qué distancia cocanal D resulta aproximadamente de D/R = √(3N)?',
  '9,17 km', [('4,58 km','Es el valor numérico de D/R; falta multiplicar por el radio de 2 km.'),('42 km','Usa 3N×R y omite la raíz cuadrada.'),('14 km','Multiplica N por R sin aplicar √(3N).')],
  'D = R√(3N) = 2√21 ≈ 2×4,5826 = 9,17 km. D/R no tiene unidades; D sí se mide en kilómetros.', 'Cálculo')
q('t32','Señal e interferencia','23–27',
  'En el modelo de seis interferentes iguales, N = 7 y exponente de pérdidas n = 4. Usando S/I = (3N)^(n/2)/6, ¿qué relación lineal se obtiene?',
  '73,5', [('441','Es (3N)²; falta dividir entre los seis interferentes.'),('18,7','Es aproximadamente el resultado en dB, no la relación lineal pedida.'),('3,5','Divide 3N entre seis sin elevar a n/2.')],
  'S/I = 21²/6 = 441/6 = 73,5. Su equivalente en decibelios es 10 log₁₀(73,5) ≈ 18,66 dB.', 'Cálculo')
q('t32','Decibelios','24',
  'La potencia de una señal es cien veces la potencia de interferencia. ¿Cuánto vale S/I en dB?',
  '20 dB', [('40 dB','Aplica 20 log₁₀ a una relación de potencias; aquí corresponde 10 log₁₀.'),('10 dB','Corresponde a una relación de potencia de 10, no de 100.'),('100 dB','Confunde directamente el cociente lineal con su representación logarítmica.')],
  'Para una relación de potencias se utiliza 10 log₁₀(100) = 10×2 = 20 dB.', 'Cálculo')
q('t32','Capacidad e interferencia','21, 27–28',
  'Con el mismo total de canales y radio de celda, se reduce N de 7 a 4 en el modelo clásico de reutilización. ¿Qué compromiso se produce?',
  'Más canales por celda y más interferencia cocanal', [('Más canales por celda y menos interferencia cocanal','Disminuir N acerca las celdas cocanal y empeora la interferencia.'),('Menos canales por celda y menos interferencia cocanal','Eso describe el efecto de aumentar N.'),('Menos canales por celda y más distancia cocanal','Ambos efectos están invertidos respecto a reducir N.')],
  'K = T/N aumenta si baja N, pero D/R = √(3N) disminuye. Las celdas que reutilizan los canales quedan más cerca y la relación S/I empeora.', 'Aplicación')
q('t32','División celular','29',
  'En una zona saturada se sustituye una celda por varias celdas más pequeñas con sus propias estaciones base y planificación. ¿Cuál es el objetivo principal?',
  'Aumentar la capacidad por unidad de superficie', [('Eliminar la necesidad de planificar las frecuencias','La división requiere coordinar recursos y añade complejidad a la asignación.'),('Evitar todos los traspasos de los usuarios en movimiento','Las celdas menores pueden exigir más traspasos al desplazarse.'),('Dar más cobertura con una única antena de mayor potencia','La división utiliza varias estaciones y radios menores, no una única antena más potente.')],
  'Cell splitting facilita reutilizar recursos más veces en una zona, a costa de nuevos emplazamientos y mayor complejidad. No elimina interferencias ni movilidad.', 'Aplicación')
q('t32','Arquitectura celular clásica','35–36',
  'En la arquitectura GSM del tema, ¿qué elemento controla varias BTS y gestiona traspasos entre ellas dentro de su dominio?',
  'BSC', [('BTS','La BTS mantiene el enlace radio con los móviles de la celda.'),('MSC como estación radio de cada celda','El MSC realiza conmutación y coordinación de mayor alcance; no es la estación radio.'),('UE','UE es el equipo del usuario, no el controlador de varias BTS.')],
  'El Base Station Controller controla varias estaciones BTS. El MSC conecta y conmuta a un nivel superior. Este esquema se pregunta en su contexto GSM, no como arquitectura idéntica de 4G/5G.')
q('t32','Alcance del handover','36–40',
  'Un móvil cambia de BTS, pero la BTS de origen y la de destino dependen del mismo BSC. ¿Qué tipo de traspaso es?',
  'Inter-celda, intra-BSC', [('Intra-celda','En el intra-celda cambia el canal dentro de la misma celda, no la BTS.'),('Inter-BSC, intra-MSC','Requeriría cambiar de BSC, que aquí se mantiene.'),('Inter-MSC','Requeriría cambiar de central MSC, no solo de BTS dentro de un BSC.')],
  'Se cambia de celda dentro del mismo controlador, por lo que es un handover inter-celda e intra-BSC.', 'Aplicación')
q('t32','MAHO','41',
  'En un traspaso asistido por el móvil (MAHO), ¿quién realiza las medidas y quién toma la decisión?',
  'Mide el móvil y decide la red', [('Mide la red y decide el móvil','Invierte los papeles del esquema MAHO.'),('Mide la red y decide la red','Ese reparto corresponde al NCHO descrito.'),('Mide el móvil y decide el móvil','Ese reparto corresponde al MCHO descrito.')],
  'MAHO significa Mobile Assisted Handover: el móvil aporta medidas y la red decide. No debe confundirse asistencia con control completo por el terminal.')
q('t32','Hard y soft handover','42',
  '¿Qué secuencia caracteriza a un soft handover?',
  'Establecer el enlace nuevo antes de soltar el anterior', [('Soltar el enlace anterior antes de establecer el nuevo','Esa secuencia es hard handover, break before make.'),('Mantener la llamada en la misma celda sin cambiar recursos','Eso no describe por sí solo un traspaso soft.'),('Rechazar la llamada y pedir al usuario que vuelva a marcar','Un traspaso busca conservar la llamada en curso, no iniciar una nueva.')],
  'Soft handover es make before break: durante la transición coexisten enlaces. Hard handover corta primero y establece después.')
q('t32','Canales de guarda','43–45',
  'Una celda tiene diez canales, dos reservados a traspasos. Los ocho compartidos están ocupados y los dos de guarda libres. ¿Qué sucede con una llamada nueva según esta política?',
  'Se bloquea aunque haya canales de guarda libres', [('Usa uno de los dos canales reservados automáticamente','Los canales de guarda del caso son exclusivos para traspasos.'),('Desplaza una llamada en curso para liberar un canal','La política descrita no expulsa llamadas en curso.'),('Se considera un traspaso porque ya ha solicitado acceso','Pedir una llamada nueva no la convierte en una comunicación ya en curso.')],
  'La reserva protege los traspasos y reduce cortes de llamadas existentes. Su coste es aumentar el bloqueo de nuevas llamadas al limitar sus canales disponibles.', 'Aplicación')
q('t32','Intensidad en erlangs','49, 56',
  'Durante tres horas se cursan 600 llamadas de tres minutos de duración media. ¿Qué intensidad media de tráfico cursado representan?',
  '10 erlangs', [('30 erlangs','Divide por una hora cuando el intervalo observado son tres horas.'),('600 erlangs','Confunde el número de llamadas con la ocupación media de circuitos.'),('1800 erlangs','Es el volumen en minutos de llamada, sin dividir entre los 180 minutos observados.')],
  'El volumen es 600×3 = 1800 minutos de llamada. La intensidad es 1800/180 = 10 erlangs, equivalente a diez circuitos ocupados de media.', 'Cálculo')
q('t32','Grado de servicio','50, 52, 57',
  'En un sistema con pérdidas se ofrecen 25 erlangs y se cursan 15. Usando GoS = tráfico perdido / tráfico ofrecido, ¿cuál es el grado de servicio?',
  '40 %', [('60 %','Es la fracción de tráfico cursado 15/25, no la de tráfico perdido.'),('10 %','La diferencia es 10 erlangs, que no equivale directamente a un porcentaje.'),('66,7 %','Divide el tráfico perdido entre el cursado en lugar de entre el ofrecido.')],
  'El tráfico perdido es 25 − 15 = 10 erlangs. GoS = 10/25 = 0,4 = 40 %. En esta definición un porcentaje de pérdidas menor indica mejor servicio.', 'Cálculo')
q('t32','Volumen frente a intensidad','51, 55',
  'Un grupo cursa 500 llamadas de cuatro minutos en tres horas. ¿Qué pareja indica correctamente su volumen y su intensidad de tráfico?',
  '2000 minutos de llamada y aproximadamente 11,11 erlangs', [('2000 erlangs y aproximadamente 11,11 minutos de llamada','Intercambia las magnitudes y sus unidades.'),('500 minutos de llamada y aproximadamente 2,78 erlangs','Omite la duración de cuatro minutos de cada llamada.'),('2000 minutos de llamada y aproximadamente 33,33 erlangs','Divide el volumen entre 60 minutos en lugar de los 180 de observación.')],
  'Volumen = 500×4 = 2000 minutos de llamada. Intensidad = 2000/(3×60) ≈ 11,11 erlangs. No se necesita aplicar la fórmula de Erlang B.', 'Cálculo')

def save():
    from guide_update import apply_guide
    retired=apply_guide(questions,BLOCKS,q)
    from practice_expansion import expand
    expand(q)
    # Orden numérico/binario ascendente en ejercicios donde facilita comparar resultados.
    ordered={'t21-28','t22-02','t22-03','t22-05','t22-06','t22-07','t22-13','t22-23',
             't32-03','t32-04','t32-05','t32-06','t32-07','t32-08','t32-09','t32-10','t32-18','t32-19'}
    def number(text):
        value=re.match(r'^[\d\s.,/]+',text).group().replace(',','.').replace(' ','')
        if '/' in value:
            a,b=value.split('/')
            return float(a)/float(b)
        return float(value)
    for question in questions:
        if question['id'] in ordered:
            question['options'].sort(key=lambda o:number(o['text']))
            question['shuffle_options']=False
    out=ROOT/'content'/'draft.json'
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps({'title':'DISM · Banco de estudio','expected_questions':len(questions),'options_per_question':4,
        'guide_version':'repaso-2','practice_version':'2026-10-26','retired_question_ids':list(retired),'blocks':BLOCKS,'questions':questions},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (ROOT/'content/retired.json').write_text(json.dumps(retired,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Written {len(questions)} questions')

if __name__=='__main__': save()
