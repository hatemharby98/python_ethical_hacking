# 🛡️ Advanced Python Keylogger (Educational Project)

A Python-based security tool designed to simulate spyware behavior by capturing keystrokes and exfiltrating logs via email using SMTP. This project focuses on understanding **Input Hooking** and **Data Exfiltration** techniques for defensive purposes.

---

## ⚠️ DISCLAIMER

**PLEASE READ BEFORE USING:**

This software is developed for **EDUCATIONAL PURPOSES ONLY**.

* This tool is intended to be used only on systems **you own** or have **explicit permission** to test.
* The developer is **not responsible** for any illegal use or damage caused by this tool.
* Using this software to monitor others without their consent is a crime and a violation of privacy laws.

---

## 🚀 Features

* **Keystroke Logging:** Captures all keyboard inputs using the `pynput` library.
* **Email Reporting:** Automatically sends captured logs to a remote email address using `smtplib`.
* **Threaded Reporting:** Sends reports at specific time intervals without freezing the main process.
* **Stealth Simulation:** Demonstrates how background processes operate in a Windows environment.

## 🛠️ Prerequisites

Before running the script, ensure you have the following:

1.  **Python 3.x** installed.
2.  A **Gmail Account** (Sender email).
    * *Note: You must enable "2-Step Verification" and generate an [App Password](https://myaccount.google.com/apppasswords) to allow the script to login.*

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR-USERNAME/REPO-NAME.git](https://github.com/YOUR-USERNAME/REPO-NAME.git)
    cd REPO-NAME
    ```

2.  **Install required dependencies:**
    ```bash
    pip install pynput
    ```

## ⚙️ Configuration

Open the main python file (e.g., `keylogger.py`) and update the authentication variables:

```python
email = "YOUR_EMAIL@gmail.com"
password = "YOUR_APP_PASSWORD"  # Do NOT use your real login password
