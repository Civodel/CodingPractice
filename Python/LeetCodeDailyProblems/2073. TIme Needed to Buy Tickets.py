from typing import List

"""
There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.

You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].

Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.

Return the time taken for the person at position k (0-indexed) to finish buying tickets.
"""
"""class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0

        for i, x in enumerate(tickets):
            breakpoint()
            if i <= k:
                total += min(tickets[i], tickets[k])
            else:
                total += min(tickets[i], tickets[k] - 1)

        return total
"""

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_to_buy =0

        if k+1 <= len(tickets):
            if k+1 == len(tickets):
                time_to_buy = len(tickets)*(k)
            elif tickets[k] == 1:
                return k+1
            else:
                while tickets[k]>0:
                    for ticket in range(len(tickets)):
                        if tickets[ticket]>0 :
                            time_to_buy = time_to_buy + 1
                            tickets[ticket] = tickets[ticket]-1
                        else:
                            tickets[ticket]
        return time_to_buy



if __name__ == "__main__":
    tickets=[1,3,2]
    k=2
    print(Solution().timeRequiredToBuy(tickets, k))







