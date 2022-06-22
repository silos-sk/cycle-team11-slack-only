import constants

from game.scripting.action import Action
from game.casting.cycle import Cycle
from game.shared.point import Point


class ResetGameAction(Action):
    """
    An action that resets the game.
    
    The responsibility of ResetGameAction is to clear the players and reset their original states
    """

    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        #delete the original cycles and game over message
        cycle_one = cast.get_first_actor("cycle_one")
        cycle_two = cast.get_first_actor("cycle_two")
        cast.remove_actor("cycle_one", cycle_one)
        cast.remove_actor("cycle_two", cycle_two)

        game_over = cast.get_actors("messages")
        for i in game_over:
            cast.remove_actor("messages", i)
        
        #recreate the cycles in their original positions
        cycle_one = Cycle(Point(int(constants.MAX_X - 600), int(constants.MAX_Y / 2)))
        cycle_two = Cycle(Point(int(constants.MAX_X - 300), int(constants.MAX_Y / 2)))
        cycle_one.set_cycle_color(constants.RED)
        cycle_two.set_cycle_color(constants.GREEN)
        
        cycle_one_name = "Player one"
        cycle_two_name = "Player two"
        cycle_one.set_name(cycle_one_name)
        cycle_two.set_name(cycle_two_name)

        cast.add_actor("cycle_one", cycle_one)
        cast.add_actor("cycle_two", cycle_two)