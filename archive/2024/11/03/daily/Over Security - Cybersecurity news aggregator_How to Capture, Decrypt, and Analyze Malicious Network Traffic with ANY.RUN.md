---
title: How to Capture, Decrypt, and Analyze Malicious Network Traffic with ANY.RUN
url: https://any.run/cybersecurity-blog/how-to-analyze-malicious-network-traffic/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-03
fetch_date: 2025-10-06T19:16:27.015624
---

# How to Capture, Decrypt, and Analyze Malicious Network Traffic with ANY.RUN

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2022/10/mini-logo.png)](/cybersecurity-blog/)

* + Search

![How to Capture, Decrypt, and Analyze Malicious Network Traffic with ANY.RUN](/cybersecurity-blog/wp-content/uploads/2024/11/traffic_blog.jpg)

[Analyst Training](/cybersecurity-blog/category/training/)

# How to Capture, Decrypt, and Analyze Malicious Network Traffic with ANY.RUN

November 2, 2024

[Add comment](#comments-9599)
3241 views
7 min read

[Home](/cybersecurity-blog/)[Analyst Training](/cybersecurity-blog/category/training/)

How to Capture, Decrypt, and Analyze Malicious Network Traffic with ANY.RUN

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1402
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3024
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3048
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Analyst Training](/cybersecurity-blog/category/training/)

How to Capture, Decrypt, and Analyze Malicious Network Traffic with ANY.RUN

Network traffic analysis provides critical insights into malware and phishing attacks. Doing it effectively requires using proper tools like ANY.RUN’s [Interactive Sandbox](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=network_analysis&utm_term=021124&utm_content=linktolanding). It simplifies the entire process, letting you investigate threats with ease and speed.

Take a look at the key ways you can monitor and analyze network activity with the service.

## Connections

Examining network connections involves looking at source and destination IP addresses, ports, URLs, and protocols. During this process, you can observe all activities that may pose a risk to the system, such as connections to known malicious domains and attempts to access external resources.

To correlate the network activity with other behaviors or components of the malware, ANY.RUN identifies the process name and [Process Identifier](https://any.run/cybersecurity-blog/advanced-process-details/) (PID) initiating the connection. This allows you to gain a better understanding of the threat’s functionality and purpose.

![](/cybersecurity-blog/wp-content/uploads/2024/11/connections_section-1024x221.png)

In the *Connections* section, additional attributes like the country (CN) and Autonomous System Number (ASN) provide context for the geographical location and the organization managing the IP address.

The service also lists DNS requests that help you identify malicious domains used for Command & Control (C&C) communication or phishing campaigns.

### Use Case: Identifying Agent Tesla’s Data Exfiltration Attempt

Consider the [following sandbox session](https://app.any.run/tasks/0845d9f1-8ab5-4755-a213-ab65d9693828/?utm_source=anyrunblog&utm_medium=article&utm_campaign=network_analysis&utm_term=021124&utm_content=linktoservice). Here, we can discover a malicious connection to an external server.

![](/cybersecurity-blog/wp-content/uploads/2024/11/image-1024x218.png)

We can navigate to the process that started this connection (PID 6904) to see the details.

![](/cybersecurity-blog/wp-content/uploads/2024/11/image2-1024x849.png)

The service displays two signatures related to the connection, which specify that it was made to a server suspected of data theft over the SMTP port. The sandbox also links the process of [Agent Tesla](https://any.run/malware-trends/agenttesla), a malware family used by cyber criminals for remote control and data exfiltration.

![](/cybersecurity-blog/wp-content/uploads/2024/11/image3-1024x573.png)

Thanks to ANY.RUN’s integration of [Suricata IDS](https://any.run/cybersecurity-blog/new-threat-details-window/), you can discover triggered detection rules by navigating to the *Threats* tab. The detection of data exfiltration over SMTP in this case is done without decryption. The sandbox relies solely on specific sequences of packet lengths characteristic of sending victim data.

## HTTP Requests and Content

ANY.RUN provides comprehensive analysis of HTTP requests and their content. To access header information, simply navigate to the *Network* tab. Here, you’ll find a detailed list of all HTTP requests recorded by the sandbox.

![](/cybersecurity-blog/wp-content/uploads/2024/11/requests_one-1024x224.png)

Click on a specific request to view its headers, which include information such as the request method, user-agent, cookies, and response status codes.

ANY.RUN also offers static analysis of the resources transmitted as part of HTTP requests and responses. These may include HTML pages, binary, and other types of files. The sandbox extracts their metadata and strings.

### Use Case: Discovering a Server for Collecting Stolen Passwords

When investigating phishing attacks, it is sometimes necessary to check which server ends up receiving the passwords entered by victims on a malicious webpage. To accomplish this task, we need to enable...