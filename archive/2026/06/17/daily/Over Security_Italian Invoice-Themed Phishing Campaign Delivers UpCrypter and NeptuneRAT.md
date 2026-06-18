---
title: Italian Invoice-Themed Phishing Campaign Delivers UpCrypter and NeptuneRAT
url: https://www.d3lab.net/italian-invoice-themed-phishing-campaign-delivers-upcrypter-and-neptunerat/
source: Over Security
date: 2026-06-17
fetch_date: 2026-06-18T06:51:18.502346
---

# Italian Invoice-Themed Phishing Campaign Delivers UpCrypter and NeptuneRAT

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

# Italian Invoice-Themed Phishing Campaign Delivers UpCrypter and NeptuneRAT

[Malware](https://www.d3lab.net/category/malware/)

[![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/06/NeptuneRAT_Chain.png?resize=1210%2C423&ssl=1)](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/06/NeptuneRAT_Chain.png?fit=1030%2C580&ssl=1 "NeptuneRAT_Chain")

Since February 2026, we have been tracking an invoice-themed malware campaign targeting Italian users and organizations. The messages are written in Italian and abuse a familiar business pretext: a short invoice notification that asks the recipient to open an attached HTML document. The lure is minimal, credible enough for a busy inbox, and designed to move the victim from email to browser to script execution.

One of the analyzed emails used the subject `Nostra fattura nr. 91B`. The body asked the recipient to review the attached document to view invoice details. The attachment was named `Fattura_00121.html`.

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/06/NeptuneRAT_Mail.png?resize=949%2C755&ssl=1)

The attached HTML file is intentionally small. It redirects the browser to a phishing page hosted at `https://pillarsesolution[.]com/i#...`, where the URL fragment contains the recipient’s email address encoded in Base64. This identifier is likely used by the threat actor to track victims and store, in a dropzone, the email addresses of users who reached the phishing page and proceeded to download the malicious ZIP package.

The landing page presents a polished download interface in Italian. It tells the user that the document is ready, displays `Fattura_00121.pdf`, marks it as protected, and invites the user to click `Scarica File`. This visual layer is important: the malware does not rely only on attachment execution, but on making the transition from email to download feel routine.

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/06/NeptuneRAT_Web.png?resize=1030%2C863&ssl=1)

When the victim clicks the download button, the page reaches `https://bonanza.davidsabido[.]com/wp-includes/images/ic/i.php`. The server-side logic appears to gate delivery by user agent. Windows browser user agents receive a ZIP archive, while non-Windows or unsuitable clients are redirected to a generic PDF hosted on Google Drive. This split helps the campaign look less suspicious during casual inspection and avoids delivering the Windows payload to environments unlikely to execute it.

In the last analyzed case, the ZIP archive was `B00225511855210021-00551.zip` and contained a heavily obfuscated JavaScript file named `B00225511855210021-00551.js`. Opening the JavaScript starts the real infection chain through Windows Script Host. The script builds and launches a PowerShell command with execution policy bypass, then drops and executes additional PowerShell stages under `C:\Users\Public`.

The first decoded PowerShell stage checks connectivity against `www.google.com`, flushes DNS cache, disables or weakens Windows Defender settings, and looks for analysis tools. The anti-analysis process list includes names such as `handle`, `autorunsc`, `Dbgview`, `tcpvcon`, `any.run`, `sandbox`, `tcpview`, `OLLYDBG`, `ImmunityDebugger`, `Wireshark`, `apateDNS`, and `analyze`. If the environment looks suspicious, execution may stop or the host may be restarted.

After these checks, the malware downloads `03.txt` from a `meusitehostgator[.]com[.]br` domain. The downloaded data is parsed after a `%x%` marker and reconstructed as a .NET loader, `ClassLibrary3`, which is loaded directly in memory via PowerShell reflection. This behavior matches public reporting on UpCrypter campaigns: JavaScript and PowerShell act as staging layers, while an MSIL loader prepares and deploys the final payload.

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/06/NeptuneRAT_Chain.png?resize=1030%2C580&ssl=1)

