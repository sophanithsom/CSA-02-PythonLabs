
# Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter.
# Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes a hyphen will separate the two letters in the string.

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

user_range = input("Enter a range of letters (e.g., a-z): ")

start_char = alphabet.index(user_range[0])
end_char = alphabet.index(user_range[-1])

result_string = alphabet[start_char:end_char + 1]
print(result_string)
