# Solucionario: DISM · T1 · Aplicaciones multiplataforma

## 1. A) Uno Platform

Uno Platform es una alternativa del ecosistema .NET con soporte de WebAssembly y Linux, además de destinos móviles y de escritorio.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 52, 69.

Distractores:

- B) React Native usa JS/TS con React; no se define por XAML.
- C) Cordova empaqueta tecnologías web, no ofrece ese modelo C#/XAML.
- D) El material diferencia Uno por incluir WebAssembly entre sus destinos.

## 2. D) Una app web con capacidades como instalación y funcionamiento sin conexión

Una PWA parte de una aplicación web e incorpora capacidades de experiencia de app. El funcionamiento sin conexión depende de lo que se implemente y almacene, no significa que todos sus servicios funcionen sin red.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 42–44.

Distractores:

- A) Una PWA puede descubrirse y compartirse mediante una URL.
- B) La base de la PWA son tecnologías web, no UIKit.
- C) Rust y los ejecutables de escritorio no definen una PWA.

## 3. A) La compilación para ese destino requiere un equipo Apple

El temario indica que la compilación de aplicaciones iOS requiere un equipo Apple también con MAUI. Es un requisito de plataforma, distinto de compartir código.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 23, 49.

Distractores:

- B) El lenguaje no determina que la distribución sea una aplicación web progresiva.
- C) Compartir código no hace intercambiables los paquetes de sistemas distintos.
- D) La reutilización de C# no elimina la cadena de herramientas exigida para compilar para iOS.

## 4. A) Multiplataforma con interfaz nativa

React Native permite construir una interfaz con componentes nativos utilizando JavaScript o TypeScript. La clasificación depende de cómo se ejecuta y presenta la app, no solo de su lenguaje.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 16, 57.

Distractores:

- B) React Native no presenta la app como una página HTML tradicional.
- C) Compartir código no implica distribución como aplicación web progresiva.
- D) El lenguaje por sí solo no determina que exista una interfaz híbrida.

## 5. C) Tauri

Tauri utiliza tecnologías web para la interfaz y Rust para el núcleo nativo. El tema destaca que aprovecha la WebView del sistema en lugar de empaquetar un navegador completo.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 64.

Distractores:

- A) Ionic también usa tecnologías web, pero no se define por el núcleo Rust descrito.
- B) KMP comparte código Kotlin; no se define por un núcleo Rust.
- D) Xamarin utiliza C# y el ecosistema .NET.

## 6. A) Una app híbrida puede utilizar funciones del dispositivo mediante integración nativa

Híbrida no significa incapaz de usar hardware. El acceso suele apoyarse en plugins o integraciones nativas; su disponibilidad y los permisos siguen importando.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 15, 29, 34–37.

Distractores:

- B) La integración sigue sometida a los permisos y condiciones de la plataforma.
- C) El uso de una API del dispositivo no cambia por sí solo la interfaz web.
- D) Los plugins permiten integrar capacidades como GPS o cámara.

## 7. C) Una herramienta para crear apps nativas compartiendo código C#

Xamarin permitió reutilizar C# en aplicaciones móviles nativas. El material lo presenta como antecedente histórico de .NET MAUI, no como una recomendación de soporte actual.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 18–19, 24.

Distractores:

- A) Xamarin pertenece a .NET y utiliza C#, no solo tecnologías web.
- B) Esta descripción corresponde a Kotlin Multiplatform.
- D) Xamarin permite compartir C# entre plataformas, no es un entorno exclusivo de Swift.

## 8. A) Ofrecer integración con funciones nativas mediante plugins

Capacitor conecta el código web con capacidades del dispositivo mediante plugins. La apariencia similar a la del sistema no implica que la interfaz deje de ser web.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 34–37.

Distractores:

- B) El sistema de estilos no proporciona la integración nativa que necesita la cámara.
- C) La subida depende de la lógica y servicios de la app; el papel del plugin es integrar la cámara.
- D) Capacitor facilita acceso a APIs nativas pero mantiene la interfaz web en una WebView.

## 9. A) La disponibilidad o creación de un plugin para ese sensor

