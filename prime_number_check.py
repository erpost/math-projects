def is_prime(number):
    if number == 1:
        print('{} is not a prime number'.format(number))
        exit(0)

    for n in range(2, number):
        modulus = number % n
        print('Modulus of {} / {} = {}'.format(number, n, modulus))
        if modulus == 0:
            print('{} is not a prime number'.format(number))
            exit(0)
    print('{} is a prime number'.format(number))


if __name__ == "__main__":
    number = int(input('What is the number to check for prime: '))
    is_prime(number)
