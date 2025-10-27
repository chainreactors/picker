---
title: Mastering Amass: The Ultimate Recon Toolkit
url: https://infosecwriteups.com/mastering-amass-the-ultimate-recon-toolkit-d66a56627849?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-02-12
fetch_date: 2025-10-06T20:34:37.705938
---

# Mastering Amass: The Ultimate Recon Toolkit

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd66a56627849&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmastering-amass-the-ultimate-recon-toolkit-d66a56627849&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmastering-amass-the-ultimate-recon-toolkit-d66a56627849&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d66a56627849---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d66a56627849---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Mastering Amass: The Ultimate Recon Toolkit

## From Basics to Pro: Amass Explained

[![Muhammad Abdullah Niazi](https://miro.medium.com/v2/resize:fill:64:64/1*BdjGIN56aSSFYW-NTDWhHA.jpeg)](https://medium.com/%40NiaziSec?source=post_page---byline--d66a56627849---------------------------------------)

[Muhammad Abdullah Niazi](https://medium.com/%40NiaziSec?source=post_page---byline--d66a56627849---------------------------------------)

4 min read

·

Jan 26, 2025

--

Listen

Share

In this blog, I’ll explain Amass, its key features, subcommands, how to configure APIs, and some useful commands for reconnaissance and security scanning. If you have any questions or want to add something, feel free to comment below!

Amass is an open-source reconnaissance tool by OWASP, designed for network mapping and external asset discovery. It performs DNS enumeration and deep scanning to identify subdomains, IPs, and network-related assets, leveraging multiple data sources simultaneously.

Press enter or click to view image in full size

![]()

<https://github.com/owasp-amass/amass>

### **Key Features and Capabilities:**

* **DNS Enumeration**: Brute force subdomain discovery, recursive lookups, zone transfers, certificate transparency logs, wildcard detection, and name alterations.
* **Data Sources Integration**: Collects data from DNS databases, search engines, SSL/TLS logs, APIs, web archives, and WHOIS records.
* **Advanced Features**: Graph database support, visualization tools, custom scripting, active/passive gathering, and multi-format output (JSON, CSV, GraphML).

The primary subcommands of Amass are:

1. `amass intel`: Collects open-source intelligence to discover targets for enumeration.
2. `amass enum`: Performs DNS enumeration and network mapping.
3. `amass db`: Manages the graph databases storing the enumeration results.
4. `amass viz`: Generates graphical representations of enumeration results.
5. `amass track`: Monitor Attack Surface Changes.
6. `amass dns`: Resole domain names quickly and efficiently

## API Configuration

To enhance Amass’s capabilities with additional data sources, you can configure APIs for services like Shodan, Censys, VirusTotal, etc.

1. **Configuration File**: The default configuration file for Amass is located at `~/.config/amass/config.ini`.
2. **Edit the Configuration File**: Open the `config.ini` file in a text editor:

```
nano ~/.config/amass/config.ini
```

**3. Add Your API Keys**: Paste your API keys under the respective sections.

```
[Censys] api = <your_censys_api_key>
[Shodan] api = <your_shodan_api_key>
[VirusTotal] api = <your_virustotal_api_key>
```

Save the changes and exit the editor. Amass will now use these APIs during enumeration.

## Useful Commands

### 1. Subdomain Enumeration

* `amass enum -d <target_domain>` Performs active and passive subdomain enumeration.
* `amass enum -d <target_domain> -passive`Passive subdomain enumeration only (doesn't interact directly with the target).
* `amass enum -d <target_domain> -active` Active enumeration using DNS, web scraping, and other techniques.
* `amass enum -d <target_domain> -ip` Enumerates subdomains and resolves them to their associated IPs.
* `amass enum -d <target_domain> -src` Displays the sources of discovered subdomains.

### 2. Domain Asset Discovery

* `amass intel -org <organization_name>` Discovers domains owned by the specified organization.
* `amass intel -d <target_domain>` Identifies additional domains.
* `amass intel -whois -d <target_domain>` Uses WHOIS data to find domains sharing the same WHOIS details.
* `amass intel -asn <ASN_number>` Finds domains within a specific Autonomous System Number.

### 3. Network Mapping

**Purpose:** Map out the target’s network infrastructure.

* `amass track -d <target_domain>` Tracks changes
* `amass viz -d <target_domain> -o amass_graph.dot` Creates a graph representation of the network structure.
* `amass netblocks -asn <ASN_number>` Lists IP ranges owned by the ASN.

### 4. Vulnerability Scanning Integration

* `amass enum -d <target_domain> | nikto -h -`Runs Nikto scan on all discovered subdomains for vulnerabilities.
* `amass enum -d <target_domain> -ip | awk '{print $NF}' | nmap -iL -`
  Uses Nmap to scan IPs resolved from subdomains.

### 5. Reverse WHOIS

* `amass db -whois -d <target_domain>` Searches the Amass database for WHOIS connections to the target.

### 6. Historical Data Analysis

* `amass db -history -d <target_domain>` Shows the historical data of subdomains and IPs.
* `amass db -names` Lists all discovered names for past enumerations.

### 7. Brute Forcing

* `amass enum -d <target_domain> -brute` Brute forces subdomains using the default wordlist.
* `amass enum -d <target_domain> -brute -w <wordlist.txt>` Performs brute force subdomain discovery with a custom wordlist.

### 8. ASN and IP Analysis

* `amass netblocks -asn <ASN_number>` Displays netblocks associated with a given ASN.
* `amass intel -cidr <CIDR>` Identifies domains within the specified CIDR range.

### 9. Output Management

* `amass enum -d <target_domain> -o <output_file.txt>` Outputs results to a text file.
* `amass enum -d <target_domain> -json <output_file.json>` Saves results in JSON format for easier automation.
* `amass enum -d <target_domain> -csv <output_file.csv>` Exports findings into a CSV file.

### 10. Active Reconnaissance

* `amass enum -d <target_domain> -active -p 80,443` Scans subdomains for active services on ports 80 and 443.
* `amass enum -d <target_domain> -active -o <output_file.txt>` Saves active recon results in a file.

### 11. Third-Party API Integration

* `amass enum -d <target_domain> -config <config.ini>` Uses the specified configuration file for API keys and settings.
* `amass enum -d <target_domain> -active -max-dns-queries 200` Limits DNS queries to stay within API or rate limits.

### 12. Real-Time Updates

* `amass track -d <target_domain>` Tracks changes to subdomains over time.
* `amass enum -...