---
title: Making New Connections – Leveraging Cisco AnyConnect Client to Drop and Run Payloads
url: https://buaq.net/go-151571.html
source: unSafe.sh - 不安全
date: 2023-03-02
fetch_date: 2025-10-04T08:25:26.838132
---

# Making New Connections – Leveraging Cisco AnyConnect Client to Drop and Run Payloads

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

![](https://8aqnet.cdn.bcebos.com/7ad494c715b897677eb4c07e8504db0c.jpg)

Making New Connections – Leveraging Cisco AnyConnect Client to Drop and Run Payloads

The Cisco AnyConnect client has received a fair amount of scrutiny from the security communi
*2023-3-1 21:18:33
Author: [research.nccgroup.com(查看原文)](/jump-151571.htm)
阅读量:40
收藏*

---

The Cisco AnyConnect client has received a fair amount of scrutiny from the security community over the years, with a particular focus on leveraging the vpnagent.exe service for privilege escalation. A while ago, we started to look at whether AnyConnect could be used to deliver payloads during red team engagements and having used the technique successfully, it seemed appropriate to make the technique public.

TL;DR – the tool release can be found at:

<https://github.com/nccgroup/DroppedConnection>

## Working From Home

Most users are familiar with the concept of a VPN due to the increase in working-from-home, and how to make a VPN connection from their laptop (or at least knowing the software/icon that relates to the VPN connection). This increases odds on successful social engineering efforts using a VPN related pretext – users know what it is and can be walked through performing desired actions and more importantly, they need it so that they can continue working remotely.

The function that the VPN provides means that we can assume a few things to be aware of when considering as a vector for payload deployment:

* TLS VPN connections are unlikely to be forced through a proxy, nor are they likely to actually have access to the corporate proxy when not connected to the corporate network – this means
  + No proxy logs for any connections
  + No filtering based on categorisation
* DNS requests will be resolved by a public server, rather than the target’s internal service, reducing telemetry
* Dropped payloads may not be able to connect to command and control infrastructure until the legitimate corporate VPN connection is re-established

## AnyConnect connection flow

A new VPN connection is initiated from the vpnui.exe process by supplying a fully qualified domain name:

![](https://i0.wp.com/research.nccgroup.com/wp-content/uploads/2022/08/anyconnect1.png?w=1100&ssl=1)

After the initial TLS handshake is complete, the VPN server sends an XML response, detailing the name of the VPN and the supported authentication methods. The example below shows a VPN name of TEST-VPN and that the server expects a username and password:

```
<?xml version="1.0" encoding="UTF-8"?>
<config-auth client="vpn" type="auth-request" aggregate-auth-version="2">
<opaque is-for="sg">
<tunnel-group>VPN</tunnel-group>
<aggauth-handle>864640002</aggauth-handle>
<auth-method>multiple-cert</auth-method>
<auth-method>single-sign-on</auth-method>
<group-alias>TEST-VPN</group-alias>
<config-hash>1517719014268</config-hash>
</opaque>
<auth id="main">
<form>
<input type="text" name="username" label="Username:"></input>
<input type="password" name="password" label="Password:"></input>
<select name="group_list" label="GROUP:">
<option selected="true">TEST-VPN</option>
</select>
</form>
</auth>
</config-auth>
```

The content of this XML response determines the appearance of the prompt for authentication, with the two main choices being:

* A username and password window, contained within the vpnui.exe process
* A web-based SAML login, rendered using acwebhelper.exe

In this scenario, we’ll focus on the standard username and password window that the XML above would cause to be displayed.

Credentials entered into this resulting window are sent to the VPN server in the body of a POST request. Assuming authentication is successful, the response contains information relating to:

* Any software upgrades that are available
* The profile that should be subsequently requested by the VPN client
* Any customisations, such as logos, locales or post-connection scripts

An example of this XML can be seen below:

```
<?xml version="1.0" encoding="UTF-8"?>
<config-auth client="vpn" type="complete" aggregate-auth-version="2">
<session-id>101111</session-id>
<session-token>[email protected]@[email protected]</session-token>
<auth id="success">
<message id="0" param1="" param2=""></message>
</auth>
<capabilities>
<crypto-supported>ssl-dhe</crypto-supported>
</capabilities>
<config client="vpn" type="private">
<vpn-base-config>
<base-package-uri>/CACHE/stc/1</base-package-uri>
<server-cert-hash>###SERVERCERT###</server-cert-hash>
</vpn-base-config>
<opaque is-for="vpn-client"><service-profile-manifest>
<ServiceProfiles rev="1.0">
  <Profile service-type="user">
    <FileName></FileName>
    <FileExtension>xml</FileExtension>
    <Directory></Directory>
    <DeployDirectory></DeployDirectory>
    <Description>AnyConnect VPN Profile</Description>
    <DownloadRemoveEmpty>false</DownloadRemoveEmpty>
  </Profile>
  <---REMOVED--->
</ServiceProfiles>
</service-profile-manifest>
<vpn-client-pkg-version>
<pkgversion>4,9,04053</pkgversion>
</vpn-client-pkg-version>
<vpn-core-manifest>
<vpn rev="1.0">
  <file version="4.9.04053" id="VPNCore" is_core="yes" type="msi" action="install" os="win:6.1.7601">
    <uri>binaries/anyconnect-win-4.9.04053-core-vpn-webdeploy-k9.msi</uri>
    <display-name>AnyConnect Secure Mobility Client</display-name>
  </file>
  <---REMOVED--->
</vpn>
</vpn-core-manifest>
</opaque>
<vpn-profile-manifest>
<vpn rev="1.0">
<file type="profile" service-type="user">
<uri>/CACHE/stc/profiles/profile_test.xml</uri>
<hash type="sha1">###PROFILEHASH###</hash>
</file>
</vpn>
</vpn-profile-manifest>
<vpn-customization-manifest>
<vpn rev="1.0">
<file app="AnyConnect" platform="win" type="binary">
<filename>scripts_OnDisconnect.vbs</filename>
<hash type="sha1">###VBSHASH###</hash>
<file app="AnyConnect" platform="win" type="binary">
<filename>scripts_OnConnect.vbs</filename>
<hash type="sha1">###VBSHASHTWO###</hash>
</file>
</file>
</vpn>
</vpn-customization-manifest>
</config>
</config-auth>
```

The .vbs files referenced in the customisation section are downloaded following the delivery of this XML and then executed as the authenticated user upon a successful connection being established and then terminated respectively. Usable file types are not restricted to .vbs but this (along with .bat) appears to be the most commonly used.

Finally, the referenced profile is requested by the VPN client and returned by the server. This also has an XML structure and determines which usability and security features should be enabled for the connection. This is an important as it allows any restrictions imposed by the user’s regular VPN profile to be overridden, for example to permit script execution.

So what we can take from this is that the VPN server is able to execute arbitrary code on any connecting client, which sounds like something that would be useful for initial access into an environment.

## Can’t we just use an ASA?

Research into the initial communications between the AnyConnect client and the VPN server was carried out using a legitimate Cisco ASA. In theory, it would be possible to spin up an ASA instance in a cloud provider and serve scripts to any user that connects to it, although this has some obvious drawbacks:

* A specific username and password need to be sent to the target in order for them to complete a connection
* The process would not be capable of capturing the user’s credentials.
* Served script names are automatically modified by the ASA

With this is mind, an old python web server script was dusted off and modified to respond to the series of requests that the AnyConnect client was expecting. Initial...