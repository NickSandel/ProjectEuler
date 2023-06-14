# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below).
# But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); 
# if the highest cards tie then the next highest cards are compared, and so on.

# Consider the following five hands dealt to two players:

# Hand		Player 1		Player 2		        Winner
# 1		5H 5C 6S 7S KD		2C 3S 8S 8D TD		    Player 2
# 		Pair of Fives		Pair of Eights		
# 2		5D 8C 9S JS AC		2C 5C 7D 8S QH		    Player 1
# 		Highest card Ace		Highest card Queen		
# 3		2D 9C AS AH AC		3D 6D 7D TD QD		    Player 2
# 		Three Aces		Flush with Diamonds		
# 4		4D 6S 9H QH QC		3D 6D 7H QD QS		    Player 1
# 		Pair of Queens		Pair of Queens		
# 		Highest card Nine		Highest card Seven		
# 5		2H 2D 4C 4D 4S		3C 3D 3S 9S 9D			Player 1
# 		Full House		Full House		
# 		With Three Fours		with Three Threes		


# The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space):
# the first five are Player 1's cards and the last five are Player 2's cards. 
# You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

# How many hands does Player 1 win?

def card_face_value(card_face):
    #2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace
    if card_face == "T":
        return 10
    elif card_face == "J":
        return 11
    elif card_face == "Q":
        return 12
    elif card_face == "K":
        return 13
    elif card_face == "A":
        return 14
    else:
        return int(card_face)

def winning_hand(player_1_cards, player_2_cards):
    player_1_royal_flush = has_royal_flush(player_1_cards)
    player_2_royal_flush = has_royal_flush(player_2_cards)

    if player_1_royal_flush and player_2_royal_flush:
        return 0
    elif player_1_royal_flush:
        return 1
    elif player_2_royal_flush:
        return 2
    
    player_1_straight_flush = has_straight_flush(player_1_cards)
    player_2_straight_flush = has_straight_flush(player_2_cards)

    player_1_card_values_and_counts = card_values_and_counts(player_1_cards)
    player_2_card_values_and_counts = card_values_and_counts(player_2_cards)

    if player_1_straight_flush and player_2_straight_flush:
        return tie_breaker(player_1_card_values_and_counts, player_2_card_values_and_counts, 5)
    elif player_1_straight_flush:
        return 1
    elif player_2_straight_flush:
        return 2

    
    player_1_four_of_a_kind = has_four_of_a_kind(player_1_card_values_and_counts)
    player_2_four_of_a_kind = has_four_of_a_kind(player_2_card_values_and_counts)

    if player_1_four_of_a_kind and player_2_four_of_a_kind:
        return tie_breaker(player_1_card_values_and_counts, player_2_card_values_and_counts, 4)
    elif player_1_four_of_a_kind:
        return 1
    elif player_2_four_of_a_kind:
        return 2
    
    player_1_full_house = has_full_house(player_1_card_values_and_counts)
    player_2_full_house = has_full_house(player_2_card_values_and_counts)

    if player_1_full_house and player_2_full_house:
        return tie_breaker(player_1_card_values_and_counts, player_2_card_values_and_counts, 3)
    elif player_1_full_house:
        return 1
    elif player_2_full_house:
        return 2
    
    player_1_flush = has_flush(player_1_cards)
    player_2_flush = has_flush(player_2_cards)

    if player_1_flush and player_2_flush:
        return tie_breaker(player_1_card_values_and_counts, player_2_card_values_and_counts, 5)
    elif player_1_flush:
        return 1
    elif player_2_flush:
        return 2
    
    player_1_straight = has_straight(player_1_cards)
    player_2_straight = has_straight(player_2_cards)

    if player_1_straight and player_2_straight:
        return tie_breaker(player_1_card_values_and_counts, player_2_card_values_and_counts, 5)
    elif player_1_straight:
        return 1
    elif player_2_straight:
        return 2
    
    player_1_three_of_a_kind = has_three_of_a_kind(player_1_card_values_and_counts)
    player_2_three_of_a_kind = has_three_of_a_kind(player_2_card_values_and_counts)

    if player_1_three_of_a_kind and player_2_three_of_a_kind:
        return tie_breaker(player_1_card_values_and_counts, player_2_card_values_and_counts, 3)
    elif player_1_three_of_a_kind:
        return 1
    elif player_2_three_of_a_kind:
        return 2
    
    player_1_two_pairs = has_two_pairs(player_1_card_values_and_counts)
    player_2_two_pairs = has_two_pairs(player_2_card_values_and_counts)

    if player_1_two_pairs and player_2_two_pairs:
        return tie_breaker(player_1_card_values_and_counts, player_2_card_values_and_counts, 22)
    elif player_1_two_pairs:
        return 1
    elif player_2_two_pairs:
        return 2
    
    player_1_pair = has_one_pair(player_1_card_values_and_counts)
    player_2_pair = has_one_pair(player_2_card_values_and_counts)

    if player_1_pair and player_2_pair:
        return tie_breaker(player_1_card_values_and_counts, player_2_card_values_and_counts, 2)
    elif player_1_pair:
        return 1
    elif player_2_pair:
        return 2
    
    # Highest card should work through this tie breaker
    return tie_breaker(player_1_card_values_and_counts, player_2_card_values_and_counts, 5)
    
