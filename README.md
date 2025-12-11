# 🧠 Anti-Procrastination Assistant
*A privacy-respecting, open-source productivity tool*

Anti-Procrastination Assistant is a desktop utility that helps users understand and improve their focus habits. With full user consent, it monitors **keyboard activity**, **mouse activity**, and **screen context patterns** to estimate when you might be drifting into procrastination — and gently reminds you to refocus.

This project is **free**, **open-source**, and designed to be **transparent**, **ethical**, and **privacy-first**.

---

## ✨ Features

- **Focus Monitoring (Opt-In)**  
  Observes interaction patterns (never raw keystrokes) to estimate focus loss.

- **Distraction Awareness**  
  Detects user-defined distraction apps and windows.

- **Local-Only Screen Context Analysis**  
  Pattern detection runs on-device. No screenshots or personal data are saved or transmitted.

- **Daily Focus Reports**  
  Generates privacy-friendly summaries of your focused vs. distracted time.

- **Fully Open Source**  
  Reviewable, modifiable, community-driven.

---

## 🔒 Privacy & Ethical Use

This project adheres to strict ethical guidelines:

- ❌ No raw keystroke logging  
- ❌ No password capturing  
- ❌ No screenshot recording or uploading  
- ❌ Never operates without explicit user consent  
- ✔️ All processing happens locally  
- ✔️ Monitoring is optional and easy to disable  
- ✔️ All local data can be deleted at any time  

If you modify or redistribute this tool, you must preserve transparency and user consent requirements.

---

# 📦 Installation

## 🔧 Prerequisites
- Linux only so far
- Permissions to install desktop applications  
- One of the supported runtimes (depends on your build):  
  - Python 3.9+  

---

### **Build From Source**
```terminal
git clone https://github.com/AshtonMarley/procrastinatoin-alerter-python
cd procrastinatoin-alerter-python
source ./install.sh
