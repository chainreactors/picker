---
title: WinHttpOpen user agents
url: https://www.hexacorn.com/blog/2026/02/14/winhttpopen-user-agents/
source: Hexacorn
date: 2026-02-14
fetch_date: 2026-02-15T04:25:33.966949
---

# WinHttpOpen user agents

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2026/02/14/1-little-known-secret-of-compattelrunner-exe/)

# WinHttpOpen user agents

Posted on [2026-02-14](https://www.hexacorn.com/blog/2026/02/14/winhttpopen-user-agents/ "10:40 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

When you call [WinHttpOpen](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpopen) API you can specify the user agent that will be used in subsequent WinHTTP calls.

Windows OS and its native binaries use WinHttp APIs a lot, so the below is list of all user agents I could find that are used internally by Windows 11:

* Activation UX Library
* App Virt Client/1.0
* CHttpConnector
* client connection
* Client NCA
* CloudSdb
* DAFUPnP
* DavClnt
* Delegated Service Installer
* DiagnosticCSP upload
* ENROLLClient
* Escl Scan Client
* Facilitator
* FDSSDP
* HttpWrapper
* Internet Print Provider
* kerberos/1.0
* LFSVC
* MAPS\_PROXY\_RESOLUTION
* Microsoft BITS/7.8
* Microsoft Connection Manager
* Microsoft HP Printer Wifi Provisioning
* Microsoft NCSI
* Microsoft NetworkListManager
* Microsoft WinRM Client
* Microsoft WinRM Client – Proxy Autodetection
* Microsoft-CryptoAPI/10.0
* Microsoft-Delivery-Optimization/10.1
* MMP-C Discovery Client
* Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)
* Mozilla/4.0 (compatible; Win32; NDES client 10.0.26100.4768/ge\_release\_svc\_prod3)
* Mozilla/4.0 (compatible; Win32; NDES client 10.0.26100.5074/ge\_release\_svc\_prod3)
* Mpssvc Proxy Detection
* MSAWindows/55
* msde/10.0
* MSDW
* MSPROV
* MSRPC
* MS\_WorkFoldersClient
* NetworkProxyCSP
* OneSettingsQuery
* OTPCEP Client
* Peernet HTTP Transport/1.0
* ProxyResolver/1.0
* PushButtonReset
* rasapi32
* RPCPing
* SLSSoapClient
* SSTP
* TenantRestrictions
* TSG connection
* TSWorkspace/2.0
* TSWorkspace/3.0
* User-Agent: Microsoft-DLNA DLNADOC/1.50
* WebDefenseClient
* WicaAgent
* Windows Credential Recovery Client
* Windows Device Management Platform
* Windows Dlp Manager
* Windows EK Retrieval 1.0
* Windows Health Cert Retrieval 1.0
* Windows LAPS
* Windows Print User Agent
* Windows Store/1.0
* Windows Web Sign-in Client
* Windows-AzureAD-Authentication-Provider/1.0
* WinHTTP connection from WS to IMDS
* WinHTTP global session
* WinHTTP Session
* WinHttpGetIEProxyConfigForCurrentUser Redirect
* WSDAPI
* XblAuthManager

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Windows 11](https://www.hexacorn.com/blog/category/windows-11/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2026/02/14/winhttpopen-user-agents/ "Permalink to WinHttpOpen user agents").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")