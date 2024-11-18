Feature:  Creación de Miembros
 
@user5 @web
 Scenario: AUT-003 Creación exitosa de un Miembro con datos válidos (Positiva)
  
      Given I navigate to page "http://localhost:2368/ghost/#/signin"
      When  Enter the credentials in the login field 
      And   I click on sign in
      Then  I should see the dashboard page
      And   Se encuentra en la sección de Miembros
      And   da click en el botón “New Member”
      And   el usuario ingresa un nombre y correo electrónico válidos
      And   el usuario selecciona la opción "Guardar"
      Then  se muestra al usuario la información del miembro creado