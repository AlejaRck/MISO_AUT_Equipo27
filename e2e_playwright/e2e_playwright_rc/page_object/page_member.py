from playwright.sync_api import Page


class MemberPage:
    def __init__(self, page: Page):
        self.page = page
        self.select_members = 'a[data-test-nav="members"]'
        self.new_member = 'a[data-test-new-member-button="true"]'
        self.email_input = "input[name='email']"
        self.name_input = "input[name='name']"
        self.save_button = 'button[data-test-button="save"]'
        self.member_list = 'h3.gh-members-list-name'
        self.error_message_email = 'div.form-group.max-width.error p.response'
        self.error_message_note = '.form-group.mb0.gh-member-note.error'
        self.save_button_no_disable = "gh-btn gh-btn-primary gh-btn-icon ember-view"
        self.label_dropdown_selector = "div.ember-basic-dropdown-trigger"
        self.label_selector = "div.ember-basic-dropdown-trigger"
        self.label_input = "input.ember-power-select-trigger-multiple-input"
        self.textarea_selector = "textarea#member-note"


    def go_to_create_member(self):
        self.page.click(self.select_members, force=True)
        self.page.wait_for_selector(self.new_member)

        self.page.click(self.new_member)
        self.page.wait_for_selector(self.email_input)

    def create_member(self, name:str='', email:str='', label:str='', note:str=''):
        self.page.fill(self.name_input, name)
        self.page.fill(self.email_input, email)
        self.page.click(self.label_dropdown_selector)
        self.page.wait_for_selector(self.label_selector)
        self.page.fill(self.label_input, label)
        self.page.fill(self.textarea_selector, note)
        self.page.wait_for_selector(self.save_button)
        self.page.click(self.save_button)
        self.page.wait_for_timeout(2000)

    def is_member_created(self, name:str='') -> bool:

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

    def invalid_email(self) -> bool:

        self.page.wait_for_selector(self.error_message_email, state='visible',
                                    timeout=10000)

        response_text = self.page.locator(self.error_message_email).inner_text()
        if "Invalid Email." in response_text:
            return True
        else:
            return False

    def note_long(self) -> bool:

        self.page.wait_for_selector(self.error_message_note, state='visible',
                                    timeout=10000)

        response_text = self.page.locator(self.error_message_note).inner_text()
        if "Note is too long." in response_text:
            return True
        else:
            return False

