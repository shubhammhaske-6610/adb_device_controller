import os
import re
from ppadb.client import Client as AdbClient  # Used to communicate with Android devices via ADB

# Display the available options for user interaction
print("\noptions:")
print("1. Check the device")
print("2. Home Button")
print("3. Back Button")
print("4. Enter")
print("5. Open Browser")
print("6. Contacts")
print("7. Brightness up")
print("8. Brightness down")
print("9. Receiving a call")
print("10. Rejecting a call")
print("11. Open Email")
print("12. Volume up")
print("13. Volume down")
print("14. Notifications")
print("15. Searching")
print("16. Make Outgoing Call")
print("17. Send a Message")
print("18. Incoming Call")

# Infinite loop to keep the menu running until user chooses to exit
while True:
    choice = int(input("Enter the choice: "))

    # 1. Check connected device model
    if choice == 1:
        print("Checking device...")
        os.system("adb shell getprop ro.product.model")

    # 2. Simulate Home button press
    elif choice == 2:
        os.system("adb shell input keyevent 3")

    # 3. Simulate Back button press
    elif choice == 3:
        os.system("adb shell input keyevent 4")

    # 4. Simulate Enter key press
    elif choice == 4:
        os.system("adb shell input keyevent 66")

    # 5. Open a web browser (Google as default)
    elif choice == 5:
        os.system("adb shell am start -a android.intent.action.VIEW -d http://www.google.com")

    # 6. Open Contacts app
    elif choice == 6:
        os.system("adb shell input keyevent 207")

    # 7. Increase screen brightness
    elif choice == 7:
        os.system("adb shell input keyevent 221")

    # 8. Decrease screen brightness
    elif choice == 8:
        os.system("adb shell input keyevent 220")

    # 9. Simulate answering an incoming call
    elif choice == 9:
        os.system("adb shell input keyevent 5")  # KEYCODE_CALL

    # 10. Simulate rejecting or ending a call
    elif choice == 10:
        os.system("adb shell input keyevent 6")  # KEYCODE_ENDCALL

    # 11. Open Email app
    elif choice == 11:
        os.system("adb shell input keyevent 65")

    # 12. Increase device volume
    elif choice == 12:
        os.system("adb shell input keyevent 24")

    # 13. Decrease device volume
    elif choice == 13:
        os.system("adb shell input keyevent 25")

    # 14. Open the notifications panel
    elif choice == 14:
        os.system("adb shell input keyevent 83")

    # 15. Open the search function
    elif choice == 15:
        os.system("adb shell input keyevent 84")

    # 16. Make an outgoing call to the entered number
    elif choice == 16:
        a = input("Enter a number starting with +91: ")
        os.system(f"adb shell am start -a android.intent.action.CALL -d tel:{a}")

    # 17. Send an SMS message to a specific number
    elif choice == 17:
        a = input("Enter a number starting with +91: ")
        b = input(f"Enter a message to send to {a}: ")
        # The message is wrapped in quotes to handle spaces
        os.system(f'adb shell am start -a android.intent.action.SENDTO -d sms:{a} --es sms_body "{b}" --ez exit_on_sent true')

    # 18. Detect if there’s an incoming call and display the number
    elif choice == 18:
        client = AdbClient(host="127.0.0.1", port=5037)  # Connect to ADB server
        devices = client.devices()

        if not devices:
            print("No device connected.")
        else:
            device = devices[0]
            # Extract telephony info from the device
            info = device.shell("dumpsys telephony.registry")
            match = re.search(r"mCallIncomingNumber=\+?\d+", info)

            # If an incoming call is found, print the number
            if match:
                number = match.group().split('=')[1]
                print("Incoming number:", number)
            else:
                print("No incoming call.")

    # If the user enters an invalid choice, exit the loop
    else:
        print("Invalid choice. Exiting...")
        break
