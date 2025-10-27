---
title: 以公私钥方式登录SSH Server
url: http://blog.nsfocus.net/ssh-server/
source: 绿盟科技技术博客
date: 2023-02-23
fetch_date: 2025-10-04T07:51:14.899426
---

# 以公私钥方式登录SSH Server

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# 以公私钥方式登录SSH Server

### 以公私钥方式登录SSH Server

[2023-02-22](https://blog.nsfocus.net/ssh-server/ "以公私钥方式登录SSH Server")[scz](https://blog.nsfocus.net/author/scz/ "View all posts by scz")

阅读： 4,410

## 一、背景介绍

公网上有台Ubuntu 22，考虑到暴力猜测SSH密码太疯狂，应该只允许公私钥方式登录SSH，端口应该开在非标端口。初始有个非标端口、随机生成的密码，先用密码登录，再配置公私钥登录。意外发现两个Windows客户端公私钥登录失败，排查后发现是服务端OpenSSH版本过高，出现向后不兼容的安全升级，而客户端较旧，两相一凑，歇菜。出于各种综合考虑，以向后兼容为主要矛盾，对此记录一番。

从安全角度讲，C/S两侧都升至最新版是最佳选择，但现实世界中不这样干的原因有很多。

## 二、生成公私钥

ssh-keygen -q -C “<comment>” -t rsa -b 4096 -N “<passphrase>” -m PEM -f rsa\_4096
ls -l rsa\_4096\*

ssh-keygen生成两个文件，扩展名为.pub的是公钥，没有扩展名的是私钥，公钥需要上传到目标SSH Server。不喜欢所谓免密登录，指定了<passphrase>。

新版ssh-keygen默认不再是”-m PEM”，而是OpenSSH自己的一种新格式。某些旧版SecureCRT不认新格式私钥，为此必须给ssh-keygen显式指定”-m PEM”生成旧版私钥。

rsa\_4096形如

—–BEGIN RSA PRIVATE KEY—–
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,…
…
—–END RSA PRIVATE KEY—–

作为对比，OpenSSH新版私钥形如

—–BEGIN OPENSSH PRIVATE KEY—–
…
—–END OPENSSH PRIVATE KEY—–

从安全性讲，应该用新版私钥，从向后兼容性讲，用旧版私钥。

rsa\_4096.pub形如

ssh-rsa …== <comment>

## 三、/etc/ssh/sshd\_config

PermitRootLogin yes
StrictModes yes
Protocol 2
# RSAAuthentication yes
PubkeyAuthentication yes
PubkeyAcceptedAlgorithms +ssh-rsa
AuthorizedKeysFile .ssh/authorized\_keys
PasswordAuthentication yes

将Protocol设为2，避免使用脆弱的1。注释掉RSAAuthentication，该选项只为1所用。测试阶段将PasswordAuthentication设为yes，公私钥方式登录SSH成功后再改成no。是否允许root远程登录看情况。

重启sshd使配置生效

service sshd restart

## 四、 $HOME/.ssh/authorized\_keys

在目标SSH Server上执行

mkdir -p $HOME/.ssh
chmod 0500 $HOME/.ssh
cat rsa\_4096.pub >> $HOME/.ssh/authorized\_keys
chown -R <user> $HOME/.ssh
chmod 0600 $HOME/.ssh/authorized\_keys

其实就是将公钥内容放入authorized\_keys，chown、chmod是防止sshd以不安全为由拒绝使用authorized\_keys。

$HOME/.ssh/known\_hosts(0644)是Linux作为SSH Client使用时自动生成的，与本文无关。

## 五、WinSCP

WinSCP和PuTTY必须使用some.ppk这种格式的私钥，可用puttygen完成格式转换

————————————————————————–
<path>\putty\puttygen.exe
Load
rsa\_4096
Save private key
rsa\_4096.ppk
————————————————————————–

rsa\_4096.ppk形如

————————————————————————–
PuTTY-User-Key-File-2: ssh-rsa
Encryption: aes256-cbc
Comment: imported-openssh-key
Public-Lines: 12
…
Private-Lines: 28
…
Private-MAC: …
————————————————————————–

WinSCP需要对目标站点配置私钥

————————————————————————–
WinSCP
Advanced Site Settings
SSH
Authentication
Private key file
rsa\_4096.ppk
————————————————————————–

我用WinSCP 5.17.8，Ubuntu 22中是OpenSSH 8.9p1，这两个C/S配对时存在兼容性问题。若服务端没有”PubkeyAcceptedAlgorithms +ssh-rsa”，WinSCP 5.17.8公私钥登录时提示”Server refused our key”；WinSCP 5.20做了安全增强，无需修改服务端配置。

参[3]，里面有一段

2021-10-12 17:36, OpenSSH 8.8 disabled ssh-rsa by default. Until WinSCP
5.20 is released, add this to server’s sshd\_config to re-enable it:

PubkeyAcceptedAlgorithms +ssh-rsa

Ubuntu 20中是OpenSSH\_8.2p1，没这幺蛾子。

## 六、SecureCRT

SecureCRT 7.3.3密码登录Ubuntu 22时失败

Key exchange failed.

No compatible key exchange method. The server supports these methods:

curve25519-sha256,
curve25519-sha256@libssh.org,
ecdh-sha2-nistp256,
ecdh-sha2-nistp384,
ecdh-sha2-nistp521,
sntrup761x25519-sha512@openssh.com,
diffie-hellman-group-exchange-sha256,
diffie-hellman-group16-sha512,
diffie-hellman-group18-sha512,
diffie-hellman-group14-sha256

No compatible cipher. The server supports these ciphers:

chacha20-poly1305@openssh.com,
AES-128-CTR,
AES-192-CTR,
AES-256-CTR,
aes128-gcm@openssh.com,
aes256-gcm@openssh.com

意思是说服务端支持上面这一堆，但客户端当前配置不支持。

检查SecureCRT的”Session Options”，下面是一种方案，充分非必要

————————————————————————–
Connection
SSH2
Authentication
Password
Key exchange
ecdh-sha2-nistp256
Advanced
Cipher
AES-256-CTR
MAC
SHA2-256
————————————————————————–

先用Password登录成功，再配置公私钥登录

————————————————————————–
Connection
SSH2
Authentication
Publickey
Properties
Use session public key setting
Use identity or certificate file
rsa\_4096
————————————————————————–

SecureCRT 7.3.3不认OpenSSH新版私钥

ssh-keygen -q -C “test” -t rsa -b 4096 -N “test” -f test\_4096

用test\_4096时，SecureCRT 7.3.3提示

————————————————————————–
The private key file could not be found

Note that the public key file and private key file must have the same name(e.g., “Identity.pub” and “Identity”) and must be located in the same
folder.

Unknown file format
————————————————————————–

过去的套路突然不灵，起初我挺懵逼的，后来无意中发现新旧私钥格式不一样，问ChatGPT如何生成旧版私钥，从它的回答中意识到ssh-keygen可以指定生成哪种格式的私钥，在man手册中看到

By default OpenSSH will write newly-generated private keys in its own format. Setting a format of “PEM” when generating a supported private key
type will cause the key to be stored in the legacy PEM private key format.

ssh-keygen的缺省值变了，为了保持向后兼容性，应该”ssh-keygen -m PEM”。

SecureCRT 7.3.3与Ubuntu 22中的OpenSSH 8.9p1，这两个C/S配对时存在兼容性问题。若服务端没有”PubkeyAcceptedAlgorithms +ssh-rsa”，SecureCRT 7.3.3公私钥登录时提示

————————————————————————–
Public-key authentication with the server for user scz failed. Please verify username and public/private key pair.

The client has disconnected from the server. Reason: Unable to authenticate using any of the configured authentication methods.
————————————————————————–

假设没有先验知识，只根据上述提示，很难定位PubkeyAcceptedAlgorithms，这个提示不合格。新版SecureCRT应该有安全增强，无需修改服务端配置，未实测。

实测SecureCRT 7.3.3不支持rsa-sha2-512、ed25519(ecdsa)。

## 七、 Linux SSH Client

服务端没有”PubkeyAcceptedAlgorithms +ssh-rsa”时，旧版SecureCRT、WinSCP公私钥登录失败，之前以为是不加此配置时服务端不认RSA公钥。意外发现服务端不加此配置时Linux SSH Client公私钥登录成功，用的是同一套RSA公私钥，那就不是服务端不认RSA公钥，应该有其他合理解释，与协商过程强相关，这让我对公私钥登录流程产生好奇。

用Linux SSH Client时，注意私钥权限最小化，否则拒绝使用

chmod 0400 rsa\_4096
ssh -i rsa\_4096 <user>@<host>

查看SSH Server/Client版本

$ sshd -V
OpenSSH\_8.9p1 Ubuntu-3, OpenSSL 3.0.2 15 Mar 2022

$ ssh -V
OpenSSH\_8.4p1 Debian-3, OpenSSL 1.1.1i 8 Dec 2020

查看客户端连接指定站点时所用配置

$ ssh -G -i rsa\_4096 <user>@<host>
…
hostkeyalgorithms …,rsa-sha2-512,rsa-sha2-256,ssh-rsa
…
pubkeyacceptedkeytypes …,rsa-sha2-512,rsa-sha2-256,ssh-rsa
…

查看客户端支持的(签名)算法

$ ssh -Q sig
ssh-ed25519
sk-ssh-ed25519@openssh.com
ssh-rsa
rsa-sha2-256
rsa-sha2-512
ssh-dss
ecdsa-sha2-nistp256
ecdsa-sha2-nistp384
ecdsa-sha2-nistp521
sk-ecdsa-sha2-nistp256@openssh.com
webauthn-sk-ecdsa-sha2-nistp256@openssh.com

rsa-sha2-512/rsa-sha2-256/ssh-rsa三者公私钥都用RSA，签名算法分别用SHA-512、SHA-256、SHA-1。

参[1]

————————————————————————–
HostkeyAlgorithms

the public key algorithms accepted for an SSH server to authenticate itself to an SSH client

PubkeyAcceptedKeyTypes

(ssh/sshd): the public key algorithms that will be attempted by the client, and accepted by the server for public-key authentication (e.g.
via .ssh/authorized\_keys)
————————————————————————–

客户端用PubkeyAcceptedKeyTypes指定用哪种(签名)算法，而非HostKeyAlgorithms。

rm $HOME/.ssh/known\_hosts
ssh -i rsa\_4096 -o PubkeyAcceptedKeyTypes=rsa-sha2-256 <user>@<host>

上述命令登录成功，等价于无”-o”参数的默认情形

rm $HOME/.ssh/known\_hosts
ssh -i rsa\_4096 -o PubkeyAcceptedKeyTypes=ssh-rsa <user>@<host>

上述命令登录失败，相当于模拟了旧版SecureCRT、WinSCP登录失败的情形，后两者无法指定PubkeyAcceptedKeyTypes。

☆ /var/log/auth.log

前述登录失败是旧版Client对新版Server，也有反过来的，同样可能失败，参[2]。C/S两侧在协商过程中向对方展示己方支持的算法，只要存在交集，就能成功，反之失败。从运维角...