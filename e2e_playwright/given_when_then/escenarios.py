import time

import pytest
from playwright.sync_api import sync_playwright
from page_object.login_page import LoginPage
from page_object.page_post import PostPage
from page_object.create_member import MemberPage
from page_object.page_tags import TagsPage
from page_object.page_page import PagePage
from page_object.page_config import ConfigPage
from utils.open_yaml import get_config
from faker import Faker


@pytest.fixture(scope="function")
def setup():
    config = get_config()

    with sync_playwright() as p:
        # Lanzamos el navegador en modo no-headless (para ver el navegador)
        browser = p.chromium.launch(headless=False)  # Cambiar a headless=False para ver el navegador
        context = browser.new_context()
        page = context.new_page()

        # Accedemos al sitio de inicio de sesión
        page.goto(config['ghost_url'])

        # Realizamos el login
        login_page = LoginPage(page)
        login_page.login_as_admin(config['admin_user'], config['admin_pass'])

        # Devolver la página para usarla en las pruebas
        yield page

        # Cerrar el navegador después de la prueba
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
    assert post_page.is_post_published("New Post Title")


@pytest.mark.test_id("AUT-002")
def test_intentar_crear_un_post_sin_titulo_aut_002(setup):

    page = setup
    post_page = PostPage(page)

    # Given
    post_page.go_to_create_post()

    # When
    post_page.create_post("", "nuevo post")

    # Then
    assert post_page.is_post_not_published("")


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
    assert member_page.is_member_created(nombre)


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
    assert member_page.is_email_no_present()


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
    nombre = fake.name()
    member_page.create_member(nombre, email)

    # Then
    assert member_page.is_email_duplicate()


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
    assert tags_page.is_tag_created(nombre)


@pytest.mark.test_id("AUT-010")
def test_intentar_crear_un_tag_sin_autenticacion_aut_0010():
    with sync_playwright() as p:
        # Lanzamos el navegador en modo no-headless (para ver el navegador)
        browser = p.chromium.launch(headless=False)  # Cambiar a headless=False para ver el navegador
        context = browser.new_context()
        page_new = context.new_page()

        config = get_config()
        page_new.goto(f'{config["ghost_url"]}/#/tags/new')
        
        page_new.wait_for_load_state()
        page_new.wait_for_selector("input[name='identification']")
        input_element = page_new.query_selector("input[name='identification']")

        assert input_element is not None and input_element.is_visible()


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

    assert page_page.is_page_published(title)


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
    assert not page_page.is_page_published(title)


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
    assert config_page.is_title_updated(title)
