#!/usr/bin/python3.4
# -*-coding:utf-8 -*

import Data
import random
import pickle


def loose(x):
    """condtion for loose"""
    if x == len(Data.pendu):
        return x


def adderror(x):
    """add 1 error for the player"""
    x += 1
    return x


def addscore(x):
    """ add 100 points for the player"""
    x += 100
    return x


def randomword():
    """generate a random word"""
    x = random.randint(0, len(Data.words) - 1)
    word = Data.words[x]
    del x
    return word


def listconvstr(liste):
    """convert a list in str"""
    string = ".".join(liste)
    return string


def strconvlist(string):
    """convert a string in list"""
    x = 0
    liste = []
    while x < len(string):
        liste.append(string[x])
        x += 1
    return liste


def hangedwordlist(string):
    """convert a str in list and replace the char by '_'"""
    x = 0
    liste = []
    while x < len(string):
        liste.append("_")
        x += 1
    return liste


def searchletter(word, word2, char):
    """search a string in the word listed"""
    x = 0
    y = 0
    while x < len(word):
        if char == word[x]:
            word2[x] = word[x]
            y += 1
        x += 1
    if y > 0:
        return word2


def printwordhanged(liste):
    x = listconvstr(liste)
    print("{0}".format(x.center(50)))


def menu():
    """Print the menu"""
    print("MENU\n".center(60))
    for numbermenu, menuname in enumerate(Data.menu):
        print("{0} {1}".center(60).format(numbermenu, menuname))
    try:
        x = input("Your Choice : ")
        if int(x) + 1 <= len(Data.menu):
            if int(x) == 0:
                play()
            if int(x) == 1:
                printscore(readfilescore())
                menu()
    except ValueError:
        menu()


def printpendu(x):
    print("{0}".format(Data.pendu[x]))


def play():
    """GAME"""
    word = randomword()
    word2 = hangedwordlist(word)
    word = strconvlist(word)
    save = []
    x = 0
    y = 0
    while not loose(x):
        try:
            space()
            printpendu(x)
        except IndexError:
            quit()
        printwordhanged(word2)
        print("your score = {0}".format(y))
        space()
        if word[:] == word2[:]:
            print("victory")
            y = addscore(y) * 2
            word = randomword()
            word2 = hangedwordlist(word)
            word = strconvlist(word)
        letter = input("Choice a letter : ")
        if not searchletter(word, word2, letter):
            x = adderror(x)
        else:
            word2 = searchletter(word, word2, letter)
            if save != word2:
                y = addscore(y)
                save = word2[:]
    print("you have loose")
    print("The word is : {0}".format(listconvstr(word)))
    scoreliste = readfilescore()
    scoreliste = registerscore(y, scoreliste)
    writefilescore(scoreliste)
    menu()


def registerscore(scoreplayer, scorelist):
    nameplayer = input("what you're name : ")
    scorelist[nameplayer] = scoreplayer
    return scorelist


def writefilescore(score):
    try:
        with open("score", "wb") as file:
            pickle.Pickler(file).dump(score)
    except:
        x = {}
        writefilescore(x)
        menu()


def readfilescore():
    try:
        with open("score", "rb") as file:
            score = pickle.Unpickler(file).load()
        return score
    except:
        x = {}
        writefilescore(x)
        menu()


def space():
    print("\n\n\n")


def printscore(score):
    """ print the score for all player"""
    space()
    print("score".center(60))
    for name, scorep in score.items():
        print("{0} = {1}".format(name, scorep))
    space()

if __name__ == "__main__":

    menu()
