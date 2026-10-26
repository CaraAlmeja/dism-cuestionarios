"""65 ejercicios adicionales dentro del alcance vigente, conservando los 135 IDs previos."""
import re

def expand(q):
    def add(block,tag,pages,stem,correct,wrong,explanation,level='Aplicación',*,ordered=False,url=None):
        item=q(block,tag,pages,stem,correct,wrong,explanation,level,url=url)
        item['practice_batch']='2026-10-26'
        if ordered:
            def number(option):
                text=re.match(r'^[\d\s.,/]+',option['text']).group().replace(' ','').replace(',','.')
                if '/' in text:
                    a,b=text.split('/');return float(a)/float(b)
                return float(text)
            item['options'].sort(key=number)
            item['shuffle_options']=False
        return item

    # T1: cinco casos conceptuales, sin arquitectura interna ni Flutter.
    add('t1','Herramientas de la plataforma destino','23, 49',
        'Un equipo comparte C# con MAUI y quiere compilar para iOS. Según los requisitos del tema, ¿qué debe seguir teniendo en cuenta?',
        'La compilación para ese destino requiere un equipo Apple',
        [('Compartir el lenguaje elimina todos los requisitos de la plataforma destino','La reutilización de C# no elimina la cadena de herramientas exigida para compilar para iOS.'),('El proyecto se convierte en una PWA por utilizar C#','El lenguaje no determina que la distribución sea una aplicación web progresiva.'),('El mismo paquete Android puede instalarse directamente como app iOS','Compartir código no hace intercambiables los paquetes de sistemas distintos.')],
        'El temario indica que la compilación de aplicaciones iOS requiere un equipo Apple también con MAUI. Es un requisito de plataforma, distinto de compartir código.')
    add('t1','Acceso al dispositivo desde una app híbrida','15, 29, 34–37',
        'Una app Ionic obtiene la posición GPS mediante un plugin compatible y los permisos necesarios. ¿Qué conclusión es correcta?',
        'Una app híbrida puede utilizar funciones del dispositivo mediante integración nativa',
        [('Usar el GPS convierte automáticamente toda la interfaz en nativa','El uso de una API del dispositivo no cambia por sí solo la interfaz web.'),('Una app híbrida solo puede mostrar contenido y no puede usar sensores','Los plugins permiten integrar capacidades como GPS o cámara.'),('Obtener el GPS elimina la necesidad de comprobar permisos','La integración sigue sometida a los permisos y condiciones de la plataforma.')],
        'Híbrida no significa incapaz de usar hardware. El acceso suele apoyarse en plugins o integraciones nativas; su disponibilidad y los permisos siguen importando.')
    add('t1','Apariencia frente a tecnología de interfaz','16, 33, 39',
        'Una app usa componentes Ionic con apariencia Material Design en Android. ¿Basta esa apariencia para clasificar su interfaz como nativa?',
        'No; el aspecto visual no determina cómo se presenta la interfaz',
        [('Sí; cualquier botón con apariencia Material se implementa con un control nativo','Un componente web puede imitar o adaptar esa apariencia.'),('Sí; la adaptación visual obliga a sustituir JavaScript por Kotlin','Adaptar los estilos no exige cambiar al lenguaje específico de Android.'),('No; las aplicaciones nativas tienen que mostrar el mismo diseño en todos los sistemas','La uniformidad entre sistemas no es el criterio que define una interfaz nativa.')],
        'Ionic adapta el aspecto de sus componentes al sistema, pero la apariencia no equivale a utilizar controles nativos. Debe atenderse al enfoque de ejecución y presentación.')
    add('t1','Qué se comparte con Kotlin Multiplatform','60–61',
        'Un proyecto comparte reglas de negocio con Kotlin Multiplatform y conserva interfaces distintas en cada plataforma. ¿Encaja con el objetivo de KMP del tema?',
        'Sí; compartir la lógica no obliga a compartir toda la interfaz',
        [('No; KMP exige que todos los controles visuales sean idénticos','El tema explica que compartir la UI es una posibilidad, no una obligación.'),('No; si hay dos interfaces deja de existir código común','La lógica compartida puede coexistir con interfaces específicas.'),('Sí; porque las interfaces distintas tienen que ser páginas dentro de una WebView','Conservar interfaces específicas no implica convertirlas en interfaces web.')],
        'KMP permite compartir datos, red y reglas de negocio manteniendo interfaces por plataforma. La decisión de compartir también la UI es adicional.')
    add('t1','Límites del funcionamiento offline','42–43',
        'Una PWA conserva apuntes para leer sin conexión, pero consulta un servicio remoto para obtener nuevos resultados. Si se pierde la red, ¿qué cabe esperar?',
        'Puede mostrar lo guardado, mientras la consulta remota necesita conectividad',
        [('Todas las funciones remotas siguen operativas por ser una PWA','Soportar funciones offline no garantiza acceso a servicios remotos sin red.'),('El contenido ya guardado debe desaparecer cuando se pierde la red','La pérdida de conexión no obliga a eliminar el contenido local.'),('La app se transforma en una aplicación nativa al quedarse sin conexión','El estado de la red no cambia el enfoque tecnológico de la aplicación.')],
        'El soporte offline depende de qué recursos y datos estén disponibles localmente. No elimina la dependencia de red de operaciones que requieren un servidor.')

    # T2.1: más casos de arquitectura, servicios y calidad, además de un cálculo de arranque.
    add('t21','Origen del contenido y tipo de servicio','21–24',
        'Un servidor emite a una hora fija un vídeo grabado y todos los espectadores siguen el mismo instante del programa. ¿Qué describe mejor el servicio?',
        'Una emisión en directo con contenido previamente almacenado',
        [('Vídeo bajo demanda porque el material fue grabado antes','Que el material esté grabado no implica que cada usuario elija el inicio.'),('Descarga completa previa porque todos ven el mismo contenido','Una programación común no exige descargar el archivo entero antes de reproducir.'),('Un servicio que no puede utilizar streaming por no proceder de una cámara','El streaming también distribuye información previamente almacenada.')],
        'El tipo de servicio depende del control temporal que tiene el usuario, no solo de cuándo se capturó el contenido. El tema distingue emisiones live con información en vivo o almacenada.')
    add('t21','Pausa en el modelo live clásico','21–22',
        'En el modelo live del temario, sin DVR ni retroceso, un usuario pausa durante un minuto y después reanuda. ¿Qué ve?',
        'Lo que se está emitiendo en ese momento',
        [('El punto exacto que pausó, con un minuto de retraso','Ese comportamiento exigiría una función de retardo o recuperación que el caso excluye.'),('El programa desde el comienzo del archivo','El modelo descrito no ofrece inicio individual bajo demanda.'),('El minuto perdido acelerado antes de volver al directo','El modelo no incorpora una recuperación acelerada del intervalo perdido.')],
        'En el live clásico descrito, al reanudar se vuelve a la señal actual. El enunciado excluye DVR porque existen servicios reales de directo con otras funciones.')
    add('t21','Sesiones VOD independientes','25–26',
        'Tres usuarios ven la misma película en puntos distintos y pueden pausar por separado. ¿Qué plantea eso para un único flujo multicast idéntico a todos?',
        'No basta para ofrecer por sí solo esas posiciones independientes',
        [('Cada pausa individual se resuelve pausando ese flujo para todos','Pausarlo para todos no satisface la independencia pedida.'),('Multicast convierte automáticamente cada posición en un archivo diferente','La modalidad de envío no crea versiones temporales independientes.'),('Los tres usuarios deben recibir necesariamente el mismo fotograma','Eso impediría las posiciones diferentes que requiere el servicio.')],
        'El VOD del tema mantiene flujos e interacciones individuales. Un único flujo compartido con el mismo contenido temporal no proporciona por sí solo controles independientes.')
    add('t21','Canal de control y canal de medios','36',
        'En la arquitectura de streaming del tema, el cliente envía PAUSE y el servidor confirma la orden. ¿Qué canal permite ese intercambio?',
        'El canal de control bidireccional',
        [('El canal unidireccional que transporta el vídeo al cliente','El envío de medios hacia el cliente no es el intercambio de orden y respuesta.'),('El archivo comprimido del vídeo, que contiene las órdenes del usuario','Las interacciones se envían durante la sesión, no se introducen en el archivo del vídeo.'),('El búfer local, que envía por sí mismo todas las respuestas del servidor','El búfer almacena datos; no sustituye la comunicación de control.')],
        'El canal de control recibe interacciones y devuelve respuestas. El esquema lo distingue del canal de transporte de datos multimedia hacia el cliente.')
    add('t21','Proxy bajo demanda','40',
        'Varios clientes solicitan de nuevo segmentos que un proxy VOD acaba de guardar. ¿Qué puede hacer ese proxy?',
        'Servir los segmentos desde su caché si siguen disponibles',
        [('Volver a solicitarlos siempre al origen aunque sean reutilizables','Desaprovecha la función de caché descrita.'),('Obligar a todos los clientes a compartir los mismos controles de reproducción','Reutilizar segmentos no exige sincronizar todas las sesiones.'),('Cambiar la codificación del contenido a Unicode antes de enviarlo','Unicode representa texto; no es la operación que permite reutilizar vídeo en caché.')],
        'En VOD, el proxy puede almacenar información recientemente utilizada y reutilizarla en peticiones posteriores. Así evita volver a traer esos mismos datos del origen.')
    add('t21','Proxy en una emisión live','40',
        'Un servidor envía una copia de un directo a un proxy, que lo distribuye a muchos clientes. ¿Qué ventaja aporta respecto a enviar desde el origen una copia por cliente?',
        'Reduce los flujos que deben salir del servidor de origen',
        [('Elimina el tráfico entre el proxy y los espectadores','El proxy todavía tiene que entregar el directo a sus clientes.'),('Evita que los clientes necesiten recibir los datos del vídeo','Cada espectador sigue necesitando los datos para reproducir.'),('Convierte el directo en un servicio con inicio libre para cada usuario','Redistribuir el flujo no añade por sí solo funciones de VOD.')],
        'El origen puede enviar una sola copia al punto de distribución. La carga de atender las entregas posteriores se desplaza hacia el proxy; no desaparece el tráfico de los clientes.')
    add('t21','Orden y tiempo en RTP','42–43',
        'Un flujo multimedia recibe paquetes fuera de orden. ¿Para qué sirven los números de secuencia y marcas temporales de RTP?',
        'Ayudan a reconstruir el orden y el tiempo de presentación del flujo',
        [('Garantizan que la red entregará todos los paquetes sin pérdidas','Esos campos no convierten la red en un transporte sin pérdidas.'),('Sustituyen las órdenes de iniciar y pausar la sesión','El control de esas órdenes se asocia a RTSP, no a esos campos de RTP.'),('Eliminan la necesidad de interpretar el tiempo del contenido','Las marcas temporales aportan precisamente información de tiempo para su tratamiento.')],
        'RTP incorpora información para ordenar y temporizar el contenido. No garantiza por sí mismo entregar perfectamente todos los paquetes ni controla todas las acciones de sesión.')
    add('t21','Qué aporta el feedback RTCP','43–44',
        'El receptor informa mediante RTCP de pérdidas y retardo variable. ¿Qué uso puede dar la aplicación a ese feedback?',
        'Ajustar la transmisión según la calidad de recepción observada',
        [('Dar por recuperados automáticamente todos los paquetes perdidos','El informe de pérdidas no reconstruye por sí solo los paquetes.'),('Sustituir el audio y el vídeo por los informes de control','RTCP complementa al transporte de medios; no convierte sus informes en el contenido.'),('Enviar la orden de pausa como si RTCP fuera el mando RTSP','Confunde supervisión de calidad con control de reproducción.')],
        'RTCP aporta estadísticas para que la aplicación tome decisiones de adaptación. Informar de una pérdida no equivale a corregirla automáticamente.')
    add('t21','Órdenes de sesión RTSP','46–47',
        'El reproductor quiere finalizar una sesión RTSP y liberar su estado, en lugar de pausarla temporalmente. ¿Qué orden corresponde?',
        'TEARDOWN',
        [('PAUSE','PAUSE detiene temporalmente la reproducción, conservando la sesión.'),('PLAY','PLAY inicia o reanuda la reproducción.'),('SETUP','SETUP prepara la sesión y sus recursos, no la finaliza.')],
        'En el flujo del tema, TEARDOWN termina la sesión. Se diferencia de PAUSE, que permite conservarla para reanudar.', 'Comprensión')
    add('t21','Componentes del cliente de streaming','51',
        'Ya han llegado los datos al cliente y deben mostrarse respetando su temporización. ¿Qué componente del esquema se encarga de reproducirlos?',
        'Presentación',
        [('Recepción','Se encarga de recibir la información solicitada, no de su presentación temporizada.'),('Búfer','Mantiene una reserva temporal; la presentación se encarga de reproducirla según su temporización.'),('Sistema de almacenamiento del servidor','Conserva contenido en el origen; no presenta el vídeo en el dispositivo del usuario.')],
        'El cliente distingue recepción, presentación y búfer. Presentación reproduce la información de forma temporizada y ofrece la interacción al usuario.', 'Comprensión')
    add('t21','Espera inicial de búfer','52–53',
        'Antes de iniciar la reproducción, un cliente quiere acumular 12 Mbit y recibe a 6 Mbit/s constantes. Sin consumo durante esa espera, ¿cuánto tarda en reunir la reserva?',
        '2 segundos',
        [('1 segundo','En un segundo solo recibe 6 Mbit, la mitad de la reserva solicitada.'),('3 segundos','Correspondería a recibir 18 Mbit con la tasa indicada.'),('6 segundos','Confunde la tasa numérica con el tiempo que resulta de dividir reserva entre tasa.')],
        'El tiempo es reserva/tasa = 12/6 = 2 s. Aquí todavía no hay consumo de reproducción; no se resta una tasa de salida.', 'Cálculo',ordered=True)
    add('t21','Entrega a tiempo frente a entrega tardía','14, 42, 53',
        'En una comunicación audiovisual interactiva, un paquete llega íntegro después del instante en que debía reproducirse. ¿Qué limitación ilustra?',
        'Entregar todos los datos no basta si llegan fuera del plazo útil',
        [('La ausencia de errores de bits garantiza que el retardo deja de importar','La información correcta puede resultar demasiado tardía para una interacción fluida.'),('Un búfer más grande garantiza que el retardo percibido sea cero','Aumentar la reserva puede mejorar estabilidad, pero no elimina el retraso y puede añadir espera.'),('Basta aumentar el caudal máximo anunciado sin atender al retardo real','La capacidad de transferencia y el tiempo de entrega son aspectos distintos.')],
        'Los sistemas multimedia temporizados deben atender a cuándo llegan los datos, además de a su integridad. En servicios interactivos, esperar indefinidamente también perjudica la calidad.')
    add('t21','Netflix: informes de estado de OCA','61',
        'Según el flujo Netflix del PDF, ¿para qué comunican los OCA su carga y los vídeos disponibles al servicio de control de caché?',
        'Para que el control conozca el estado y contenido de los servidores de entrega',
        [('Para que el OCA cobre directamente el plan de cada espectador','La facturación pertenece al backend de servicio, no a esos informes.'),('Para enviar cada película entera dentro de los informes de salud','Los informes describen estado; no sustituyen la entrega audiovisual al cliente.'),('Para convertir al cliente en un servidor OCA de la misma red','Informar sobre el OCA no cambia el papel del reproductor del usuario.')],
        'Los informes permiten conocer disponibilidad de contenidos, carga y condiciones relevantes de los OCA. Esa información ayuda a organizar la entrega.')
    add('t21','Netflix: elección del servidor de entrega','64–66',
        'El cliente recibe una lista de OCA apropiados para un vídeo. En el esquema del PDF, ¿qué criterio utiliza después para elegir uno?',
        'Prueba las conexiones y elige una entrega rápida y fiable',
        [('Elige siempre el geográficamente más cercano sin medir la conexión','La distancia geográfica no basta para medir el comportamiento de la ruta de red.'),('Descarta los OCA y descarga obligatoriamente del servicio de identidad','El flujo del tema entrega el vídeo desde un OCA, no desde el servicio de identidad.'),('Selecciona solo por la resolución de pantalla, ignorando la conexión','Las condiciones del enlace también importan para escoger una entrega adecuada.')],
        'Tras obtener candidatos, el cliente prueba las conexiones y escoge un OCA adecuado para solicitar el vídeo. La cercanía geográfica o la pantalla por sí solas no sustituyen esa evaluación.')
    add('t21','Netflix y representaciones de vídeo','57–58, 67',
        '¿Qué relación tiene la transcodificación con ofrecer un vídeo de Netflix en varias calidades?',
        'Permite preparar representaciones que el cliente puede elegir según sus condiciones',
        [('Obliga a todos los clientes a reproducir siempre la misma representación','Ofrecer varias calidades permite adaptar la entrega a clientes y conexiones distintos.'),('Sustituye el servicio de identidad y autorización de la cuenta','Preparar vídeo y comprobar permisos son responsabilidades distintas.'),('Convierte un vídeo con pérdida en una copia idéntica de todo detalle original','La transcodificación no recupera información que ya se descartó de forma irreversible.')],
        'El backend prepara contenido y Open Connect entrega archivos codificados en distintas calidades. Esa variedad hace posible adaptar la reproducción; no reemplaza la autorización.')

    _storage(add)
    _devices(add)
    _cellular(add)

