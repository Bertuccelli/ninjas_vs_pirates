from classes.ninja import Ninja
from classes.pirate import Pirate
import random

turn = random.randint(1,2)



michelangelo = Ninja("Michelangelo")
jack_sparrow = Pirate("Jack Sparrow")

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

play = True

Ninja.compare_speed(michelangelo.speed, jack_sparrow.speed)

while play == True:
    if turn ==1:
        michelangelo.choose_action(jack_sparrow)
        if jack_sparrow.health <=0:
            play = False
        turn = 2
    if turn == 2:
        jack_sparrow.choose_action(michelangelo)
        if michelangelo.health <=0:
            play = False
        turn = 1