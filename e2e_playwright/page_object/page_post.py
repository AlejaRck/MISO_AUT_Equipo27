from playwright.sync_api import Page


class PostPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_create_post(self):

        self.page.click('[title="New post"]')
        self.page.wait_for_selector('textarea[placeholder="Post title"]')

    def create_post(self, title: str, content: str):
        self.page.fill('textarea[placeholder="Post title"]', title)
        self.page.fill('div[contenteditable="true"]', content)
        self.page.click('button.gh-btn.gh-btn-editor.darkgrey.gh-publish-trigger')
        self.page.wait_for_selector('button[data-test-button="continue"]')
        self.page.click('button[data-test-button="continue"]')
        self.page.wait_for_selector('button.gh-btn.gh-btn-large.gh-btn-pulse.ember-view:not([disabled]):visible')
        self.page.click('button.gh-btn.gh-btn-large.gh-btn-pulse.ember-view', force=True)
        self.page.wait_for_selector('button[data-test-button="close-publish-flow"]')
        self.page.click('button[data-test-button="close-publish-flow"]')

    def is_post_published(self, title: str) -> bool:
        return self.page.is_visible(f"text='{title}'")

    def is_post_not_published(self, title: str) -> bool:
        return not self.page.is_visible(f"text='{title}'")