def has_royal_flush(cards):
    # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit
    # Return True if the hand has a royal flush
    # Otherwise, return False
    royal_flush = ["T", "J", "Q", "K", "A"]
    card_suits = []
    card_face_values = []
    for card in cards:
        card_suits.append(card[1])
        card_face_values.append(card[0])
    
    # Check if all the cards are the same suit
    if len(set(card_suits)) == 1:
        # Check if all the cards are royal flush cards
        if set(card_face_values) == set(royal_flush):
            return True
    return False

def has_straight_flush(cards):
    # Straight Flush: All cards are consecutive values of same suit
    # Return True if the hand has a straight flush
    # Otherwise, return False
    card_suits = []
    card_face_values = []
    for card in cards:
        card_suits.append(card[1])
        card_face_values.append(card_face_value(card[0]))
    
    # Check if all the cards are the same suit
    if len(set(card_suits)) == 1:
        # Check if all the cards are consecutive
        card_face_values.sort()
        for i in range(len(card_face_values) - 1):
            if card_face_values[i] + 1 != card_face_values[i + 1]:
                return False
        return True
    return False

def card_values_and_counts(cards):
    # Return a dictionary of the card values and their counts
    card_values = []
    for card in cards:
        card_values.append(card_face_value(card[0]))

    card_values_and_counts = {}
    for card in card_values:
        if card in card_values_and_counts:
            card_values_and_counts[card] += 1
        else:
            card_values_and_counts[card] = 1
    return card_values_and_counts

def has_four_of_a_kind(card_values_and_counts):
    # Four of a Kind: Four cards of the same value
    # Return True if the hand has a four of a kind
    # Otherwise, return False
    for card_value in card_values_and_counts:
        if card_values_and_counts[card_value] == 4:
            return True
    return False

def has_three_of_a_kind(card_values_and_counts):
    # Three of a Kind: Three cards of the same value
    # Return True if the hand has a three of a kind
    # Otherwise, return False
    for card_value in card_values_and_counts:
        if card_values_and_counts[card_value] == 3:
            return True
    return False

def has_two_pairs(card_values_and_counts):
    # Two Pairs: Two different pairs
    # Return True if the hand has two pairs
    # Otherwise, return False
    pairs = 0
    for card_value in card_values_and_counts:
        if card_values_and_counts[card_value] == 2:
            pairs += 1
    return pairs == 2

def has_one_pair(card_values_and_counts):
    # One Pair: Two cards of the same value
    # Return True if the hand has one pair
    # Otherwise, return False
    for card_value in card_values_and_counts:
        if card_values_and_counts[card_value] == 2:
            return True
    return False

def has_full_house(card_values_and_counts):
    # Full House: Three of a kind and a pair
    # Return True if the hand has a full house
    # Otherwise, return False
    has_three_of_a_kind = False
    has_pair = False
    for card_value in card_values_and_counts:
        if card_values_and_counts[card_value] == 3:
            has_three_of_a_kind = True
        elif card_values_and_counts[card_value] == 2:
            has_pair = True
    return has_three_of_a_kind and has_pair

