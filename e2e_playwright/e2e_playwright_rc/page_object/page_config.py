from playwright.sync_api import Page
import time

class ConfigPage:
    def __init__(self, page: Page):
        self.page = page
        self.page_config = "a:has-text('Settings')"
        self.edit_title_des_visible = "div[data-testid='title-and-description'] button:has-text('Edit'):visible"
        self.edit_button = "div[data-testid='title-and-description'] button:has-text('Edit')"
        self.title_input = "input[placeholder='Site title']"
        self.save_button = "button.cursor-pointer.bg-green.text-white"
        self.exit_button = 'button[data-testid="exit-settings"]'
        self.dasboard = "text=Dashboard"

    def go_to_config_page(self):

        self.page.click(self.page_config)

    def actualizar_config_page(self, title: str):
        self.page.wait_for_selector(self.edit_title_des_visible)
        self.page.click(self.edit_button)
        self.page.wait_for_selector(self.title_input)
        self.page.fill(self.title_input, title)
        self.page.wait_for_selector(self.save_button)
        self.page.click(self.save_button)
        self.page.wait_for_timeout(2000)

    def is_title_updated(self, title):

        self.page.reload()
        self.page.wait_for_timeout(2000)
        titulo = self.page.title()
        if f'Ghost Admin - {title}' == titulo:
            return True
        else:
            return False

