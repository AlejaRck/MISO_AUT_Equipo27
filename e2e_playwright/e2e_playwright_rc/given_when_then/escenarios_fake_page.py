import os
import pytest
import random
from e2e_playwright_rc.metadata.path import Path
from playwright.sync_api import BrowserType, sync_playwright
from e2e_playwright_rc.page_object.login_page import LoginPage
from e2e_playwright_rc.page_object.page_page import PagePage
from e2e_playwright_rc.utils.open_yaml import get_config
from e2e_playwright_rc.utils.screenshot import screenshot_test
from faker import Faker
from playwright._impl._errors import TimeoutError


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


@pytest.mark.test_id("page-001")
def test_creacion_pagina_titulo_numero_page_001(setup):
    page = setup
    page_page = PagePage(page)
    fake = Faker()
    title = fake.random_int(min=0, max=1000)
    contenido = ''
    # Given
    page_page.go_to_create_page()

    # When
    page_page.create_page(str(title), contenido)

    # Then
    page_public = page_page.is_page_published(title)
    if not page_public:
        screenshot_test(page, 'page-001')
    assert page_public


@pytest.mark.test_id("page-002")
def test_creacion_pagina_sin_imagen_page_002(setup):
    page = setup
    page_page = PagePage(page)
    fake = Faker()
    title = fake.name()
    contenido = fake.sentence(nb_words=10)
    # Given
    page_page.go_to_create_page()

    # When
    page_page.create_page(title, contenido)

    # Then
    page_public = page_page.is_page_published(title)
    if not page_public:
        screenshot_test(page, 'page-002')
    assert page_public


@pytest.mark.test_id("page-003")
def test_creacion_pagina_sin_titulo_page_003(setup):
    page = setup
    page_page = PagePage(page)
    fake = Faker()
    contenido = fake.sentence(nb_words=10)
    # Given
    page_page.go_to_create_page()

    # When
    page_page.create_page(content=contenido)

    # Then
    page_public = page_page.is_page_published()
    if page_public:
        screenshot_test(page, 'page-003')
    assert not page_public


@pytest.mark.test_id("page-004")
def test_creacion_pagina_sin_contenido_page_004(setup):
    page = setup
    page_page = PagePage(page)
    fake = Faker()
    title = fake.name()
    # Given
    page_page.go_to_create_page()

    # When
    page_page.create_page(title=title)

    # Then
    page_public = page_page.is_page_published(title)
    if not page_public:
        screenshot_test(page, 'page-004')
    assert page_public


@pytest.mark.test_id("page-005")
def test_creacion_titulo_con_caracteres_especiales_page_005(setup):
    page = setup
    page_page = PagePage(page)
    fake = Faker()
    caracteres_especiales = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    title = fake.name()
    contenido = fake.sentence(nb_words=10)
    texto_modificado = ''.join(
        char + random.choice(caracteres_especiales) if random.random() > 0.9 else char
        for char in title
    )
    # Given
    page_page.go_to_create_page()

    # When
    page_page.create_page(title=texto_modificado, content=contenido)

    # Then
    page_public = page_page.is_page_published(texto_modificado)
    if not page_public:
        screenshot_test(page, 'page-005')
    assert page_public


@pytest.mark.test_id("page-008")
def test_creacion_contenido_con_caracteres_especiales_page_008(setup):
    page = setup
    page_page = PagePage(page)
    fake = Faker()
    caracteres_especiales = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    title = fake.name()
    contenido = fake.sentence(nb_words=10)
    texto_modificado = ''.join(
        char + random.choice(caracteres_especiales) if random.random() > 0.9 else char
        for char in contenido
    )
    # Given
    page_page.go_to_create_page()

    # When
    page_page.create_page(title=title, content=texto_modificado)

    # Then
    page_public = page_page.is_page_published(title)
    if not page_public:
        screenshot_test(page, 'page-008')
    assert page_public


@pytest.mark.test_id("page-006")
def test_creacion_contenido_con_emojies_page_006(setup):
    page = setup
    page_page = PagePage(page)
    fake = Faker()
    title = fake.name()
    contenido = fake.sentence(nb_words=10)
    emoji = chr(random.randint(0x1F600, 0x1F64F))  # Emoji aleatorio
    contenido = f"{emoji} {contenido} {emoji}"
    # Given
    page_page.go_to_create_page()

    # When
    page_page.create_page(title=title, content=contenido)

    # Then
    page_public = page_page.is_page_published(title)
    if not page_public:
        screenshot_test(page, 'page-006')
    assert page_public


@pytest.mark.test_id("page-007")
def test_creacion_titulo_con_espacios_blanco_page_007(setup):
    page = setup
    page_page = PagePage(page)
    fake = Faker()
    title = fake.name()
    title = f"   {title}   "
    contenido = fake.sentence(nb_words=10)

    # Given
    page_page.go_to_create_page()

    # When
    page_page.create_page(title=title, content=contenido)

    # Then
    page_public = page_page.is_page_published(title)
    if not page_public:
        screenshot_test(page, 'page-007')
    assert page_public



@pytest.mark.test_id("page-009")
def test_creacion_titulo_largo_page_009(setup):
    page = setup
    page_page = PagePage(page)
    fake = Faker()
    title = fake.sentence(nb_words=1000)
    contenido = fake.sentence(nb_words=10)

    # Given
    page_page.go_to_create_page()

    # When
    try:
        page_page.create_page(title=title, content=contenido)
    except TimeoutError as e:
        screenshot_test(page, f'POST-009_time')

    # Then
    page_public = page_page.is_page_published(title)
    if page_public:
        screenshot_test(page, 'page-009')
    assert not page_public


@pytest.mark.test_id("page-010")
def test_creacion_titulo_corto_page_010(setup):
    page = setup
    page_page = PagePage(page)
    fake = Faker()
    title = fake.sentence(nb_words=1)
    contenido = fake.sentence(nb_words=10)

    # Given
    page_page.go_to_create_page()

    # When
    try:
        page_page.create_page(title=title, content=contenido)
    except TimeoutError as e:
        screenshot_test(page, f'POST-010_time')

    # Then
    page_public = page_page.is_page_published(title)
    if not page_public:
        screenshot_test(page, 'page-010')
    assert page_public


@pytest.mark.test_id("page-011")
def test_creacion_contenido_largo_page_011(setup):
    page = setup
    page_page = PagePage(page)
    fake = Faker()
    title = fake.name()
    contenido = fake.sentence(nb_words=20000)

    # Given
    page_page.go_to_create_page()

    # When
    try:
        page_page.create_page(title=title, content=contenido)
    except TimeoutError as e:
        screenshot_test(page, f'POST-011_time')

    # Then
    page_public = page_page.is_page_published(title)
    if not page_public:
        screenshot_test(page, 'page-011')
    assert page_public



@pytest.mark.test_id("page-012")
def test_creacion_titulo_duplicado_012(setup):
    page = setup
    page_page = PagePage(page)
    fake = Faker()
    title = fake.name()
    contenido = fake.sentence(nb_words=10)

    # Given
    page_page.go_to_create_page()

    # When
    try:
        page_page.create_page(title=title, content=contenido)

    except TimeoutError as e:
        screenshot_test(page, f'POST-012_time')

    # Then
    page_page.go_to_create_page()
    try:
        page_page.create_page(title=title, content=contenido)

    except TimeoutError as e:
        screenshot_test(page, f'POST-012_time')

    page_public = page_page.is_page_published(title)
    if not page_public:
        screenshot_test(page, 'page-012')
    assert page_public