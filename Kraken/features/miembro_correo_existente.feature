Feature:  Crear Miembro
 
@user8 @web
 Scenario: AUT-005 Intentar crear un miembro con correo electrónico ya existente (Negativo)
  
      Given I navigate to page "http://localhost:2368/ghost/#/signin"
      When  Enter the credentials in the login field 
      And   I click on sign in
      Then  I should see the dashboard page
      And   Se encuentra en la sección de Miembros
      And   da click en el botón “New Member”
      And   el usuario ingresa un nombre y correo electrónico válidos
      And   el usuario selecciona la opción "Guardar"
      And   Ingresa nuevamente a la sección de Miembros
      And   Intenta crear un nuevo miembro con el mismo correo
      And   el usuario selecciona la opción "Guardar"
      Then  se muestra el mensaje de error indicando "El correo electrónico ya está en uso"

       