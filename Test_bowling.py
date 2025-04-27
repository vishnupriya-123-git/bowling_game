import unittest
from .Bowling import BowlingGame

class TestBowlingGame(unittest.TestCase):
    """Unit tests for the BowlingGame class."""
    def setUp(self):
        self.game = BowlingGame()

    def roll_total(self, n, pins):
        """
        This method is used to simulate multiple rolls in a game.
        It rolls the ball `n` times, each time knocking down `pins` pins.
            n: The number of rolls.
            pins: The number of pins knocked down in each roll.
        """
        rolls= [pins] * n
        for roll in rolls:
            self.game.roll(roll)

    def test_gutter_game(self):
        """Tests a game with all gutter balls (score should be 0)."""
        self.roll_total(20, 0)
        self.assertEqual(self.game.score(), 0)

    def test_all_ones(self):
        self.roll_total(20, 1)
        self.assertEqual(self.game.score(), 20)

    def test_spare(self):
        self.game.roll(5)
        self.game.roll(5)  # Spare
        self.game.roll(3)
        self.roll_total(17, 0)
        self.assertEqual(self.game.score(), 16)

    def test_one_strike(self):
        self.game.roll(10)  # Strike
        self.game.roll(3)
        self.game.roll(4)
        self.roll_total(16, 0)
        self.assertEqual(self.game.score(), 24)

    def test_perfect_game(self):
        self.roll_total(12, 10)
        self.assertEqual(self.game.score(), 300)

    def test_sample_game(self):
        rolls = [1, 4, 4, 5, 6, 4, 5, 5, 10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6]
        for pins in rolls:
            self.game.roll(pins)
        self.assertEqual(self.game.score(), 133)

    def test_invalid_pins(self):
        with self.assertRaises(ValueError):
            self.game.roll(11)
        with self.assertRaises(ValueError):
            self.game.roll(-1)

    def test_too_many_rolls(self):
        self.roll_total(21, 0)  
        with self.assertRaises(ValueError):
            self.game.roll(0)  
    def test_spare_on_last_frame(self):
        self.roll_total(18, 0)
        self.game.roll(5)
        self.game.roll(5)  # Spare in the 10th
        self.game.roll(5)  # Bonus roll
        self.assertEqual(self.game.score(), 15)

    def test_strike_on_last_frame(self):
        self.roll_total(18, 0)
        self.game.roll(10)  # Strike in the 10th
        self.game.roll(5)
        self.game.roll(4)
        self.assertEqual(self.game.score(), 19)

    def test_two_strikes_in_last_frame(self):
        self.roll_total(18, 0)
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(10)
        self.assertEqual(self.game.score(), 30)

    def test_strike_and_spare_in_last_frame(self):
        self.roll_total(18, 0)
        self.game.roll(10)
        self.game.roll(2)
        self.game.roll(8)
        self.assertEqual(self.game.score(), 20)

    def test_game_with_strikes_and_spares(self):
        rolls = [1, 4, 4, 5, 6, 4, 5, 5, 10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6]
        for roll in rolls:
            self.game.roll(roll)
        self.assertEqual(self.game.score(), 133)
    
    def test_tenth_frame_strike_then_spare(self):
        self.roll_total(18, 0)
        self.game.roll(10)
        self.game.roll(2)
        self.game.roll(8)
        self.assertEqual(self.game.score(), 20)

    def test_tenth_frame_spare_then_strike(self):
        self.roll_total(18, 0)
        self.game.roll(9)
        self.game.roll(1)
        self.game.roll(10)
        self.assertEqual(self.game.score(), 20)
   
if __name__ == '__main__':
    # Run the test suite
    test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestBowlingGame)
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)

    print("\nSummary of Test Results:")
    print(f"Total Tests Run: {result.testsRun}")
    print(f"Tests Passed: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Tests Failed: {len(result.failures)}")
    print(f"Tests Errored: {len(result.errors)}")
