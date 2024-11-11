from playwright.sync_api import Page
import time

class TagsPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_create_tags(self):

        self.page.click('a[data-test-nav="tags"]', force=True)

        self.page.click('a.gh-btn.gh-btn-primary')


    def create_tag(self, title: str):
            self.page.wait_for_selector("input[name='name']")
            self.page.fill("input[name='name']", title)
            self.page.wait_for_selector('button[data-test-button="save"]')
            self.page.click('button[data-test-button="save"]')


    def is_tag_created(self, name: str) -> bool:

        self.page.click('a[data-test-nav="tags"]', force=True)
        time.sleep(4)
        self.page.wait_for_selector('h3.gh-tag-list-name', timeout=5000)
        tag_name = self.page.inner_text('h3.gh-tag-list-name')
        if name in tag_name:
            return True
        else:
            return False