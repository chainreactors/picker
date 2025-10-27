---
title: Forwarding Traffic Through SSH
url: https://www.blackhillsinfosec.com/forwarding-traffic-through-ssh/
source: Black Hills Information Security
date: 2023-02-24
fetch_date: 2025-10-04T07:58:21.122301
---

# Forwarding Traffic Through SSH

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

23
Feb
2023

[Fernando Panizza](https://www.blackhillsinfosec.com/category/author/fernando-panizza/), [General InfoSec Tips & Tricks](https://www.blackhillsinfosec.com/category/infosec-101/general-infosec-tips-tricks/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/)

# [Forwarding Traffic Through SSH](https://www.blackhillsinfosec.com/forwarding-traffic-through-ssh/)

[Fernando Panizza](https://www.blackhillsinfosec.com/team/fernando-panizza/) //

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/02/BLOG_chalkboard_00617-1024x576.png)

This was meant to be an OpenSSH how-to blog, but since I had time, I decided to read the [man pages](https://man7.org/linux/man-pages/man1/ssh.1.html) (manual pages that you can access on a Linux terminal by typing `man ssh`) and had fun chasing every possible rabbit hole while at it. While going through the man pages, I learned that it was possible to use SSH to set up VPN networks and decided to give it a try. Although I just learned this and haven’t used it on a test yet, I think it could be a nice to have resource, especially in cases where the tool in use does not support SOCKS proxies or the protocol is not supported by Proxychains.

## Port Forwarding

Port forwarding with SSH is a very well-documented subject, but here is a quick recap in case you’re new to it. (You can also find a video explanation by Ralph May here: <https://www.youtube.com/watch?v=zG4jYmHoEr8&t=348s>)

SSH can be used for local, remote, and dynamic port forwarding. Local port forwarding basically opens a port on your local machine (the one that you’re SSHing from) and forwards its traffic to a remote port on the machine or the network you are connecting to. This can be useful once you obtain shell access to a system and find services listening on the loopback or an internal interface. Local port forwarding will allow you to forward that service to a port on your local machine.

The syntax for the command is the following:

```
ssh –N -L local_port:remote_service_ip:remote_service_port
```

Optionally, you can specify on which interface you want the port to listen by adding the IP address before the port.

```
ssh –N -L local_ip:local_port:remote_service_ip:remote_service_port
```

As an example, let’s say you have access to a system (192.168.136.120) and after running netstat, you found that there is a service running on port 8080 of the loopback interface.

For demonstration purposes, we are going to use the Python’s `http.server` module to set a web server listening in the loopback interface of our target host, which will be hosting a simple text file.

On the target host, we run the following commands to create the file and start the server:

```
echo "This is a local service" > file.txt
python3 -m http.server --bind 127.0.0.1 8080
```

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/02/Picture1-3.png)

Server Started on Target Machine

You can forward that port to your local machine with the following command:

```
ssh  -N -L 8081:127.0.0.1:8080  [email protected]
```

This will open port 8081 on your local machine and forward all its traffic to 127.0.0.1:8080 on the remote machine 192.168.136.120.

Now if we request the file at http://127.0.0.1:8081/file.txt on the testing machine, we should be able to access the file hosted at 127.0.0.1:8080 on the target machine.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/02/Picture2-3.png)

File Accessed Using Local Port Forward

Remote port forwarding behaves in the opposite way. It opens a port on the remote machine and forwards all the traffic to that port from the remote network to a local port on the local machine or network. This can be useful when you want to forward a local port to listen on a remote machine.

The syntax for remote port forwarding is similar; this time the `-R` flag is used, and the remote ip and port are specified first.

```
ssh  -N -R [remote_service_ip]:remote_port:local_ip:local_port
```

Going back to the previous example, let’s say you find yourself in the same situation — having access to the system (192.168.136.120) and finding a service listening at 127.0.0.1:8080, but this time ingress traffic is blocked on port 22 of the target machine so local port forwarding is not an option. In cases like this, you can use remote port forwarding to achieve the same result. You can use SSH from the target computer to connect to your testing machine and forward local port 8080 on the target to the remote port 8081 on your testing machine.

```
ssh -N -R 8081:127.0.0.1:8080 [email protected]
```

![](https://www.blackhillsinfosec.com/wp-content/...