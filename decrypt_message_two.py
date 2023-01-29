encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here

def decrypt_transposed(encrypted_string):
    '''Takes a string encrypted so every 2nd character at the beginning of the string must 
    be transposed with the same 2nd character from the end of the string. Returns a decrypted string.
    Example: decrypt_transposed("hol orh woa elyeu") -> "hello how are you" '''

    # Convert the string to a list for mutability
    lstString = [*encrypted_string] # I'm iterating through the input three times total - twice converting back and forth between string and list. I tried to do the whole thing iterating through only once but couldn't figure out the middle character, where sometimes I duplicated it and sometimes I skipped it

    # Iterate through half of the list. Swap every odd indexed character from the front with the corresponding index from the back
    i = 0
    while (i <= len(lstString)-i-1):
        if (i % 2 == 1):
            char = lstString[-i-1] # use -i-1 to pair with i because python starts negative indices at -1, not -0
            lstString[-i-1] = lstString[i]
            lstString[i] = char
        i += 1
    # Return it as a string
    return ''.join(lstString) 

if __name__ == '__main__':
    decrypted_message = decrypt_transposed(encrypted_message)
    print(decrypted_message)
    assert((decrypt_transposed('hol orh woa elyeu')) == 'hello how are you')