import random
def hashing(input_str):
    hash_val = 0
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2,num//2 + 1):
            if (num % i == 0):
                return False
        return True
    
    def generate_prime_num():
        while True:
            candidate = random.randint(2,100)
            if (is_prime(candidate)):
                return candidate
    
    prime1 = generate_prime_num()
    prime2 = generate_prime_num()

    for char in input_str:
        hash_val += ((hash_val >> prime2)+ ord(char)*prime1) % (prime1**prime2)
    return hash_val

print(hashing("helllooo"))