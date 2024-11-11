from playwright.sync_api import Page


class MemberPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_create_member(self):
        self.page.click('a[data-test-nav="members"]', force=True)
        self.page.wait_for_selector('a[data-test-new-member-button="true"]')

        self.page.click('a[data-test-new-member-button="true"]')
        self.page.wait_for_selector("input[name='email']")

    def create_member(self, name: str, email: str):
        self.page.fill("input[name='name']", name)
        self.page.fill("input[name='email']", email)
        self.page.wait_for_selector('button[data-test-button="save"]')
        self.page.click('button[data-test-button="save"]')



    def is_member_created(self, name: str) -> bool:

        self.page.click('a[data-test-nav="members"]', force=True)
        self.page.wait_for_selector('a[data-test-new-member-button="true"]')
        self.page.wait_for_selector('h3.gh-members-list-name', timeout=5000)
        member_name = self.page.inner_text('h3.gh-members-list-name')
        if name in member_name:
            return True
        else:
            return False

    def is_email_no_present(self) -> bool:

        self.page.wait_for_selector('div.form-group.max-width.error p.response', state='visible',
                               timeout=10000)

        response_text = self.page.locator('div.form-group.max-width.error p.response').inner_text()
        if "Please enter an email." in response_text:
            return True
        else:
            return False

    def is_email_duplicate(self):
        self.page.wait_for_selector('div.form-group.max-width.error p.response', state='visible',
                               timeout=10000)

        response_text = self.page.locator('div.form-group.max-width.error p.response').inner_text()
        if "Member already exists. Attempting to add member with existing email address" in response_text:
            return True
        else:
            return False
