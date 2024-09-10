from scapy.all import IP, ICMP, sr1

# Define the target IP address
target_ip = "8.8.8.8"

# Create an IP packet with the target IP address
ip_packet = IP(dst=target_ip)

# Create an ICMP echo request packet
icmp_packet = ICMP()

# Combine the IP and ICMP packets
packet = ip_packet / icmp_packet

# Send the packet and get the response
response = sr1(packet, timeout=1, verbose=0)

# Check if we got a response
if response:
    print("Received response from", target_ip)
    print(response.show())
else:
    print("No response from", target_ip)
