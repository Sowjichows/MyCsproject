from Food.Icecream import Icecream

Icecream = Icecream("Amul", "Chennai", 560, "Serves 2", "Mixed fruit")


def test_icecream_category():
    assert Icecream.category() == "It is a Desert-dish"

def test_Icecream_price():
    assert Icecream.price() == "It costs around $6"