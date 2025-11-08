# 📱 ADB Device Controller 🚀  
> Control your Android device directly from your PC — through simple Python commands powered by ADB!  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![ADB](https://img.shields.io/badge/ADB-Android%20Debug%20Bridge-green?logo=android)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Mac-lightgrey)
![License](https://img.shields.io/badge/License-MIT-orange)

---

## 🧠 Overview  
The **ADB Device Controller** is a **Python-based automation tool** that allows users to control Android devices using ADB (Android Debug Bridge) commands.  
It provides an interactive menu to perform common phone actions like calling, sending messages, adjusting volume/brightness, and even detecting incoming calls — **right from your terminal!**

---

## ✨ Features  

✅ Check connected Android device details  
✅ Open apps like Browser, Contacts, and Email  
✅ Simulate hardware buttons (Home, Back, Enter, Volume, Brightness, etc.)  
✅ Control calls – make, answer, or reject  
✅ Send SMS messages 📩  
✅ Detect incoming calls in real time 🔔  
✅ Lightweight and beginner-friendly  

---

## 🧩 Tech Stack  

| Component | Description |
|------------|-------------|
| 🐍 **Python 3.x** | Core programming language |
| ⚙️ **ADB (Android Debug Bridge)** | Communication layer between PC and Android |
| 🧰 **ppadb** | Python ADB client for advanced device interaction |
| 💻 **OS / RE Modules** | Execute and parse system-level commands |

---

## ⚙️ Installation & Setup  

### 1️⃣ Prerequisites  
Make sure you have the following installed:  
- [Python 3.8+](https://www.python.org/downloads/)  
- [ADB Tools](https://developer.android.com/studio/releases/platform-tools)  
- Android device with **USB Debugging** enabled  

### 2️⃣ Clone the Repository  

git clone https://github.com/<shubhammhaske-6610>/adb-device-controller.git

cd adb-device-controller

3️⃣ Install Required Python Packages
pip install pure-python-adb

4️⃣ Start the ADB Server
adb start-server

5️⃣ Run the Script
python adb-device-controller.py


🧭 Usage Guide

When you run the script, you’ll see an interactive menu like this:
options:
1. Check the device
2. Home Button
3. Back Button
4. Enter
5. Open Browser
6. Contacts
7. Brightness up
8. Brightness down
9. Receiving a call
10. Rejecting a call
11. Open Email
12. Volume up
13. Volume down
14. Notifications
15. Searching
16. Make Outgoing Call
17. Send a Message
18. Incoming Call

💡 Example:

Press 5 → Opens Google in your Android browser 🌐

Press 16 → Dial a number directly from your PC ☎️

Press 18 → Detect incoming call number 📞

🖼️ Demo Preview
Action	Screenshot
📲 Checking device connection	
☎️ Making a call	
💬 Sending message	

🧑‍💻 Author
👨‍💻 Shubham Mhaske
📍 Aspiring Python Developer | Automation Enthusiast | Tech Explorer




🧾 License
This project is licensed under the MIT License — feel free to modify and use it!

⭐ Support
If you like this project, don’t forget to star ⭐ the repository and share it with others!
Your support motivates me to build more awesome open-source tools 💪

💬 “Control your Android — like a pro, right from your terminal!” 🚀
Would you like me to make it **GitHub-optimized with emojis and badges rendered inline (Markdown + HTML hybrid)** for maximum recruiter appeal (i.e., better formatting on your repo page)?  
I can create that next.
