""" https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true """

def merge_the_tools(string, k):
    # your code goes here
    num_subsegments = int(len(string) / k)

    for index in range(num_subsegments):
        # Subsegment string
        t = string[index * k : (index + 1) * k]
        
        # Subsequence string having distinct characters
        u = ""
        
        # If a character is not already in 'u', append
        for c in t:
            if c not in u:
                u += c

        # Print final converted string
        print(u)
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
