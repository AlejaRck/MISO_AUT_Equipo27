Feature:  Creación de Posts
 
@user1 @web
 Scenario: AUT-001 Creación exitosa de un Post con datos válidos (Positiva)
  
      Given I navigate to page "http://localhost:2368/ghost/#/signin"
      When  Enter the credentials in the login field 
      And   I click on sign in
      Then  I should see the dashboard page
      And   Se encuentra en la sección de Post
      And   da click en el botón “New Post”
      And   el usuario ingresa un título y contenido válidos
      And   selecciona la opción "Publicar"
      And   selecciona la opción "Continuar"
      And   confirma la publicación
      Then  se muestra el mensaje de confirmación de "Boom! It’s out there"

