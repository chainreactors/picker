---
title: evil-winrm v4.1
url: https://kitploit.com/en/posts/github-hackplayers-evil-winrm-v41
source: Kitploit
date: 2026-09-04
fetch_date: 2026-09-05T06:28:23.022932
---

# evil-winrm v4.1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/2709/77875912286a99ed7f1d4f7f77dc32d6219355545785a93a7b3515d19c682958.png)

New releaseSep 4, 2026

# evil-winrm v4.1

The ultimate WinRM shell for hacking/pentesting

Share

# Evil-WinRM [![Version-shield](https://img.shields.io/badge/version-4.1-blue.svg?style=flat-square&colorA=273133&colorB=0093ee "Latest version")](https://raw.githubusercontent.com/Hackplayers/evil-winrm/master/evil-winrm.rb) [![Ruby2.3-shield](https://img.shields.io/badge/ruby-2.3+-blue.svg?style=flat-square&colorA=273133&colorB=ff0000 "Ruby 2.3 or later")](https://www.ruby-lang.org/en/news/2015/12/25/ruby-2-3-0-released/) [![Gem-Version](https://img.shields.io/gem/v/evil-winrm?style=flat-square&colorA=273133&colorB=46c249 "Ruby gem")](https://rubygems.org/gems/evil-winrm) [![License-shield](https://img.shields.io/badge/license-LGPL%20v3+-blue.svg?style=flat-square&colorA=273133&colorB=bd0000 "LGPL v3+")](https://raw.githubusercontent.com/Hackplayers/evil-winrm/master/LICENSE) [![Docker-shield](https://github.com/Hackplayers/evil-winrm/actions/workflows/master.yml/badge.svg?branch=master "Docker CI master")](https://github.com/Hackplayers/evil-winrm/actions/workflows/master.yml)

The ultimate WinRM shell for hacking/pentesting

