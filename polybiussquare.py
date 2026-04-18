square = [
    ['A','B','C','D','E'],
    ['F','G','H','I','K'],
    ['L','M','N','O','P'],
    ['Q','R','S','T','U'],
    ['V','W','X','Y','Z']
]

for_Space = "00"

def encrypt(text):
    text = text.upper().replace("J","I")
    result = ""

    for char in text:
        if char == " ":
            result += for_Space + " "
        else: 
         for i in range(5):
            for j in range (5):
              if square[i][j] == char:
                  result+= str(i+1) + str(j+1) + " "
    return result.strip()


def decrypt(code):
    result = ""
    parts = code.split()

    for part in parts:
        if part == for_Space:
            result += " "
        else: 
         row = int (part[0]) - 1
         col = int(part[1]) - 1
         result += square[row][col]
    return result


def test():
    while True:
        print(" Zgjidhni një opsion: ")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Zgjedh: ")

        if choice == "1":
            text = input("Shkruaj tekstin qe doni ta enkriptoni: ")
            print("Encrypted:", encrypt(text))

        elif choice == "2":
            code = input("Shkruaj tekstin qe doni ta dekriptoni: ")
            print("Decrypted:", decrypt(code))

        elif choice == "3":
            print("Exit!")
            break

        else:
            print("Gabim, provo përsëri!")


if __name__ == "__main__":
    test()
