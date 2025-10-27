---
title: Automating Windows installation in a VM
url: https://palant.info/2023/02/13/automating-windows-installation-in-a-vm/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-01
fetch_date: 2025-10-04T08:22:03.698600
---

# Automating Windows installation in a VM

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# Automating Windows installation in a VM

2023-02-13
 [Windows](/categories/windows/)/[Kvm](/categories/kvm/)
 6 mins
 [4 comments](/2023/02/13/automating-windows-installation-in-a-vm/#comments)

I recently switched from VirtualBox to KVM for my virtualization needs. While this approach has clear advantages such as not requiring custom kernel drivers, the downside is that snapshots arenât currently supported for Windows 11. And since I donât want applications I analyze to corrupt my main Windows VM, I decided that I should run these in freshly created Windows VMs.

The issue with this approach is: setting up a new Windows VM is fairly time-consuming. Not only is it necessary to answer a number of questions during installation, installing the proper guest tools for KVM is non-trivial as well. And I also rely on some further applications for my work.

Luckily, Windows installation supports [answer files](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11) which make this task far easier. With the right answer file and some scripts, setting up a Windows VM is a fully automated task that takes half an hour and none of my attention. The necessary information was rather scattered and often outdated, so I decided to put it all into one blog post.

![Screenshot of Windows Setup installing Windows](/2023/02/13/automating-windows-installation-in-a-vm/wininstall.png)

#### Contents

* [Preparing the installation medium](#preparing-the-installation-medium)
* [Creating an answer file](#creating-an-answer-file)
* [The custom setup scripts](#the-custom-setup-scripts)
* [Starting the installation process](#starting-the-installation-process)

## Preparing the installation medium

With current Windows versions, there is an official way of getting an installation medium: via [the Microsoft web page](https://www.microsoft.com/software-download/windows11). I asked for the Windows 11 x64 disk image in English and got a file named `Win11_22H2_English_x64v1.iso`.

This image needs to be modified in order to add the `autounattend.xml` file and any scripts required. On Linux, this is fairly easy. First, you need a copy of the data:

```
mkdir mnt
sudo mount -o loop Win11_22H2_English_x64v1.iso mnt
mkdir win11_iso
cp -r mnt/* win11_iso/
sudo umount mnt
rm -rf mnt
```

You could modify the data in the `win11_iso` directory, but itâs probably better to keep your modifications in a separate directory. This way you can easily replace `win11_iso` with a newer Windows version.

So letâs say you create a `win11_iso_modifications` directory for your additions like the `autounattend.xml` file. How does one create a new installation medium with these modifications? Today the magic incantation to produce the right kind of disk image appears to be:

```
mkisofs \
    -iso-level 4 \
    -rock \
    -disable-deep-relocation \
    -untranslated-filenames \
    -b boot/etfsboot.com \
    -no-emul-boot \
    -boot-load-size 8 \
    -eltorito-alt-boot \
    -eltorito-platform efi \
    -b efi/microsoft/boot/efisys_noprompt.bin \
    -o Win11_22H2_English_x64v1_modified.iso \
    win11_iso win11_iso_modifications
```

This will merge the original `win11_iso` directory with the additions from the `win11_iso_modifications` directory and produce `Win11_22H2_English_x64v1_modified.iso` disk image which can be used to install Windows.

## Creating an answer file

Much of the `autounattend.xml` boilerplate can be generated using the [online generator](https://schneegans.de/windows/unattend-generator/) created by Christoph Schneegans. You can choose the VMâs hard drive to be partitioned with GPT automatically, and you can select the user accounts you need. âFocus on privacyâ will automatically configure your system to transmit less data to Microsoft.

Some things can be improved of course. For example, I donât actually need a password to protect access to a temporary VM. According to the [Rufus tool](https://rufus.ie/), replacing the `<Password>` tag with the following undocumented value sets an empty password:

```
<Password>
  <Value>UABhAHMAcwB3AG8AcgBkAA==</Value>
  <PlainText>false</PlainText>
</Password>
```

I did not actually verify that Windows treats the string `Password` like an empty password because Iâve also set up autologon. This is highly recommendable as Windows will spend a fair deal of time setting up everything on first logon. So itâs better for this first logon to happen automatically after the installation.

The `<AutoLogon />` tag needs to be replaced by the following (use the user name you chose for your account):

```
<AutoLogon>
  <Username>Admin</Username>
  <Password>
    <Value>UABhAHMAcwB3AG8AcgBkAA==</Value>
    <PlainText>false</PlainText>
  </Password>
  <Enabled>true</Enabled>
  <LogonCount>9999999</LogonCount>
</AutoLogon>
```

Finally, answer files support running custom commands at various points of the installation process. This is useful to install required applications and to change settings. I tried doing most tasks in the `specialize` pass: the commands execute elevated here, so installers can run without stalling on an elevation prompt. I put everything required into a PowerShell script, this is easier to manage and to debug. To run the script, one would replace `<settings pass="specialize" />` in `autounattend.xml` with:

```
<settings pass="specialize">
  <component name="Microsoft-Windows-Deployment" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS">
    <RunSynchronous>
      <RunSynchronousCommand wcm:action="add">
        <Order>1</Order>
        <Path>powershell.exe -noprofile -ExecutionPolicy unrestricted C:\Windows\Setup\Scripts\InstallRequirements.ps1</Path>
      </RunSynchronousCommand>
    </RunSynchronous>
  </component>
</settings>
```

A few things cannot be customized on the operating system level however, these are specific to the user account you create. For example, you might want to change Windows Explorer settings so that it doesnât hide any files from you. This is another PowerShell script, executed during the first user logon. You put the following code after the `<AutoLogon>` block mentioned above:

```
<FirstLogonCommands>
  <SynchronousCommand wcm:action="add">
    <Order>1</Order>
    <CommandLine>powershell.exe -noprofile -ExecutionPolicy unrestricted C:\Windows\Setup\Scripts\FirstRun.ps1</CommandLine>
  </SynchronousCommand>
</FirstLogonCommands>
```

## The custom setup scripts

How do the scripts `InstallRequirements.ps1` and `FirstRun.ps1` get into our fresh Windows install? These need to be in the right directory of the installation medium, specifically the `$OEM$/$$/Setup/Scripts` directory. You create it inside your `win11_iso_modifications` directory and any files you put here will land in `C:\Windows\Setup\Scripts`.

I use PowerShell rather than plain batch files because PowerShell scripts can do a lot without requiring installation of third party tools. For example, they can both download and install SPICE Agent to enable clipboard sharing:

```
Invoke-WebRequest `
  -Uri https://www.spice-space.org/download/windows/vdagent/vdagent-win-0.10.0/spice-vdagent-x64-0.10.0.msi `
  -OutFile "C:\Windows\Temp\spice-vdagent.msi"
Invoke-Expression "msiexec /i C:\Windows\Temp\spice-vdagent.msi /qn /norestart"
```

Note that I chose not to install the full SPICE guest tools because the driver installation here will require a user confirmation. Instead, I install the drivers via virtio guest tools:

```
Invoke-WebRequest `
  -Uri https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/archive-virtio/virtio-win-0.1.229-1/virtio-win-gt-x64.msi `
  -OutFile "C:\Windows\Temp\virtio-gt.msi"
Invoke-Expression "msiexec /i C...