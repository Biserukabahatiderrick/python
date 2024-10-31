numbers=[2,5,6,7,8,9,10]

def sum_odd_even(numbers):
    odd_sum=0
    even_sum=0
    for num in numbers:
        if num%2==0:
            even_sum+=num
        else:
            odd_sum+=num
    return(even_sum,odd_sum)   
print(sum_odd_even(numbers))

