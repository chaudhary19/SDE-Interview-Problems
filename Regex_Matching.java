class Solution {
    public boolean isMatch(String s, String p) {
        char st[]=s.toCharArray();
        char pat[]=p.toCharArray();
        boolean t[][]=new boolean[s.length()+1][p.length()+1];
        t[0][0]=true;
        for(int i=1;i<t[0].length;i++)
        {
            if(pat[i-1]=='*')
                t[0][i]=t[0][i-2];
        }
        for(int i=1;i<t.length;i++)
        {
            for(int j=1;j<t[0].length;j++)
            {
                if(pat[j-1]=='.' || (pat[j-1]==st[i-1]))
                    t[i][j]=t[i-1][j-1];
                else if(pat[j-1]=='*')
                {
                    t[i][j]=t[i][j-2];
                    if(st[i-1]==pat[j-2] || pat[j-2]=='.')
                        t[i][j]|=t[i-1][j];
                }
            }
        }
        return t[s.length()][p.length()];
    }
}
