from playwright.sync_api import Page
import time

class ConfigPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_config_page(self):

        self.page.click("a:has-text('Settings')")

    def actualizar_config_page(self, title: str):
        self.page.wait_for_selector("div[data-testid='title-and-description'] button:has-text('Edit'):visible")
        self.page.click("div[data-testid='title-and-description'] button:has-text('Edit')")
        self.page.wait_for_selector("input[placeholder='Site title']")
        self.page.fill("input[placeholder='Site title']", title)
        self.page.wait_for_selector("button.cursor-pointer.bg-green.text-white")
        self.page.click("button.cursor-pointer.bg-green.text-white")

    def is_title_updated(self, title):

        self.page.wait_for_selector('button[data-testid="exit-settings"]')
        self.page.click('button[data-testid="exit-settings"]')
        self.page.wait_for_selector("text=Dashboard")

        titulo = self.page.title()
        if f'Ghost Admin - {title}' == titulo:
            return True
        else:
            return False

