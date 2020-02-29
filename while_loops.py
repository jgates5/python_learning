#for in loop start and finish to looping
#while loop will not end reaching at the end of a list, have to define what that set a setinel value when you tell yu while llop to stop
#nums = list(range(1, 100))

"""
 well the length of nums so the count of the nums list is greater than zero. Then I want you to print nums.pop())
 And what this is going to do is it's going to iterate over and list and it's going to pop an element off it's going to 
 print out that value and if you remember the behavior of the pop function this will also remove the item from the names list. 
 So this is going to create our sentinel value it's going to continually decrease the length of the nums list until it reaches 0 once it reaches that value.
  This condition. So where it says while the length of nums is greater than zero. This is finally going to be false and when it's false the while loop is going to stop.
 """
#while len(nums) > 0:
    #print(nums.pop())


#using a while loop looping continue to guess
def guessing_game():
    while True:
        print('What is your guess?')
        guess = input()

        if guess == '42':
            print('You correctly guessed it!')
            return False
        else:
            print(f'No, {guess} is not the answer, please try again\n')

guessing_game()
