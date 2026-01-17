import random
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()

a=10000

def send_otp(receiver_email, otp):
    sender_email = os.getenv("EMAIL")
    sender_password = os.getenv("PASSWORD")

    message = f"Subject: OTP Verification\n\nYour OTP for verification is: {otp}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()

while True:
    print("- Enter 1 for deposit.\n- Enter 2 for Withdrawl.\n- Enter 3 for Balance Check.\n")
    n=int(input("Enter a number: "))

    if(n==1):
     # User se email input 
        user_email = input("Enter your email: ")

     # OTP generate (6 digit)
        otp = random.randint(100000, 999999)

        send_otp(user_email, otp)

        print("OTP sent successfully to your email!")
        
        user_otp = int(input("Enter OTP: "))
        if user_otp == otp:
            print("OTP Verified ✅")
            deposit = float(input("Enter the amount for deposit: "))
            a += deposit
            print("New Balance:", a)
        else:
            print("Invalid OTP ❌")

    elif(n==2):
        user_email = input("Enter your email: ")

        otp = random.randint(100000, 999999)

        send_otp(user_email, otp)

        print("OTP sent successfully to your email!")
        user_otp = int(input("Enter OTP: "))
        if user_otp == otp:
            print("OTP Verified ✅")
            withdraw = float(input("Enter the amount for withdrawl: "))

            if withdraw > a:
               print("Insufficient Balance.")
            else:
               a -= withdraw
               print("New Balance:", a)
        else:
            print("Invalid OTP ❌")
        
    elif(n==3):
      user_email = input("Enter your email: ")
      otp = random.randint(100000, 999999)
      send_otp(user_email, otp)

      print("OTP sent successfully to your email!")
      user_otp = int(input("Enter OTP: "))

      if user_otp == otp:
        print("OTP Verified ✅")
        print("Balance:", a)
      else:
        print("Invalid OTP ❌")
    else:
        print("Invalid Arguments")

