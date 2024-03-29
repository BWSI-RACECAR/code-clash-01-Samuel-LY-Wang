"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #1 - Paul's Palindrome Password (palindrome.py)


Author: Chris Lai

Difficulty Level: 1/10

Prompt: Paul has a brand new autonomous driving RACECAR that requires a password input 
before unlocking and allowing the user to drive. Since Paul can never remember his exact 
password, he set the following rule for a valid password: “If the password given to the 
RACECAR is more than 6 letters long and is a palindrome, unlock the car”. Write a Python
script that it returns “True” if the given password unlocks the car (is more than 6 
characters long and is a palindrome) and returns “False” if the given password is invalid.

Extra Challenge: Solve this problem in 1 line of code! (Excluding function definitions) 

Test Cases:
Input: “racecar”    Output: True
Input: “314156”     Output: False
Input: “dad”        Output: False
"""

class Solution:
    # Write code below to complete prompt
    def isPalindrome(self, s):
      if (len(s)<=6):
        return False
      for i in range(len(s)):
        if (s[i] != s[-i-1]):
          return False
      return True
      pass

def main():
    tc1 = Solution()
    inpyt = input()
    # Write code below to complete prompt
    print(tc1.isPalindrome(inpyt))

if __name__ == "__main__":
    main()