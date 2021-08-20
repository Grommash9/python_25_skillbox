import math
from vehicle import Vehicle, Bus

nabi = Bus(0, 0, 0)

print()

nabi.turn('влево', 5000)
nabi.move(-10)
nabi.move(152)

print()

nabi.take_passengers(11)
nabi.turn('влево', 70)
nabi.move(-40)
nabi.move(700)

print()

nabi.let_passengers_go(3)
nabi.turn('вправо', 100)
nabi.move(-50)
nabi.move(200)

print()

print(f'всего вы заработали {nabi.get_money()} $')
