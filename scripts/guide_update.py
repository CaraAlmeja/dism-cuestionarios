"""Cambios de alcance de la segunda guía. Mantiene IDs y clave de los ítems conservados."""

def apply_guide(questions,blocks,q):
    retired={
        't1-12':'Mecanismo interno de una PWA: fuera del alcance de funcionamiento interno.',
        't1-14':'Flutter: exclusión expresa de la segunda guía.',
        't31-17':'Generaciones WiFi: exclusión expresa de versiones de conectividad.',
        't32-01':'Generaciones móviles: exclusión expresa de versiones de redes móviles.',
    }
    blocks.append({'id':'t4','code':'T4','title':'OpenAPI','subtitle':'Una única pregunta: qué es OpenAPI','icon':'book','color':'blue'})
    by_id={item['id']:item for item in questions}
    def option(qid,oid,text,why):
        item=by_id[qid]
        next(o for o in item['options'] if o['id']==oid)['text']=text
        item['distractor_rationales'][oid]=why
    option('t1-05','o3','C# y Android Studio como entorno específico de Apple','Android Studio es el entorno de Android; para el desarrollo iOS del caso se usa Swift con Xcode.')
    option('t1-06','o3','Un entorno exclusivo para escribir apps iOS con Swift','Xamarin permite compartir C# entre plataformas, no es un entorno exclusivo de Swift.')
    option('t1-07','o2','Desplegar servicios backend HTTP sin interfaz móvil','Cordova se ocupa de aplicaciones móviles web empaquetadas y su acceso al dispositivo, no de alojar servicios backend.')
    option('t1-08','o3','Un servicio de compilación exclusivo para proyectos Swift de iOS','Ionic es un framework multiplataforma de tecnologías web, no un servicio exclusivo de Swift.')
    option('t1-09','o2','Sustituir la WebView por controles nativos de interfaz','Capacitor facilita acceso a APIs nativas pero mantiene la interfaz web en una WebView.')
    option('t1-09','o3','Subir las fotografías al servidor de la aplicación','La subida depende de la lógica y servicios de la app; el papel del plugin es integrar la cámara.')
    option('t1-13','o4','Un conjunto de plugins JavaScript para aplicaciones híbridas','Esa descripción encaja con integraciones híbridas como Cordova, no con el framework C#/XAML de MAUI.')
    option('t1-15','o3','Ionic','Ionic puede utilizar React, pero presenta su interfaz web en una WebView, frente a la interfaz nativa solicitada.')
    option('t1-16','o4','MAUI con controles escritos en XAML','MAUI trabaja con C# y XAML; no es la tecnología de compartición de lógica Kotlin del caso.')
    option('t1-17','o2','Ionic','Ionic también usa tecnologías web, pero no se define por el núcleo Rust descrito.')
    wifi=by_id['t31-16']
    wifi['stem']='Se comparan dos enlaces WiFi, uno en 2,4 GHz y otro en 6 GHz, con potencia, antenas y entorno comparables. ¿Qué banda tiende a ofrecer mayor alcance y penetración en interiores?'
    wifi['explanation']='En condiciones comparables, 2,4 GHz tiende a atravesar obstáculos mejor y cubrir más distancia que 6 GHz. El alcance real también depende de potencia, antenas, sensibilidad e interferencias; la comparación no se basa en el nombre de una generación.'
    option('t31-16','o2','6 GHz, porque una frecuencia mayor garantiza más cobertura','Una frecuencia más alta no garantiza más alcance; en igualdad de condiciones suele atenuarse más al atravesar obstáculos.')

    # Nuevas preguntas. Se añaden antes de retirar para no reutilizar IDs históricos.
    q('t1','Aplicaciones móviles','2–3',
      '¿Qué describe el desarrollo de aplicaciones móviles en el contexto del tema?',
      'Crear software orientado a dispositivos como smartphones y tabletas',
      [('Diseñar únicamente páginas web para ordenadores de sobremesa','El desarrollo móvil tiene como destino dispositivos móviles, aunque pueda reutilizar tecnologías web.'),('Instalar y mantener las antenas de una red de telefonía','Eso es infraestructura de comunicaciones, no el proceso de desarrollo de apps.'),('Fabricar procesadores y pantallas para teléfonos','El desarrollo de aplicaciones escribe software; no fabrica los componentes físicos.')],
      'El tema define el desarrollo móvil como procesos y procedimientos para crear software destinado a pequeños dispositivos inalámbricos, como teléfonos y tabletas.')

    q('t21','Aplicaciones multimedia','2–3',
      '¿Qué caracteriza a una aplicación multimedia?',
      'Integra varios medios, como texto, audio e imagen, bajo control informático',
      [('Utiliza exclusivamente vídeo, aunque disponga de texto o sonido','La multimedia integra diferentes medios; no exige limitarse al vídeo.'),('Presenta cada medio en un equipo aislado, sin integración entre ellos','La integración controlada es parte del concepto.'),('Sustituye los datos digitales por señales analógicas independientes','El sistema del tema representa y procesa la información digitalmente.')],
      'Una aplicación multimedia combina información de distintos medios y fuentes, de forma coordinada por el sistema informático.')
    q('t21','Hipermedia','4–5',
      'Un museo ofrece fichas de obras enlazadas con vídeos y audios. El visitante elige qué enlaces seguir. ¿Qué rasgo aporta la hipermedia?',
      'Navegación entre contenidos de distintos medios',
      [('Reproducción de todo el material en una secuencia obligatoria','Una secuencia obligatoria se corresponde con multimedia lineal, sin la elección descrita.'),('Duplicación del mismo vídeo en varios discos','La redundancia de almacenamiento no define la navegación hipermedia.'),('Transmisión de un único directo a todos los visitantes','La distribución simultánea no explica los enlaces elegidos individualmente.')],
      'La hipermedia combina medios y un sistema de navegación que permite al usuario elegir su recorrido.', 'Aplicación')
    q('t21','Integración digital','6',
      '¿Qué requisito permite a un sistema multimedia almacenar y procesar de forma integrada información de medios distintos?',
      'Representar digitalmente la información bajo control del computador',
      [('Mantener los medios como señales analógicas sin conversión','No permite el procesamiento digital integrado descrito.'),('Utilizar un programa sin relación para cada medio y no intercambiar datos','La ausencia de integración contradice el sistema multimedia del tema.'),('Asignar el mismo tamaño de archivo a todos los medios','Texto, audio e imagen tienen representaciones y necesidades diferentes; igualar tamaños no los integra.')],
      'La integración requiere representaciones digitales manejables por el sistema. No significa que todos los medios usen un mismo formato o tamaño.')
    q('t21','Proyecto multimedia: planificación','13',
      'Antes de producir los materiales se estiman personas, equipos, costes y tiempo, y se redactan los requisitos. ¿A qué etapa corresponde?',
      'Planificación y evaluación de costes',
      [('Diseño y producción de materiales','Esa etapa desarrolla los recursos y el código a partir de la planificación.'),('Pruebas de conformidad del sistema terminado','Las pruebas contrastan el sistema con requisitos ya definidos.'),('Distribución y promoción del producto','La distribución prepara y entrega el producto al final del proceso.')],
      'La planificación concreta necesidades, costes y especificaciones. Sirve de referencia para producir y evaluar el sistema.', 'Aplicación')
    q('t21','Proyecto multimedia: pruebas','13',
      'Un equipo ejecuta su aplicación en distintas situaciones y contrasta el resultado con las especificaciones. ¿Cuál es el propósito de esa etapa?',
      'Comprobar si el sistema cumple los requisitos definidos',
      [('Definir por primera vez qué producto se quiere construir','Los requisitos se establecen durante la planificación y sirven de criterio a las pruebas.'),('Limitarse a empaquetar la aplicación para su distribución','Empaquetar y distribuir no verifica por sí mismo los requisitos.'),('Producir todos los audios y vídeos que aún faltan','La producción genera recursos; aquí se está evaluando el sistema.')],
      'Las pruebas evalúan si el sistema funciona de acuerdo con sus requisitos en diferentes situaciones de uso.', 'Aplicación')
    q('t21','Requerimientos multimedia','14–15',
      'Una aplicación reproduce vídeo en tiempo real, pero su sistema de archivos entrega datos de forma irregular y demasiado lenta. ¿Qué requisito necesita reforzar directamente?',
      'La eficiencia y rapidez de entrada/salida de los datos',
      [('La capacidad total de almacenamiento, aunque la lectura siga igual','Más capacidad no resuelve por sí misma la velocidad o regularidad de lectura.'),('La potencia gráfica, manteniendo el mismo suministro insuficiente de datos','El cuello de botella descrito es entregar datos, no procesarlos una vez recibidos.'),('La rapidez con que aparece el menú inicial de la aplicación','Una interfaz que abre antes no garantiza el caudal de datos durante el vídeo.')],
      'La captura y reproducción en tiempo real necesitan E/S suficiente y regular. Más capacidad de almacenamiento no implica por sí sola más rapidez de acceso.', 'Aplicación')
    q('t21','Jitter frente a latencia','52–53',
      'Todos los paquetes tardan 200 ms y llegan separados exactamente por los mismos intervalos con los que se enviaron. ¿Qué describe mejor ese enlace idealizado?',
      'Tiene retardo constante y no presenta jitter de llegada',
      [('Tiene mucho jitter porque el retardo no es cero','Un retardo grande pero constante no implica variación del retardo.'),('No tiene latencia porque conserva los intervalos','La latencia sigue siendo 200 ms, aunque los intervalos sean regulares.'),('Tiene jitter igual al bitrate del vídeo','El jitter y el bitrate son magnitudes distintas.')],
      'La latencia es el tiempo de tránsito; el jitter es su variación. Puede existir latencia elevada con una llegada perfectamente regular.', 'Aplicación')
    q('t21','Dimensionado de una reserva','52–53',
      'Un reproductor guarda una reserva de 8 Mbit. Consume a 4 Mbit/s y recibe de forma constante 2 Mbit/s. Sin adaptación de calidad, ¿cuánto tarda en agotar esa reserva?',
      '4 segundos',
      [('2 segundos','Divide la reserva por el consumo, pero omite los datos que siguen llegando.'),('8 segundos','No divide por el déficit neto de 2 Mbit/s.'),('16 segundos','Multiplica por el déficit en lugar de dividir la reserva entre ese déficit.')],
      'La reserva disminuye a 4 − 2 = 2 Mbit/s. Por tanto, tarda 8/2 = 4 s en vaciarse. Un búfer finito no compensa indefinidamente un caudal inferior al consumo.', 'Cálculo')
    q('t21','Netflix: control y entrega','57–59, 67',
      'En el esquema simplificado de Netflix del tema, ¿qué reparto de responsabilidades es correcto?',
      'El backend gestiona identidad y catálogo; Open Connect entrega el vídeo',
      [('El OCA factura las suscripciones y el backend sirve todos los bytes de vídeo','Intercambia la función de entrega del OCA con la lógica de servicio del backend.'),('El cliente administra los servidores y el OCA decide las recomendaciones','El cliente reproduce y los OCA entregan; la personalización pertenece al backend.'),('El backend solo guarda fotogramas y Open Connect ejecuta el inicio de sesión','Reduce el backend a almacenamiento y atribuye al OCA una función de identidad que no le corresponde.')],
      'La arquitectura distingue el plano de control (identidad, catálogo y decisiones) de la entrega audiovisual desde Open Connect.')
    q('t21','Netflix: autorización de reproducción','62–64',
      'Un cliente solicita reproducir una película. Según el flujo del PDF, ¿qué debe comprobar el servicio de reproducción antes de facilitar el acceso?',
      'Que la solicitud esté autorizada por el plan y la licencia del contenido',
      [('Que el cliente haya elegido ya el OCA de menor latencia','La selección del OCA es un paso posterior a validar la petición en el flujo descrito.'),('Que todos los OCA contengan la totalidad del catálogo','No se necesita replicar todo el catálogo en cada caché para autorizar una película.'),('Que todos los espectadores utilicen la misma calidad de vídeo','La autorización no exige una representación idéntica para todos los clientes.')],
      'El servicio comprueba que la petición sea válida para el contenido y el suscriptor antes de organizar su reproducción.', 'Aplicación')
    q('t21','Netflix: ubicación de OCA','57–59',
      '¿Por qué resulta útil ubicar un OCA dentro de la red de un proveedor de Internet?',
      'Acerca los archivos al usuario y reduce tráfico de tránsito externo',
      [('Evita que el cliente necesite conexión a la red','El cliente sigue necesitando conectividad para solicitar y recibir contenido.'),('Convierte cada película en un vídeo sin compresión','La ubicación del servidor no elimina la codificación de los vídeos.'),('Sustituye las cuentas y permisos por acceso anónimo a todo el catálogo','Los controles de acceso siguen gestionándose aunque la caché sea cercana.')],
      'La entrega localizada reduce la distancia de red y la dependencia de enlaces externos. No equivale a reproducir sin conexión ni a eliminar la autorización.', 'Aplicación', url='https://openconnect.netflix.com/en/')
    q('t21','Unicast y multicast','25',
      'Desde una misma interfaz de origen se envía un directo de 8 Mbit/s a 100 usuarios. Sin sobrecarga y suponiendo multicast admitido por la red, ¿qué tráfico sale del origen en cada caso?',
      'Unicast: 800 Mbit/s; multicast: 8 Mbit/s',
      [('Unicast: 8 Mbit/s; multicast: 800 Mbit/s','Invierte el flujo individual de unicast y el flujo compartido de multicast.'),('Unicast: 800 Mbit/s; multicast: 800 Mbit/s','Cuenta una copia por usuario también en el origen multicast.'),('Unicast: 8 Mbit/s; multicast: 8 Mbit/s','Omite las cien copias individuales que debe enviar ese origen en unicast.')],
      'Unicast envía 100 flujos: 100×8 = 800 Mbit/s. Multicast emite un flujo de 8 Mbit/s en el origen y la red lo replica donde corresponde.', 'Cálculo')
    q('t21','QoS y medios interactivos','14–15',
      '¿Por qué una videoconferencia necesita cuidar especialmente el retardo además del caudal de datos?',
      'El retraso excesivo dificulta la interacción aunque llegue todo el contenido',
      [('La ausencia de pérdidas garantiza por sí sola una conversación fluida','Una entrega perfecta pero muy tardía sigue perjudicando la conversación.'),('Aumentar la reserva de búfer elimina el retraso percibido','Una reserva mayor puede mejorar estabilidad, pero añade espera y no elimina la latencia.'),('Ancho de banda y latencia son dos nombres de la misma magnitud','Miden capacidad de transferencia y tiempo, respectivamente; hay que atender a ambas.')],
      'En aplicaciones interactivas importa que la información llegue a tiempo. Una tasa suficiente o una entrega sin pérdidas no garantizan por sí mismas baja latencia.', 'Aplicación')

    # Continúa con codificación, arquitectura y dispositivos en la siguiente sección.
    _add_hardware(q)
    questions[:]=[item for item in questions if item['id'] not in retired]
    return retired


