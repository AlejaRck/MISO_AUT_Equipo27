from playwright.sync_api import Page
from e2e_playwright_rc.utils.open_yaml import get_config

class TagsPage:
    def __init__(self, page: Page):
        self.page = page
        self.config = get_config()
        self.page_tags = 'a[data-test-nav="tags"]'
        self.new_tag = 'a.gh-btn.gh-btn-primary'
        self.name_input = "input[name='name']"
        self.slug_input = "input[name='slug']"
        self.color_input = "input[name='accent-color']"
        self.des_input = "textarea#tag-description"
        self.save_button = 'button[data-test-button="save"]'
        self.tags_names = '.gh-tag-list-name'
        self.tags_url = f'{self.config["ghost_url"]}/#/tags/new'
        self.name_input_aut = "input[name='identification']"
        self.name_error = 'div.form-group.mr2.flex-auto.error span.error p.response:first-of-type'
        self.color_error = 'div.gh-tag-settings-multiprop div.form-group.gh-tag-settings-colorcontainer.error'
        self.error_message_url = 'div.form-group.success p.response:first-of-type'
        self.error_message_description = 'div.form-group.no-margin.error p.response:first-of-type'
        self.edit_tag = "a[title='Edit tag'] h3:has-text"


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


    def create_tag(self, title:str='', slug:str='', color:str='', descripcion=''):
            self.page.wait_for_selector(self.name_input)
            self.page.fill(self.name_input, title)
            self.page.fill(self.slug_input, slug)
            self.page.fill(self.color_input, color),
            self.page.fill(self.des_input, descripcion)
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

    def is_name_no_present(self) -> bool:

        self.page.wait_for_selector(self.name_error, state='visible',
                                    timeout=10000)

        response_text = self.page.locator(self.name_error).inner_text()
        if "You must specify a name for the tag." in response_text or 'Tag names cannot be longer than 191 characters.' \
                in response_text:
            return True
        else:
            return False

    def is_color_invalid(self) -> bool:
        self.page.wait_for_selector(self.color_error, state='visible',
                                    timeout=10000)

        response_text = self.page.locator(self.color_error).inner_text()
        if 'in valid hex format' in response_text:
            return True
        else:
            return False

    def is_slug_invalid(self) -> bool:
        self.page.wait_for_selector(self.error_message_url, state='visible',
                                    timeout=10000)

        response_text = self.page.locator(self.error_message_url).inner_text()
        if 'URL cannot be longer than 191 characters.' in response_text:
            return True
        else:
            return False

    def is_descripti_invalid(self) -> bool:
        self.page.wait_for_selector(self.error_message_description, state='visible',
                                    timeout=10000)

        response_text = self.page.locator(self.error_message_description).inner_text()
        if 'Description cannot be longer than 500 characters.' in response_text:
            return True
        else:
            return False

    def go_to_edit_tag(self, name: str) -> bool:

        if self.is_tag_created(name):
            self.page.click(f"{self.edit_tag}('{name}')")
            self.page.wait_for_timeout(2000)