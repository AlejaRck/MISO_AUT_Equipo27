import os
import pytest
from e2e_playwright_rc.metadata.path import Path
from playwright.sync_api import BrowserType, sync_playwright
from e2e_playwright_rc.page_object.login_page import LoginPage
from e2e_playwright_rc.page_object.page_post import PostPage
from e2e_playwright_rc.utils.screenshot import screenshot_test
from e2e_playwright_rc.utils.open_yaml import get_config, get_mockaroo_data
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


@pytest.mark.test_id("Post-001")
def test_creacion_post_sin_imagen_post_001(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    post_page = PostPage(page)

    post_data = get_mockaroo_data('post_001', 'post')
    prueba = 1
    for data in post_data:
        post_page.go_to_create_post()
        title = data['title']
        contenido = data['contenido']
        post_page.create_post(title=title, content=contenido)

        is_public = post_page.is_post_published(title)
        if not is_public:
            screenshot_test(page, f'POST-001-{prueba}')
            prueba += 1
        assert is_public


@pytest.mark.test_id("Post-002")
def test_creacion_post_sin_imagen_sin_titulo_post_002(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    post_page = PostPage(page)

    post_data = get_mockaroo_data('post_002', 'post')
    prueba = 1
    for data in post_data:
        post_page.go_to_create_post()
        contenido = data['contenido']
        post_page.create_post(content=contenido)

        is_public = post_page.is_post_not_published('')
        if not is_public:
            screenshot_test(page, f'POST-002-{prueba}')
            prueba += 1
        assert is_public


@pytest.mark.test_id("Post-003")
def test_creacion_post_sin_imagen_sin_contenido_post_003(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    post_page = PostPage(page)

    post_data = get_mockaroo_data('post_003', 'post')
    for data in post_data:
        post_page.go_to_create_post()
        title = data['title']
        post_page.create_post(title=title)

        is_public = post_page.is_post_published(title)
        if not is_public:
            screenshot_test(page, f'POST-003-{title}')
        assert is_public


@pytest.mark.test_id("Post-004")
def test_creacion_post_titulo_naughty_post_004(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    post_page = PostPage(page)

    post_data = get_mockaroo_data('post_004', 'post')
    for data in post_data:
        post_page.go_to_create_post()
        title = data['title']
        try:
            post_page.create_post(title=title)
        except TimeoutError as e:
            screenshot_test(page, f'POST-004_time')
            post_page.go_to_create_post()
        finally:
            is_public = post_page.is_post_published(title)
            if not is_public:
                screenshot_test(page, f'POST-004')

            assert is_public


@pytest.mark.test_id("Post-005")
def test_creacion_post_contenido_naughty_post_005(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    post_page = PostPage(page)

    post_data = get_mockaroo_data('post_005', 'post')
    for data in post_data:
        post_page.go_to_create_post()
        title = data['title']
        contenido = data['contenido']
        post_page.create_post(title=title, content=contenido)

        is_public = post_page.is_post_published(title)
        if not is_public:
            screenshot_test(page, f'POST-005-{title}')

        assert is_public


@pytest.mark.test_id("Post-006")
def test_creacion_post_espacios_blanco_post_006(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    post_page = PostPage(page)

    post_data = get_mockaroo_data('post_006', 'post')
    for data in post_data:
        title = data['title']
        contenido = data['contenido']
        post_page.go_to_create_post()
        try:
            post_page.create_post(title=title, content=contenido)
        except TimeoutError as e:
            screenshot_test(page, f'POST-006_time')

        finally:
            is_public = post_page.is_post_published(title)
            if not is_public:
                screenshot_test(page, f'POST-006')

            assert is_public



@pytest.mark.test_id("Post-007")
def test_creacion_post_titulo_largo_post_007(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    post_page = PostPage(page)

    post_data = get_mockaroo_data('post_007', 'post')
    for data in post_data:
        title = data['title']
        contenido = data['contenido']
        try:
            post_page.go_to_create_post()
            post_page.create_post(title=title, content=contenido)
        except TimeoutError as e:
            screenshot_test(page, f'POST-007_time')
        finally:
            is_public = post_page.is_post_not_published(title)

            if not is_public:
                screenshot_test(page, f'POST-007')

            assert is_public


@pytest.mark.test_id("Post-008")
def test_creacion_post_titulo_corto_post_008(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    post_page = PostPage(page)

    post_data = get_mockaroo_data('post_008', 'post')
    for data in post_data:
        post_page.go_to_create_post()
        title = data['title']
        contenido = data['contenido']
        post_page.create_post(title=title, content=contenido)

        is_public = post_page.is_post_published(title)
        if not is_public:
            screenshot_test(page, f'POST-008-{title}')

        assert is_public


@pytest.mark.test_id("Post-009")
def test_creacion_post_titulo_contenido_null_post_009(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    post_page = PostPage(page)

    post_data = get_mockaroo_data('post_009', 'post')
    for data in post_data:
        post_page.go_to_create_post()
        title = data['title']
        contenido = data['contenido']
        post_page.create_post(title=title, content=contenido)

        is_public = post_page.is_post_published(title)
        if not is_public:
            screenshot_test(page, f'POST-009-{title}')

        assert is_public


@pytest.mark.test_id("Post-010")
def test_creacion_post_titulo_emojis_post_010(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    post_page = PostPage(page)

    post_data = get_mockaroo_data('post_010', 'post')
    for data in post_data:
        post_page.go_to_create_post()
        title = data['title']
        try:
            post_page.create_post(title=title)
        except TimeoutError as e:
            screenshot_test(page, f'POST-010-time')
        finally:
            is_public = post_page.is_post_not_published(title)
            if not is_public:
                screenshot_test(page, f'POST-010')

            assert is_public


@pytest.mark.test_id("Post-011")
def test_creacion_post_titulo_numerico_post_011(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    post_page = PostPage(page)

    post_data = get_mockaroo_data('post_011', 'post')
    for data in post_data:
        post_page.go_to_create_post()
        title = data['title']
        try:
            post_page.create_post(title=str(title))
        except TimeoutError as e:
            screenshot_test(page, f'POST-011-time')
        finally:
            is_public = post_page.is_post_published(title)
            if not is_public:
                screenshot_test(page, f'POST-011-{title}')

            assert is_public


@pytest.mark.test_id("Post-012")
def test_creacion_post_titulo_duplicado_post_012(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    post_page = PostPage(page)

    post_data = get_mockaroo_data('post_012', 'post')
    for data in post_data:
        post_page.go_to_create_post()
        title = data['title']
        try:
            post_page.create_post(title=title)
        except TimeoutError as e:
            screenshot_test(page, f'POST-012-time')
        finally:
            is_public = post_page.is_post_published(title)
            if not is_public:
                screenshot_test(page, f'POST-012-{title}')
        try:
            post_page.create_post(title=title)
        except TimeoutError as e:
            screenshot_test(page, f'POST-012-time')
        finally:
            is_public = post_page.is_post_published(title)
            if not is_public:
                screenshot_test(page, f'POST-012-{title}')
            assert is_public
