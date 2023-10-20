import random

# Function to generate a random 6-digit OTP
def generate_otp():



    return str(random.randint(181818, 888888)) 
    
       # Function to send the OTP (you can replace this with your own logic)

def send_otp_to_user(otp, user_email):
    print(f"OTP {otp} sent to {user_email}")

# Function to verify the OTP entered by the user
def verify_otp(otp, user_input):
    return otp == user_input                         
    
    
     # Main program

if _name_ == "_main_":

    # Replace 'user_email' with the user's email or phone number
    user_email = input("Enter your email or phone number: ")
    
    # Generate and send OTP to the user
    otp = generate_otp()
    send_otp_to_user(otp, user_email)
    
    # Prompt the user to enter the OTP
    user_input = input("Enter the OTP sent to your email or phone: ")
    
    
    # Verify the OTP
    if verify_otp(otp, user_input):
        print("OTP verification successful. Access granted.")

    else:
        print("OTP verification failed. Access denied.")