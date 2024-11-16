import os


class Path:
    path_folder = os.path.dirname(__file__)
    """Path principal del proyecto"""

    input_ = os.path.join(path_folder, '..', 'input')
    """Path donde se encuentran los archivos de entrada"""

    output_ = os.path.join(path_folder, '..', 'output')
    result_img = os.path.join(output_, 'resultado_img')

    config = os.path.join(input_, 'config.yaml')
    """Path donde se encuentran el archivo de config"""

    env = os.path.join(input_, 'credenciales', '.env')
    """Archivo que contiene las variables de entorno"""
