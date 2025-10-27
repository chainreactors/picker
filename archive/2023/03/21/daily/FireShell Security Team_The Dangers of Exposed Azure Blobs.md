---
title: The Dangers of Exposed Azure Blobs
url: https://fireshellsecurity.team/dangers-of-exposed-blobs/
source: FireShell Security Team
date: 2023-03-21
fetch_date: 2025-10-04T10:09:00.525891
---

# The Dangers of Exposed Azure Blobs

[![](/assets/images/title.gif)](/)

* [Home](/)
* [Team](/team/)
* [Articles](/articles/)
* [Portfolio](/portfolio/)
* [Sponsors](/sponsors/)
* [About](/about/)
* Toggle theme
  + Light
  + Dark
  + Auto

Monday, March 20, 2023

# The Dangers of Exposed Azure Blobs

by [Marzano "Macmod"](/macmod/)

The Dangers of Exposed Azure Blobs

![wordcloud-banner.png](https://i.imgur.com/DxjIyD5.png)

# Introduction

Being one of the most widely used storage services on the web - probably only falling behind to AWS’s storage services - Azure storage accounts provide a simple and effective way of storing many kinds of data in the cloud. It allows you to store your data in **blob containers**, **file shares**, **tables** or **queues** without having to worry about scalability, durability and availability. In less than 5 minutes you can set up an storage account under your subscription and upload your data into the cloud. After that you can use all sorts of cloud services on top of your data, develop data analysis pipelines, automated notifications, or just host static websites.

The simplest type of storage service you can use is object storage: services that allow you to store any kind of file in them and access the file by its name, usually providing an URL for your file under the cloud’s domain. One of such services is Azure blob storage, a service from Azure storage accounts. Azure blob storage works similarly to S3 buckets - you create a **storage account**, then in that account you create a **Container** for your files, choose the appropriate **Public access level** for your container and upload your files into it.

Azure enables public access to blobs by default when you create a storage account:

![BlobPublicAccess](https://i.imgur.com/msrny7d.png)

Then, when you decide to use Azure blob storage, this is the page you will be looking at:

![AzureBlobStorage](https://i.imgur.com/NRM3jbP.png)

When you’re creating the container for your objects, you choose one of these **Public access levels**:

* **Private** - No anonymous access. *If someone tries to access your data via the public endpoint, they will simply get a 404 back*.
* **Blob** - Anonymous read access to blobs directly. *The paths of your blobs can still be guessed if they are simple enough, but they can’t be listed directly by accessing the container endpoint*.
* **Container** - Anonymous read access to blobs and containers. *This allows anyone to list which blobs are in a container and access them, given that they know your storage account and container name*.

Azure pre-selects **Private** for you and then warns against using **Container** as the access level for your container - but many ignore it:

![ContainerAccessLevel](https://i.imgur.com/jiDXLSs.png)

# The Problem & The Plan

The issue with the **Container** public access level is that, although an attacker will not be able enumerate the containers in the root of the storage account, it’s a bit obvious that most organizations will tend to use a small set of common names for their containers, like **images**, **videos** or **logs**. An attacker can easily just try a small wordlist like this on the public endpoint of the blob storage service, since there doesn’t seem to be any sort of rate limiting in Azure that prevents this sort of behavior.

I decided to take a look at this issue to understand how big the problem is, so I developed a fast scanning tool, [goblob](https://github.com/Macmod/goblob), to enumerate exposed blob containers in Azure storage accounts. A friend pointed out to me that **SpongeBlob** would be much funnier, but then it was too late and I had already chosen a name 🫤.

The idea is that, if you get an **HTTP 200** accessing the container endpoint:

```
https://<storageaccount>.blob.core.windows.net/<containername>?restype=container
```

Then it means that the specified container exists under that storage account and that it’s publicly exposed with an access level of Container. Then you can append `&comp=list` to the URL to get a pretty XML listing all blobs under that container.

To perform this analysis I’d need more than just that, though - I needed a sample of **existing storage account names**, and then **a wordlist of possible container names** under these storage accounts.

For the issue of finding storage account names, I decided to find subdomains of Azure storage services, since they always include the name of the storage account. I used a combined approach - first I used my [NameScraper](https://github.com/Macmod/NameScraper) tool to scrape SecurityTrails’ public data for subdomains of `blob.core.windows.net`, `table.core.windows.net`, `queue.core.windows.net` and `file.core.windows.net`. Then I used `amass` to gather more subdomains of these domains from miscellaneous OSINT sources. For the wordlist, I adapted an existing open-source wordlist of bucket names into a 2087-word wordlist of possible container names.

The full plan was as follows:

![The plan](https://i.imgur.com/lIjoYXS.png)

# Results

This approach yielded a list of **39.731** possible storage account names to check against **2.087** container names - a search space of almost **83 million** container URLs. I checked them with goblob to find the URLs of the first 20 pages of blobs in each container:

```
$ ./goblob -accounts=storage-accounts.txt -containers=wordlists/goblob-folder-names.txt -maxpages=20 -output=blobs.txt -blobs=true
```

Obviously this took some hours to run, but by the time it finished I had a list of URLs for **19.630.450 exposed blobs**. These blobs amounted for a total of **55 TB** of data. The public containers were found across **1.272** storage accounts (3.2% of my sample) using a total of **516** distinct container names (~1/4 of my wordlist). Here is a wordcloud of the exposed container names found:

![Wordcloud of exposed container names](https://i.imgur.com/AP1R38Q.png)

An even harder problem is to figure out which of these URLs contain sensitive information, as most people won’t have 55 TB of storage hanging around to download and analyze the full data. I didn’t download this data for obvious reasons, but I did analyze their URLs and file extensions briefly. Here are the main highlights that I found interesting (and worrisome!):

* **13.232.720 (67.4%) blobs contained common extensions for pictures, videos and audio files.**
* **1.921.353 (9.7%) blobs contained documents (.docx, .doc, .pdf, .rtf), presentations (.pptx, .ppt), spreadsheets (.xlsx, .xls) or CSV files (.csv);**
* 1.039.401 (5.2%) blobs contained JSON, YAML or XML files.
* **321.666 (1.6%) blobs mentioned “invoice” or “contract” in their URLs;**
* **181.859 (0.92%) blobs contained text files (.txt);**
* **165.771 (0.84%) blobs mentioned “backup” in their URLs;**
* 116.731 (0.59%) blobs contained executable files, mobile apps or libraries (.exe, .jar, .apk, .com, .wsf, .bin, .bat, .dll, .o);
* **64.486 (0.32%) blobs contained back-end source code (.java, .cpp, .c, .h, .py, .php, .asp, .aspx, .rb, .cs, .go, .swift, .scala, .vb);**
* **58.678 (0.29%) blobs contained compressed files (.zip, .tar.gz, .tar.bz2, .tar, .gz, .bz2, .xz, .7z, .rar);**
* **38.675 (0.19%) blobs contained log files (.log);**
* 3.484 (0.017%) blobs contained .config files, of which 1.396 (40%) were named web.config;
* 3 containers contained git repos;

# Mitigations

The simplest mitigation for this sort of issue is to have an up-to-date inventory of your storage account containers and make sure all containers containing sensitive information have an access level of **Private**. In some cases it might be okay to use an access level of **Blob** on your container, such as when the only files you intend to store there have a sufficiently random identifier in the name, like a GUID, but the **Container** access level should be avoided whenever possible.

If you have a scenario where you can’t use the Private access level because you have an external partner that needs access to your dat...