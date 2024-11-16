from playwright.sync_api import Page


class PagePage:
    def __init__(self, page: Page):
        self.page = page
        self.page_pages = 'a[href="#/pages/"]'
        self.new_pages = "a.gh-btn.gh-btn-primary.view-actions-top-row"
        self.title_input = 'textarea[placeholder="Page Title"]'
        self.content_input = 'div[contenteditable="true"]'
        self.save_page = 'div.gh-btn.gh-btn-editor.gh-publishmenu-trigger'
        self.button_public = 'button.gh-btn.gh-btn-black.gh-publishmenu-button'
        self.button_return_post = 'a.gh-editor-back-button'


    def go_to_create_page(self):

        self.page.click(self.page_pages, force=True)
        self.page.wait_for_selector(self.new_pages)
        self.page.click(self.new_pages)
        self.page.wait_for_selector(self.title_input)


    def create_page(self, title: str, content: str):
        self.page.fill(self.title_input, title)
        self.page.fill(self.content_input, content)
        self.page.click(self.save_page)
        self.page.wait_for_selector(self.button_public)
        self.page.click(self.button_public)
        self.page.wait_for_timeout(2000)

    def is_page_published(self, title: str) -> bool:
        self.page.wait_for_selector(self.button_return_post)
        self.page.click(self.button_return_post)
        return self.page.is_visible(f"text='{title}'")