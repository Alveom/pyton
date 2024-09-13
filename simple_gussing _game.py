import random 

def generating(max_number,low_number):
    random_number = random.randint(low_number,max_number)
    return random_number

def user_input():
    max_number = input("Enter the max number: ")
    low_number = input('Enter the low number: ')
    user_guess = input('Enter your guess: ')
    if max_number.isdigit() and low_number.isdigit() and user_guess.isdigit():
        max_number = int(max_number)
        low_number = int(low_number)
        user_guess = int(user_guess)
        return max_number , low_number,user_guess
    else :
        print('INVAID! input try again ')
        return user_input()

def main():
    
    max_number, low_number, user_guess =  user_input()
   
    i = 0 
    
    computer_guess_list = []
    while True : 
        random_number = generating(max_number , low_number)
        i += 1 
        print(i, random_number)
        computer_guess_list.append(random_number)
        if random_number == user_guess:
            
            print(f'We found your guess at {i}. tries. Your guess was {user_guess}' )
            break
            
    print(len(computer_guess_list))
    print(computer_guess_list)



if __name__ == "__main__":
    main()