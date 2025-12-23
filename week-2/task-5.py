N = int(input("Input: "))
plates = [input() for i in range(N)]
allowed_letters = set("ABCEHKMOPTXY")

for plate in plates:
    if len(plate) == 6 and \
       plate[0] in allowed_letters and \
       plate[1].isdigit() and plate[2].isdigit() and plate[3].isdigit() and \
       plate[4] in allowed_letters and plate[5] in allowed_letters:
        print("Yes")
    else:
        print("No")