### **Problem Statement**- Implement a peer to peer network monitoring system using socket programming that can collect data such as if other user is online or not, how much round trip time is there between two clients.

### **Step To Run the Program**
- `python3 p2p.py` (For the first peer)
- `python3 p2p.py` `<ip-add>` (For the second peer)

### **Configuration for the setup of other computer(If the connection is refused)**
- `sudo ufw enable`
- `sudo ufw allow <port>`
- `sudo ufw allow incommig`
- `sudo ufw allow outgoing`

