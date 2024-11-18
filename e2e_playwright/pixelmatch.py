import os
import subprocess

def resgresion_visual():

    imagenes_base = 'e2e_playwright_45/output/resultado_img_version_base'
    imagenes_rc = 'e2e_playwright_rc/output/resultado_img_version_rc'
    out_diff_imagen = 'output/result_img_diff'

    os.makedirs(out_diff_imagen, exist_ok=True)


    # Iterar sobre las imágenes en la carpeta base
    for file_name in os.listdir(imagenes_base):
        base_path = os.path.join(imagenes_base, file_name)
        vrc_path = os.path.join(imagenes_rc, file_name)
        diff_path = os.path.join(out_diff_imagen, f"diff_{file_name}")

        # Verificar si la imagen existe en ambas carpetas
        if os.path.exists(base_path) and os.path.exists(vrc_path):
            print(f"Comparando: {file_name}")

            # Llamar al script de Node.js con las rutas de las imágenes
            subprocess.run(["node", "pixelmatch.js", base_path, vrc_path, diff_path])
        else:
            print(f"Archivo no encontrado en ambas carpetas: {file_name}")


if __name__ == '__main__':
    resgresion_visual()