![Banner](https://assets.kitploit.com/production/public/readmes/2709/6e61b1e6b393919b453743344d1108dbb1952a95d894652af6717658198d9c58.png)

## Description & Purpose

This shell is the ultimate WinRM shell for hacking/pentesting.

WinRM (Windows Remote Management) is the Microsoft implementation of WS-Management Protocol. A standard SOAP based protocol
that allows hardware and operating systems from different vendors to interoperate. Microsoft included it in their Operating
Systems in order to make life easier to system administrators.

This program can be used on any Microsoft Windows Servers with this feature enabled (usually at port 5985), of course only
if you have credentials and permissions to use it. So we can say that it could be used in a post-exploitation hacking/pentesting
phase. The purpose of this program is to provide nice and easy-to-use features for hacking. It can be used with legitimate
purposes by system administrators as well but the most of its features are focused on hacking/pentesting stuff.

It is based mainly in the WinRM Ruby library which changed its way to work since its version 2.0. Now instead of using WinRM
protocol, it is using PSRP (Powershell Remoting Protocol) for initializing runspace pools as well as creating and processing pipelines.

## Features

* Compatible to Linux and Windows client systems
* Load in memory Powershell scripts
* Load in memory dll files bypassing some AVs
* Load in memory C# (C Sharp) assemblies bypassing some AVs
* Load x64 payloads generated with awesome [donut](https://github.com/TheWover/donut) technique
* Dynamic AMSI Bypass to avoid AV signatures
* Pass-the-hash support
* Kerberos auth support including also ccache and kirbi files
* SSL and certificates support
* Upload and download files showing progress bar
* List remote machine services without privileges
* Command History
* WinRM command completion
* Local files/directories completion
* Remote path (files/directories) completion (can be disabled optionally)
* Colorization on prompt and output messages (can be disabled optionally)
* Optional logging feature
* Docker support (prebuilt images available at [Dockerhub](https://hub.docker.com/r/oscarakaelvis/evil-winrm))
* Trap capturing to avoid accidental shell exit on Ctrl+C
* Customizable user-agent using legitimate Windows default one
* ETW (Event Tracing for Windows) bypass

## Help

root@kitploit:~

```
Usage: evil-winrm -i IP -u USER [-s SCRIPTS_PATH] [-e EXES_PATH] [-P PORT] [-a USERAGENT] [-p PASS] [-H HASH] [-U URL] [-S] [-c PUBLIC_KEY_PATH ] [-k PRIVATE_KEY_PATH ] [-r REALM] [-K TICKET_FILE] [--spn SPN_PREFIX] [-l]
    -S, --ssl                        Enable ssl
    -c, --pub-key PUBLIC_KEY_PATH    Local path to public key certificate
    -k, --priv-key PRIVATE_KEY_PATH  Local path to private key certificate
    -r, --realm DOMAIN               Kerberos auth, it has to be set also in /etc/krb5.conf file using this format -> CONTOSO.COM = { kdc = fooserver.contoso.com }
    -K, --ccache TICKET_FILE        Path to Kerberos ticket file (ccache or kirbi format, auto-detected)
    -s, --scripts PS_SCRIPTS_PATH    Powershell scripts local path
        --spn SPN_PREFIX             SPN prefix for Kerberos auth (default HTTP)
    -e, --executables EXES_PATH      C# executables local path
    -i, --ip IP                      Remote host IP or hostname. FQDN for Kerberos auth (required)
    -U, --url URL                    Remote url endpoint (default /wsman)
    -u, --user USER                  Username (required if not using kerberos)
    -p, --password PASS              Password
    -H, --hash HASH                  NTHash
    -P, --port PORT                  Remote host port (default 5985)
    -a, --user-agent                 Specify connection user-agent (default Microsoft WinRM Client)
    -V, --version                    Show version
    -n, --no-colors                  Disable colors
    -N, --no-rpath-completion        Disable remote path completion
    -l, --log                        Log the WinRM session
    -h, --help                       Display this help message
```

## Requirements

Ruby 2.3 or higher is needed. Some ruby gems are needed as well: `winrm >=2.3.7`, `winrm-fs >=1.3.2`, `stringio >=0.0.2`, `logger >= 1.4.3`, `fileutils >= 0.7.2`, `readline ~> 0.0.4`, `readline-ext ~> 0.2.0`.
Depending of your installation method (4 availables) the installation of them could be required to be done manually.

Another important requirement only used for Kerberos auth is to install the Kerberos package used for network authentication.
For some Linux like Debian based (Kali, Parrot, etc.) it is called `krb5-user`. For BlackArch it is called `krb5` and probably it could be called in a different way for other Linux distributions.

The remote path completion feature requires the native `readline-ext` binding, which is installed automatically as an Evil-WinRM dependency. Some systems require additional development packages to compile it. Check [the section below](#Remote-path-completion) for more info.

## Installation & Quick Start (4 methods)

### Method 1. Installation directly as ruby gem (dependencies will be installed automatically on your system)

* Step 1. Install it (it will install automatically dependencies): `gem install evil-winrm`
* Step 2. Ready. Just launch it!

root@kitploit:~

```
evil-winrm  -i 192.168.1.100 -u Administrator -p 'MySuperSecr3tPass123!' -s '/home/foo/ps1_scripts/' -e '/home/foo/exe_files/'
```

### Method 2. Git clone and install dependencies on your system manually

* Step 1. Install dependencies manually: `sudo gem install winrm winrm-fs stringio logger fileutils readline readline-ext`
* Step 2. Clone the repo: `git clone https://github.com/Hackplayers/evil-winrm.git`
* Step 3. Ready. Just launch it!

root@kitploit:~

```
cd evil-winrm && ruby evil-winrm.rb -i 192.168.1.100 -u Administrator -p 'MySuperSecr3tPass123!' -s '/home/foo/ps1_scripts/' -e '/home/foo/exe_files/'
```

### Method 3. Using bundler (dependencies will not be installed on your system, just to use evil-winrm)

* Step 1. Install bundler: `gem install bundler`
* Step 2. Clone the repo: `git clone https://github.com/Hackplayers/evil-winrm.git`
* Step 3. Install dependencies with bundler: `cd evil-winrm && bundle install --path vendor/bundle`
* Step 4. Launch it with bundler:

root@kitploit:~

...