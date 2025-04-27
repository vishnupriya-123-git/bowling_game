# Bowling Game Score Calculator
import pdb
class BowlingGame:
    def __init__(self):
        self.rolls = []
        self.frames = 10

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Pins should be between 0 and 10")
        if len(self.rolls) >= 21:
            raise ValueError("rolls are not allowed. The game is over")
        
        self.rolls.append(pins)
        print(f"Roll {len(self.rolls)}: {pins} pins")
  
    def score(self):
        """total score for the game"""
        if len(self.rolls) < 12 or len(self.rolls) > 21:
            raise ValueError("Invalid number of rolls")
        
        total_score = 0
        roll_index = 0
        for frame in range(self.frames):
            if roll_index >= len(self.rolls):
                break
            if self.strike(roll_index):
                if roll_index + 2 >= len(self.rolls):
                    raise ValueError("Incomplete strike bonus")
                total_score += 10 + self.strike_bonus(roll_index)
                print(f"Frame {frame + 1} :{total_score}")
                roll_index += 1
            elif self.spare(roll_index):
                if roll_index + 2 >= len(self.rolls):
                    raise ValueError("Incomplete spare bonus")
                total_score += 10 + self.spare_bonus(roll_index)
                print(f"Frame {frame + 1}: {total_score}")
                roll_index += 2
            else:
                if roll_index + 1 >= len(self.rolls):
                    raise ValueError("Incomplete frame")
                total_score += self.frame_score(roll_index)
                roll_index += 2
        return total_score

    def strike(self, roll_index):
        return roll_index < len(self.rolls) and self.rolls[roll_index] == 10
    
    def spare(self, roll_index):
        return roll_index + 1 < len(self.rolls) and \
               self.rolls[roll_index] + self.rolls[roll_index + 1] == 10
        
    def frame_score(self, roll_index):
        if roll_index + 1 >= len(self.rolls):
            raise ValueError("Incomplete frame")
        return self.rolls[roll_index] + self.rolls[roll_index + 1]
       
    def strike_bonus(self, roll_index):
        if roll_index + 2 >= len(self.rolls):
            raise ValueError("Incomplete strike bonus")
        return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
    
    def spare_bonus(self, roll_index):
        if roll_index + 2 >= len(self.rolls):
            raise ValueError("Incomplete spare bonus")
        return self.rolls[roll_index + 2]
   
if __name__ == "__main__":
    game = BowlingGame()
    rolls = [1, 4, 4, 5, 6, 4, 5, 5, 10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6]
    
    for pins in rolls:
        game.roll(pins)
    print("Final Score:", game.score())  
    print("Total Rolls:", len(game.rolls))
    print("Rolls:", game.rolls)  
    print("Total Score:", game.score()) 
    print("Total Frames:", game.frames) 
    print("Total Strikes:", sum(1 for roll in game.rolls if roll == 10)) 
    print("Total Spares:", sum(1 for i in range(len(game.rolls) - 1) if game.rolls[i]!=10 and game.rolls[i] + game.rolls[i + 1] == 10))  
    print("Total Misses:", sum(1 for roll in game.rolls if roll == 0)) 
    print("Total Gutter Balls:", sum(1 for roll in game.rolls if roll == 0))  
