cards = list(range(1, 14))
card_types = ["♠", "♣", "♥", "♦"]

all_cards = []


def card_generator():
    """
    Function that generates all possible cards in a deck.
    :return:
    """
    for symbol in card_types:
        for card in cards:
            card1 = f"{card}{symbol}"
            all_cards.append(card1)
    return all_cards


