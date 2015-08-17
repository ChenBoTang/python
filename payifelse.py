hrs = raw_input("Enter Hours:")
h = float(hrs)
if h > 40:
    pay = float( 40*10.50+(h-40)*15.75)
    print  pay
else:
    pay = float (h*10.50)
    print  pay
        
