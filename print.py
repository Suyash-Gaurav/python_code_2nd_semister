
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_cunningham_chain(start, step, length):
    chain = []
    current = start
    while len(chain) < length:
        if is_prime(current):
            chain.append(current) # appends adds the value of current in chain
        current += step
    return chain

# Example usage
start_prime = 7  # Starting prime number
step = 4  # Step size
chain_length = 5  # Length of the chain
cunningham_chain = find_cunningham_chain(start_prime, step, chain_length)
print(cunningham_chain)