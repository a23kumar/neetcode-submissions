from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #[a, b]
        # means that you must take 'b' before 'a'\
        # You just need to meet numCourses
        # if [0, 0] it would be false because it is a cycle. 

        conns = defaultdict(list)
        visit_set = set()
        # Step #1: Create the hashmap with all presequisites of course
        for course, prereq in (prerequisites):
            conns[course].append(prereq)
        def dfs(course):
            if course in visit_set:
                return False
            if conns[course] == []:
                return True

            visit_set.add(course)
            for pre in conns[course]:
                if not dfs(pre): return False

            visit_set.remove(course)
            conns[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        return True


