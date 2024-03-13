class CalcStren:
  def calcSuit(self, card1, card2, flop1, flop2, flop3, turn, river):
    self.Card1 = card1
    self.Card2 = card2
    self.flop1 = flop1
    self.flop2 = flop2
    self.flop3 = flop3
    self.turn = turn
    self.river =river
    
    suits = {"Heart": 0, "Spade": 0, "Club": 0, "Diamond": 0}
    
    for card in [self.Card1, self.Card2, self.flop1, self.flop2, self.flop3, self.turn, self.river]:
      suits["Heart"] += card.count("Heart")

    # Check spades
    for card in [self.Card1, self.Card2, self.flop1, self.flop2, self.flop3, self.turn, self.river]:
      suits["Spade"] += card.count("Spade")

    # Check clubs
    for card in [self.Card1, self.Card2, self.flop1, self.flop2, self.flop3, self.turn, self.river]:
      suits["Club"] += card.count("Club")

    # Check diamonds
    for card in [self.Card1, self.Card2, self.flop1, self.flop2, self.flop3, self.turn, self.river]:
      suits["Diamond"] += card.count("Diamond")
      
    return suits