def _storage(add):
    add('t22','Capacidad de un espejo con discos distintos','6',
        'Se crea un RAID 1 con un disco de 2 TB y otro de 3 TB. Sin metadatos ni configuraciones especiales, ¿qué capacidad de datos ofrece el espejo?',
        '2 TB',
        [('3 TB','El disco menor no puede contener una copia completa de 3 TB.'),('4 TB','Duplicar la capacidad del disco menor cuenta dos veces los mismos datos.'),('5 TB','Suma las capacidades físicas como si los discos almacenaran datos distintos.')],
        'El espejo conserva copias de los mismos datos. Su capacidad útil queda limitada por el menor disco: 2 TB.', 'Cálculo',ordered=True)
    add('t22','Número mínimo de discos RAID 5','7–9',
        '¿Cuál es el mínimo de discos que necesita un RAID 5 según el temario?',
        '3 discos',
        [('2 discos','Dos unidades permiten otros esquemas, pero RAID 5 requiere al menos tres.'),('4 discos','Cuatro es un tamaño posible, pero no el mínimo de RAID 5.'),('5 discos','El número 5 designa el nivel RAID, no la cantidad mínima de discos.')],
        'RAID 5 necesita como mínimo tres discos para distribuir datos y paridad. El número del nivel no indica cuántos discos deben instalarse.', 'Comprensión',ordered=True)
    add('t22','Reconstrucción del bloque de paridad','9, 11',
        'En una franja RAID 5 sobreviven D0 = 0101, D1 = 0011 y D2 = 1000. Falta el bloque de paridad P. ¿Qué valor se reconstruye?',
        '1110',
        [('0110','Es solo D0 XOR D1; falta incorporar el tercer bloque.'),('1011','Es D1 XOR D2, sin incorporar D0.'),('1111','Combina los bits mediante OR, en lugar de calcular el XOR de los tres bloques.')],
        'P = 0101 XOR 0011 XOR 1000 = 0110 XOR 1000 = 1110. Perder el bloque de paridad de una franja no obliga a perder los datos que siguen disponibles.', 'Cálculo',ordered=True)
    add('t22','Cambios que se cancelan en la paridad','9–11',
        'Una franja tiene D0 = 0000 y D1 = 0000, con P = 0000. Ambos datos cambian a 0001. ¿Cuál es la nueva paridad XOR?',
        '0000',
        [('0001','Equivale a aplicar solo uno de los dos cambios; los dos bits a 1 se cancelan mediante XOR.'),('0010','Trata los cambios como una suma binaria con acarreo, no como XOR.'),('0011','Activa posiciones que no aparecen en el XOR de los datos nuevos.')],
        '0001 XOR 0001 = 0000. Que la paridad no cambie no significa que los datos sean idénticos: la paridad no es una copia completa de ellos.', 'Cálculo',ordered=True)
    add('t22','Datos necesarios para una escritura parcial','10–11',
        'Para cambiar un único bloque mediante Read-Modify-Write en RAID 5, sin caché previa, ¿qué información antigua se lee?',
        'El bloque de datos que cambia y la paridad de su franja',
        [('Solo el bloque nuevo, porque la paridad anterior no interviene','Para actualizar por XOR la paridad se necesitan las contribuciones antiguas.'),('Todos los bloques de todas las franjas del conjunto','El procedimiento no requiere releer todo el volumen.'),('Solo la paridad, porque el dato antiguo se deduce del dato nuevo','No puede deducirse en general el valor antiguo a partir del nuevo.')],
        'La actualización utiliza P nueva = P antigua XOR dato antiguo XOR dato nuevo. En ese procedimiento se leen dato y paridad antiguos y luego se escriben los nuevos.')
    add('t22','Capacidad útil RAID 6','14–15',
        'Un RAID 6 utiliza seis discos iguales de 4 TB. Sin contar metadatos, ¿qué capacidad útil queda al reservar el equivalente de dos discos para redundancia?',
        '16 TB',
        [('8 TB','Descuenta cuatro discos equivalentes, más redundancia de la indicada.'),('20 TB','Descuenta solo un disco, como en el cálculo de capacidad de RAID 5.'),('24 TB','Suma toda la capacidad física sin descontar la doble paridad.')],
        'La capacidad es (6 − 2)×4 TB = 16 TB. El equivalente de dos discos corresponde a la redundancia de RAID 6.', 'Cálculo',ordered=True)
    add('t22','Patrones de fallo en RAID 10','16',
        'Un RAID 10 se forma con parejas espejo A/B y C/D. Fallan A y B; C y D siguen operativos. ¿Puede el conjunto conservar todos sus datos?',
        'No, porque se han perdido las dos copias de una misma pareja',
        [('Sí, porque RAID 10 soporta cualquier combinación de dos fallos','La tolerancia depende de qué discos fallen, no solo de su número.'),('Sí, porque la pareja C/D contiene también un espejo completo de A/B','Las parejas contienen partes distintas del conjunto; cada una refleja sus propios datos.'),('Sí, porque se reconstruye A/B con la paridad doble de C/D','RAID 10 no utiliza la doble paridad propia de RAID 6.')],
        'La división se hace entre parejas reflejadas. Si desaparece una pareja completa, falta una parte de los datos aunque sobrevivan los discos de la otra.')
    add('t22','Unicode fuera del BMP','23',
        'Para un punto de código Unicode suplementario, fuera del BMP, ¿qué tamaños indica el tema para UTF-8, UTF-16 y UTF-32?',
        'UTF-8: 4 bytes; UTF-16: 4 bytes; UTF-32: 4 bytes',
        [('UTF-8: 4 bytes; UTF-16: 2 bytes; UTF-32: 4 bytes','UTF-16 necesita un par de unidades de 16 bits para ese punto de código.'),('UTF-8: 1 byte; UTF-16: 2 bytes; UTF-32: 4 bytes','Los tamaños de uno y dos bytes no bastan para el punto suplementario especificado.'),('UTF-8: 4 bytes; UTF-16: 4 bytes; UTF-32: 8 bytes','UTF-32 mantiene una unidad de 32 bits por punto de código, no dos.')],
        'UTF-8 utiliza cuatro bytes para estos puntos de código; UTF-16 usa un par de unidades de 16 bits, también cuatro bytes; UTF-32 emplea cuatro bytes. Se pregunta por punto de código, no por carácter visual.', 'Comprensión')
    add('t22','Códigos de Huffman','27',
        '¿Qué idea utiliza Huffman para reducir la longitud media de una representación simbólica?',
        'Dar códigos más cortos a los símbolos más frecuentes',
        [('Usar una longitud fija para todos sin considerar sus frecuencias','No aprovecha la distribución de probabilidad para variar el coste de cada símbolo.'),('Dar los códigos más largos a los símbolos más frecuentes','Eso aumenta el coste medio de los símbolos que más aparecen.'),('Eliminar los símbolos menos frecuentes de la reconstrucción','Descartar símbolos perdería información; no es el mecanismo de Huffman.')],
        'La asignación de longitudes tiene en cuenta las frecuencias de los símbolos. La idea es reducir el coste medio conservando una representación decodificable.', 'Comprensión')
    add('t22','Compresión mediante diccionario LZW','28, 34',
        '¿Qué mecanismo caracteriza a LZW en el temario?',
        'Sustituir cadenas de símbolos por códigos de un diccionario',
        [('Descartar píxeles de color para que la imagen sea más pequeña','Eso describe pérdida de información, no la sustitución de cadenas de LZW.'),('Crear un código nuevo para cada aparición sin reutilizar entradas','El diccionario permite reutilizar códigos de cadenas; renunciar a ello no explica la compresión descrita.'),('Asignar a cada símbolo un código según un árbol de probabilidades','Esa descripción corresponde a la codificación simbólica de Huffman, no al diccionario de cadenas de LZW.')],
        'LZW mantiene una tabla de cadenas y puede sustituir una cadena por su código. El tema lo relaciona con GIF y lo distingue de los códigos de símbolos individuales.', 'Comprensión')
    add('t22','Adaptación por software en un procesador','47–48, 63',
        'Un procesador conserva sus circuitos y cambia de algoritmo ejecutando otro programa. ¿Qué familia describe esa forma de adaptación?',
        'Una arquitectura programable',
        [('Un circuito ASIC que cambia físicamente al cargar cada archivo','Cargar otro programa no modifica físicamente un ASIC.'),('Una FPGA que necesariamente cambia sus interconexiones con cada dato','No se ha descrito una reconfiguración de hardware ni un cambio por cada dato.'),('Un sistema de almacenamiento que alterna el nivel RAID','Cambiar el programa del procesador no equivale a reorganizar discos.')],
        'El comportamiento se adapta mediante instrucciones sobre el hardware disponible. Esto se distingue de reconfigurar la lógica de una FPGA o de utilizar un circuito dedicado fijo.')
    add('t22','Elección de una arquitectura dedicada','61, 63',
        'Se fabricarán muchas unidades para una tarea estable y se priorizan rendimiento y bajo consumo frente a flexibilidad. ¿Qué opción destaca el tema?',
        'Un ASIC dedicado a la tarea',
        [('Una CPU elegida únicamente por poder ejecutar cualquier programa','La flexibilidad general no es la prioridad indicada en el caso.'),('Una FPGA elegida porque su principal ventaja es un circuito que nunca se puede cambiar','La ventaja distintiva de una FPGA es precisamente su reconfigurabilidad.'),('Un procesador de propósito general por eliminar todo coste de ejecución','Ejecutar programas generales no elimina costes de cómputo ni consumo.')],
        'El ASIC puede proporcionar gran eficiencia para una tarea fija, a costa de diseño costoso y poca flexibilidad. El volumen de fabricación ayuda a justificar ese coste.')
    add('t22','Ejes distintos de clasificación','47, 61–62',
        'Un sistema combina varios chips ASIC de función fija. ¿Qué clasificación encaja con los dos ejes usados en el tema?',
        'Dedicado y modular',
        [('Reconfigurable y modular por el hecho de tener varios chips','Modular describe varios chips; no implica que su lógica sea reconfigurable.'),('Dedicado y monolítico por tratarse de ASIC','Ser ASIC no obliga a integrar todo el sistema en un único chip.'),('Programable de propósito general y monolítico','El caso especifica varios chips de función fija, no un único procesador general.')],
        'Dedicado/reconfigurable/programable y monolítico/modular son clasificaciones diferentes. Varios chips de función fija forman una realización dedicada modular.')
    add('t22','Localidad del código frente a los datos','44–46',
        'Un bucle pequeño se ejecuta miles de veces mientras procesa datos nuevos que apenas relee. ¿Qué combinación es coherente?',
        'Alta reutilización temporal del código y baja de los datos del flujo',
        [('Baja reutilización del código porque cada dato de entrada es nuevo','Que cambien los datos no impide repetir las mismas instrucciones del bucle.'),('Alta reutilización temporal de todos los datos porque se repite el bucle','Repetir instrucciones no significa volver a usar los mismos datos.'),('Imposibilidad de aprovechar caché para las instrucciones del bucle','Un código pequeño y repetido puede beneficiarse de permanecer accesible en memoria rápida.')],
        'Hay que distinguir qué se reutiliza. El código puede ejecutarse repetidamente y tener alta localidad temporal, mientras los datos entran como un flujo con poca reutilización.')
    add('t22','SIMD y VLIW','48, 56',
        '¿Qué asociación de tipos de paralelismo recoge el temario?',
        'SIMD: paralelismo de datos; VLIW: paralelismo de instrucciones',
        [('SIMD: paralelismo de instrucciones; VLIW: paralelismo de datos','Invierte los tipos de paralelismo asociados a ambas técnicas.'),('SIMD y VLIW: únicamente paralelismo sobre los datos','VLIW se asocia al paralelismo a nivel de instrucciones.'),('SIMD y VLIW: únicamente paralelismo de instrucciones','SIMD se asocia al procesamiento paralelo de varios datos.')],
        'SIMD aplica operaciones a varios datos y VLIW explota paralelismo a nivel de instrucciones. El tema los presenta entre las técnicas para acelerar procesamiento multimedia.', 'Comprensión')

