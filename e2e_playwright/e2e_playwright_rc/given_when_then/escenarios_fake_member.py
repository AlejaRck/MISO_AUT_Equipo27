import os
import pytest
import random
from e2e_playwright_rc.metadata.path import Path
from playwright.sync_api import BrowserType, sync_playwright
from e2e_playwright_rc.page_object.login_page import LoginPage
from e2e_playwright_rc.page_object.page_member import MemberPage
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


@pytest.mark.test_id("mem-001")
def test_creacion_miembro_sin_email_mem_001(setup):
    page = setup
    member_page = MemberPage(page)
    fake = Faker()
    nombre = fake.name()
    lable = fake.name()
    note = fake.sentence()
    # Given
    member_page.go_to_create_member()

    # When
    member_page.create_member(name=nombre, label=lable, note=note)

    # Then
    no_present = member_page.is_email_no_present()
    screenshot_test(page, 'mem-001')
    assert no_present


@pytest.mark.test_id("mem-002")
def test_creacion_miembro_sin_labels_mem_002(setup):
    page = setup
    member_page = MemberPage(page)
    fake = Faker()
    email = fake.email()
    nombre = fake.name()
    note = fake.sentence()
    # Given
    member_page.go_to_create_member()

    # When
    member_page.create_member(name=nombre, email=email, note=note)

    # Then
    no_present = member_page.is_member_created(nombre)
    screenshot_test(page, 'mem-002')
    assert no_present


@pytest.mark.test_id("mem-003")
def test_creacion_miembro_sin_notes_mem_003(setup):
    page = setup
    member_page = MemberPage(page)
    fake = Faker()
    email = fake.email()
    nombre = fake.name()
    lable = fake.name()

    # Given
    member_page.go_to_create_member()

    # When
    member_page.create_member(name=nombre, email=email, label=lable)

    # Then
    no_present = member_page.is_member_created(nombre)
    screenshot_test(page, 'mem-003')
    assert no_present


@pytest.mark.test_id("mem-004")
def test_creacion_miembro_email_sin_arroba_mem_004(setup):
    page = setup
    member_page = MemberPage(page)
    fake = Faker()
    email = fake.user_name() + ".com"
    nombre = fake.name()
    lable = fake.name()
    note = fake.sentence()

    # Given
    member_page.go_to_create_member()

    # When
    member_page.create_member(name=nombre, email=email, label=lable, note=note)

    # Then
    no_present = member_page.invalid_email()
    screenshot_test(page, 'mem-004')
    assert no_present


@pytest.mark.test_id("mem-005")
def test_creacion_miembro_nombre_especiales_mem_005(setup):
    page = setup
    member_page = MemberPage(page)
    fake = Faker()
    email = fake.email()
    caracteres_especiales = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    nombre = fake.name()
    nombre = ''.join(
        char + random.choice(caracteres_especiales) if random.random() > 0.9 else char
        for char in nombre
    )
    lable = fake.name()
    note = fake.sentence()

    # Given
    member_page.go_to_create_member()

    # When
    member_page.create_member(name=nombre, email=email, label=lable, note=note)

    # Then
    no_present = member_page.is_member_created(nombre)
    screenshot_test(page, 'mem-005')
    assert no_present


@pytest.mark.test_id("mem-006")
def test_creacion_miembro_note_largo_mem_006(setup):
    page = setup
    member_page = MemberPage(page)
    fake = Faker()
    email = fake.email()
    nombre = fake.name()
    lable = fake.name()
    note = fake.sentence(nb_words=700)

    # Given
    member_page.go_to_create_member()

    # When
    member_page.create_member(name=nombre, email=email, label=lable, note=note)

    # Then
    no_present = member_page.note_long()
    screenshot_test(page, 'mem-006')
    assert no_present


@pytest.mark.test_id("mem-007")
def test_creacion_miembro_note_emojis_mem_007(setup):
    page = setup
    member_page = MemberPage(page)
    fake = Faker()
    email = fake.email()
    nombre = fake.name()
    lable = fake.name()
    note = fake.sentence(nb_words=10)
    emoji = chr(random.randint(0x1F600, 0x1F64F))  # Emoji aleatorio
    note = f"{emoji} {note} {emoji}"

    # Given
    member_page.go_to_create_member()

    # When
    member_page.create_member(name=nombre, email=email, label=lable, note=note)

    # Then
    no_present = member_page.is_member_created(nombre)
    screenshot_test(page, 'mem-007')
    assert no_present


