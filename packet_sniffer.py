from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"\n[+] Packet: {ip_layer.src} -> {ip_layer.dst}")
        print(f"    Protocol: {packet.proto}")
        
        if packet.haslayer(TCP):
            print("    Layer: TCP")
        elif packet.haslayer(UDP):
            print("    Layer: UDP")
        elif packet.haslayer(ICMP):
            print("    Layer: ICMP")
        else:
            print("    Layer: Other")

# Sniff packets on interface (use eth0, wlan0, etc., if needed)
print("🔍 Starting packet capture... Press Ctrl+C to stop.\n")
sniff(prn=packet_callback, store=0)
