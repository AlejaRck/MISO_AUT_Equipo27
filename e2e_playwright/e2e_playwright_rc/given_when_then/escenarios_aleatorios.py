import os
import pytest
import random
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


@pytest.mark.test_id("tag-005")
def test_creacion_slug_corte_tags_005(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    tag_page = TagsPage(page)
    fake = Faker()
    tags_data = generate_random_data_tag('tag_005')
    if not tags_data:
        tags_data = {'nombre': fake.name(),
                     'slug': fake.sentence(nb_words=1),
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
        screenshot_test(page, f'tag-005')

    assert is_public


@pytest.mark.test_id("tag-006")
def test_creacion_color_incorrecto_tags_006(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    tag_page = TagsPage(page)
    fake = Faker()
    tags_data = generate_random_data_tag('tag_006')
    if not tags_data:
        tags_data = {'nombre': fake.name(),
                     'slug': fake.sentence(),
                     'descripcion': fake.sentence(),
                     'color': '#XYZ123'
                     }

    tag_page.go_to_create_tags()
    name = tags_data['nombre']
    slug = tags_data['slug']
    descripcion = tags_data['descripcion']
    color = tags_data['color']
    color = color.replace("#", "")
    tag_page.create_tag(title=name, slug=slug, color=str(color), descripcion=descripcion)

    is_public = tag_page.is_color_invalid()
    if not is_public:
        screenshot_test(page, f'tag-006')

    assert is_public


@pytest.mark.test_id("tag-007")
def test_creacion_nombre_especiales_tags_007(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    tag_page = TagsPage(page)
    fake = Faker()
    tags_data = generate_random_data_tag('tag_006')
    if not tags_data:
        tags_data = {'nombre': fake.name(),
                     'slug': fake.sentence(),
                     'descripcion': fake.sentence(),
                     'color': fake.color()
                     }
        caracteres_especiales = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
        tags_data['nombre'] = ''.join(
            char + random.choice(caracteres_especiales) if random.random() > 0.9 else char
            for char in tags_data['nombre']
        )


    tag_page.go_to_create_tags()
    name = tags_data['nombre']
    slug = tags_data['slug']
    descripcion = tags_data['descripcion']
    color = tags_data['color']
    color = color.replace("#", "")
    tag_page.create_tag(title=name, slug=slug, color=str(color), descripcion=descripcion)

    is_public = tag_page.is_tag_created(name)
    if not is_public:
        screenshot_test(page, f'tag-007')

    assert is_public


@pytest.mark.test_id("tag-008")
def test_creacion_color_codigo_invalido_tags_008(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    tag_page = TagsPage(page)
    fake = Faker()
    tags_data = generate_random_data_tag('tag_008')
    if not tags_data:
        tags_data = {'nombre': fake.name(),
                     'slug': fake.sentence(),
                     'descripcion': fake.sentence(),
                     'color': '#12345'
                     }

    tag_page.go_to_create_tags()
    name = tags_data['nombre']
    slug = tags_data['slug']
    descripcion = tags_data['descripcion']
    color = tags_data['color']
    color = color.replace("#", "")
    tag_page.create_tag(title=name, slug=slug, color=str(color), descripcion=descripcion)

    is_public = tag_page.is_color_invalid()
    if not is_public:
        screenshot_test(page, f'tag-008')

    assert is_public


@pytest.mark.test_id("tag-009")
def test_creacion_nombre_largo_tags_009(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    tag_page = TagsPage(page)
    fake = Faker()
    tags_data = generate_random_data_tag('tag_009')
    if not tags_data:
        tags_data = {'nombre': fake.sentence(nb_words=500),
                     'slug': fake.sentence(),
                     'descripcion': fake.sentence(),
                     'color': fake.color()                     }

    tag_page.go_to_create_tags()
    name = tags_data['nombre']
    slug = tags_data['slug']
    descripcion = tags_data['descripcion']
    color = tags_data['color']
    color = color.replace("#", "")
    tag_page.create_tag(title=name, slug=slug, color=str(color), descripcion=descripcion)

    is_public = tag_page.is_name_no_present()
    if not is_public:
        screenshot_test(page, f'tag-009')

    assert is_public


@pytest.mark.test_id("tag-010")
def test_creacion_slug_largo_tags_010(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    tag_page = TagsPage(page)
    fake = Faker()
    tags_data = generate_random_data_tag('tag_010')
    if not tags_data:
        tags_data = {'nombre': fake.sentence(),
                     'slug': fake.sentence(nb_words=500),
                     'descripcion': fake.sentence(),
                     'color': fake.color()                     }

    tag_page.go_to_create_tags()
    name = tags_data['nombre']
    slug = tags_data['slug']
    descripcion = tags_data['descripcion']
    color = tags_data['color']
    color = color.replace("#", "")
    tag_page.create_tag(title=name, slug=slug, color=str(color), descripcion=descripcion)

    is_public = tag_page.is_slug_invalid()
    if not is_public:
        screenshot_test(page, f'tag-010')

    assert is_public


@pytest.mark.test_id("tag-011")
def test_creacion_slug_especial_tags_011(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    tag_page = TagsPage(page)
    fake = Faker()
    tags_data = generate_random_data_tag('tag_010')
    if not tags_data:
        tags_data = {'nombre': fake.sentence(),
                     'slug': fake.sentence(),
                     'descripcion': fake.sentence(),
                     'color': fake.color()}
        caracteres_especiales = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
        tags_data['slug'] = ''.join(
            char + random.choice(caracteres_especiales) if random.random() > 0.9 else char
            for char in tags_data['slug']
        )

    tag_page.go_to_create_tags()
    name = tags_data['nombre']
    slug = tags_data['slug']
    descripcion = tags_data['descripcion']
    color = tags_data['color']
    color = color.replace("#", "")
    tag_page.create_tag(title=name, slug=slug, color=str(color), descripcion=descripcion)

    is_public = tag_page.is_tag_created(name)
    if not is_public:
        screenshot_test(page, f'tag-011')

    assert is_public


@pytest.mark.test_id("tag-012")
def test_creacion_slug_emogi_tags_012(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    tag_page = TagsPage(page)
    fake = Faker()
    tags_data = generate_random_data_tag('tag_012')
    if not tags_data:
        tags_data = {'nombre': fake.sentence(),
                     'slug': fake.sentence(),
                     'descripcion': fake.sentence(),
                     'color': fake.color()}
        emoji = chr(random.randint(0x1F600, 0x1F64F))  # Emoji aleatorio
        tags_data['slug'] = f'{tags_data["slug"]}{emoji}'

    tag_page.go_to_create_tags()
    name = tags_data['nombre']
    slug = tags_data['slug']
    descripcion = tags_data['descripcion']
    color = tags_data['color']
    color = color.replace("#", "")
    tag_page.create_tag(title=name, slug=slug, color=str(color), descripcion=descripcion)

    is_public = tag_page.is_tag_created(name)
    if not is_public:
        screenshot_test(page, f'tag-012')

    assert is_public


@pytest.mark.test_id("tag-013")
def test_creacion_tag_name_duplicado_tags_013(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    tag_page = TagsPage(page)
    fake = Faker()
    tags_data = generate_random_data_tag('tag_013')
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
    tag_page.go_to_create_tags()
    tag_page.create_tag(title=name, color=str(color), descripcion=descripcion)

    is_public = tag_page.is_tag_created(name)
    if not is_public:
        screenshot_test(page, f'tag-013')

    assert is_public


@pytest.mark.test_id("tag-014")
def test_creacion_tag_name_corto_tags_014(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    tag_page = TagsPage(page)
    fake = Faker()
    tags_data = generate_random_data_tag('tag_014')
    if not tags_data:
        tags_data = { 'nombre': fake.sentence(nb_words=1),
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
    tag_page.go_to_create_tags()
    tag_page.create_tag(title=name, color=str(color), descripcion=descripcion)

    is_public = tag_page.is_tag_created(name)
    if not is_public:
        screenshot_test(page, f'tag-014')

    assert is_public


@pytest.mark.test_id("tag-015")
def test_creacion_tag_descip_largo_tags_015(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    tag_page = TagsPage(page)
    fake = Faker()
    tags_data = generate_random_data_tag('tag_015')
    if not tags_data:
        tags_data = { 'nombre': fake.sentence(),
                      'slug': fake.word(),
                      'descripcion': fake.sentence(nb_words=600),
                      'color': fake.color()
        }

    tag_page.go_to_create_tags()
    name = tags_data['nombre']
    descripcion = tags_data['descripcion']
    color = tags_data['color']
    color = color.replace("#", "")
    tag_page.create_tag(title=name, color=str(color), descripcion=descripcion)
    tag_page.go_to_create_tags()
    tag_page.create_tag(title=name, color=str(color), descripcion=descripcion)

    is_public = tag_page.is_descripti_invalid()
    if not is_public:
        screenshot_test(page, f'tag-015')

    assert is_public


@pytest.mark.test_id("tag-016")
def test_creacion_tag_sin_desr_tags_016(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    tag_page = TagsPage(page)
    fake = Faker()
    tags_data = generate_random_data_tag('tag_016')
    if not tags_data:
        tags_data = { 'nombre': fake.name(),
                      'slug': fake.word(),
                      'descripcion': fake.sentence(),
                      'color': fake.color()
        }

    tag_page.go_to_create_tags()
    name = tags_data['nombre']
    color = tags_data['color']
    color = color.replace("#", "")
    tag_page.create_tag(title=name, color=str(color))

    is_public = tag_page.is_tag_created(name)
    if not is_public:
        screenshot_test(page, f'tag-016')

    assert is_public


@pytest.mark.test_id("tag-017")
def test_creacion_tag_descrip_especiales_tags_017(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    tag_page = TagsPage(page)
    fake = Faker()
    tags_data = generate_random_data_tag('tag_017')
    if not tags_data:
        tags_data = { 'nombre': fake.name(),
                      'slug': fake.word(),
                      'descripcion': fake.sentence(),
                      'color': fake.color()
        }

        caracteres_especiales = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
        tags_data['descripcion'] = ''.join(
            char + random.choice(caracteres_especiales) if random.random() > 0.9 else char
            for char in tags_data['descripcion']
        )


    tag_page.go_to_create_tags()
    name = tags_data['nombre']
    descripcion = tags_data['descripcion']
    color = tags_data['color']
    color = color.replace("#", "")
    tag_page.create_tag(title=name, color=str(color), descripcion=descripcion)

    is_public = tag_page.is_tag_created(name)
    if not is_public:
        screenshot_test(page, f'tag-017')

    assert is_public


@pytest.mark.test_id("tag-018")
def test_creacion_tag_nombre_blanco_tags_018(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    tag_page = TagsPage(page)
    fake = Faker()
    tags_data = generate_random_data_tag('tag_018')
    if not tags_data:
        tags_data = { 'nombre': fake.name(),
                      'slug': fake.word(),
                      'descripcion': fake.sentence(),
                      'color': fake.color()
        }

        tags_data['nombre'] = f' {tags_data["nombre"]} '

    tag_page.go_to_create_tags()
    name = tags_data['nombre']
    descripcion = tags_data['descripcion']
    color = tags_data['color']
    color = color.replace("#", "")
    tag_page.create_tag(title=name, color=str(color), descripcion=descripcion)

    is_public = tag_page.is_tag_created(name)
    if not is_public:
        screenshot_test(page, f'tag-018')

    assert is_public