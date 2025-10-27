---
title: Resilient Secure Backup Connectivity for SMB/Home Users, (Thu, May 22nd)
url: https://isc.sans.edu/diary/rss/31972
source: SANS Internet Storm Center, InfoCON: green
date: 2025-05-23
fetch_date: 2025-10-06T22:30:57.120609
---

# Resilient Secure Backup Connectivity for SMB/Home Users, (Thu, May 22nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31968)
* [next](/diary/31976)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Resilient Secure Backup Connectivity for SMB/Home Users](/forums/diary/Resilient%2BSecure%2BBackup%2BConnectivity%2Bfor%2BSMBHome%2BUsers/31972/)

**Published**: 2025-05-22. **Last Updated**: 2025-05-22 17:27:38 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Resilient%2BSecure%2BBackup%2BConnectivity%2Bfor%2BSMBHome%2BUsers/31972/#comments)

If you are reading this, you are probably someone who will not easily go without internet connectivity for an extended amount of time. You may also have various home systems that you would like to be able to reach in case of an outage of your primary internet connection. A typical setup would include a primary connection via cable/fiber and a secondary connection via cellular or sattelite.

In this post, I will skip over setting up the failover part, but instead, I will focus on securing remote access and monitoring the backup connection.

### 1 - "Jump Host" (aka "Bastion Host")

If you need reliable and secure connectivity TO your network, a "jump host" is required. This is typically a minimal virtual machine with a cloud provider. Any affordable backup connectivity usually uses "carrier-grade NAT." Your IP address will not only be dynamic. You will only receive a non-routable IP address. Even IPv6 will sadly not help in many cases. Some cellular providers will NAT IPv6 (no idea why, but I suspect to prevent inbound connectivity so it can be sold as a "business feature").

A "jump host" will provide a static IPv4/v6 address that is globally reachable. It also provides a perimeter to manage better and monitor inbound connectivity.

Pick the cloud provider you choose (AWS, Digitalocean...) and set up a minimum virtual machine. You want to reduce your attack surface as much as possible. I only expose SSH "to the world" and run it on an odd port.

To enhance monitoring of the jump host, I am adding a "login.sh" script to the /etc/profile.d directory to alert me via SMS whenever anybody logs in to the host. You may want to put some guardrails around this; for example, do not alert if the connection originates from a "known good" IP address. But logins should not be too familiar. But remember that it is essential to guard these types of "backdoors" into your network well.

Follow standard hardening guidelines for SSH!

Here is the login.sh script I dropped in /etc/profile.d:

`#!/usr/bin/bach
[env variables removed]
details=$(who --ips | sed 's/ +/ /g')
/usr/bin/curl -sX POST -d "Body=Bastion Login: $details" \
     -d "From=$TWILIO_NUMBER" \
     -d "To=$TO_NUMBER" \
     "https://api.twilio.com/2010-04-01/Accounts/$TWILIO_ACCOUNT_SID/Messages" \
     -u "$TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN" > ~/twilio.log`
In this example,

I use SMS via Twilio for the alert to provide better reliability during an outage. However, you may use email or another simple messaging API like Telegram. Whatever works for you (and keeps working if your primary network connectivity is down)

### 2 -Internal Host![sketch of tunnel routed via isp 2 to a jump host](https://isc.sans.edu/diaryimages/images/Screenshot%202025-05-22%20at%201_21_44%E2%80%AFPM.png)

The internal host may be implemented using a stand-alone system like a Raspberry Pi or a virtual system. The gateway/router should be configured to route traffic from this system exclusively via the backup connection. This system covers two purposes: It does provide the outbound tunnel to our "Jump Host", and it monitors the backup connection. The backup connection will (hopefully) be used only sporadically. Without careful monitoring, the connection may go down and will be noticed during the failover.

To monitor the connection, I use the command line version of the "speedtest-cli" tool. This tool is based on speedtest.com. Once an hour, I perform a speed test and check the results. One nice advantage of the speedtest-cli tool is that it also reports your ISP. This way, you can monitor that traffic is routed via the correct connection. Hourly checks are sufficient in this case. Don't forget that the speed test will download some data that could be significant on a capped connection.

I noticed that T-Mobile does throttle ping traffic to hosts like 8.8.8.8. Be careful using simple pings like this for testing, as it may flood you with false positives. In particular, if you use the connectivity test for automatic failover, be careful how you use it to detect downtime. It is often better to use the ISP's advertised DNS server.

Here is the simple bash script I use to monitor the connection:

> `#!/bin/bash`
>
> `result=$(speedtest-cli --no-upload --json | tee -a speedtest.log)`
> `isp=$(echo $result | jq .client.isp | tr -d '"')
> speed=$(echo $result | jq .download | cut -f1 -d'.')
> latency=$(echo $result | jq .ping | cut -f1 -d'.')
> error=''`
>
> `if [ "$isp" != "Starlink" ]; then
>     error="wrong ISP"
> fi
> if [ "$speed" -lt 10000000 ]; then
>     error="$error low speed"
> fi
> if [ "$latency" -gt 100 ]; then
>     error="$error high latency"
> fi
> if [ "$error" != "" ]; then
>     mail jullrich@e... -s "Backup Connectivity Problem" <<EOF
> $error`
>
> `ISP $isp SPEED $speed LATENCY $latency
> EOF`
> `echo $error
>     echo "ISP $isp SPEED $speed LATENCY $latency"
> fi`

You may also implement a login alert on the internal endpoint, just like on the jump host. Remember that a connection from the jump host to the internal system will be invisible to most of your other network detection systems.

### 3 - Connectivity

Finally, you need to connect the internal host to the jump host. There are several different options. I use ssh, and the "autossh" script to automatically restart ssh if the connection should get disrupted. Various VPN solutions like OpenVPN, Wireguard or Tailscale will likely work well too. SSH has been working for me for about 30 years now, so not going to change :)

You will now have a "backdoor" into your network. As outlined above, make sure you secure that backdoor well. Many cloud providers will allow you to further limit access to the "jump host". These types of backup systems will also easily get forgotten. I like to use automatic updates as much as possible for these systems. Make sure logs from the "Jump Host" are forwarded to your main log aggregation solution.

Once everything is set up, there are two options:

1. You are at home during an outage: Your outbound traffic should be routed via your backup connection. All should be good, and the jump host doesn't get involved
2. You are away from home during an outage: Connect to your jump host, and from there via a forwarded port or VPN to your internal host. The internal host may not be used to do things like, for example, reboot equipment, or debug the underlying issue (or just retrieve a file you need).

The cost of it all is small. You may get away with a free cloud system. For extra credit: Automate starting up the jump host only while your main connection is down :) . A backup internet connection via 5G or Sattelite (Starlink) will run you around $50/month (more for an unmetered Starlink connection). In the "good old days", we had dialup modems as out-of-band backups. It is still handy to have a console server for remote access (but connect to it via the tunnel described above) or maybe a small IP-KVM, as they have not become available. I would advise against exposing any kind of KVM or console server directly to ...