The final PowerShell stage, `sgyof.ps1`, was recovered from [Joe Sandbox](https://www.joesandbox.com/analysis/1929225/0/html). It is a UTF-16LE PowerShell file containing a large byte array. That byte array loads a .NET assembly in memory through `[System.Reflection.Assembly]::Load(...)` and invokes `ClassLibrary1.Class1.Run(...)`. The embedded assembly contains RunPE functionality and a nested .NET executable.

Extracting the nested executable revealed the final payload. It is a .NET GUI executable internally identified as `MasonClient.exe`. Its strings include `MasonRAT`, `MasonGroup`, `NeptuneRAT V5.3`, and the C2 configuration `afxwd[.]ddns[.]net:143`. This indicates that UpCrypter is the delivery and loading framework, while the malware deployed in this case is NeptuneRAT, also labelled MasonRAT by its own configuration.

The sandbox behavior supports this conclusion. Joe Sandbox captured `sgyof.ps1` as a dropped file and detected NeptuneRAT in PowerShell memory dumps and unpacked PE artifacts. Other sandboxes stopped earlier in the chain, likely because the loader checks for analysis environments and specifically includes sandbox-related process names. This explains why some environments observed only `gdwfw.txt`, `tpkws.txt`, or `np.txt`, while Joe Sandbox progressed far enough to recover the final PowerShell stage.

For defenders, the user-facing lesson is simple: an HTML attachment that immediately redirects to a document download page should be treated as hostile, especially when the email uses generic invoice language and high-priority headers. For analysts, the important point is that the campaign is not a single malware family from the first stage onward. It is a layered delivery chain where UpCrypter stages and executes a final RAT payload.

## Indicators of Compromise

### URLs and domains

| Type | Indicator |
| --- | --- |
| Redirect landing page | `https://pillarsesolution[.]com/i#<base64-email>` |
| Download handler | `https://bonanza.davidsabido[.]com/wp-includes/images/ic/i.php` |
| ZIP payload | `https://bonanza.davidsabido[.]com/wp-includes/images/ic/B00225511855210021-00551.zip` |
| Decoy PDF | `https://drive.google.com/file/d/1XASle6sijkTrXEX_Elyk0C_R5uP33Oe-/view` |
| Stage host | `andrefelipedonascime1778799406970.2241107.meusitehostgator[.]com[.]br` |
| Stage URL | `https://andrefelipedonascime1778799406970.2241107.meusitehostgator[.]com[.]br/GpazlLUWIJ_14_05_Meus_ArquivosDeTexto/03.txt` |
| Secondary payload URL | `https://viveturetiro[.]mx/np.txt` |
| C2 | `afxwd[.]ddns[.]net:143` |

### Files and hashes

| File | SHA-256 |
| --- | --- |
| `R Nostra fattura nr. 91B.eml` | `1d4b0079863f439199fa58f83ff85d229685f652042eb2f0181008c0cc38b3cb` |
| `Fattura_00121.html` | `c3114ff7d4837dd11334ef841f5861e834efea948c56c72d1f64c1e93a5fa2fa` |
| `B00225511855210021-00551.zip` | `5437ccfa4cd32dff8908884a8ca328e6b7b8fd4b41ad78344668c60baed7c556` |
| `B00225511855210021-00551.js` | `bd56e7dd350b63c5492ebac88bcb8f2a9a45c0c0050f52f786dcae948eab9145` |
| `01.txt` | `2f2b5290c5339b94d80342172590f17300150870ea9416ab6661e1cb38c9ac0d` |
| `03.txt` / `gdwfw.txt` | `fa894470086ee4fb5ee581b398b0828f22e9397aa840a2f79dd2945e867220b3` |
| `np.txt` | `3d9b98e3aa9b467d08d5f21648d629228766af2...