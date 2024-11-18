Feature:  Configuración información del sitio 
 
@user5 @web
Scenario: AUT-008 Actualización exitosa de la información del sitio
  
      Given I navigate to page "http://localhost:3001/ghost/#/signin"
      When  Enter the credentials in the login field 
      And   I click on sign in
      Then  I should see the dashboard page
      And   El usuario ingresa a la opción Settings a la sección Título y Descripción
      And   el usuario ingresa un nuevo título y descripción para el sitio
      And   selecciona la opción "Guardar"
      Then  El sistema confirma la actualización de la información 
      

      
