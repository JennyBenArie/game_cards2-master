from codeRon.Deck_Of_Cards import DeckOfCards
from Player_class import Player


class CardGame:
    def __init__(self, playername1, playername2, num_cards1, num_cards2):
        '''this method gets the number of the cards for each player and his name. then it start the game. '''
        self.player1 = Player(playername1, num_cards1)
        self.player2 = Player(playername2, num_cards2)
        self.deck = DeckOfCards()
        self.__new_game()

    def __repr__(self):
        return f"{self.player1}, {self.player2}, {self.deck}"

    def __new_game(self):
        '''this method is private. it stars a new game, shuffle the cards and give each player his cards. '''
        self.deck.cards_shuffle()
        print(self.deck)
        self.player1.set_hand()
        self.player2.set_hand()


    def get_winner(self):
        '''this method gives the winner of the game, based on the number of his cards.'''
        if self.player1.num_of_cards>self.player2.num_of_cards:
            return f"{self.player1.player_name}, is the winner!"
        elif self.player2.num_of_cards>self.player1.num_of_cards:
            return f"{self.player2.player_name}, is the winner!"
        else:
            return None




