from playwright.sync_api import Page
import time

class ConfigPage:
    def __init__(self, page: Page):
        self.page = page
        self.page_config = "a:has-text('Settings')"
        self.general_config = 'a[href="#/settings/general/"]'
        self.edit_title_des_visible = 'h4.gh-expandable-title:has-text("Title & description")'
        self.edit_button = 'div.gh-expandable-header:has(h4.gh-expandable-title:has-text("Title & description")) button.gh-btn'
        self.title_input = 'input[type="text"]'
        self.save_button = 'button.gh-btn:has-text("Save settings")'

    def go_to_config_page(self):

        self.page.click(self.page_config)
        self.page.wait_for_selector(self.general_config)
        self.page.click(self.general_config)

    def actualizar_config_page(self, title: str):
        self.page.wait_for_selector(self.edit_title_des_visible)
        self.page.click(self.edit_button)
        self.page.wait_for_selector(self.title_input)
        self.page.fill(self.title_input, title)
        self.page.wait_for_selector(self.save_button)
        self.page.click(self.save_button)
        self.page.wait_for_timeout(2000)

    def is_title_updated(self, title):

        titulo = self.page.title()
        print(titulo)
        if f'Settings - General - {title}' == titulo:
            return True
        else:
            return False

