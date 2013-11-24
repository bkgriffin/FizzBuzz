#!/usr/bin/python
#
# author: Brandon Griffin <brandon.k.griffin@gmail.com>
# ver:    0.1
# date:   11/24/13

class FizzBuzz:
    """
    FizzBuzz class.
    Tests numbers for Fizz/Buzz.
    Contains Fizz/Buzz attributes.
    """
    # FizzBuzz attributes.
    Fizz = 'Fizz'
    Buzz = 'Buzz'
    
    # If a number is a fizz if it's a multiple of 3.
    def IsFizz(self, number):
        if number % 3 == 0:
            return True
        else:
            return False

    # If a number is a buzz if it's a multiple of 5.
    # Print "Buzz" if the number is a fizz.
    def IsBuzz(self, number):
        if number % 5 == 0:
            return True
        else:
            return False

# Main entry point.
def main():
    fizzBuzzer = FizzBuzz()
    for i in xrange(1, 101):
        IsNumberFizz = fizzBuzzer.IsFizz(i)
        IsNumberBuzz = fizzBuzzer.IsBuzz(i)
        if IsNumberFizz and IsNumberBuzz:
            print (str(i) + ': ' + fizzBuzzer.Fizz + fizzBuzzer.Buzz)
        elif IsNumberFizz:
            print (str(i) + ': ' + fizzBuzzer.Fizz)
        elif IsNumberBuzz:
            print (str(i) + ': ' + fizzBuzzer.Buzz)
        else:
            print (str(i) + ':')

if __name__ == "__main__":
    main()