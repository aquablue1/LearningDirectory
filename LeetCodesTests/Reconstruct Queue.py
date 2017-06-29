
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        def findIndex(list, value, count):
            tallerCount = 0
            for l in list:
                if l[0] > value and tallerCount < count:
                    tallerCount += 1
                elif l[0] > value and tallerCount >= count:
                    return list.index(l)
                else:
                    continue
            return 0

        if len(people) < 1:
            return []
        retVal = []
        people.sort(key=lambda x: x[1])
        print(people)
        ret = []
        ret.append(people[0])
        for p in people[1:]:
            ret.insert(findIndex(ret, p[0], p[1]), p)

        print(ret)


if __name__ == 'main':
    sol = Solution()
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    sol.reconstructQueue(people)