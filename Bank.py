balance = []
balanceTotal = 0
draft = []
limit = 500
draftLimit = 3

while True:
  print("[1] - Deposit\n[2] - Draft\n[3] - Statement\n[0] - Exit\n")
  menu = input()

  if menu == "1":
    value = float(input("Insert value for Deposit: \n"))
    if value > 0:
      balance.append(value)
      balanceTotal = sum(balance)
      print(f"Deposit made! Your current balance is: R${balanceTotal:.2f}\n")
    else:
      print("Operation unavailable\n")

  elif menu == "2":
    if draftLimit <= 0:
      print("Draft limit reached. Operation unavailable.\n")
    elif draftLimit > 0:
      value = float(input("Insert value for Draft: \n"))

      if value > 0 and value <= 500:
        if balanceTotal == 0 or balanceTotal < value:
          print("Insufficient funds.\n")
        else:
          draft.append(value)
          balanceTotal -= value
          draftLimit -= 1
          print(f"Your current balance is: R${balanceTotal:.2f}\n")
          if draftLimit == 0:
            print("You reached your daily draft limit.")
          else:
            print(f"You can make this operation only {draftLimit} more times")
      else:
        print("Operation unavailable")

  elif menu == "3":

    print("STATEMENT\n")

    if len(balance) > 0:
      print("DEPOSIT HISTORY\n")
      for i in range(len(balance)):
        print(f"Deposit number #{i + 1}: R${balance[i]:.2f}")
        print()

    if len(draft) > 0:
      print("DRAFT HISTORY\n")
      for i in range(len(draft)):
        print(f"Draft number #{i + 1}: R${draft[i]:.2f}")
        print()

    if len(draft) == 0 and len(balance) == 0:
      print("HISTORY UNAVAILABLE\n")

    print(f"Your current balance is: R${balanceTotal:.2f}")

  elif menu == "0":
    break

  else:
    print("Unavailable Operation. Try again!")
