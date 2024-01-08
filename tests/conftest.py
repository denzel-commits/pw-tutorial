import pytest
from playwright.sync_api import Page

from src.pages.result import ResultPage
from src.pages.search import SearchPage


def pytest_addoption(parser):
    parser.addoption("--base_url", required=True, help="Base application URL")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture()
def search_page(page: Page):
    return SearchPage(page)


@pytest.fixture()
def result_page(page: Page):
    return ResultPage(page)
