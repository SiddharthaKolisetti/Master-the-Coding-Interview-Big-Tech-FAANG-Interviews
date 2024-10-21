class Solution:
    def NetworkTimeDelay(self, times, N, k):
        distances = [float('inf')] * N
        distances[k - 1] = 0
        for _ in range(N - 1):
            count = 0
            for source, target, weight in times:
                if distances[source - 1] + weight < distances[target - 1]:
                    distances[target - 1] = distances[source - 1] + weight
                    count += 1
            if count == 0:
                break
        ans = max(distances)
        return -1 if ans == float('inf') else ans
