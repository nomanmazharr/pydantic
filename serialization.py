from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    Postcode: int

class Player(BaseModel):
    name: str
    age: int
    address: Address


player_address  = {'city': 'Faisalabad', 'state': 'punjab', 'Postcode': 38000}

address = Address(**player_address)

player_biodata = {'name': 'Jon', 'age': 30, 'address': address}

player = Player(**player_biodata)

print(player)
temp = player.model_dump(exclude_unset=True)
print(type(temp))