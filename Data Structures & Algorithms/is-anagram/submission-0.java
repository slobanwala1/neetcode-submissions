class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;
        int[] isAna = new int[26];
        char myChar = 'a'; // so for example if its a it will be 97-97 = 0 so isAna[0] will be incremented
        //int value = myChar - 'a';   
        for(int i = 0; i < s.length(); i++) {
            isAna[s.charAt(i)-myChar] = isAna[s.charAt(i)-myChar] + 1;
        }
        for(int i = 0; i < t.length(); i++) {
            isAna[t.charAt(i)-myChar] = isAna[t.charAt(i)-myChar] - 1;
        }
        for (int n : isAna) {
            if (n > 0) {
                return false;
            }
        }
        return true;
    }
}
