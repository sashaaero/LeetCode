class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() == 0)
            return 0;
        int length = 1;
        int check = nums[0];
        for(int i=1;i<nums.size();i++)
        {
            if(check != nums[i])
            {
                nums[length] = nums[i];
                check = nums[i];
                length++;
            }
            
        }
        return length;
    }
};