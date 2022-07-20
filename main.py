from pex.net import Net

net = Net()
gateways = net.get_gateways()

for iface in gateways:
    for host, mac in net.get_arp_hosts(gateways[iface]):
        if net.get_vendor(mac) == 'Raspberry PI Foundation':
            print(host)
