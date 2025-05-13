import secrets

def generate_random(min, max):
    return secrets.randbelow(max - min + 1) + min

# Usage:
print(generate_random(5, 10))
print(generate_random(5, 10))
print(generate_random(5, 10))
print(generate_random(5, 10))
print(generate_random(5, 10))
print(generate_random(5, 10))