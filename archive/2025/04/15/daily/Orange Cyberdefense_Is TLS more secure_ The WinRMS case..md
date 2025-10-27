---
title: Is TLS more secure? The WinRMS case.
url: https://sensepost.com/blog/2025/is-tls-more-secure-the-winrms-case./
source: Orange Cyberdefense
date: 2025-04-15
fetch_date: 2025-10-06T22:05:18.704421
---

# Is TLS more secure? The WinRMS case.

# [![Orange Cyberdefense](/img/master-logo.svg) ![](/images/orange-logo-small.svg) ![Orange Cyberdefense](/img/logo-text-x.svg)](/)

* [![Orange Cyberdefense](/img/master-logo.svg)

  ![](/images/orange-logo-small.svg)

  ![Orange Cyberdefense](/img/logo-text-x.svg)](/)

# Our Blog

* [2025 (16)](/blog/2025/)
* [2024 (10)](/blog/2024/)
* [2023 (19)](/blog/2023/)
* [2022 (10)](/blog/2022/)
* [2021 (13)](/blog/2021/)
* [2020 (30)](/blog/2020/)
* [2019 (10)](/blog/2019/)
* [2018 (14)](/blog/2018/)
* [2017 (27)](/blog/2017/)
* [2016 (22)](/blog/2016/)
* [2015 (17)](/blog/2015/)
* [2014 (15)](/blog/2014/)
* [2013 (30)](/blog/2013/)
* [2012 (27)](/blog/2012/)
* [2011 (33)](/blog/2011/)
* [2010 (36)](/blog/2010/)
* [2009 (81)](/blog/2009/)
* [2008 (75)](/blog/2008/)
* [2007 (80)](/blog/2007/)

# Is TLS more secure? The WinRMS case.

Reading time
~10 min

*Posted
by aurelien.chalot@orangecyberdefense.com
on
14 April 2025*

Categories:
[Active directory](/blog/active%20directory/),
[Ntlm](/blog/ntlm/),
[Relay](/blog/relay/),
[Winrm](/blog/winrm/)

## 0/ TL;DR

WinRM is protected against NTLMRelay as communications are encrypted. However WinRMS (the one communicating over HTTPS) is not entirely. That said, WinRMS is not configured on a default server installation (while WinRM is). So, if someone tried to harden their servers’ configurations (by removing the HTTP endpoint), they would open a new possible target that can be used to relay HTTP/SMB and LDAP NTLMv1 only authentications to WinRMS and thus gain remote code execution.

## **I/ Stupidest idea becoming an actual thing**

At the end of my talk at Insomni’hack 2025 about Browser Cache Smuggling, I said that “most of the time, huge innovations come from the stupidest and/or smallest idea”. What you are going to read is a perfect example of these words.

Six months ago I was doing an internal assessment in which the client had a super strong security baseline. No known CVE’s exposed, no relay possibilities… Nothing that could be used. Except a missconfigured server that was administrator of another one (that’s a classic SCCM configuration). Thing is, even if you can trigger an authentication from a server to another one, it won’t be useful if:

* SMB and LDAP are signed ;
* LDAP channel binding is set ;
* ESC8 is patched.

Turns out, all of these protections were set… Is it game over ? Well yes but no. A client may be secured against known exploits but what about those even us, hackerz, are not yet aware of ? That in mind, I started looking for new potential exploits.

Especially there are two things we deeply like for internal AD assessments:

* Ways of coercing a HTTP authentication (such as webdav) since those ones do not support signing/channel binding ;
* Endpoints to which we can coerce HTTP authentication since, most of the time they are not protected either!

And now let me introduce our new target:

![](/img/pages/blog/2025/is-tls-more-secure-the-winrms-case./image-4.png)

WinRM!

## **II/ What’s WinRM**

WinRM (Windows Remoting) is a specific protocol used to manage Windows computers and servers through an API exposed on a web server. WinRM comes with two versions:

* Classic WinRM exposed on port 5985;
* TLS encapsulated WinRM exposed on port 5986.

From a hacker point of view, WinRM looks like a promising target as it is exposed unencrypted. As such, it should be possible to relay SMB/LDAP/HTTP NTLM authentication to that endpoint. And it worked… Until I realise that even if WinRM does expose itself on HTTP, its communications are actually encrypted:

![](/img/pages/blog/2025/is-tls-more-secure-the-winrms-case./image-5-1224x472.png)

