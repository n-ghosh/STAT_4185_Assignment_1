cipher = {
    'a':'v',
    'b':'h',
    'c':'r',
    'd':'j',
    'e':'t',
    'f':'x',
    'g':'s',
    'h':'a',
    'i':'e',
    'j':'f',
    'k':'b',
    'l':'n',
    'm':'o',
    'n':'i',
    'o':'g',
    'p':'l',
    'q':'m',
    'r':'z',
    's':'q',
    't':'u',
    'u':'c',
    'v':'k',
    'w':'d',
    'x':'p',
    'y':'y',
    'z':'w',
    ' ': '}',
    '\n': '^',
    ',': '5',
    '!': '[',
    ':':'-',
    ')':'*',
    '.': '%' 
}

encrypted_file = open("encrypted_message_one.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write code below

def decrypt(encrypted_string, encryption_cipher): 
    'Decrypts the given string using the given cipher. Returns a decrypted string'

    # Create a reverse cipher from encryption_cipher's key:value pairs
    reverse_cipher = {}
    for key,value in encryption_cipher.items():
        reverse_cipher[value] = key 

    # Decipher each character in encrypted_string with reverse_cipher, and store it 
    decrypted_string = ''
    for char in encrypted_string:
        # Confirm that the character is actually in the reverse_cipher 
        if char in reverse_cipher.keys():
            decrypted_string += reverse_cipher[char]
        else: 
            print(f'Unexpected char: "{char}" !! \n')
    
    # Testing
    if __name__ == '__main__':
        assert(reverse_cipher['v'] == 'a')
        assert(reverse_cipher['%'] == '.')
        assert(reverse_cipher['^'] == '\n')

    return decrypted_string

decrypted_message = decrypt(encrypted_message, cipher)
print(decrypted_message)