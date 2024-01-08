from playwright.sync_api import Page


class SearchPage:
    def __init__(self, page: Page):
        self.page = page

        self.search_button = page.locator("button[aria-label='Search']")
        self.search_input = page.locator("#searchbox_input")

    def load(self, url):
        self.page.goto(url)

        return self

    def search(self, phrase: str):
        self.search_input.fill(phrase)
        self.search_button.click()

        return self
