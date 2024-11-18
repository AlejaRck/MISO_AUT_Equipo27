Feature:  Crear de Posts

@user2 @web
Scenario: AUT-002 Crear Post sin título (Negativo)
  
      Given I navigate to page "http://localhost:2368/ghost/#/signin"
      When  Enter the credentials in the login field 
      And   I click on sign in
      Then  I should see the dashboard page
      And   Se encuentra en la sección de Post
      And   da click en el botón “New Post”
      And   el usuario deja el campo de título vacío y escribe un contenido
      And   selecciona la opción "Publicar"
      And   selecciona la opción "Continuar"
      Then  confirma y el post no es publicado y el usuario permanece en la vista de confirmación