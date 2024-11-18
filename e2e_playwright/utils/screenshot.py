import os
from playwright.sync_api import Page
from metadata.path import Path


def screenshot_test(page:Page, test_id:str):
    path = os.path.join(Path.result_img_versrion_rc, f'{test_id}.png')
    page.screenshot(path=path)