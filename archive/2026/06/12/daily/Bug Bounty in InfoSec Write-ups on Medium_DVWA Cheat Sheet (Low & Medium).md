---
title: DVWA Cheat Sheet (Low & Medium)
url: https://infosecwriteups.com/dvwa-cheat-sheet-low-medium-c7490e76f1b5?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-06-12
fetch_date: 2026-06-13T06:10:08.768396
---

# DVWA Cheat Sheet (Low & Medium)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdvwa-cheat-sheet-low-medium-c7490e76f1b5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdvwa-cheat-sheet-low-medium-c7490e76f1b5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c7490e76f1b5---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c7490e76f1b5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# DVWA Cheat Sheet (Low & Medium)

[![Loay Salah](https://miro.medium.com/v2/resize:fill:64:64/1*Oyx6_UZiWR_io6xmVpWaBg.jpeg)](https://prankster99.medium.com/?source=post_page---byline--c7490e76f1b5---------------------------------------)

[Loay Salah](https://prankster99.medium.com/?source=post_page---byline--c7490e76f1b5---------------------------------------)

11 min read

·

Aug 30, 2024

--

1

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dc7490e76f1b5&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdvwa-cheat-sheet-low-medium-c7490e76f1b5&source=---header_actions--c7490e76f1b5---------------------post_audio_button------------------)

Share

![]()

**Damn Vulnerable Web Application**

## **Brute Force: Low & Medium**

Press enter or click to view image in full size

![]()

**Just testing with this username & password to get the error message (we will need it)**

As you can see, we got this error message, So let's hop on Burp Suite and intercept the GET Request

![]()

**This is the GET Request**

Send it to the Intruder, hit Clear to clear any saved parameter, select the password that you sent for mine it was ‘admin’ so select it and hit Add

Press enter or click to view image in full size

![]()

**The word after (password=) must be colored like this**

Now let's go to the payloads section in the intruder and load our txt payload file (i used the top 100 words from rockyou.txt wordlist for simplicity)

![]()

Now we set the payload, How can we find if tha password is right ot not ?
So,let's go to settings in the intruder section to make our customization

![]()

**add incorrect word to these words**

Intruder use these words to define if the attack fails, so it have some famous error messages
In the First Image that i posted, there was word ‘incorrect’ in it
So, after we added ‘incorrect’ , if we got the right password of course we will not find the ‘incorrect’ word. NOW Let's start the attack

Press enter or click to view image in full size

![]()

**The Password is ‘password’**

The password section is the only one that didn't find the ‘incorrect’ word

Press enter or click to view image in full size

![]()

**Low Level**

**Brute Force: Medium**In medium level we can make the same steps as i did in low level but i’ll go through another tool just for a change, we'll use [wfuzz](https://www.kali.org/tools/wfuzz/) tool on kali linux

Press enter or click to view image in full size

![]()

This is the Intercept, as you can see the password must be ‘FUZZ’ , but why?

to tell [wfuzz](https://www.kali.org/tools/wfuzz/) tool that the password is the one that we want to brute force it

Press enter or click to view image in full size

![]()

this is the code that i used for the attack

```
wfuzz -c -z file,/home/prankster/top_100_Rock_You.txt -b 'security=medium; PHPSESSID=17ef46f3cec5a583f4bf12da8c0a4daf' 'http://192.168.1.4/dvwa/vulnerabilities/brute/?username=admin&password=FUZZ&Login=Login'
```

Now let’s find the correct password

![]()

**Line ‘4’ is different, am i right !**

All of these the response is 200 (OK) , have 86 lines, but the words number for Line 4 is different ! , also the characters are different ! that means that other passwords were wrong because they tell us the same incorrect sentence each time execpt ‘password’ which is the password for user admin

Press enter or click to view image in full size

![]()

**Medium Level**

**Command Execution: Low**

You can find that there is page for pinging that takes ip address as input BUT, do you think it can take the ip address only ?

Press enter or click to view image in full size

![]()

Let's add our commands now

What if you typed the ip address and then ls command ? , let’s find out

Press enter or click to view image in full size

![]()

**127.0.0.1;ls**

simicolon ; is the separator between commands , you can use whatever you want (&&) or (&) or (|)

After pinging, he read the ls command also, so now we can do whatever command we want

Press enter or click to view image in full size

![]()

**127.0.0.1;ls;whoami;uname -a**

after pinging, we can find there's 3 files (help, index.php, source), and the current username (www-data) , and some system information using (uname -a) command.

**Command Execution: Medium**

The concept of command execution is the same, you just type the desired command and then put the malicious command that you want,
the only change is the separator between the commands like
 ( ; ) or (&) or (&&) or ( | ) So, Let's see which of these is working

Press enter or click to view image in full size

![]()

127.0.0.1 & ls

Press enter or click to view image in full size

![]()

127.0.0.1 | uname -a

So, pipe (|) , and (&) separators are the working separators in medium level

**Cross-Site Request Forgery (CSRF): Low**

Press enter or click to view image in full size

![]()

this page for changing password for user admin, so if we tried to change the password to ‘test123’ it will change in the url as it's shown down

Press enter or click to view image in full size

![]()

**URL**: http://192.168.1.4/dvwa/vulnerabilities/csrf/?password\_new=test123&password\_conf=test123&Change=Change#

As you can see the password new and the confirmation of it is in the URL ‘test123’ are now the new password

if we changed the URL to *http://192.168.1.4/dvwa/vulnerabilities/csrf/?password\_new=****Hello****&password\_conf=****Hello****&Change=Change#*

And open this new link, the password will change directly to ‘Hello’

Press enter or click to view image in full size

![]()

if you logged out and tried to login with ‘**test123**’ password, it will give you Login Failed
if you tried ‘**Hello**’ instead, you'll be logged in successfully

so you can use this malicious link with some phishing techniques and so on

**Cross-Site Request Forgery (CSRF): Medium**

first, we need to intercept the GET packet for password changing

Press enter or click to view image in full size

![]()

**Let's intercept this packet**

Press enter...