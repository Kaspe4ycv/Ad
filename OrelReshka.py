from .. import loader
import random

class OrelReshkaMod(loader.Module):
	strings = {"name": "OrelReshka"}
	
	async def monetkacmd(self, message):
		a = ["Орёл", "Решка"]
		b = random.choice(a)
		await message.edit("<b>Выпадает: </b>" + str(b))