
import json
import os
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests

API_ENDPOINT = "https://www.googleapis.com/youtube/v3/commentThreads"
VIDEO_ID = "M6aisVwwkEg"
VIDEO_URL = f"https://youtu.be/{VIDEO_ID}"
MAX_COMENTARIOS = 500
SALIDA = Path("comentarios_youtube.csv")
METADATOS = Path("comentarios_youtube_metadata.json")


def obtener_clave():
    clave = os.getenv("YOUTUBE_API_KEY", "").strip()
    if not clave:
        try:
            from google.colab import userdata
            clave = (userdata.get("YOUTUBE_API_KEY") or "").strip()
        except (ImportError, KeyError, AttributeError):
            pass
    if not clave:
        raise RuntimeError("Configura YOUTUBE_API_KEY en las variables de entorno o Secrets de Colab.")
    return clave


def extraer(api_key):
    filas, token = [], None
    paginas = 0
    fecha_consulta = datetime.now(timezone.utc).isoformat()
    while len(filas) < MAX_COMENTARIOS:
        params = {
            "key": api_key,
            "part": "snippet",
            "videoId": VIDEO_ID,
            "maxResults": min(100, MAX_COMENTARIOS - len(filas)),
            "textFormat": "plainText",
            "order": "time",
        }
        if token:
            params["pageToken"] = token
        response = requests.get(API_ENDPOINT, params=params, timeout=30)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            try:
                mensaje = response.json().get("error", {}).get("message", response.text[:300])
            except ValueError:
                mensaje = response.text[:300]
            raise RuntimeError(f"YouTube API: {mensaje}") from e
        datos = response.json()
        paginas += 1
        for item in datos.get("items", []):
            snippet = item["snippet"]["topLevelComment"]["snippet"]
            filas.append({
                "texto": snippet.get("textDisplay", ""),
                "fecha": snippet.get("publishedAt", ""),
                "likes": snippet.get("likeCount", 0),
            })
        token = datos.get("nextPageToken")
        if not token:
            break
    return filas[:MAX_COMENTARIOS], paginas, fecha_consulta


def main():
    filas, paginas, fecha = extraer(obtener_clave())
    df = pd.DataFrame(filas, columns=["texto", "fecha", "likes"])
    # Conservamos cada comentario extraído, también duplicados o vacíos,
    # para que la limpieza y sus conteos se documenten por separado.
    df.to_csv(SALIDA, index=False, encoding="utf-8-sig")
    metadata = {
        "video_url": VIDEO_URL,
        "video_id": VIDEO_ID,
        "endpoint": API_ENDPOINT,
        "fecha_extraccion_utc": fecha,
        "fecha_ejecucion_utc": datetime.now(timezone.utc).isoformat(),
        "max_comentarios": MAX_COMENTARIOS,
        "comentarios_extraidos": len(df),
        "paginas_consultadas": paginas,
        "orden": "time",
        "alcance": "Solo comentarios de primer nivel; no se descargan respuestas anidadas",
        "campos": ["texto", "fecha", "likes"],
    }
    METADATOS.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Video: {VIDEO_URL}\nComentarios extraídos: {len(df)}\nArchivo: {SALIDA}\nMetadatos: {METADATOS}")
    try:
        from google.colab import files
        files.download(str(SALIDA))
        files.download(str(METADATOS))
    except ImportError:
        pass


if __name__ == "__main__":
    main()
