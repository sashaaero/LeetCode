# LeetCode
Repository that contains [leetcode.com](leetcode.com) solutions to the problems in different programming languages.

## How to contribute
If you want to make a contribution to this project, you can wo to the [leetcode.com](leetcode.com) website and look for a problem that isn't already in this repository.

Make a solution to that problem, then copy that solution and the URL, the result times and place and add it tho a new file in the repo with the next filename format.

`leet_{problem_number}.{language}`

## Example:

### file name: 

`leet_1046.py`

### file content:

```
# https://leetcode.com/problems/last-stone-weight/submissions/
# Runtime: 36 ms, faster than 83.65% of Python3 online submissions for Last Stone Weight.

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) >= 2:
            stones = sorted(stones)

            num_stones = len(stones)

            heaviest_1 = stones[num_stones - 1]
            heaviest_2 = stones[num_stones - 2]

            if heaviest_2 != heaviest_1:
                result_stone = heaviest_1 - heaviest_2

                stones.pop()
                stones.pop()

                stones.append(result_stone)
            else:
                stones.pop()
                stones.pop()

        if stones:
            return stones[0]
        else:
            return 0
```




