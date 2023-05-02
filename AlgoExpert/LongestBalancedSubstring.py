"""
Write a function that takes in a string made up of parentheses ((and)). The function should return an integer repersenting the length of the longest balanced substring with regards to parentheses.

A string is said to be balanced if it has as many opening parentheses as it has closing parentheses and if no parenthesis is unmatched. Note that an opening parenthesis can't match a closing parenthesis that comes before it, and similarly, a closing parenthesis can't match an opening parenthesis that comes after it.
"""
def getLongestBalancedInDirection(string, leftToRight):
    openingParens = "(" if leftToRight else ")"
    startIndex = 0 if leftToRight else len(string) - 1
    incrementValue = 1 if leftToRight else -1
    maxLen = 0
    openingCount = 0
    closingCount = 0
    idx = startIndex
    while idx >=0 and idx < len(string):
        if string[idx] == openingParens:
            openingCount += 1
        else:
            closingCount += 1
        if closingCount == openingCount:
            maxLen = max(maxLen, openingCount*2)
        elif closingCount > openingCount:
            closingCount = 0
            openingCount = 0
        idx += incrementValue   
    return maxLen

def longestBalancedSubstring(string):
    return max (
        getLongestBalancedInDirection(string, True), getLongestBalancedInDirection(string, False)
        )

def main():
    pString = input("Enter the parentheses string: ")
    maxLen = longestBalancedSubstring(pString)
    print(f'''The longest balanced substring is {maxLen} characters long''')

if __name__ == "__main__":
    main()