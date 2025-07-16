import numpy as np
letters=[chr(i) for i in range(97,123)]
def keyMatrix(key):

    key = key.replace(" ", "").lower()
    newkey=[]
    # add all letter in key to newkey[] without repeating 
    for i in key:
        if i not in newkey:
            # replace j into i if found in key because the matrex is 5*5 needs only 25 letters
            if i=='j':
                newkey.append('i')
            else:
                newkey.append(i)
    #add to the newkey[] the ather letter remainder in order
    for j in letters:
        if j.lower() not in newkey:
            if j.lower()=='j':
                continue
            newkey.append(j.lower())
    #chainge the list in to array using numby libriry 

    matrix=np.array(newkey).reshape(5, 5)
    return matrix
def Pairs(plainText):
    plain=plainText.replace(" ","").lower()
    i=0
    x=0
    plaintextPair=[]
    while(i<len(plain)-1):
        if (plain[i]==plain[i+1]) and not plain[i]=='x':
            plaintextPair.append(plain[i]+'x')
            i+=1
            x+=1
        elif (plain[i]==plain[i+1]) and plain[i]=='x':
            plaintextPair.append(plain[i]+'z')
            i+=1
            x+=1
        else:
            plaintextPair.append(plain[i]+plain[i+1])#['ab','cx','cd','fg','hi']
            i+=2
    if len(plaintextPair)*2 < len(plain)+x:
        plaintextPair.append(plain[-1]+'x')
        print("pairs: ", plaintextPair)
    return plaintextPair
def CipherPairs(pairs,matrix):
    cipher=[]
    for pair in pairs:
            Done=False
            for row in range(5):
                cipher1=''
                cipher2=''
                currentRow=matrix[row, :]
                if pair[0] in currentRow and pair[1] in currentRow:
                    First_index=list(currentRow).index(pair[0])
                    Second_index=list(currentRow).index(pair[1])
                    cipher1=currentRow[(First_index +1) % 5]
                    cipher2=currentRow[(Second_index +1) % 5]
                    cipher.append(cipher1+cipher2)
                    Done=True
                    break
            if Done:
                continue
            for col in range(5):
                currentcol=matrix[:,col]
                if pair[0] in currentcol and pair[1] in currentcol:
                    First_index=list(currentcol).index(pair[0])
                    Second_index=list(currentcol).index(pair[1])
                    cipher1=currentcol[(First_index +1) % 5]
                    cipher2=currentcol[(Second_index +1) % 5]
                    cipher.append(cipher1+cipher2)
                    Done=True
                    break
            if Done:
                continue    
            if  not Done:    
                r1,c1=np.where(matrix==pair[0]) # this finds the row and column of the first letter
                r2,c2=np.where(matrix==pair[1]) # this finds the row and column of the second letter    
                cipher1=matrix[r1[0],c2[0]]
                cipher2=matrix[r2[0],c1[0]]
                cipher.append(cipher1+cipher2)
    return cipher


def decryptPairs(pairs, matrixKey):
    cipher=[]
    for pair in pairs:
            Done=False
            for row in range(5):
                cipher1=''
                cipher2=''
                currentRow=matrixKey[row, :]
                if pair[0] in currentRow and pair[1] in currentRow:
                    First_index=list(currentRow).index(pair[0])
                    Second_index=list(currentRow).index(pair[1])
                    cipher1=currentRow[(First_index -1) % 5]
                    cipher2=currentRow[(Second_index -1) % 5]
                    cipher.append(cipher1+cipher2)
                    Done=True
                    break
            if Done:
                continue
            for col in range(5):
                currentcol=matrixKey[:,col]
                if pair[0] in currentcol and pair[1] in currentcol:
                    First_index=list(currentcol).index(pair[0])
                    Second_index=list(currentcol).index(pair[1])
                    cipher1=currentcol[(First_index -1) % 5]
                    cipher2=currentcol[(Second_index -1) % 5]
                    cipher.append(cipher1+cipher2)
                    Done=True
                    break
            if Done:
                continue    
            if  not Done:    
                r1,c1=np.where(matrixKey==pair[0]) # this finds the row and column of the first letter
                r2,c2=np.where(matrixKey==pair[1]) # this finds the row and column of the second letter    
                cipher1=matrixKey[r1[0],c2[0]]
                cipher2=matrixKey[r2[0],c1[0]]
                cipher.append(cipher1+cipher2)
    return cipher

def encrypt(plaintText, key):
    FromTistToString = ''
    pairs = Pairs(plaintText)
    matrixKey = keyMatrix(key)
    ciphertext = CipherPairs(pairs, matrixKey)
    for i in ciphertext:
        FromTistToString += i  # 🔁 تصحيح التجميع هنا
    return FromTistToString

def decryption(ciphertext, key):
    FromTistToStringDecrypt=''
    pairs=Pairs(ciphertext)#lsit
    matrixKey=keyMatrix(key) # aray
    OriginalPlain=decryptPairs(pairs,matrixKey)
    for i in OriginalPlain:
        FromTistToStringDecrypt+=i
    return FromTistToStringDecrypt
# plainText=input("Enter Message to Encrypt using play fair : ")
plainText=input("enter message: ")
key="plain"
p=Pairs(plainText)
print(p)

ciphertex=encrypt(plainText,key)
print("cipher text :",ciphertex)

plainTextPack=decryption(ciphertex,key)
print("Plain text is : ",plainTextPack)

