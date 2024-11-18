from playwright.sync_api import Page


class PostPage:
    def __init__(self, page: Page):
        self.page = page
        self.new_post = '[title="New post"]'
        self.post_title = 'textarea[placeholder="Post Title"]'
        self.post_content = 'div[contenteditable="true"]'
        self.post_save = 'div.gh-btn.gh-btn-editor.gh-publishmenu-trigger'
        self.button_public = 'button.gh-btn.gh-btn-black.gh-publishmenu-button'
        self.button_return_post = 'a.gh-editor-back-button'


    def go_to_create_post(self):

        self.page.click(self.new_post)
        self.page.wait_for_selector(self.post_title)

    def create_post(self, title: str, content: str):
        self.page.fill(self.post_title, title)
        self.page.fill(self.post_content, content)
        self.page.click(self.post_save)
        self.page.wait_for_selector(self.button_public)
        self.page.click(self.button_public)
        self.page.wait_for_timeout(2000)

    def is_post_published(self, title: str) -> bool:
        self.page.wait_for_selector(self.button_return_post)
        self.page.click(self.button_return_post)
        self.page.wait_for_timeout(2000)
        return self.page.is_visible(f"text='{title}'")

    def is_post_not_published(self, title: str) -> bool:
        return not self.page.is_visible(f"text='{title}'")