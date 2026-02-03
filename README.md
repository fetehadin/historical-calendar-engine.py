# Historical Calendar Engine  
**Gregorian • Julian • Ethiopian (EC)**

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Stars](https://img.shields.io/badge/Stars-Welcome-lightgrey)
![Forks](https://img.shields.io/badge/Forks-Welcome-lightgrey)

A **pure Python calendar engine** that generates a **full yearly calendar** and displays  
**Gregorian / Julian dates alongside Ethiopian (EC) dates** for every day.

This project focuses on **historical accuracy, calendar mathematics, and algorithmic clarity**  built deliberately **without external date libraries** to deeply understand how calendars work internally.

---

## ✨ Key Features

-  Full **12-month calendar output** for a given year  
-  Automatic handling of **Gregorian, Julian, and Ethiopian calendars**
-  Displays **Ethiopian date (EC)** together with Gregorian/Julian date in each cell
-  Correct handling of **historical calendar transitions**
-  Graceful validation for unsupported early years
-  Interactive loop: generate calendars until the user chooses to exit
-  Implemented using **vanilla Python only**

---

##  Motivation, Why This Project?

Calendar systems look simple on the surface, but they hide **centuries of history, math, and edge cases**.

This project was built to:
- Understand **Julian vs Gregorian leap year rules**
- Learn **Julian Day Number (JDN)** based date conversion
- Handle **real historical anomalies** (e.g., September 1752)
- Strengthen Python fundamentals through a **non-trivial real-world problem**
- Create a **credible portfolio project** that demonstrates depth, not just syntax

---

## 🗓 Supported Calendar Rules

The program automatically selects the correct calendar system:

| Year Range | Calendar Behavior |
|-----------|------------------|
| `< 8 AD` | ❌ Rejected (Ethiopian calendar undefined) |
| `8 – 1751` | Julian Calendar |
| `1752` | Hybrid Year (Julian → Gregorian) |
| `1753 – 2100` | Gregorian Calendar |
| `> 2100` | Gregorian Calendar |

###  September 1752 (Historical Cutover)
- Days **September 3–13, 1752 do not exist**
- Calendar jumps directly from **September 2 → September 14**
- Correctly implemented according to historical records

---

##  Technical Highlights

-  Julian Day Number (JDN) conversions
-  Accurate leap-year logic (Julian vs Gregorian)
-  Ethiopian calendar conversion using fixed epoch
-  Month-spanning EC month detection
-  Robust edge-case handling
-  No `datetime`, no third-party libraries

---

##  Installation & Requirements

### Requirements
- Python **3.8+**
- Any OS (Linux, macOS, Windows)

### Installation
```bash
git clone https://github.com/your-username/historical-calendar-engine.git
cd historical-calendar-engine
```

## 👨‍💻 Author

**Fetehadin**  
Software Engineering Student  
Passionate about systems, algorithms, and historically accurate computing.

---

## 📜 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it.

---

⭐ If you find this project interesting or helpful, feel free to **star the repository** and explore the code!
