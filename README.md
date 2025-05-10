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
   
     `pip install pyfiglet`

   > If `pip` is not recognized, try this alternative command:
   
     `python -m pip install pyfiglet`

4. **Run the script:**
   - On **Windows**, you can **double-click** the `shopping_manager.py` file to run the script. The terminal window will appear, and you can interact with the application.
   - If double-clicking doesn't work (i.e., the terminal closes immediately), open **Command Prompt** or **PowerShell**, navigate to the script's folder, and run:

     `python shopping_manager.py`

5. **Using Docker (Alternative):**
   If you'd like to run the app using Docker, follow these steps:

   - **Dockerfile:** Ensure the `Dockerfile` is in your project folder with the following content:

     ```Dockerfile
     FROM python:3.13-slim

     WORKDIR /app

     # Install system packages (e.g., git)
     RUN apt-get update && apt-get install -y git && apt-get upgrade -y

     # Install Python libraries directly
     RUN pip install --no-cache-dir requests pyfiglet

     # Clone the Git repository
     RUN git clone https://github.com/vetronics/shopping_manager.git \
         && mv shopping_manager/* . \
         && rm -rf shopping_manager

     # Run the app
     CMD ["python", "shopping_manager.py"]
     ```

   - **Build the Docker image:**
     In your terminal, navigate to the project folder (where the `Dockerfile` is located) and run:

     ```bash
     docker build -t shopping-manager .
     ```

   - **Run the Docker container:**
     Once the image is built, you can run it with:

     ```bash
     docker run -it shopping-manager
     ```

---

### 🍎 macOS

1. **Install Python 3:**
   - With [Homebrew](https://brew.sh/):

     `brew install python`
   
   - Or download it from [python.org](https://www.python.org/downloads/)

2. **Open Terminal:**
   - Press `Command + Space`, type **Terminal**, then press Enter

3. **Install `pyfiglet`:**
   - Run the following command in your terminal:
   
     `pip3 install pyfiglet`

   > Or try:
   
     `python3 -m pip install pyfiglet`

4. **Run the Script:**
   - Open **Terminal**, navigate to the script's directory, and run:

     `python3 shopping_manager.py`

5. **Using Docker (Alternative):**
   - **Dockerfile:** Ensure the `Dockerfile` is in your project folder with the following content:

     ```Dockerfile
     FROM python:3.13-slim

     WORKDIR /app

     # Install system packages (e.g., git)
     RUN apt-get update && apt-get install -y git && apt-get upgrade -y

     # Install Python libraries directly
     RUN pip install --no-cache-dir requests pyfiglet

     # Clone the Git repository
     RUN git clone https://github.com/vetronics/shopping_manager.git \
         && mv shopping_manager/* . \
         && rm -rf shopping_manager

     # Run the app
     CMD ["python", "shopping_manager.py"]
     ```

   - **Build the Docker image:**
     In your terminal, navigate to the project folder (where the `Dockerfile` is located) and run:

     ```bash
     docker build -t shopping-manager .
     ```

   - **Run the Docker container:**
     Once the image is built, you can run it with:

     ```bash
     docker run -it shopping-manager
     ```

---

### 🐧 Linux (Debian/Ubuntu)

1. **Install Python and pip:**

   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
