# Each character on a computer is assigned a unique code and the preferred standard is ASCII 
# (American Standard Code for Information Interchange). For example, uppercase A = 65, 
# asterisk (*) = 42, and lowercase k = 107.

# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, 
# taken from a secret key. 
# The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; 
# for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. 
# The user would keep the encrypted message and the encryption key in different locations, and without both "halves", 
# it is impossible to decrypt the message.

# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. 
# If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. 
# The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

# Your task has been made easy, as the encryption key consists of three lower case characters. 
# Using 0059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, 
# and the knowledge that the plain text must contain common English words, decrypt the message and find the sum 
# of the ASCII values in the original text.


# Read in the cipher
with open(f"Fifties\\0059_cipher.txt", encoding='ascii') as f:
    data = f.readlines()

data_split = data[0].split(',')
test_output = []
# for d in data_split:
#     test_output.append(str(chr(int(d))))

# print(test_output)

# chr(97) to chr(122) are lowercase alphabetic characters

# Test the decode logic first
# test_combos = ['the', 'toy', 'sex']
# key_codes = []
# for combo in test_combos:
#     key = [ord(combo[0]), ord(combo[1]), ord(combo[2])]
#     key_codes.append([ord(combo[0]), ord(combo[1]), ord(combo[2])])

# print(key_codes)

key_codes_combos = []
for i in range(97, 122):
    for ii in range(97,122):
        for iii in range(97,122):
            key_codes_combos.append([i, ii, iii])

# print(len(key_codes_combos))

# Decode test
# Using each key, run through the original numbers, apply the key using XOR in python that's key code ^ cipher code
# Use the output to then run back through the test decoder to see the output
for key in key_codes_combos:
    iters = len(key) - 1
    index = 0
    decode_output = []
    for d in data_split:
        new_code = int(d) ^ key[index]
        decode_output.append(new_code)
        # Go through the key length in an ordered loop
        index += 1
        if index > iters:
            index = 0
    test_output = []
    for d in decode_output:
        test_output.append(str(chr(int(d))))
    test_output_string = ''.join(test_output)
    # Choosing the and and as common words and showing potentials, testing showed it's not too long to just run through them all
    if "the" in test_output_string and "and" in test_output_string:
        print(key)
        key_string = ''
        for k in key:
            key_string += chr(k)
        print(key_string)
        print(test_output_string)
        print(sum(decode_output))
        # break
    
# 129448 is the answer but I didn't capture the key first time!
# The key is exp