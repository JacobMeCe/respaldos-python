
import os
import shutil
import socket
from datetime import datetime
import paramiko

def archivos_mp3(directorio, nombres):
    ignorados = set()
    for nombre in nombres:
        if nombre.endswith('.mp3'):
            ignorados.add(nombre)
    return ignorados

def enviar_sftp(archivo_zip):
    servidor = ""#servidor
    puerto = 22
    usuario = ""#nombre de usuario
    contrasena = ""#contraseña
    ruta_remota = ""#ruta de respaldo

    try:
        transport = paramiko.Transport((servidor, puerto))
        transport.connect(username=usuario, password=contrasena)

        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(archivo_zip, os.path.join(ruta_remota, os.path.basename(archivo_zip)))

        sftp.close()
        transport.close()
        return True
    except Exception as e:
        print(f"Error al enviar el respaldo: {str(e)}")
        return False

def generar_respaldo():
    nombreEquipo = socket.gethostname()
    ruta = f"C:/Users/{nombreEquipo}/"

    carpetas = [
        os.path.join(ruta, "Descargas"),
        os.path.join(ruta, "Documentos"),
        os.path.join(ruta, "Escritorio"),
        os.path.join(ruta, "Imagenes"),
        os.path.join(ruta, "Musica"),
        os.path.join(ruta, "Videos"),
    ]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archivo_zip = os.path.join(ruta, f"respaldo_{nombreEquipo}_{timestamp}.zip")

    with shutil.make_archive(archivo_zip.split(".")[0], 'zip') as zipf:
        for carpeta in carpetas:
            if os.path.exists(carpeta):
                zipf.write(carpeta, os.path.basename(carpeta), archivos_mp3)

    if enviar_sftp(archivo_zip):
        mensaje = f"Respaldo realizado en: {archivo_zip} y enviado al servidor \n"
    else:
        mensaje = f"Respaldo realizado en: {archivo_zip}, pero no se pudo enviar al servidor \n"

    return mensaje
