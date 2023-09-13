from itertools import combinations

def main():
  values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
  suits = ['C', 'D', 'H', 'S']
  cards = [(v, s) for v in values for s in suits]

  counts = {
      "Royal flush": 0,
      "Straight flush": 0,
      "Four of a kind": 0,
      "Full house": 0,
      "Flush": 0,
      "Straight": 0,
      "Three of a kind": 0,
      "Two pair": 0,
      "One pair": 0,
      "Nothing": 0,
      "Total": 0,
  }

  # Generate all combinations of 5 cards
  for hand in combinations(cards, 5):
    values = [v for v, _ in hand]
    suits = [s for _, s in hand]
    values.sort()

    # Determine what combination the hand qualifies for
    combos = {}
    combos["Royals"] = values == [10, 11, 12, 13, 14]
    combos["Four of a kind"] = isFourOfAKind(values)
    combos["Full house"] = isFullHouse(values)
    combos["Flush"] = isFlush(suits)
    combos["Straight"] = isStraight(values)
    combos["Three of a kind"] = isThreeOfAKind(values)
    combos["Two pair"] = isTwoPair(values)
    combos["One pair"] = isPair(values)

    # Using the qualified combinations, check them in order and increment the count
    # of the highest possible value
    if combos["Royals"] and combos["Flush"]:
      counts["Royal flush"] += 1
    elif combos["Straight"] and combos["Flush"]:
      counts["Straight flush"] += 1
    elif combos["Four of a kind"]:
      counts["Four of a kind"] += 1
    elif combos["Full house"]:
      counts["Full house"] += 1
    elif combos["Flush"]:
      counts["Flush"] += 1
    elif combos["Straight"]:
      counts["Straight"] += 1
    elif combos["Three of a kind"]:
      counts["Three of a kind"] += 1
    elif combos["Two pair"]:
      counts["Two pair"] += 1
    elif combos["One pair"]:
      counts["One pair"] += 1
    else:
      counts["Nothing"] += 1
 
  # Calculate the total number of hands
  for key, value in counts.items():
    if key != "Total":
      counts["Total"] += value

  # Print the results
  print("Royal flush:", counts["Royal flush"])
  print("Straight flush:", counts["Straight flush"])
  print("Four of a kind:", counts["Four of a kind"])
  print("Full house:", counts["Full house"])
  print("Flush:", counts["Flush"])
  print("Straight:", counts["Straight"])
  print("Three of a kind:", counts["Three of a kind"])
  print("Two pair:", counts["Two pair"])
  print("One pair:", counts["One pair"])
  print("Nothing:", counts["Nothing"])
  print("Total:", counts["Total"])

def isFlush(suits):
  # Suits should only have 1 unique value
  return len(set(suits)) == 1

def isStraight(values):
  # The values are sorted, so the difference between the largest and smallest
  # values should be 4, and there should be no duplicates
  # The second condition is for the special case of A2345
  return (
     ((values[4] - values[0] == 4) and (len(set(values)) == 5))
     or (values == [2, 3, 4, 5, 14])
  )

def isPair(values):
  # There should be 4 unique values, this means exactly 1 of them is a duplicate
  return len(set(values)) == 4

def isTwoPair(values):
  # There should be 3 unique values, and at least 1 of them should be a duplicate
  # If 1 is a duplicate, there are 3 cards that are 2 unique values
  # We can safely assume that 1 other one is a duplicate
  if len(set(values)) == 3:
      for value in values:
          if values.count(value) == 2:
              return True
  return False

def isThreeOfAKind(values):
  # There should be 3 unique values, and at least 1 of them should be a triplicate
  if len(set(values)) == 3:
      for value in values:
          if values.count(value) == 3:
              return True
  return False
            
def isFourOfAKind(values):
  # There should be 2 unique values, and at least 1 of them should be a quadruplicate
  if len(set(values)) == 2:
      for value in values:
          if values.count(value) == 4:
              return True
  return False

def isFullHouse(values):
  # There should be 2 unique values, and at least 1 of them should be a triplicate
  # If 1 is a triplicate, and there's only 1 unique value remaining, we can safely assume it's a duplicate
  if len(set(values)) == 2:
      for value in values:
          if values.count(value) == 3:
              return True
  return False

if __name__ == "__main__":
    main()