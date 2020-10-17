import java.io.*; 
import java.util.*; 
  
public class GFG { 
    final static int MAX_CHAR = 256
  
    // Function to find if two strings are equal 
    static boolean isCountZero(int[] count) 
    { 
        for (int i = 0; i < MAX_CHAR; i++) 
            if (count[i] != 0) 
                return false; 
        return true; 
    } 
  
    static int countAnagrams(String text, String word) 
    { 
        int N = text.length(); 
        int n = word.length(); 
  
        // Check for first window. The idea is to 
        // use single count array to match counts 
        int[] count = new int[MAX_CHAR]; 
        for (int i = 0; i < n; i++) 
            count[word.charAt(i)]++; 
        for (int i = 0; i < n; i++) 
            count[text.charAt(i)]--; 
  
        // If first window itself is anagram 
        int res = 0; 
        if (isCountZero(count)) 
            res++; 
  
        for (int i = n; i < N; i++) { 
  
            // Add last character of current 
            // window 
            count[text.charAt(i)]--; 
  
            // Remove first character of previous 
            // window. 
            count[text.charAt(i - n)]++; 
  
            // If count array is 0, we found an 
            // anagram. 
            if (isCountZero(count)) 
                res++; 
        } 
        return res; 
    } 
  
    // Driver code 
    public static void main(String args[]) 
    { Scanner scan = new Scanner(System.in);
        int t= scan.nextInt();
        while(t--)

        {String text= scan.nextLine();

            int n=scan.nextInt();
            // String text = "doyouknowvegetahasatail"; 

        for(int i=0;i<)
        String word = "kylie"; 
        System.out.print(countAnagrams(text, word));}
    } 
}