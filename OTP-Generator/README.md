# 🔐 OTP Generator

A beginner-friendly Python script that generates a random 4-digit OTP (One-Time Password). This project demonstrates basic Python programming concepts like loops, lists, string manipulation, and randomness.

---

## 📌 Features

- Generates a random 4-digit numeric OTP
- Uses Python’s built-in `random.randint()` function
- Stores individual digits in a list and combines them into a single string
- Simulates sending an OTP via SMS-style console output

---

## 💻 How It Works

1. Random digits (0–9) are generated and stored in a list  
2. Each digit is converted to a string  
3. The strings are joined together to form the OTP  
4. The final OTP is displayed on the screen as if sent via SMS

---

## 🧠 Concepts Used

- `for` loops  
- `random.randint()` for digit generation  
- List and string operations  
- Basic I/O with `print()`

---

## 🚀 Run the Script

Make sure you have Python 3 installed.

```bash
python otp_generator.py
```

Example output:
```
SMS Otp: 3947
```

---

## 📜 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and share it with proper credit.

---

## 🙌 Contributions

Pull requests are welcome!  
You can extend this project by adding:
- 6-digit OTP support
- Expiry timer
- OTP delivery via email (simulation)
- GUI interface using Tkinter or CustomTkinter

---
