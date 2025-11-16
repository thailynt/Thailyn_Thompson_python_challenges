def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read().lower()
        words = text.split()
        frequency = {}
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1
    return frequency


from datetime import datetime
def write_log():
    message = input("Enter message: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as log_file:
        file.write(timestamp + message + "\n")

        def calculator():
            operation = input("Enter operation (+, -, *, /): ")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if operation == '+':
                return num1 + num2
            elif operation == '-':
                return num1 - num2
            elif operation == '*':
                return num1 * num2
            elif operation == '/':
                return num1 / num2
            else:
                return "Invalid operation"
            print(f"Result: {calculator()}")

            def check_password_strength(password):
                length = len(password) >= 8
                upper = any(c.isupper() for c in password)
                lower = any(c.islower() for c in password)
                digit = any(c.isdigit() for c in password)
                special = any(not c.isalnum() for c in password)
                return length and upper and lower and digit and special
            print(check_password_strength("Password123!"))  # Output: True
            print(check_password_strength("weakpass"))      # Output: False 

            fo i in range(1, 101):
            output = ""
            if i % 3 == 0:
                output += "Fizz"
            if i % 5 == 0:
                output += "Buzz"
            print(output or i)  


