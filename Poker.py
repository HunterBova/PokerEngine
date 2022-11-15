# Hunter Bova
# Poker Program
import random

class Poker:
    #private methods (Not inherited)
    # def __init__(self,deck):
    #     self._deck = deck

    def __init__(self):
        self._deck = self._generateDeck()
        self._hands = []
        self._hand = self._getHand()
        self._hands.append(self._hand)           
    #protected methods (Inherited)
    def _generateDeck(self):
        suitsList = ["Spade","Club","Heart","Diamond"]
        pokerDeck = []
        faceValue = 0
        suitIndex = 0
        for i in range(52):
            faceValue = faceValue + 1
            if(faceValue == 14):
                faceValue = 1
                suitIndex = suitIndex + 1

            if(faceValue == 11):
                pokerDeck.append("Jack " + suitsList[suitIndex])
            elif(faceValue == 12):
                pokerDeck.append("Queen " + suitsList[suitIndex])
            elif(faceValue == 13):
                pokerDeck.append("King " + suitsList[suitIndex])
            elif(faceValue == 1):
                pokerDeck.append("Ace " + suitsList[suitIndex])
            else:
                pokerDeck.append(str(faceValue) + " " + suitsList[suitIndex])

        return pokerDeck
    
    def _buildListSTring(self,deck):
        deckString = ""
        for i in deck:
            card = i.split()
            deckString = deckString + " " + (card[0]+" of "+card[1]+"s\n")
        return deckString

    def _cardString(self,card):
        cardString = ""
        i = card.split()
        cardString = i[0] + " of " + i[1] + "s"
        return cardString

    def _getCard(self):
        card = random.choice(self._deck)
        self._deck.remove(card)
        return card

    def _getHand(self):
        tmpHand = []
        for i in range(5):
            tmpHand.append(self._getCard())
        return tmpHand

    def _convertCard(self,card):
        i = card.split()
        if (i[0] == "Ace"):
            i[0] = "14"
        elif (i[0] == "King"):
            i[0] = "13"
        elif (i[0] == "Queen"):
            i[0] = "12"
        elif (i[0] == "Jack"):
            i[0] = "11"
        return i

    def _getBiggerCard(self,i,j):
        card1 = i
        card2 = j
        if (int(self._convertCard(card1)[0]) > int(self._convertCard(card2)[0])):
            return card1
        else:
            return card2

    def _getSmallerCard(self,i,j):
        card1 = i
        card2 = j
        if (int(self._convertCard(card1)[0]) < int(self._convertCard(card2)[0])):
            return card1
        else:
            return card2
        
    def _getHighestCard(self,hand):
        runningHighest = hand[0]
        for i in hand:
            runningHighest = self._getBiggerCard(runningHighest,i)
        return runningHighest

    def _getLowestCard(self,hand):
        runningLowest = hand[0]
        for i in hand:
            runningLowest = self._getSmallerCard(runningLowest,i)
        return runningLowest

    def _cardEqualTo(self,i,j):
        if (self._convertCard(i)[0] == self._convertCard(j)[0]):
            return True
        else:
            return False

    def _removePair(self,hand):
        for i in range(len(hand)):
            for j in range(i+1,len(hand),1):
                if(self._cardEqualTo(hand[i],hand[j])):
                    card1 = hand[i]
                    card2 = hand[j]
                    hand.remove(hand[j])
                    hand.remove(hand[i])
                    return self._cardString(card1) + " / " + self._cardString(card2)
        return ""

    def _listPrint(self,deck):
        return self._buildListSTring(deck)

    def _checkPair(self,hand):
        tmpHand = hand
        removedPair = self._removePair(tmpHand)
        if (removedPair != ""):
            return removedPair
        else:
            return ""

    def _checkTwoPair(self,hand):
        pairs = ""
        if (self._checkPair(hand.copy()) != ""):
            pairs = pairs + self._checkPair(hand)
            if (self._checkPair(hand.copy()) != ""):
                pairs = pairs + " + " +  self._checkPair(hand)
                return pairs
        return ""

    def _checkThreeOfKind(self,deck):
        runningTotal = 0
        threeString = ""
        for i in range(len(deck)):
            runningTotal = 0
            for j in range(i+1,len(deck),1):
                if(self._cardEqualTo(deck[i],deck[j])):
                    runningTotal += 1
                    if(runningTotal == 1):
                        threeString = self._cardString(deck[j])
                    else:
                        return threeString + " / " + self._cardString(deck[i]) + " / " + self._cardString(deck[j])
            
        return ""

    def _checkStraight(self,hand):
        straightString = ""
        lowestCard = self._getLowestCard(hand)
        highestCard = self._getHighestCard(hand)
        if (self._convertCard(highestCard)[0] == "14"):
            straightString = straightString + self._cardString(highestCard)
        else:
            straightString = straightString + self._cardString(lowestCard)
        c = 0
        for i in range(len(hand)):
            if (int(self._convertCard(highestCard)[0]) == 14 and int(self._convertCard(hand[i])[0]) == 2):
                straightString = straightString + " / " + self._cardString(hand[i])
                lowestCard = hand[i]
                i = 0
                c += 1
            elif (int(self._convertCard(hand[i])[0]) == int(self._convertCard(lowestCard)[0]) + 1):
                straightString = straightString + " / " + self._cardString(hand[i])
                lowestCard = hand[i]
                print(straightString)
                i = 0
                c += 1
            else:
                lowestCard = hand[i]
                straightString = ""
                straightString = straightString + self._cardString(hand[i])
                i = 0
                c = 0
            if (c == 4):
                return straightString

        return ""

    def _checkFlush(self, hand):
        c = 0
        end = hand[len(hand) - 1]
        flushString = self._cardString(hand[4])
        for i in range(len(hand) - 1):
            if (self._convertCard(hand[i])[1] == self._convertCard(end)[1]):
                c += 1
                flushString = flushString + " / " + self._cardString(hand[i])
            if(c == 4):
                return flushString
        return ""
           
    # Public Methods
    def printHands(self):
        counter = 0
        for i in self._hands:
            counter += 1
            print("Player #" + str(counter) + "'s hand:\n" + self._listPrint(i))

    def getCardCombo(self):
        counter = 0
        cardCombo = ""
        for i in self._hands:
            highestCombo = "High Card: " + self._getHighestCard(i.copy())
            if (self._checkPair(i.copy()) != ""):
                highestCombo = "Pair: " + self._checkPair(i.copy())
            if (self._checkTwoPair(i.copy()) != ""):
                highestCombo = "Two Pair: " + self._checkTwoPair(i.copy())
            if (self._checkThreeOfKind(i.copy()) != ""):
                highestCombo = "Three of a Kind: " + self._checkThreeOfKind(i.copy())
            if (self._checkStraight(i.copy()) != ""):     
                highestCombo = "Straight: " + self._checkStraight(i.copy())
            if (self._checkFlush(i.copy()) != ""):
                highestCombo = "Flush: " + self._checkFlush(i.copy())

            counter = counter + 1
            cardCombo = cardCombo + "Player " + str(counter) + " highest combo: " + highestCombo + "\n"

        return cardCombo

#Child class of Poker
#To Display a 2 player game
class Poker2(Poker):
    def __init__(self):
        self._deck = self._generateDeck()
        self._hands = []

        self._hand = self._getHand()
        self._hands.append(self._hand)
        self._hand2 = self._getHand()
        self._hands.append(self._hand2)

#Child class of Poker
#To Display a 3 Player Game
class Poker3(Poker):
    def __init__(self):
        self._deck = self._generateDeck()
        self._hands = []

        self._hand = self._getHand()
        self._hands.append(self._hand)
        self._hand2 = self._getHand()
        self._hands.append(self._hand2)
        self._hand3 = self._getHand()
        self._hands.append(self._hand3)

#Child class of Poker
#To Display a 4 Player Game
class Poker4(Poker):
    def __init__(self):
        self._deck = self._generateDeck()
        self._hands = []

        self._hand = self._getHand()
        self._hands.append(self._hand)
        self._hand2 = self._getHand()
        self._hands.append(self._hand2)
        self._hand3 = self._getHand()
        self._hands.append(self._hand3)
        self._hand4 = self._getHand()
        self._hands.append(self._hand4)