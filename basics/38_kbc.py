questions = [
  ["Who is the best football Player of all time?", "Ronaldo" , "Messi","Neymar","Zlatan", 1],
  ["Who is the best football Player of all time?", "Ronaldo" , "Messi","Neymar","Zlatan", 1],
  ["Who is the best football Player of all time?", "Ronaldo" , "Messi","Neymar","Zlatan", 1],
  ["Who is the best football Player of all time?", "Ronaldo" , "Messi","Neymar","Zlatan", 1]]
Levels = [10000,15000,30000,50000]
money = 0
for i in range(0,len(questions)) :
  print(f"\nYour {i+1} question for {Levels[i]} is :")
  print(f"{questions[i][0]}\n")
  print(f" 1){questions[i][1]}      2){questions[i][2]}")
  print(f" 3){questions[i][3]}      4){questions[i][4]}")
  reply = int(input("Choose Any option :"))
  if reply == questions[i][-1]:
    print(f"\nCongratulations!! {reply} is the crct answer.")
    money = Levels[i]
    print(f"You have won Rs.{money}.")
  else:
    print("Oops,that\'s the Wrong Answer.\n")
    print(f"You stil win Rs.{money}.")
    