# 🔍 Port Scanner (Python)

A multithreaded TCP port scanner written in Python.  
Uses `socket`, `tqdm`, and `ThreadPool` for fast scanning of open ports.

---

## ⚙️ How It Works

- Scans all 65,535 TCP ports (1–65535)
- Checks each port using `socket.connect_ex`
- Runs up to **3000 threads** in parallel
- Shows real-time progress with `tqdm`
- Prints a list of open ports at the end

---

## ⚠️ Disclaimer

> Use this tool **only on devices you own or have permission to scan**.  
> This project is created for **educational purposes only**.

---

## 📦 Requirements

- Python 3.8 or higher
- tqdm library  
  Install with:

  ```bash
  pip install tqdm

## 🚀 Usage

--Replace the HOST variable in port_scanner.py with your target IP address:
    
    HOST = '192.168.11.33'  # <- your target IP

--Run the script:
    python3 port_scanner.py

## 🧠 What I Learned

  -Working with sockets in Python

  -Basic network programming (TCP ports)

  -Multithreading with ThreadPool

  -Visual progress tracking with tqdm
