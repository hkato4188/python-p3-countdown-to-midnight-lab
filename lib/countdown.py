from time import sleep

def countdown(integer):

    while integer:
        print(f'{integer} SECOND(S)!')
        integer -= 1

    print('HAPPY NEW YEAR!')

def countdown_with_sleep(integer):

    while integer:
        print(f'{integer} SECOND(S)!')
        integer -= 1
        sleep(1)

    print('HAPPY NEW YEAR!')