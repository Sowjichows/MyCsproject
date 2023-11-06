from Food.Icecream import Icecream
from Food.Samosa import Samosa
from Food.Vadapav import Vadapav

Icecream = Icecream("Amul", "Chennai", 560, "Serves 2", "Mixed fruit")
Vadapav =  Vadapav("Aalo pav", "Mumbai", 720, "Serves 2", "Texture is crucial")
Samosa = Samosa("Large Samosa", "Hyderabad", 210, "Serves 1", "Spicy taste")


print(Icecream.category())
print(Vadapav.category())
print(Samosa.category())
print(Icecream.price())
print(Vadapav.price())
print(Samosa.price())
