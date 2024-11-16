from playwright.sync_api import Page
from utils.open_yaml import get_config

class TagsPage:
    def __init__(self, page: Page):
        self.page = page
        self.config = get_config()
        self.page_tags = 'a[data-test-nav="tags"]'
        self.new_tag = 'a.gh-btn.gh-btn-primary'
        self.name_input = "input[name='name']"
        self.save_button = 'button[data-test-button="save"]'
        self.tags_names = '.gh-tag-list-name'
        self.tags_url = f'{self.config["ghost_url"]}/#/tags/new'
        self.name_input_aut = "input[name='identification']"

    def go_to_create_tags(self):

        self.page.click(self.page_tags, force=True)
        self.page.click(self.new_tag)


    def go_to_create_tags_sin_aut(self):

        self.page.goto(self.tags_url)
        self.page.wait_for_load_state()


    def validate_page_tags_sin_aut(self):

        self.page.wait_for_selector(self.name_input_aut)
        input_element = self.page.query_selector(self.name_input_aut)
        return input_element is not None and input_element.is_visible()


    def create_tag(self, title: str):
            self.page.wait_for_selector(self.name_input)
            self.page.fill(self.name_input, title)
            self.page.click(self.save_button)
            self.page.wait_for_timeout(2000)


    def is_tag_created(self, name: str) -> bool:

        self.page.click(self.page_tags, force=True)
        self.page.wait_for_selector(self.tags_names, timeout=5000)
        tags = self.page.query_selector_all(self.tags_names)
        tags_texto = [tag.text_content().strip() for tag in tags]
        if name in tags_texto:
            return True
        else:
            return False