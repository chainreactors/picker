---
title: Kazakhstan - the world's last SSLv2 superpower... and a country with potentially vulnerable last-mile internet infrastructure, (Wed, Jun 28th)
url: https://isc.sans.edu/diary/rss/29988
source: SANS Internet Storm Center, InfoCON: green
date: 2023-06-29
fetch_date: 2025-10-04T11:50:20.298554
---

# Kazakhstan - the world's last SSLv2 superpower... and a country with potentially vulnerable last-mile internet infrastructure, (Wed, Jun 28th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29984)
* [next](/diary/29990)

# [Kazakhstan - the world's last SSLv2 superpower... and a country with potentially vulnerable last-mile internet infrastructure](/forums/diary/Kazakhstan%2Bthe%2Bworlds%2Blast%2BSSLv2%2Bsuperpower%2Band%2Ba%2Bcountry%2Bwith%2Bpotentially%2Bvulnerable%2Blastmile%2Binternet%2Binfrastructure/29988/)

**Published**: 2023-06-28. **Last Updated**: 2023-06-28 06:32:20 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[1 comment(s)](/diary/Kazakhstan%2Bthe%2Bworlds%2Blast%2BSSLv2%2Bsuperpower%2Band%2Ba%2Bcountry%2Bwith%2Bpotentially%2Bvulnerable%2Blastmile%2Binternet%2Binfrastructure/29988/#comments)

In my last Diary, we looked at internet-connected web servers, which still support SSL version 2.0. Since this cryptographic protocol was deprecated all the way back in 2011, one might not think that there would be many such devices left on the internet, nevertheless, we have shown that there still appear to be over 460,000 of them[[1](https://isc.sans.edu/diary/29908)].

Last week, I was talking to [Justin Searle](https://www.sans.org/latest/profiles/justin-searle/), one of our fellow SANS instructors, about the SSLv2 situation, and Justin raised a good point about how it might be interesting to learn what the devices are and where they are located… So, I have decided to find out – I did a quick analysis with the help of [Shodan](https://www.shodan.io/), and the results turned out to be quite interesting indeed!

While web servers which support SSLv2 are located in many countries all over the world, as the following image shows, we can clearly see that there are “hot spots” where their concentration is highest.

[![](https://isc.sans.edu/diaryimages/images/23-06-28-map.png)](https://isc.sans.edu/diaryimages/images/23-06-28-map.png)

In fact, if we filter out just the top 10 countries with the highest numbers of web servers supporting SSLv2, we can see that there are 3 at the top, which account for most of what’s out there…

[![](https://isc.sans.edu/diaryimages/images/23-06-28-chart.png)](https://isc.sans.edu/diaryimages/images/23-06-28-chart.png)

[![](https://isc.sans.edu/diaryimages/images/23-06-28-map2.png)](https://isc.sans.edu/diaryimages/images/23-06-28-map2.png)

It is worth noting that we get similar results (at least in the top spot) with regards to geographic distribution of systems which support only SSLv2 and SSLv3.

[![](https://isc.sans.edu/diaryimages/images/23-06-28-sslv2.png)](https://isc.sans.edu/diaryimages/images/23-06-28-sslv2.png)

[![](https://isc.sans.edu/diaryimages/images/23-06-28-sslv2-sslv3.png)](https://isc.sans.edu/diaryimages/images/23-06-28-sslv2-sslv3.png)

Getting back to all devices which support SSL version 2.0, we saw that most of them are located in Kazakhstan, Tunisia and in the U.S.

It can be clearly seen that in Tunisia and in the United States, public IP addresses where SSLv2 support was detected are located in IP ranges/autonomous systems assigned to different ISPs, and that devices to which these IP addresses are mapped are running different types of software (if we can identify the SW at all).

[![](https://isc.sans.edu/diaryimages/images/23-06-28-tn-us.png)](https://isc.sans.edu/diaryimages/images/23-06-28-tn-us.png)

The situation was somewhat different in Kazakhstan… But before we get to that, let’s take a look at which web servers are, according to Shodan, most common when it comes to SSLv2 support.

[![](https://isc.sans.edu/diaryimages/images/23-06-28-time-global.png)](https://isc.sans.edu/diaryimages/images/23-06-28-time-global.png)

As we can see from the chart, by far the most common has been for some time the GoAhead Embedded Web Server. As its name suggests, it is a lightweight web server intended for integration into IoT and embedded devices[[2](https://www.embedthis.com/goahead/)].

While this software is still being developed, it is worth mentioning that several high-impact vulnerabilities (for example, CVE-2017-17562 and CVE-2019-5096, to name just two[[3](https://www.securityweek.com/devices-running-goahead-web-server-prone-remote-attacks/),[4](https://nsfocusglobal.com/advisory-two-high-risk-vulnerabilities-goahead-web-server/)]) have been identified in some of its older versions (e.g., those, which one might expect to be configured to support SSLv2).

At this point, we can get back to the large number of SSLv2 devices in Kazakhstan.

Almost all of them are located in IP ranges assigned to the JSC Kazakhtelecom, the largest ISP in Kazahkstan…

[![](https://isc.sans.edu/diaryimages/images/23-06-28-kz-asn.png)](https://isc.sans.edu/diaryimages/images/23-06-28-kz-asn.png)

…and, as you have probably guessed by now, most of them seem to be running the GoAhead Embedded Web Server.

[![](https://isc.sans.edu/diaryimages/images/23-06-28-kz-servers.png)](https://isc.sans.edu/diaryimages/images/23-06-28-kz-servers.png)

In fact, most of these devices appear to be of the same exact type - they use an identical SSL server certificate (serial number “fe676b96c70714f9”, issuing organization “CIG”) and if one were to connect to any of them over HTTP(S), one would be greeted by the same login screen for a “GPON Home Gateway”[[5](https://en.wikipedia.org/wiki/GPON)].

Given this data, it seems probable that most of the devices which support SSLv2 in Kazakhstan are last-mile network devices made by a Chinese company Cambridge Industries Group (CIG)[[6](https://www.cigtech.com/)] and used by JSC Kazakhtelecom to provide connectivity to their customers.

Due to the support of SSL version 2.0, it is also probable that these devices are quite old, which, in connection with the fact that they are running the GoAhead Embedded Web Server, would seem to indicate that they might be affected by known high-impact vulnerabilities, even if we can’t reliably identify the specific version of the software installed on the devices.

If these assumptions were true, and it seems probable they might be, it would make large portions of the internet in Kazakhstan potentially vulnerable to malicious actions of even less advanced threat actors... On the other hand, it should be mentioned that while it is almost certain that the identified devices are running outdated and vulnerable versions of the webserver, it is possible that the vulnerable components themselves might not be accessible to a remote attacker, and it might therefore not be possible to use exploits for known vulnerabilities in order to compromise the devices.

It should also be noted that, although, at the time of writing, Shodan detects over 166 thousand (please disregard the discrepancy between this number and the values shown in the images above – Shodan seems to count systems differently in different tools and views) devices of the type discussed above within Kazakhstan, it is possible that there might really be significantly less of them, since it is possible that the ISP, in whose networks these devices are placed, might have repeatedly mapped multiple public IP addresses to a single device.

In any case, once I’ve gathered all the data discussed above, it seemed appropriate to get in touch with JSC  Kazakhtelecom and the Kazakhstan national CERT, KZ-CERT[[7](https://www.cert.gov.kz/)], inform them about the situation and give them time to take any steps they might believe necessary before I publish any information about it.

While Kazakhtelecom didn’t respond to even repeated requests for communication, KZ-CERT did. They evaluated the information I’ve provided and let me know that they don’t object to me releasing it publicly, though they did ask if I could provide them with some more detailed data about specific IP addresses, which the situation concerned. I have done so and here we a...