# 📡 Task-05: Network Packet Analyzer (Educational Use Only)

This is Task-05 of my Cybersecurity Internship at **Prodigy InfoTech**.

The goal is to build a simple network packet analyzer using Python and Scapy.  
It captures live packets and displays key information such as source, destination, and protocol types.

---

## 🚀 Features

- Real-time packet capture
- Displays:
  - Source IP
  - Destination IP
  - Protocol (TCP, UDP, ICMP)
- Lightweight and CLI-based

---

## ⚠️ Legal Disclaimer

This tool is strictly for **educational use** on **your own network**.  
Do not run it on public or unauthorized networks.

---

## 🖥️ How to Run

### ▶️ Install Scapy:
bash
pip install scapy

▶️ Run the script:
bash
sudo python3 packet_sniffer.py

📸 Sample Output

[+] Packet: 192.168.1.5 -> 8.8.8.8
    Protocol: 17
    Layer: UDP

[+] Packet: 10.0.0.1 -> 10.0.0.254
    Protocol: 6
    Layer: TCP
    
👨‍💻 Author
Sahil Khan
Cybersecurity Intern @ Prodigy InfoTech
GitHub: sudoxsahil

```bash
pip install scapy
