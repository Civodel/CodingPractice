
'''
You are given an integer array deck. There is a deck of cards where every card has a unique integer. The integer on the ith card is deck[i].

You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.

You will do the following steps repeatedly until all cards are revealed:

Take the top card of the deck, reveal it, and take it out of the deck.
If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.
If there are still unrevealed cards, go back to step 1. Otherwise, stop.
Return an ordering of the deck that would reveal the cards in increasing order.

Note that the first entry in the answer is considered to be the top of the deck.
'''
from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        deck.sort()
        revealed_cards=[0]*len(deck)
        pair=2
        impair =1
        while deck:
            if revealed_cards[0] == 0:
                revealed_cards[0]=(deck.pop(0))

            if pair<len(revealed_cards):
                revealed_cards[pair]=(deck.pop(0))
                pair = pair + 2

            elif impair<len(revealed_cards):
                if deck and revealed_cards[len(revealed_cards)-1] != 0:
                    deck.append(deck.pop(0))
                    revealed_cards[impair] = (deck.pop(0))

                if deck and revealed_cards[len(revealed_cards)-1] == 0:
                    revealed_cards[impair] = (deck.pop(0))
                    if deck:
                        deck.append(deck.pop(0))

                impair = impair + 2

        return revealed_cards


if __name__ == '__main__':
    deck=[1,2,3,4,5,6,7,8,9]
    s = Solution()
    print(s.deckRevealedIncreasing(deck))
