'''You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.'''
from typing import List


class Solution:



    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inter=[]

        if not intervals:
            return [newInterval]

        for interval in intervals:
            inter_count=0
            dummy_inter=newInterval

            if newInterval[0]>interval[1] and newInterval[1]>interval[1]:
                inter.append(interval)
            elif newInterval[0]<interval[0] and newInterval[1]<interval[0]:
                inter.append(interval)

            elif interval[0]<newInterval[0] and newInterval[1]<interval[1]:
                inter.append(interval)

            else:

                if interval[0] < newInterval[0]:
                    newInterval[0] = interval[0]
                    inter.append(newInterval)
                elif newInterval[1]<interval[1]:
                    newInterval[1] = interval[1]

                elif newInterval[0] <= interval[1] and newInterval[1] <=interval[1]:
                    inter.append(newInterval)

        return  inter

if __name__ == '__main__':
    list1 = [[1,3],[6,9]]
    newInterval =[2,5]


    print(Solution().insert(list1, newInterval))