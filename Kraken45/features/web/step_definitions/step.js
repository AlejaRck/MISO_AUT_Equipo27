const { Given, When, Then } = require('@cucumber/cucumber');

//Login

When('Enter the credentials in the login field', async function () {
    const email = "ma.pinzons1@uniandes.edu.co"; 
    const password = "Monkey2024*";
  
    const emailField = await this.driver.$('input[name="identification"]');
    const passwordField = await this.driver.$('input[name="password"]');
  
    await emailField.waitForDisplayed({ timeout: 5000 });
    await emailField.setValue(email);
  
    await passwordField.waitForDisplayed({ timeout: 5000 });
    await passwordField.setValue(password);
  });

  When ('I click on sign in', async function () {
    const signInButton = await this.driver.$('.login');
    await signInButton.waitForClickable({ timeout: 5000 });
    await signInButton.click();
  });


// Page Home aplicación 
Then('I should see the dashboard page', async function () {
    const titleHomePage = await this.driver.$('h2.gh-canvas-title');
    console.log(titleHomePage + " titleHomePage")
    const titleText = await titleHomePage.getText();
      try {
        await titleHomePage.waitForDisplayed({ timeout: 5000 });
        if(titleHomePage.isDisplayed() && titleText=='Dashboard'){
          console.log('Title home screen is displayed');
        }
      } catch (error) {
          throw new Error('Title home screen is not displayed'); 
      } 
  });
  
  
  
  // Page Listar Post 
  
  When('Se encuentra en la sección de Post', async function () {
    const link = await this.driver.$('.//a[@href="#/posts/"]');
    const labelSectionPost = await link.getText();
    console.log(labelSectionPost + " texto link test");
  
    try {
      await link.waitForDisplayed({ timeout: 5000 });
      if(link.isDisplayed() && labelSectionPost=='Posts'){
        console.log('test');
        await link.click(); 
        console.log('Entry to Post section');
      }
    } catch (error) {
        throw new Error('Post section is not displayed'); 
    }
  })
  
  When ('da click en el botón “New Post”', async function () {
    const buttonNewPost = await this.driver.$('.gh-btn-primary');
    const labelButtonNewPost = await buttonNewPost.getText();
    console.log(labelButtonNewPost + " texto boton")
  
    try {
      await buttonNewPost.waitForDisplayed({ timeout: 5000 });
      if(buttonNewPost.isDisplayed() && labelButtonNewPost=='New post'){
        console.log('into test');
        await buttonNewPost.click(); 
        console.log('Entry to Create new Post');
      }
    } catch (error) {
        throw new Error('Post new screen is not displayed'); 
    }
    
  })
  
  // Page Crear Post 
  function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
  
  When ('el usuario ingresa un título y contenido válidos', async function () {
    const labelNewTitle = await this.driver.$('.gh-editor-title');
    const bodyNewContent = await this.driver.$('.koenig-editor__editor');
    let consecutive = getRandomInt (1,100);
    console.log(labelNewTitle + " Nuevo titulo " + consecutive )
    await labelNewTitle.setValue('Nuevo titulo de prueba ' + consecutive)
    await bodyNewContent.waitForDisplayed ({ timeout: 3000 });
    await bodyNewContent.setValue('Contenido nuevo')
  })
  
  When ('el usuario deja el campo de título vacío y escribe un contenido', async function () {
    const labelTitleNewPost = await this.driver.$('.gh-editor-title');
    const bodyNewPost = await this.driver.$('.kg-prose');
    console.log(labelTitleNewPost + "...titulo vacio nuevo post")
    await labelTitleNewPost.setValue(''  )
    await bodyNewPost.waitForDisplayed ({ timeout: 3000 });
    await bodyNewPost.setValue('Contenido nuevo post')
  })
  
  
  When ('selecciona la opción "Publicar"', async function () {
    const buttonPublish = await this.driver.$('.gh-publishmenu-trigger');
    await buttonPublish.waitForDisplayed({ timeout: 5000 })
    console.log ('Boton publicar ' + buttonPublish)
    await buttonPublish.click();
  })
  
  // Page confirmación publicacion Post
  
  When ('confirma la publicación', async function () { 
    const buttonConfirm = await this.driver.$('.gh-publishmenu-button');
    await buttonConfirm.waitForDisplayed({ timeout: 5000 })
    console.log ('Boton publish ' + buttonConfirm)
    await buttonConfirm.click();
  })
  
  Then ('se muestra el mensaje de confirmación de la publicación', async function () {
    const notifyPublish = await this.driver.$('.gh-notification-title');
    const textNotify = await notifyPublish.getText();
    console.log ( textNotify + 'textNotify')
    try {
      await notifyPublish.waitForDisplayed({ timeout: 2000 });
      if(notifyPublish.isDisplayed() && textNotify=="Published"){
        console.log('Post was published successfully');
      }
    } catch (error) {
        throw new Error('Post was not published successfully'); 
    }
  
  })

  // Page Listar páginas

  When('Se encuentra en la sección de Páginas', async function () {
    const linkPage = await this.driver.$('.//a[@href="#/pages/"]');
    const labelSectionPages = await linkPage.getText();
    console.log(labelSectionPages + " texto link test");
  
    try {
      await linkPage.waitForDisplayed({ timeout: 5000 });
      if(linkPage.isDisplayed() && labelSectionPages=='Pages'){
        console.log('test Pages');
        await linkPage.click(); 
        console.log('Entry to Pages section');
      }
    } catch (error) {
        throw new Error('Pages section is not displayed'); 
    }
  })

  When ('da click en el botón "New Page"', async function () {
    const buttonNewPage = await this.driver.$('.gh-btn-primary');
    const labelButtonNewPage= await buttonNewPage.getText();
    console.log(labelButtonNewPage + " texto boton Page")
  
    try {
      await buttonNewPage.waitForDisplayed({ timeout: 5000 });
      if(buttonNewPage.isDisplayed() && labelButtonNewPage=='New page'){
        console.log('into test page');
        await buttonNewPage.click(); 
        console.log('Entry to Create new Page');
      }
    } catch (error) {
        throw new Error('Page new screen is not displayed'); 
    }
    
  })

  // Page listar Miembros
