spam_amount = 0
print(spam_amount);
spam_amount = spam_amount+4
if spam_amount > 0:
    print("But I don't want to any spam!")
    viking_song = "Spam " * spam_amount; #Spam is written four times
    print(viking_song);
    A = "NO WAY!"
    print(A);
    print(type(spam_amount)); #int (integer the number-based type)
    print(type(A));
    print(type(viking_song)); #str (string the text-based type)
    print(type(19.95)) #float (float the decimal-based type)
    
    # Operators in Python Quickly
    # + (Addition)
    print(3+5);
    # - (Subtraction)
    print(26-16);
    # * (Multiplication)
    print(4*9);
    # / (True Division) [Quotient of a and b]
    print(68/38);
    # // (Floor Division) [Quotient of a and b, removing fractional parts]
    print(1560//572);
    # % (Modulus) [Integer remainder after division of a by b]
    print(47%23);
    # ** (Exponentiation) [a raised to the power of b]
    print(2**10);
    # -a (Negation) [The negative of a]
    print(-5)
    
    #PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction.
    #Python follows similar rules about which calculations to perform first.
    nose_height = 3;
    body_height = 176;
    power_of_human = (body_height // nose_height) % 3 
    print("The your sacred power blessed by ", power_of_human, " king!" )
    
    #min and max return the minimum and maximum of their arguments, respectively...
    print(min(38,34,70))
    print(max(26,13,48))
    
    #abs returns the absolute value of an argument
    print(abs(-47))
    print(abs((-2^7)//5))
    
    #In addition to being the names of Python's two main numerical types, int 
    #and float can also be called as functions which convert their arguments to
    #the corresponding type:
    print(float(24));
    print(int(7.47));
    print(int('30')+2)
    
    #Question 2
    x = [1, 2, 3]
    y = [3, 2, 1] #make the orders same for a & b such as 1,2,3 for both
    tmp = x
    x = y
    y = tmp
    print(x)
    print(y)
    
    #Question 4
    alice_candies = 121
    bob_candies = 77
    carol_candies = 109
    to_smash = (alice_candies + bob_candies + carol_candies)% 3 