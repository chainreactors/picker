---
title: AirPlay Dual‑Mode Discovery Scanner for Flipper Zero ESP32 WiFi Dev Board
url: https://cxsecurity.com/issue/WLB-2026030010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-08
fetch_date: 2026-03-09T04:08:05.282518
---

# AirPlay Dual‑Mode Discovery Scanner for Flipper Zero ESP32 WiFi Dev Board

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
|  |  | |  | | --- | | **AirPlay Dual‑Mode Discovery Scanner for Flipper Zero ESP32 WiFi Dev Board** **2026.03.08**  Credit:  **[indoushka](https://cxsecurity.com/author/indoushka/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

=============================================================================================================================================
| # Title : AirPlay Dual‑Mode Discovery Scanner for Flipper Zero ESP32 WiFi Dev Board |
| # Author : indoushka |
| # Tested on : windows 11 Fr(Pro) / browser : Mozilla firefox 147.0.4 (64 bits) |
| # Vendor : https://www.apple.com/airplay/ |
=============================================================================================================================================
[+] Summary : This project implements a dual‑mode AirPlay discovery scanner using an ESP32 WiFi Dev Board attached to a Flipper Zero. The tool is designed strictly for network discovery and visibility, not exploitation.
The scanner supports two operating modes:
[+] WiFi mDNS Mode (Connected Mode)
Connects to a specified WiFi network.
Listens to multicast DNS (mDNS) traffic on UDP port 5353.
Detects AirPlay service advertisements:
\_airplay.\_tcp.local
\_raop.\_tcp.local
Identifies unique device IP addresses.
Prevents duplicate counting.
Displays total discovered AirPlay devices.
This mode provides higher accuracy because it operates within the network and processes legitimate multicast service announcements.
[+] Sniffer Mode (Promiscuous Mode – No WiFi Password Required)
Enables ESP32 promiscuous mode.
Passively monitors nearby wireless traffic.
Searches packet payloads for AirPlay service identifiers.
Counts detected broadcast announcements.
This mode does not connect to any network and does not transmit packets. It passively inspects broadcast traffic only.
[+] What It Detects
The scanner may discover devices such as:
Apple TV
Devices running iOS
Systems running macOS
[+] POC :
#include <WiFi.h>
#include <WiFiUdp.h>
#include "esp\_wifi.h"
WiFiUDP udp;
const char\* ssid = "YOUR\_WIFI";
const char\* password = "YOUR\_PASSWORD";
const int MDNS\_PORT = 5353;
const IPAddress multicastIP(224, 0, 0, 251);
#define MAX\_DEVICES 50
IPAddress discoveredIPs[MAX\_DEVICES];
int deviceCount = 0;
bool wifiMode = true;
bool alreadyDiscovered(IPAddress ip) {
for (int i = 0; i < deviceCount; i++) {
if (discoveredIPs[i] == ip) return true;
}
return false;
}
void startWiFiMode() {
Serial.println("Starting WiFi mDNS Mode...");
WiFi.mode(WIFI\_STA);
WiFi.begin(ssid, password);
while (WiFi.status() != WL\_CONNECTED) {
delay(500);
Serial.print(".");
}
Serial.println("\nConnected!");
Serial.print("IP: ");
Serial.println(WiFi.localIP());
udp.beginMulticast(WiFi.localIP(), multicastIP, MDNS\_PORT);
}
void sniffer(void\* buf, wifi\_promiscuous\_pkt\_type\_t type) {
wifi\_promiscuous\_pkt\_t \*pkt = (wifi\_promiscuous\_pkt\_t\*)buf;
uint8\_t \*payload = pkt->payload;
for (int i = 0; i < pkt->rx\_ctrl.sig\_len; i++) {
if (i < pkt->rx\_ctrl.sig\_len - 12) {
if (memcmp(payload + i, "\_airplay.\_tcp", 13) == 0 ||
memcmp(payload + i, "\_raop.\_tcp", 10) == 0) {
deviceCount++;
Serial.println("=================================");
Serial.println("AirPlay Broadcast Detected (Sniffer)");
Serial.print("Total Detected: ");
Serial.println(deviceCount);
Serial.println("=================================");
break;
}
}
}
}
void startSnifferMode() {
Serial.println("Starting Sniffer Mode...");
WiFi.mode(WIFI\_MODE\_NULL);
esp\_wifi\_set\_promiscuous(true);
esp\_wifi\_set\_promiscuous\_rx\_cb(&sniffer);
}
void setup() {
Serial.begin(115200);
delay(1000);
Serial.println("AirPlay Dual Mode Scanner");
Serial.println("Type 1 for WiFi Mode");
Serial.println("Type 2 for Sniffer Mode");
while (!Serial.available()) {
delay(100);
}
char choice = Serial.read();
if (choice == '2') {
wifiMode = false;
startSnifferMode();
} else {
wifiMode = true;
startWiFiMode();
}
}
void loop() {
if (wifiMode) {
int packetSize = udp.parsePacket();
if (packetSize) {
char packet[512];
int len = udp.read(packet, sizeof(packet) - 1);
if (len > 0) packet[len] = 0;
String data = String(packet);
if (data.indexOf("\_airplay.\_tcp") >= 0 ||
data.indexOf("\_raop.\_tcp") >= 0) {
IPAddress remoteIP = udp.remoteIP();
if (!alreadyDiscovered(remoteIP) && deviceCount < MAX\_DEVICES) {
discoveredIPs[deviceCount] = remoteIP;
deviceCount++;
Serial.println("=================================");
Serial.println("New AirPlay Device Found (WiFi)");
Serial.print("IP: ");
Serial.println(remoteIP);
Serial.print("Total Devices: ");
Serial.println(deviceCount);
Serial.println("=================================");
}
}
}
}
delay(10);
}
Greetings to :==============================================================================
jericho \* Larry W. Cashdollar \* r00t \* Yougharta Ghenai \* Malvuln (John Page aka hyp3rlinx)|
============================================================================================

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030010)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2026**, cxsecurity.com

|  |

Back to Top