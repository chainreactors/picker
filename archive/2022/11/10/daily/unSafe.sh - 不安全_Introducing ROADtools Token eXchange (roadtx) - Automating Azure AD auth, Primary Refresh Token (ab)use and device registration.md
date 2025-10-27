---
title: Introducing ROADtools Token eXchange (roadtx) - Automating Azure AD auth, Primary Refresh Token (ab)use and device registration
url: https://buaq.net/go-134915.html
source: unSafe.sh - 不安全
date: 2022-11-10
fetch_date: 2025-10-03T22:12:56.142960
---

# Introducing ROADtools Token eXchange (roadtx) - Automating Azure AD auth, Primary Refresh Token (ab)use and device registration

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/4cb71312e7c05a403b922e9a093c9610.jpg)

Introducing ROADtools Token eXchange (roadtx) - Automating Azure AD auth, Primary Refresh Token (ab)use and device registration

Ever since the initial release of ROADrecon and the ROADtools framework I have bee
*2022-11-9 19:8:57
Author: [dirkjanm.io(查看原文)](/jump-134915.htm)
阅读量:15
收藏*

---

Ever since the initial release of [ROADrecon](https://dirkjanm.io/introducing-roadtools-and-roadrecon-azure-ad-exploration-framework/) and the ROADtools framework I have been adding new features to it, especially on the authentication side. As a result, it supports many forms of authentication, such as using [Primary Refresh Tokens](https://dirkjanm.io/digging-further-into-the-primary-refresh-token/) (PRTs), PRT cookies, and regular access/refresh tokens. The authentication modules are all part of the shared library roadlib, and can be used in other tools by importing the library. Even though you can request tokens for any Azure AD connected resource and with many client IDs, the only tool exposing this authentication part was ROADrecon. It always felt unnatural and illogical to tell people that you can use a recon tool to request tokens for many other purposes. So I decided to start writing a new tool, which resolves around requesting and using Azure AD tokens. As I was working on this, I started adding proof of concepts I wrote during my Azure AD devices research into the tool, adding support for registering devices and requesting Primary Refresh Tokens using device credentials. I also added various modules for injecting PRTs into browser sessions with Selenium, and for automating authentication with MFA. The result is a comprehensive tool called ROADtools Token eXchange, or simply roadtx. Currently it has the following capabilities:

* Register and join devices to Azure AD.
* Request Primary Refresh Tokens from user credentials or other valid tokens.
* Use Primary Refresh Tokens in a similar way as the Web Account Manager (WAM) in Windows does.
* Perform several different Oauth2 token redemption flows.
* Perform interactive logins based on Browser SSO by injecting the Primary Refresh Token into the authentication flow.
* Add SSO capabilities to Chrome via the Windows 10 accounts plugin and a custom browsercore implementation.
* Automate sign-ins, MFA and token requesting to various resources in Azure AD by using Selenium.
* Possibility to load credentials and MFA TOTP seeds from a KeePass database to use in (semi-)automated flows.

In this blog I will describe the tools features and show some demonstrations of the cool stuff you can do with it. You can also skip directly to [GitHub](https://github.com/dirkjanm/ROADtools) or read the [Wiki](https://github.com/dirkjanm/ROADtools/wiki/ROADtools-Token-eXchange-%28roadtx%29) for details on each command.

roadtx is structured as a wrapper tool around features implemented in roadlib. With the release of roadtx, a new class has been added to roadlib with all device authentication logic, containing functions that register/join devices and can request or use Primary Refresh Tokens in the same way that Windows uses them. In roadtx itself, there is a class with helper functions for [Selenium](https://www.selenium.dev/)-based authentication and support for intercepting browser requests to add SSO features to the browser window.

The main function of roadtx itself is about 400 lines of code to construct an (I hope) straightforward collection of commands with their parameters. It also has about 300 lines of code to deal with the commands and call library functions with the data needed. The actual device logic being in roadlib means that it is possible to re-use it in other tools or to make light standalone tools without needing all the roadtx specific dependencies.

I’ve also tried to make it intuitive and straightforward to use roadtx, reducing the command line arguments needed to perform specific actions. For example, `roadtx device` will register a device with randomized defaults, and functions dealing with Primary Refresh Tokens will by default load the PRT from a `roadtx.prt` file, so you don’t have to specify it every time you use a function.

## Devices and Primary Refresh Tokens

Most of the modules of roadtx are designed around Primary Refresh Tokens and device identities. To obtain a PRT, we must first register a device in Azure AD. Registering a device requires an access token to the device registration service resource. The access token must be a token without a device claim, so you cannot use single sign-on or an existing PRT to request one. There are a few ways to obtain such a token with roadtx, where some methods support MFA and others do not. MFA could be required to register a device, depending on tenant settings. If it is not, you can request a token for the device registration service (specified here through the *devicereg* alias) with only a username and password:

If MFA is required, you can use the device authentication flow to request the tokens from a browser window somewhere:

```
roadtx gettokens --device-auth -r devicereg
```

Alternatively, we can already skip ahead a bit to the functionalities shown later in this blog, and use a Selenium based window for MFA, while autofilling the username + password:

Any of the commands above with save an access token to the `.roadtools_auth` file. The device registration command will automatically load it from this file. You can customize what you want for device properties with various commandline parameters to the `roadtx device` module:

![device command](https://dirkjanm.io/assets/img/roadtx/roadtx_device.png)

We register an Azure AD joined device with the name “blogdevice”:

```
roadtx device -n blogdevice
Saving private key to blogdevice.key
Registering device
Device ID: 5f138d8b-6416-448d-89ef-9b279c419943
Saved device certificate to blogdevice.pem
```

We get two pieces of data that identify our device. The first is the device certificate saved in `blogdevice.pem`, which is issued by Azure AD and identifies our device. The second part is the `blogdevice.key` file, which contains the private key of the certificate and is also used as transport key. Now that we have the device certificate, we can do operations that require a device identity. The most useful one is requesting a Primary Refresh Token, since that will enable us to add Single Sign On capabilities to our (interactive or automated) token requests.

### Requesting a Primary Refresh Token

A primary refresh token is most often requested with a username and password. When you log in to an Azure AD joined or hybrid joined workstation with your username and password, Windows immediately requests a PRT from Azure AD. I’ve talked about the technicalities behind this flow at my Troopers and Romhack [talks](https://dirkjanm.io/talks/) in the past, so if you’re interested in the technicalities have a read through those slides. To request a PRT with roadtx, run the `roadtx prt` command, specify the device cert/key and the username + password to use, and you get a PRT:

```
roadtx prt -u [email protected] -p password --key-pem blogdevice.key --cert-pem blogdevice.pem
```

The command will give us a PRT (in the form of an encrypted token), and a session key that we need to use the PRT. The PRT is by default saved to `roadtx.prt`, where it can be picked up by other roadtx modules.

A PRT is by default valid for 90 days, but we can renew it at any time to extend the validity for another 90 days with the `renew` action:

```
roadtx prt -a renew
Renewing PRT
Saved PRT to roadtx.prt
```

N...