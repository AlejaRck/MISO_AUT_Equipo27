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

Ademas se deben instalar las dependencias necesarias para el pixelmatch.js:

         1. Se debe tener insalado node v20.18.0
         
         2. instalar pixelmatch con npm install pngjs pixelmatch
         
         3. Edita el archivo package.json: Agrega "type": "module" en la raíz del archivo package.json de tu proyecto:
         
```json
{
    "type": "module",
    "dependencies": {
        // otras dependencias
    }
}
``` 

Consideraciones
Dentro de la carpeta de cada versión (e2e_playwright_45, e2e_playwright_rc), es necesario modificar el archivo ubicado en la carpeta input. En este archivo, se debe configurar lo siguiente:

    1. URL de Ghost: Proporcionar la dirección del servidor de Ghost que se utilizará.
    2. Usuario: Especificar el nombre de usuario con permisos para acceder al sistema.
    3. Contraseña: Incluir la contraseña asociada al usuario.
    
Asegúrate de guardar los cambios correctamente antes de continuar con la ejecución del proyecto

ejemplo:
```yaml
ghost_url: http://localhost:3001/ghost: "module"
admin_user: pruebas@gmail.com
admin_pass: Lego123456789
```

Ejecutar las pruebas de e2e_playwright: Ahora, puedes ejecutar las pruebas. Para hacerlo, ejecuta el archivo main.py con el siguiente comando:

         para la version base main.py =  main_version_base.py
         
         para la version rc main.py = main_version_rc.py

         para la verison final (Entrega Semana 8) main.py = main_entrega_final.py
         
         linux = python3 main.py
         
         mac =  python3 main.py
         
         windows = python3 main.py

Ejecutar pruebas de regresión visual:

         linux = python3 pixelmatch.py
         
         mac =  python3 pixelmatch.py
         
         windows = python3 pixelmatch.py

Crear reporte de la regresión visual:
         
         linux = python3 report.py
         
         mac =  python3 report.py
         
         windows = python3 report.py

Este comando ejecutará las pruebas y, al finalizar, generará un reporte en formato HTML en la carpeta test-result que podrás revisar para ver los resultados.
