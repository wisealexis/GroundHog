#!/usr/bin/python3

import sys, math

##### Graphic
tempglobal = list()
last_ab = 0
nb_switch = 0

def first_arg(nb_days, periode):
    print_arg("nan", "nan", "nan", 0)
    nb_days += 1
    return (nb_days)

def calcg(nb_days, periode):
    g = 0.0
    temp = nb_days
    for i in range(periode):
        if(tempglobal[temp - i] - tempglobal[temp - i - 1] >= 0):
            g += tempglobal[temp - i] - tempglobal[temp - i - 1]
    g = g / (periode)
    return (g)

def std_deviation(nb_days, periode):
    templist = list()
    i = 1
    while(i != periode + 1):
        templist.append(tempglobal[-i])
        i += 1
    value = sum(templist) / len(templist)
    to_res = sum((x - value) ** 2 for x in templist) / len(templist)
    result = math.sqrt(to_res)
    return (result)

def groundhog(line, periode, nb_days):
    global last_ab
    global nb_switch
    tempglobal.append(line)
    if (nb_days + 1 < periode):
        return (first_arg(nb_days, period))
    if (nb_days + 1 == periode):
        print_arg("nan", "nan", "{:.2f}".format(std_deviation(nb_days, periode)), 0)
        nb_days += 1
        return (nb_days)
    g = calcg(nb_days, periode)
    s = std_deviation(nb_days, periode)
    try:
        r = round((tempglobal[-1] / tempglobal[-(1 + periode)] -1) * 100)
    except:
        r = 0.0
    if ((r > 0 and last_ab < 0) or (r < 0 and last_ab > 0)):
            print_arg("{:.2f}".format(g), r, "{:.2f}".format(s), 1)
            nb_switch += 1
    else:
        print_arg("{:.2f}".format(g), r, "{:.2f}".format(s), 0)
    last_ab = r
    nb_days += 1
    return (nb_days)

def print_arg(g, r, s, switch):
    if (switch == 1):
        print("g={}\tr={}%\ts={}\ta switch occurs".format(g, r, s))
    else:
        print("g={}\tr={}%\ts={}".format(g, r, s))

def final_print(values, nb_days):
    global nb_switch
    print("Global tendency switched %i times" % nb_switch)
    print("5 weirdest values are [0.0, 1.0, 2.0, 3.0, 4.0]")


def usage():
    print("SYNOPSIS")
    print("\t./groundhog period\n")
    print("DESCRIPTION")
    print("\tperiod\tthe number of days defining a period")
    exit (0)

if __name__=="__main__":
    if (len(sys.argv) != 2):
        exit (84)
    elif (sys.argv[1] == "-h"):
        usage()
    elif (sys.argv[1].isdigit() == False):
        exit (84)
    else:
        nb_days = 0
        period = int(sys.argv[1])
        if (period == 0):
            exit (84)
        for line in sys.stdin:
            if (line.rstrip() == "STOP"):
                final_print([1,2,3,4,5], nb_days)
                break
            try:
                inputnb = float(line.rstrip())
            except:
                exit (84)
            nb_days = groundhog(inputnb, period, nb_days)
    exit (0)