with open("Spørsmål.txt") as file:
    all_text = file.read()
Q = all_text.split("Q:")
Q.remove("")
QA_list = [[] for i in range(len(Q))]

for i in range(len(Q)):
    QA = Q[i].split("-")
    for j in range(len(QA)):
        a = QA[j]
        a = a.strip()
        a = a.rstrip("\nA:")
        QA_list[i].append(a)

nr = int(input("Which question do you want?\n"))-1
print("\n\n{}\n".format(QA_list[nr][0]))
for i in range(1, len(QA_list[nr])-1):
    print("{})   {}".format(i, QA_list[nr][i]))
print("\n")

success = False
while success == False:
    ans = input()
    if ans == QA_list[nr][-1]:
        print("\nCorrect!")
        success = True
    else:
        print("\nTry again :(")
