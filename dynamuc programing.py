import json
import copy

answerlist = []
firstpass = True


def loadjson():
    with open('coin-change.json') as openfile:
        json_stuff = json.load(openfile)
    openfile.close()
    return json_stuff


def writejson(coins):
    with open('coin-change.json', 'w') as outfile:
        json.dump(coins, outfile)
    outfile.close()


def chadanswer():
    global answerlist
    chaddest_answer = []
    chaddest_number = answerlist[0][0]
    for i in range(len(answerlist)):
        if answerlist[i][0] < chaddest_number:
            chaddest_answer = answerlist[i]
            chaddest_number = answerlist[i][0]

    return chaddest_answer


def deductcoins(coins, coinsvaluelist, bestans):
    global answerlist
    for i in range(len(coinsvaluelist) - 1, -1, -1):
        while bestans[1][i] > 0:
            coins[coinsvaluelist[i][0]] -= 1
            bestans[1][i] -= 1
    return coins


def printchange(bestans, coinsvaluelist):
    print("Se le ha devuelto:")
    for i in range(len(bestans[1])):
        if bestans[1][i] > 0:
            print(f'{bestans[1][i]} monedas de {int(coinsvaluelist[i][0])}')


def forceogvalues(coins, pay, maxchanage, coinsvaluelist, paylist, i):
    while pay > 0:
        if int(coins[coinsvaluelist[i][0]]) >= 1 and int(coinsvaluelist[i][0]) <= pay:
            pay = pay - int(coinsvaluelist[i][0])
            paylist[0] += 1
            paylist[1][i] += 1
            coinsvaluelist[i][1] -= 1
        else:
            i -= 1
            if i < 0:
                break
    if pay == 0:
        if paylist not in answerlist:
            answerlist.append(copy.deepcopy(paylist))


def checkbroke(answerlist):
    if len(answerlist) == 0:
        print("No hay suficientes monedas para darle cambio")
        exit()


def arrcoinvalues(coins):
    tempval = coins.items()
    coinsvaluelistt = list(tempval)
    coinsvaluelist = []
    for i in range(len(coinsvaluelistt)):
        tempadd = list(coinsvaluelistt[i])
        coinsvaluelist.append(tempadd)
    for i in range(len(coinsvaluelist)):
        coinsvaluelist[i][0] = coinsvaluelist[i][0]
    return coinsvaluelist


def actualrecursive(coins, pay, maxchanage, coinsvaluelist, paylist, i):
    actualrecursive2(coins, pay, maxchanage, copy.deepcopy(coinsvaluelist), copy.deepcopy(paylist), i)
    forceogvalues(coins, pay, maxchanage, copy.deepcopy(coinsvaluelist), copy.deepcopy(paylist), len(coinsvaluelist) - 1)


def actualrecursive2(coins, pay, maxchanage, coinsvaluelist, paylist, i):
    global answerlist
    global firstpass
    while pay > 0:

        if i > len(coinsvaluelist) - 1:
            return False
        if int(coinsvaluelist[i][1]) >= 1 and int(coinsvaluelist[i][0]) <= pay:

            if not firstpass:
                pay -= int(coinsvaluelist[i][0])
                paylist[0] += 1
                paylist[1][i] += 1
                coinsvaluelist[i][1] -= 1
            firstpass = False
            if actualrecursive2(coins, pay, maxchanage, copy.deepcopy(coinsvaluelist), copy.deepcopy(paylist), i):
                pass
                i += 1
            else:  # false

                i += 1


        else:

            if actualrecursive2(coins, pay, maxchanage, copy.deepcopy(coinsvaluelist), copy.deepcopy(paylist), i + 1):  # true
                pass
                i += 1
                pass
            else:  # false

                i += 1

            # actualrecursive(coins, pay, maxchanage, coinsvaluelist, copy.deepcopy(paylist), i + 1)

    if pay == 0:
        if paylist not in answerlist:
            answerlist.append(copy.deepcopy(paylist))
            return True
        else:
            return True
    if pay <= -1:
        return False
    else:
        return False


def recursive(amntpay, maxchange):
    global answerlist
    coins = loadjson()
    coinlinked = arrcoinvalues(coins)
    paylist = [0, [0 for i in range(len(coinlinked))]]
    # i=len(coinlinked)-1
    i = 0
    actualrecursive(coins, amntpay, maxchange, coinlinked, paylist, i)
    checkbroke(answerlist)
    bestans = chadanswer()
    printchange(bestans, coinlinked)
    deductcoins(coins, coinlinked, bestans)
    writejson(coins)


recursive(6, 1000)

# 1 1 1 1 1 1
# 2 1 1 1 1
# 2 2 1 1
################
# 2 2 2
# 5 1
