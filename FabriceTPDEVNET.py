from netmiko import ConnectHandler

cisco1 = {
 "device_type": "cisco_nxos",
 "host": "sandbox-iosxr-1.cisco.com",
 "username": "admin",
 "password": "C1sco12345"
}
net_connect = ConnectHandler(**cisco1)
question1 = net_connect.send_command("show running-config")
question2 = net_connect.send_command("show ip int brief down") 
question3 = net_connect.send_command("show ip interface brief up")
question4 = net_connect.send_command("show ip route")
print(question1, question2, question3, question4)
net_connect.disconnect()
