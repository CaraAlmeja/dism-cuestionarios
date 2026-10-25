# DISM Lab

Web de estudio de Diseño e Infraestructura de Sistemas Multimedia para 3.º de Ingeniería Multimedia de la Universidad de Alicante. Material independiente de apoyo, no oficial.

## Incluye

- 100 preguntas originales, 20 por bloque: T1, T2.1, T2.2, T3.1 y T3.2.
- Test mixto equilibrado de 20 preguntas y recorrido completo de 100.
- Modo estudio con explicación inmediata; modo examen con corrección al terminar.
- Motivo específico del distractor elegido y referencia a página del PDF.
- Repaso de fallos, sesión reanudable e historial personal.
- Progreso en el navegador, exportable e importable en JSON.
- Copias del alumno y solucionarios descargables en Markdown desde Guía y materiales.
- Diseño adaptable a móviles, navegación con teclado y respeto a movimiento reducido.

## Ejecutar

Se necesita Node.js 20 o posterior. No hay dependencias que instalar.

```sh
npm start
```

Abre la URL local que imprime el servidor (por defecto `http://127.0.0.1:4173`). No abras `index.html` directamente: los módulos y la carga del banco necesitan HTTP.

```sh
npm test
npm run build
```

La salida estática se genera en `dist/`. Todos los recursos propios usan rutas relativas, compatibles con GitHub Pages bajo un subdirectorio. La tipografía remota es opcional y tiene fuentes de respaldo.

## Publicar en GitHub Pages

El workflow `.github/workflows/pages.yml` ejecuta las pruebas y publica `dist/` con cada push a `main`. En el repositorio, Settings → Pages → Source debe estar configurado como **GitHub Actions**. La pestaña Actions muestra el estado y la URL final del despliegue.

## Contenido

`public/data/questions.json` es la fuente final usada por la web. Las claves apuntan a IDs de opción estables, nunca a letras. `content/draft.json` conserva el borrador y `content/audit.json` el informe automático. `content/REVISION.md` documenta alcance, matices y límites de la revisión. Las exportaciones separadas están en `public/exports/`.

El banco parte de los cinco PDF entregados y de las prioridades del examen. No se incluyen los PDF originales ni sus extracciones en Git. Las preguntas son material de práctica y deben contrastarse con las aclaraciones del profesor.

Para regenerar el banco se necesitan Python 3 y el helper local de la skill `cuestionarios` en `~/.codex/skills/cuestionarios/scripts/quiz.py`:

```sh
python scripts/prepare_bank.py
```

Las fuentes de contraste enlazadas en los ítems son Netflix Open Connect, Bluetooth SIG, Garmin ANT/ANT+ y NFC Forum.

## Privacidad y persistencia

Sin cuentas, analítica ni backend. El progreso pertenece a cada navegador, en la clave `dism-lab:v1` de localStorage. No se comparten resultados entre compañeros ni se sincronizan dispositivos. Exportar crea una copia de las estadísticas y el historial; importar la sustituye tras confirmación. El modo privado o borrar los datos del navegador puede eliminar el progreso. Las sesiones en curso se conservan en ese navegador, pero no se incluyen en la exportación.

Cada intento corregido cuenta en el porcentaje acumulado. Mis fallos usa el resultado del último intento; acertar retira la pregunta de esa lista. Los blancos no son intentos y se separan en el resultado. No se aplica una fórmula oficial de calificación ni penalización.
