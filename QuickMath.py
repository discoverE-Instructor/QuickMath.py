import random

while (True):
    ####################################################################################
    ### DEV VARIABLE: change this to allow for different amount of numbers for the game
    HOW_MANY_NUMBERS = 6
    ####################################################################################


    original_numbers = [ i for i in input('Enter ' + str(HOW_MANY_NUMBERS) + ' small numbers: ').split() ]
    # Ask again if it was not exactly four numbers
    while not len(original_numbers) == HOW_MANY_NUMBERS:
        original_numbers = [ i for i in input('Enter ' + str(HOW_MANY_NUMBERS) + ' small numbers: ').split() ]

    # Randomly position the numbers in the array
    random.shuffle(original_numbers)
    numbers = original_numbers[:]   # Create a shallow copy of the numbers

    nsize = len(original_numbers)
    randbrac = random.randrange(0,HOW_MANY_NUMBERS//2+1)  # Add brackets depending on the amount of numbers
    for i in range(randbrac):
        index = random.randrange(0,nsize-1)
        numbers[index] = '(' + numbers[index]
        index2 = random.randrange(index+1, nsize)
        numbers[index2] = numbers[index2] + ')'

    increment = 1
    for i in range(nsize-1):
        randop = random.randrange(0,2)
        if(randop == 0):
            numbers.insert(i+increment, '+')
        else:
            numbers.insert(i+increment, '*')
        increment += 1
        nsize += 1

    ans1 = ' '.join(numbers)
    ans2 = eval(ans1)

    response=''
    response2=''

    while response2!='0':
        response = ''
        print('Try and guess the Target Number using  +  *  (  )  along with your Numbers')
        print('Target Number: ' + str(ans2))
        response = input('Your answer: ')
        eval_response = ''
        try:
            eval_response = eval(response)
        except Exception as e:
            print('Invalid input:', e)
            continue  # Cut this iteration of the loop to ask for the eval response again

        if(eval_response == ans2):
            test = response.split("+")
            test = ' '.join(test).split("*")
            test = ' '.join(test).split("(")
            test = ' '.join(test).split(")")
            test = ' '.join(test).split(" ")
            test = [i for i in test if not i == '' ]
            error = False
            for i in test:
                if i not in original_numbers:
                    error = True
                    break
                test.remove(i)

            if not error:
                print("Correct!")
                break
            else:
                print("Wrong Numbers. Try again.")
        else:
            response2 = input("Incorrect. Would you like to keep trying (No, Yes)? ")
            if response2 == '0' or response2 == 'n' or response2 == 'N' or response2 == 'No' or response2 == 'no' or response2 == 'NO':
                break
            else:
                hresponse = input("Would you like a hint (No, Yes)? ")
                if hresponse == '0' or hresponse == 'n' or response2 == 'N' or hresponse == 'No' or hresponse == 'no' or hresponse == 'NO':
                    continue
                else:
                    hint = 'Hint! The order of the numbers should follow: ' + ' '.join(map(str, original_numbers))
                    print(hint)

    print("Solution: " + ans1)
    print('-'*64)
