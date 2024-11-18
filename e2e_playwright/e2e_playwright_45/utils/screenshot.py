import os
from playwright.sync_api import Page
from e2e_playwright_45.metadata.path import Path


def screenshot_test(page:Page, test_id:str):
    path = os.path.join(Path.result_img_version_base, f'{test_id}.png')
    page.screenshot(path=path)