# FriendsExploit (AppDevsX)

A PyQt5-based desktop application obfuscated and secured using PyArmor. This repository contains the runtime binaries and dependencies required to execute the tool across Windows and Linux platforms.

---

## 📋 Prerequisites & Requirements

The application requires Python and a set of library dependencies:
- **Python**: Recommended version **3.11.x** (compatible with the obfuscation runtime configuration).
- **Python Libraries**:
  - `PyQt5` (GUI Interface)
  - `requests` (HTTP Networking)
  - `urllib3` (HTTP Client)

---

## 🚀 Installation & Running

### 🐧 Running on Linux (Debian/Ubuntu/Fedora)

To run the application on Linux, you must use **Python 3.11** because the obfuscated source targets Python 3.11 bytecode, and a Linux native PyArmor runtime library (`pyarmor_runtime.so`) is supplied.

1. **Install Python 3.11 and pip** (if not already installed):
   ```bash
   sudo apt update
   sudo apt install python3.11 python3.11-venv python3-pip
   ```

2. **Install Python dependencies**:
   ```bash
   python3.11 -m pip install PyQt5 requests urllib3 --break-system-packages
   ```

3. **Install System Display libraries for PyQt5** (if running in a minimal desktop environment):
   ```bash
   sudo apt install libxcb-xinerama0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-shape0 libxcb-shm0 libxcb-sync1 libxcb-xfixes0 libxkbcommon-x11-0
   ```

4. **Launch the application**:
   ```bash
   python3.11 main.py
   ```

---

### 🪟 Running on Windows

To run the application on Windows, you will use the Windows binary helper (`pyarmor_runtime.pyd`) included in the project directory.

1. **Install Python 3.11** from the [official website](https://www.python.org/downloads/).
2. **Open Command Prompt (cmd) or PowerShell** in the project directory and install the required dependencies:
   ```cmd
   pip install PyQt5 requests urllib3
   ```
3. **Launch the application**:
   ```cmd
   python main.py
   ```

---

## 🔒 Security & Code Obfuscation

This application uses **PyArmor** to protect its source code:
- **Obfuscated Core**: The main application logic resides within the protected `main.py`.
- **Platform Runtimes** (`pyarmor_runtime_000000/`):
  - `pyarmor_runtime.pyd`: Dynamically loaded extension for **Windows** environments.
  - `pyarmor_runtime.so`: Dynamically loaded extension for **Linux x86_64** environments.
