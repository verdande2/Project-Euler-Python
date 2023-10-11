import time

# text is an array of ascii codes, key can be a string
def xor(text, key):
    ascii_decrypted_text = []
    decrypted_text = []
    keyLen = len(key)
    counter = 0
    for char_code in text:
        #print(char," ",ord(key[counter]))
        ascii_decrypted_text.append(char_code ^ ord(key[counter]))
        if counter == keyLen - 1:
            counter = 0
        else:
            counter += 1
    for char in ascii_decrypted_text:
        decrypted_text.append(chr(char))
    #print(decrypted_text)
    decrypted_text = "".join(decrypted_text)
    return decrypted_text


start = time.time()
text = []
text_file = open('problem59_files/cipher1.txt', 'r')
for line in text_file:
    ascii_text = line
ascii_text = ascii_text.split(",")
for char in ascii_text:
    text.append(int(char.replace("\n","")))
#text = "".join(text)
searchString = []
searchString.append("the")
searchString.append("The")
searchString.append("and")
searchString.append("that")
searchString.append("of")
searchString.append("to")
searchString.append("in")
searchString.append("it")
searchString.append("you")
searchString.append("he")
searchString.append("was")
searchString.append("for")
searchString.append("on")

found = False
for a in range(97, 122+1):
    for b in range(97, 122+1):
        for c in range(97, 122+1):
            possibleCorrectKey = 0
            testKey = chr(a) + chr(b) + chr(c)
            decryptedText = xor(text,testKey)
            decryptedText = "".join(decryptedText)
            for searchTerm in searchString:
                if searchTerm in decryptedText:
                    possibleCorrectKey +=1

            
            if possibleCorrectKey > 9:
                print(testKey," decrypts into:",decryptedText)
                found = True
                break
        if found: break
    if found: break
cumSum = 0
for char in decryptedText:
    cumSum += ord(char)
end = time.time()
print("found in",str(end-start),"Answer is",str(cumSum))
