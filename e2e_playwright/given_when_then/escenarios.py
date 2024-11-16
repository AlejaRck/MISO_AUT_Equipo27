import os
import pytest
from metadata.path import Path
from playwright.sync_api import BrowserType, sync_playwright
from page_object.login_page import LoginPage
from page_object.page_post import PostPage
from page_object.page_member import MemberPage
from page_object.page_tags import TagsPage
from page_object.page_page import PagePage
from page_object.page_config import ConfigPage
from utils.open_yaml import get_config
from utils.screenshot import screenshot_test
from faker import Faker



@pytest.fixture(scope="function")
def setup():
    config = get_config()

    os.makedirs(Path.result_img, exist_ok=True)

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

@pytest.fixture(scope="function")
def setup_sin_login():
    config = get_config()

    with sync_playwright() as p:
        # Lanzamos el navegador en modo no-headless (para ver el navegador)
        browser = p.chromium.launch(headless=False)  # Cambiar a headless=False para ver el navegador
        context = browser.new_context(ignore_https_errors=True, bypass_csp=True)
        page = context.new_page()

        # Devolver la página para usarla en las pruebas
        yield page

        # Cerrar el navegador después de la prueba
        context.close()
        browser.close()

@pytest.mark.test_id("AUT-001")
def test_creacion_exitosa_post_aut_001(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    post_page = PostPage(page)

    # Given
    post_page.go_to_create_post()

    # When
    post_page.create_post("New Post Title", "nuevo post")

    # Then
    is_public = post_page.is_post_published("New Post Title")
    screenshot_test(page, 'AUT-001')
    assert is_public


@pytest.mark.test_id("AUT-002")
def test_intentar_crear_un_post_sin_titulo_aut_002(setup):

    page = setup
    post_page = PostPage(page)

    # Given
    post_page.go_to_create_post()

    # When
    post_page.create_post("", "nuevo post")

    # Then
    not_public = post_page.is_post_not_published("")
    screenshot_test(page, 'AUT-002')
    assert not_public


@pytest.mark.test_id("AUT-003")
def test_creacion_exitosa_de_un_miembro_aut_003(setup):
    page = setup
    member_page = MemberPage(page)
    fake = Faker()
    nombre = fake.name()
    email = fake.email()
    # Given
    member_page.go_to_create_member()

    # When
    member_page.create_member(nombre, email)

    # Then
    created_member = member_page.is_member_created(nombre)
    screenshot_test(page, 'AUT-003')
    assert created_member


@pytest.mark.test_id("AUT-004")
def test_intentar_crear_un_miembro_sin_correo_electronico_aut_004(setup):
    page = setup
    member_page = MemberPage(page)
    fake = Faker()
    nombre = fake.name()
    email = ''
    # Given
    member_page.go_to_create_member()

    # When
    member_page.create_member(nombre, email)

    # Then
    no_present = member_page.is_email_no_present()
    screenshot_test(page, 'AUT-004')
    assert no_present


@pytest.mark.test_id("AUT-005")
def test_intento_de_crear_un_miembro_con_correo_duplicado_aut_005(setup):
    page = setup
    member_page = MemberPage(page)
    fake = Faker()
    nombre = fake.name()
    email = fake.email()
    # Given
    member_page.go_to_create_member()

    # When
    member_page.create_member(nombre, email)
    member_page.go_to_create_member()
    member_page.create_member(nombre, email)

    # Then
    is_duplicate = member_page.is_email_duplicate()
    screenshot_test(page, 'AUT-005')
    assert is_duplicate


@pytest.mark.test_id("AUT-009")
def test_creacion_exitosa_tag_aut_009(setup):
    page = setup
    tags_page = TagsPage(page)
    fake = Faker()
    nombre = fake.name()
    # Given
    tags_page.go_to_create_tags()

    # When
    tags_page.create_tag(nombre)

    # Then
    tag_created = tags_page.is_tag_created(nombre)
    screenshot_test(page, 'AUT-009')
    assert tag_created


@pytest.mark.test_id("AUT-010")
def test_intentar_crear_un_tag_sin_autenticacion_aut_0010(setup_sin_login):

    page = setup_sin_login
    tags_page = TagsPage(page)
    #Given
    tags_page.go_to_create_tags_sin_aut()
    #when
    validate_page_tags = tags_page.validate_page_tags_sin_aut()

    #Then
    screenshot_test(page, 'AUT-010')
    assert validate_page_tags


@pytest.mark.test_id("AUT-006")
def test_creacion_exitosa_pagina_aut_006(setup):
    page = setup
    page_page = PagePage(page)
    fake = Faker()
    title = fake.name()
    # Given
    page_page.go_to_create_page()

    # When
    page_page.create_page(title, 'nueva pagina')

    # Then
    page_public = page_page.is_page_published(title)
    screenshot_test(page, 'AUT-006')
    assert page_public


@pytest.mark.test_id("AUT-007")
def test_intentar_crear_pagina_sin_contenido_aut_007(setup):
    page = setup
    page_page = PagePage(page)
    fake = Faker()
    title = fake.name()
    # Given
    page_page.go_to_create_page()

    # When
    page_page.create_page(title, '')

    # Then
    page_public = page_page.is_page_published(title)
    screenshot_test(page, 'AUT-007')
    assert not page_public


@pytest.mark.test_id("AUT-008")
def test_actualizacion_del_sitio_aut_008(setup):
    page =  setup
    config_page =  ConfigPage(page)
    fake = Faker()
    title = fake.name()

    #    Given
    config_page.go_to_config_page()

     # When
    config_page.actualizar_config_page(title)

    # Then
    page_updated = config_page.is_title_updated(title)
    screenshot_test(page, 'AUT-008')
    assert page_updated
