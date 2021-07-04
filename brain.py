from random import choice
from data import card_generator


class Brain:

    def __init__(self):
        self.player_cards = []
        self.computer_cards = []
        self.all_cards = card_generator()
        self.player_cards_digits = []
        self.player_cards_symbols = []
        self.computer_cards_digits = []
        self.computer_cards_symbols = []
        self.card_giver()
        self.card_splitter()

    def card_giver(self):
        for i in range(3):
            player_choice = choice(self.all_cards)
            self.player_cards.append(player_choice)
            self.all_cards.remove(player_choice)

            computer_choice = choice(self.all_cards)
            self.computer_cards.append(computer_choice)
            self.all_cards.remove(computer_choice)

    def card_splitter(self):
        self.player_cards_digits = [int(card[:-1]) for card in self.player_cards]
        self.player_cards_symbols = [card[1] for card in self.player_cards]
        self.computer_cards_digits = [int(card[:-1]) for card in self.computer_cards]
        self.computer_cards_symbols = [card[1] for card in self.computer_cards]

    def trial_check(self, digit_list):
        if digit_list[0] == digit_list[1] and digit_list[1] == digit_list[2]:
            return True
        else:
            return False

    def color_check(self, symbol_list):
        if symbol_list[0] == symbol_list[1] and symbol_list[1] == symbol_list[2]:
            return True
        else:
            return False

    def run_check(self, digit_list):
        digit_list.sort()
        if digit_list[1] == digit_list[0] + int(1) and digit_list[2] == digit_list[1] + int(1):
            return True
        else:
            return False

    def color_run_check(self, digit_list, symbol_list):
        if self.color_check(symbol_list) and self.run_check(digit_list):
            return True
        else:
            return False

    def duplicate_check(self, digit_list):
        if digit_list[0] == digit_list[1] or digit_list[1] == digit_list[2] or digit_list[2] == digit_list[1]:
            return True
        else:
            return False

    def top_check(self, player_digit_list, computer_digit_list):
        player_top = 0
        for digit in player_digit_list:
            if digit > player_top:
                player_top = digit

        computer_top = 0
        for digit in computer_digit_list:
            if digit > computer_top:
                computer_top = digit

        if 0 in computer_digit_list and 0 not in player_digit_list:
            return "Computer Wins!"
        elif 0 in player_digit_list and 0 not in computer_digit_list:
            return "Player Wins!"
        if player_top == computer_top:
            if sum(player_digit_list) == sum(computer_digit_list):
                return "Draw"
            elif sum(player_digit_list) > sum(computer_digit_list):
                return "Player has top. Player Wins"
            else:
                return "Computer has top. Computer wins"

        elif computer_top > player_top:
            return "Computer has top. Computer Wins"
        else:
            return "Player has top. Player Wins"

    def win_check(self):
        if self.trial_check(self.player_cards_digits) and not self.trial_check(self.computer_cards_digits):
            return "Player wins with trial"
        elif self.trial_check(self.computer_cards_digits) and not self.trial_check(self.player_cards_digits):
            return "Computer wins with trial"
        elif self.color_run_check(self.player_cards_digits,
                                  self.player_cards_symbols) and not self.color_check(self.computer_cards_digits,
                                                                                      self.computer_cards_symbols):
            return "Player wins with color run"
        elif not self.color_run_check(self.player_cards_digits,
                                  self.player_cards_symbols) and self.color_run_check(self.computer_cards_digits,
                                                                                      self.computer_cards_symbols):
            return "Computer wins with color run"
        elif self.run_check(self.player_cards_digits) and not self.run_check(self.computer_cards_digits):
            return "Player wins with run"
        elif not self.run_check(self.player_cards_digits) and self.run_check(self.computer_cards_digits):
            return "Computer wins with run"
        elif self.color_check(self.player_cards_symbols) and not self.color_check(self.computer_cards_symbols):
            return "Player wins with color"
        elif not self.color_check(self.player_cards_symbols) and self.color_check(self.computer_cards_symbols):
            return "Computer wins with color"
        elif self.duplicate_check(self.player_cards_digits) and not self.duplicate_check(self.computer_cards_digits):
            return "Player wins with jut"
        elif not self.duplicate_check(self.player_cards_digits) and self.duplicate_check(self.computer_cards_digits):
            return "Computer wins with jut"
        else:
            return self.top_check(self.player_cards_digits, self.computer_cards_digits)