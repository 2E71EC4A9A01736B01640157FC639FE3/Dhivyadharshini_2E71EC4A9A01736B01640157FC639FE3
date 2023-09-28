# Define the base class player
class player:
  def play(self):
      print("The player is playing cricket.") 

# Define the derived class Batsman
class Batsmanplayer:
    def play(self):
      print("The batsman is batting.")

# Define the derivedclass Bowler
class Bowler(player):
    def play(self):
        print("The bowler is bowling.")

batsman = Batsmanplayer()
bowler =  Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()