---
title: Kali & LLM: Completely local with Ollama & 5ire
url: https://www.kali.org/blog/kali-llm-ollama-5ire/
source: Kali Linux
date: 2026-03-10
fetch_date: 2026-03-11T04:05:22.870461
---

# Kali & LLM: Completely local with Ollama & 5ire

* [Join Free CTF](https://www.offsec.com/events/the-gauntlet/?utm_source=kali&utm_medium=web&utm_campaign=menu)
* [Get Kali](https://www.kali.org/get-kali/)
* [Blog](https://www.kali.org/blog/)
* Documentation

  [Documentation Pages](https://www.kali.org/docs/)
  [Tools Documentation](https://www.kali.org/tools/)
  [Frequently Asked Questions](https://www.kali.org/faq/)
  [Known Issues](https://bugs.kali.org/search.php?project_id=1&category_id[]=General%20Bug&category_id[]=Kali%20Package%20Bug&category_id[]=Kali%20Package%20Improvement&status[]=30&status[]=40&status[]=50&sticky=on&sort=id%2Clast_updated&dir=DESC%2CDESC&hide_status=-2&match_type=0)
* Community

  [Community Support](https://www.kali.org/community/)
  [Forums](https://forums.kali.org/)
  [Discord](https://discord.kali.org/)
  [Join Newsletter](https://www.kali.org/newsletter/)
  [Mirror Location](https://http.kali.org/README?mirrorlist)
  [Get Involved](https://www.kali.org/docs/community/contribute/)
* [Courses](https://www.offsec.com/kali-training/courses/?utm_source=kali&utm_medium=web&utm_campaign=menu)
* Developers

  [Git Repositories](https://gitlab.com/kalilinux)
  [Packages](https://pkg.kali.org/)
  [Auto Package Test](https://autopkgtest.kali.org/)
  [Bug Tracker](https://bugs.kali.org/)
  [Kali NetHunter Stats](https://nethunter.kali.org/)
* About

  [Kali Linux Overview](https://www.kali.org/features/)
  [Press Pack](https://gitlab.com/kalilinux/documentation/press-pack/-/archive/main/press-pack-main.zip)
  [Wallpapers](https://www.kali.org/wallpapers/)
  [Kali Swag Store](https://offsec.usa.dowlis.com/kali/view-all.html)
  [Meet The Kali Team](https://www.kali.org/about-us/)
  [Partnerships](https://www.kali.org/partnerships/)
  [Contact Us](https://www.kali.org/contact/)

LIGHT
[ ] DARK

![](https://www.kali.org/blog/kali-llm-ollama-5ire/images/banner-kali-ollama-5ire.jpg)
Tuesday, 10 March 2026

# Kali & LLM: Completely local with Ollama & 5ire

Table of Contents

* [GPU (Nvidia)](#gpu-nvidia)
  + [Drivers](#drivers)
  + [Testing](#testing)
* [Ollama](#ollama)
  + [LLM](#llm)
  + [Testing](#testing-1)
* [MCP Server (MCP Kali Server)](#mcp-server-mcp-kali-server)
  + [Testing](#testing-2)
* [5ire](#5ire)
  + [Testing](#testing-3)
* [MCP Client (5ire)](#mcp-client-5ire)
  + [Testing](#testing-4)
* [Recap](#recap)

We are extending our LLM-driven Kali series, where natural language replaces manual command input. This time however, we are doing **everything locally and offline**. We are using our own hardware and not relying on any 3rd party services/SaaS.

*Note: Local LLMs are hardware-hungry. The cost factor here is buying hardware and the running costs. If you have anything that you can re-use, great!*

## GPU (Nvidia)

Let’s first find out what our hardware is:

```
$ lspci | grep -i vga
07:00.0 VGA compatible controller: NVIDIA Corporation GP106 [GeForce GTX 1060 6GB] (rev a1)
$
```

*NVIDIA GeForce GTX 1060 (6 GB).*

### Drivers

We will check that our hardware is ready by making sure “non-free” proprietary drivers are installed. The non-free option allows for CUDA support which the open-source, `nouveau`, drivers lack.
At the same time, make sure our Kernel and headers are at the latest version too:

```
$ sudo apt update
[...]
$
$ sudo apt install -y linux-image-$(dpkg --print-architecture) linux-headers-$(dpkg --print-architecture) nvidia-driver nvidia-smi
[...]
│ Conflicting nouveau kernel module loaded                                                                  │
│ The free nouveau kernel module is currently loaded and conflicts with the non-free nvidia kernel module.  │
│ The easiest way to fix this is to reboot the machine once the installation has finished.                  |
[...]
$
$ sudo reboot
```

Using a different GPU manufacture, such as AMD or Intel etc, is out of scope for this guide.

### Testing

Once the box is back up and we are logged in again, we can do a quick check with `nvidia-smi`:

```
$ lspci -s 07:00.0 -v | grep Kernel
  Kernel driver in use: nvidia
  Kernel modules: nvidia
$
$ lsmod | grep '^nouveau'
$
$ lsmod | grep '^nvidia'
nvidia_drm            126976  2
nvidia_modeset       1605632  3 nvidia_drm
nvidia              60710912  29 nvidia_drm,nvidia_modeset
$
$ nvidia-smi
Tue Jan 27 14:33:31 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.163.01             Driver Version: 550.163.01     CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce GTX 1060 6GB    Off |   00000000:07:00.0  On |                  N/A |
|  0%   30C    P8              6W /  120W |      25MiB /   6144MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A       969      G   /usr/lib/xorg/Xorg                             21MiB |
+-----------------------------------------------------------------------------------------+
$
```

Everything looks to be in order.

## Ollama

Next up, we need to install [Ollama](https://ollama.com/download/linux). Ollama will allow us to load our local LLM.
*Ollama is a wrapper for `llama.cpp`. 5ire supports Ollama, but not llama.cpp.*

If you do not want to-do `curl|bash`, see the [manual method](https://docs.ollama.com/linux), or follow below for `v0.15.2` *(latest at the time of writing, 2026-01-27)*:

```
$ sudo apt install -y curl
[...]
$
$ curl --fail --location https://ollama.com/download/ollama-linux-amd64.tar.zst > /tmp/ollama-linux-amd64.tar.zst
[...]
$
$ file /tmp/ollama-linux-amd64.tar.zst
/tmp/ollama-linux-amd64.tar.zst: Zstandard compressed data (v0.8+), Dictionary ID: None
$ sha512sum /tmp/ollama-linux-amd64.tar.zst
1c16259de4898a694ac23e7d4a3038dc3aebbbb8247cf30a05f5c84f2bde573294e8e612f3a9d5042201ebfe148f5b7fe64acc50f5478d3453f62f85d44593a1  /tmp/ollama-linux-amd64.tar.zst
$
$ sudo tar x -v --zstd -C /usr -f /tmp/ollama-linux-amd64.tar.zst
[...]
$
$ sudo useradd -r -s /bin/false -U -m -d /usr/share/ollama ollama
$
$ sudo usermod -a -G ollama $(whoami)
$
$ cat <<EOF | sudo tee /etc/systemd/system/ollama.service >/dev/null
[Unit]
Description=Ollama Service
After=network-online.target

[Service]
ExecStart=/usr/bin/ollama serve
User=ollama
Group=ollama
Restart=always
RestartSec=3
Environment="PATH=\$PATH"

[Install]
WantedBy=multi-user.target
EOF
$
$ sudo systemctl daemon-reload
$
$ sudo systemctl enable --now ollama
Created symlink '/etc/systemd/system/multi-user.target.wants/ollama.service' → '/etc/systemd/system/ollama.service'.
$
$ systemctl status ollama
● ollama.service - Ollama Service
     Loaded: loaded (/etc/systemd/system/ollama.service; enabled; preset: disabled)
     Active: active (running) since Tue 2026-01-27 14:44:39 GMT; 18s ago
[...]
$
$ ollama -v
ollama version is 0.15.2
$
```

The service is reporting to be active and running (and nothing is off in the logs files).

### LLM

Now we need an LLM for Ollama to run! There are a few places to find pre-generated LLMs:

* ...