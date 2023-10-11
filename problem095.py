##Problem 95

from timeit import default_timer as timer

def proper_divisors(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    return divisors


# start timer
start = timer()

answer_n = 0 # init to 0


for n in range(1,10**6):
    # test all numbers from 1 to 10^6
    

            
    

print("min:",str(answer_n_by_phi)," - n:",str(answer_n)," - phi(n):",str(answer_phi_n))
end = timer()
print("Runtime: ",str(end-start)," s",sep="")

