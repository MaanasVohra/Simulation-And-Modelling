"""
    Finding the root of polynomial using bisection method
"""

def take_polynomial_input():
    n_term = int(input('Enter highest coefficient '))
    coeff = []
    for i in range(n_term + 1) :
        coeff_i = float(input('Enter coefficient for power {} '.format(i)))
        coeff.append(coeff_i)
    return coeff

def value_of_polynomial(input_val, polynomial_coeff) :
    value = 0
    
    for i in range(len(polynomial_coeff)) :
        value += (input_val ** i) * (polynomial_coeff[i])

    return value

def main():
    polynomial_coeff = take_polynomial_input()
    
    eps = 1e-03
    lower_limit = float(input('Enter lower limit '))
    upper_limit = float(input('Enter upper limit '))

    value_lower_limit = value_of_polynomial(lower_limit, polynomial_coeff)
    value_upper_limit = value_of_polynomial(upper_limit, polynomial_coeff)
    value =  value_lower_limit * value_upper_limit
            
    if(value > 0): 
        raise Exception('The value has to be negative in order to solve using bisection method')

    while(upper_limit - lower_limit >= eps) :
        print("Current range is [{}, {}]".format(lower_limit, upper_limit))

        mid_ele = (upper_limit + lower_limit) / 2.0
        mid_ele_val = value_of_polynomial(mid_ele, polynomial_coeff)

        if(mid_ele_val == 0) :
            ans = mid_ele_val
            break
        
        elif(mid_ele_val > 0) :
            upper_limit = mid_ele
        
        else:
            lower_limit = mid_ele

    ans = (upper_limit + lower_limit) / 2.0
    print("The answer is {}".format(ans))
    print("Value at {} is {}".format(ans, value_of_polynomial(ans, polynomial_coeff)))

if __name__ == "__main__" :
    main()