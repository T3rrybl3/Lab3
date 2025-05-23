import price_info as p


def test_total_cost_shopping():
    price = p.total_cost_shopping()

    assert (price == 46.75)


def test_cost_of_fruit():
    price = p.cost_of_fruits('pear', 1)

    assert (price == 0.90)
