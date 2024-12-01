import os
from importlib.resources import contents

import pytest
from e2e_playwright_rc.metadata.path import Path
from playwright.sync_api import BrowserType, sync_playwright
from e2e_playwright_rc.page_object.login_page import LoginPage
from e2e_playwright_rc.page_object.page_post import PostPage
from e2e_playwright_rc.page_object.page_member import MemberPage
from e2e_playwright_rc.page_object.page_tags import TagsPage
from e2e_playwright_rc.page_object.page_page import PagePage
from e2e_playwright_rc.page_object.page_config import ConfigPage
from e2e_playwright_rc.utils.open_yaml import get_config
from e2e_playwright_rc.utils.screenshot import screenshot_test
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


@pytest.mark.test_id("SEM8-001")
def test_edit_post_sem8_001(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    post_page = PostPage(page)
    fake = Faker()
    title = fake.name()
    contenido = fake.sentence(nb_words=10)

    # Given
    post_page.go_to_create_post()

    # When
    post_page.create_post(title, contenido)

    # Then
    post_page.go_to_public_post(title)

    new_title = fake.name()
    new_contenido = fake.sentence(nb_words=10)
    post_page.edit_post(new_title, new_contenido)

    # Then
    publicado = post_page.is_post_published(new_title)
    screenshot_test(page, 'SEM8-001')

    assert publicado


@pytest.mark.test_id("SEM8-002")
def test_post_eliminar_titutlo_sem8_002(setup):
    # Accedemos a la página que ya está autenticada
    page = setup
    post_page = PostPage(page)
    fake = Faker()
    title = fake.name()
    contenido = fake.sentence(nb_words=10)

    # Given
    post_page.go_to_create_post()

    # When
    post_page.create_post(title, contenido)

    # Then
    post_page.go_to_public_post(title)

    new_contenido = fake.sentence(nb_words=10)
    post_page.edit_post(content=new_contenido)

    # Then
    publicado = post_page.is_post_not_published()
    screenshot_test(page, 'SEM8-002')

    assert publicado


@pytest.mark.test_id("SEM8-003")
def test_edicion_de_un_miembro_sem_003(setup):
    page = setup
    member_page = MemberPage(page)
    fake = Faker()
    nombre = fake.name()
    email = fake.email()
    # Given created_member
    member_page.go_to_create_member()

    # When
    member_page.create_member(nombre, email)

    # Then
    new_nombre = fake.name()
    new_email = fake.email()
    member_page.go_to_edit_member(nombre)
    member_page.create_member(new_nombre, new_email)

    created_member = member_page.is_member_created(nombre)

    screenshot_test(page, 'SEM8-003')
    assert created_member


@pytest.mark.test_id("SEM8-004")
def test_eliminar_nombre_de_un_miembro_sem_004(setup):
    page = setup
    member_page = MemberPage(page)
    fake = Faker()
    nombre = fake.name()
    email = fake.email()
    # Given created_member
    member_page.go_to_create_member()

    # When
    member_page.create_member(nombre, email)

    # Then
    new_email = fake.email()
    member_page.go_to_edit_member(nombre)
    member_page.create_member(email=new_email)

    created_member = member_page.is_member_created()

    screenshot_test(page, 'SEM8-004')
    assert not created_member


@pytest.mark.test_id("SEM8-005")
def test_editar_tag_sem_005(setup):
    page = setup
    tags_page = TagsPage(page)
    fake = Faker()
    nombre = fake.name()
    slug = fake.word()
    # Given
    tags_page.go_to_create_tags()

    # When
    tags_page.create_tag(title=nombre,slug=slug)

    # Then
    tags_page.go_to_edit_tag(nombre)
    new_name = fake.name()
    new_slug = fake.word()
    tags_page.create_tag(title=new_name, slug=new_slug)
    tag_created = tags_page.is_tag_created(new_name)
    screenshot_test(page, 'SEM-005')
    assert tag_created


@pytest.mark.test_id("SEM8-006")
def test_eliminar_slug_tag_sem_006(setup):
    page = setup
    tags_page = TagsPage(page)
    fake = Faker()
    nombre = fake.name()
    slug = fake.word()
    # Given
    tags_page.go_to_create_tags()

    # When
    tags_page.create_tag(title=nombre,slug=slug)

    # Then
    tags_page.go_to_edit_tag(nombre)
    new_name = fake.name()
    tags_page.create_tag(title=new_name)
    tag_created = tags_page.is_tag_created(new_name)
    screenshot_test(page, 'SEM-006')
    assert tag_created


@pytest.mark.test_id("SEM8-007")
def test_editar_pagina_sem8_007(setup):
    page = setup
    page_page = PagePage(page)
    fake = Faker()
    title = fake.name()
    contenido = fake.sentence(nb_words=10)
    # Given
    page_page.go_to_create_page()

    # When
    page_page.create_page(title, content=contenido)
    page_page.go_to_public_page(title)

    # Then
    new_title = fake.name()
    new_contenido = fake.sentence(nb_words=10)
    page_page.edit_page(new_title, new_contenido)

    page_public = page_page.is_page_published(new_title)
    screenshot_test(page, 'SEM8-007')
    assert page_public


@pytest.mark.test_id("SEM8-008")
def test_eliminar_nombre_pagina_sem8_008(setup):
    page = setup
    page_page = PagePage(page)
    fake = Faker()
    title = fake.name()
    contenido = fake.sentence(nb_words=10)
    # Given
    page_page.go_to_create_page()

    # When
    page_page.create_page(title, content=contenido)
    page_page.go_to_public_page(title)

    # Then
    new_contenido = fake.sentence(nb_words=10)
    page_page.edit_page(new_contenido=new_contenido)

    page_public = page_page.is_page_published()
    screenshot_test(page, 'SEM8-008')
    assert not page_public