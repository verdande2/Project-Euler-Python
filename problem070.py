##Problem 70

from timeit import default_timer as timer

def phi(n):
    result = n  # Initialize the result with n
    
    # Iterate through all prime factors of n
    p = 2
    while p * p <= n:
        # If p is a prime factor of n
        if n % p == 0:
            # Subtract multiples of p from result
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    
    # If n is a prime number greater than 1
    if n > 1:
        result -= result // n
    
    return result


def are_permutations(num1, num2):
    # Convert numbers to strings and sort the characters
    num1_str = sorted(str(num1))
    num2_str = sorted(str(num2))
    
    # Compare sorted strings
    return num1_str == num2_str


# start timer
start = timer()

answer_n = 0 # init to 0
answer_n_by_phi = 123456789 # something large so that we can find a min
answer_phi_n = 0

for n in range(2,10**7):
    phi_n = phi(n)
    
    if are_permutations(n,phi_n):
        #print("PERMUTATIONS: ",str(n),": totient=",str(phi_n))
        #print("n:",str(n),"n/phi_n:",str(n/phi_n))
        if n/phi_n < answer_n_by_phi:
            answer_n = n
            answer_phi_n = phi_n
            answer_n_by_phi = n/phi_n
            print("hit!! new low!",str(answer_n_by_phi),"n:",str(answer_n)," - phi(n):",str(answer_phi_n))
            
    

print("min:",str(answer_n_by_phi)," - n:",str(answer_n)," - phi(n):",str(answer_phi_n))
end = timer()
print("Runtime: ",str(end-start)," s",sep="")

