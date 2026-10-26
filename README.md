# DISM Lab

Web de estudio independiente de Diseño e Infraestructura de Sistemas Multimedia para 3.º de Ingeniería Multimedia de la Universidad de Alicante.

**Web:** [Abrir DISM Lab](https://caraalmeja.github.io/dism-cuestionarios/).

## Contenido actualizado

200 preguntas de cuatro alternativas y una respuesta correcta, dentro del alcance de las dos guías. La ampliación del 26 de octubre añade 65 ejercicios sin retirar los 135 existentes: 5 en T1 y 15 en cada bloque T2.1, T2.2, T3.1 y T3.2. T4 mantiene su única pregunta de OpenAPI.

| Bloque | Banco |
| --- | ---: |
| T1 · Aplicaciones multiplataforma | 24 |
| T2.1 · Streaming multimedia | 48 |
| T2.2 · Almacenamiento y arquitecturas | 46 |
| T3.1 · Dispositivos y conectividad | 47 |
| T3.2 · Telefonía móvil | 34 |
| T4 · Qué es OpenAPI | 1 |

- Tests por bloque de hasta 20 preguntas, mixto de 20 y recorrido completo de 200.
- Estudio con corrección inmediata y examen con soluciones al finalizar.
- Explicación del error y referencia a página PDF o fuente web.
- Repaso de fallos, sesión reanudable, historial y exportación/importación del progreso.
- Cuestionarios de alumno y solucionarios separados en Markdown.
- Tema claro/oscuro, vista móvil y mapa largo con desplazamiento interno.

Cada test por tema toma hasta 20 preguntas aleatorias de su banco, sin duplicados en esa sesión. Entre tests distintos pueden repetirse. El mixto reparte 20 entre los bloques y el completo recorre las 200.

En el cuestionario, 1–4 eligen; Espacio/Enter comprueban y otra pulsación avanza. En examen continúan sin revelar la solución. Tab entra en el grupo de respuesta única y las flechas cambian la selección. Mantener la tecla no repite la acción.

La comparación de las guías se descarga desde Guía y materiales. Allí se explican las simplificaciones de RFID/NFC y las condiciones de alcance. El material no predice el examen oficial.

## Ejecutar y publicar

Node.js 20 o posterior, sin dependencias que instalar:

```sh
npm start
npm test
npm run build
```

El servidor imprime su URL local (por defecto http://127.0.0.1:4173). Los módulos y el banco necesitan HTTP; no se debe abrir index.html directamente. La salida estática queda en dist/, con rutas relativas compatibles con GitHub Pages bajo subdirectorio. La tipografía remota tiene fuentes de respaldo.

El workflow .github/workflows/pages.yml prueba y publica cada push a main. En Settings → Pages debe estar seleccionado GitHub Actions.

## Fuentes y regeneración

public/data/questions.json es el banco final de la web. Las claves apuntan a IDs estables, nunca a letras. content/draft.json conserva el borrador; content/retired.json, los IDs retirados; content/audit.json, el informe automático. content/REVISION.md documenta el alcance vigente. Las exportaciones están en public/exports/.

Los cinco PDF y sus extracciones permanecen fuera de Git. OpenAPI usa una fuente primaria web. No se ha realizado validación psicométrica ni revisión independiente.

Para regenerar se necesita Python 3 y el helper de la skill cuestionarios en ~/.codex/skills/cuestionarios/scripts/quiz.py:

```sh
python scripts/prepare_bank.py
```

scripts/author_bank.py conserva los ítems originales y scripts/guide_update.py aplica las exclusiones y nuevas preguntas de la segunda guía; scripts/practice_expansion.py añade los 65 ejercicios de práctica. El proceso mezcla dentro de los bloques, equilibra las claves y regenera ambas exportaciones desde un único JSON.

## Datos y privacidad

Sin cuentas, analítica ni backend. El progreso es propio de cada navegador, en la clave dism-lab:v1 de localStorage. No hay sincronización ni resultados compartidos. Exportar guarda estadísticas e historial; importar los sustituye tras confirmación. Las sesiones se conservan localmente, pero no se incluyen en la copia exportada.

La actualización conserva respuestas de preguntas vigentes y retira de sesiones recuperadas únicamente los IDs excluidos. Los blancos no son intentos fallados. El porcentaje no aplica penalización ni representa la nota oficial.
