class Solution {
    public int minimumDeletions(int[] nums) {
        int minIndex=0;
        int maxIndex=0;
        int n=nums.length;


        for(int i=1;i<n;i++){
            if(nums[i]<nums[minIndex]){
                minIndex=i;
            }

            if(nums[i]>nums[maxIndex]){
                maxIndex=i;
            }

        }

        int left=Math.min(minIndex,maxIndex);
        int right=Math.max(minIndex,maxIndex);


        int removefromFront=right + 1;
        int removefromback=n- left;
        int fromBothEnds=(left+1)+(n-right);


        return Math.min(removefromFront,Math.min(removefromback,fromBothEnds));

    }
}