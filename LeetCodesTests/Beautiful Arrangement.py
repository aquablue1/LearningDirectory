import collections

class Solution(object):
    def countArrangement(self, N):
        def rain(valid, counts, ind, N, used):
            if ind > N: return 1  # end
            s = ''.join(used)  # remainder string to be hashed
            if s in counts[ind]: return counts[ind][s]  # if in memo, return memoized value
            cnt = 0
            for i in valid[ind]:
                _i = i - 1
                if used[_i] == '0': continue
                used[_i] = '0'  # backtracking
                cnt += rain(valid, counts, ind + 1, N, used)
                used[_i] = '1'
            counts[ind][s] = cnt  # memoize
            return cnt

        if not N: return 0
        valid, counts = collections.defaultdict(list), collections.defaultdict(dict)
        # generating valid entries for each position
        for i in range(1, N + 1):
            for n in range(1, N + 1):
                if i % n == 0 or n % i == 0: valid[i].append(n)
        return rain(valid, counts, 1, N, ['1' for _ in range(N)])


if __name__ == '__main__':
    sol = Solution()
    arr = 2
    print(sol.countArrangement(arr))