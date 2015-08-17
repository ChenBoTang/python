score = raw_input("input a score: ")
num = float(score)
try:
    if num >= 0.9 :
        print "A"
    elif num >= 0.8:
        print "B"
    else if num>= 0.7:
        print "C"
            else if num >=0.6:
                print "D"
                else if num < 0.6:
                print "F"
except:
    print "please input 0-1"
    break:
