import os

def INR_TO_NPR():
    os.system('cls')
    print("Currency Exchange\n")
    print("\tINR to NPR")
    inr=int(input("Enter INR:Rs "))
    print("NPR =Rs",end=" ")
    print(inr*1.6)
    inputss=input("\nDO Again or Not: ")
    if inputss=='DO' or inputss=='do':
        INR_TO_NPR()
    else:
        main()

def NPR_TO_INR():
    os.system('cls')
    print("Currency Exchange\n")
    print("\tNPR to INR")
    npr=int(input("Enter NPR:Rs "))
    print("INR =Rs",end=" ")
    print(npr/1.6)
    inputss=input("\nDO Again or Not: ")
    if inputss=='DO' or inputss=='do':
        NPR_TO_INR()
    else:
        main()


def USD_TO_NPR():
    os.system('cls')
    print("Currency Exchange\n")
    print("\tUSD to NPR")
    usd=int(input("Enter USD:$ "))
    print("NPR =Rs",end=" ")
    print(usd*119)
    inputss=input("\nDO Again or Not: ")
    if inputss=='DO' or inputss=='do':
        USD_TO_NPR()
    else:
        main()


def NPR_TO_USD():
    os.system('cls')
    print("Currency Exchange\n")
    print("\tNPR to USD")
    npr=int(input("Enter NPR:Rs "))
    print("USD =$",end=" ")
    print(npr/119)
    inputss=input("\nDO Again or Not: ")
    if inputss=='DO' or inputss=='do':
        NPR_TO_USD()
    else:
        main()


def NPR_TO_AUD():
    os.system('cls')
    print("Currency Exchange\n")
    print("\tNPR to AUD")
    npr=int(input("Enter NPR:Rs "))
    print("AUD =$",end=" ")
    print(npr/88)
    inputss=input("\nDO Again or Not: ")
    if inputss=='DO' or inputss=='do':
        NPR_TO_AUD()
    else:
        main()



def AUD_TO_NPR():
    os.system('cls')
    print("Currency Exchange\n")
    print("\tAUD to  NPR")
    aud=int(input("Enter AUD:$ "))
    print("NPR =Rs",end=" ")
    print(aud*88)
    inputss=input("\nDO Again or Not: ")
    if inputss=='DO' or inputss=='do':
        INR_TO_NPR()
    else:
        main()

 
 
def main():
  os.system('cls')
  print("Currency Exchange\n")
  print("1.INR to NPR")
  print("2.NPR to INR")
  print("3.USD to NPR")
  print("4.NPR to USD")
  print("5.NPR to AUD")
  print("6.AUD to  NPR")
  print("7.Exit")
  inputs = input("select your option:")
  if (inputs =="1"):
      INR_TO_NPR()
  elif(inputs=='2'):
      NPR_TO_INR()
  elif(inputs=="3"):
      USD_TO_NPR()
  elif(inputs=='4'):
      NPR_TO_USD()
  elif(inputs=='5'):
      NPR_TO_AUD()
  elif(inputs == '6'):
      AUD_TO_NPR()
  elif(inputs=='7'):
      os.system("cls")
      print("Currency Exchange\n")
      print("Thank you for using this Software.")
  else:
      print("wrong option.")
      main()
  
 
main()