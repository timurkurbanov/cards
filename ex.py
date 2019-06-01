def select_cards(possible_cards, hand):
#no more than 3 cards.
    if len(possible_cards) <= 3:
        return possible_cards
#start the loop
    while len(hand) < 3:
        for current_card in possible_cards:
            print("Do you want to pick up {}?".format(current_card))
            answer = input()
            if answer.lower() == 'y':
                hand.append(current_card)
                possible_cards.remove(current_card)
            if len(hand) == 3:
                return hand


available_cards = ['queen of spades', '2 of clubs', '3 of diamonds', 'jack of spades', 'queen of hearts']

new_hand = select_cards(available_cards, [])

display_hand = "\n".join(new_hand)

print("Your new hand is: \n{}".format(display_hand))