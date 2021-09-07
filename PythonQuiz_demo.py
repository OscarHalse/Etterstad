import re as re

with open("Spørsmål.txt") as file:
    all_text = file.read()
Qlist = all_text.split("Q:")
Qlist.remove("")
QA_list = [[] for i in range(len(Qlist))]

for i in range(len(Qlist)):
    Q = Qlist[i]
    QA = Q.split("-")
    for j in range(len(QA)):
        a = QA[j]
        a = a.strip()
        a = a.rstrip("\nA:")
        QA_list[i].append(a)

nr = int(input("Which question do you want?\n"))-1
print("\n\n{}\n".format(QA_list[nr][0]))
for i in range(1, len(QA_list[nr])-1):
    print("{})   {}".format(i, QA_list[nr][i]))

success = False
while success == False:
    ans = input()
    if ans == QA_list[nr][-1]:
        print("\nCorrect!")
        success = True
    else:
        print("\nTry again :(")
