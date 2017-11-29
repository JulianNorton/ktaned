import inflect
from ktaned import Bomb, SimpleWires

p = inflect.engine()

# Set up a bomb object
bomb = Bomb()
bomb.serial = 'abc123'
bomb.batteries = True
bomb.labels = ['FRK']

# Set up a simple wire module
module1 = SimpleWires(bomb)
module1.set_wires(['yellow', 'yellow', 'yellow']) # Or module1.add_wire(<color>)

# Solve it!
solution = module1.solve()
print('Cut the {} wire'.format(p.ordinal(solution)))
# > Cut the 3rd wire