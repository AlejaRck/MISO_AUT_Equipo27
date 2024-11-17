from playwright.sync_api import Page


class MemberPage:
    def __init__(self, page: Page):
        self.page = page
        self.select_members = 'a[href="#/members/"]'
        self.new_member = 'a.gh-btn.gh-btn-primary.ember-view'
        self.email_input = "input[name='email']"
        self.name_input = "input[name='name']"
        self.save_button = 'button.gh-btn.gh-btn-primary.gh-btn-icon.ember-view'
        self.member_list = 'h3.gh-members-list-name'
        self.error_message_email = 'div.form-group.max-width.error p.response'
        self.save_button_no_disable = "gh-btn gh-btn-primary gh-btn-icon ember-view"


    def go_to_create_member(self):
        self.page.click(self.select_members, force=True)
        self.page.wait_for_selector(self.new_member)

        self.page.click(self.new_member)
        self.page.wait_for_selector(self.email_input)

    def create_member(self, name: str, email: str):
        self.page.fill(self.name_input, name)
        self.page.fill(self.email_input, email)
        self.page.wait_for_selector(self.save_button)
        self.page.click(self.save_button)
        self.page.wait_for_timeout(2000)

    def is_member_created(self, name: str) -> bool:

        self.page.click(self.select_members, force=True)
        self.page.wait_for_selector(self.new_member)
        self.page.wait_for_selector(self.member_list, timeout=5000)
        member_name = self.page.inner_text(self.member_list)
        if name in member_name:
            return True
        else:
            return False

    def is_email_no_present(self) -> bool:

        self.page.wait_for_selector(self.error_message_email, state='visible',
                               timeout=10000)

        response_text = self.page.locator(self.error_message_email).inner_text()
        if "Please enter an email." in response_text:
            return True
        else:
            return False

    def is_email_duplicate(self):
        self.page.wait_for_selector(self.error_message_email, state='visible',
                               timeout=10000)

        response_text = self.page.locator(self.error_message_email).inner_text()
        if "Member already exists" in response_text:
            return True
        else:
            return False