def _devices(add):
    add('t31','Trabajo de CPU y GPU en el móvil','4',
        'Dentro de un SoC, ¿qué reparto general distingue a CPU y GPU?',
        'La CPU ejecuta lógica general y la GPU acelera tareas gráficas',
        [('La CPU conserva archivos apagado y la GPU mide movimiento','Confunde procesadores con almacenamiento no volátil y sensores.'),('La GPU realiza la función de batería y la CPU capta la luz ambiental','La alimentación y la medición de luz no son esas funciones de procesamiento.'),('CPU y GPU son dos nombres de la misma memoria flash','Son bloques de procesamiento distintos del almacenamiento flash.')],
        'El SoC integra bloques con funciones especializadas. La CPU ejecuta tareas generales y la GPU acelera trabajo gráfico; no deben confundirse con memoria, sensores o alimentación.', 'Comprensión')
    add('t31','Sensores de movimiento','4',
        '¿Qué pareja relaciona correctamente dos sensores de un smartphone con su medida física?',
        'Acelerómetro: aceleración; giroscopio: velocidad de rotación',
        [('Acelerómetro: luz ambiental; giroscopio: presión atmosférica','Esas medidas pertenecen a otros sensores, no a los dos de movimiento indicados.'),('Acelerómetro: velocidad de rotación; giroscopio: aceleración','Intercambia las magnitudes medidas por ambos.'),('Acelerómetro: identificación NFC; giroscopio: potencia WiFi','Identificación y conectividad radio no son las medidas físicas de estos sensores.')],
        'El acelerómetro mide aceleración y el giroscopio velocidad angular. Sus datos pueden combinarse para interpretar movimiento; no son por sí solos un receptor de posición GPS.', 'Comprensión',url='https://developer.android.com/develop/sensors-and-location/sensors/sensors_motion')
    add('t31','Sensores y brillo de pantalla','4',
        'El teléfono ajusta automáticamente el brillo al pasar de una habitación oscura al exterior iluminado. ¿Qué sensor aporta directamente esa medida del entorno?',
        'El sensor de luz ambiental',
        [('El giroscopio','Mide rotación, no iluminación.'),('El barómetro','Mide presión ambiental, no luz.'),('El acelerómetro','Mide aceleración, no iluminación.')],
        'El sensor de luz mide la iluminación ambiental y puede utilizarse para regular el brillo. El sistema necesita disponer del sensor y de una política de control que use su lectura.',url='https://developer.android.com/develop/sensors-and-location/sensors/sensors_environment')
    add('t31','Contaminación en pantallas SAW','55–56',
        'Un quiosco SAW sigue mostrando bien la imagen, pero el toque empeora al acumularse suciedad o agua en la superficie. ¿Qué explica el problema?',
        'La suciedad altera las ondas acústicas de detección',
        [('La suciedad impide el cambio de capacitancia de la superficie','La alteración de capacitancia corresponde a otro principio de detección, no a SAW.'),('La presión ha unido las dos capas resistivas del panel','Eso describe una pantalla resistiva, no el sistema acústico especificado.'),('La cámara de seguimiento ha perdido la sombra del dedo','La localización mediante cámaras pertenece a imagen óptica, no a SAW.')],
        'SAW utiliza ondas acústicas sobre la superficie. El material señala que polvo, agua y otros contaminantes pueden interferir en su propagación y en la detección del toque.')
    add('t31','Pantalla táctil por haces interrumpidos','55, 57',
        'Un marco tiene emisores y receptores enfrentados en ejes horizontal y vertical. Un objeto corta haces de luz y se localiza su posición, sin usar cámaras. ¿Qué tecnología describe?',
        'Pantalla táctil infrarroja',
        [('Pantalla táctil SAW','SAW detecta cambios en ondas acústicas, no interrupción de haces luminosos.'),('Capacitiva de superficie','Detecta una alteración eléctrica en la superficie, no haces interrumpidos.'),('Resistiva','Detecta contacto entre capas conductoras al presionarlas.')],
        'La retícula de haces infrarrojos permite localizar el cruce que interrumpe el objeto. No debe confundirse con la triangulación de sombras mediante cámaras.')
    add('t31','Contacto en capacitiva de superficie','61–62',
        'Una pantalla capacitiva de superficie convencional exige un dedo o un dispositivo conductor adecuado. ¿Por qué un puntero completamente aislante puede no activarla?',
        'No produce el acoplamiento eléctrico requerido por ese sensor',
        [('Le falta presión para juntar las dos capas conductoras','Ese es el principio de una resistiva, no el del sensor capacitivo del caso.'),('No emite las ondas acústicas que la pantalla necesita recibir','El puntero no debe actuar como emisor acústico de una SAW.'),('No tiene una cámara para triangular su propia sombra','La triangulación óptica no es la condición de funcionamiento de esa capacitiva.')],
        'La capacitiva de superficie detecta cambios de capacitancia mediante interacción conductiva. El enunciado acota el sensor convencional; no generaliza a todas las soluciones de guantes o lápices activos.')
    add('t31','Matriz activa en AMOLED','71',
        '¿Qué significa que AMOLED sea una variante OLED de matriz activa?',
        'Los píxeles se controlan mediante una matriz activa de transistores TFT',
        [('Añade una retroiluminación LCD que sustituye la emisión orgánica','AMOLED sigue siendo autoemisiva; no se convierte en LCD por utilizar TFT.'),('Detecta el toque mediante una matriz de haces infrarrojos','La forma de detectar el toque es independiente de esa matriz de control del display.'),('Limita todos los píxeles a permanecer encendidos al mostrar negro','Los píxeles OLED pueden apagarse para representar negro.')],
        'La matriz activa controla eléctricamente los píxeles OLED. TFT no significa por sí mismo que un panel sea LCD: también participa en el control de AMOLED.', 'Comprensión')
    add('t31','Mini-LED frente a tecnología autoemisiva','67, 73',
        '¿Qué describe correctamente Mini-LED en el panorama de displays del tema?',
        'Un LCD con retroiluminación formada por muchos LED pequeños',
        [('Un panel en el que cada píxel es un LED microscópico autoemisivo','Eso describe MicroLED, no la retroiluminación Mini-LED de un LCD.'),('Una OLED cuya matriz activa se elimina por completo','Mini-LED no es una variante definida por quitar la matriz de una OLED.'),('Una capa de tinta electrónica que solo refleja luz ambiental','No corresponde a un LCD con iluminación trasera.')],
        'Mini-LED mejora la retroiluminación de un LCD y permite control local de zonas. MicroLED y OLED se basan en emisión por píxel; son conceptos distintos.', 'Comprensión')
    add('t31','Perfiles compatibles en ANT+','84–85',
        'Un receptor ANT+ solo interpreta el perfil de cadencia y un sensor emite el de frecuencia cardíaca. ¿Basta que ambos sean ANT+ para que ese receptor interprete esa medida?',
        'No; debe admitir el perfil correspondiente a los datos enviados',
        [('Sí; todos los perfiles ANT+ representan exactamente la misma magnitud','Los perfiles definen información diferente según el uso.'),('Sí; compartir la tecnología convierte cadencia en frecuencia cardíaca','La comunicación no transforma una magnitud física en otra.'),('No; ANT+ solo permite conectar productos de una misma marca','La interoperabilidad permite productos de marcas distintas con perfiles compatibles.')],
        'ANT+ aporta perfiles de dispositivo. La compatibilidad depende de que las partes manejen el perfil adecuado, no solo de usar el protocolo base o mostrar el mismo nombre comercial.')
    add('t31','Zigbee y su base de comunicación','86',
        '¿Qué relación tiene Zigbee con IEEE 802.15.4 según el material?',
        'Define protocolos de alto nivel apoyados en esa base de comunicación de bajo consumo',
        [('Es el nombre de un formato de vídeo comprimido que se transmite por esa red','Zigbee describe comunicaciones, no un códec audiovisual.'),('Sustituye el enlace inalámbrico por un cable para cada sensor','El caso trata redes inalámbricas de área personal.'),('Es una denominación de WiFi que exige el mismo protocolo en los terminales','Zigbee no es una versión ni un nombre alternativo de WiFi.')],
        'Zigbee utiliza IEEE 802.15.4 como base y añade protocolos orientados a aplicaciones de baja tasa y bajo consumo, como domótica. No se pregunta por tasas ni versiones.', 'Comprensión')
    add('t31','Modos NFC en dos situaciones','101–103',
        'Un móvil lee una URL de una etiqueta y, en otra ocasión, se presenta como tarjeta ante un terminal de acceso. ¿Qué modos corresponden, en ese orden?',
        'Lectura/escritura y emulación de tarjeta',
        [('Emulación de tarjeta y lectura/escritura','Invierte quién actúa como lector y quién se presenta como tarjeta.'),('Punto a punto y lectura/escritura','Leer una etiqueta no es necesariamente intercambio entre dos pares; en el segundo caso el móvil actúa como tarjeta.'),('Lectura/escritura y punto a punto','El segundo caso describe emulación ante un lector, no intercambio entre pares.')],
        'En el primer caso el móvil actúa como lector de la etiqueta. En el segundo emula una tarjeta sin contacto ante un lector de acceso.')
    add('t31','Elementos de una etiqueta RFID','95',
        '¿Qué combinación forma el transpondedor o etiqueta RFID del esquema básico del tema?',
        'Un microchip unido a una antena',
        [('Un lector conectado a la base de datos del inventario','Eso describe parte de la infraestructura que consulta etiquetas, no la etiqueta.'),('Una batería obligatoria y un punto de acceso WiFi','Las etiquetas RFID no requieren ser equipos WiFi ni llevar necesariamente batería.'),('Una cámara y un código óptico impreso','La identificación por radio del caso no se basa en leer un código con cámara.')],
        'La etiqueta combina chip y antena. El lector comunica con ella y convierte la respuesta en información utilizable por otros equipos.', 'Comprensión')
    add('t31','Puntos de acceso y terminales WiFi','92–93',
        'Se necesita generar una red WiFi a la que se conecten los teléfonos. ¿Qué dispositivo del tema desempeña directamente esa función?',
        'Un punto de acceso inalámbrico',
        [('Una tarjeta WiFi instalada solo como cliente receptor','El terminal cliente se conecta a una red; no es el punto de acceso descrito.'),('Un switch Ethernet sin interfaz radio','Sin radio no genera por sí mismo la red inalámbrica pedida.'),('Un lector RFID de inventario','La lectura de etiquetas RFID no proporciona una red WiFi a los teléfonos.')],
        'El punto de acceso genera la red inalámbrica. Un router doméstico puede integrar esa función, pero el caso distingue la función AP de otros componentes.')
    add('t31','Interfaz común en prendas inteligentes','46',
        '¿Qué ventaja busca una interfaz común para conectar sensores y procesadores de un meta-wearable?',
        'Facilitar módulos intercambiables y reducir soluciones específicas para cada fabricante',
        [('Eliminar la necesidad de interpretar las señales captadas por los sensores','Una interfaz común no sustituye el procesamiento de señal.'),('Hacer que todas las prendas midan obligatoriamente una sola magnitud','La normalización de conexión no reduce todas las funciones a una única medida.'),('Garantizar que ningún componente necesitará alimentación','Los módulos activos pueden seguir necesitando energía aunque la conexión sea común.')],
        'La interfaz común facilita intercambiar módulos y utilizar dispositivos más generales. El material relaciona esa compatibilidad con menor coste de integración.')
    add('t31','Niveles de integración textil','42–43',
        'Una banda lleva un módulo extraíble sobre la prenda; otra prenda usa fibras que hacen de sensor y cableado. ¿Qué niveles de integración representan, respectivamente?',
        'Electrónica añadida y tela como dispositivo',
        [('Tela como dispositivo y electrónica añadida','Invierte el módulo colocado sobre la prenda y la función electrónica de sus fibras.'),('Electrónica integrada y electrónica añadida','La segunda prenda no se limita a sostener un módulo externo.'),('Electrónica añadida y sensores únicamente en un módulo externo','La segunda prenda utiliza la propia tela, no solo un módulo externo.')],
        'El tema distingue módulos añadidos, electrónica integrada y la propia tela como dispositivo. En el segundo ejemplo las fibras realizan funciones de sensor y de interconexión.')

