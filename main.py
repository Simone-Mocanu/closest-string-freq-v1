import random


#hamming_dist calculates the hamming distance between two strings with the same length
def hamming_dist(s1, s2):
    if len(s1) != len(s2):
        raise Exception("Length of string1 is not equal to the length of string2")

    length = len(s1)

    # if length <= 1:
    #     raise Exception("Length must be greater than 1")

    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count

#INPUT
#[1, 0, 0, 1, 1]
#[o, i, l]
strings = ["cotal", "pomap", "pitll", "simnp", "slbap"]
solution_string = ""

length = len(strings[0])
for string in strings:
    if len(string) != length:
        raise Exception("All strings should have the same length")
    
#hda - hamming distances array
hda = []

#populate the hamming distance array
for i in range(length):
    hda.append(0)

#lfda - letter frequency dictionary array
#populate lfda
lfda = []
for i in range(length):

    full_of_zeroes = True
    for hd in hda:
        if hd != 0:
            full_of_zeroes = False
            break

    #chd = count hamming distance?
    chd = 0
    if not full_of_zeroes:
        for hd in hda:
            if chd < hd:
                chd = hd

    lfd = {}
    #i - index of string(letter)
    if not full_of_zeroes: 
        #[1, 0, 0, 1, 1]
        #cotal, pomap, pitll, simmp, slbap
        for index in range(length):
            if hda[index] == chd:
                letter = strings[index][i]
                if letter not in lfd:
                    lfd[letter] = 0


        for key in lfd.keys():
            for string in strings:
                if string[i] == key:
                    lfd[key] += 1

    else:
        # lfd - letter frequency dictionary
        for string in strings:
            if string[i] not in lfd:
                lfd[string[i]] = 1
            else:
                lfd[string[i]] += 1

        # print(lfd)

    #hhd - highest hamming distance
    hhd = list(lfd.values())[0]

    #get the hhd value in each array
    for key, value in lfd.items():
        if hhd < value:
            hhd = value

    #populate the array(char_arr) with characters that have the hhd
    char_arr = []
    for key, value in lfd.items():
        if value == hhd: 
            char_arr.append(key)

    #if we got more than one character with the hhd, we select one of the characters randomly
    #else we select the only character in the array
    if len(char_arr) > 1:
        solution_string += random.choice(char_arr)
    else:
        solution_string += char_arr[0]

    #ssl - solution string length
    ssl = len(solution_string)
    #tsa - temporary string array
    tsa = []
    for string in strings:
        temp_str = ""
        for j in range(len(solution_string)):
            temp_str += string[j]

        tsa.append(temp_str)

    for u in range(len(tsa)):
        hda[u] = hamming_dist(solution_string, tsa[u]) 

    print(hda)

    print("solution string: " + solution_string)   

print("")
print("Hamming distances between the solution string and the input")
print("-------------------------")
for string in strings:
    print(solution_string, string, hamming_dist(solution_string, string))


print("-------------------------")
#STEPS:
#Initialize the hamming distances array with zeroes.
#BEGIN LOOP
#Select letter with the highest frequency and add it to the solution string.
#   if more than one letter has the highest freq select one of the letters
#Update the hamming distances array(compare the solution string with 'column')
#Take the letters of the position of the highest hamming distances in the h.d.a
#from the next 'column'
#REPEAT