@pytest.mark.test_id("mem-008")
def test_creacion_miembro_validos_mem_008(setup):
    page = setup
    member_page = MemberPage(page)
    fake = Faker()
    nombre = fake.name()
    lable = fake.name()
    note = fake.sentence()
    email = fake.email()
    # Given
    member_page.go_to_create_member()

    # When
    member_page.create_member(name=nombre, label=lable, note=note, email=email)

    # Then
    no_present = member_page.is_member_created(nombre)
    screenshot_test(page, 'mem-008')
    assert no_present



@pytest.mark.test_id("mem-009")
def test_intento_de_crear_un_miembro_con_correo_duplicado_mem_009(setup):
    page = setup
    member_page = MemberPage(page)
    fake = Faker()
    nombre = fake.name()
    email = fake.email()
    note =  fake.sentence()
    # Given
    member_page.go_to_create_member()

    # When
    member_page.create_member(name=nombre, email=email, note=note)
    member_page.go_to_create_member()
    member_page.create_member(name=nombre, email=email, note=note)

    # Then
    is_duplicate = member_page.is_email_duplicate()
    screenshot_test(page, 'mem-009')
    assert is_duplicate



@pytest.mark.test_id("mem-010")
def test_intento_de_crear_un_miembro_sin_nombre_mem_010(setup):
    page = setup
    member_page = MemberPage(page)
    fake = Faker()
    email = fake.email()
    note =  fake.sentence()
    # Given
    member_page.go_to_create_member()

    # When
    member_page.create_member(email=email, note=note)

    # Then
    is_duplicate = member_page.is_member_created()
    screenshot_test(page, 'mem-010')
    assert is_duplicate


@pytest.mark.test_id("mem-011")
def test_intento_de_crear_un_miembro_nombre_largo_mem_011(setup):
    page = setup
    member_page = MemberPage(page)
    fake = Faker()
    email = fake.email()
    note =  fake.sentence()
    nombre = fake.sentence(nb_words=300)
    # Given
    member_page.go_to_create_member()

    # When
    member_page.create_member(email=email, note=note, name=nombre)

    # Then
    is_duplicate = member_page.is_member_created(nombre)
    screenshot_test(page, 'mem-011')
    assert is_duplicate


@pytest.mark.test_id("mem-012")
def test_intento_de_crear_un_miembro_nombre_emoji_mem_012(setup):
    page = setup
    member_page = MemberPage(page)
    fake = Faker()
    email = fake.email()
    note =  fake.sentence()
    nombre = fake.name()
    emoji = chr(random.randint(0x1F600, 0x1F64F))  # Emoji aleatorio
    nombre = f"{emoji} {nombre} {emoji}"
    # Given
    member_page.go_to_create_member()

    # When
    member_page.create_member(email=email, note=note, name=nombre)

    # Then
    is_duplicate = member_page.is_member_created(nombre)
    screenshot_test(page, 'mem-012')
    assert is_duplicate


@pytest.mark.test_id("mem-013")
def test_intento_de_crear_un_miembro_nombre_numerico_mem_013(setup):
    page = setup
    member_page = MemberPage(page)
    fake = Faker()
    email = fake.email()
    note =  fake.sentence()
    nombre = str(fake.random_number(digits=8))

    # Given
    member_page.go_to_create_member()

    # When
    member_page.create_member(email=email, note=note, name=nombre)

    # Then
    is_duplicate = member_page.is_member_created(nombre)
    screenshot_test(page, 'mem-013')
    assert is_duplicate



@pytest.mark.test_id("mem-014")
def test_intento_de_crear_un_miembro_nombre_espacios_blancos_mem_014(setup):
    page = setup
    member_page = MemberPage(page)
    fake = Faker()
    email = fake.email()
    note =  fake.sentence()
    nombre = fake.name()
    nombre_blanco = f' {nombre} '

    # Given
    member_page.go_to_create_member()

    # When
    member_page.create_member(email=email, note=note, name=nombre_blanco)

    # Then
    is_duplicate = member_page.is_member_created(nombre)
    screenshot_test(page, 'mem-014')
    assert is_duplicate



@pytest.mark.test_id("mem-015")
def test_intento_de_crear_un_miembro_email_espacios_blancos_mem_015(setup):
    page = setup
    member_page = MemberPage(page)
    fake = Faker()
    email = fake.email()
    note =  fake.sentence()
    nombre = fake.name()
    email_blanco = f' {email} '

    # Given
    member_page.go_to_create_member()

    # When
    member_page.create_member(email=email_blanco, note=note, name=nombre)

    # Then
    is_duplicate = member_page.is_member_created(nombre)
    screenshot_test(page, 'mem-015')
    assert is_duplicate