def _cellular(add):
    add('t32','Conmutación en la red celular clásica','7, 35',
        'En la arquitectura celular clásica, ¿qué elemento conmuta llamadas y conecta la red móvil con otras redes?',
        'MSC, central de conmutación móvil',
        [('BTS, estación radio de una celda','La BTS proporciona el enlace radio con los terminales, no la función central de conmutación del caso.'),('BSC, controlador de varias estaciones base','El BSC controla BTS y traspasos de su dominio; la conmutación y conexión de nivel superior corresponden al MSC.'),('MS, terminal del usuario','El terminal no realiza la conmutación central de toda la red.')],
        'El esquema clásico distingue terminales, estaciones base, controladores y central MSC. El MSC conmuta y conecta con otras redes; no se pregunta por generaciones.', 'Comprensión')
    add('t32','Canales de control frente a tráfico','16, 20',
        'Un clúster dispone de 420 canales dúplex en total; 70 se reservan a control. Las siete celdas reparten uniformemente los restantes para tráfico. ¿Cuántos canales de tráfico recibe cada celda?',
        '50 canales',
        [('60 canales','Divide 420 entre siete sin descontar los reservados para control.'),('70 canales','Confunde la reserva total de control con los canales de tráfico por celda.'),('350 canales','Es el total de tráfico del clúster, antes de repartirlo entre celdas.')],
        'Quedan 420 − 70 = 350 canales de tráfico. Al dividirlos entre siete celdas se obtienen 50 por celda.', 'Cálculo',ordered=True)
    add('t32','Geometría del clúster','14–15',
        'Se planifica un clúster hexagonal con i = 2 y j = 2. Usando N = i² + j² + i·j, ¿cuántas celdas tiene?',
        '12 celdas',
        [('4 celdas','Suma i+j en vez de aplicar la fórmula.'),('8 celdas','Suma los dos cuadrados, pero omite i·j.'),('16 celdas','Calcula (i+j)² e incluye dos veces el término cruzado.')],
        'N = 2² + 2² + 2×2 = 4 + 4 + 4 = 12. El producto cruzado aparece una vez.', 'Cálculo',ordered=True)
    add('t32','Radio y densidad de celdas','29',
        'Se reduce a la mitad el radio de celdas de la misma forma para cubrir una superficie fija. Sin contar efectos de borde, ¿por qué factor aumenta el número necesario de celdas?',
        '4',
        [('2','El área cambia con el cuadrado de la escala lineal, no solo con el radio.'),('8','Introduce un factor cúbico que no corresponde a una superficie.'),('16','Confunde la relación de áreas con otro posible escalado, como el de potencia con exponente cuatro.')],
        'El área de cada celda queda en (1/2)² = 1/4. Para cubrir el mismo territorio hacen falta cuatro veces más celdas.', 'Cálculo',ordered=True)
    add('t32','Obtener N a partir de la distancia cocanal','21, 25',
        'Una planificación satisface D/R = 6. En el modelo D/R = √(3N), ¿qué tamaño de clúster N corresponde?',
        '12',
        [('6','Repite D/R sin despejar N.'),('18','Divide 6² entre dos en lugar de entre tres.'),('36','Eleva al cuadrado D/R, pero omite dividir entre tres.')],
        '(D/R)² = 3N. Por tanto N = 6²/3 = 36/3 = 12.', 'Cálculo',ordered=True)
    add('t32','Potencia e interferencia cocanal','21, 25',
        'En el modelo de estaciones con la misma potencia, se duplica la potencia de todas las BS, incluida la útil y las interferentes. Sin cambiar geometría ni pérdidas, ¿qué sucede con S/I?',
        'Se mantiene, porque señal e interferencia se multiplican por el mismo factor',
        [('Se duplica porque solo importa el aumento de la señal útil','La interferencia también aumenta en las condiciones dadas.'),('Se reduce a la mitad aunque todas las potencias escalen igual','El mismo factor aparece tanto en numerador como en denominador y se cancela.'),('La interferencia cocanal desaparece por aumentar la potencia','Subir todas las potencias no elimina que las celdas reutilicen los mismos canales.')],
        'La relación se mantiene: 2S/(2I) = S/I. La mejora debe buscarse en factores como separación y planificación, no en subir igual la potencia de todos.')
    add('t32','Pérdida de propagación con la distancia','23',
        'La potencia recibida sigue P ∝ 1/d⁴. Si la distancia se duplica, ¿qué fracción de potencia se recibe respecto a antes?',
        '1/16',
        [('1/8','Aplica un exponente tres en lugar de cuatro.'),('1/4','Aplica un exponente dos en lugar de cuatro.'),('1/2','Trata la caída como inversamente proporcional solo a la distancia.')],
        'La nueva potencia es proporcional a 1/(2d)⁴ = 1/(16d⁴). Se recibe una dieciseisava parte.', 'Cálculo',ordered=True)
    add('t32','Interpretación de una mejora en dB','24',
        'Una relación de potencias S/I mejora aproximadamente 3 dB. ¿Qué cambio lineal representa esa mejora?',
        'Multiplicarse aproximadamente por 2',
        [('Multiplicarse aproximadamente por 3','El número de dB no se utiliza directamente como factor lineal.'),('Multiplicarse aproximadamente por 10','Un factor diez corresponde a 10 dB, no a 3 dB.'),('Dividirse aproximadamente por 2','Dividir entre dos supone una caída cercana a 3 dB, no una mejora.')],
        '10 log₁₀(2) ≈ 3,01 dB. Por eso una mejora de unos 3 dB equivale aproximadamente a duplicar la relación lineal.', 'Cálculo')
    add('t32','Traspaso entre controladores de un MSC','36, 39',
        'La BTS de destino pertenece a otro BSC, pero ambos BSC dependen del mismo MSC. ¿Qué tipo de traspaso describe el esquema?',
        'Inter-BSC, intra-MSC',
        [('Intra-celda','Se cambia de estación y de controlador, no solo de canal en la misma celda.'),('Inter-celda, intra-BSC','Las dos estaciones no comparten BSC en este caso.'),('Inter-MSC','El enunciado mantiene el mismo MSC para los dos controladores.')],
        'Cambia el controlador BSC pero se conserva la central MSC. El temario sitúa la gestión de este alcance en el MSC.')
    add('t32','Cambio de canal sin cambiar de celda','36–37',
        'El móvil conserva su celda, pero cambia de canal para mejorar la calidad del enlace. ¿Cómo se clasifica ese traspaso?',
        'Intra-celda',
        [('Inter-celda, intra-BSC','Implicaría cambiar de celda, que el caso descarta.'),('Inter-BSC','Implicaría cambiar de controlador, no solo de canal dentro de la celda.'),('Inter-MSC','Implicaría un cambio de central de un alcance mucho mayor.')],
        'Handover no significa necesariamente desplazarse a otra celda. El traspaso intra-celda cambia recursos del enlace dentro de la misma.')
    add('t32','Control del handover por el móvil','41',
        'El terminal mide sus condiciones y toma por sí mismo la decisión de traspaso. ¿Qué clasificación de control corresponde?',
        'MCHO',
        [('MAHO','En MAHO el móvil aporta medidas, pero decide la red.'),('NCHO','En NCHO la red realiza el control descrito.'),('Hard handover','Hard describe el orden de desconexión y conexión, no quién toma la decisión.')],
        'MCHO es controlado por el móvil. No debe mezclarse el eje de quién decide con el de cómo se ejecuta la transición entre enlaces.', 'Comprensión')
    add('t32','Cola temporal de traspasos','43–44',
        'Un móvil permanece brevemente en una zona de solapamiento. Si el destino está lleno, su petición de traspaso puede esperar un tiempo limitado a que se libere un canal. ¿Qué mecanismo se está usando?',
        'Cola de traspasos',
        [('Canales de guarda como única medida','La reserva separa recursos; el caso describe además una espera temporal de la petición.'),('Rechazo inmediato de todo traspaso sin recursos','El caso permite esperar en vez de rechazar inmediatamente.'),('Expulsión inmediata de otra llamada para liberar su canal','No se ha descrito interrumpir otra llamada, sino esperar un recurso.')],
        'La cola aprovecha el intervalo en que el móvil aún puede conservar su enlace anterior. Si la espera se agota, el traspaso puede fallar y la llamada perderse.')
    add('t32','Llamada bloqueada frente a llamada perdida','43',
        'Una llamada ya está en curso. El traspaso es necesario, el destino no tiene canal y no hay espera ni alternativa disponibles. ¿Qué resultado describe el tema?',
        'Pérdida de la llamada en curso',
        [('Bloqueo de una llamada nueva que todavía no ha comenzado','La comunicación del caso ya estaba establecida.'),('Conservación garantizada de la llamada aunque no haya enlace','Sin recursos ni alternativa no se garantiza la continuidad.'),('Creación automática de un canal radio adicional','La necesidad de traspaso no crea por sí misma nuevos recursos.')],
        'El tema diferencia rechazar el inicio de una llamada nueva de cortar una llamada que ya existía. Por esa diferencia de impacto se puede dar prioridad a los traspasos.')
    add('t32','Tráfico ofrecido y cursado','49–50, 54',
        'Se ofrecen 180 llamadas por hora, de dos minutos de duración cada una. Se pierde el 10 % y las aceptadas mantienen esa duración. ¿Qué pareja da tráfico ofrecido y cursado?',
        '6 erlangs ofrecidos y 5,4 erlangs cursados',
        [('6 erlangs ofrecidos y 0,6 erlangs cursados','0,6 es el tráfico perdido; el cursado es el 90 % del ofrecido.'),('180 erlangs ofrecidos y 162 erlangs cursados','Confunde el número de llamadas por hora con la ocupación media en erlangs.'),('12 erlangs ofrecidos y 10,8 erlangs cursados','Introduce un factor dos adicional en el cálculo del tráfico.')],
        'TO = 180×(2/60) = 6 E. TC = 6×(1−0,10) = 5,4 E. El tráfico perdido es 0,6 E. No se utiliza Erlang B.', 'Cálculo')
    add('t32','Qué significa el tráfico cursado','49–51',
        'Un grupo dispone de doce circuitos y cursa una intensidad media de 9 erlangs durante el intervalo observado. ¿Qué significa ese valor?',
        'Hay nueve circuitos ocupados de media en ese intervalo',
        [('Solo se han cursado nueve llamadas en todo el intervalo','La intensidad no es el número total de llamadas.'),('Llegan exactamente nueve llamadas nuevas cada segundo','El valor no es una tasa de llegadas; también depende de la duración.'),('Cada uno de los doce circuitos está ocupado nueve veces a la vez','Un circuito individual no atiende nueve llamadas simultáneas; el valor se refiere al grupo.')],
        'El tráfico cursado representa ocupación media de recursos. Puede superar un erlang en un grupo de varios circuitos, aunque un recurso individual no pueda estar ocupado más del 100 % del tiempo.')
