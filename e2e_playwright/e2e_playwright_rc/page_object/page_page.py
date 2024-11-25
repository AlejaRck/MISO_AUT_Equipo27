from playwright.sync_api import Page
from playwright._impl._errors import TimeoutError


class PagePage:
    def __init__(self, page: Page):
        self.page = page
        self.return_page = 'a[href="#/pages/"]'
        self.page_pages = 'a[data-test-nav="pages"]'
        self.new_pages = "a[data-test-new-page-button]"
        self.title_input = 'textarea[placeholder="Page title"]'
        self.content_input = 'div[contenteditable="true"]'
        self.save_page = 'button.gh-btn.gh-btn-editor.darkgrey.gh-publish-trigger'
        self.continue_button = 'button[data-test-button="continue"]'
        self.button_accept_visable = 'button.gh-btn.gh-btn-large.gh-btn-pulse.ember-view:not([disabled]):visible'
        self.button_accept = 'button.gh-btn.gh-btn-large.gh-btn-pulse.ember-view'
        self.button_public = 'button[data-test-button="close-publish-flow"]'


    def go_to_create_page(self):

        self.page.click(self.page_pages, force=True)
        self.page.wait_for_selector(self.new_pages)
        self.page.click(self.new_pages)
        self.page.wait_for_selector(self.title_input)


    def create_page(self, title:str='', content:str=''):
        self.page.fill(self.title_input, title)
        self.page.fill(self.content_input, content)
        try:
            self.page.click(self.save_page)
            self.page.wait_for_selector(self.continue_button)
            self.page.click(self.continue_button)
            self.page.wait_for_selector(self.button_accept_visable)
            self.page.click(self.button_accept, force=True)
            self.page.wait_for_selector(self.button_public)
            self.page.click(self.button_public)
            self.page.wait_for_timeout(2000)
        except TimeoutError:
            self.page.click(self.return_page, force=True)
            self.page.wait_for_timeout(2000)

    def is_page_published(self, title:str='') -> bool:
        return self.page.is_visible(f"text='{title}'")