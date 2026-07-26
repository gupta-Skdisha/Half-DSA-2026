class Solution {
    public int maxProduct(int n) {
        ArrayList<Integer> digits=new ArrayList<>();

        while(n>0){
            digits.add(n%10);
            n/=10;

        }
        Collections.sort(digits);

        int size=digits.size();

        return digits.get(size-1) * digits.get(size-2); 
 
    }
}