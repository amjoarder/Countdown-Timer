import time  # Importing the time module for the sleep function

# Function to perform the countdown
def countdown(t):
    # Loop until the timer reaches zero
    while t:
        # Calculate minutes and seconds from the total time
        mins, secs = divmod(t, 60)  
        
        # Format the timer as MM:SS with leading zeros
        timer = '{:02d}:{:02d}'.format(mins, secs)  
        
        # Print the timer on the same line and overwrite the previous output
        print(timer, end="\r")  
        
        # Wait for 1 second before continuing the loop
        time.sleep(1)  
        
        # Decrease the timer by 1 second
        t -= 1  
    
    # Notify the user when the countdown is complete
    print('Time Completed!')  

# Prompt the user to enter the countdown time in seconds
t = input('Enter the time in seconds: ')

# Call the countdown function with the user-provided time (converted to an integer)
countdown(int(t))
