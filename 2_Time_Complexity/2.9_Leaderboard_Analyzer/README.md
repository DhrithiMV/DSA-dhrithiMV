# Leaderboard Analyzer
**Topic:** Time & Space Complexity

**Type:** Home Challenge

Statement: 

 You are given scores of N students in an exam. Write a program to: 

Find the highest score. 

Compute the average score. 

Print how many students scored above average. 

Print the rank list in descending order. 

Constraints: 

 1 ≤ N ≤ 1000 

 0 ≤ score ≤ 100 

Complexity Expectations: 

Highest score → O(n) 

Average → O(n) 

Count above average → O(n) 

Rank list → O(n²) (bubble sort) OR O(n log n) (built-in sort) 

Test Cases: 

Input: N=5, Scores=[50,70,90,60,80] 

 Output: 

Highest Score: 90 
Average Score: 70 
Students Above Average: 2 
Rank List: [90, 80, 70, 60, 50] 
  

Input: N=3, Scores=[30,30,30] 

 Output: 

Highest Score: 30 
Average Score: 30 
Students Above Average: 0 
Rank List: [30, 30, 30] 
  

Input: N=4, Scores=[100,40,60,80] 

 Output: 

Highest Score: 100 
Average Score: 70 
Students Above Average: 2 
Rank List: [100, 80, 60, 40] 


### Approach
Describe your approach here...

### Pseudocode
CLASS Leaderboard:
    FUNCTION __init__():
        scores = {}

    FUNCTION addScore(playerId, score):
        IF playerId NOT IN scores:
            scores[playerId] = 0
        scores[playerId] += score

    FUNCTION top(K):
        top_scores = SORT(scores.values(), descending)
        RETURN SUM(first K of top_scores)

    FUNCTION reset(playerId):
        scores.pop(playerId)



### Time Complexity
O(1)

### Space Complexity
O(n)
