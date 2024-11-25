# MISO_AUT_Equipo27
#integrantes 
Sebastian Betancourth Zapata correo = s.betancourth@uniandes.edu.co
Alejandra pinzon suarez correo = ma.pinzons1@uniandes.edu.co
         
## Instrucciones para ejecutar las pruebas con playwrigh y generar el reporte HTML:

    Clonar el repositorio: Primero, debes clonar el repositorio en tu máquina local utilizando el siguiente comando:

git clone https://github.com/AlejaRck/MISO_AUT_Equipo27

Luego, navega hasta la carpeta llamada e2e_playwright dentro del repositorio clonado:

cd e2e_playwright

Tener python instalado (3.10)
https://www.python.org/downloads/

Crear un entorno virtual de Python: Ahora, es necesario crear un entorno virtual para las pruebas. Utiliza Python 3.10 para asegurarte de que todo funcione correctamente. Para ello, ejecuta:

         1. linux = python3.10 -m venv venv
         2. windwos = python -m venv venv
         3. mac = python3.10 -m venv venv

Activar el entorno virtual: Una vez creado el entorno virtual, actívalo con el siguiente comando:
         
         linuxs = source venv/bin/activate
         windows = venv\Scripts\activate
         mac = source venv/bin/activate

Instalar las dependencias: Con el entorno virtual activado, instala las dependencias necesarias ejecutando:

pip install -r requirements.txt

En este punto ya puede ejecutar el script de main_escenarios_data.py para realizar las pruebas con la generación de datos 
