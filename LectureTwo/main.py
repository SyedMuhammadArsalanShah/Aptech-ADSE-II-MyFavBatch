a=1
while a<=10:
    print(a)
    # a=a+1
    a+=1



final_bill=0

while True:
    products = input("Enter Your Product Item")
    priceOfProduct= float(input("Enter Your Product Price"))
    if products == "counter_closed" :
        print("Allah Hafiz " )
        break
    else: 
        final_bill+=priceOfProduct

print("Your Final Bill Is ", final_bill)

