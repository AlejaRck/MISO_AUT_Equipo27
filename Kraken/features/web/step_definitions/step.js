const { Given, When, Then } = require('@cucumber/cucumber');
const loginFlow = require('../pages/loginFlow');
const assert = require ('assert');
 

// Login App 

When('Enter the credentials in the login field', async function () {
  const email = "ma.pinzons1@uniandes.edu.co"; 
  const password = "Monkey2024*";

  const emailField = await this.driver.$('#identification');
  const passwordField = await this.driver.$('#password');

  await emailField.waitForDisplayed({ timeout: 5000 });
  await emailField.setValue(email);

  await passwordField.waitForDisplayed({ timeout: 5000 });
  await passwordField.setValue(password);
});

When ('I click on sign in', async function () {
  const signInButton = await this.driver.$('#ember5');
  await signInButton.waitForClickable({ timeout: 5000 });
  await signInButton.click();
});

// Page Home aplicación 
Then('I should see the dashboard page', async function () {
  const titleHomePage = await this.driver.$('h2.gh-canvas-title');
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

When ('El usuario ingresa a la opción Settings', async function () {
  const linkSettings = await this.driver.$('.//a[@href="#/settings/"]');
  await linkSettings.waitForClickable({ timeout: 5000 })
  await linkSettings.click();
  
})

When ('El usuario ingresa a la opción Settings a la sección Título y Descripción', async function () {
  const generalSettings = await this.driver.$('.//a[@href="#/settings/"]');
  await generalSettings.waitForClickable({ timeout: 5000 })
  await generalSettings.click();
})


// Page Listar Post 

When('Se encuentra en la sección de Post', async function () {
  const link = await this.driver.$('.//a[@href="#/posts/"]');
  const labelSectionPost = await link.getText();
  try {
    await link.waitForDisplayed({ timeout: 5000 });
    if(link.isDisplayed() && labelSectionPost=='Posts'){
      await link.click(); 
      console.log('Entry to Post section');
    }
  } catch (error) {
      throw new Error('Post section is not displayed'); 
  }
})

When ('da click en el botón “New Post”', async function () {
  const buttonNewPost = await this.driver.$('[data-test-new-post-button]');
  const labelButtonNewPost = await buttonNewPost.getText();

  try {
    await buttonNewPost.waitForDisplayed({ timeout: 5000 });
    if(buttonNewPost.isDisplayed() && labelButtonNewPost=='New post'){
      await buttonNewPost.click(); 
      console.log('Entry to Create new Post');
    }
  } catch (error) {
      throw new Error('Post new screen is not displayed'); 
  }
  
})

// Page listar Pages 
When('Se encuentra en la sección de Páginas', async function () {
  const linkPage = await this.driver.$('.//a[@href="#/pages/"]');
  const labelSectionPages = await linkPage.getText();

  try {
    await linkPage.waitForDisplayed({ timeout: 5000 });
    if(linkPage.isDisplayed() && labelSectionPages=='Pages'){
      await linkPage.click(); 
      console.log('Entry to Pages section');
    }
  } catch (error) {
      throw new Error('Pages section is not displayed'); 
  }
})

When ('da click en el botón "New Page"', async function () {
  const buttonNewPage = await this.driver.$('[data-test-new-page-button]');
  const labelButtonNewPage= await buttonNewPage.getText();

  try {
    await buttonNewPage.waitForDisplayed({ timeout: 5000 });
    if(buttonNewPage.isDisplayed() && labelButtonNewPage=='New page'){
      await buttonNewPage.click(); 
      console.log('Entry to Create new Page');
    }
  } catch (error) {
      throw new Error('Page new screen is not displayed'); 
  }
  
})

// Page listar Miembros
When('Se encuentra en la sección de Miembros', async function () {
  const linkMembers = await this.driver.$('a[data-test-nav="members"]');
  try {
    await linkMembers.waitForDisplayed({ timeout: 5000 });
    if(linkMembers.isDisplayed()){
      await linkMembers.click(); 
      console.log('Entry to Members section');
    }
  } catch (error) {
      throw new Error('Members section is not displayed'); 
  }
})

When ('da click en el botón “New Member”', async function () {
  const buttonNewMember = await this.driver.$('[data-test-new-member-button]');
  const labelButtonNewMember= await buttonNewMember.getText();

  try {
    await buttonNewMember.waitForDisplayed({ timeout: 5000 });
    if(buttonNewMember.isDisplayed() && labelButtonNewMember=='New member'){
      await buttonNewMember.click(); 
      console.log('Entry to Create new Member');
    }
  } catch (error) {
      throw new Error('Member new screen is not displayed'); 
  }
  
})

Then('Ingresa nuevamente a la sección de Miembros', async function () {
  const linkMembers = await this.driver.$('a[data-test-nav="members"]');
  await linkMembers.waitForDisplayed({ timeout: 5000 });
  await linkMembers.click(); 
})

// Page listar tags 

When('Se encuentra en la sección de Tags', async function () {
  const linkTags = await this.driver.$('.//a[@href="#/tags/"]');
  const labelSectionTags = await linkTags.getText();

  try {
    await linkTags.waitForDisplayed({ timeout: 5000 });
    if(linkTags.isDisplayed() && labelSectionTags=='Tags'){
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

  try {
    await buttonNewTag.waitForDisplayed({ timeout: 5000 });
    if(buttonNewTag.isDisplayed() && labelButtonNewTag=='New tag'){
      await buttonNewTag.click(); 
      console.log('Entry to Create new Tag');
    }
  } catch (error) {
      throw new Error('Tag new screen is not displayed'); 
  }
  
})
// Page Crear Post 
function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

When ('el usuario ingresa un título y contenido válidos', async function () {
  const labelNewTitle = await this.driver.$('.gh-editor-title');
  const bodyNewContent = await this.driver.$('.kg-prose');
  let consecutive = getRandomInt (1,100);
  await labelNewTitle.setValue('Nuevo titulo de prueba ' + consecutive)
  await bodyNewContent.waitForDisplayed ({ timeout: 3000 });
  await bodyNewContent.setValue('Contenido nuevo')
})

When ('el usuario deja el campo de título vacío y escribe un contenido', async function () {
  const labelTitleNewPost = await this.driver.$('.gh-editor-title');
  const bodyNewPost = await this.driver.$('.kg-prose');
  await labelTitleNewPost.setValue(''  )
  await bodyNewPost.waitForDisplayed ({ timeout: 3000 });
  await bodyNewPost.setValue('Contenido nuevo post')
})


When ('selecciona la opción "Publicar"', async function () {
  const buttonPublish = await this.driver.$('[data-test-button="publish-flow"]');
  await buttonPublish.waitForDisplayed({ timeout: 5000 })
  await buttonPublish.click();
})

// Page confirmación publicacion Post
When ('selecciona la opción "Continuar"', async function () {
  const buttonContinue = await this.driver.$('button[data-test-button="continue"] span');
  await buttonContinue.waitForDisplayed({ timeout: 5000 })
  await buttonContinue.click();
})

When ('confirma la publicación', async function () { 
  const buttonConfirm = await this.driver.$('button[data-test-button="confirm-publish"]');
  await buttonConfirm.waitForDisplayed({ timeout: 5000 })
  await buttonConfirm.click();
})

Then ('se muestra el mensaje de confirmación de "Boom! It’s out there"', async function () {
  const modalPostPublished = await this.driver.$('.modal-content');
  await modalPostPublished.waitForDisplayed({ timeout: 5000 });
  const titleModal = await this.driver.$('.modal-content h1 span:first-child', el => el.textContent.trim());
  const textModal = await titleModal.getText();
  try {
    await titleModal.waitForDisplayed({ timeout: 5000 });
    if(titleModal.isDisplayed() && textModal=="Boom! It's out there."){
      console.log('Post was published successfully');
    }
  } catch (error) {
      throw new Error('Post was not published successfully'); 
  }

})

Then ('confirma y el post no es publicado y el usuario permanece en la vista de confirmación', async function () {
  await new Promise(resolve => setTimeout(resolve, 2000));
  
  const buttonConfirm = await this.driver.$('button[data-test-button="confirm-publish"]');
  const buttonBackToSettings = await this.driver.$('.gh-btn.gh-btn-link.gh-btn-large.gh-publish-cta-secondary')
  const labelButtonBack = await buttonBackToSettings.getText ();
  await buttonConfirm.click();

  try {
    await buttonConfirm.waitForDisplayed ({timeout: 5000 });
    await buttonBackToSettings.waitForDisplayed ({timeout: 5000 });

    if(buttonConfirm.isDisplayed() && labelButtonBack=='Back to settings'){
      console.log('Post without title was not published');
    } else 
      console.log ('Error: Post title is empty'); 
  } catch (error) {
      throw new Error('Post title is empty'); 
  }
})

Then ('No se publica la página y el usuario permanece en la vista de confirmación', async function () {
  await new Promise(resolve => setTimeout(resolve, 2000));
  
  const buttonConfirm = await this.driver.$('button[data-test-button="confirm-publish"]');
  const buttonBackToSettings = await this.driver.$('.gh-btn.gh-btn-link.gh-btn-large.gh-publish-cta-secondary')
  const labelButtonBack = await buttonBackToSettings.getText ();
  await buttonConfirm.click();

  try {
    await buttonConfirm.waitForDisplayed ({timeout: 5000 });
    await buttonBackToSettings.waitForDisplayed ({timeout: 5000 });

    if(buttonConfirm.isDisplayed() && labelButtonBack=='Back to settings'){
      console.log('Page without content was not published');
    } else 
      console.log ('Error: Page content is empty'); 
  } catch (error) {
      throw new Error('Page content is empty'); 
  }
})

When('El usuario retorna a la vista de listar Post', async function () {
  //const buttonClose =  await this.driver.$('[data-test-button="close-publish-flow"]');
  const buttonClose =  await this.driver.$('.close');
  await buttonClose.waitForClickable({timeout: 5000});
  await buttonClose.click;
  const linkPost = await this.driver.$('.//a[@href="#/posts/"]');
  await linkPost.click();
  await new Promise(resolve => setTimeout(resolve, 2000));
})

When('Selecciona un Post y edita el titulo', async function () {
  await new Promise(resolve => setTimeout(resolve, 2000));
  const titlePostSelector = await this.driver.$('.gh-content-entry-title', el => el.textContent.trim());
  const postText = await titlePostSelector.getText();
  const postLink = await this.driver.$('a.gh-post-list-title'); 
  const postTitle = await postLink.$('h3.gh-content-entry-title', title => title.textContent.trim());
  await postLink.click();
  await new Promise(resolve => setTimeout(resolve, 2000));
  const labelNewTitle = await this.driver.$('.gh-editor-title');
  let consecutive = getRandomInt (1,100);
  console.log(labelNewTitle + " Actualización titulo titulo " + consecutive )
  await labelNewTitle.setValue('Actualizacion titulo de prueba ' + consecutive)
})

When ('selecciona la opción "Update"', async function () {
  const updateButton = await this.driver.$('button[data-test-button="publish-save"]');
  await updateButton.click();
})

Then ('se muestra el mensaje de confirmación de la edición del post', async function () {
const notifyPublish = await this.driver.$('.gh-notification-title');
const textNotify = await notifyPublish.getText();
try {
  await notifyPublish.waitForDisplayed({ timeout: 2000 });
  if(notifyPublish.isDisplayed() && textNotify=="Post updated"){
    console.log('Post was update successfully');
  }
} catch (error) {
    throw new Error('Post was not update successfully'); 
}
 
})

// Page crear página  
When ('el usuario ingresa un título y deja el contenido vacío', async function () {
  const labelTitleNewPage = await this.driver.$('.gh-editor-title');
  const bodyNewPage = await this.driver.$('.kg-prose');
  let randomNum = getRandomInt (1,100);
  await labelTitleNewPage.setValue('Nuevo titulo de prueba ' + randomNum)
  await bodyNewPage.waitForDisplayed ({ timeout: 3000 });
  await bodyNewPage.setValue('')
})

// Page crear Miembros
When ('el usuario ingresa un nombre y correo electrónico válidos', async function () {
  const inputName = await this.driver.$('[data-test-input="member-name"]');
  const inputEmail = await this.driver.$('[data-test-input="member-email"]');
  let randomNum = getRandomInt (1,100);
  await inputName.setValue('Nuevo nombre ' + randomNum);
  await inputEmail.setValue('newmember' + randomNum + '@gmail.com');
})

When ('el usuario selecciona la opción "Guardar"', async function () {
  const buttonSave= await this.driver.$('[data-test-button="save"]');
  await buttonSave.waitForClickable({ timeout: 5000 })
  await buttonSave.click();
})

Then ('se muestra al usuario la información del miembro creado', async function () {
  await new Promise(resolve => setTimeout(resolve, 2000));
  const linkPost = await this.driver.$('.//a[@href="#/posts/"]');
  const linkMembers = await this.driver.$('a[data-test-nav="members"]');
  await linkPost.waitForClickable({ timeout: 5000 })
  await linkMembers.waitForClickable({ timeout: 5000 })
  await linkPost.click();
  await linkMembers.click();
  const memberInformation = await this.driver.$("//h3[contains(text(), 'Nuevo nombre')]");
  const labelInformation = await memberInformation.getText();
  const nameMember = labelInformation.substring(0, 12);

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

When ('Intenta crear un nuevo miembro con el mismo correo', async function () {
  const emailSelector = await this.driver.$('.gh-members-list-email', el => el.textContent.trim());
  let emailText = await emailSelector.getText();

  const buttonNewMember = await this.driver.$('[data-test-new-member-button]');
  await buttonNewMember.waitForClickable();
  await buttonNewMember.click();

  const inputName = await this.driver.$('[data-test-input="member-name"]');
  const inputEmail = await this.driver.$('[data-test-input="member-email"]');
  let randomNum = getRandomInt (1,100);
  await inputName.setValue('Nuevo nombre ' + randomNum);
  await inputEmail.setValue(emailText);

})

Then ('se muestra el mensaje de error indicando "El correo electrónico ya está en uso"',async function () {
  const msgValidationEmail = await this.driver.$("//*[text()='Member already exists. Attempting to add member with existing email address']");
  const labeValidationEmail = await msgValidationEmail.getText();

  try {
    await msgValidationEmail.waitForDisplayed ({timeout: 5000 });

    if(msgValidationEmail.isDisplayed() && labeValidationEmail=='Member already exists. Attempting to add member with existing email address'){
      console.log('Email is duplicated when trying to create a member');
    } else 
      console.log ('Error: Email validation is not displayed correctly'); 
  } catch (error) {
      throw new Error('Email validation is not displayed correctly'); 
  } 

})

Then('se muestra un mensaje de error indicando "Por favor ingrese un correo"', async function () {
  const msgInputEmail = await this.driver.$("//*[text()='Please enter an email.']");
  const labelErrorEmail = await msgInputEmail.getText();
  
  try {
    await msgInputEmail.waitForDisplayed ({timeout: 5000 });

    if(msgInputEmail.isDisplayed() && labelErrorEmail=='Please enter an email.'){
      console.log('Missing email to create an member');
    } else 
      console.log ('Error: Email validation is not displayed correctly'); 
  } catch (error) {
      throw new Error('Email validation is not displayed correctly'); 
  } 

})

When('el usuario permanece en la vista de crear tag', async function () {
  const titleMembersView = await this.driver.$('h2.gh-canvas-title');
  const buttonRetry = await this.driver.$('button[data-test-button="save"] span[data-test-task-button-state="failure"]');
  const labelTitle = await titleMembersView.getText();
  const labelButton = await buttonRetry.getText();

  if(labelTitle=='New member' && labelButton=='Retry'){
    console.log('New member creation failed');
  } else 
    console.log('Please check member creation process');

})

// Page crear Tags

When ('el usuario ingresa un nombre válido para el tag', async function () {
  const inputNameTag = await this.driver.$('[data-test-input="tag-name"]');
  let randomNum = getRandomInt (1,100);
  await inputNameTag.setValue('NuevoTag ' + randomNum);
})

Then ('se crea el tag y se muestra en la lista de tags', async function () {
  await new Promise(resolve => setTimeout(resolve, 2000));
  const linkTags = await this.driver.$('.//a[@href="#/tags/"]');
  await linkTags.waitForClickable({ timeout: 5000 })
  await linkTags.click();
  const tagInformation = await this.driver.$$('h3.gh-tag-list-name');
  const extInformation = tagInformation[2];
  const labelInformation = await extInformation.getText();
  const nameTag = labelInformation.substring(0, 8);
  await new Promise(resolve => setTimeout(resolve, 2000));
  
  if(nameTag=='NuevoTag'){
      console.log('Tag created successfully');
  } else 
      console.log ('Error: Tag is not created'); 
  
})

// Page Configuraciones generales 

When ('el usuario ingresa un nuevo título y descripción para el sitio', async function () {
  const buttonEdit = await this.driver.$('div[data-testid="title-and-description"] button')
  await buttonEdit.waitForDisplayed ({timeout: 5000 });
  await buttonEdit.click();

  const inputTitle = await this.driver.$('input[placeholder="Site title"]'); 
  const inputDescription = await this.driver.$('input[placeholder="Site description"]'); 
  let consecutive = getRandomInt (1,100);
  await inputTitle.setValue("Automated Customization " + consecutive);
  await inputDescription.setValue("New text to describe the site " + consecutive);

})

When ('selecciona la opción "Guardar"', async function () {
  const buttonSave = await this.driver.$('button.bg-green')
  await buttonSave.click();
})

Then('El sistema confirma la actualización de la información', async function () {
  const buttons = await this.driver.$$('button');   
  if (buttons.length > 0) {
    for (let button of buttons) {
      try {
        const text = await this.driver.$(el => el.textContent.trim(), button);
        if (text === 'Saved') {
          console.log ('Title & Description was update success')
          break;
        }
      } catch (error) {
        console.error('Error al verificar la actualización', error);
      }
    }
  } else {
    console.log('No se encontraron botones en la página');
  }

})