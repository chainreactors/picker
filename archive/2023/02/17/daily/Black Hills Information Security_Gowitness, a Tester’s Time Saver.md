---
title: Gowitness, a Tester’s Time Saver
url: https://www.blackhillsinfosec.com/gowitness-a-testers-time-saver/
source: Black Hills Information Security
date: 2023-02-17
fetch_date: 2025-10-04T06:52:43.450821
---

# Gowitness, a Tester’s Time Saver

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

16
Feb
2023

[Alyssa Snow](https://www.blackhillsinfosec.com/category/author/alyssa-snow/), [External/Internal](https://www.blackhillsinfosec.com/category/red-team/external/), [General InfoSec Tips & Tricks](https://www.blackhillsinfosec.com/category/infosec-101/general-infosec-tips-tricks/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Recon](https://www.blackhillsinfosec.com/category/red-team/recon/), [Web App](https://www.blackhillsinfosec.com/category/red-team/web-app/)

# [Gowitness, a Tester’s Time Saver](https://www.blackhillsinfosec.com/gowitness-a-testers-time-saver/)

[Alyssa Snow](https://www.linkedin.com/in/alyssa-snow-2b8437169) //

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/02/BLOG_chalkboard_00616-1024x576.png)

During an external or internal network penetration test, it can be challenging to comb through each web server in scope to find the juicy stuff. During a timeboxed assessment, a tool like Gowitness (<https://github.com/sensepost/gowitness/wiki>) can help prioritize the web applications available on your target network.

Gowitness is an automated website screenshot tool, inspired by Eyewitness (<https://github.com/FortyNorthSecurity/EyeWitness>), written in Golang. Gowitness navigates to each web application and uses a headless browser to generate screenshots of the web application. It fingerprints these applications by capturing the HTML response and HTTPheaders. Additionally, Gowitness attempts to identify technologies used by the application. Next, it generates a report that allows the tester to browse through the available web services easily.

## Installation

Gowitness installation can be as simple as downloading one of the prebuilt binaries found here: <https://github.com/sensepost/gowitness/releases>.

You can install the tool with go as follows:

```
go install github.com/sensepost/gowitness@latest
```

You can run the tool using a docker container:

```
docker pull leonjza/gowitness
```

You can also clone the repository and compile the tool from the source code:

```
git clone https://github.com/sensepost/gowitness.git
cd gowitness
make linux
```

*Make sure you have Chrome and Golang installed on your machine before attempting to use the tool.*

## Gowitness Scanning

There are many other automated screenshot tools, and I encourage you to investigate whichever interests you most. We also have another blog post about Eyewitness (<https://www.blackhillsinfosec.com/eyewitness-and-why-it-rocks/>). One cool feature Eyewitness has that I hope to see Gowitness implement at some point is default credential identification. Eyewitness will supply the user with default credentials (if it knows them) alongside the application HTTP header information. I use Gowitness because I am a fan of Golang, and I like the tool’s UI.

I typically use Gowitness to process Nessus and Nmap scan results. Gowitness accepts targets in several formats. You can provide the tool with a single target URL, a list of URLs, IPs, or CIDRs.

Process Nessus scan command:

```
gowitness nessus -f basic-scan.nessus
```

GoWitness can process Nmap results in XML format. To output Nmap results in XML format you can run Nmap using the -o flag with argument X. An example of this is shown below.

```
nmap <TARGET> -oX nmap-results.xml
```

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/02/Picture15-2-1024x191.png)

**Partial Nmap XML Results**

Process Nmap scan command:

```
gowitness nmap -f nmap-results.xml
```

Gowitness has various flag options that can be used to fine-tune your scan. For example, the `--user-agent flag`. The default user agent string is “`Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36`“. Let’s say you wanted to experiment with different results using a mobile user-agent string; you may set this flag value to something like `--user-agent “Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1`”.

I have listed a couple of other useful flags below:

* `--timeout` – timeout string. The default is 10 seconds.
* `-t/--threads` – threads used to run Gowitness. The default is 4 threads.

If you are on a reliable network but you have many invalid domains, you might consider reducing the timeout to 4 to reduce the scanning time.

I recommend setting the thread count to somewhere between 1 and 2 times the number of cores on your system. So, if your system has 4 cores, you could set the threads to 8. You can keep an eye on your CPU usage and tune up or down if you hit bottl...