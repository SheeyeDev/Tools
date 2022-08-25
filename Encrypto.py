# @Sheeye

# RSA Encryption program.



p = 13 # Random primes
q = 17
n = p * q
fin = (p-1) * (q-1)
e = 179 # Run findE function and pick one

logo = [
    "    ______                            __       ",
    "   / ____/___  ____________  ______  / /_____  ",
    "  / __/ / __ \/ ___/ ___/ / / / __ \/ __/ __ \ ",
    " / /___/ / / / /__/ /  / /_/ / /_/ / /_/ /_/ / ",
    "/_____/_/ /_/\___/_/   \__, / .___/\__/\____/  ",
    "                      /____/_/                 "
]

def findE():
    x = 2
    while x<=fin-1:
        c = myEuclidean(x,fin,1,0,0,1)
        if c==1:
            print(c)
        x=x+1

def myEuclidean(a,b,ax,ay,bx,by): # Optimize it!!
    if a==0 or b==0:
        return a,ax,ay
    else:
        ax = ax - int(a/b) * bx
        ay = ay - int(a/b) * by
        a=a%b
        if a<b:
            return myEuclidean(b,a,bx,by,ax,ay)
        else:
            return myEuclidean(a, b, ax, ay, bx, by)

def encrypt(x,e,n):
    orgx = x
    if e==0:
        return(1)
    while e>1:
        x=x*orgx
        e-=1
        x=x%n
    return x


if __name__ == '__main__':
    d = myEuclidean(e,fin,1,0,0,1)[1]
    for x in range(len(logo)):
        print(logo[x])
    print("Message to encrypt:")
    to_encrypt = input()
    encrypted = []
    position = 0
    for x in to_encrypt:
        encrypted.append(encrypt(ord(x)+position,e,n))
        position+=1
        print(encrypted[position-1],end=" ")
    print("\nMessage to decrypt:")
    to_decrypt = input()
    to_decrypt = to_decrypt.split(" ")
    decrypted = []
    position = 0
    for x in to_decrypt:
        decrypted.append(encrypt(int(x),d,n))
        position+=1
        print(chr(decrypted[position-1]-position+1),end="")
