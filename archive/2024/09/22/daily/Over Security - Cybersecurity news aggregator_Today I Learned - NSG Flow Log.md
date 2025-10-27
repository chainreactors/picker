---
title: Today I Learned - NSG Flow Log
url: https://dfir.ch/posts/today_i_learned_nsg_flow_log/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-22
fetch_date: 2025-10-06T18:26:14.509038
---

# Today I Learned - NSG Flow Log

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# Today I Learned - NSG Flow Log

21 Sep 2024

**Table of Contents**

* [Introduction](#introduction)
* [Storage Account](#storage-account)
* [Flow log](#flow-log)
* [Analysis](#analysis)
* [Next Steps](#next-steps)
* [Conclusion](#conclusion)

## Introduction

Azure flow logs are a feature in Azure that allows you to capture and analyze network traffic to and from virtual network interfaces (NICs) in Azure. Specifically, flow logs provide granular data about IP traffic flowing through a Network Security Group (NSG). Azure automatically creates a network security group (NSG) when you create a virtual machine: `$vmname-nsg`.

This data includes information on the source and destination IP addresses, ports, and protocols, as well as traffic allowed or denied by NSG rules. Flow logs are useful for security analysis, network monitoring, and troubleshooting in Azure environments. They can be stored in Azure Storage, analyzed with Azure Monitor, or visualized with an SIEM.

**Flow logs are the source of truth for all network activity in your cloud environment.**

Read the official Microsoft documentation [Flow logging for network security groups](https://learn.microsoft.com/en-us/azure/network-watcher/nsg-flow-logs-overview) for an in-depth discussion of this topic.

Here is a quote from the documentation: ***Flow logs should be enabled on all critical subnets in your subscription as an auditing and security best practice.*** So read this short blog post, read the complete documentation from Microsoft (because this post does not explain everything in the necessary depth), and start enabling flow logs in your Tenant today :)

## Storage Account

First, we must create a storage account to store the flow logs. In this case, the storage account is named `dfirflowlog`.

![Create a storage account](/images/nsg_flowlog/storage_account.png "Create a storage account")

Figure 1: Create a storage account

## Flow log

Next, we create a new flow log. After clicking on the + sign, `Select target resource`, we choose the `dfir-nsg` network security group for logging.

![Create a flow log](/images/nsg_flowlog/flow_log.png "Create a flow log")

Figure 2: Create a flow log

## Analysis

Flow logs are essential for accurately tracking all network activity in your cloud environment and are indispensable for any thorough investigation. Let’s have a look at these flow logs:

![Overview of available logs](/images/nsg_flowlog/storage_overview.png "Overview of available logs")

Figure 3: Overview of available logs

Inside the created storage account that holds our flow logs, we see that a directory structure was created. Azure creates a new log file on a one-minute interval, resulting in this nested directory structure. Looking at a sample entry from last month:

```
      "time": "2024-08-12T16:58:37.1801159Z",
      "systemId": "02277b3f-0f45-4d71-a816-f16ee2a7e63c",
      "macAddress": "6045BD2C0D3A",
      "category": "NetworkSecurityGroupFlowEvent",
      "resourceId": "/SUBSCRIPTIONS/8DD45A8F-4308-4206-817E-55A1325EC4E7/RESOURCEGROUPS/DFIR_GROUP/PROVIDERS/MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/DFIR-NSG",
      "operationName": "NetworkSecurityGroupFlowEvents",
      "properties": {
        "Version": 2,
        "flows": [
          {
            "rule": "DefaultRule_AllowInternetOutBound",
            "flows": [
              {
                "mac": "6045BD2C0D3A",
                "flowTuples": [
                  "1723481866,10.0.0.4,51.104.136.2,61563,443,T,O,A,E,0,0,0,0",
                  "1723481890,10.0.0.4,2.22.154.9,61627,443,T,O,A,B,,,,",
                  [...]
                ]
              }
            ]
          },
          {
            "rule": "DefaultRule_DenyAllInBound",
            "flows": [
              {
                "mac": "6045BD2C0D3A",
                "flowTuples": [
                  "1723481855,194.180.49.75,10.0.0.4,55364,14647,T,I,D,B,,,,",
                  "1723481855,194.180.49.75,10.0.0.4,55364,10435,T,I,D,B,,,,",
                  [...]
                ]
              }
            ]
          },
          {
            "rule": "UserRule_RDP",
            "flows": [
              {
                "mac": "6045BD2C0D3A",
                "flowTuples": [
                  "1723481878,46.42.240.226,10.0.0.4,28482,3389,T,I,A,B,,,,",
                  "1723481880,103.147.14.137,10.0.0.4,65195,3389,T,I,A,B,,,,",
                  "1723481904,147.50.240.111,10.0.0.4,60548,3389,T,I,A,B,,,,"
                ]
              }
            ]
          }
```

We see three rules:

* `DefaultRule_AllowInternetOutBound`
* `DefaultRule_DenyAllInBound`
* `UserRule_RDP`

The `flowTuples` array holds multiple properties for the flow tuple in a comma-separated format:

* `Timestamp`: The time stamp of when the flow occurred in UNIX epoch format.
* `Source IP`: Source IP address.
* `Destination IP`: Destination IP address.
* `Source port`: Source port.
* `Destination port`: Destination port.
* `Protocol`: Protocol of the flow. Valid values are T for TCP and U for UDP.
* `Traffic flow`: Direction of the traffic flow. Valid values are I for inbound and O for outbound.
* `Traffic decision`: Whether traffic was allowed or denied. Valid values are A for allowed and D for denied.

**Flow State (Version 2 Only)**

* `B`: Begin when a flow is created. Statistics aren’t provided.
* `C`: Continuing for an ongoing flow. Statistics are provided at 5-minute intervals.
* `E`: End, when a flow is terminated. Statistics are provided

## Next Steps

Integrating flow logs with Azure Monitor, Sentinel, or external SIEMs such as Splunk or the ELK Stack allows for detailed traffic analysis and real-time monitoring. This is critical for detecting unusual traffic, troubleshooting issues, and enhancing incident response by identifying potential threats, such as unauthorized access or lateral movement.

## Conclusion

Azure NSG Flow Logs are invaluable for securing cloud environments. They provide deep insights into network activity, helping to detect and respond to suspicious behavior, improve troubleshooting, and ensure robust security postures.

Â© 2025 .
Powered by [Hugo blog awesome](https://github.com/hugo-sid/hugo-blog-awesome).