from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def login_as_admin(self, username: str, password: str):
        self.page.fill("input[name='identification']", username)
        self.page.fill("input[name='password']", password)
        self.page.click("button[type='submit']")
        self.page.wait_for_selector("text=Dashboard")  # Confirmación de inicio exitoso

