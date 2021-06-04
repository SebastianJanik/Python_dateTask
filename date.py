from itertools import permutations
import datetime

def dateConverter(line) :
    numbers = [int(number) for number in line.split("/")]
    numbers.sort()
    possiblyDates = list(permutations(numbers))
    for earliestDate in possiblyDates :
        year,month,day = earliestDate
        if month == 0 :
            month += 1
        if day == 0 :
            day += 1
        if(len(str(year))) < 4 :
            year += 2000
        try :
            if(datetime.datetime(int(year), int(month), int(day))) :
                return line + "  =>  " + str(year) + "-" + str(month) + "-" + str(day)
        except ValueError :
            None
    return line + " is illegal"

def main() :
    file = open("input.txt", "r")
    line = file.read()
    file.close()
    print(dateConverter(line))

main()






