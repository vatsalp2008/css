import random

def custom_hash(input_string):
    hash_value = 0
    
    def is_prime(n):
        if (n<=1): 
            return False
        for i in range(2, (n//2)+1):
            if (n % i) == 0:
                return False
        return True

    def generate_random_prime():
        while True:
            candidate = random.randint(2, 100)
            if is_prime(candidate):
                return candidate
    # random prime numbers
    prime1 = generate_random_prime()
    prime2 = generate_random_prime()
    
    for char in input_string:
        hash_value += ((hash_value >> prime2) + ord(char) * prime1) % (prime1**prime2)
    
    return hash_value

input_string1 = "hello"
input_string2 = "hello"
hashed_value1 = custom_hash(input_string1)
hashed_value2 = custom_hash(input_string2)
print("Hash value for", input_string1, ":", hashed_value1)
print("Hash value for", input_string2, ":", hashed_value2)