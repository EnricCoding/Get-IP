import scapy.all as scapy

def scap(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.arp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clientes = []
    for direccion in answered_list:
        client_direcc = {"su ip es": direccion[1].psrc, " y su mac": direccion[1].hwsrc }
        clientes.append(client_direcc)
    return (clientes)

def resultados(results_list):
    print("Aqui tiene las IP Y MACS")
    for client in results_list:
        print(client["SU IP" + client["SU MAC"]])

scan_result = scan("") #introduce IP
print(scan_result)
