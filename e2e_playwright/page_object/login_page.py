from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.name_input = "input[name='identification']"
        self.pass_input = "input[name='password']"
        self.summit_button = "button[type='submit']"
        self.text_board = "text=Dashboard"

    def login_as_admin(self, username: str, password: str):
        self.page.fill(self.name_input, username)
        self.page.fill(self.pass_input, password)
        self.page.click(self.summit_button)
        self.page.wait_for_selector(self.text_board)  # Confirmación de inicio exitoso

