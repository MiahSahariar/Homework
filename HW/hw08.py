def locateEvenNumbers(limit):
    even_number = []
    number = 2
    
    while number <= limit:
        even_number.append(number)
        number += 2
        
    return even_number

def sum_even_numbers(even_numbers):
    return sum(even_numbers)

def main():
    limit = 100
    even_number = locateEvenNumbers(limit)
    totalSum = sum_even_numbers(even_number)
    
    print("Even numbers up to", limit, ":", even_number)
    print("Sum of even numbers:", totalSum)
    
