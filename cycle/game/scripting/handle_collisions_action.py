import constants

from game.scripting.action import Action
from game.shared.point import Point
from game.casting.game_over_action import GameOver
from game.scripting.reset_game_action import ResetGameAction


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when a cycle collides
    with its segments or the segments of the other cycle, or the game is over.

    Attributes:
    ---
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self, keyboard_service):
        """Constructs a new HandleCollisionsAction.
        
        Args:
        ---
            keyboard_service (KeyboardService): An instance of KeyboardService.
            """
        self._is_game_over = False
        self._game_over_action = ""
        self._keyboard_service = keyboard_service

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
        ---
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
        self._handle_wall(cast)
        self._handle_game_over(cast, script)

    def _handle_wall(self, cast):
        """"Handles how the cycles interact with the walls

        Args:
        ---
            cast (Cast): The cast of Actors in the game.
        """

        cycle_one = cast.get_first_actor("cycle_one")
        cycle_two = cast.get_first_actor("cycle_two")
        cycle_one.wall(self._is_game_over)
        cycle_two.wall(self._is_game_over)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if a cycle collides with one of its segments or the other
        cycle.

        Args:
        ---
            cast (Cast): The cast of Actors in the game.
        """
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        # Adjustments for two players
        cycle_one = cast.get_first_actor("cycle_one")
        cycle_two = cast.get_first_actor("cycle_two")

        cycle_one_head = cycle_one.get_cycle()
        cycle_two_head = cycle_two.get_cycle()
        
        segments_one = cycle_one.get_segments()[1:]
        segments_two = cycle_two.get_segments()[1:]

        
        
        # which user wins and displays their name

        # If cycle_two hits cycle_one's then displays cycle_one wins
        for segment_one in segments_one:
            if cycle_two_head.get_position().equals(segment_one.get_position()):
                score1.add_points(1)
                self._game_over_action = f"{cycle_one.get_name()} wins!\nPress spacebar to reset!"
                self._is_game_over = True
            
            # If cycle_one hits its own body then displays cycle_two wins
            if cycle_one_head.get_position().equals(segment_one.get_position()):
                #first check to see if they both hit themselves
                for segment_two in segments_two:
                    if cycle_two_head.get_position().equals(segment_two.get_position()):
                        self._game_over_action = f"Game Over!\nPress spacebar to reset!"
                        self._is_game_over = True
                        #something I did glitches and gives cycle_two a point anyway, this corrects that
                        score2.reduce_points()
                    #otherwise proceed with cycle_two wins
                    else:
                        if self._is_game_over == False:
                            score2.add_points(1)
                            self._game_over_action = f"{cycle_two.get_name()} wins!\nPress spacebar to reset!"
                            self._is_game_over = True

        # If cycle one hits cycle_two's body then displays cycle_two wins
        for segment_two in segments_two:
            if cycle_one_head.get_position().equals(segment_two.get_position()):
                score2.add_points(1)
                self._game_over_action = f"{cycle_two.get_name()} wins!\nPress spacebar to reset!"
                self._is_game_over = True

            # If cycle_two hits its own body then displays cycle_one wins
            if self._is_game_over == False:
                if cycle_two_head.get_position().equals(segment_two.get_position()):
                    score1.add_points(1)
                    self._game_over_action = f"{cycle_one.get_name()} wins!\nPress spacebar to reset!"
                    self._is_game_over = True

        # If cycle_one hits cycle_two display cycle_two wins
        if cycle_one_head.get_position().equals(cycle_two_head.get_position()):
            score2.add_points(1)
            self._game_over_action = f"{cycle_two.get_name()} wins!\nPress spacebar to reset!"
            self._is_game_over = True

        # If cycle_two hits cycle_one display cycle_one wins
        if cycle_two_head.get_position().equals(cycle_one_head.get_position()):
            score1.add_points(1)
            self._game_over_action = f"{cycle_one.get_name()} wins!\nPress spacebar to reset!"
            self._is_game_over = True

        """
        #Don't know what to replace this with
        if score1.get_points() == 0 and score2.get_points() == 0:
            self._game_over_action = f"Game Over!"
            self._is_game_over = True
        """


    def _handle_game_over(self, cast, script):
        """Shows the 'game over' message and turns both cycles white if the game is over.

        Args:
        ---
            cast (Cast): The cast of Actors in the game.
        """

        # position for gameover message
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        position = Point(x, y)


        if self._is_game_over:
            cycle_one = cast.get_first_actor("cycle_one")
            cycle_two = cast.get_first_actor("cycle_two")
            
            # segments for cycle one and two
            segments_one = cycle_one.get_segments()
            segments_two = cycle_two.get_segments()
            
            # Creates gameover message
            game_over = GameOver()
            game_over.set_position(position)
            game_over.set_text(self._game_over_action)
            game_over.set_font_size(50)
            cast.add_actor("messages", game_over)

            # Changes color of cycles to white after the game finishes 
            for segment in segments_one:
                segment.set_color(constants.WHITE)

            for segment in segments_two:
                segment.set_color(constants.WHITE)

            if self._keyboard_service.is_key_down(' '):
                reset = ResetGameAction()
                reset.execute(cast, script)
                self._is_game_over = False
                self._game_over_action = ""
                cast.remove_actor("messages", game_over)
                
                

            
