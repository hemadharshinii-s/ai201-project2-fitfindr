from tools import (
    search_listings,
    suggest_outfit,
    create_fit_card,
)

from utils.data_loader import (
    get_example_wardrobe,
    get_empty_wardrobe,
)


def test_search_returns_results():
    results = search_listings(
        "vintage graphic tee",
        size=None,
        max_price=50,
    )

    assert isinstance(results, list)
    assert len(results) > 0


def test_search_empty_results():
    results = search_listings(
        "designer ballgown",
        size="XXS",
        max_price=5,
    )

    assert results == []


def test_search_price_filter():
    results = search_listings(
        "jacket",
        size=None,
        max_price=10,
    )

    assert all(item["price"] <= 10 for item in results)


def test_search_size_filter():
    results = search_listings(
        "shirt",
        size="M",
        max_price=500,
    )

    for item in results:
        assert "M" in item["size"].upper()


def test_suggest_outfit_empty_wardrobe():
    item = search_listings(
        "vintage graphic tee",
        max_price=50,
    )[0]

    result = suggest_outfit(
        item,
        get_empty_wardrobe(),
    )

    assert isinstance(result, str)
    assert len(result.strip()) > 0


def test_suggest_outfit_example_wardrobe():
    item = search_listings(
        "vintage graphic tee",
        max_price=50,
    )[0]

    result = suggest_outfit(
        item,
        get_example_wardrobe(),
    )

    assert isinstance(result, str)
    assert len(result.strip()) > 0


def test_create_fit_card_empty_outfit():
    item = search_listings(
        "vintage graphic tee",
        max_price=50,
    )[0]

    result = create_fit_card("", item)

    assert isinstance(result, str)
    assert "missing" in result.lower()


def test_create_fit_card_valid():
    item = search_listings(
        "vintage graphic tee",
        max_price=50,
    )[0]

    outfit = (
        "Pair the tee with relaxed jeans and chunky sneakers "
        "for an effortless vintage streetwear look."
    )

    result = create_fit_card(outfit, item)

    assert isinstance(result, str)
    assert len(result.strip()) > 0