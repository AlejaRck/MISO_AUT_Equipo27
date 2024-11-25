import os
import pytest
from e2e_playwright_rc.metadata.path import Path
from playwright.sync_api import BrowserType, sync_playwright
from e2e_playwright_rc.page_object.login_page import LoginPage
from e2e_playwright_rc.page_object.page_tags import TagsPage
from e2e_playwright_rc.utils.screenshot import screenshot_test
from e2e_playwright_rc.utils.open_yaml import get_config, generate_random_data_tag

from playwright._impl._errors import TimeoutError
from faker import Faker



@pytest.fixture(scope="function")
def setup():
    config = get_config()

    os.makedirs(Path.result_img_versrion_rc, exist_ok=True)

    with sync_playwright() as p:
        # Lanzamos el navegador en modo no-headless (para ver el navegador)
        browser = p.chromium.launch(headless=False)  # Cambiar a headless=False para ver el navegador
        context = browser.new_context(ignore_https_errors=True, bypass_csp=True)
        page = context.new_page()

        # Accedemos al sitio de inicio de sesión
        page.goto(config['ghost_url'])

        # Realizamos el login
        login_page = LoginPage(page)
        login_page.login_as_admin(config['admin_user'], config['admin_pass'])

        # Devolver la página para usarla en las pruebas
        yield page

        # Cerrar el navegador después de la prueba
        context.close()
        browser.close()


@pytest.mark.test_id("tag-001")
def test_creacion_tag_sin_nombre_tags_001(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    tag_page = TagsPage(page)
    fake = Faker()
    tags_data = generate_random_data_tag('tag_001')
    if not tags_data:
        tags_data = { 'nombre': fake.name(),
                      'slug': fake.word(),
                      'descripcion': fake.sentence(),
                      'color': fake.color()
        }

    tag_page.go_to_create_tags()
    slug = tags_data['slug']
    descripcion = tags_data['descripcion']
    color = tags_data['color']
    color = color.replace("#", "")
    tag_page.create_tag(slug=slug, color=str(color), descripcion=descripcion)

    is_public = tag_page.is_name_no_present()
    if not is_public:
        screenshot_test(page, f'tag-001')

    assert is_public


@pytest.mark.test_id("tag-002")
def test_creacion_tag_sin_slug_tags_002(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    tag_page = TagsPage(page)
    fake = Faker()
    tags_data = generate_random_data_tag('tag_002')
    if not tags_data:
        tags_data = { 'nombre': fake.name(),
                      'slug': fake.word(),
                      'descripcion': fake.sentence(),
                      'color': fake.color()
        }

    tag_page.go_to_create_tags()
    name = tags_data['nombre']
    descripcion = tags_data['descripcion']
    color = tags_data['color']
    color = color.replace("#", "")
    tag_page.create_tag(title=name, color=str(color), descripcion=descripcion)

    is_public = tag_page.is_tag_created(name)
    if not is_public:
        screenshot_test(page, f'tag-002')

    assert is_public


@pytest.mark.test_id("tag-003")
def test_creacion_sin_datos_tags_003(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    tag_page = TagsPage(page)
    fake = Faker()
    tags_data = generate_random_data_tag('tag_003')
    if not tags_data:
        tags_data = { 'nombre': '',
                      'slug': '',
                      'descripcion': '',
                      'color': ''
        }

    tag_page.go_to_create_tags()
    name = tags_data['nombre']
    slug = tags_data['slug']
    descripcion = tags_data['descripcion']
    color = tags_data['color']
    color = color.replace("#", "")
    tag_page.create_tag(title=name, slug=slug, color=str(color), descripcion=descripcion)

    is_public = tag_page.is_name_no_present()
    if not is_public:
        screenshot_test(page, f'tag-003')

    assert is_public


@pytest.mark.test_id("tag-004")
def test_creacion_nombre_corte_tags_004(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    tag_page = TagsPage(page)
    fake = Faker()
    tags_data = generate_random_data_tag('tag_004')
    if not tags_data:
        tags_data = {'nombre': fake.sentence(nb_words=1),
                     'slug': fake.word(),
                     'descripcion': fake.sentence(),
                     'color': fake.color()
                     }

    tag_page.go_to_create_tags()
    name = tags_data['nombre']
    slug = tags_data['slug']
    descripcion = tags_data['descripcion']
    color = tags_data['color']
    color = color.replace("#", "")
    tag_page.create_tag(title=name, slug=slug, color=str(color), descripcion=descripcion)

    is_public = tag_page.is_tag_created(name)
    if not is_public:
        screenshot_test(page, f'tag-004')

    assert is_public