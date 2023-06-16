
def interestCalc(initialLoan,monthlyInterest,noMonths):
    P = round(((monthlyInterest/100)*initialLoan)/(1-(1+(monthlyInterest/100))**(-noMonths)),2)
    return(P)

print(f"£{interestCalc(1000,10,6)}")






