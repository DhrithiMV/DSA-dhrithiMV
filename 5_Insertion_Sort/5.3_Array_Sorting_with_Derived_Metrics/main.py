# Array Sorting with Derived Metrics
# Topic: Insertion Sort
# Type: Home Challenge
class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        for i in range(1, len(seats)):
            key = seats[i]
            j = i - 1
            while j >= 0 and seats[j] > key:
                seats[j + 1] = seats[j]
                j -= 1
            seats[j + 1] = key
        for i in range(1, len(students)):
            key = students[i]
            j = i - 1
            while j >= 0 and students[j] > key:
                students[j + 1] = students[j]
                j -= 1
            students[j + 1] = key
        moves = 0
        for i in range(len(seats)):
            moves += abs(seats[i] - students[i])
        return moves
# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.minMovesToSeat([3,1,5], [2,7,4]))  # Output: 4
