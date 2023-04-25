class StringUtility:
    def __init__(self, string):
        self.string = string
    
    def __str__(self):
        """
        Returns the internal string itself, unchanged.
        """
        return self.string
    
    def vowels(self):
        """
        Counts the number of vowels in the string and returns the result as a string.
        If the count is less than 5, returns the string representation of the count.
        If the count is 5 or more, returns the word 'many' instead of the actual count.
        
        Returns:
        str: The number of vowels in the string, or 'many' if the count is 5 or more.
        """
        vowel_count = 0
        for char in self.string.lower():
            if char in 'aeiou':
                vowel_count += 1
        if vowel_count < 5:
            return str(vowel_count)
        else:
            return 'many'
    
    def bothEnds(self):
        """
        Returns a string made of the first 2 and last 2 characters of the original string.
        If the length of the string is less than or equal to 2, returns an empty string.
        
        Returns:
        str: The first 2 and last 2 characters of the original string, or an empty string if the length is 2 or less.
        """
        if len(self.string) <= 2:
            return ''
        else:
            return self.string[:2] + self.string[-2:]
    
    def fixStart(self):
        """
        Returns a string where all occurrences of the first character have been changed to '*', except do not change the first char itself.
        
        Returns:
        str: The modified string with all occurrences of the first character (excluding the first character itself) replaced with '*'.
        If the parameter is length 1 or less, returns the parameter as is.
        """
        if len(self.string) <= 1:
            return self.string
        else:
            first_char = self.string[0]
            return first_char + self.string[1:].replace(first_char, '*')
    
    def asciiSum(self):
        """
        Returns an integer that contains the sum of all ASCII values in the string.
        
        Returns:
        int: The sum of all ASCII values in the string.
        """
        return sum(ord(char) for char in self.string)
    
    def cipher(self):
        """
        Returns an encoded string by incrementing all letters by the length of the string.
        Leaves any characters that are not letters unchanged.
        Uppercase always wraps around to uppercase, and lowercase always wraps around to lowercase.
        
        Returns:
        str: The encoded string.
        """
        encoded = ''
        shift = len(self.string)
        for char in self.string:
            if char.isalpha():
                if char.isupper():
                    encoded += chr((ord(char) - 65 + shift) % 26 + 65)
                else:
                    encoded += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encoded += char
        return encoded

#Extra Credit Attempt: Please look
# def vowels(self):
#         return str(len([c for c in self.string.lower() if c in 'aeiou'])) if len([c for c in self.string.lower() if c in 'aeiou']) < 5 else 'many'

#     def bothEnds(self):
#         return self.string[:2] + self.string[-2:] if len(self.string) > 2 else ''

#     def fixStart(self):
#         return self.string[0] + self.string[1:].replace(self.string[0], '*') if len(self.string) > 1 else self.string

#     def asciiSum(self):
#         return sum(ord(c) for c in self.string)

#     def cipher(self):
#         return ''.join(chr((ord(c) - 65 + len(self.string)) % 26 + 65) if c.isupper() else
#                        chr((ord(c) - 97 + len(self.string)) % 26 + 97) if c.islower() else c for c in self.string)


