# Solucionario: DISM · T1 · Aplicaciones multiplataforma

## 1. B) Una app web con capacidades como instalación y funcionamiento sin conexión

Una PWA parte de una aplicación web e incorpora capacidades de experiencia de app. El funcionamiento sin conexión depende de lo que se implemente y almacene, no significa que todos sus servicios funcionen sin red.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 42–44.

Distractores:

- A) Una PWA puede descubrirse y compartirse mediante una URL.
- C) La base de la PWA son tecnologías web, no UIKit.
- D) Rust y los ejecutables de escritorio no definen una PWA.

## 2. D) Añade capacidades como tipos y se transpila a JavaScript

TypeScript incorpora un sistema de tipos y otras herramientas para el desarrollo. El código se transforma a JavaScript para ejecutarse en el entorno web.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 38.

Distractores:

- A) TypeScript amplía JavaScript; no se define por eliminar sus funciones.
- B) No es un lenguaje de consulta de bases de datos.
- C) Su resultado habitual para la web es JavaScript, no instrucciones de GPU.

## 3. A) Un framework para apps nativas móviles y de escritorio con C# y XAML

.NET Multi-platform App UI permite compartir una base de código C# y XAML para Android, iOS, macOS y Windows. Aquí se evalúa qué es, sin preguntar su arquitectura interna.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 48–49.

Distractores:

- B) Esa descripción encaja con integraciones híbridas como Cordova, no con el framework C#/XAML de MAUI.
- C) El enfoque nativo de MAUI utiliza C# y XAML; HTML no es obligatorio.
- D) MAUI es una herramienta de desarrollo de aplicaciones, no un protocolo o reproductor.

## 4. D) Un framework de interfaces y apps multiplataforma con tecnologías web

Ionic facilita aplicaciones con tecnologías web y componentes adaptados visualmente a cada plataforma. Puede trabajar con Angular, React o Vue.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 33, 37, 39.

Distractores:

- A) Ionic permite distintos destinos y no es una herramienta exclusiva de Apple.
- B) Ionic es un framework multiplataforma de tecnologías web, no un servicio exclusivo de Swift.
- C) Ionic es un framework; no un nuevo lenguaje de programación.

## 5. C) Tauri

Tauri utiliza tecnologías web para la interfaz y Rust para el núcleo nativo. El tema destaca que aprovecha la WebView del sistema en lugar de empaquetar un navegador completo.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 64.

Distractores:

- A) KMP comparte código Kotlin; no se define por un núcleo Rust.
- B) Ionic también usa tecnologías web, pero no se define por el núcleo Rust descrito.
- D) Xamarin utiliza C# y el ecosistema .NET.

## 6. D) Uno Platform

Uno Platform es una alternativa del ecosistema .NET con soporte de WebAssembly y Linux, además de destinos móviles y de escritorio.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 52, 69.

Distractores:

- A) React Native usa JS/TS con React; no se define por XAML.
- B) Cordova empaqueta tecnologías web, no ofrece ese modelo C#/XAML.
- C) El material diferencia Uno por incluir WebAssembly entre sus destinos.

## 7. A) Empaquetar apps web móviles y acceder al dispositivo mediante plugins

Cordova permite usar HTML, CSS y JavaScript en una app empaquetada y ofrece plugins para cámara, GPS y otras capacidades. La interfaz continúa siendo web.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 26–30.

Distractores:

- B) Cordova se ocupa de aplicaciones móviles web empaquetadas y su acceso al dispositivo, no de alojar servicios backend.
- C) Esa combinación se asocia con MAUI o Xamarin.Forms.
- D) Ese objetivo se asocia con Kotlin Multiplatform.

## 8. B) Reutilizar conocimientos web y reducir duplicación de desarrollo

La reutilización de código y de las competencias web puede reducir tiempo y coste. El ahorro no elimina las pruebas específicas ni las diferencias entre plataformas.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 13–14.

Distractores:

- A) El enfoque híbrido descrito mantiene la interfaz en una WebView.
- C) La base compartida sigue necesitando pruebas en los dispositivos objetivo.
- D) El ahorro destacado se obtiene compartiendo código, no manteniendo dos implementaciones independientes.

## 9. A) Crear software orientado a dispositivos como smartphones y tabletas

El tema define el desarrollo móvil como procesos y procedimientos para crear software destinado a pequeños dispositivos inalámbricos, como teléfonos y tabletas.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 2–3.

Distractores:

- B) Eso es infraestructura de comunicaciones, no el proceso de desarrollo de apps.
- C) El desarrollo de aplicaciones escribe software; no fabrica los componentes físicos.
- D) El desarrollo móvil tiene como destino dispositivos móviles, aunque pueda reutilizar tecnologías web.

## 10. D) Una herramienta para crear apps nativas compartiendo código C#

