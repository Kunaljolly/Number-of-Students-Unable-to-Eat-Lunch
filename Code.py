class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import deque
        students = deque(students)
        sandwiches = deque(sandwiches)
        while sandwiches:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                
            else:
                students.rotate(-1)
            if not sandwiches or students.count(sandwiches[0]) == 0:
                break
        return len(students)
