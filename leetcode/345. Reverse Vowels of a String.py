class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        # pointers 
        forward = 0
        reverse = len(s) - 1
        
        string = list(s) # original string to a list 
        
        while reverse > forward: # iterate over the string 
            # using continues repeats those if statements by restarting the while loop 
            if not string[forward] in vowels: 
                forward+=1
                continue
            if not string[reverse] in vowels: 
                reverse-=1
                continue
                
            # found vowels 
            string[forward], string[reverse] = string[reverse], string[forward] # swap them 
            
            # keep going 
            forward+=1
            reverse-=1
            
        return "".join(string)