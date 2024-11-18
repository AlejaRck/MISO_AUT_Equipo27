from playwright.sync_api import Page


class PostPage:
    def __init__(self, page: Page):
        self.page = page
        self.new_post = '[title="New post"]'
        self.post_title = 'textarea[placeholder="Post title"]'
        self.post_content = 'div[contenteditable="true"]'
        self.post_save = 'button.gh-btn.gh-btn-editor.darkgrey.gh-publish-trigger'
        self.continue_button = 'button[data-test-button="continue"]'
        self.button_accept_visable = 'button.gh-btn.gh-btn-large.gh-btn-pulse.ember-view:not([disabled]):visible'
        self.button_accept = 'button.gh-btn.gh-btn-large.gh-btn-pulse.ember-view'
        self.button_public = 'button[data-test-button="close-publish-flow"]'


    def go_to_create_post(self):

        self.page.click(self.new_post)
        self.page.wait_for_selector(self.post_title)

    def create_post(self, title: str, content: str):
        self.page.fill(self.post_title, title)
        self.page.fill(self.post_content, content)
        self.page.click(self.post_save)
        self.page.wait_for_selector(self.continue_button)
        self.page.click(self.continue_button)
        self.page.wait_for_selector(self.button_accept_visable)
        self.page.click(self.button_accept, force=True)
        self.page.wait_for_selector(self.button_public)
        self.page.click(self.button_public)
        self.page.wait_for_timeout(2000)

    def is_post_published(self, title: str) -> bool:
        return self.page.is_visible(f"text='{title}'")

    def is_post_not_published(self, title: str) -> bool:
        return not self.page.is_visible(f"text='{title}'")