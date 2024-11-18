PRUEBAS AUTOMATIZADAS CON KRAKEN (VERSION 5.96)
Equipo: 27 
Integrantes: 
* Sebastian Betancourth Zapata (s.betancourth@uniandes.edu.co)
* Alejandra Pinzón Suárez (ma.pinzons1@uniandes.edu.co) 

INSTRUCCIONES DE INSTALACIÓN: (Instrucciones para Mackbook con Chip Intel. No se asegura que sean compatibles con otros dispositivos) 
* Precondiciones dependencias: 
  Contar con las siguientes instalaciones de forma global en la máquina: 
  - Node.js - Versión 16 (En caso de no tenerlo instalar con nvm)
  - Appium  (En caso de no tenerlo instalar con el comando npm install -g appium )
* Instalación Kraken 
  - Ejecutar el comando npm install kraken-node -g fuera del directorio principal del proyecto  
  - Crear un directorio en la ubicación de su preferencia y estando adentro ejecutar el comando kraken-node gen
  - Igualmente estando dentro del directorio ejecute el comando npm install kraken-node 
  - Verificar que esté usando la versión de 16 de node.
* Preparación ambiente de pruebas. 
  - Iniciar Ghost 5.96 (En caso de no tenerlo instalar siguiendo la documentación del link https://ghost.org/docs/install/)
  - Crear un usuario Administrador  en Ghost
  - Clonar el repositorio https://github.com/AlejaRck/MISO_AUT_Equipo27 y ubicarse en el branch main
  - Modificar las credenciales de acceso en el archivo step.js (Lineas 9 y 10)
* Preparación data para ejecución 
  - Tener un usuario nuevo y haber realizado el onboarding de Ghost
  - Contar solo con el tag que se crea por defecto 
* Ejecución de las pruebas
  - Ejecutar el comando npx kraken-node run para iniciar la ejecución 