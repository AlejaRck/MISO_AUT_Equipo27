Feature:  Creación de Tags
 
@user6 @web
 Scenario: AUT-010 Creación exitosa de un tag con datos válidos (Positiva)
  
      Given I navigate to page "http://localhost:2368/ghost/#/signin"
      When  Enter the credentials in the login field 
      And   I click on sign in
      Then  I should see the dashboard page
      And   Se encuentra en la sección de Tags
      And   da click en el botón “New Tag”
      And   el usuario ingresa un nombre válido para el tag
      And   el usuario selecciona la opción "Guardar"
      Then  se crea el tag y se muestra en la lista de tags