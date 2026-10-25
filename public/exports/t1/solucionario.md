# Solucionario: DISM · T1 · Aplicaciones multiplataforma

## 1. D) Desarrollo híbrido

El rasgo decisivo es la interfaz web ejecutada en una WebView dentro de la aplicación. Instalarla desde una tienda no cambia su naturaleza híbrida.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 13–16.

Distractores:

- A) MAUI usa controles de plataforma en el enfoque nativo descrito, no esta interfaz web.
- B) El lenguaje de Android no convierte una interfaz web en controles nativos.
- C) Swift no describe una interfaz HTML ejecutada en una WebView.

## 2. B) Multiplataforma con interfaz nativa

React Native permite construir una interfaz con componentes nativos utilizando JavaScript o TypeScript. La clasificación depende de cómo se ejecuta y presenta la app, no solo de su lenguaje.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 16, 57.

Distractores:

- A) Compartir código no implica distribución como aplicación web progresiva.
- C) React Native no presenta la app como una página HTML tradicional.
- D) El lenguaje por sí solo no determina que exista una interfaz híbrida.

## 3. A) Reutilizar conocimientos web y reducir duplicación de desarrollo

La reutilización de código y de las competencias web puede reducir tiempo y coste. El ahorro no elimina las pruebas específicas ni las diferencias entre plataformas.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 13–14.

Distractores:

- B) La base compartida sigue necesitando pruebas en los dispositivos objetivo.
- C) El ahorro destacado se obtiene compartiendo código, no manteniendo dos implementaciones independientes.
- D) El enfoque híbrido descrito mantiene la interfaz en una WebView.

## 4. A) La disponibilidad o creación de un plugin para ese sensor

El código web accede a muchas funciones del dispositivo a través de plugins. Si falta el del sensor, hay que implementarlo o esperar a que exista.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 15, 41.

Distractores:

- B) Las apps híbridas pueden empaquetarse y distribuirse en tiendas.
- C) XAML pertenece a otro ecosistema y no resuelve por sí mismo ese acceso.
- D) El acceso al sensor requiere integración nativa, no eliminar la lógica.

## 5. A) Swift y Xcode

Para iOS, el tema sitúa Swift (y el histórico Objective-C) junto a Xcode. Para Android, sitúa Kotlin y Android Studio.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 8, 12.

Distractores:

- B) Esta pareja corresponde a Android.
- C) Cordova usa tecnologías web y C# se asocia con el ecosistema .NET.
- D) Dart se asocia con Flutter; no es el lenguaje específico de iOS.

## 6. B) Una herramienta para crear apps nativas compartiendo código C#

Xamarin permitió reutilizar C# en aplicaciones móviles nativas. El material lo presenta como antecedente histórico de .NET MAUI, no como una recomendación de soporte actual.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 18–19, 24.

Distractores:

- A) Esta descripción corresponde a Flutter.
- C) Esta descripción corresponde a Kotlin Multiplatform.
- D) Xamarin pertenece a .NET y utiliza C#, no solo tecnologías web.

## 7. D) Empaquetar apps web móviles y acceder al dispositivo mediante plugins

Cordova permite usar HTML, CSS y JavaScript en una app empaquetada y ofrece plugins para cámara, GPS y otras capacidades. La interfaz continúa siendo web.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 26–30.

Distractores:

- A) Ese objetivo se asocia con Kotlin Multiplatform.
- B) Esa combinación se asocia con MAUI o Xamarin.Forms.
- C) Esta función corresponde al enfoque de Flutter.

## 8. A) Un framework de interfaces y apps multiplataforma con tecnologías web

Ionic facilita aplicaciones con tecnologías web y componentes adaptados visualmente a cada plataforma. Puede trabajar con Angular, React o Vue.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 33, 37, 39.

Distractores:

- B) Ionic es un framework; no un nuevo lenguaje de programación.
- C) Ionic permite distintos destinos y no es una herramienta exclusiva de Apple.
- D) Dart es el lenguaje de Flutter, no un requisito de Ionic.

## 9. B) Ofrecer integración con funciones nativas mediante plugins

Capacitor conecta el código web con capacidades del dispositivo mediante plugins. La apariencia similar a la del sistema no implica que la interfaz deje de ser web.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 34–37.

Distractores:

- A) El sistema de estilos no proporciona la integración nativa que necesita la cámara.
- C) Capacitor no convierte la app en Flutter.
- D) XAML pertenece a .NET y no es la función de Capacitor.

## 10. A) Añade capacidades como tipos y se transpila a JavaScript

TypeScript incorpora un sistema de tipos y otras herramientas para el desarrollo. El código se transforma a JavaScript para ejecutarse en el entorno web.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 38.

Distractores:

- B) TypeScript amplía JavaScript; no se define por eliminar sus funciones.
- C) Su resultado habitual para la web es JavaScript, no instrucciones de GPU.
- D) No es un lenguaje de consulta de bases de datos.

