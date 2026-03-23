# FizzBuzz Program (1-50) with Count

def check_fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

def run_fizzbuzz():
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0

    for i in range(1, 51):
        result = check_fizzbuzz(i)
        print(result)
        if result == "Fizz":
            fizz_count += 1
        elif result == "Buzz":
            buzz_count += 1
        elif result == "FizzBuzz":
            fizzbuzz_count += 1

    print("\n--- Count Summary ---")
    print("Fizz Count:", fizz_count)
    print("Buzz Count:", buzz_count)
    print("FizzBuzz Count:", fizzbuzz_count)

run_fizzbuzz()