When('Se encuentra en la sección de Miembros', async function () {
    const linkMembers = await this.driver.$('a[href="#/members/"]');
    console.log('click seccion miembros');
    try {
      await linkMembers.waitForDisplayed({ timeout: 5000 });
      console.log(linkMembers + "...link test members here");
      if(linkMembers.isDisplayed()){
        console.log('test');
        await linkMembers.click(); 
        console.log('Entry to Members section');
      }
    } catch (error) {
        throw new Error('Members section is not displayed'); 
    }
  })
  
  When ('da click en el botón “New Member”', async function () {
    const buttonNewMember = await this.driver.$('.gh-btn-primary');
    const labelButtonNewMember= await buttonNewMember.getText();
    console.log(labelButtonNewMember + " texto boton Page")
  
    try {
      await buttonNewMember.waitForDisplayed({ timeout: 5000 });
      if(buttonNewMember.isDisplayed() && labelButtonNewMember=='New member'){
        console.log('into test page');
        await buttonNewMember.click(); 
        console.log('Entry to Create new Member');
      }
    } catch (error) {
        throw new Error('Member new screen is not displayed'); 
    }
    
  })

  When ('el usuario ingresa un nombre y correo electrónico válidos', async function () {
    const inputName = await this.driver.$('#member-name');
    const inputEmail = await this.driver.$('#member-email');
    let randomNum = getRandomInt (1,100);
    await inputName.setValue('Nuevo nombre ' + randomNum);
    await inputEmail.setValue('newmember' + randomNum + '@gmail.com');
  })

  When ('el usuario selecciona la opción "Guardar"', async function () {
    const buttonSave= await this.driver.$('.gh-btn-primary');
    await buttonSave.waitForClickable({ timeout: 5000 })
    await buttonSave.click();
  })

  Then ('se muestra al usuario la información del miembro creado', async function () {
    await new Promise(resolve => setTimeout(resolve, 2000));
    const linkPost = await this.driver.$('.//a[@href="#/posts/"]');
    const linkMembers = await this.driver.$('a[href="#/members/"]');
    await linkPost.waitForClickable({ timeout: 5000 })
    await linkMembers.waitForClickable({ timeout: 5000 })
    await linkPost.click();
    await linkMembers.click();
    const memberInformation = await this.driver.$("//h3[contains(text(), 'Nuevo nombre')]");
    const labelInformation = await memberInformation.getText();
    const nameMember = labelInformation.substring(0, 12);
    console.log (nameMember +  " informacion miembro");
  
    try {
      await memberInformation.waitForDisplayed ({timeout: 5000 });
  
      if(memberInformation.isDisplayed() && nameMember=='Nuevo nombre'){
        console.log('Member created successfully');
      } else 
        console.log ('Error: Member is not created'); 
    } catch (error) {
        throw new Error('Member is not created'); 
    }
     
  })

  When('Se encuentra en la sección de Tags', async function () {
    const linkTags = await this.driver.$('.//a[@href="#/tags/"]');
    const labelSectionTags = await linkTags.getText();
    console.log(labelSectionTags + " texto link tags");
  
    try {
      await linkTags.waitForDisplayed({ timeout: 5000 });
      if(linkTags.isDisplayed() && labelSectionTags=='Tags'){
        console.log('test tags');
        await linkTags.click(); 
        console.log('Entry to Tags section');
      }
    } catch (error) {
        throw new Error('Tags section is not displayed'); 
    }
  })
  
  When ('da click en el botón “New Tag”', async function () {
    const buttonNewTag = await this.driver.$('.//a[@href="#/tags/new/"]');
    const labelButtonNewTag= await buttonNewTag.getText();
    console.log(labelButtonNewTag + " texto boton Tags")
  
    try {
      await buttonNewTag.waitForDisplayed({ timeout: 5000 });
      if(buttonNewTag.isDisplayed() && labelButtonNewTag=='New tag'){
        console.log('into test tag');
        await buttonNewTag.click(); 
        console.log('Entry to Create new Tag');
      }
    } catch (error) {
        throw new Error('Tag new screen is not displayed'); 
    }
    
  })

  // Page crear Tags

  When ('el usuario ingresa un nombre válido para el tag', async function () {
    const inputNameTag = await this.driver.$('#tag-name');
    let randomNum = getRandomInt (1,100);
    await inputNameTag.setValue('NuevoTag ' + randomNum);
    console.log (inputNameTag + " Nuevo tag")
  })

  Then ('se crea el tag y se muestra en la lista de tags', async function () {
    await new Promise(resolve => setTimeout(resolve, 2000));
    const linkTags = await this.driver.$('.//a[@href="#/tags/"]');
    await linkTags.waitForClickable({ timeout: 5000 })
    await linkTags.click();
    console.log ('verificacion tag creado');
    const tagInformation = await this.driver.$$('h3.gh-tag-list-name');
    const extInformation = tagInformation[2];
    const labelInformation = await extInformation.getText();
    const nameTag = labelInformation.substring(0, 8);
    console.log (nameTag +  " informacion tag substring");
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    if(nameTag=='NuevoTag'){
        console.log('Tag created successfully');
    } else 
        console.log ('Error: Tag is not created'); 
    
  })