def has_flush(cards):
    # Flush: All cards of the same suit
    # Return True if the hand has a flush
    # Otherwise, return False
    card_suits = []
    for card in cards:
        card_suits.append(card[1])
    return len(set(card_suits)) == 1

def has_straight(cards):
    # Straight: All cards are consecutive values
    # Return True if the hand has a straight
    # Otherwise, return False
    card_face_values = []
    for card in cards:
        card_face_values.append(card_face_value(card[0]))
    
    # Check if all the cards are consecutive
    card_face_values.sort()
    for i in range(len(card_face_values) - 1):
        if card_face_values[i] + 1 != card_face_values[i + 1]:
            return False
    return True

def tie_breaker(player_1_card_values_and_counts, player_2_card_values_and_counts, hand_type, player_1_cards = None, player_2_cards = None):
    if hand_type == 4:
        # Check the value of the four of a kind card, there can't be a tie here
        for card_value in player_1_card_values_and_counts:
            if player_1_card_values_and_counts[card_value] == 4:
                player_1_four_of_a_kind_card_value = card_face_value(card_value)
        for card_value in player_2_card_values_and_counts:
            if player_2_card_values_and_counts[card_value] == 4:
                player_2_four_of_a_kind_card_value = card_face_value(card_value)

        if player_1_four_of_a_kind_card_value > player_2_four_of_a_kind_card_value:
            return 1
        elif player_1_four_of_a_kind_card_value < player_2_four_of_a_kind_card_value:
            return 2
        
        # No need for further tie breaking because there are only 4 cards of each value so there can't be a tie from this setup

    if hand_type == 3:
        # Check the value of the three of a kind card, there can't be a tie here
        for card_value in player_1_card_values_and_counts:
            if player_1_card_values_and_counts[card_value] == 3:
                player_1_three_of_a_kind_card_value = card_face_value(card_value)
        for card_value in player_2_card_values_and_counts:
            if player_2_card_values_and_counts[card_value] == 3:
                player_2_three_of_a_kind_card_value = card_face_value(card_value)

        if player_1_three_of_a_kind_card_value > player_2_three_of_a_kind_card_value:
            return 1
        elif player_1_three_of_a_kind_card_value < player_2_three_of_a_kind_card_value:
            return 2
        
        # No need for further tie breaking because there are only 4 cards of each value so there can't be a tie from this setup

    # Flush, straight and high card all have the same tie breaking rules
    if hand_type == 5:
        # Check the value of the highest card, there can can be a tie so iterate until there isn't or there are no more to check
        # Sort both hands by card value
        # Convert the card values to face values
        player_1_card_values = []
        for card_value in player_1_card_values_and_counts:
            player_1_card_values.append(card_face_value(card_value))
        player_1_card_values.sort(reverse = True)
        player_2_card_values = []
        for card_value in player_2_card_values_and_counts:
            player_2_card_values.append(card_face_value(card_value))
        player_2_card_values.sort(reverse = True)

        # Iterate through the card values and compare them
        for i in range(len(player_1_card_values)):
            if player_1_card_values[i] > player_2_card_values[i]:
                return 1
            elif player_1_card_values[i] < player_2_card_values[i]:
                return 2
            
    # When there are 2 pairs check the highest pair
    if hand_type == 22:
        # There can be a tie so then check the next pair which can also be tied. Finally check the final card which can lead to a full tie
        player_1_pairs = []
        player_2_pairs = []
        for card_value in player_1_card_values_and_counts:
            if player_1_card_values_and_counts[card_value] == 2:
                player_1_pairs.append(card_face_value(card_value))
        for card_value in player_2_card_values_and_counts:
            if player_2_card_values_and_counts[card_value] == 2:
                player_2_pairs.append(card_face_value(card_value))

        # Check the highest pair
        if max(player_1_pairs) > max(player_2_pairs):
            return 1
        elif max(player_1_pairs) < max(player_2_pairs):
            return 2
        elif min(player_1_pairs) > min(player_2_pairs):
            return 1
        elif min(player_1_pairs) < min(player_2_pairs):
            return 2
        
        # Check the final card
        player_1_final_card = 0
        player_2_final_card = 0
        for card_value in player_1_card_values_and_counts:
            if player_1_card_values_and_counts[card_value] == 1:
                player_1_final_card = card_face_value(card_value)
        for card_value in player_2_card_values_and_counts:
            if player_2_card_values_and_counts[card_value] == 1:
                player_2_final_card = card_face_value(card_value)

        if player_1_final_card > player_2_final_card:
            return 1
        elif player_1_final_card < player_2_final_card:
            return 2
        else:
            return 0      

            
    # When there is a pair check the highest pair
    if hand_type == 2:
        # There can be a tie so then check the next highest card which can also be tied. Finally check the final card which can lead to a full tie
        # Sort both hands by card value
        # Convert the card values to face values
        for card_value in player_1_card_values_and_counts:
            if player_1_card_values_and_counts[card_value] == 2:
                player_1_pair_card_value = card_face_value(card_value)
        for card_value in player_2_card_values_and_counts:
            if player_2_card_values_and_counts[card_value] == 2:
                player_2_pair_card_value = card_face_value(card_value)

        if player_1_pair_card_value > player_2_pair_card_value:
            return 1
        elif player_1_pair_card_value < player_2_pair_card_value:
            return 2
        
        # When there is a high card check the highest card
        return tie_breaker(player_1_card_values_and_counts, player_2_card_values_and_counts, 5)
            
        
