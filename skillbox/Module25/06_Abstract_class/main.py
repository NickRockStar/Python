import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.goto(
        "https://www.google.com/search?q=%D0%A1%D1%85%D0%B5%D0%BC%D0%B0+%D0%BC%D0%B5%D1%82%D1%80%D0%BE&sca_esv=be445f0cc062ab15&source=hp&ei=8So5ZtyrAq_BwPAPqrKEkA4&iflsig=AL9hbdgAAAAAZjk5AQJDoCkBPqVU5Jdjb-c620AFEfJl&udm=&ved=0ahUKEwic6PH73PmFAxWvIBAIHSoZAeIQ4dUDCA0&uact=5&oq=&gs_lp=Egdnd3Mtd2l6IgBIAFAAWABwAHgAkAEAmAEAoAEAqgEAuAEDyAEAmAIAoAIAmAMAkgcAoAcA&sclient=gws-wiz")
    page.goto("https://yandex.ru/metro/moscow?scheme_id=sc34974011")
    page.get_by_role("link", name="Москва — схема метро Яндекс").click()
    page.get_by_placeholder("Откуда").click()
    # page.get_by_placeholder("Откуда").fill("Ряза")
    page.get_by_role("list").get_by_text("Рязанский проспект").click()
    page.get_by_placeholder("Куда", exact=True).click()
    page.get_by_placeholder("Куда", exact=True).fill("Перо")
    page.get_by_role("list").get_by_text("Перово").nth(1).click()
    page.locator("svg").filter(
        has_text="D3D3D1D1D2D2D4AD4D41122334566778991010121411A8A15151111 bus-terminal-14 copy 6").click()
    page.get_by_placeholder("Откуда").click()
    page.get_by_placeholder("Куда", exact=True).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
