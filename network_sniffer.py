# Import necessary modules from Scapy
from scapy.all import sniff, wrpcap

# List to store captured packets
packets = []

# Callback function to process each packet and store them
def process_packet(packet):
    packets.append(packet)
    print(packet.summary())

# Sniff packets on the default network interface
sniff(prn=process_packet)

# After sniffing, save packets to a pcap file
wrpcap('captured_packets.pcap', packets)