# Royal flush test
player_1_cards = ["TC", "JC", "QC", "KC", "AC"]
player_2_cards = ["2C", "3C", "4C", "5C", "6C"]
print("Royal flush test")
print(winning_hand(player_1_cards, player_2_cards))

# Straight flush test
player_1_cards = ["TC", "JC", "QC", "KC", "9C"]
player_2_cards = ["2C", "3C", "4C", "5C", "6C"]
print("Straight flush test")
print(winning_hand(player_1_cards, player_2_cards))

# Four of a kind test
player_1_cards = ["5H", "5C", "5S", "5D", "9C"]
player_2_cards = ["2C", "6H", "6C", "6S", "6D"]
print("Four of a kind test")
print(winning_hand(player_1_cards, player_2_cards))

# Full house test
player_1_cards = ["5H", "5C", "7S", "7H", "7D"]
player_2_cards = ["5D", "5S", "8S", "8H", "8D"]
print("Full house test")
print(winning_hand(player_1_cards, player_2_cards))

# Flush test
player_1_cards = ["5H", "2H", "4H", "JH", "7H"]
player_2_cards = ["5D", "6D", "7D", "8D", "TD"]
print("Flush test")
print(winning_hand(player_1_cards, player_2_cards))

# Straight test
player_1_cards = ["5H", "6C", "7S", "8H", "9D"]
player_2_cards = ["5D", "6S", "7S", "8H", "4D"]
print("Straight test")
print(winning_hand(player_1_cards, player_2_cards))

# Three of a kind test
player_1_cards = ["5H", "5C", "5S", "8H", "9D"]
player_2_cards = ["2D", "2S", "2C", "JH", "KD"]
print("Three of a kind test")
print(winning_hand(player_1_cards, player_2_cards))

# Two pair test
player_1_cards = ["5H", "5C", "7S", "7H", "9D"]
player_2_cards = ["5D", "5S", "8S", "8H", "9D"]
print("Two pair test")
print(winning_hand(player_1_cards, player_2_cards))

# One pair test
player_1_cards = ["5H", "5C", "7S", "8H", "9D"]
player_2_cards = ["5D", "5S", "8S", "9H", "TD"]
print("One pair test")
print(winning_hand(player_1_cards, player_2_cards))

# High card test
player_1_cards = ["5H", "2C", "7S", "8H", "9D"]
player_2_cards = ["5D", "3S", "8S", "9H", "TD"]
print("High card test")
print(winning_hand(player_1_cards, player_2_cards))

# Read in the poker hands
with open("Fifties\p054_poker.txt") as f:
    hands = f.readlines()

# Remove the newline characters
hands = [hand.strip() for hand in hands]

# Split the hands into player 1 and player 2 hands
player_1_hands = [hand[:14] for hand in hands]
player_2_hands = [hand[15:] for hand in hands]

# Count the number of times player 1 wins
player_1_wins = 0
for i in range(len(player_1_hands)):
    if winning_hand(player_1_hands[i].split(), player_2_hands[i].split()) == 1:
        player_1_wins += 1

print("The number of times player 1 wins is: " + str(player_1_wins))