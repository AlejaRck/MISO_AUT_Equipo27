Feature:  Crear Página

@user4 @web
Scenario: AUT-007 Intentar crear una página sin contenido (Negativo)
      Given I navigate to page "http://localhost:2368/ghost/#/signin"
      When  Enter the credentials in the login field 
      And   I click on sign in
      Then  I should see the dashboard page
      And   Se encuentra en la sección de Páginas
      And   da click en el botón "New Page"
      And   el usuario ingresa un título y deja el contenido vacío
      And   selecciona la opción "Publicar"
      And   selecciona la opción "Continuar"
      Then  No se publica la página y el usuario permanece en la vista de confirmación

