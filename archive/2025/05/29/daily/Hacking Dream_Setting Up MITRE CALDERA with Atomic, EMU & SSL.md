---
title: Setting Up MITRE CALDERA with Atomic, EMU & SSL
url: https://www.hackingdream.net/2025/05/setting-up-mitre-caldera-with-atomic-emu-ssl.html
source: Hacking Dream
date: 2025-05-29
fetch_date: 2025-10-06T22:26:31.567973
---

# Setting Up MITRE CALDERA with Atomic, EMU & SSL

* [Home](http://www.hackingdream.net)
* [About Author](http://www.hackingdream.net/p/about-author.html)
* [Contact US](http://www.hackingdream.net/p/contact-us.html)

[# ![Hacking Dream](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI3MZul9awsB7xmLlAs9J9xDOsiYxbMQoa4EQkvg9T9oe4q5zkZRqV0W4UN2KhrQQWPLveTvQ9kkuHu2HfrahqY0Gc53G1cVCwQNY2G3MVkEOJoDvLIK9lFtBUc-HhRciiteWdHYV4SaE/s1600/Size-Modified.png)](https://www.hackingdream.net/)

Main menu

close

* [Home](http://www.hackingdream.net)
* [AI Sec](https://www.hackingdream.net/search/label/AI)
* [AI Pentest](http://www.hackingdream.net/search/label/AI%20Attacks)
* [Cheatsheets](https://www.hackingdream.net/search/label/Cheatsheet)
* [Pentest](https://www.hackingdream.net/search/label/Pentest)
* [\_Active Directory](https://www.hackingdream.net/search/label/Active%20Directory)
* [\_Linux](http://www.hackingdream.net/search/label/Kali%20Linux)
* [\_Wireless](http://www.hackingdream.net/search/label/Wifi%20Hacking)
* [\_Target Hacking](http://www.hackingdream.net/search/label/Target%20Hacking)
* [Purple Team](https://www.hackingdream.net/search/label/Purple%20Team)
* [Bin Exp](https://www.hackingdream.net/search/label/Exploitation)
* How To
* [\_Blogging](http://www.hackingdream.net/search/label/Blogging)
* [\_Solved Problems](http://www.hackingdream.net/search/label/Solved%20Problems)
* [\_Money Making](http://www.hackingdream.net/search/label/Money%20Making)
* [\_Top Ten](http://www.hackingdream.net/search/label/Top%20Ten)
* [\_Gaming](http://www.hackingdream.net/search/label/Games)

### Setting Up MITRE CALDERA with Atomic, EMU & SSL

[May 28, 2025](https://www.hackingdream.net/2025/05/setting-up-mitre-caldera-with-atomic-emu-ssl.html "permanent link")

##

In this tutorial, you’ll learn how to build and run a customized **MITRE CALDERA** Docker image with the *Atomic* and *EMU* plugins enabled, secured by a self-signed SSL certificate via HAProxy.

[![Setting Up MITRE CALDERA](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2XoMFyt49OhCClwiIRgmhSLyv0UF5gHqrRw06i4lD81_r9VLoe0jU7j0-mykCHwFu97zWvjwO2_rhQib_OxLYp6gvV1-JlEUAppERNZmDpQ8QxcsvbfZHfmTcIgj-OS8nDHNMDWeYdq5joXGnhLU7-3snzkDGO6KnuE7YjrYMY12Z_eX6DydCiZh8abbs/w640-h426/Setting%20Up%20MITRE%20CALDERA.jpg "Setting Up MITRE CALDERA")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2XoMFyt49OhCClwiIRgmhSLyv0UF5gHqrRw06i4lD81_r9VLoe0jU7j0-mykCHwFu97zWvjwO2_rhQib_OxLYp6gvV1-JlEUAppERNZmDpQ8QxcsvbfZHfmTcIgj-OS8nDHNMDWeYdq5joXGnhLU7-3snzkDGO6KnuE7YjrYMY12Z_eX6DydCiZh8abbs/s1536/Setting%20Up%20MITRE%20CALDERA.jpg)

### Prerequisites

* Docker & Docker Compose installed on your host. (sudo apt install docker.io docker-compose -y)
* git command-line tools.
* Basic familiarity with editing files in a terminal (e.g., `nano`, `sed`).

### 1. Clone the CALDERA Repository

```
# Recursively clone the Caldera repository if you have not done so
git clone https://github.com/mitre/caldera.git --recursive
cd caldera
```

### 2. Enable the Atomic Plugin

Edit the `Dockerfile` to re-enable the Atomic plugin:

```
nano Dockerfile

# Inside the Dockerfile, remove the line that disables atomic:
sed -i '/- atomic/d' conf/local.yml;
```

### 3. Install HAProxy & Generate SSL Certificate

Add the following to your `Dockerfile` by running `nano Dockerfile` to install HAProxy and create a self-signed cert:

```
# Install HAProxy
RUN apt-get update &&
DEBIAN\_FRONTEND=noninteractive apt-get install -y --no-install-recommends
haproxy &&
apt-get clean &&
rm -rf /var/lib/apt/lists/\*

# Generate self-signed cert (key + cert → PEM)
RUN openssl req -x509 -newkey rsa:4096
-keyout plugins/ssl/conf/private.key
-out plugins/ssl/conf/public.crt
-days 365 -nodes
-subj "/C=US/ST=VA/L=McLean/O=Mitre/OU=IT/CN=mycaldera.caldera" &&
cat plugins/ssl/conf/private.key plugins/ssl/conf/public.crt > plugins/ssl/conf/certificate.pem

# Configure HAProxy to use the new cert
RUN cp plugins/ssl/templates/haproxy.conf conf/ &&
sed -i 's#bind\ \*:8443\ ssl\ crt\ plugins/ssl/conf/insecure\_certificate.pem#bind\ \*:8443\ ssl\ crt\ plugins/ssl/conf/certificate.pem#g' conf/haproxy.conf
```

### 4. Enable EMU & SSL Plugins

Edit `conf/default.yml` to include both `emu` and `ssl` under the `plugins:` section:

```
nano conf/default.yml

# Add under `plugins:`:

- atomic
- emu
- ssl
```

### 5. Build & Run the Docker Image

Build the image with the `full` variant (includes Atomic support) and then run it:

```
# Build (change tag as desired)
docker build --build-arg VARIANT=full -t caldera .

# Run in detached mode, exposing ports 8888 (UI/API) & 8443 (SSL)
docker run -d -p 8888:8888 -p 8443:8443 caldera\:latest

#Run Docker Container with Persistent Data
docker volume create caldera-data
docker run -d -p 8888:8888 -p 8443:8443 -v caldera-data:/usr/src/app/data caldera\:latest
```

### 6. Access the Container & Retrieve Credentials

If you need a shell inside the container or want to grab the default `red` user password:

```
# Get an interactive shell
sudo docker exec -it $(docker ps -qf "ancestor=caldera:latest") /bin/bash

# View the `red` user password
cat /usr/src/app/conf/local.yml | grep red
```

### 7. Connect to CALDERA

* Open your browser to [https://your-host:8443](https://<your-host>:8443) for the SSL-secured UI.
* Or use `http://<your-host>:8888` if you prefer the non-SSL port.
* Default creds are red/admin

*That’s it!* You now have a fully functional CALDERA instance with Atomic, EMU, and SSL support. Experiment with adversary emulation, test your detections, and iterate on your Purple Team workflows. Leave a comment below if you run into any issues or have questions!

[![](https://img1.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/7320167475718896234/1505511525776420839 "Email Post")

[Cheatsheet](https://www.hackingdream.net/search/label/Cheatsheet)

By:

[Bhanu Namikaze](https://www.blogger.com/profile/11095863747944917885 "author profile")

![](//lh5.googleusercontent.com/-5klQY__bhSE/AAAAAAAAAAI/AAAAAAAAFfc/f8794NZCX3M/s512-c/photo.jpg)

##### Bhanu Namikaze

Bhanu Namikaze is an Ethical Hacker, Security Analyst, Blogger, Web Developer and a Mechanical Engineer. He Enjoys writing articles, Blogging, Debugging Errors and Capture the Flags. Enjoy Learning; There is Nothing Like Absolute Defeat - Try and try until you Succeed.

#### No comments:

#### Post a Comment

## Search for a Post

## Recent Posts

[Recent Posts Widget](http://www.hackingdream.net/2015/12/recent-post-widgets-for-blogger-with-thumbnails.html)
Your browser does not support JavaScript!

## Popular Posts

[Recent Posts Widget](http://www.hackingdream.net/2015/12/recent-post-widgets-for-blogger-with-thumbnails.html)
Your browser does not support JavaScript!

* [facebook](http://www.facebook.com/HackingDream)
* [twitter](http://www.twitter.com/HackingDream)
* [youtube](https://www.youtube.com/channel/UCKgOUVTaT-6LKLvUQhfBhig)

## About us

![about footer](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPNiXyJNB8w-IovFpOQWeftMUoBrVjS1T-fL9Xe9iixFQvIijmZC4TC0j8Y8E384vrStxGn58Etcw-KbG-ISpaK5eL3payYyjd84WHa9Ps9GQUFd0qToRbnLzW4Sz4R5s46i73WmcJvPQb/s1600/Size-Modified.png)

## Labels

[Active Directory](https://www.hackingdream.net/search/label/Active%20Directory)

[AI](https://www.hackingdream.net/search/label/AI)

[AI Attacks](https://www.hackingdream.net/search/label/AI%20Attacks)

[Andriod](https://www.hackingdream.net/search/label/Andriod)

[Android](https://www.hackingdream.net/search/label/Android)

[AppSec](https://www.hackingdream.net/search/label/AppSec)

[BackTrack](https://www.hackingdream.net/search/label/BackTrack)

[Blogging](https://www.hackingdream.net/search/label/Blogging)

[Buffer Overflow](https://www.hackingdream.net/search/label/Buffer%20Overflow)

[C Programs](https://www.hackingdream.net/search/label/C%20Programs)

[Certifications](https://www.hackingdream.net/search/label/Certifications)

[Cheatsheet](https://www.hackingdream.net/search/...