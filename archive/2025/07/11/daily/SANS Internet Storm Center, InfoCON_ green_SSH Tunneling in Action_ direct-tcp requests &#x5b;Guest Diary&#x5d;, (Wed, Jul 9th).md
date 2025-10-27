---
title: SSH Tunneling in Action: direct-tcp requests &#x5b;Guest Diary&#x5d;, (Wed, Jul 9th)
url: https://isc.sans.edu/diary/rss/32094
source: SANS Internet Storm Center, InfoCON: green
date: 2025-07-11
fetch_date: 2025-10-06T23:51:03.375626
---

# SSH Tunneling in Action: direct-tcp requests &#x5b;Guest Diary&#x5d;, (Wed, Jul 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32092)
* [next](/diary/32100)

# [SSH Tunneling in Action: direct-tcp requests [Guest Diary]](/forums/diary/SSH%2BTunneling%2Bin%2BAction%2Bdirecttcp%2Brequests%2BGuest%2BDiary/32094/)

**Published**: 2025-07-09. **Last Updated**: 2025-07-10 21:22:00 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/SSH%2BTunneling%2Bin%2BAction%2Bdirecttcp%2Brequests%2BGuest%2BDiary/32094/#comments)

[This is a Guest Diary by Sihui Neo, an ISC intern as part of the SANS.edu [BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

As part of the SANS degree program curriculum, I had the opportunity to set up a honeypot to monitor log activities mimicking a vulnerable server. I used the AWS free tier EC2 instance to set up the honeypot sensor in Japan and deployed Cowrie, a SSH and Telnet honeypot designed to log brute force attacks and shell interaction performed by an attacker.

In addition to the sensor setup, to allow me to easily look at all the logs in a single platform, I purchased a separate virtual private server and installed ELK SIEM, following the setup instructions from ISC mentor, Guy Bruneau’s github page.[[1](https://github.com/bruneaug/DShield-SIEM)] Then setup the sensor to send all logs to the SIEM server.

Since the setup of the honeypot, one of the interesting observations in logs was direct-tcp connection requests. More than 1000 different IPs within a month were seen to have made these requests and more than 75% were made to a single destination IP. In this post, I’ll cover how and why these connections are set up, and where the destination IP points to.

**What did the logs look like?**

*Sample of direct-tcp connection request seen in honeypot logs*

![](https://isc.sans.edu/diaryimages/images/Sihui_Neo_pic10.png)

The sample log on the original event field seen above indicates that the request originated from 127.0.0.1 (the local loopback interface), but when looking at the source.ip in kibana, the actual source IPs were different external addresses.

![](https://isc.sans.edu/diaryimages/images/Sihui_Neo_pic1.png)
*125.20.251.66 was the actual source IP*

Using the source IP 125.20.251.66, I took a look at the traffic before the direct-tcp connection and the PCAP traffic.

![](https://isc.sans.edu/diaryimages/images/Sihui_Neo_pic2.png)
Figure 1. *Logs from 125.20.251.66 at the time of the direct-tcp connection request showing source port of 32069 in a red box*

In Figure 1, I extracted the logs for traffic from source IP 125.20.251.66 as seen in kibana. The line direct-tcp connection request to 77.88.21.158:25 from 127.0.0.1:32069 is highlighted in the red box, yet the source address shows 125.20.251.66 while the source port matches 32069.

Additional evidence is in the PCAP. The entire stream below showed the connection using the source port of 42948, which was indeed the source port for the initial SSH connection as seen in the Figure 1 above, highlighted in a blue box, source IP seen in the last column.

![](https://isc.sans.edu/diaryimages/images/Sihui_Neo_pic3.png)
Figure 2. *PCAP and TCP stream for traffic from 125.20.251.66*

Lastly, the SSH banner SSH-2.0-OpenSSH\_7.4 was seen in Figure 1, highlighted in green as well as in the TCP Stream at the bottom of Figure 2. All these suggested that the traffic was being forwarded or proxied to help obscure the real source IP.

**So how does it work?**
![](https://isc.sans.edu/diaryimages/images/Sihui_Neo_pic4.png)

![](https://isc.sans.edu/diaryimages/images/Sihui_Neo_pic9.png)

**Reconnaissance and Initial access**

As explained before, the attacker has to initiate a connection to the honeypot server to create a SSH tunnel and to do that, they require valid SSH login credentials. This is usually fulfilled by brute forcing. When looking at initial activities of IPs that had direct-tcp connection requests, they had a similar pattern of :

* Only attempting to connect to port 2222
* Throttled brute forcing attempts, meaning brute forcing attempts from the same IP were spaced out at least 2 hours if it failed.
* TTL of less than 50, means starting TTL is likely 64, which could be indicative of Linux/MAX OSX systems [[3](https://www.imperva.com/learn/performance/time-to-live-ttl/)]
* SSH client hash fingerprint: acaa53e0a7d7ac7d1255103f37901306

After successfully obtaining valid SSH credentials, the SSH tunnel would usually be set up within the second.

**Going somewhere?**

As mentioned before, more than 1000 IPs were seen to have made these proxy connections in the honeypot and interestingly, the majority, more than 75%, were seen to be proxying to the destination IP of 77.88.21.158 at port 25.

![](https://isc.sans.edu/diaryimages/images/Sihui_Neo_pic5.png)

77.88.21.158 port 25 seems to be the smtp server for yandex mail, based in Russia [[4](https://search.censys.io/hosts/77.88.21.158)] which is a common blocked location for many countries.

![](https://isc.sans.edu/diaryimages/images/Sihui_Neo_pic6.png)

Referencing the SSH tunnel diagram shown earlier, this likely means that the client set their email client to use ‘127.0.0.1:1080’ as the proxy, which instructed the email traffic to go through the established SSH tunnel to reach 77.88.21.158.

As the honeypot server does not really have SSH service on port 2222, the connection is closed quickly after the tunnel is set up and the PCAP logs do not capture outbound traffic to the destination IPs.

**What’s the worst that could happen?**

Direct-tcp connections are usually a form of proxy connection that uses the honeypot server in this case, as an intermidiary to either mask origin IPs or to bypass traffic rules. The reason attackers use compromised servers instead of paid or free VPN is attribution and/or possibly consistency. Commercial VPN requires sign up and services like peer-to-peer networks do not usually allow users to choose the route or hops.

Establishing a SSH tunnel does not require root and can easily be set up as long as you have a valid user’s credentials to login to the SSH server (honeypot, in this case). In fact, brute forcing is one of the more common and easy tactics to gain access to vulnerable servers due to password leaks, reusing of passwords and default passwords.

Once your server is compromised and successfully used as a proxy, your server may be susceptible to:

* Malicious Traffic Attribution: Actors can route illegal activities (hacking, fraud, DDoS) through your server, making you appear responsible.
* Bandwidth Overuse: Proxy traffic consumes resources, which can lead to throttling by your host/ISP and extra costs especially in the cloud.
* IP Blacklisting: Your server’s IP may end up on firewall blacklists preventing you from your daily activities

[1] https://github.com/bruneaug/DShield-SIEM
[2] https://ma.ttias.be/socks-proxy-linux-ssh-bypass-content-filters/
[3] https://www.imperva.com/learn/performance/time-to-live-ttl/
[4] https://search.censys.io/hosts/77.88.21.158
[5] https://www.sans.edu/cyber-security-programs/bachelors-degree/

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My GitHub Page](https://github.com/bruneaug/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [Analysis](/tag.html?tag=Analysis) [BACS](/tag.html?tag=BACS) [directtcp](/tag.html?tag=directtcp) [DShield](/tag.html?tag=DShield) [Investigation](/tag.html?tag=Investigation) [tunneling](/tag.html?tag=tunneling)

[0 comment(s)](/diary/SSH%2BTunneling%2Bin%2BAction%2Bdirecttcp%2Brequests%2BGuest%2BDiary/32094/#comments)

* [previous](/diary/32092)
* [next](/diary/32100)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives]...