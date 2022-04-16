def main():
    phrase = input("Choose a phrase: ")
    print("Your phrase is '", phrase, "'", sep = "")
    pos = input("Which character would you like to see? [ENTER NUMBER] ")
    print("The character at position ", pos, " is '", phrase[int(pos)-1], "'", sep = "")

main()
