from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
import pytest

queries = ['panda', 'python', 'dark souls']


@pytest.mark.parametrize('phrase', queries)
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    search_page.load()

    search_page.search(phrase)

    assert phrase == result_page.search_input_value()

    for title in result_page.result_link_titles():
        assert phrase.lower() in title.lower()

    assert phrase in result_page.title()
