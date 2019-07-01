from IPSocket import IPSocket
import struct
import socket 

protocol = 0x806

ipsocket = IPSocket("wlp3s0", protocol)

def constructData(dest_ip):

    source_mac = b"\xe8\x6a\x64\xa6\xc2\xc4"
    source_ip = "172.16.10.116"
    dest_mac = b"\xff\xff\xff\xff\xff\xff"
    # dest_ip = "172.16.10.1"

    payload = struct.pack("!6s6sH", dest_mac, source_mac, protocol)

    htype = 1                               # Hardware_type ethernet
    ptype = 0x0800                          # Protocol type TCP
    hlen = 6                                # Hardware address Len
    plen = 4                                # Protocol addr. len
    operation = 1                           # 1=request/2=reply
    src_ip = socket.inet_aton(source_ip)
    dst_ip = socket.inet_aton(dest_ip)
    header = struct.pack("!HHBBH6s4s6s4s", htype, ptype, hlen, plen, operation, source_mac, src_ip, dest_mac, dst_ip)

    return payload + header

counter = 0
while True:
    counter %= 255
    packet = constructData(f"172.16.10.{counter}")
    ipsocket.send(packet)

    counter += 1