---
title: Azure Batch Misused for Crypto Mining
url: https://dfir.ch/posts/azure_batch/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-31
fetch_date: 2025-10-06T18:08:02.178383
---

# Azure Batch Misused for Crypto Mining

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

# Azure Batch Misused for Crypto Mining

15 Mar 2024

**Table of Contents**

* [Introduction](#introduction)
* [Background](#background)
* [Attacker’s action](#attackers-action)
* [Conclusion](#conclusion)
* [Appendix A - ba.sh](#appendix-a---bash)
* [Appendix B - 00ca23e288f0686e5721b097f9617e2a05ad84508e84f0c27dee2c97261ae0a1.json](#appendix-b---00ca23e288f0686e5721b097f9617e2a05ad84508e84f0c27dee2c97261ae0a1json)

## Introduction

*A huge thanks to the [Invictus-IR](https://www.invictus-ir.com/) team for proofreading this blog post* 🙏

Recently, I posted a [tweet](https://twitter.com/malmoeb/status/1764585545596797143) regarding an unpatched TeamCity server that an attacker exploited to deploy a CoinMiner. In response to my tweet, the X (former Twitter) user, *the cybersecurity doge*, shared another story they investigated:

*An attacker obtained access to an administrator Azure environment user. Once logged on the tenant he created a resource group, and built 3 different batch accounts insides. Meanwhile, he opened a ticket to MS support asking for the increase of batch’s limit. Why? The limit increase was needed in order to boost on mining capacity. In fact, once the batch accounts were created, he built on these a complete autonomous crypto-mining system. The attacker used the miner reported above to mine crypto currency.* [[1]](https://twitter.com/red_cth/status/1754970064560763199)

In this blog post, we explore the Azure Batch capabilities before diving into the logs from the incident described above (the logs were provided to us by the X (former Twitter) user “the cybersecurity doge” - unfortunately, we didnât have access to the affected Tenant at any time).

## Background

**What is Azure Batch?**

*Azure Batch is a platform service for running large-scale parallel and HPC applications efficiently in the cloud. Azure Batch schedules compute-intensive work to run on a managed pool of virtual machines, and can automatically scale compute resources to meet the needs of your jobs.* [[2]](https://learn.microsoft.com/en-us/azure/architecture/topics/high-performance-computing)

We will provide a brief walkthrough on how to create a new Azure Batch service. This will help comprehend the steps the attackers took, as outlined in the next section. Please refer to the [official documentation](https://learn.microsoft.com/en-us/azure/batch/) for a more comprehensive discussion on Azure Batch.

**Step 1 - New batch account**

First and foremost, we create a new Batch account. We create a new Resource group (named *dfir.ch*), within which our Batch account will be part of. The Batch account name will be *dfir*.

![New batch account](/images/azure_batch/new_batch_account.png "New batch account")

Figure 1: New Batch account

**Step 2 - Deployment is complete**

The deployment is complete, and we can go to our created resource (click on *Go to resource*).

![Newly created Batch account](/images/azure_batch/deployment_batch.png "Newly created Batch account")

Figure 2: Newly created Batch account

**Step 3 - Resource group - Activity log**

When inspecting the Activity log of the newly created Resource group, we find the following operations:

| localizedValue | operationName:value |
| --- | --- |
| Update resource group | Microsoft.Resources/subscriptions/resourceGroups/write |
| Validate deployment | Microsoft.Resources/deployments/validate/action |
| Create or Update Batch Account | Microsoft.Batch/batchAccounts/write |
| Create Deployment | Microsoft.Resources/deployments/write |

![Resource group Activity log](/images/azure_batch/ressource_group_activity.png "Resource group Activity log")

Figure 3: Resource group Activity log

**Step 4 - Batch account - Activity log**

Here is the operation from the Activity log from the Batch account:

| localizedValue | operationName:value |
| --- | --- |
| Create or Update Batch Account | Microsoft.Batch/batchAccounts/write |

![Batch account Activity log](/images/azure_batch/batch_account_activity.png "Batch account Activity log")

Figure 4: Batch account Activity log

**Step 5 - Add pool**

Next, we create a new pool. In Azure Batch, a pool refers to a collection of compute resources (virtual machines) used to execute batch processing tasks. When you create a pool in Azure Batch, you specify the configuration details, such as the size and type of virtual machines, the operating system, and other settings. In the example, we spin up a new Ubuntu Server. The pool will be named *dfir*.

| localizedValue | operationName:value |
| --- | --- |
| Create or Update Pool | Microsoft.Batch/batchAccounts/pools/write |

![Add pool](/images/azure_batch/add_pool.png "Add pool")

Figure 5: Add pool

**Step 6 - Start Task**

Within the parameters required to initiate the pool, we have the option to define a Start Task. Please bear this in mind for the discussion later when we delve into the steps executed by the attacker.

In Azure Batch, StartTask is a concept related to configuring tasks within a job. When you define a job in Azure Batch, you can specify a StartTask that runs before any other tasks in the job. The StartTask is typically used for setup or initialization tasks that need to be performed before the main batch processing tasks begin.

![Start Task](/images/azure_batch/start_task.png "Start Task")

Figure 6: Start Task

**Step 7 - Adjust Quota**

*For capacity management purposes, the default quotas for new Batch accounts in some regions and for some subscription types have been reduced from the above range of values. In some cases, these limits have been reduced to zero. When you create a new Batch account, check your quotas and request an appropriate core or service quota increase, if necessary.*

This is exactly the case in our Tenant. To run the App pool, we must adjust our Quota. *To request an increase beyond this limit, contact Azure Support.* [[3]](https://learn.microsoft.com/en-us/azure/batch/batch-quota-limit) Keep that in mind, too, for the next section.

![PoolQuotaReached](/images/azure_batch/quota_reached.png "PoolQuotaReached")

Figure 7: PoolQuotaReached

**Step 8 - Profit 💰 (as an attacker)**

These steps, particularly the Start Task, are crucial for comprehending the attack flow, which we will discuss in the next section of this blog post. If the Quota is adjusted, our newly created Pool will spin up and execute the Start Task as configured.

## Attacker’s action

In this section, we outline the attackers’ traces, as good as it gets, because we didn’t have access to the Tenant, but were provided with the logs of the incident (see the introduction section).

**Creation of the Batch-Account**

A new Batch Account named *websecv1* is created inside the resource group *Bch*.

```
[
  {
      "provisioningOperation": "Create",
      "provisioningState": "Succeeded",
      ...
      "statusCode": "OK",
      "targetResource": {
        "id": "/subscriptions/[REDACTED]/resourceGroups/Bch/
                providers/Microsoft.Batch/batchAccounts/websecv1",
        "resourceType": "Microsoft.Batch/batchAccounts",
        "resourceName": "websecv1"
      }
    }
  }
```

**Support needed** 💜

The compromised Tenant analyzed by “the cybersecurity doge” had initially set the Quota to 0, preventing the attacker from spinning up new App pools. Consequently, the attacker contacted the Microsoft support and requested an adjustment to the Quota.

![Microsoft Support](/images/azure_batch/support_answer.jpg "Microsoft Support")

Figure 8: Microsoft Support

Here is an overview of the support requests that the attacker opened:

![All support requests](/images/azure_batch/support_request.jpg "All support requests")

Figure 9: All support requests

**Creation of the pool**

The Batch-Account *websecv1* started a new Pool named *WebApp*, a Linux Ubuntu server.

```
{
    "id": "WebApp",
    "displ...