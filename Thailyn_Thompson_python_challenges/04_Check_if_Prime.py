def is_prime(n):
    if n <= 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    print(is_prime(11))  # Output: True
    print(is_prime(4))   # Output: False
    print(is_prime(1))   # Output: False
    print(is_prime(2))   # Output: False
    