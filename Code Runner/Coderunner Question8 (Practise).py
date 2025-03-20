cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

card = input('Enter a card: ')
while card in cards:
  print("That's a playing card!")
  card = input('Enter a card: ')
while card not in cards:
    print("That's not a playing card!")
    break