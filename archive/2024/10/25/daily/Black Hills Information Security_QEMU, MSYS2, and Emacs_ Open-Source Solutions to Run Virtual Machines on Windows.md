---
title: QEMU, MSYS2, and Emacs: Open-Source Solutions to Run Virtual Machines on Windows
url: https://www.blackhillsinfosec.com/qemu-msys2-and-emacs/
source: Black Hills Information Security
date: 2024-10-25
fetch_date: 2025-10-06T18:51:58.307998
---

# QEMU, MSYS2, and Emacs: Open-Source Solutions to Run Virtual Machines on Windows

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

24
Oct
2024

[Dave Blandford](https://www.blackhillsinfosec.com/category/author/dave-blandford/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/)
[QEMU](https://www.blackhillsinfosec.com/tag/qemu/), [virtual machines](https://www.blackhillsinfosec.com/tag/virtual-machines/), [VM](https://www.blackhillsinfosec.com/tag/vm/)

# [QEMU, MSYS2, and Emacs: Open-Source Solutions to Run Virtual Machines on Windows](https://www.blackhillsinfosec.com/qemu-msys2-and-emacs/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/10/DBlandford-150x150.png)

| [Dave Blandford](https://www.blackhillsinfosec.com/team/david-blandford/)

*Penetration Tester. Developer. Pure GNU/Linux Phone Enthusiast*.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/10/BLOG_chalkboard_00694-1.png)

As a tester, I do all my work inside a Virtual Machine (VM). Recently, I found myself in a situation where I needed to get a VM on a Windows PC. The problem is, I did not want to create an account with Broadcom or work with VirtualBox. I needed to get QEMU (<https://www.qemu.org/>), the Quick Emulator, up and running. QEMU is open-sourced (always a win in my book!) and allows for running virtual machines from a qcow2 image.

That started the quest to find a decent QEMU walkthrough to get started and one did not exist, so I decided to write my own.

QEMU is both an emulator and a virtualizer. As an emulator, QEMU can run VMs that use a different architecture than your host. Android Virtual Device (AVD), for example, uses QEMU to run ARM-based Android systems regardless of your host’s physical architecture. This feature is especially useful in the event you are working with IoT firmware, where translating instructions between the two architectures can be difficult/cumbersome/impossible.

As a virtualizer, QEMU uses hardware virtualization on the host to create a virtual machine.

Whatever your requirements, QEMU can do both!

On to how to get QEMU to work with Windows. I could install QEMU directly on the Windows PC, but that would require manual configuration and managing dependencies. I wanted the easy button. I also wanted to use an open-source project to accomplish this. That is where MSYS2 (<https://www.msys2.org/>) came in. An open-sourced project, MSYS2 gave me the UNIX shell I wanted to set up QEMU, which is more native to QEMU’s design. MSYS2 automatically handles the dependencies, saving time. Also, it has an Arch Linux vibe and uses Pacman package manager so bonus points! Keep in mind that when you install MSYS2, multiple terminals will be installed. For this write-up, we are using MSYS2 MinGW 64-bit shell. This shell gives us a native Windows environment.

Installing MSYS2 is as easy as downloading the installer and running the installer. Once you install MSYS2, open a MSYS2 terminal, update the package databases, and install QEMU:

Update:

```
pacman -Syu
```

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/10/image-8-500x426.png)

Updating Using Pacman

Install:

```
pacman -S mingw-w64-x86_64-qemu
```

Verify the install:

```
qemu-system-x86_64 --version
```

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/10/image-4-1024x208.png)

Installed Version of QEMU 9.1.0

Awesome – QEMU is up and running. Next, download your favorite GNU Linux distro (I guess you could use Windows, and there are BSD people out there, but we are sticking with GNU Linux). We are grabbing a 64-bit Kali virtual machine image for this walkthrough, which will give us a virtualized environment.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/10/image-14-1024x519.png)

Downloading the Kali qcow2 Image

Once you have your image, create a snapshot if you would like. You will more than likely need to run this from a MYSYS2 console opened as Administrator:

```
qemu-img create -f qcow2 -F qcow2 -b "C:\path\to\image\kali-linux-2024.2-qemu-amd64.qcow2" "C:\path\to\snapshot\kali-snapshot.qcow2"
```

Then, running this command will give you a Kali VM. A description of the flags is provided in the comments:

```
qemu-system-x86_64 \
        #Uses a modern PC chipset model and enables Windows Hypervisor Platform
        -machine type=q35,accel=whpx \
        #Basic x86_64 CPU model.
        -cpu qemu64 \
        #2 CPU cores to VM
        -smp 2 \
        #4GB of RAM
        -m 4G \
        #Path to qcow2 image. MSYS2 also accepts this format: /c/Path/to/snapshot
        -drive file="C:\Path\to\your\kali-snapshot.qcow2",format=qcow2,if=virtio \
        #virtuio GPU for performance
        -vga virtio \
        #Display is using SDL
        -display sdl \
        #S...