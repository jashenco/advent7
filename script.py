# Set of hands being played with bid value
hands_set = [
                [['3', '2', 'T', '3', 'K'], 765],
                [['T', '5', '5', 'J', '5'], 684],
                [['K', 'K', '6', '7', '7'], 28],
                [['K', 'T', 'J', 'J', 'T'], 220],
                [['Q', 'Q', 'Q', 'J', 'A'], 483]
            ]

# make cards into counted dictionary
def makeCardsDict(cards):
    cards_dict = {}
    for card in cards:
        if card in cards_dict:
            cards_dict[card] += 1
        else:
            cards_dict[card] = 1

    return cards_dict

def isFiveOfAKind(hand):
    cards_dict = makeCardsDict(hand)
    # if only one entry, it has to be 5 of the same cards
    if len(cards_dict) == 1:
        return True
    else:
        return False

def isFourOfAKind(hand):
    cards_dict = makeCardsDict(hand)
    if len(cards_dict) == 2:
        # if first or second entry is 4, return true
        if (cards_dict[list(cards_dict.keys())[0]] == 4) | (cards_dict[list(cards_dict.keys())[1]] == 4):
            return True
    return False

def isFullHouse(hand):
    cards_dict = makeCardsDict(hand)
    if len(cards_dict) == 2: # max can only be 2 different type of cards
        # if entry 1 or 2 has 3 occurences, it has to be a full house
        if (cards_dict[list(cards_dict.keys())[0]] == 3) | (cards_dict[list(cards_dict.keys())[1]] == 3):
            return True
    return False

def isThreeOfAKind(hand):
    cards_dict = makeCardsDict(hand)

    if len(cards_dict) == 3: # Can only happen with 3 different types of cards, otherwise it would be 4of a kind or 5 of a kind
        if (cards_dict[list(cards_dict.keys())[0]] == 3) | (cards_dict[list(cards_dict.keys())[1]] == 3) | (cards_dict[list(cards_dict.keys())[2]] == 3):
            return True
    return False

def isTwoPair(hand):
    cards_dict = makeCardsDict(hand)
    if len(cards_dict) == 3:
        if ((cards_dict[list(cards_dict.keys())[0]] == 2) & (cards_dict[list(cards_dict.keys())[1]] == 2)) | ((cards_dict[list(cards_dict.keys())[0]] == 2) & (cards_dict[list(cards_dict.keys())[2]] == 2)) | ((cards_dict[list(cards_dict.keys())[1]] == 2) & (cards_dict[list(cards_dict.keys())[2]] == 2)):
            return True
    return False

def isOnePair(hand):
    cards_dict = makeCardsDict(hand)
    if len(cards_dict) == 4: # 4 different types, so one is double hence one pair is only possibility
        return True
    return False

def sort_entries(entries):
    # Define the card values
    values = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
        "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14
    }

    # Sort entries based on their second element first (already checked rank)
    entries.sort(key=lambda x: x[2])

    i = 0
    while i < len(entries) - 1:
        if entries[i][2] == entries[i+1][2]: # Same rank
            for j in range(len(entries[i][0])): # Loop through the cards
                if values[entries[i][0][j]] < values[entries[i+1][0][j]]: # swap the entries if the second one has a higher card value
                    entries[i], entries[i+1] = entries[i+1], entries[i]
                    break
                elif values[entries[i][0][j]] > values[entries[i+1][0][j]]:
                    break
            i += 1
        else:
            i += 1

    return entries

# Main program
def main():
    total_winnings = 0

    # Set a value for what happened
    # Five of a kind = 1
    # Four of a kind = 2
    # Full house = 3
    # Three of a kind = 4
    # Two pair = 5
    # One pair = 6
    # Nothing = 7

    for entry in hands_set:
        if isFiveOfAKind(entry[0]):
            entry.append(1)

        elif isFourOfAKind(entry[0]):
            entry.append(2)
            
        elif isFullHouse(entry[0]):
            entry.append(3)
            
        elif isThreeOfAKind(entry[0]):
            entry.append(4)
            
        elif isTwoPair(entry[0]):
            entry.append(5)
            
        elif isOnePair(entry[0]):
            entry.append(6)
            
        else:
            entry.append(7)

    sorted_list = (sort_entries(hands_set))
    reversed_sorted_list = list(reversed(sorted_list)) # as then we can count up with from index as multiplier

    for entry in reversed_sorted_list:
        total_winnings += (entry[1] * (reversed_sorted_list.index(entry) + 1))

    print(total_winnings)

main()