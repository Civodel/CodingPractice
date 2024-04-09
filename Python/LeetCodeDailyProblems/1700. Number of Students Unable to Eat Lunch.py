from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        if len(sandwiches) == 0:
            studnets_unable_to_eat = len(students)
        while len(sandwiches)>0 and sandwiches[0] in students:

            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            
            else:
                last_student = students.pop(0)
                students.append(last_student)

        studnets_unable_to_eat = len(students)


        return studnets_unable_to_eat


if __name__ == '__main__':
    students = [1,1,1,0,0,1]
    sandwiches = [1,0,0,0,1,1]
    print(Solution().countStudents(students, sandwiches))