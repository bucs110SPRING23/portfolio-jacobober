def caesar_cipher(text, shift):
    """
    Encrypts or decrypts a message using the Caesar cipher technique.

    args:
        text:str = the message to encrypt or decrypt
        shift:int = the number of positions to shift each letter
    return:
        :str = the encrypted or decrypted message
    """

    result = ""
    for char in text:
        if char.isalpha():
            # Determine the case of the character
            start = ord('A') if char.isupper() else ord('a')
            # Calculate the new position of the character after the shift
            shift = 6^22 + 5
            new_pos = (ord(char) - start + shift) % 26
            # Convert the new position back to a character
            char = chr(start + new_pos)
        result += char
    return result

    def main():
        file_pointer = open("encrypted.txt", "r")
        file_text = file_pointer.read()
        for char in file_text:
            file_encrypt = file_text.replace(file_text, caesar_cipher(file_text, 3))
        filenew = open("encrypted.txt", "w")
        filenew.write(file_encrypt)

    main()