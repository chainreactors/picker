---
title: Refinery raid
url: https://blog.nviso.eu/2025/07/29/refinery-raid/
source: NVISO Labs
date: 2025-07-30
fetch_date: 2025-10-06T23:28:25.867128
---

# Refinery raid

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# Refinery raid

[Nick Foulon](https://blog.nviso.eu/author/nick-foulon/ "Posts by Nick Foulon")

[ICS](https://blog.nviso.eu/category/ics/), [Industrial Security](https://blog.nviso.eu/category/industrial-security/), [Awareness](https://blog.nviso.eu/category/awareness/), [Uncategorized](https://blog.nviso.eu/category/uncategorized/), [Cybersecurity](https://blog.nviso.eu/category/cybersecurity/), [NVISO](https://blog.nviso.eu/category/nviso/), [Operational Technology (OT)](https://blog.nviso.eu/category/uncategorized/operational-technology-ot/), [Tools](https://blog.nviso.eu/category/tools/), [Passwords](https://blog.nviso.eu/category/passwords/)

July 29, 2025July 29, 2025
13 Minutes

1. [Introduction](https://blog.nviso.eu/2025/07/29/refinery-raid/#introduction)
   1. [Purpose of the blogpost](https://blog.nviso.eu/2025/07/29/refinery-raid/#purpose-of-the-blogpost)
   2. [What is Labshock?](https://blog.nviso.eu/2025/07/29/refinery-raid/#what-is-labshock)
   3. [What Will We Do?](https://blog.nviso.eu/2025/07/29/refinery-raid/#what-will-we-do)
2. [Setting Up the Virtual Oil Plant](https://blog.nviso.eu/2025/07/29/refinery-raid/#setting-up-the-virtual-oil-plant)
   1. [Create Your Environment](https://blog.nviso.eu/2025/07/29/refinery-raid/#create-your-environment)
   2. [Install Labshock](https://blog.nviso.eu/2025/07/29/refinery-raid/#install-labshock)
      1. [Docker](https://blog.nviso.eu/2025/07/29/refinery-raid/#docker)
      2. [Download & build Labshock](https://blog.nviso.eu/2025/07/29/refinery-raid/#download-build-labshock)
      3. [Starting Labshock](https://blog.nviso.eu/2025/07/29/refinery-raid/#starting-labshock)
3. [Conducting the Hack](https://blog.nviso.eu/2025/07/29/refinery-raid/#conducting-the-hack)
   1. [Step 1: Reconnaissance](https://blog.nviso.eu/2025/07/29/refinery-raid/#step-1-reconnaissance)
   2. [Step 2: Explore the PLC & SCADA](https://blog.nviso.eu/2025/07/29/refinery-raid/#step-2-explore-the-plc-scada)
   3. [Step 3: Find the correct IP](https://blog.nviso.eu/2025/07/29/refinery-raid/#step-3-find-the-correct-ip)
   4. [Step 4: Interact with Modbus (Read Data)](https://blog.nviso.eu/2025/07/29/refinery-raid/#step-4-interact-with-modbus-read-data)
      1. [Modbus](https://blog.nviso.eu/2025/07/29/refinery-raid/#modbus)
      2. [Coils & Registers](https://blog.nviso.eu/2025/07/29/refinery-raid/#coils-registers)
      3. [Pump 1 & 2](https://blog.nviso.eu/2025/07/29/refinery-raid/#pump-1-2)
   5. [Step 5: Hack the Pumps (Write Data)](https://blog.nviso.eu/2025/07/29/refinery-raid/#step-5-hack-the-pumps-write-data)
      1. [Hack the pump (python) script:](https://blog.nviso.eu/2025/07/29/refinery-raid/#hack-the-pump-python-script)
      2. [Explanation of mbtget -w5 1 -a 0 {PLC\_HOST}](https://blog.nviso.eu/2025/07/29/refinery-raid/#explanation-of-mbtget-w5-1-a-0-plc-host)
   6. [Does this happen in real life?](https://blog.nviso.eu/2025/07/29/refinery-raid/#does-this-happen-in-real-life)
4. [Conclusion](https://blog.nviso.eu/2025/07/29/refinery-raid/#conclusion)
5. [Acknowledgments](https://blog.nviso.eu/2025/07/29/refinery-raid/#acknowledgments)
6. [Additional Resources](https://blog.nviso.eu/2025/07/29/refinery-raid/#additional-resources)
7. [Nick Foulon](https://blog.nviso.eu/2025/07/29/refinery-raid/#nick-foulon)

## Introduction

### Purpose of the blogpost

This blog post provides a step-by-step guide for setting up a virtual oil processing plant using <https://labshock.github.io/>. We will then demonstrate how to simulate a cyberattack by writing a custom python script. This exercise is designed for security professionals, engineers, and researchers interested in OT/ICS security.

### What is Labshock?

Labshock is a practical operational technology (OT) and industrial control systems (ICS) cybersecurity lab environment. It provides the opportunity to analyze industrial protocols, simulate cyber attacks, and test defensive strategies within a secure, virtualized setting. This environment mimics an industrial network, encompassing various devices that together manage the operations of an oil refinery.

There are not many “ready built” environments like this available for free, so a big thanks to Zakhar from Labshock for providing such a valuable resource. We need resources like Labshock to train and educate people in the field of ICS/OT, as they offer a hands-on approach to understanding and managing cybersecurity in industrial settings.

The primary focus will be on attacking the Programmable Logic Controller (PLC), which is responsible for managing and controlling process data, and the Supervisory Control and Data Acquisition (SCADA) system, which presents this data in real time. By modifying the data within the PLC, it is possible to affect the operational processes of the refinery.

![](https://blog.nviso.eu/wp-content/uploads/2025/06/image-15-1024x553.png)

website @ <https://labshock.github.io/>

### What Will We Do?

1. Set up the virtual oil plant with docker on Ubuntu
2. Explore its architecture and potential attack surfaces
3. Hack the pumps of the refinery via the Modbus protocol

## Setting Up the Virtual Oil Plant

### Create Your Environment

First, spin up a fresh (Ubuntu) Virtual Machine. This guide on installing Ubuntu in VMware can help: [https://medium.com/@florenceify74/how-to-download-install-and-run-ubuntu-in-vmware-workstation-ce5f2d4d0438](https://medium.com/%40florenceify74/how-to-download-install-and-run-ubuntu-in-vmware-workstation-ce5f2d4d0438). Of course, you are free to choose your own VM.

**Backups, Backups, and More Backups!**

Before moving further, create snapshots. One after the fresh Ubuntu install, another after Labshock is successfully running. It saves you hours if something breaks (and it will at one point).

![](https://blog.nviso.eu/wp-content/uploads/2025/06/952ab6e9c8fb67db31ddfccb8d32aea39f3b6362.png)

3-2-1 Backup Strategy <https://www.cisa.gov/sites/default/files/publications/data_backup_options.pdf>.

### Install Labshock

Follow the official <https://github.com/zakharb/labshock/wiki/Quickstart-Guide> guide to install Labshock on your host.

Below you will find all the code or scripts that I used to setup Labshock:

#### Docker

```
#!/bin/bash
set -e
# Uninstall old Docker versions
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do
    sudo...