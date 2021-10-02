class Solution {
public:
    string longestPalindrome(string &s) {
        int n = s.size();
        
        bool dp[n][n];
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < n; j++)
            {
                dp[i][j] = false;
                if(i == j) dp[i][j] = true;
            }
        }
        
        int maxLength = 1, Start = 0;
        for(int start = n-1; start >= 0; start--)
        {
            for(int end = start+1; end <= n; end++)
            {
                if(s[start] == s[end])
                {
                    if(end-start == 1 || dp[start + 1][end - 1])
                    {
                        dp[start][end] = true;
                        if(end-start+1 > maxLength)
                        {
                            maxLength = end - start + 1;
                            Start = start;
                        }
                    }
                }
            }
        }
        
        return s.substr(Start, maxLength);
    }
};

// this is DP based solution
// Time Complexity: O(n^2)
// Space Complexity: O(n^2)
