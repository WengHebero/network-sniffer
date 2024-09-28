Here’s the complete `README.md` in a format suitable for your GitHub repository, including all the steps for building a network sniffer using Python:

```markdown
# 🐍 Network Sniffer

A simple network sniffer built using Python and Scapy. This tool captures and analyzes packets on a network interface.

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## 📋 Prerequisites

Before you begin, ensure you have the following software installed:

- **Python** (3.6 or higher) 🐍
- **Homebrew** (for MacOS) 🍺
- **Wireshark** (for packet analysis) 📊
- **Scapy** (for packet manipulation) ⚡

### Install Prerequisites

1. **Install Homebrew** (if you haven't already):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python**:
   ```bash
   brew install python
   ```

3. **Install Wireshark**:
   ```bash
   brew install --cask wireshark
   ```

4. **Install Scapy**:
   ```bash
   pip install scapy
   ```

## 📦 Installation

### Step 1: Install Python and Dependencies

Make sure Python is installed on your Mac (usually pre-installed). You can check by running:

```bash
python3 --version
```

#### Install `Scapy` library

`Scapy` is a powerful Python library used to interact with network packets.

1. Install `pip` if not already installed:
   ```bash
   sudo easy_install pip
   ```

2. Install `Scapy` using `pip`:
   ```bash
   sudo pip3 install scapy
   ```

### Step 2: Create the Python Script

1. Open your terminal and create a new Python file:
   ```bash
   nano network_sniffer.py
   ```

2. Write a basic script to capture packets:

   ```python
   from scapy.all import sniff

   # Callback function to process each packet
   def process_packet(packet):
       print(packet.summary())

   # Sniff packets on the default network interface
   sniff(prn=process_packet)
   ```

### Step 3: Run the Sniffer

1. Save and exit the file (`Ctrl + X`, then `Y` to confirm).
2. To run the script, use:
   ```bash
   sudo python3 network_sniffer.py
   ```

   **Note:** You need `sudo` because capturing network packets requires administrative privileges.

You should start seeing packet summaries as they are captured on your network.

### Step 4: Customize the Sniffer

#### Filter Traffic by Protocol

You can filter the types of packets you want to capture. For example, to only capture TCP packets, modify the script:

```python
from scapy.all import sniff

def process_packet(packet):
    if packet.haslayer('TCP'):
        print(packet.summary())

sniff(prn=process_packet)
```

#### Save Captured Packets to a File

You might want to save captured packets for analysis later. You can do that by writing the packets to a `.pcap` file:

```python
from scapy.all import sniff, wrpcap

packets = []

def process_packet(packet):
    packets.append(packet)
    print(packet.summary())

sniff(prn=process_packet)

# Save packets to a file after sniffing is stopped
wrpcap('captured_packets.pcap', packets)
```

### Step 5: Analyze Captured Packets

You can analyze the `.pcap` file using **Wireshark**, a popular tool for network analysis, by opening the file:

1. Open Wireshark and open the `captured_packets.pcap` file.

This will allow you to visualize and analyze the captured traffic.

### Step 6: Add More Functionality

You can further enhance your sniffer by:

- Capturing only specific IP addresses.
- Counting packet types.
- Displaying detailed packet information, including the packet’s source and destination IP addresses, ports, and protocol.

For example, to capture HTTP requests, you could modify the script like this:

```python
from scapy.all import sniff, TCP

def process_packet(packet):
    if packet.haslayer(TCP) and packet.dport == 80:
        print(f"HTTP Request: {packet.summary()}")

sniff(prn=process_packet)
```

## ⭐ Features

- Capture network packets in real-time.
- Filter captured packets based on protocols.
- Save captured packets in `.pcap` format for analysis in Wireshark.
- Supports live packet analysis.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## 📞 Contact

For questions, suggestions, or feedback, feel free to reach out to me:

- **GitHub**: [WengHebero](https://github.com/WengHebero)

---

Happy Sniffing! 🐾
```

### Instructions for Use

1. **Copy the above template** and paste it into a file named `README.md` in your project directory.
2. **Customize** the sections, especially the contact details and any additional features you want to highlight.
3. **Save** the file, and then push your changes to GitHub using the following commands:
   ```bash
   git add README.md
   git commit -m "Add detailed README.md"
   git push origin main
   ```