El código web accede a muchas funciones del dispositivo a través de plugins. Si falta el del sensor, hay que implementarlo o esperar a que exista.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 15, 41.

Distractores:

- B) Las apps híbridas pueden empaquetarse y distribuirse en tiendas.
- C) XAML pertenece a otro ecosistema y no resuelve por sí mismo ese acceso.
- D) El acceso al sensor requiere integración nativa, no eliminar la lógica.

## 10. D) No; el aspecto visual no determina cómo se presenta la interfaz

Ionic adapta el aspecto de sus componentes al sistema, pero la apariencia no equivale a utilizar controles nativos. Debe atenderse al enfoque de ejecución y presentación.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 16, 33, 39.

Distractores:

- A) Adaptar los estilos no exige cambiar al lenguaje específico de Android.
- B) La uniformidad entre sistemas no es el criterio que define una interfaz nativa.
- C) Un componente web puede imitar o adaptar esa apariencia.

## 11. B) Empaquetar apps web móviles y acceder al dispositivo mediante plugins

Cordova permite usar HTML, CSS y JavaScript en una app empaquetada y ofrece plugins para cámara, GPS y otras capacidades. La interfaz continúa siendo web.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 26–30.

Distractores:

- A) Esa combinación se asocia con MAUI o Xamarin.Forms.
- C) Cordova se ocupa de aplicaciones móviles web empaquetadas y su acceso al dispositivo, no de alojar servicios backend.
- D) Ese objetivo se asocia con Kotlin Multiplatform.

## 12. B) Crear software orientado a dispositivos como smartphones y tabletas

El tema define el desarrollo móvil como procesos y procedimientos para crear software destinado a pequeños dispositivos inalámbricos, como teléfonos y tabletas.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 2–3.

Distractores:

- A) El desarrollo de aplicaciones escribe software; no fabrica los componentes físicos.
- C) El desarrollo móvil tiene como destino dispositivos móviles, aunque pueda reutilizar tecnologías web.
- D) Eso es infraestructura de comunicaciones, no el proceso de desarrollo de apps.

## 13. D) React Native

React Native combina el modelo de React con componentes nativos para las plataformas móviles. Es la opción alineada con el conocimiento y el resultado solicitados.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 57.

Distractores:

- A) MAUI se centra en C# y XAML, no en React con JS/TS.
- B) Cordova ofrece el enfoque de app web empaquetada, no la interfaz nativa solicitada.
- C) Ionic puede utilizar React, pero presenta su interfaz web en una WebView, frente a la interfaz nativa solicitada.

## 14. B) Desarrollo específico con las herramientas nativas de la plataforma

El desarrollo específico utiliza las herramientas y APIs de la plataforma. Puede exigir más esfuerzo al mantener versiones distintas, pero facilita aprovechar sus particularidades.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 3, 11–15.

Distractores:

- A) El contenedor requiere integración adicional para acceder a las funciones del dispositivo.
- C) Las capacidades dependen de las APIs y permisos expuestos por el navegador.
- D) Los plugins pueden ofrecer acceso, pero añaden una integración intermedia respecto a las APIs nativas.

## 15. B) Puede mostrar lo guardado, mientras la consulta remota necesita conectividad

El soporte offline depende de qué recursos y datos estén disponibles localmente. No elimina la dependencia de red de operaciones que requieren un servidor.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 42–43.

Distractores:

- A) El estado de la red no cambia el enfoque tecnológico de la aplicación.
- C) Soportar funciones offline no garantiza acceso a servicios remotos sin red.
- D) La pérdida de conexión no obliga a eliminar el contenido local.

## 16. C) Un framework para apps nativas móviles y de escritorio con C# y XAML

.NET Multi-platform App UI permite compartir una base de código C# y XAML para Android, iOS, macOS y Windows. Aquí se evalúa qué es, sin preguntar su arquitectura interna.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 48–49.

Distractores:

