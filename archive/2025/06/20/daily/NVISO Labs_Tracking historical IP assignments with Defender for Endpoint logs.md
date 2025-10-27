---
title: Tracking historical IP assignments with Defender for Endpoint logs
url: https://blog.nviso.eu/2025/06/19/tracking-historical-ip-assignments-with-defender-for-endpoint-logs/
source: NVISO Labs
date: 2025-06-20
fetch_date: 2025-10-06T22:51:37.356602
---

# Tracking historical IP assignments with Defender for Endpoint logs

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

# Tracking historical IP assignments with Defender for Endpoint logs

[Ethan Bowen](https://blog.nviso.eu/author/ethan-bowen/ "Posts by Ethan Bowen")

[Forensics](https://blog.nviso.eu/category/forensics/), [Microsoft 365 Defender](https://blog.nviso.eu/category/microsoft-365-defender/), [Blue Team](https://blog.nviso.eu/category/blue-team/), [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/), [Detection Engineering](https://blog.nviso.eu/category/detection-engineering/), [Sentinel](https://blog.nviso.eu/category/cloud-security/sentinel/), [Kusto Query Language](https://blog.nviso.eu/category/kusto-kql/)

June 19, 2025June 18, 2025
10 Minutes

---

![](https://blog.nviso.eu/wp-content/uploads/2025/06/image-13-1024x535.png)

A new incident comes in. The CEO’s laptop shows possible Cobalt Strike activity. Your host investigation shows that the attacker likely gained privileged access to her host and the initial activity is from two days ago. You contain the host in your EDR agent. But now you must determine if the attacker moved laterally inside your network.

It would be easiest to search her host name in the SIEM, but there are many types of logs that don’t include a host name (certain Active Directory events, unauthenticated proxy logs, firewall logs, web application logs, etc). The next best option is to determine every IP address this device had in the last two days and when those IP addresses were assigned to the device.

Unfortunately, the CEO is very busy and moves around constantly. She was initially in her office (connected via ethernet cable), and then moved to multiple conference rooms (Wi-Fi), and is currently on a business trip (multiple VPN sessions). It is important that we know when her device started and stopped specific IPs, because the IPs are likely in a dynamic assignment pool, which means they are automatically reassigned to new devices. For example: If she was only assigned a Wi-Fi IP address for 20 minutes, then those 20 minutes are the only times we care about that IP address.

This is a common investigation requirement, so let’s see if we can automate it.

## Visualizing the desired output

Let’s first visualize the outcome we want.

We know the CEO moved around a lot during this time period. It would be great if we had a table showing us a list of IP addresses that the device had throughout the investigation timeframe.

Something like:

![](https://blog.nviso.eu/wp-content/uploads/2025/05/image-15.png)

Before we spend time trying to do this ourselves, let’s investigate if Defender XDR and Microsoft Defender for Endpoint (MDE) already provide this information.

## Data in the Defender XDR Portal

MDE provides information about the assigned IP addresses of a device in a few different places. One place is the Defender XDR portal, under the device’s object page.

On the device’s object page, click on **See IP addresses info** on the left panel (scroll down):

![](https://blog.nviso.eu/wp-content/uploads/2025/05/image-16.png)

Figure 1: Device Object’s IP address information

![](https://blog.nviso.eu/wp-content/uploads/2025/05/image-28.png)

Figure 2: Expanded IP address information in Defender XDR

There is a lot of great info here. However, it is only the **last seen information.** In order to build a table showing assignments over time, we need historical information from the time the activity started to containment.

## DeviceNetworkEvents

This table is part of Defender XDR’s [Advanced Hunting](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview) capability, which allows analysts to query logs from different Defender products. This feature retains logs for 30 days. This table is populated by devices onboarded to MDE and contains network events from the hosts.

For example:

* outbound connections,
* inbound connections,
* listening sockets,
* some application-level protocol information.

We **could** try to create a distinct list of source IPs (for outbound connections) and destination IPs (for inbound connections) and generate our table from that. However, MDE does not log every single **event** that occurs on a host[[1]](#_ftn1), so we could get false negatives. We’ll keep this as a backup.

## AssignedIPAddresses()

In Advanced Hunting, there is a built-in function called **AssignedIPAddresses**. This function returns “the latest IP addresses that have been assigned to the device or the most recent IP addresses from a specified point in time”. The output looks like:

![](https://blog.nviso.eu/wp-content/uploads/2025/05/image-29-1024x79.png)

Figure 3: Output of AssignedIPAddresses() function

This does not meet our requirement, because it only provides the IP addresses at a specific point in time. We need results from **multiple** days.

It would be easier if we just had a list of IP addresses assigned to the device…

## DeviceNetworkInfo

This is where the **DeviceNetworkInfo** table is helpful. This table contains information about network adapters, MAC addresses, connected networks, DNS servers, and most importantly, assigned IP Addresses.

Additionally, this is not an event-based table. That means devices report the data with some frequency (if the device is online of course). Therefore, we can use the table to create logs similar to DHCP, which show when a device **started** using an IP and when it **stopped** using an IP address.

![](https://blog.nviso.eu/wp-content/uploads/2025/05/image-17.png)

Figure 4: Sample rows from DeviceNetworkInfo table

First, we need to understand the data in the table. The **IPAddresses** column contains any IP addresses assigned to the adapter. Since adapters can have multiple IPs (IPv4 + IPv6), it is an array. Below, the device reports two IPs. (The IPv6 address is a link-local address, which we will exclude in our final queries.)

![](https://blog.nviso.eu/wp-content/uploads/2025/05/image-31-1024x62.png)

Figure 5: The IPAddresses column showing two assigned IP addresses for the adapter

The first step is to get every IP address the device reported during our time of investigation. We need each IP on a separate row, in order to do analysis.

We can use the amazing [**mv-expand**](https://learn.microsoft.com/en-us/kusto/query/mv-expand-operator?view=microsoft-sentinel) operator to do this. **mv-expand** takes an array column from a row and creates new rows for ea...