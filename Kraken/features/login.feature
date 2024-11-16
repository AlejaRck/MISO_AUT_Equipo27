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


Feature:  Creación de Páginas

@user3 @web
 Scenario: AUT-006 Creación exitosa de una Página con datos válidos (Positiva)
  
      Given I navigate to page "http://localhost:2368/ghost/#/signin"
      When  Enter the credentials in the login field 
      And   I click on sign in
      Then  I should see the dashboard page
      And   Se encuentra en la sección de Páginas
      And   da click en el botón "New Page"
      And   el usuario ingresa un título y contenido válidos
      And   selecciona la opción "Publicar"
      And   selecciona la opción "Continuar"
      And   confirma la publicación
      Then  se muestra el mensaje de confirmación de "Boom! It’s out there"

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