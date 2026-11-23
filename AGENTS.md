# Instrucciones para agentes de IA (Claude, ChatGPT/Codex u otros)

Este repositorio contiene el perfil de Vinicius Covas para su página de investigador
del CICA, Facultad de Comunicación, Universidad Anáhuac México:
https://investigadores-cica.pages.dev/vinicius-covas

Cada cambio guardado en `main` aparece en la página publicada en unos minutos.

## Cómo guardar
- Guarda los cambios directamente en la rama `main`, con un commit. No crees otra rama ni un
  pull request, salvo que el investigador lo pida: él no revisa ni aprueba pull requests.
- Después de cada cambio en `main`, una revisión automática (`.github/workflows/validar.yml`) valida
  `perfil.yml`. Si falla, regresa el repositorio a la versión anterior por sí sola. Si eso pasa,
  corrige el error y vuelve a guardar.

## Qué puedes tocar
- `perfil.yml` y, si el investigador te da una foto, una imagen en la raíz del repositorio
  (referénciala en `foto:` por su nombre de archivo).
- No cambies `AGENTS.md`, `CLAUDE.md`, `README.md` ni la carpeta `.github/`, salvo que él lo pida expresamente.

## Cómo editar `perfil.yml`
- Es YAML. Conserva la sangría de dos espacios y los comentarios existentes.
- Pon entre comillas dobles cualquier texto que contenga dos puntos (`:`).
- Campos vacíos se escriben `""` (o `[]` en listas); no los borres.
- Publicaciones: agrega cada obra nueva al inicio de la lista con
  `anio`, `tipo` (libro | articulo | capitulo | ponencia | preprint | editorial | otro), `titulo`,
  `autores`, `fuente`, `enlace`. Solo una obra puede llevar `destacada: true` (con `resumen`).
- Prefiere el enlace DOI (`https://doi.org/...`). No inventes DOI, páginas, años ni coautores:
  si falta un dato, pregúntalo o déjalo vacío.
- La semblanza (`bio`) admite párrafos separados por una línea en blanco y *cursivas* con asteriscos.
  Escríbela en tercera persona, con hechos verificables; esta página la leen buscadores y asistentes de IA.
- Encuadre de la foto (opcional): `foto_zoom` (número, 1 = sin acercar) y `foto_posicion` ("X% Y%").
- Al terminar, cambia `actualizado` a la fecha de hoy (`"AAAA-MM-DD"`).

## Privacidad
- El repositorio es público y el historial también. No agregues teléfonos personales,
  domicilios particulares ni otros datos que el investigador no haya pedido publicar.

## Antes de guardar
- Corre la misma revisión que hace GitHub: `pip install pyyaml && python .github/validar_perfil.py`
- Muestra al investigador un resumen de lo que cambiaste y pide su visto bueno; luego guarda en `main`.
- Mensaje de commit: `Actualiza perfil: <qué cambió>`.
- Al terminar, dale el enlace de su página para que vea el cambio en unos minutos.
