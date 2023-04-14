def my_country(country="Kenya"):
    print(f"Hello from {country}")

def great(*names):
    for name in names:
        print(f"Hello {name}")

def sum(*numbers):
    output=0
    for number in numbers:
        output+=number
    return output

# A function named concatenate_args that takes any number of string arguments
# in positional arguments format and concatenates them into a single string

def concatenate_args(*names):
    single = " "
    for name in names:
        single+=name
    return single
    
# A function named concatenate_kwargs that takes any number of string arguments
#  in keyword arguments  format and concatenates them into a single string

def concatenate_kwargs(**digits):
    answer = ""
    for key,value in digits.items():
        answer += values
    return answer
