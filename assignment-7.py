def is_prime(num):
  """Checks if a number is prime."""
  if num <= 1:
    return False
  if num <= 3:
    return True
  if num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
  return True

def main():
  name = input("What's your name? ")
  print(f"Salam, {name}!")

  numbers = []
  for i in range(3):
    number = int(input(f"Enter your {i + 1} favorite number: "))
    numbers.append(number)

  number_parity = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]

  print("\nLet's explore your numbers!")
  print("Number\tSquare")
  for num in numbers:
    print(f"{num}\t{num * num}")

  sum_of_numbers = sum(numbers)
  print(f"\nThe sum of your numbers is {sum_of_numbers}. Keep exploring!")

  if is_prime(sum_of_numbers):
    print("Your sum is a prime number! That's pretty cool.")
  else:
    print("Your sum is not a prime number, but it's still a unique number.")

if __name__ == "__main__":
  main()