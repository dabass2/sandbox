import random
# print('--- Welcome to High-Low ---\n Start with 100 points. Each round a card will be drawn and shown.\n Select whether you think the 2nd card will be Higher or Lower than the 1st card.\n Then enter the amount you want to bet.If you are right, you win the amount you bet, otherwise you lose.\n Try to make it to 500 points within 10 tries.\n -------------------------')

def getCardValue():
  return random.randint(2, 14)

def getCardStr(cardValue):
  if cardValue < 10:
    return str(cardValue)
  elif cardValue == 10:
    return "T"
  elif cardValue == 11:
    return "J"
  elif cardValue == 12:
    return "Q"
  elif cardValue == 13:
    return "K"
  elif cardValue == 14:
    return "A"

def getHLGuess():
    while True:
      ans = input('High or Low (H/L)?: ')
      if ans == "l" or ans == "L":
        return "LOW"
      elif ans == "h" or ans == "H":
        return "HIGH"

def getBetAmount(ipoints):
  while True:
    try:
      maximum = int(input('Input bet amount: '))
      if 0 < maximum < ipoints+1:
          return maximum
      raise ValueError()
    except ValueError:
      continue

def playerGuessCorrect(card1, card2, betType):
  return betType == "HIGH" and card2 > card1 or betType == "LOW" and card2 < card1

def game():
  ipoints = 100
  rounds = 0
  while rounds < 10 and ipoints > 0:
    card1 = getCardValue()
    card2 = getCardValue()
    while card2 == card1:
      card2 = getCardValue()
    print('OVERALL POINTS:', ipoints)
    print(f'First card is a {getCardStr(card1)}')
    guess = getHLGuess()
    bet = getBetAmount(ipoints)
    print(f'Second card is a {getCardStr(card2)}')
    result = playerGuessCorrect(card1, card2, guess)
    if result:
      ipoints += bet
    else:
      ipoints -= bet
    print(f"You were {'correct' if result else 'wrong'}.\n")
    rounds += 1
  print(f"Game over, your final score is {ipoints}")

def tic():
  board = {0: '-',1: '-',2: '-',
         3: '-',4: '-',5: '-',
         6: '-',7: '-',8: '-'}
  count = 1
  for k,v in board.items():
    print(v, end="")
    if count == 3:
      count = 0
      print("")
    count += 1

if __name__ == "__main__":
  tic()