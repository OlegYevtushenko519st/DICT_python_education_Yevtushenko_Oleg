import random


def main():
  friends_number = int(input("Enter the number of friends joining (including you): "))
  if friends_number <= 0:
    print("No one is joining for the party")
    return
  friends = {}
  for i in range(friends_number):
    name = input("Enter the name of every friend (including you), each on a new line: ")
    friends[name] = 0
  total_amount = float(input("Enter the total amount: "))
  lucky_friend = None
  if input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No: ") == "yes":
    lucky_friend = get_random_friend(friends)
    friends[lucky_friend] = 0
  for friend, amount in friends.items():
    if lucky_friend is not None and friend == lucky_friend:
      continue
    if lucky_friend is not None:
      friends[friend] = round(total_amount / (friends_number - 1), 2)
    else:
      friends[friend] = round(total_amount / friends_number, 2)
  print(friends)


def get_random_friend(friends):
  return list(friends.keys())[random.randint(0, len(friends) - 1)]


if __name__ == "__main__":
  main()