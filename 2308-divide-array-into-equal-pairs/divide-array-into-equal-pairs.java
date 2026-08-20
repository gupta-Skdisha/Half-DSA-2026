class Solution {
    public boolean divideArray(int[] nums) {
        HashMap<Integer,Integer>map=new HashMap<>();
        for(int num:nums){
            map.put(num,map.getOrDefault(num,0)+1);
        }
        for(int freq:map.values()){
            if(freq % 2 !=0){
                return false;
            }
        }
        return true;
    }
}