def isPalindrome(str):
    if str == "exit":
        quit()
    while(str != "exit"):
        word = str[:: -1]
        if str.lower() == word.lower():
            print("Palindrome test:", True)
        else:
            print("Palindrome test:", False)
        isPalindrome(input("Enter string to test for palindrome or 'exit': "))

x = input("Enter string to test for palindrome or 'exit': ") # The prompt for the user
isPalindrome(x)