Xamarin permitió reutilizar C# en aplicaciones móviles nativas. El material lo presenta como antecedente histórico de .NET MAUI, no como una recomendación de soporte actual.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 18–19, 24.

Distractores:

- A) Xamarin pertenece a .NET y utiliza C#, no solo tecnologías web.
- B) Esta descripción corresponde a Kotlin Multiplatform.
- C) Xamarin permite compartir C# entre plataformas, no es un entorno exclusivo de Swift.

## 11. C) Multiplataforma con interfaz nativa

React Native permite construir una interfaz con componentes nativos utilizando JavaScript o TypeScript. La clasificación depende de cómo se ejecuta y presenta la app, no solo de su lenguaje.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 16, 57.

Distractores:

- A) Compartir código no implica distribución como aplicación web progresiva.
- B) El lenguaje por sí solo no determina que exista una interfaz híbrida.
- D) React Native no presenta la app como una página HTML tradicional.

## 12. B) Ofrecer integración con funciones nativas mediante plugins

Capacitor conecta el código web con capacidades del dispositivo mediante plugins. La apariencia similar a la del sistema no implica que la interfaz deje de ser web.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 34–37.

Distractores:

- A) Capacitor facilita acceso a APIs nativas pero mantiene la interfaz web en una WebView.
- C) El sistema de estilos no proporciona la integración nativa que necesita la cámara.
- D) La subida depende de la lógica y servicios de la app; el papel del plugin es integrar la cámara.

## 13. B) Desarrollo específico con las herramientas nativas de la plataforma

El desarrollo específico utiliza las herramientas y APIs de la plataforma. Puede exigir más esfuerzo al mantener versiones distintas, pero facilita aprovechar sus particularidades.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 3, 11–15.

Distractores:

- A) El contenedor requiere integración adicional para acceder a las funciones del dispositivo.
- C) Las capacidades dependen de las APIs y permisos expuestos por el navegador.
- D) Los plugins pueden ofrecer acceso, pero añaden una integración intermedia respecto a las APIs nativas.

## 14. A) React Native

React Native combina el modelo de React con componentes nativos para las plataformas móviles. Es la opción alineada con el conocimiento y el resultado solicitados.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 57.

Distractores:

- B) Ionic puede utilizar React, pero presenta su interfaz web en una WebView, frente a la interfaz nativa solicitada.
- C) MAUI se centra en C# y XAML, no en React con JS/TS.
- D) Cordova ofrece el enfoque de app web empaquetada, no la interfaz nativa solicitada.

## 15. A) La disponibilidad o creación de un plugin para ese sensor

El código web accede a muchas funciones del dispositivo a través de plugins. Si falta el del sensor, hay que implementarlo o esperar a que exista.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 15, 41.

Distractores:

- B) Las apps híbridas pueden empaquetarse y distribuirse en tiendas.
- C) XAML pertenece a otro ecosistema y no resuelve por sí mismo ese acceso.
- D) El acceso al sensor requiere integración nativa, no eliminar la lógica.

## 16. C) Kotlin Multiplatform

KMP permite compartir lógica y conservar interfaces específicas. Compartir UI es una posibilidad adicional con Compose Multiplatform, no una obligación.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 60–61.

Distractores:

- A) MAUI trabaja con C# y XAML; no es la tecnología de compartición de lógica Kotlin del caso.
- B) Ionic prioriza la interfaz web; no el objetivo de lógica común en Kotlin indicado.
- D) Cordova no es la tecnología de compartición de lógica Kotlin descrita.

## 17. C) Probar y ajustar el comportamiento en cada plataforma objetivo

El código compartido reduce duplicación, pero el material recuerda la puesta a punto por sistema operativo y la elección según los requisitos del proyecto.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 11–12, 70.

Distractores:

- A) Compilar sin errores no comprueba el comportamiento durante la ejecución.
- B) No cubre diferencias de interfaz, permisos o integración del dispositivo.
- D) Compartir código no garantiza el mismo resultado visual y funcional en todas.

## 18. C) Swift y Xcode

Para iOS, el tema sitúa Swift (y el histórico Objective-C) junto a Xcode. Para Android, sitúa Kotlin y Android Studio.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 8, 12.

Distractores:

- A) Cordova usa tecnologías web y C# se asocia con el ecosistema .NET.
- B) Esta pareja corresponde a Android.
- D) Android Studio es el entorno de Android; para el desarrollo iOS del caso se usa Swift con Xcode.

## 19. B) Desarrollo híbrido

El rasgo decisivo es la interfaz web ejecutada en una WebView dentro de la aplicación. Instalarla desde una tienda no cambia su naturaleza híbrida.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 13–16.

Distractores:

- A) MAUI usa controles de plataforma en el enfoque nativo descrito, no esta interfaz web.
- C) El lenguaje de Android no convierte una interfaz web en controles nativos.
- D) Swift no describe una interfaz HTML ejecutada en una WebView.
