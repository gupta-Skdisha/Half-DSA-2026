class Solution {
    public int solve(int[] nums,int i,int j) {
        
        if(i==j){
           return nums[i];
        }

        int left=nums[i] - solve(nums,i+1,j);
        int right=nums[j]-solve(nums,i,j-1);

        return Math.max(left,right);
    }

     public boolean predictTheWinner(int[] nums) {
        return solve(nums, 0, nums.length - 1) >= 0;
    }
    }