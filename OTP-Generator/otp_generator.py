from random import randint  # Import randint to generate random digits

otp = []  # Empty list to store individual digits of the OTP

for i in range(0, 4):  # Loop 4 times to generate a 4-digit OTP
    otp.append(randint(0, 9))  # Append a random digit (0 to 9) to the list

otp_str = ""  # Initialize an empty string to store the full OTP

for i in otp:  # Loop through the list of digits
    otp_str += str(i)  # Convert each digit to string and append to otp_str

print("SMS Otp: ", otp_str)  # Display the generated OTP
