def fizz_buzz(input):
    if int(input)%3==0 and int(input)%5==0:
        return 'fizzbuz'
    if int(input)%3==0 :
        return 'fizz'
    if int(input)%5==0 :
        return'buzz'
    return input


print(fizz_buzz(15))