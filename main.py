import subprocess
import os


def transponedor(name):
    carpeta_mkv = "C:/Users/NEAT-H1/Videos/CYGYC/mkv/"
    carpeta_webm ="C:/Users/NEAT-H1/Videos/CYGYC/webm/"

    videos_a_transformar = []
    extension_mkv = ".mkv"
    extension_webm = ".webm"

    for archivo in os.listdir(carpeta_mkv):
        if archivo.endswith(extension_mkv):
            videos_a_transformar.append(archivo)

    for video in videos_a_transformar:
        nombre_video_completo = video.title()
        nombre_video = nombre_video_completo[:-4]
        print(nombre_video)
        # Define la instrucción que deseas ejecutar
        comando = f"ffmpeg -y -i {nombre_video}{extension_mkv} -q:a 0 -q:v 0 {carpeta_webm}{nombre_video}{extension_webm}"
        print(comando)
        # Ejecuta el comando y captura la salida
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True, cwd=carpeta_mkv)
        # Imprime la salida del comando
        print(resultado.stdout)
        # Imprime la salida de error, si la hubiera
        print(resultado.stderr)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    transponedor('PyCharm')

