def fibonacci_sequence(i):
    if i <= 1:
        return(fibonacci_sequence(i-1) + (fibonacci_sequence(i-2)))
    
