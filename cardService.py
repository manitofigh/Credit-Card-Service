import random

def checkCard(cardNum):
  sumOdd, sumEven = 0, 0
  for i in range (1, 16, 2):
    sumOdd += int(cardNum[i])

  for j in range (0, 16, 2):
    if int(cardNum[j]) == 5:
      sumEven += 1
    elif int(cardNum[j]) == 6:
      sumEven += 3
    elif int(cardNum[j]) == 7:
      sumEven += 5
    elif int(cardNum[j]) == 8:
      sumEven += 7
    elif int(cardNum[j]) == 9:
      sumEven += 9
    else:
      sumEven += (int(cardNum[j]) * 2)

  totalSum = sumEven + sumOdd
  if (totalSum % 10 == 0): 
    return True
  else:
    return False

def generateCard():
  randCard = random.randint(1000000000000000, 9999999999999999)
  while (not checkCard(str(randCard))):
    randCard = random.randint(1000000000000000, 9999999999999999)
  return randCard

print("***********************************")
print("***                             ***")
print("***  Welcome to card services!  ***")
print("***                             ***")
print("***********************************")
print()
print("Choose a service: ")
print("1) Credit Card Validator")
print("2) Credit Card Generator")
choice = input()
choice.lower().replace(" ", "")
arr1 = ["1", "1)", "validator", "creditcardvalidator", "cardvalidator", "creditvalidator"]
arr2 = ["2", "2)", "generator", "creditcardgenerator", "cardgenerator", "creditgenerator"]

if choice in arr1:
    print()
    userCard = input("Please enter your credit card number: ")
    userCard = userCard.replace(" ", "").replace("-", "")
    while (not userCard.isdigit() or len(userCard) != 16):
      print()
      userCard = input("Please enter your card number: ")
      userCard = userCard.replace(" ", "").replace("-", "")
    if (checkCard(userCard)):
      print()
      print("Valid card number")
    else:
      print()
      print("Invalid card number")
else:
    print("Your input was not validated!")
    exit()

print("Generated card: " + str(generateCard()))