## 11. B) Una app web con capacidades como instalación y funcionamiento sin conexión

Una PWA parte de una aplicación web e incorpora capacidades de experiencia de app. El funcionamiento sin conexión depende de lo que se implemente y almacene, no significa que todos sus servicios funcionen sin red.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 42–44.

Distractores:

- A) La base de la PWA son tecnologías web, no UIKit.
- C) Rust y los ejecutables de escritorio no definen una PWA.
- D) Una PWA puede descubrirse y compartirse mediante una URL.

## 12. C) Un service worker con una estrategia de caché

El service worker permite gestionar peticiones y recursos en caché. Para abrir contenido sin conexión, ese contenido debe haberse guardado previamente.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 43–44.

Distractores:

- A) La suscripción no proporciona el almacenamiento de recursos web.
- B) CSS adapta la presentación; no intercepta peticiones ni proporciona caché programable.
- D) El manifiesto describe la app; no compila Swift ni guarda por sí solo los recursos.

## 13. D) Un framework para apps nativas móviles y de escritorio con C# y XAML

.NET Multi-platform App UI permite compartir una base de código C# y XAML para Android, iOS, macOS y Windows. Aquí se evalúa qué es, sin preguntar su arquitectura interna.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 48–49.

Distractores:

- A) El enfoque nativo de MAUI utiliza C# y XAML; HTML no es obligatorio.
- B) Esa asociación corresponde al ecosistema Flutter, no a MAUI.
- C) MAUI es una herramienta de desarrollo de aplicaciones, no un protocolo o reproductor.

## 14. C) SDK de Google y lenguaje Dart

Flutter es el SDK multiplataforma de Google cuyo lenguaje de desarrollo es Dart. Permite crear apps para móvil, web y escritorio.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 53–54.

Distractores:

- A) Esta combinación se relaciona con React Native.
- B) Esta combinación se relaciona con .NET MAUI.
- D) Esta combinación se relaciona con Kotlin Multiplatform.

## 15. D) React Native

React Native combina el modelo de React con componentes nativos para las plataformas móviles. Es la opción alineada con el conocimiento y el resultado solicitados.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 57.

Distractores:

- A) MAUI se centra en C# y XAML, no en React con JS/TS.
- B) Cordova ofrece el enfoque de app web empaquetada, no la interfaz nativa solicitada.
- C) Flutter utiliza Dart; no es la opción que reutiliza directamente React.

## 16. D) Kotlin Multiplatform

KMP permite compartir lógica y conservar interfaces específicas. Compartir UI es una posibilidad adicional con Compose Multiplatform, no una obligación.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 60–61.

Distractores:

- A) Flutter propone Dart y una interfaz con sus widgets, que no es el requisito dado.
- B) Ionic prioriza la interfaz web; no el objetivo de lógica común en Kotlin indicado.
- C) Cordova no es la tecnología de compartición de lógica Kotlin descrita.

## 17. B) Tauri

Tauri utiliza tecnologías web para la interfaz y Rust para el núcleo nativo. El tema destaca que aprovecha la WebView del sistema en lugar de empaquetar un navegador completo.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 64.

Distractores:

- A) KMP comparte código Kotlin; no se define por un núcleo Rust.
- C) Xamarin utiliza C# y el ecosistema .NET.
- D) Flutter utiliza Dart y su propio sistema de interfaz.

## 18. C) Uno Platform

Uno Platform es una alternativa del ecosistema .NET con soporte de WebAssembly y Linux, además de destinos móviles y de escritorio.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 52, 69.

Distractores:

- A) Cordova empaqueta tecnologías web, no ofrece ese modelo C#/XAML.
- B) El material diferencia Uno por incluir WebAssembly entre sus destinos.
- D) React Native usa JS/TS con React; no se define por XAML.

## 19. C) Desarrollo específico con las herramientas nativas de la plataforma

El desarrollo específico utiliza las herramientas y APIs de la plataforma. Puede exigir más esfuerzo al mantener versiones distintas, pero facilita aprovechar sus particularidades.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 3, 11–15.

Distractores:

- A) Las capacidades dependen de las APIs y permisos expuestos por el navegador.
- B) Los plugins pueden ofrecer acceso, pero añaden una integración intermedia respecto a las APIs nativas.
- D) El contenedor requiere integración adicional para acceder a las funciones del dispositivo.

## 20. C) Probar y ajustar el comportamiento en cada plataforma objetivo

El código compartido reduce duplicación, pero el material recuerda la puesta a punto por sistema operativo y la elección según los requisitos del proyecto.

Fuente: Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf, páginas PDF 11–12, 70.

Distractores:

- A) Compartir código no garantiza el mismo resultado visual y funcional en todas.
- B) Compilar sin errores no comprueba el comportamiento durante la ejecución.
- D) No cubre diferencias de interfaz, permisos o integración del dispositivo.
