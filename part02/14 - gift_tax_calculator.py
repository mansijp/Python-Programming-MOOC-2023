gift = int(input("Value of gift: "))

if gift < 5000:
    print("No tax!")
elif gift < 25000:
    print("Amount of tax: " + str(100+(gift-5000)*0.08) + " euros")
elif gift < 55000:
    print("Amount of tax: " + str(1700+(gift-25000)*0.1) + " euros")
elif gift < 200000:
    print("Amount of tax: " + str(4700+(gift-55000)*0.12) + " euros")
elif gift < 1000000:
    print("Amount of tax: " + str(22100+(gift-200000)*0.15) + " euros")
elif gift >= 1000000:
    print("Amount of tax: " + str(142100+(gift-1000000)*0.17) + " euros")