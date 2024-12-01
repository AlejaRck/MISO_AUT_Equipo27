from playwright.sync_api import Page
from playwright._impl._errors import TimeoutError


class PostPage:
    def __init__(self, page: Page):
        self.page = page
        self.return_post = 'a[href="#/posts/"]'
        self.new_post = '[title="New post"]'
        self.post_title = 'textarea[placeholder="Post title"]'
        self.post_content = 'div[contenteditable="true"]'
        self.post_imagen_button = 'button.gh-editor-feature-image-add-button'
        self.post_imgaen = "input[type='file']"
        self.post_save = 'button.gh-btn.gh-btn-editor.darkgrey.gh-publish-trigger'
        self.continue_button = 'button[data-test-button="continue"]'
        self.button_accept_visable = 'button.gh-btn.gh-btn-large.gh-btn-pulse.ember-view:not([disabled]):visible'
        self.button_accept = 'button.gh-btn.gh-btn-large.gh-btn-pulse.ember-view'
        self.button_public = 'button[data-test-button="close-publish-flow"]'
        self.button_update = 'button[data-test-button="publish-save"]'
        self.edit_post_button= 'h3.gh-content-entry-title:has-text'


    def go_to_create_post(self):

        self.page.click(self.new_post)
        self.page.wait_for_selector(self.post_title)

    def create_post(self, title:str='', content:str='', imagen: str=None):
        self.page.fill(self.post_title, title)
        self.page.fill(self.post_content, content)
        if imagen:
            self.page.click(self.post_imagen_button)
            self.page.wait_for_selector(self.post_imgaen)
            self.page.wait_for_timeout(2000)
            self.page.evaluate("""
                   (base64Data) => {
                       // Encuentra el contenedor donde debe ir la imagen
                       const container = document.querySelector('.image-upload-container'); // Ajusta el selector
                       if (container) {
                           const img = document.createElement('img');
                           img.src = base64Data;
                           container.appendChild(img);

                           // Simula el evento de subida
                           container.dispatchEvent(new Event('change', { bubbles: true }));
                       }
                   }
               """, imagen)
        try:
            self.page.click(self.post_save)
            self.page.wait_for_selector(self.continue_button)
            self.page.click(self.continue_button)
            self.page.wait_for_selector(self.button_accept_visable)
            self.page.click(self.button_accept, force=True)
            self.page.wait_for_selector(self.button_public)
            self.page.click(self.button_public)
            self.page.wait_for_timeout(2000)
        except TimeoutError:
            self.page.click(self.return_post, force=True)


    def is_post_published(self, title:str='') -> bool:
        return self.page.is_visible(f"text='{title}'")

    def is_post_not_published(self, title:str='') -> bool:
        return not self.page.is_visible(f"text='{title}'")

    def go_to_public_post(self, title:str) -> bool:

        if self.is_post_published(title):
            self.page.click(f'{self.edit_post_button}("{title}")')

    def edit_post(self, new_title:str='' ,new_contenido:str=''):
        self.page.fill(self.post_title, new_title)
        self.page.fill(self.post_content, new_contenido)
        self.page.click(self.button_update)
        self.page.wait_for_timeout(2000)
        self.page.click(self.return_post, force=True)
        self.page.wait_for_timeout(2000)
