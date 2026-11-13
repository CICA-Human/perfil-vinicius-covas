"""Revisa perfil.yml antes de que se publique. Lo corre GitHub en cada cambio.
Si encuentra un problema, explica en qué campo está y cómo corregirlo."""
import datetime
import os
import re
import sys

import yaml

TIPOS = {"libro", "articulo", "capitulo", "ponencia", "preprint", "editorial", "otro"}
errores, avisos = [], []


def texto(v):
    return "" if v is None else str(v).strip()


try:
    with open("perfil.yml", encoding="utf-8") as f:
        p = yaml.safe_load(f) or {}
except FileNotFoundError:
    print("::error::No existe perfil.yml en la raíz del repositorio.")
    sys.exit(1)
except yaml.YAMLError as e:
    linea = getattr(getattr(e, "problem_mark", None), "line", None)
    donde = f" (cerca de la línea {linea + 1})" if linea is not None else ""
    print(f"::error file=perfil.yml::El archivo no tiene un formato válido{donde}. "
          "Revisa los espacios al inicio de las líneas y pon entre comillas los textos con dos puntos (:).")
    print(e)
    sys.exit(1)

if not isinstance(p, dict):
    errores.append("El archivo debe ser una lista de campos (nombre:, cargo:, ...).")
    p = {}

if not texto(p.get("nombre")):
    errores.append("Falta el nombre. Agrega una línea como: nombre: Tu Nombre Completo")

color = texto(p.get("color"))
if color and not re.fullmatch(r"#[0-9a-fA-F]{6}", color):
    errores.append(f'El color "{color}" no es válido. Usa el formato "#RRGGBB", por ejemplo "#F29B66".')

foto = texto(p.get("foto"))
if foto and not re.match(r"^(https?:|data:)", foto) and not os.path.isfile(foto):
    errores.append(f'La foto "{foto}" no está en el repositorio. Súbela a la raíz o pega un enlace completo.')
zoom = p.get("foto_zoom")
if zoom not in (None, "") and not isinstance(zoom, (int, float)):
    errores.append("foto_zoom debe ser un número, por ejemplo 1.4.")

orcid = texto((p.get("perfiles") or {}).get("orcid")).replace("https://orcid.org/", "")
if orcid and not re.fullmatch(r"\d{4}-\d{4}-\d{4}-\d{3}[\dX]", orcid):
    errores.append(f'El ORCID "{orcid}" no tiene el formato 0000-0000-0000-0000.')
for clave, valor in (p.get("perfiles") or {}).items():
    v = texto(valor)
    if clave != "orcid" and v and not v.startswith(("http://", "https://")):
        errores.append(f'El enlace de {clave} debe empezar con https://')

correo = texto((p.get("contacto") or {}).get("correo"))
if correo and not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", correo):
    errores.append(f'El correo "{correo}" no parece válido.')

pubs = p.get("publicaciones") or []
if not isinstance(pubs, list):
    errores.append("publicaciones debe ser una lista: cada obra empieza con un guion (-).")
    pubs = []
destacadas = 0
anio_actual = datetime.date.today().year
for i, o in enumerate(pubs, 1):
    if not isinstance(o, dict):
        errores.append(f"La publicación {i} no tiene el formato esperado (anio:, tipo:, titulo:, ...).")
        continue
    nombre = texto(o.get("titulo")) or f"número {i}"
    if not texto(o.get("titulo")):
        errores.append(f"A la publicación {i} le falta el título.")
    tipo = texto(o.get("tipo"))
    if tipo not in TIPOS:
        errores.append(f'"{nombre}": el tipo "{tipo}" no es válido. Usa: {", ".join(sorted(TIPOS))}.')
    anio = texto(o.get("anio"))
    if anio and not (re.fullmatch(r"\d{4}", anio) and 1900 <= int(anio) <= anio_actual + 1):
        errores.append(f'"{nombre}": el año "{anio}" no es válido (usa cuatro cifras, como 2025).')
    enlace = texto(o.get("enlace"))
    if enlace and not enlace.startswith(("http://", "https://")):
        errores.append(f'"{nombre}": el enlace debe empezar con https:// (para un DOI: https://doi.org/...).')
    if o.get("destacada") is True:
        destacadas += 1
if destacadas > 1:
    errores.append(f"Hay {destacadas} obras con destacada: true. Solo puede haber una.")

act = p.get("actualizado")
if act and not isinstance(act, datetime.date) and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", texto(act)):
    avisos.append('La fecha "actualizado" debe tener el formato "AAAA-MM-DD".')

for a in avisos:
    print(f"::warning file=perfil.yml::{a}")
for e in errores:
    print(f"::error file=perfil.yml::{e}")
if errores:
    print(f"\n{len(errores)} problema(s) por corregir.")
    sys.exit(1)
print(f"perfil.yml está bien: {texto(p.get('nombre'))}, {len(pubs)} publicaciones.")
