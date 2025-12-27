from . import DownVi as app

from flask import request, send_file, jsonify
import yt_dlp
import io


@app.route('/descargar', methods=["POST"])
def descargar():
    url = request.form.get("url")
    if not url:
        return jsonify({'message': 'no se envio url'})

    try:
        # Usamos un buffer en memoria
        buffer = io.BytesIO()

        # Configuración de yt-dlp para escribir en memoria
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": "-",  # "-" indica salida a stdout
            "quiet": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            # Descargar el archivo en binario
            data = ydl.urlopen(info['url']).read()
            buffer.write(data)
            buffer.seek(0)

        filename = f"{info['title']}.mp4"

        # Enviar el archivo al navegador
        return send_file(
            buffer,
            as_attachment=True,
            download_name=filename,
            mimetype="video/mp4"
        )

    except Exception as e:
        return jsonify({'message': str(e)})