Sucks right? Sucks even more when I realised that encryption is done via a key derived from the user’s password… Naively I thought that WinRMS would be protected too, but as it turns, data is not encrypted inside the TLS tunnel! I mean, why would they? TLS is already encrypted stuff. Last thing I needed to know is whether channel binding is enabled on WinRMS. People said yes but ultimately I asked the question on Twitter and @filip\_dragovic replied with this screenshot:

![](/img/pages/blog/2025/is-tls-more-secure-the-winrms-case./image-6-1224x612.png)

This is quite interesting because the paper says that relay to WinRMS should not work, even thought it also says that Channel Binding (CBT) is set to “Relaxed” in the WinRM configuration. However, Channel Binding, which is used to protect NTLM authentication by binding it to a TLS session, can be configured with one of the following three values:

* None: Channel Binding is not supported (that’s the default configuration for ADCS HTTPS web enrolment) ;
* Strict: Channel Binding is required. If not sent by the client, the server must NOT process the request ;
* Relaxed: Channel Binding is optional. If the client sends it then the server protects the communication otherwise it does not.

Sounds interesting right? :D

## **III/ Weaponizing the relay**

That information got me thinking that there is something we can do here. But I forgot about it until @EAGAIIN asked for any new information, which ultimately led me into getting back to that subject. All I had to do was to create a new relay server/client for WinRM on NTLMRelayX which I started doing… Until I found [foofus’s github repo](https://github.com/jmk-foofus/impacket/issues/1) which already provided most of the things I needed! So I’m not going deep dive into the internals of NTLMRelayX because most of it is really all about catching the NTLM authentication and forwarding it to another target. However, let’s check what the WinRM protocol looks like.

First of all, WinRM is a protocol that relies on, mostly, four XML files. The first one is used to initiate a “ShellId” that will be used in all our future calls:

```
<?xml version="1.0" encoding="utf-8"?>
<env:Envelope
    xmlns:env="http://www.w3.org/2003/05/soap-envelope"
    xmlns:a="http://schemas.xmlsoap.org/ws/2004/08/addressing"
    xmlns:w="http://schemas.dmtf.org/wbem/wsman/1/wsman.xsd"
    xmlns:p="http://schemas.microsoft.com/wbem/wsman/1/wsman.xsd"
    xmlns:rsp="http://schemas.microsoft.com/wbem/wsman/1/windows/shell">

    <env:Header>
        <a:To>http://windows-host:5985/wsman</a:To>
        <a:ReplyTo>
            <a:Address mustUnderstand="true">
                http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous
            </a:Address>
        </a:ReplyTo>
        <a:MessageID>uuid:2a8ac24f-00f0-4a87-860c-bf58d33a1e0a</a:MessageID>
        <a:Action mustUnderstand="true">
            http://schemas.xmlsoap.org/ws/2004/09/transfer/Create
        </a:Action>
        <w:ResourceURI mustUnderstand="true">
            http://schemas.microsoft.com/wbem/wsman/1/windows/shell/cmd
        </w:ResourceURI>
        <w:OperationTimeout>PT20S</w:OperationTimeout>
        <w:MaxEnvelopeSize mustUnderstand="true">153600</w:MaxEnvelopeSize>
        <w:OptionSet>
            <w:Option Name="WINRS_NOPROFILE">FALSE</w:Option>
            <w:Option Name="WINRS_CODEPAGE">437</w:Option>
        </w:OptionSet>
        <w:Locale xml:lang="en-US"/>
        <p:DataLocale xml:lang="en-US"/>
    </env:Header>

    <env:Body>
        <rsp:Shell>
            <rsp:InputStreams>stdin</rsp:InputStreams>
            <rsp:OutputStreams>stdout stderr</rsp:OutputStreams>
        </rsp:Shell>
    </env:Body>
</env:Envelope>
```

Nothing interesting in that file to me. The only thing to remember is that sending that XML content will end up in the server sending you back a ShellID (a UUID). Now that you have that ID, you can send another XML file in which you will provide the command you want to launch:

```
<?xml version="1.0" encoding="utf-8"?>
<env:Envelope
    xmlns:env="http://www.w3.org/2003/05/soap-envelope"
    xmlns:a="http://schemas.xmlsoap.org/ws/2004/08/addressing"
    xmlns:w="http://schemas.dmtf.org/wbem/wsman/1/wsman.xsd"
    xmlns:rsp="http://schemas.microsoft.com/wbem/wsman/1/windows/shell">

    <env:...