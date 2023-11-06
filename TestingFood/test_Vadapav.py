from Food.Vadapav import Vadapav


Vadapav = Vadapav("Aalo pav", "Hyderabad", 720, "Serves 2", "Texture is crucial")

def test_Vadapav_category():
    assert Vadapav.category() == "It is a Weather-food"

def test_Vadapav_price():
    assert Vadapav.price() == "It costs around $30"

 