- A) El enfoque nativo de MAUI utiliza C# y XAML; HTML no es obligatorio.
- B) MAUI es una herramienta de desarrollo de aplicaciones, no un protocolo o reproductor.
- D) Esa descripción encaja con integraciones híbridas como Cordova, no con el framework C#/XAML de MAUI.

## 17. B) Reutilizar conocimientos web y reducir duplicación de desarrollo

La reutilización de código y de las competencias web puede reducir tiempo y coste. El ahorro no elimina las pruebas específicas ni las diferencias entre plataformas.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 13–14.

Distractores:

- A) El enfoque híbrido descrito mantiene la interfaz en una WebView.
- C) La base compartida sigue necesitando pruebas en los dispositivos objetivo.
- D) El ahorro destacado se obtiene compartiendo código, no manteniendo dos implementaciones independientes.

## 18. C) Probar y ajustar el comportamiento en cada plataforma objetivo

El código compartido reduce duplicación, pero el material recuerda la puesta a punto por sistema operativo y la elección según los requisitos del proyecto.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 11–12, 70.

Distractores:

- A) Compartir código no garantiza el mismo resultado visual y funcional en todas.
- B) Compilar sin errores no comprueba el comportamiento durante la ejecución.
- D) No cubre diferencias de interfaz, permisos o integración del dispositivo.

## 19. D) Añade capacidades como tipos y se transpila a JavaScript

TypeScript incorpora un sistema de tipos y otras herramientas para el desarrollo. El código se transforma a JavaScript para ejecutarse en el entorno web.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 38.

Distractores:

- A) Su resultado habitual para la web es JavaScript, no instrucciones de GPU.
- B) TypeScript amplía JavaScript; no se define por eliminar sus funciones.
- C) No es un lenguaje de consulta de bases de datos.

## 20. C) Un framework de interfaces y apps multiplataforma con tecnologías web

Ionic facilita aplicaciones con tecnologías web y componentes adaptados visualmente a cada plataforma. Puede trabajar con Angular, React o Vue.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 33, 37, 39.

Distractores:

- A) Ionic permite distintos destinos y no es una herramienta exclusiva de Apple.
- B) Ionic es un framework multiplataforma de tecnologías web, no un servicio exclusivo de Swift.
- D) Ionic es un framework; no un nuevo lenguaje de programación.

## 21. C) Kotlin Multiplatform

KMP permite compartir lógica y conservar interfaces específicas. Compartir UI es una posibilidad adicional con Compose Multiplatform, no una obligación.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 60–61.

Distractores:

- A) MAUI trabaja con C# y XAML; no es la tecnología de compartición de lógica Kotlin del caso.
- B) Ionic prioriza la interfaz web; no el objetivo de lógica común en Kotlin indicado.
- D) Cordova no es la tecnología de compartición de lógica Kotlin descrita.

## 22. B) Sí; compartir la lógica no obliga a compartir toda la interfaz

KMP permite compartir datos, red y reglas de negocio manteniendo interfaces por plataforma. La decisión de compartir también la UI es adicional.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 60–61.

Distractores:

- A) La lógica compartida puede coexistir con interfaces específicas.
- C) El tema explica que compartir la UI es una posibilidad, no una obligación.
- D) Conservar interfaces específicas no implica convertirlas en interfaces web.

## 23. D) Swift y Xcode

Para iOS, el tema sitúa Swift (y el histórico Objective-C) junto a Xcode. Para Android, sitúa Kotlin y Android Studio.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 8, 12.

Distractores:

- A) Esta pareja corresponde a Android.
- B) Cordova usa tecnologías web y C# se asocia con el ecosistema .NET.
- C) Android Studio es el entorno de Android; para el desarrollo iOS del caso se usa Swift con Xcode.

## 24. D) Desarrollo híbrido

El rasgo decisivo es la interfaz web ejecutada en una WebView dentro de la aplicación. Instalarla desde una tienda no cambia su naturaleza híbrida.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 13–16.

Distractores:

- A) MAUI usa controles de plataforma en el enfoque nativo descrito, no esta interfaz web.
- B) Swift no describe una interfaz HTML ejecutada en una WebView.
- C) El lenguaje de Android no convierte una interfaz web en controles nativos.
