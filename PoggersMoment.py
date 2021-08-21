STOP = 5
while True:
    f = open("certifiedPOGGERS.txt", "a")
    f.write("PoggersMoment???")
    f.close()
    f = open("certifiedPOGGERS.txt", "r")
    print(f.read())
    STOP = STOP - 1
    if STOP == 0:
        break

print("Get Fucked")
