class Solution {
public:
    string reverseWords(string &s) {
        
        int n = s.size();
        reverse(s, 0, n-1);
        reverseEachWord(s, n);
        cleanSpaces(s, n);
        
        return s;
    }
    
    void reverse(string &s, int i, int j)
    {
        while(i < j)
        {
            swap(s[i++], s[j--]);
        }
    }
    
    void reverseEachWord(string &s, int n)
    {
        int i = 0, j = 0;
        
        while(i < n)
        {
            while(i < j) i++;
            while(i < n && s[i] == ' ') i++;
            while(j < i) j++;
            while(j < n && s[j] != ' ') j++;
            
            reverse(s, i, j-1);
        }
    }
    
    void cleanSpaces(string &s, int n)
    {
        int i = 0, j = 0;
        
        while(j < n)
        {
            while(j < n && s[j] == ' ') j++;
            while(j < n && s[j] != ' ') swap(s[i++], s[j++]);
            while(j < n && s[j] == ' ') j++;
            if(j < n) s[i++] = ' ';
        }
        
        s = s.substr(0, i);
    }
};
