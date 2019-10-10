// https://leetcode.com/problems/two-sum/submissions/
// Runtime: 112 ms, faster than 37.73% of JavaScript online submissions for Two Sum.

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for(let i = 0; i < nums.length; i++) {
         for(let y = i + 1; y < nums.length; y++) {
            if(nums[i] + nums[y] === target) {
                return [i, y];
            }
        }
    }
};