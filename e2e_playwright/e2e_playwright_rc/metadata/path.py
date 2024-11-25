import os


class Path:
    path_folder = os.path.dirname(__file__)
    """Path principal del proyecto"""

    input_ = os.path.join(path_folder, '..', 'input')
    """Path donde se encuentran los archivos de entrada"""
    input_mockaroo = os.path.join(input_, 'mockaroo')

    output_ = os.path.join(path_folder, '..', 'output')
    result_img_version_base = os.path.join(output_, 'resultado_img_version_base')
    result_img_versrion_rc = os.path.join(output_, 'resultado_img_version_rc')
    result_diff_imge = os.path.join(output_, 'resultado_img_diff')


    config = os.path.join(input_, 'config.yaml')
    """Path donde se encuentran el archivo de config"""

    env = os.path.join(input_, 'credenciales', '.env')
    """Archivo que contiene las variables de entorno"""
