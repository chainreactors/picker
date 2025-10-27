---
title: Passive detection of internet-connected systems affected by vulnerabilities from the CISA KEV catalog, (Wed, Jan 11th)
url: https://isc.sans.edu/diary/rss/29426
source: SANS Internet Storm Center, InfoCON: green
date: 2023-01-12
fetch_date: 2025-10-04T03:41:51.669028
---

# Passive detection of internet-connected systems affected by vulnerabilities from the CISA KEV catalog, (Wed, Jan 11th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29420)
* [next](/diary/29430)

# [Passive detection of internet-connected systems affected by vulnerabilities from the CISA KEV catalog](/forums/diary/Passive%2Bdetection%2Bof%2Binternetconnected%2Bsystems%2Baffected%2Bby%2Bvulnerabilities%2Bfrom%2Bthe%2BCISA%2BKEV%2Bcatalog/29426/)

**Published**: 2023-01-11. **Last Updated**: 2023-01-11 10:46:41 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[0 comment(s)](/diary/Passive%2Bdetection%2Bof%2Binternetconnected%2Bsystems%2Baffected%2Bby%2Bvulnerabilities%2Bfrom%2Bthe%2BCISA%2BKEV%2Bcatalog/29426/#comments)

CISA’s Know Exploited Vulnerabilities ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities)) catalog is a wonderful resource for vulnerability and patch management. If you have not come across it yet, it is – as the name suggests – a list of vulnerabilities that are currently known to be actively exploited in the wild, which is published by the US Cybersecurity & Infrastructure Agency ([CISA](https://www.cisa.gov/))[[1](https://www.cisa.gov/known-exploited-vulnerabilities)]. It was started back in 2021[[2](https://www.cisa.gov/binding-operational-directive-22-01)] and currently contains 870 vulnerabilities[[3](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)].

![](https://isc.sans.edu/diaryimages/images/23-01-11-triop-kev.png)

Although it was primarily intended for US federal institutions, which are required to remediate vulnerabilities listed in the catalog within certain timeframes, it quickly became an important part of vulnerability and patch management processes in many organizations around the world. Since the KEV catalog covers current, actively exploited vulnerabilities, it makes sense to prioritize them in both discovery of affected systems and their patching, especially when it comes to devices that are exposed to the internet.

For organizations with vulnerability management programs of (almost) any maturity in place, the identification of their own systems affected by vulnerabilities listed in the KEV catalog is quite straightforward, as any up-to-date vulnerability scanner/vulnerability management solution will probably be able to identify all of them. For organizations that lack any active vulnerability scanning capabilities, or for researchers or security teams who would like to monitor larger areas of the internet to see how many systems in them are affected by vulnerabilities included in the KEV catalog, it is not as straightforward.

This is where [Shodan](https://www.shodan.io/) and a new version of my [TriOp](https://untrustednetwork.net/en/triop/) tool come in.

I’ve covered TriOp in one of the ISC Diaries before[[4](https://isc.sans.edu/diary/TriOp%2Btool%2Bfor%2Bgathering%2Bnot%2Bjust%2Bsecurityrelated%2Bdata%2Bfrom%2BShodanio%2Btool%2Bdrop/27034)], so you may refer to the relevant article for further details, however it is basically a Python script for gathering information from Shodan.io about the number of IPs which satisfy one or more different queries. Therefore, if one was interested in the number of IPs with open port 25 in Germany that Shodan is aware of, one would simply have to run the script with the “search” parameter correctly set and it would return the correct number:

```

triop.py -s "port:25 country:DE"
```

And if one wanted to get the number of systems affected (by Shodan’s estimation) by BlueKeep (CVE-2019-0708) in the IP ranges 8.0.0.0/8 and 9.0.0.0/8, one would simply need to update the search parameter:

```

triop.py -s "vuln:CVE-2019-0708 net:8.0.0.0/8,vuln:CVE-2019-0708 net:9.0.0.0/8"
```

[![](https://isc.sans.edu/diaryimages/images/23-01-11-triop-search.png)](https://isc.sans.edu/diaryimages/images/23-01-11-triop-search.png)

As we can see, TriOp is capable of gathering (among other data) information about the number of IPs where Shodan detected systems affected by different vulnerabilities.

Getting back to the topic of vulnerability management, a good initial step for an organization without any vulnerability management system in place would probably be to monitor for vulnerable systems in their external perimeter, and if resources were insufficient to implement any active scanning capability, using data from Shodan for this initial step would certainly beat doing nothing. And since CISA publishes the KEV catalog, which lists what might be thought of as the most important current vulnerabilities, one could use this list as a reasonable starting point.

One could have theoretically used TriOp for this before, however to simplify the discovery of internet-exposed systems affected by one or more of the vulnerabilities listed in the KEV catalog (or, rather, to simplify the discovery of the number of such systems) in specific public IP ranges, countries, etc., I have added a new functionality which does this automatically to the latest version of TriOp, which has been published on [GitHub](https://github.com/NettleSec/TriOp) today.

It should be mentioned that Shodan currently seems capable of detecting only 44 of the 870 vulnerabilities in the KEV catalog, so TriOp will by default only look for systems affected by those. It should also be mentioned that since most checks that Shodan does to determine whether a specific system is vulnerable are based only on version checks and other passive methods, the identification of vulnerable systems will not be 100% accurate. Nevertheless, it can be an interesting source of information as well as a basis for a simple mechanism for discovery of unpatched systems.

In order to use the new functionality, which searches for relevant vulnerabilies from the CISA KEV catalog, one only needs to use the "--kev" parameter in addition to a search parameter:

[![](https://isc.sans.edu/diaryimages/images/23-01-11-triop-kev.png)](https://isc.sans.edu/diaryimages/images/23-01-11-triop-kev.png)

One further note I should make is that the list of KEV vulnerabilities that TriOp will use is downloaded from the internet any time the --kev option is used – I will periodically update it so it should always contain the relevant subset of KEV vulnerabilities, even when additions to the KEV catalog or changes to the capabilities of Shodan are made. Therefore, if one uses the "--kev" parameter for an ad-hoc lookup, such as the one shown in the image above, it should always provide the information regarding all vulnerabilities from the KEV catalog that Shodan can detect.

However, if one wanted to monitor the number of vulnerable systems over time and used TriOp to generate a CSV to which data would be added over time (one can do this using the parameters -O and -a respectively), the resulting file would – understandably – only contain Shodan queries generated for the list of vulnerabilities that was current when file was first created. In order to automate simple addition of queries for vulnerabilities newly added to the KEV catalogue to existing files, I’ve also updated the “add mode” of TriOp.

If one therefore had historically generated a CSV file containing the KEV catalog vulnerabilities using the following TriOp parameters

```

triop.py -s "country:US" --kev -O us-vuln.csv
```

it might look something like this:

[![](https://isc.sans.edu/diaryimages/images/23-01-11-vulns_old.png)](https://isc.sans.edu/diaryimages/images/23-01-11-vulns_old.png)

If one wanted to update it to also include queries for all relevant vulnerabilities that have been added to the KEV catalogue since the file was created, one could use the following TriOp parameters:

```

triop.py -m add -S us-vuln.csv --kev --filter country
```

The file containing the searches would afterwards contain newly added queries for all vulnerabilities in the KEV catalog which were not included before.
...