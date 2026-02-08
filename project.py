def main():
    print("Guess the drama name!")
    name_list =("youth of may","Twinking Watermelon","The last 10 years","The first Frost")
    print("Hints: The drama has one of these titles:")
    print("Hints: The drama has one of these titles:")
    for i, name in enumerate(name_list, start=1):
        print(f"{i}. {name[0]}{'*'*(len(name)-1)}")
        guess = input("Enter your guess: ").strip().casefold()
    
    if guess in [n.casefold() for n in name_list]:
        print("yay!")
    else:
        print(" Nope! Better luck next time!")
        print("Theanswers were:")
        for n in name_list:
            print("-", n)

if __name__ == "__main__":
    main()