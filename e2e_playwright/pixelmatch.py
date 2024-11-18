import os
import subprocess
from metadata.path import Path

# Crear carpeta de salida si no existe
os.makedirs(Path.result_diff_imge, exist_ok=True)

# Iterar sobre las imágenes en la carpeta base
for file_name in os.listdir(Path.result_img_version_base):
    base_path = os.path.join(Path.result_img_version_base, file_name)
    vrc_path = os.path.join(Path.result_img_versrion_rc, file_name)
    diff_path = os.path.join(Path.result_diff_imge, f"diff_{file_name}")

    # Verificar si la imagen existe en ambas carpetas
    if os.path.exists(base_path) and os.path.exists(vrc_path):
        print(f"Comparando: {file_name}")

        # Llamar al script de Node.js con las rutas de las imágenes
        subprocess.run(["node", "compare.js", base_path, vrc_path, diff_path])
    else:
        print(f"Archivo no encontrado en ambas carpetas: {file_name}")
