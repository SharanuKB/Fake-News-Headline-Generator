# Fake-News-Headline-Generator
# 📰 Fake News Headline Generator

A simple Python project that generates random "Breaking News" headlines using subjects, actions, and places.

---

## 🚀 Features
- Random headline generation  
- Uses Python `random` module  
- Beginner-friendly  
- Runs continuously or with user input  

---

## 📂 Project Structure
Fake-News-Headline-Generator/
│── Fake News Generator.py
│── README.md

---

## 🛠️ Requirements
- Python 3.x  

---

## ⚙️ Installation

1. Clone the repository  
git clone https://github.com/your-username/Fake-News-Headline-Generator.git  

2. Go to project folder  
cd Fake-News-Headline-Generator  

---

## ▶️ How to Run
python "Fake News Generator.py"  

---

## 💻 Example Output
Breaking News: Student discovers a secret at the airport  

Do you want to generate another headline? (yes/no): yes  

Breaking News: Teacher wins a lottery in a small village  

Do you want to generate another headline? (yes/no): no  

Thank you for watching, have a fun day!  

---

## 🔄 Continuous Mode (Optional)
To run continuously without stopping, use:

import random  
import time  

while True:  
    subject = random.choice(subjects)  
    action = random.choice(actions)  
    place = random.choice(places)  

    headline = f"Breaking News: {subject} {action} {place}"  
    print("\n" + headline)  

    time.sleep(2)  

---

## 📌 Future Improvements
- Add GUI using Tkinter  
- Save headlines to a file  
- Add categories (sports, tech, politics)  
- Improve headlines using AI  

---

## 👨‍💻 Author
Sharanabasappa K  

🔗 LinkedIn: https://www.linkedin.com/in/sharanabasappa-k/  

---

## 📄 License
This project is open-source and free to use.

---

## ⭐ Support
If you like this project, give it a ⭐ on GitHub!
