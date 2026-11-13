# Perfil de Vinicius Covas

Contenido de su página de investigador del Centro de Investigación para la Comunicación Aplicada (CICA), Facultad de Comunicación, Universidad Anáhuac México.

**Página publicada:** https://investigadores-cica.pages.dev/vinicius-covas

Todo el contenido está en un solo archivo: [`perfil.yml`](perfil.yml). Cuando se guarda un cambio aquí, la página se actualiza sola en unos minutos.

## Editar a mano (sin instalar nada)

1. Abre `perfil.yml` y pulsa el lápiz (**Edit this file**).
2. Cambia tus textos. Para agregar una publicación, copia un bloque completo
   (desde el guion `-` hasta `enlace`) y pégalo al inicio de la lista.
3. Pulsa **Commit changes**.

Tres reglas para que no se rompa:

- No borres los espacios al inicio de las líneas.
- Si un texto lleva dos puntos (`:`), ponlo entre comillas: `titulo: "Ética: una introducción"`.
- Si no tienes un dato, déjalo como `""`. No aparecerá en la página.

Después de guardar, GitHub revisa el archivo automáticamente (pestaña **Actions**). Si aparece una ✗ roja, abre el detalle: dice qué campo corregir. En **History** puedes volver a cualquier versión anterior.

## Editar con tu asistente de IA

- **Claude:** entra a claude.ai/code, conecta tu GitHub y elige este repositorio.
- **ChatGPT:** usa Codex (la app de GitHub del chat normal solo puede leer) y elige este repositorio.

Luego pídelo en lenguaje normal, por ejemplo:

> Agrega a mi perfil este artículo: https://doi.org/... y actualiza mi semblanza con este párrafo: ...

El asistente sigue las reglas de [`AGENTS.md`](AGENTS.md): solo cambia tu perfil, no inventa datos y te pide visto bueno antes de guardar. Revisa el cambio antes de aprobarlo.

## Tu foto

Pega el enlace de tu foto en `foto:`, o sube la imagen a este repositorio (**Add file → Upload files**) y escribe su nombre (`foto: foto.jpg`). Se muestra en círculo. Si la cara queda pequeña o descentrada, ajusta:

- `foto_zoom: 1.4` acerca la imagen (1 = sin acercar).
- `foto_posicion: "50% 0%"` elige qué parte se ve (horizontal y vertical; `0%` = arriba).

## Este repositorio es público

Todo lo que pongas aquí queda visible, incluido el historial de cambios. No incluyas datos personales que no quieras publicar (teléfono personal, domicilio particular).
