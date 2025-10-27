---
title: Test Authentication from Linux Console using python3 pexpect
url: https://thepcn3rd.blogspot.com/2023/01/test-authentication-from-linux-console.html
source: thepcn3rd - Passion for Infosec
date: 2023-01-23
fetch_date: 2025-10-04T04:36:33.419885
---

# Test Authentication from Linux Console using python3 pexpect

# [thepcn3rd - Passion for Infosec](https://thepcn3rd.blogspot.com/)

Twitter: @lokut
This blog is for educational purposes only. The opinions expressed in this blog are my own and do not reflect the views of my employers.

## Sunday, January 22, 2023

### Test Authentication from Linux Console using python3 pexpect

Working with the IT420 lab, you will discover that we need to discover a vulnerable user account.  The following python3 script uses the pexpect library to auth with a defined username and password.  This can be used to discover an account.

```
#!/usr/bin/python3

# Found the script at https://stackoverflow.com/questions/5286321/pam-authentication-in-python-without-root-privileges and then modified
import pexpect
def authPam(username, password):
        result = 0
        try:
                child = pexpect.spawn('/bin/su - %s'%(username))
                child.expect('Password:')
                child.sendline(password)
                result=child.expect(['su: Authentication failure',username])
                child.close()
        except Exception as err:
                child.close()
                print ("Error authenticating. Reason: "%(username))
                return True
        if result == 0:
                print ("Authentication failed for user %s."%(username))
                return True
        else:
                print ("Authentication succeeded for user %s."%(username))
                return True

if __name__ == '__main__':
        authPam(username='root',password='root')
        #authPam(username='kali',password='kali') - If the user does not exist the script implodes...
```

