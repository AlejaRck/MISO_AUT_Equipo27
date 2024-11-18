Feature:  Crear de Miembros
 
@user7 @web
 Scenario: AUT-004 Intentar crear un miembro sin correo electrónico (Negativo)
  
      Given I navigate to page "http://localhost:2368/ghost/#/signin"
      When  Enter the credentials in the login field 
      And   I click on sign in
      Then  I should see the dashboard page
      And   Se encuentra en la sección de Miembros
      And   da click en el botón “New Member”
      And   el usuario selecciona la opción "Guardar"
      Then  se muestra un mensaje de error indicando "Por favor ingrese un correo"
      And   el usuario permanece en la vista de crear tag