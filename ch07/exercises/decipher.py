def caesar_decipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the case of the character
            start = ord('A') if char.isupper() else ord('a')
            # Calculate the new position of the character after the shift
            new_pos = (ord(char) - start + shift) % 26
            # Convert the new position back to a character
            char = chr(start + new_pos)
        result += char
    return result

def main():
    file_pointer = open("encrypted-#B00829653.txt", "r")
    file_text = file_pointer.read()
    for char in file_text:
        file_encrypt = file_text.replace(file_text, caesar_decipher(file_text, 2))
    filenew = open("decrypted.txt", "w")
    filenew.write(file_encrypt)

main()