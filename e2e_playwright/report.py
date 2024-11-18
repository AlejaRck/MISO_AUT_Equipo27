import os
import re
from datetime import datetime
import shutil



def create_report():
    base_dir = './e2e_playwright_45/output/resultado_img_version_base'
    rc_dir = './e2e_playwright_rc/output/resultado_img_version_rc'
    diff_images_dir = './output/result_img_diff'



    # Verificar que los directorios existan
    if not os.path.exists(base_dir) or not os.path.exists(rc_dir) or not os.path.exists(diff_images_dir):
        print(f"Error: Uno o más directorios no existen.")
        exit()

    # Crear el directorio para los resultados si no existe
    results_dir = './test-results'
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    # Obtener la lista de imágenes de diferencia
    diff_images = [f for f in os.listdir(diff_images_dir) if f.endswith('.png')]

    if not diff_images:
        print(f"No se encontraron imágenes en {diff_images_dir}.")
        exit()

    # Generar un nombre único para el reporte
    datetime_str = datetime.now().strftime('%Y%m%dT%H%M%S%f')

    # Crear el contenido HTML
    html_content = f"""
    <html>
        <head>
            <title> VRT Report </title>
            <link href="index.css" type="text/css" rel="stylesheet">
        </head>
        <body>
            <h1>Visual Regression Test Report</h1>
            <p>Generated at {datetime_str}</p>
    
            <div id="visualizer">
    """

    # Agregar las imágenes comparadas al reporte HTML
    for diff_image in diff_images:
        # Extraer 'nombre-clave' de la imagen de diferencia usando regex
        match = re.match(r"diff_(.*)\.png", diff_image)
        if match:
            base_name = match.group(1)  # Obtiene 'nombre-clave'
        else:
            print(f"Advertencia: No se encontró un nombre válido para {diff_image}. Saltando...")
            continue

        # Verificar si existen las imágenes correspondientes en las carpetas "before" y "after"
        before_image = os.path.join(base_dir, f"{base_name}.png")
        after_image = os.path.join(rc_dir, f"{base_name}.png")

        if not os.path.exists(before_image) or not os.path.exists(after_image):
            print(f"Advertencia: No se encontraron imágenes para {base_name}. Saltando...")
            continue

        # Agregar el bloque HTML para cada imagen
        html_content += f"""
                <div class="browser">
                    <div class="imgline">
                        <div class="imgcontainer">
                            <span class="imgname">Reference</span>
                            <img class="img2" src=".{before_image}" id="refImage-{before_image}" label="Reference">
                        </div>
                        <div class="imgcontainer">
                            <span class="imgname">Test</span>
                            <img class="img2" src=".{after_image}" id="testImage-{after_image}" label="Test">
                        </div>
                    </div>
                    <div class="imgline">
                        <div class="imgcontainer">
                            <span class="imgname">Diff</span>
                            <img class="imgfull" src=".{os.path.join(diff_images_dir, diff_image)}" id="diffImage-{diff_image}" label="Diff">
                        </div>
                    </div>
                </div>
        """

    # Cerrar el contenido HTML
    html_content += """
            </div>
        </body>
    </html>
    """

    # Guardar el reporte en un archivo HTML
    report_path = os.path.join(results_dir, f"report-{datetime_str}.html")
    with open(report_path, 'w') as report_file:
        report_file.write(html_content)

    # Copiar el archivo CSS si es necesario
    css_file_path = './index.css'
    if os.path.exists(css_file_path):
        css_dest_path = os.path.join(results_dir, f"{datetime_str}-index.css")
        shutil.copy(css_file_path, css_dest_path)

    print(f"Reporte generado: {report_path}")


if __name__ == '__main__':
    create_report()