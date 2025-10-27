---
title: Opening the Door for a Knock: Creating a Custom DShield Listener, (Thu, Dec 29th)
url: https://isc.sans.edu/diary/rss/29382
source: SANS Internet Storm Center, InfoCON: green
date: 2022-12-30
fetch_date: 2025-10-04T02:45:20.855885
---

# Opening the Door for a Knock: Creating a Custom DShield Listener, (Thu, Dec 29th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29380)
* [next](/diary/29384)

# [Opening the Door for a Knock: Creating a Custom DShield Listener](/forums/diary/Opening%2Bthe%2BDoor%2Bfor%2Ba%2BKnock%2BCreating%2Ba%2BCustom%2BDShield%2BListener/29382/)

**Published**: 2022-12-29. **Last Updated**: 2022-12-29 16:14:46 UTC
**by** [Jesse La Grew](/handler_list.html#jesse-la-grew) (Version: 1)

[0 comment(s)](/diary/Opening%2Bthe%2BDoor%2Bfor%2Ba%2BKnock%2BCreating%2Ba%2BCustom%2BDShield%2BListener/29382/#comments)

There are a variety of services listening for connections on DShield honeypots [1]. Different systems scanning the internet can connect to these listening services due to exceptions in the firewall. Any attempted connections blocked by the firewall are logged and can be analyzed later. This can be useful to see TCP port connection attempts, but it's usefulness is limited. Without the ability to complete the SYN, SYN-ACK, ACK handshake process other protocol data may not be sent.

There are a few easy steps to create a listener to try and collect some additional data:

1. Modify firewall to open port
2. Start listener with socat
3. Create cron job to start listener script on boot

These steps will be outlined for opening a listener on TCP 6889.

##

## **Modify Firewall to Open Port**

Before opening the firewall port, it's probably a good idea to check what is already listening on the honeypot. If there is already a service listening on the port that will be exposed, this change may allow remote internet connections to a service that's not desired. To check for listening services, I ran sudo netstat -tulpn | grep LISTEN.

![](https://isc.sans.edu/diaryimages/images/2022-12-29_Figure1(1).png)
**Figure 1: Listing applications listening for network connections**

TCP 6889 is already listening in my case since the socat listening command is already running.

The firewall used on the honeypot is nftables [2]. To add the firewall rule, the nftables instructions could be followed to allow this port by running the following command:

```

sudo nft add rule ip filter INPUT iifname "eth0" tcp dport 6889 counter accept
```

This would open the port immediately, but only for a limited time until the honeypot rebooted. Upon reboot, the rules would be flushed and read from the file /etc/network/ruleset.nft. To keep this exception persistent, the ruleset must be modified. After modification of this file, the honeypot would need to be rebooted or the nftables service restarted by sudo systemctl restart nftables.

To modify the file /etc/network/ruleset.nft, you can use your text editor of choice, save the changes and then restart the honeypot or the nftables service.

![](https://isc.sans.edu/diaryimages/images/2022-12-29_Figure2.png)
**Figure 2: Firewall rules for honeypot in ruleset.nft**

In this case, I added the rule after other honeypot listener exceptions to keep everything organized and consistent.

##

## **Start Listener with socat**

Netcat is one very common utility that is used to connect to remote services and can also act as a listener [3]. I went with socat in this example based on the recommendation from Guy Bruneau. Socat can communicate over a variety of additional protocols and has some handy output options that help with data collection [4].

To start the listener, it's as easy as running one command:

```

socat -d -d -d -v -u TCP4-LISTEN:6889,reuseaddr,fork OPEN:<input logging location here>,creat,append
```

This will listen for connections on port 6889 and also redirect any input to the specified log file. In this case the logs are stored in the "logs/custom" directory. There is also some additional output for stderr (standard error).

```

socat -d -d -d -v -u TCP4-LISTEN:6889,reuseaddr,fork OPEN:/logs/custom/hpot.log,creat,append 2>> /logs/custom/socat_6889_verbose.txt
```

**![](https://isc.sans.edu/diaryimages/images/2022-12-29_Figure3.png)
Figure 3: Socat command for listening on port 6889 with local log output**

Looking at example data received, here are some examples of the log data.

**Log Data**

![](https://isc.sans.edu/diaryimages/images/2022-12-29_Figure4.png)
**Figure 4: Socat logged transfer data**

**Standard Error (verbose) Log Data**

```

2022/12/17 03:10:13 socat[1310] I accept(5, {2, AF=2 87.236.176.139:39125}, 16) -> 6
2022/12/17 03:10:13 socat[1310] N accepting connection from AF=2 87.236.176.139:39125 on AF=2 192.168.68.178:6889
2022/12/17 03:10:13 socat[1310] I permitting connection from AF=2 87.236.176.139:39125
2022/12/17 03:10:13 socat[1310] N forked off child process 5772
2022/12/17 03:10:13 socat[1310] I close(6)
2022/12/17 03:10:13 socat[1310] I still listening
2022/12/17 03:10:13 socat[1310] N listening on AF=2 0.0.0.0:6889
2022/12/17 03:10:13 socat[5772] I just born: child process 5772
2022/12/17 03:10:13 socat[5772] I close(4)
2022/12/17 03:10:13 socat[5772] I close(3)
2022/12/17 03:10:13 socat[5772] I just born: child process 5772
2022/12/17 03:10:13 socat[5772] I close(5)
2022/12/17 03:10:13 socat[5772] I setting option "o-create" to 1
2022/12/17 03:10:13 socat[5772] I setting option "append" to 1
2022/12/17 03:10:13 socat[5772] N opening regular file "/logs/custom/hpot.log" for writing
2022/12/17 03:10:13 socat[5772] I open("/logs/custom/hpot.log", 02101, 0666) -> 5
2022/12/17 03:10:13 socat[5772] I resolved and opened all sock addresses
2022/12/17 03:10:13 socat[5772] N starting data transfer loop with FDs [6,6] and [5,5]
> 2022/12/17 03:10:16.749080 length=198 from=0 to=197
GET / HTTP/1.1\r
Host: <redacted>:6889\r
User-Agent: Mozilla/5.0 (compatible; InternetMeasurement/1.0; +https://internet-measurement.com/)\r
Connection: close\r
Accept: */*\r
Accept-Encoding: gzip\r
\r
2022/12/17 03:10:16 socat[5772] I transferred 198 bytes from 6 to 5
2022/12/17 03:10:36 socat[5772] N socket 1 (fd 6) is at EOF
2022/12/17 03:10:36 socat[5772] I shutdown(6, 2)
2022/12/17 03:10:36 socat[5772] N exiting with status 0
2022/12/17 03:10:36 socat[1310] N childdied(): handling signal 17
2022/12/17 03:10:36 socat[1310] I childdied(signum=17)
2022/12/17 03:10:36 socat[1310] I childdied(17): cannot identify child 5772
2022/12/17 03:10:36 socat[1310] I waitpid(): child 5772 exited with status 0
2022/12/17 03:10:36 socat[1310] I waitpid(-1, {}, WNOHANG): No child processes
2022/12/17 03:10:36 socat[1310] I childdied() finished

2022/12/17 03:11:25 socat[1310] I accept(5, {2, AF=2 87.236.176.220:33827}, 16) -> 6
2022/12/17 03:11:25 socat[1310] N accepting connection from AF=2 87.236.176.220:33827 on AF=2 192.168.68.178:6889
2022/12/17 03:11:25 socat[1310] I permitting connection from AF=2 87.236.176.220:33827
2022/12/17 03:11:25 socat[1310] N forked off child process 5804
2022/12/17 03:11:25 socat[1310] I close(6)
2022/12/17 03:11:25 socat[1310] I still listening
2022/12/17 03:11:25 socat[1310] N listening on AF=2 0.0.0.0:6889
2022/12/17 03:11:25 socat[5804] I just born: child process 5804
2022/12/17 03:11:25 socat[5804] I close(4)
2022/12/17 03:11:25 socat[5804] I close(3)
2022/12/17 03:11:25 socat[5804] I just born: child process 5804
2022/12/17 03:11:25 socat[5804] I close(5)
2022/12/17 03:11:25 socat[5804] I setting option "o-create" to 1
2022/12/17 03:11:25 socat[5804] I setting option "append" to 1
2022/12/17 03:11:25 socat[5804] N opening regular file "/logs/custom/hpot.log" for writing
2022/12/17 03:11:25 socat[5804] I open("/logs/custom/hpot.log", 02101, 0666) -> 5
2022/12/17 03:11:25 socat[5804] I resolved and opened all sock addresses
2022/12/17 03:11:25 socat[5804] N starting data transfer loop with FDs [6,6] and [5,5]
> 2022/12/17 03:11:28.944065 length=44 from=0 to=43
...,'......Cookie: mstshash=eltons\r
..\b.....2022/12/17 03:11:28 socat[5804] I transferred 44 bytes from 6 to 5
2022/12/17 03:11:31 socat[5804] N socket 1 (fd 6...