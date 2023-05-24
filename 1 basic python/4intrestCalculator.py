principal=int(input("enter amount borrowed"))
years=float(input("enter num years"))
rate=float(input("enter rate of intrest"))

intrest=principal*years*rate/100
print("intrest calculated: "+ str(intrest))

#way 1
print("simple intrest"+str(principal)+"for period "+str(years)+" and the rate: "+str(rate) +"% is $"+str(intrest))
#way2 f" {var}"
print(f"principle{principal} and years are {years} rate {rate} so intrest is {intrest} ")

