# 🛒 Shopping Manager

**Shopping Manager** is a simple, cross-platform command-line tool written in Python that helps you manage shopping list items and their associated values. It features an ASCII-style interface and provides file-based storage for tracking and budgeting.

---

## ✨ Features

- ASCII Art interface using `pyfiglet`
- Interactive command-line menu
- Add or remove shopping items
- Assign values to items (e.g., cost, quantity)
- Count total items and values
- Calculate the total sum of all values
- Saves data in plain `.txt` files
- No external database required

---

## 🧰 Requirements

- Python 3.x  
  👉 [Download Python](https://www.python.org/downloads/)
- `pyfiglet` module

---

## 💻 Installation Instructions

Follow the setup guide based on your operating system. Additionally, you can also use Docker to run the application.

---

### 🪟 Windows

1. **Install Python:**
   - Download it from [python.org](https://www.python.org/downloads/)
   - ✅ Check the box **“Add Python to PATH”** before clicking *Install Now*

2. **Open the terminal:**
   - Press `Windows + S`, search for **Command Prompt**, **PowerShell**, or **Windows Terminal**

3. **Install `pyfiglet`:**
   - Run the following command in your terminal:
   
     ```bash
     pip install pyfiglet
     ```

   > If `pip` is not recognized, try this alternative command:
   
     ```bash
     python -m pip install pyfiglet
     ```

4. **Run the script:**
   - On **Windows**, you can **double-click** the `shopping_manager.py` file to run the script. The terminal window will appear, and you can interact with the application.
   - If double-clicking doesn't work (i.e., the terminal closes immediately), open **Command Prompt** or **PowerShell**, navigate to the script's folder, and run:

     ```bash
     python shopping_manager.py
     ```

---

### 🍎 macOS

1. **Install Python 3:**
   - With [Homebrew](https://brew.sh/):

     ```bash
     brew install python
     ```
   
   - Or download it from [python.org](https://www.python.org/downloads/)

2. **Open Terminal:**
   - Press `Command + Space`, type **Terminal**, then press Enter

3. **Install `pyfiglet`:**
   - Run the following command in your terminal:
   
     ```bash
     pip3 install pyfiglet
     ```

   > Or try:
   
     ```bash
     python3 -m pip install pyfiglet
     ```

4. **Run the Script:**
   - Open **Terminal**, navigate to the script's directory, and run:

     ```bash
     python3 shopping_manager.py
     ```

---

### 🐧 Linux (Debian/Ubuntu)

1. **Install Python and pip:**

   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. **Install `pyfiglet`:**

   ```bash
   pip3 install pyfiglet
   ```

3. **Run the Script:**

   * Open **Terminal**, navigate to the script's directory, and run:

     ```bash
     python3 shopping_manager.py
     ```

---

### 🐧 Linux (Fedora)

1. **Install Python and pip:**

   ```bash
   sudo dnf install python3 python3-pip
   ```

2. **Install `pyfiglet`:**

   ```bash
   pip3 install pyfiglet
   ```

3. **Run the Script:**

   * Open **Terminal**, navigate to the script's directory, and run:

     ```bash
     python3 shopping_manager.py
     ```

---

### 🐳 Docker (Alternative)

If you'd like to run the app using Docker, follow these steps:

1. **download a `Dockerfile`** inside the dicrectoy as dockerfile

2. **Build the Docker image:**
   In your terminal, navigate to the project folder (where the `Dockerfile` is located) and run:

   ```bash
   docker build -t shopping-manager .
   ```

3. **Run the Docker container:**
   Once the image is built, you can run it with:

   ```bash
   docker run -it shopping-manager
   ```

This method does not require installing Python or dependencies on your local system, as everything will be handled by Docker.

---

## ✅ Setup Checklist

* [x] Install Python 3
* [x] Add Python to PATH (Windows)
* [x] Open Terminal or Command Prompt
* [x] Install `pyfiglet` with pip

---

## 🚀 How to Run

1. **Windows:**

   * **Double-click** the `shopping_manager.py` file to run the script on Windows.
   * If double-clicking doesn't work (i.e., the terminal closes immediately), open **Command Prompt** or **PowerShell**, navigate to the script's directory, and run:

     ```bash
     python shopping_manager.py
     ```

2. **macOS and Linux (Debian/Ubuntu/Fedora):**

   * Open **Terminal**, navigate to the script's directory, and run:

     ```bash
     python3 shopping_manager.py
     ```

   > Use `python` if `python3` doesn't work on your system.

---

## 📂 File Management

* The app saves shopping list items and their values in local `.txt` files.
* Ensure you have read/write permissions in the script directory.

---

## 🧾 Example Use Case

* Add items like `Milk`, `Eggs`, or `Bread`.
* Assign values like cost or quantity.
* Track total item count and sum of values.
* Remove or update items as needed.

---

## 🧰 Troubleshooting

* **Command not found**: Use `python3` or `pip3`.
* **Permission denied**: Run as administrator or use `sudo` on GNU/Linux machines.
* **pip not working**: Ensure Python is properly installed and in PATH.

---

## 📌 Notes

* Works on Windows, macOS, and Linux.
* Great for small shopping or budget tracking tasks.
* Easy to expand or customize.

---

## ⚠️ Compatibility Notes

If you're running the script on **macOS** or **Linux** (including **Fedora**, **Debian**, **Ubuntu**), you should **comment out** the following lines in the script:

```python
# os.system("cls")  # Windows-specific clear screen
# os.system("title shopping manager")  # Set terminal window title (Windows)
# os.system("color 05")  # Change text color (Windows)
```

---