def _add_hardware(q):
    q('t22','UTF-32','23',
      '¿Qué forma de codificación Unicode emplea cuatro bytes por punto de código?',
      'UTF-32',
      [('UTF-8','UTF-8 utiliza de uno a cuatro bytes, según el punto de código.'),('UTF-16','UTF-16 utiliza una o dos unidades de 16 bits, no cuatro bytes para todos los puntos de código.'),('ASCII de 7 bits','ASCII tiene un repertorio limitado y no es una codificación de todo Unicode en cuatro bytes.')],
      'UTF-32 representa cada punto de código Unicode en una unidad de 32 bits. Un carácter visual puede componerse de varios puntos de código; no hay que confundir ambas magnitudes.')
    q('t22','Elección entre UTF','23, 25–26',
      'Un texto contiene solo ideogramas del BMP que necesitan tres bytes en UTF-8 y una unidad en UTF-16. Sin cabeceras ni BOM, ¿qué representación usa menos espacio por esos puntos de código?',
      'UTF-16, con dos bytes por punto de código',
      [('UTF-8, con un byte por punto de código','Un byte en UTF-8 corresponde a ASCII, no a los ideogramas especificados.'),('UTF-32, con un byte por punto de código','UTF-32 utiliza cuatro bytes, no uno.'),('Las tres ocupan lo mismo por tratarse de Unicode','Unicode no obliga a que todas sus codificaciones tengan el mismo tamaño.')],
      'Con las condiciones dadas, UTF-16 usa 2 bytes, UTF-8 usa 3 y UTF-32 usa 4. La ventaja de espacio de UTF-8 en textos ASCII no se generaliza a todos los repertorios.', 'Aplicación')
    q('t22','Tamaño de texto ASCII','23, 25',
      'Se guardan 100 puntos de código del repertorio ASCII, sin BOM ni cabeceras. ¿Cuántos bytes necesita UTF-8?',
      '100 bytes',
      [('200 bytes','Cuenta dos bytes por punto de código como en UTF-16 para este repertorio.'),('400 bytes','Aplica el tamaño fijo de UTF-32 en lugar de UTF-8.'),('800 bytes','Confunde bits y bytes o multiplica por ocho una cantidad que ya está en bytes.')],
      'Cada punto de código ASCII ocupa un byte en UTF-8: 100×1 = 100 bytes. En las condiciones del enunciado serían 200 en UTF-16 y 400 en UTF-32.', 'Cálculo')
    q('t22','RAID 10','16',
      'Un RAID 10 tiene dos parejas espejo: discos A/B y discos C/D. Fallan A y C y sus compañeros siguen operativos. ¿Qué ocurre con los datos del conjunto?',
      'Siguen accesibles porque queda una copia de cada pareja',
      [('Se pierden porque RAID 10 solo tolera un fallo en todo el conjunto','Puede tolerar más de un fallo si no se pierden todas las copias de una pareja.'),('Se recuperan mediante la doble paridad de A y C','RAID 10 utiliza espejos y división de datos, no doble paridad.'),('Solo queda accesible la mitad que estaba en B','D conserva la copia de C; no se pierde esa mitad de los datos.')],
      'La tolerancia depende de qué discos fallen. A y C pertenecen a parejas distintas y B/D conservan sus datos. Perder A y B sí eliminaría una pareja completa.', 'Aplicación')
    q('t22','Clasificación de arquitecturas','47, 61–63',
      'En la clasificación del tema, ¿qué asociación entre familia y forma de adaptación es correcta?',
      'Programable: cambia instrucciones; dedicada ASIC: circuito fijo; FPGA: lógica reconfigurable',
      [('Programable: circuito fijo sin instrucciones; ASIC: cambia su lógica; FPGA: solo cambia datos','Atribuye la reconfiguración al ASIC e impide a la FPGA adaptar la lógica.'),('Programable: cambia instrucciones; ASIC: lógica reconfigurable; FPGA: circuito fijo','Intercambia las propiedades de ASIC y FPGA.'),('Programable: cambia conexiones físicas; ASIC: ejecuta cualquier software; FPGA: solo almacena','Confunde el software programable, el circuito dedicado y el hardware reconfigurable.')],
      'El árbol de la página 47 distingue programables, dedicadas y reconfigurables. El programa adapta la secuencia de instrucciones; el ASIC dedica su circuito a una tarea; la FPGA permite reconfigurar su lógica.')
    q('t22','Programables de propósito general y específicas','47, 51–53, 63',
      '¿Dónde se sitúa un DSP programable en el árbol de arquitecturas del tema?',
      'En las programables específicas, optimizadas para procesamiento de señal',
      [('En las dedicadas ASIC, porque ningún DSP admite cambiar su programa','Un DSP programable permite cambiar instrucciones; especialización no significa circuito ASIC fijo.'),('En las reconfigurables FPGA, porque ejecutar un filtro cambia sus conexiones','Cambiar el programa de un DSP no equivale a reconfigurar bloques e interconexiones de una FPGA.'),('En las programables de propósito general, sin especialización para señal','El DSP del caso está optimizado para algoritmos de señal y se sitúa entre las programables específicas.')],
      'En la clasificación, ser específico indica optimización para una clase de tareas. Un DSP puede seguir siendo programable; no debe confundirse esa especialización con la rama de ASIC dedicados.')
    q('t22','Monolíticas y modulares','47, 61–62',
      '¿Qué distingue una implementación monolítica de una modular en las arquitecturas del tema?',
      'La monolítica integra el sistema en un chip; la modular combina varios chips',
      [('La monolítica ejecuta un único programa; la modular permite varios usuarios','Monolítico/modular se refiere aquí a la implementación física, no al número de programas o usuarios.'),('La monolítica carece de memoria; la modular tiene memoria externa','El número de chips no impone esa ausencia de memoria.'),('La monolítica es siempre FPGA; la modular es siempre ASIC','La distinción de uno o varios chips puede aplicarse a diferentes familias.')],
      'La distinción monolítica/modular describe la integración física. Es un eje diferente de programable, dedicado o reconfigurable.')
    q('t22','RISC y CISC','47, 49–50',
      '¿Qué diferencia conceptual entre RISC y CISC recoge el temario?',
      'RISC prioriza instrucciones simples; CISC dispone de un repertorio más complejo',
      [('RISC usa el repertorio más complejo y CISC prioriza instrucciones simples','Invierte la distinción conceptual presentada en el tema.'),('CISC tiene instrucciones de longitud fija y RISC las tiene todas variables','No corresponde a la caracterización del tema, que destaca la longitud variable en CISC.'),('Solo CISC permite compilar programas escritos en lenguajes de alto nivel','Ambas familias pueden ejecutar programas compilados desde lenguajes de alto nivel.')],
      'Dentro de las programables de propósito general, RISC se asocia con instrucciones frecuentes y simples y CISC con un juego más rico y complejo. No son familias RAID ni sinónimos de FPGA.')
    q('t22','Efectos de la compresión con pérdida','32, 34–35',
      'Se comprime una fotografía con JPEG convencional usando una compresión cada vez más agresiva. ¿Qué compromiso debe evaluarse?',
      'Reducir el tamaño frente a introducir pérdida de detalle y artefactos',
      [('Reducir el tamaño manteniendo igualdad exacta de todos los píxeles','JPEG convencional es con pérdida; esa igualdad exacta no está garantizada.'),('Aumentar la calidad original eliminando información de forma irreversible','Descartar información no crea detalle original nuevo.'),('Evitar la descompresión porque los píxeles comprimidos se muestran directamente','La información codificada necesita decodificarse para reconstruir la imagen.')],
      'La compresión con pérdida descarta información. Una reducción de tamaño mayor puede hacer visibles errores de reconstrucción; ampliar después el archivo no recupera los datos originales.', 'Aplicación')
    q('t22','Percepción y compresión de imágenes','35',
      '¿Qué propiedad de la visión humana aprovecha la compresión JPEG descrita en el tema?',
      'La mayor sensibilidad a variaciones de luminancia que de crominancia',
      [('La mayor sensibilidad a cambios de color que a cambios de brillo','Invierte la relación perceptiva que presenta el tema.'),('La incapacidad de percibir detalles en cualquier zona uniforme','El tema indica que pequeñas variaciones de brillo se perciben con facilidad en zonas homogéneas.'),('La percepción idéntica de todas las frecuencias y componentes de la imagen','La compresión perceptiva aprovecha precisamente sensibilidades diferentes.')],
      'La visión no responde por igual al brillo y al color ni a todas las variaciones espaciales. Esa diferencia permite reducir información perceptivamente menos relevante.')
    q('t22','Memoria y datos multimedia','44–46',
      'Una MMA recorre grandes flujos de datos con poca reutilización temporal. ¿Por qué sigue necesitando gran ancho de banda de memoria?',
      'Debe alimentar continuamente el procesamiento con muchos datos nuevos',
      [('La baja reutilización garantiza que todos los datos estarán siempre en caché','La poca reutilización temporal reduce la ayuda de guardar copias para accesos repetidos.'),('Los operandos pequeños hacen innecesaria la transferencia de datos','Aunque cada operando sea pequeño, se procesan muchos y con frecuencia.'),('El procesador puede reconstruir todos los datos sin leer memoria','El cómputo necesita recibir los datos de entrada del flujo.')],
      'Las MMA pueden reutilizar el código de sus bucles y, al mismo tiempo, consumir datos nuevos a gran ritmo. Eso exige memoria y E/S capaces de sostener el flujo.', 'Aplicación')

    q('t31','Componentes del móvil: SoC','4',
      '¿Qué describe un System-on-Chip (SoC) de un smartphone?',
      'Un chip que integra varios bloques, como CPU, GPU, módem y otros procesadores',
      [('La memoria flash donde se instalan todas las aplicaciones','La flash es almacenamiento; un SoC integra bloques de procesamiento y control.'),('La capa táctil que detecta la posición del dedo','La detección de toque pertenece a la interfaz de pantalla, no define un SoC.'),('Una batería que proporciona distintos voltajes al teléfono','La batería alimenta el sistema, pero no es el chip de procesamiento integrado.')],
      'Un SoC agrupa funciones que podrían requerir varios componentes: procesamiento general, gráficos, comunicaciones y otros aceleradores. No equivale al almacenamiento o a la batería.')
    q('t31','RAM y almacenamiento flash','4',
      'En un smartphone, ¿qué diferencia funcional hay entre RAM y almacenamiento flash?',
      'RAM: datos temporales de trabajo; flash: almacenamiento persistente',
      [('RAM: almacenamiento no volátil; flash: datos temporales de la app','Invierte las propiedades de memoria de trabajo y almacenamiento persistente.'),('RAM y flash son volátiles y se borran al apagar el móvil','La flash conserva datos sin alimentación; no es memoria de trabajo volátil.'),('RAM y flash son persistentes y solo cambia su velocidad','La RAM de trabajo no conserva sus datos sin alimentación.')],
      'La RAM se utiliza como memoria de trabajo volátil. El almacenamiento flash conserva datos de forma no volátil y no tiene partes móviles.')
    q('t31','Procesamiento de IA en el dispositivo','4, 8',
      '¿Qué bloque del SoC está especializado en ejecutar redes neuronales en el propio móvil?',
      'La NPU',
      [('El módem','El módem se ocupa de comunicaciones radio, no es el acelerador especializado en redes neuronales.'),('La memoria flash','Almacena datos y aplicaciones; no ejecuta por sí misma las operaciones de inferencia.'),('El controlador táctil','Detecta y comunica interacciones de toque, no es la unidad especializada en IA.')],
      'La NPU acelera operaciones de redes neuronales. Que exista una NPU no implica que todo modelo o servicio de IA pueda funcionar sin conexión.')
    q('t31','Comparativa LCD y AMOLED','68, 72',
      '¿Qué ventaja de LCD IPS frente a AMOLED recoge la comparativa del tema?',
      'Menor coste y mayor estabilidad frente al quemado de una imagen fija',
      [('Negro real obtenido al apagar individualmente los píxeles emisores','Esa propiedad corresponde a OLED/AMOLED, no a LCD retroiluminado.'),('Panel autoemisivo más delgado por carecer de retroiluminación','La ausencia de retroiluminación caracteriza a OLED/AMOLED.'),('Ahorro de consumo al apagar todos los píxeles de las zonas negras','Ese mecanismo corresponde a los píxeles emisores de OLED/AMOLED, no al LCD.')],
      'El cuadro comparativo destaca menor coste y estabilidad de LCD frente al posible quemado de AMOLED. La elección cambia si se priorizan negros, flexibilidad o consumo con imágenes oscuras.', 'Aplicación')
    q('t31','Bluetooth e interferencias','77–78',
      'Un móvil utiliza WiFi en 2,4 GHz mientras transmite audio por Bluetooth. ¿Por qué puede aparecer un problema de coexistencia?',
      'Ambas tecnologías comparten parte de la banda radioeléctrica',
      [('Bluetooth y WiFi interpretan necesariamente todos los mensajes del otro','Compartir banda no significa utilizar el mismo protocolo ni entender sus mensajes.'),('La interferencia depende de que ambos usen la misma dirección IP','El problema de radio no exige compartir una dirección de red.'),('Bluetooth necesita alineación óptica y el WiFi la interrumpe','Bluetooth utiliza radiofrecuencia, no un enlace óptico alineado.')],
      'Bluetooth y WiFi en 2,4 GHz pueden interferirse. La coexistencia radio ayuda a reducir ese efecto. No significa que toda red celular opere en 2,4 GHz ni que cualquier conexión móvil produzca la misma interferencia.', 'Aplicación',url='https://support.apple.com/en-us/102319')
    q('t31','Coexistencia de radios de un móvil','77–79',
      'En un terminal con radios Bluetooth y celular próximas, el diseño incorpora mecanismos de coexistencia. ¿Qué problema de radio pretenden reducir?',
      'Que la actividad de una radio degrade la recepción de la otra',
      [('Que los dispositivos deban utilizar el mismo códec de vídeo','La coexistencia trata interferencias radio, no imponer un códec multimedia común.'),('Que las aplicaciones compartan los mismos permisos de almacenamiento','Los permisos de archivos son una cuestión de software distinta.'),('Que ambos servicios deban facturarse mediante una misma suscripción','La coordinación radio no establece el modelo comercial de los servicios.')],
      'Las radios coubicadas pueden perjudicarse según sus bandas y condiciones. La especificación Bluetooth contempla mecanismos de coordinación con otras tecnologías, incluida la celular; no se pregunta por versiones ni por una interferencia universal.', 'Aplicación',url='https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-62/out/en/architecture%2C-change-history%2C-and-conventions/architecture.html')
    q('t31','WiFi frente a ANT/ANT+','83–85, 88',
      'Se conecta un pulsómetro que envía pequeñas medidas y se quiere maximizar la autonomía. ¿Qué propiedad de ANT/ANT+ lo hace adecuado frente a usar una red WiFi para ese sensor?',
      'Su diseño para sensores de bajo consumo y pequeños mensajes',
      [('Su obligación de transmitir archivos de vídeo de gran tamaño','ANT se orienta a redes de sensores de baja tasa, no a grandes flujos audiovisuales.'),('Su capacidad de comunicarse únicamente mediante cable','ANT es una tecnología inalámbrica.'),('Su independencia de cualquier perfil de datos en ANT+','ANT+ aporta perfiles compartidos; no prescinde de ellos.')],
      'ANT prioriza sensores de bajo consumo; ANT+ añade perfiles interoperables. WiFi resulta más adecuado para una red local con mayores volúmenes de información.', 'Aplicación',url='https://developer.garmin.com/ant-program/ant-ant-plus/')
    q('t31','Alcance de tecnologías inalámbricas','74–75, 83, 88–94',
      '¿Qué comparación de alcance entre un enlace WiFi y otro ANT+ está bien planteada?',
      'Debe considerar potencia, antenas, entorno y características de ambos equipos',
      [('El nombre ANT+ garantiza más distancia que cualquier equipo WiFi','No existe esa garantía universal por el nombre del protocolo.'),('Usar la misma banda garantiza exactamente la misma cobertura','Además de la frecuencia influyen potencia, antenas, sensibilidad y obstáculos.'),('WiFi tiene siempre alcance ilimitado si existe acceso a Internet','El acceso a Internet no elimina el alcance limitado del enlace radio local.')],
      'No se puede asignar una distancia universal a una tecnología sin indicar condiciones y hardware. ANT/ANT+ se orienta a sensores de bajo consumo y WiFi a redes locales; una mayor tasa nominal tampoco equivale por sí sola a más alcance.', 'Aplicación')
    q('t31','RFID y lectura NFC compatible','95, 100–105',
      'Una etiqueta RFID de alta frecuencia funciona a 13,56 MHz y usa un protocolo admitido por el lector NFC. Sin restricciones adicionales de acceso, ¿qué se puede afirmar?',
      'El lector NFC puede comunicarse con esa etiqueta compatible',
      [('Un lector NFC nunca puede leer ningún tipo de etiqueta RFID','NFC puede comunicarse con determinadas tarjetas y etiquetas RFID HF compatibles.'),('La etiqueta debe cambiar obligatoriamente a UHF para ser leída por NFC','NFC trabaja a 13,56 MHz; cambiar a UHF impediría ese enlace.'),('La coincidencia de frecuencia permitiría leer cualquier RFID aunque cambie el protocolo','Coincidir en frecuencia no sustituye la compatibilidad de protocolo.')],
      'RFID es una familia amplia. NFC admite ciertos protocolos HF a 13,56 MHz, por lo que la respuesta no es un «no» absoluto: importa qué etiqueta, protocolo y lector se utilizan.', 'Aplicación',url='https://nfc-forum.org/learn/nfc-technology/')
    q('t31','RFID de largo alcance y NFC','95, 97, 100–105',
      'Un inventario usa etiquetas RFID UHF y otro sistema usa NFC a 13,56 MHz. ¿Qué conclusión es correcta sobre el lector NFC por sí solo?',
      'No lee esas etiquetas UHF porque opera en otra banda y con otros protocolos',
      [('Puede leerlas porque todas las tecnologías RFID operan a 13,56 MHz','RFID incluye distintas bandas; UHF no es la banda HF de NFC.'),('Puede leerlas si se aumenta el tamaño del mensaje NFC','Cambiar el tamaño de los datos no convierte el receptor HF en uno UHF.'),('Puede leerlas únicamente porque las etiquetas son pasivas','Ser pasiva no implica compatibilidad de frecuencia o protocolo.')],
      'Un lector NFC no es un lector universal de RFID. El caso UHF queda fuera de su enlace de 13,56 MHz. Esto no contradice que pueda leer determinadas etiquetas RFID HF compatibles.', 'Aplicación')
    q('t31','Bandas RFID: LF, HF y UHF','98, 105',
      'En la clasificación RFID del temario, ¿a qué banda pertenece una etiqueta que trabaja aproximadamente a 125 kHz?',
      'LF (baja frecuencia)',
      [('HF (alta frecuencia)','La banda HF mostrada utiliza 13,56 MHz, no unos 125 kHz.'),('UHF (ultraalta frecuencia)','UHF corresponde a frecuencias mucho mayores, del orden de cientos de MHz.'),('Microondas','Los ejemplos de microondas de la tabla trabajan en GHz, no en kHz.')],
      'La figura sitúa aproximadamente 125–134 kHz en LF y 13,56 MHz en HF. Las distancias de las ilustraciones son ejemplos de sistemas y condiciones, no un alcance universal de cada banda.')
    q('t31','NFC y pequeños intercambios','100–103',
      'Se acerca un teléfono a una etiqueta NFC para abrir información de una exposición. ¿Qué uso es coherente con sus intercambios breves y de bajo volumen?',
      'Leer una dirección web y descargar después el contenido mediante otra conexión',
      [('Recibir toda una película de alta resolución como flujo continuo por la etiqueta','NFC no se orienta a transportar continuamente grandes volúmenes audiovisuales.'),('Mantener el vídeo de una videollamada a varios metros por el mismo enlace','El alcance y el tipo de tráfico no corresponden al uso NFC descrito.'),('Sustituir con esa etiqueta la cobertura de una red WiFi de todo el edificio','Una interacción de campo cercano no proporciona una red local de ese alcance.')],
      'Una etiqueta puede guardar una URL o datos pequeños. El contenido voluminoso se obtiene después por la red apropiada; no debe confundirse compartir un enlace con transmitir el archivo entero.', 'Aplicación')
    q('t31','Meta-wearable y tolerancia a fallos','42–44',
      'En una prenda con sensores interconectados se detecta un fallo del bus. ¿Qué comportamiento de tolerancia a fallos plantea el material?',
      'Reconocer el fallo y establecer un camino alternativo de comunicación',
      [('Dar por válidas las medidas sin comprobar que sigan llegando','Ignorar la pérdida de comunicación no proporciona tolerancia al fallo.'),('Exigir que el usuario sustituya manualmente todas las fibras tras cada medida','No es el funcionamiento de recuperación de la red que describe el tema.'),('Eliminar las interconexiones para que cada sensor deje de enviar datos','La solución intenta conservar la comunicación, no suprimirla.')],
      'El meta-wearable se plantea como una red distribuida en la prenda. Detectar el fallo y disponer de otra ruta evita depender de una única conexión.', 'Aplicación')

    q('t4','Qué es OpenAPI','What is OpenAPI?',
      '¿Qué es OpenAPI?',
      'Un estándar abierto para describir interfaces de APIs HTTP',
      [('Un servidor que ejecuta automáticamente cualquier API HTTP','OpenAPI describe una interfaz; no es por sí mismo el servidor que la implementa.'),('Un lenguaje de programación para implementar la lógica de una API','La descripción es independiente del lenguaje de implementación.'),('Un protocolo de transporte de audio y vídeo en tiempo real','No es un protocolo multimedia como RTP, sino un estándar de descripción de APIs.')],
      'OpenAPI Specification permite describir operaciones, parámetros, respuestas y otros aspectos de una API HTTP de forma comprensible para personas y herramientas. Es independiente del lenguaje de implementación y suele expresarse en JSON o YAML.',url='https://www.openapis.org/what-is-openapi')
