from playwright.sync_api import Page


class PagePage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_create_page(self):

        self.page.click('a[data-test-nav="pages"]', force=True)
        self.page.wait_for_selector("a[data-test-new-page-button]")
        self.page.click("a[data-test-new-page-button]")
        self.page.wait_for_selector('textarea[placeholder="Page title"]')

    def create_page(self, title: str, content: str):
        self.page.fill('textarea[placeholder="Page title"]', title)
        self.page.fill('div[contenteditable="true"]', content)
        self.page.click('button.gh-btn.gh-btn-editor.darkgrey.gh-publish-trigger')
        self.page.wait_for_selector('button[data-test-button="continue"]')
        self.page.click('button[data-test-button="continue"]')
        self.page.wait_for_selector('button.gh-btn.gh-btn-large.gh-btn-pulse.ember-view:not([disabled]):visible')
        self.page.click('button.gh-btn.gh-btn-large.gh-btn-pulse.ember-view', force=True)
        self.page.wait_for_selector('button[data-test-button="close-publish-flow"]')
        self.page.click('button[data-test-button="close-publish-flow"]')

    def is_page_published(self, title: str) -> bool:
        return self.page.is_visible(f"text='{title}'")