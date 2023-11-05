"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    if card == 'K' or 'J' or 'Q':
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    elif value_of_card(card_one) < value_of_card(card_two):
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one, card_two):
    res = int(card_one) + int(card_two)
    if res + 11 > 21:
        return 1
    else:
        return 11


def is_blackjack(card_one, card_two):
    if ('A' in card_one or card_two) and (card_one or card_two in ('K', 'Q', 'J')):
        return True
    else:
        if card_one + card_two == 21:
            return True
        return False


def can_split_pairs(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    return False


def can_double_down(card_one, card_two):
    if value_of_card(card_one) + value_of_card(card_two) in (9, 10, 11):
        return True
    return False

