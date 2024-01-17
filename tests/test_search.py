import json

import pytest
import re

from playwright.sync_api import expect, Page

from src.pages.result import ResultPage
from src.pages.search import SearchPage

ANIMALS = [
    'panda',
    'python',
    'polar bear',
    'parrot',
    'porcupine',
    'parakeet',
    'pangolin',
    'panther',
    'platypus',
    'peacock'
]


@pytest.mark.parametrize("search_phrase", ANIMALS)
def test_basic_duckduckgo_search(search_phrase,
                                 page: Page,
                                 search_page: SearchPage,
                                 result_page: ResultPage,
                                 base_url) -> None:

    search_page.\
        load(base_url).\
        search(search_phrase)

    expect(result_page.search_input).to_have_value(search_phrase), "Search input does not contain search phrase"

    assert result_page.result_link_titles_contain_phrase(search_phrase, 2), "Result links are not related to search"

    expect(page).to_have_title(re.compile(search_phrase)), "Page title does not contain search phrase"


@pytest.mark.skip("Simple test")
def test_basic_duckduckgo_search_simple(page: Page) -> None:
    search_value = 'panda'

    # Given the DuckDuckGo home page is displayed
    page.goto('https://duckduckgo.com')

    # When the user searches for a phrase
    page.locator("#searchbox_input").fill(search_value)
    page.locator("button[aria-label='Search']").click()

    # Then the search result query is the phrase
    expect(page.locator("#search_form_input")).to_have_value(search_value)

    # And the search result links pertain to the phrase
    page.locator('a[data-testid="result-title-a"]').nth(4).wait_for()
    titles = page.locator('a[data-testid="result-title-a"]').all_text_contents()
    matches = [t for t in titles if search_value in t.lower()]
    assert len(matches) > 0

    # And the search result title contains the phrase
    expect(page).to_have_title(re.compile(search_value))


def test_mytest():
    response = '[{"owner_url": "https://api.github.com/orgs/octocat", ' \
               '"url": "https://api.github.com/projects/1002605", ' \
               '"html_url": "https://github.com/orgs/api-playground/projects/1", ' \
               '"columns_url": "https://api.github.com/projects/1002605/columns", ' \
               '"id": 1002605, ' \
               '"node_id": "MDc6UHJvamVjdDEwMDI2MDU=", ' \
               '"name": "Organization Roadmap", ' \
               '"body": "High-level roadmap for the upcoming year.", ' \
               '"created_at": "2011-04-11T20:09:31Z", ' \
               '"updated_at": "2014-03-04T18:58:10Z", ' \
               '"organization_permission": "write", ' \
               '"private": true },' \
               '{' \
               '"owner_url": "https://api.github.com/orgs/octocat", ' \
               '"url": "https://api.github.com/projects/1002605", ' \
               '"html_url": "https://github.com/orgs/api-playground/projects/1", ' \
               '"columns_url": "https://api.github.com/projects/1002605/columns", ' \
               '"id": 1002605, ' \
               '"node_id": "MDc6UHJvamVjdDEwMDI2MDU=", ' \
               '"name": "Target project", ' \
               '"body": "High-level roadmap for the upcoming year.", ' \
               '"created_at": "2011-04-11T20:09:31Z", ' \
               '"updated_at": "2014-03-04T18:58:10Z", ' \
               '"organization_permission": "write", ' \
               '"private": true }]'

    dictionary_response = json.loads(response)

    gh_project_name = "Target project"
    projects = [project for project in dictionary_response if project["name"] == gh_project_name]
    project = projects[0]

    filtered = filter(lambda x: x['name'] == gh_project_name, dictionary_response)
    print("filtered", list(filtered)[0])

    assert project, "No such project found"
    print(project)

    text = '[1, 2, 3]'
    parse = text.strip('[]').replace(' ', '').split(',')

    parsed = [p for p in parse if p != '2']  # filter out list or find in list [0]
    parsed = [int(p) for p in parse]  # map list to int

    print(parsed)

    parsed_to_str = [str(v) for v in parsed]
    print(" ".join(parsed_to_str))

    def testf(k, *args, **kwargs):
        print(k)
        print(args)
        print(kwargs)

        # better than filer with lambda
        s = '12324'
        suml = sum([int(n) for n in s])

        print("suml", suml)

    scores = [3, '5', 6]
    testf("first param", scores, {1: "name", '2': 'dict'}, param=23)