at
[January 22, 2023](https://thepcn3rd.blogspot.com/2023/01/test-authentication-from-linux-console.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=450247628992736477&postID=5099954288454744377&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=450247628992736477&postID=5099954288454744377&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=450247628992736477&postID=5099954288454744377&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=450247628992736477&postID=5099954288454744377&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=450247628992736477&postID=5099954288454744377&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=450247628992736477&postID=5099954288454744377&target=pinterest "Share to Pinterest")

#### No comments:

#### Post a Comment

[Older Post](https://thepcn3rd.blogspot.com/2023/01/setup-crontab-for-www-data.html "Older Post")
[Home](https://thepcn3rd.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://thepcn3rd.blogspot.com/feeds/5099954288454744377/comments/default)

### [Test Authentication from Linux Console using python3 pexpect](https://thepcn3rd.blogspot.com/2023/01/test-authentication-from-linux-console.html)

Working with the IT420 lab, you will discover that we need to discover a vulnerable user account.  The following python3 script uses the pex...

* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYibk9C-SKPTd_Dxp0JFHv9abAT_RTwNOMLheOB5Bw0O5fRzu_kWE-JSDpDn4gnP49i74gKT6UiOyUHPjFdntq335wsNs8M9B_NFms1725AYh2k7B2I3-sTsMxtqh45Uq0hiz24m8W8wI/w72-h72-p-k-no-nu/Selection_016.png)](https://thepcn3rd.blogspot.com/2015/04/owasp-broken-web-apps-getboo-walkthrough.html)

  [OWASP Broken Web Apps - GetBoo Walkthrough](https://thepcn3rd.blogspot.com/2015/04/owasp-broken-web-apps-getboo-walkthrough.html)

  Here is a quick walk through of GetBoo.  The first item that I found was you can harvest the usernames of the existing users that are regist...
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgo8fg35w1-49ORqz0aLkEnSJvZZhEGpot4h552dq_D0KLtpKLs5AO_tthgUHnKoPV8G36Z840qPox06iz6jvFKum-Cvk4kcSiCJ9tdO9ZMSeHEmt5FcrV_sTK_wITnit5bm9aXKFkL4Aw/w72-h72-p-k-no-nu/Selection_025.png)](https://thepcn3rd.blogspot.com/2015/04/07-of-ip-addresses-continue-to-be.html)

  [0.7% or 311,026 IP Addresses found continue to be vulnerable to Heartbleed](https://thepcn3rd.blogspot.com/2015/04/07-of-ip-addresses-continue-to-be.html)

  As I was glancing through the logs of my honeypots I spent some time to look at the following logs.  In the past I have just overlooked them...
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhPqelQvMM6tetp3p0adCVe70liwYlI96lXKnVTJBicB9MawstZDwbvYBSAmURF3PBqgNG2Wa3BiGhiKnC0UGcHR1W93TzCdeaEBXqIWL1PvsQZu5noB-Q_NL-SQzoEM0xOAXZl4nPbgo/w72-h72-p-k-no-nu/Selection_006.png)](https://thepcn3rd.blogspot.com/2015/04/owasp-broken-web-apps-broken-wordpress.html)

  [OWASP Broken Web Apps - Broken Wordpress Walkthrough](https://thepcn3rd.blogspot.com/2015/04/owasp-broken-web-apps-broken-wordpress.html)

  I thought I would work through a few of these web applications provided by OWASP on their broken web applications VM. The first one I th...
* [What's in the honeypot? Frequency of SSH Login Attempts based on Country of Origin](https://thepcn3rd.blogspot.com/2015/04/whats-in-honeypot-frequency-of-ssh.html)

  Today looking at the logs of the honeypots, I became curious based on the whois of the IP Addresses attempting to login to SSH which country...
* [Using masscan with a configuration file](https://thepcn3rd.blogspot.com/2015/11/using-masscan-with-configuration-file.html)

  Recently I was doing some scanning with a tool that is available on github called masscan.  The tool allows you to configure a configuration...

## Search This Blog

|  |  |
| --- | --- |
|  |  |

## Blog Archive

* ▼
  [2023](https://thepcn3rd.blogspot.com/2023/)
  (3)
  + ▼
    [January](https://thepcn3rd.blogspot.com/2023/01/)
    (3)
    - [Test Authentication from Linux Console using pytho...](https://thepcn3rd.blogspot.com/2023/01/test-authentication-from-linux-console.html)
    - [Setup crontab for www-data](https://thepcn3rd.blogspot.com/2023/01/setup-crontab-for-www-data.html)
    - [Brute Force: Password Spray - Gather Names](https://thepcn3rd.blogspot.com/2023/01/brute-force-password-spray-gather-names.html)

* ►
  [2021](https://thepcn3rd.blogspot.com/2021/)
  (9)
  + ►
    [November](https://thepcn3rd.blogspot.com/2021/11/)
    (6)
  + ►
    [October](https://thepcn3rd.blogspot.com/2021/10/)
    (3)

* ►
  [2020](https://thepcn3rd.blogspot.com/2020/)
  (6)
  + ►
    [July](https://thepcn3rd.blogspot.com/2020/07/)
    (2)
  + ►
    [May](https://thepcn3rd.blogspot.com/2020/05/)
    (3)
  + ►
    [April](https://thepcn3rd.blogspot.com/2020/04/)
    (1)

* ►
  [2019](https://thepcn3rd.blogspot.com/2019/)
  (5)
  + ►
    [September](https://thepcn3rd.blogspot.com/2019/09/)
    (1)
  + ►
    [March](https://thepcn3rd.blogspot.com/2019/03/)
    (3)
  + ►
    [January](https://thepcn3rd.blogspot.com/2019/01/)
    (1)

* ►
  [2018](https://thepcn3rd.blogspot.com/2018/)
  (12)
  + ►
    [December](https://thepcn3rd.blogspot.com/2018/12/)
    (3)
  + ►
    [November](https://thepcn3rd.blogspot.com/2018/11/)
    (3)
  + ►
    [October](https://thepcn3rd.blogspot.com/2018/10/)
    (1)
  + ►
    [September](https://thepcn3rd.blogspot.com/2018/09/)
    (1)
  + ►
    [May](https://thepcn3rd.blogspot.com/2018/05/)
    (1)
  + ►
    [April](https://thepcn3rd.blogspot.com/2018/04/)
    (1)
  + ►
    [February](https://thepcn3rd.blogspot.com/2018/02/)
    (2)

* ►
  [2017](https://thepcn3rd.blogspot.com/2017/)
  (16)
  + ►
    [December](https://thepcn3rd.blogspot.com/2017/12/)
    (2)
  + ►
    [November](https://thepcn3rd.blogspot.com/2017/11/)
    (8)
  + ►
    [October](https://thepcn3rd.blogspot.com/2017/10/)
    (3)
  + ►
    [August](https://thepcn3rd.blogspot.com/2017/08/)
    (2)
  + ►
    [February](https://thepcn3rd.blogspot.com/2017/02/)
    (1)

* ►
  [2016](https://thepcn3rd.blogspot.com/2016/)
  (18)
  + ►
    [November](https:...