def main():
    t = input("What time is it? ")
    t = convert(t)
    if t >= 7 and t <= 8:
        print("breakfast time")

    if t >= 12 and t <= 13:
        print("lunch time")

    if t >= 18 and t <= 19:
        print("dinner time")


def convert(time):
    parts = time.split(":")
    h = int(parts[0])
    m = int(parts[1])

    total = h + (m / 60)
    return total


if __name__ == "__main__":
    main()
