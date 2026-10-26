export function renderGuide({bank,blocks,heading,escape,icon}) {
  const counts=Object.fromEntries(blocks.map(b=>[b.id,bank.filter(q=>q.block===b.id).length]));
  return `${heading('SEGUNDA GUÍA DE REPASO','El temario, actualizado.','Cambios de alcance, prioridades y referencias para preparar el examen.')}
  <section class="guide-panel">
    <h2>Más práctica: 200 preguntas</h2>
    <p>La ampliación añade 65 ejercicios: cinco en T1 y quince en cada bloque T2.1, T2.2, T3.1 y T3.2. Se conservan las preguntas anteriores, la dificultad aproximada y las exclusiones. T4 sigue limitado a una definición de OpenAPI.</p>
    <p><strong>¿Por qué cambia cada test?</strong> Al empezar se eligen hasta 20 preguntas aleatorias del banco del tema. No se repiten dentro de esa sesión, pero pueden volver a salir en otro test. Para recorrerlas todas, utiliza el test completo.</p>
  </section>
  <section class="guide-panel">
    <h2>Qué cambia respecto a la guía anterior</h2>
    <p>El banco reúne ahora <strong>${bank.length} preguntas</strong>. Las nuevas están mezcladas con las anteriores dentro de cada bloque; los tests por tema toman hasta 20 del banco correspondiente.</p>
    <ul>
      <li><strong>T1:</strong> se retiran Flutter y la pregunta sobre el mecanismo interno de una PWA. Se conserva el enfoque conceptual de apps nativas/híbridas y qué es cada herramienta, con una nueva pregunta sobre desarrollo móvil.</li>
      <li><strong>T2.1:</strong> la introducción anterior a streaming ya no se trata como algo residual. Se amplían sistemas multimedia, hipermedia, etapas del proyecto, requisitos, jitter, unicast/multicast y el caso Netflix.</li>
      <li><strong>T2.2:</strong> más diferencias y casos de uso de UTF-8/16/32, RAID 10, efectos de la compresión y clasificación de arquitecturas de la página 47.</li>
      <li><strong>T3.1:</strong> se añaden SoC, RAM/flash, NPU, comparativa LCD/AMOLED, coexistencia Bluetooth, WiFi frente a ANT, alcances, RFID/NFC y tolerancia a fallos de tejidos inteligentes.</li>
      <li><strong>T3.2:</strong> se retira la pregunta de generaciones móviles. Se mantienen planificación celular, traspasos y ejercicios de tráfico en erlangs de la guía anterior; Erlang B queda fuera.</li>
      <li><strong>T4:</strong> una única pregunta: qué es OpenAPI. Su referencia es la OpenAPI Initiative, porque no se ha facilitado un PDF de este tema.</li>
    </ul>
    <p>La clasificación de arquitecturas está marcada como prioridad de repaso en la nueva guía. El banco refuerza sus diferencias, sin dar por garantizado ningún enunciado del examen.</p>
    <p><a href="./exports/cambios-guia.md" download>${icon('download')}Descargar la comparación de las dos guías</a></p>
  </section>
  <section class="guide-panel">
    <h2>RFID/NFC: dos afirmaciones que necesitan matiz</h2>
    <p><strong>«Tienen la misma frecuencia»:</strong> NFC opera en 13,56 MHz, que también utiliza RFID HF. RFID es una familia más amplia y también abarca otras bandas, como LF y UHF. No todo RFID opera a 13,56 MHz.</p>
    <p><strong>«Un lector NFC no puede leer RFID»:</strong> es cierto para etiquetas de otras bandas, como UHF, pero no es una regla universal. Puede comunicarse con ciertas etiquetas RFID HF compatibles; hay que comprobar protocolo, lector y condiciones de acceso. Las preguntas concretan esos casos para que solo una respuesta sea defendible.</p>
    <p>El <a href="https://nfc-forum.org/learn/nfc-technology/" target="_blank" rel="noopener noreferrer">NFC Forum</a> describe la frecuencia y los protocolos compatibles. Conviene contrastar esta simplificación de la guía con el profesor.</p>
  </section>
  <section class="guide-panel">
    <h2>Alcances e interferencias</h2>
    <p>No hay una distancia universal de WiFi, ANT/ANT+ o Bluetooth válida para todo equipo. Influyen potencia, antenas, sensibilidad, obstáculos e interferencias. Se comparan usos y condiciones, sin memorizar tasas de transferencia ni versiones.</p>
    <p>Bluetooth puede interferirse con WiFi en 2,4 GHz y el diseño de un móvil debe gestionar la coexistencia de sus radios. Esto no significa que toda red celular utilice 2,4 GHz. Las preguntas distinguen la banda compartida y la coexistencia de radios próximas.</p>
  </section>
  <section class="guide-panel">
    <h2>Cómo practicar</h2>
    <p><strong>Estudio:</strong> elige una respuesta y pulsa «Comprobar». Aparecen la explicación, el motivo del error y una referencia. Una selección pendiente todavía no cuenta como pregunta comprobada.</p>
    <p><strong>Examen:</strong> puedes responder, volver y cambiar opciones antes de terminar. Las soluciones se muestran al final; las preguntas en blanco se separan de los errores. El porcentaje es de aciertos, sin penalización ni equivalencia con la nota oficial.</p>
    <p><strong>Mixto:</strong> 20 preguntas repartidas entre los seis bloques. Como T4 solo tiene una, aparece una vez y el resto se reparte entre los demás temas. El test completo recorre las ${bank.length} preguntas.</p>
    <p>Las selecciones de tests distintos son independientes y pueden compartir preguntas. Preguntas y opciones se barajan. Las alternativas numéricas conservan un orden lógico. Las preguntas añadidas no forman un test separado: se mezclan con el resto de su bloque.</p>
    <p><strong>Teclado:</strong> 1–4 eligen; Espacio o Enter comprueban y otra pulsación avanza. Tab entra en el grupo y las flechas cambian la selección. Mantener la tecla no repite acciones.</p>
    <p><strong>Mis fallos:</strong> repasa hasta 20 preguntas cuyo último intento fue incorrecto. Acertarlas las retira de la lista. Cada estudiante tiene sus datos en su propio navegador; exportar/importar permite trasladarlos.</p>
  </section>
  <section class="guide-panel">
    <h2>Banco por bloque y descargas</h2>
    <p>Las fuentes indican páginas del archivo PDF contando desde la primera. OpenAPI usa una fuente web. Es material de práctica independiente, no un banco oficial del profesor.</p>
    ${blocks.map(b=>{
      const item=bank.find(q=>q.block===b.id);
      return `<div class="material-row"><h3>${b.code} · ${b.title} · ${counts[b.id]} ${counts[b.id]===1?'pregunta':'preguntas'}</h3><p>${escape(item.source_file)}</p><div class="material-links"><a href="./exports/${b.id}/cuestionario.md" download>${icon('download')}Cuestionario sin soluciones</a><a href="./exports/${b.id}/solucionario.md" download>${icon('book')}Solucionario explicado</a></div></div>`;
    }).join('')}
  </section>
  <section class="guide-panel">
    <h2>Exclusiones vigentes</h2>
    <p>Fuera de los tests: Flutter, arquitecturas detalladas y funcionamiento interno de frameworks móviles, preguntas de generaciones WiFi/móviles, versiones Bluetooth, tasas o anchos de banda memorizados, Erlang B y el resto de T4. No se incorporan temas de bases de datos ajenos al almacenamiento RAID.</p>
    <p>«UTFS» en la primera guía se interpretó como UTF-8. En planificación celular se especifica si se pide el tamaño N del clúster o la fracción 1/N, porque el PDF usa la palabra «factor» para ambos.</p>
  </section>
  <section class="guide-panel">
    <h2>Fuentes de contraste y revisión</h2>
    <p><a href="https://openconnect.netflix.com/en/" target="_blank" rel="noopener noreferrer">Netflix Open Connect</a> · <a href="https://www.bluetooth.com/learn-about-bluetooth/tech-overview/" target="_blank" rel="noopener noreferrer">Bluetooth SIG</a> · <a href="https://developer.garmin.com/ant-program/ant-ant-plus/" target="_blank" rel="noopener noreferrer">Garmin ANT/ANT+</a> · <a href="https://nfc-forum.org/learn/nfc-technology/" target="_blank" rel="noopener noreferrer">NFC Forum</a> · <a href="https://www.openapis.org/what-is-openapi" target="_blank" rel="noopener noreferrer">OpenAPI Initiative</a>.</p>
    <p>Se han comprobado estructura, claves por ID, cálculos y exportaciones, con revisión editorial propia. No se ha realizado una evaluación psicométrica ni se conocen las preguntas oficiales.</p>
  </section>`;
}
