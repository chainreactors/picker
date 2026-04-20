---
title: 2026渗透测试0基础入门：Kali Linux安装 + 10大必装工具（新手看完就能上手）
url: https://mp.weixin.qq.com/s/Q3VLQ2WS8WrdVLK0LmO6JA
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:53:57.601530
---

# 2026渗透测试0基础入门：Kali Linux安装 + 10大必装工具（新手看完就能上手）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/r3TOKXsosZibbnVBla3HX1q4kmWGT0GjlcT5IiahVx3WEYWZlapRXvfdyKj3icoAtRDDTMzTFnJXjnXb63OGhBtGmmlEqjT2lxnicPzkKO5aV70/0?wx_fmt=jpeg)

# 2026渗透测试0基础入门：Kali Linux安装 + 10大必装工具（新手看完就能上手）

原创

hackerson
hackerson

黑客联盟l

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhqjlIpdACpYtdVvKD3OPyBmYA5brJN4sK34dYRQcSL3uKNsGNoib9fEN3CEGeChjIvOx8qClscs5w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

用心做分享，只为给您最好的学习教程

如果您觉得文章不错，欢迎持续学习

#

![](https://mmbiz.qpic.cn/sz_mmbiz_png/r3TOKXsosZiby1WPX4ict7RIFtwjjQt9Qp0meVrTkRZVIGaatjRgazC6u1msUlQTvNt92Pa6ToCbzwMqHfdBZENTicslsukvctTh4GX1SAbnvs/640?wx_fmt=png)

很多人一听到“渗透测试”，脑子里立刻蹦出几个词：

高深、神秘、门槛高、普通人学不会。

其实真没那么夸张。

你看到的那些会挖漏洞、会抓包、会写脚本的人，也都是从零开始的。
他们迈出的第一步，不是什么高级攻击技巧，而是——**先装系统。**

如果你也想进入网络安全行业，或者对黑客技术充满兴趣，这篇文章就是给你准备的。

今天不讲空话，直接带你从 0 开始入门：

### ✔ Kali Linux 怎么装

### ✔ 新手一定要会的 10 款工具

### ✔ 学习路线怎么走最省时间

看完这篇，你至少知道第一步该怎么走。

---

# 一、为什么大家学渗透测试，都绕不开 Kali Linux？

![https://images.openai.com/static-rsc-4/aqZBytOAvTM_qzpg_0S2Bk6SDz4NUvZUn-A3fPwdwHXiKFsvMqrkEPdvX01u2rlAW3LuN-FfanLgpOkp2pQGHFxLpksjjWGYVBeqfAhKDA9Vw0vIvVNH4Lj00smDPC1L_bmbLLLVOCHiXR9hThfVJejJr-TXgyqeZl88Qo1c2jvjJtuMXoGSA18CWuR9xfiZ?purpose=fullsize](https://mmbiz.qpic.cn/sz_mmbiz_jpg/r3TOKXsosZ9Ib83IX9qxWxic8ibZibqqFyxbIWyM0ibibmkObSQ6tbaDiaib3YiaiaFhuctyiaMk7QhibxniauSfSBonRym3Y3yVUs1ibk9bcyiaS4Jm7jHjE/640?wx_fmt=jpeg&from=appmsg)

![https://images.openai.com/static-rsc-4/dQZDSYCHogOPrTTreMvi6pHUz_MKbl8xpiO5ZD5taXFmusPZ9H9IYByuPYiRPizfutLLpm1kRPwr3pvS07sU_SMMpCSuQ0dQ360vWWO6r_PjuG5CRUqZOl1IxH1BBkmTY9trfmAVx3uZ63QZVnR4qcl5-crJA_4-cHSfVcWcRQIucMdk8Xf0IzoIIf8HLkXg?purpose=fullsize](https://mmbiz.qpic.cn/sz_mmbiz_jpg/r3TOKXsosZ9N4yuhRDq0vficnxdvUMamMnAclNIq8pQqqQJdrtaUWNH50VcotiafMFfyACLO7ZQICgBIde6ia5oibSpF6qdMhM2ibLkYlAL6mLy8/640?wx_fmt=jpeg&from=appmsg)

Kali Linux 是目前最主流的安全测试系统之一。

它最大的特点就一句话：

> 别人装系统是为了办公，你装 Kali 是为了学习安全技术。

系统里自带大量工具，覆盖：

* 信息收集
* 漏洞扫描
* Web安全测试
* 密码审计
* 无线测试
* 内网渗透
* 数字取证

对于新手来说，最大的好处就是：**省事。**

不用到处找环境，不用折腾兼容问题，装好就能学。

---

# 二、Kali Linux 安装教程（新手建议收藏）

![https://images.openai.com/static-rsc-4/CWC-NAJYUoB2A1572e2VsHKfCCGgvBFeMHrxZDRY_E9G62jSqJWdLraniQigi91tdxDomwe8ekavukHnihFzPcj8DCcpuDufFXFYV-aIvFs8iI4T9UhU_xehzm46vLrZ6_P5Wrk7B7Qj5gQn2N3ZuL8tivtqCrZMCAwsO8hFVLN490PUQuTqZfRX3CWC3DnA?purpose=fullsize](https://mmbiz.qpic.cn/mmbiz_jpg/r3TOKXsosZibouvGnJJsT0fXH3Mgv8CQctLzAfBdicTXBFWbROhiaQI6vF8Uv3k0yZ32oXf1O3mmF3FBu5m5V5G3XdFQic08HOflVpTjaHibdkAs/640?wx_fmt=jpeg&from=appmsg)

## 推荐方式：虚拟机安装

如果你是第一次接触，建议用虚拟机安装，最稳妥。

不会影响你电脑原本系统，出问题删掉重来就行。

---

## 第一步：准备工具

你需要：

* 一台电脑（8G内存以上更舒服）
* VMware Workstation

  或 VirtualBox
* Kali 镜像文件

---

## 第二步：创建虚拟机

建议配置：

* 内存：4GB+
* CPU：2核+
* 硬盘：50GB+

---

## 第三步：开始安装

启动后按提示操作：

* 选择 Graphical Install
* 选择语言
* 设置用户名密码
* 自动分区
* 等待安装完成

---

## 第四步：先更新系统

安装好后第一件事，不是炫技，而是更新系统。

```
sudo apt update && sudo apt upgrade -y
```

很多工具打不开、报错、闪退，往往就是因为没更新。

---

# 三、10大必装工具推荐（每个新手都用得上）

---

# 1、Nmap —— 信息收集第一神器

![https://images.openai.com/static-rsc-4/5JqfrK8VhYR0wJk7mPs3S7LHN3B-xeMmkEgh7LNgvIFwajIiuxjZvQZ_HhmSQ1pxI9qSaRLJwOXlq0ukVk4mlo-wRW1i3hsfZJJOemBeKe79Art7SKRjs7eYE4oHDyUMRqHXPu35mjILaX8qrrR-4cTHqSl7euSj0xxpCpD7urMluCwvYX2xzBjvLcisI8eq?purpose=fullsize](https://mmbiz.qpic.cn/sz_mmbiz_jpg/r3TOKXsosZ92V5GeSKQNfOmVBQtF8wibZDAraUYTiaj4sIb9QzKqPnE6PklLU0npgJLjBSMWZHicO2qbKvDYq0hGic8LWib8WaYnrWBteowtSrlA/640?wx_fmt=jpeg&from=appmsg)

![https://images.openai.com/static-rsc-4/slcq6YJIQjunFXhGUKru0umB_NlgHbWdYhXbLyMezOxOvxvI2pVMG24ORW2veXkpBjsQowBKeHRZfqi1SgJrQeiywc8H2YdT84XYRcWlf2W34_paiuIHTX1DlZI0VhvOBecvLo3GwCFpnsrkzrRL-ZsPUZa216vu8i3y-gUWJyg979NgxZBvZZ5TrGKJ39xH?purpose=fullsize](https://mmbiz.qpic.cn/mmbiz_jpg/r3TOKXsosZichTGFdxJfKT4JzHGRafPoOqN00cCSPYAkMP6r6ogNa6qn1yulkhTZxr5N7WeXibEhbb1jBM5LU85DoELPbxPxy4DSEY0Bz7LUs/640?wx_fmt=jpeg&from=appmsg)

![https://images.openai.com/static-rsc-4/Sx3vICriKGP1ZPX28LbvPMO04hbiuUjvOSaiYJ7lDzmgm3NZpCEvuBiSV5rcLKLKp4MVeqtzZfP9ZY_--VJI9P0xei0R4JyND5J-XPuMqdyZ7FzA2bSi-xpuKrCgO3ERrzj5ZEfOFQaqXmPtxGaYAm5G_s3Pz91rLS1925gsN1Sc4Xssgi9wznAH5bImvhp5?purpose=fullsize](https://mmbiz.qpic.cn/sz_mmbiz_jpg/r3TOKXsosZ8LiaYZJWRhAjL1fY2mic0FkCcOeB3iaGjWiaS1JzgrG6MoHZLxGnR0bU7Obb09fjTeUZBuTFRsYnLjFaP2tA0qbykZawR0qRJDhoA/640?wx_fmt=jpeg&from=appmsg)

Nmap 是学渗透最先接触的工具之一。

它能帮你做什么：

* 扫描端口
* 发现在线主机
* 识别服务版本
* 判断操作系统

简单理解：
你要打仗，先得知道对面城门在哪。

示例：

```
nmap -sV192.168.1.1
```

---

# 2、Burp Suite —— Web安全核心工具

![https://images.openai.com/static-rsc-4/vk5NSNSapJpQ9t-isWOkvNjBURHnfbC7r6wVlX82rXncjvZOcD03f1Lkvw15IsC91PSKEXUNe7p5Rm5IM-LMp-DyIT9Bq88EaxlZ80xZnpZMR8kjB81_st5ZI6xNHOS44mUlw_Nd_roHxj9OQdiotKeVbwgen4nTfDaugy-TNRNHH0qEkSWACx6OKtHhjv57?purpose=fullsize](https://mmbiz.qpic.cn/sz_mmbiz_jpg/r3TOKXsosZibzickGvPEkVtahCnvK6JTn8aiaTDBXibicVqbpVv1RxOcQZBwy93NbFGB7ucoLkJ0f4oPkicgZEvUVSdAwC5PeOhUHHtgZKz3UkssQ/640?wx_fmt=jpeg&from=appmsg)

![https://images.openai.com/static-rsc-4/oSqQTPqy0DYxjpcxDg3oNk9ZfTigtn-H7JiMQmY7n5cfzjSkHG8Y0P0B7J9s0xBpKdN_TfqcGJFGjKiD0bDyc9KpnYj7LqLq7lm8NRlxp-G20M5CCKdBj0l_E9VuEsQ93kGKNTXNSu6G8lexhZpEz0-vIRuY_CgUrLK30jCc-L8S9LCa60xjBeaazsdkA2OU?purpose=fullsize](https://mmbiz.qpic.cn/sz_mmbiz_jpg/r3TOKXsosZ8WRtJrH9rtdDPUiafVQTn2S9tn5purp8DYj4xAndBXQTAbU6Ay58GJpJoickWWdemlxeYWd8k42axwgUzwKcCbh1kLa5xLIVJF0/640?wx_fmt=jpeg&from=appmsg)

![https://images.openai.com/static-rsc-4/FiFWbsZIhvYUC8Pm2o5zXAH7v1OTrwZ-ga8UpHUwMvKugGg3jemJSIHjlHP81TgoDLhHjHFrjolCYAhgkB8ZV1D_RtDXCYQmhZxz9_w4Wj_D1RC-8YJTILbtBUePohjSyEaHmamxAAkO2x2G2pzJPQl9IIBLFCpDl3bBXnXWVJt853yEYdB8WAThwGYrp1hs?purpose=fullsize](https://mmbiz.qpic.cn/sz_mmbiz_jpg/r3TOKXsosZicLCwNXNxItQ30nn2jmmoqPnl9JkPqEEibHguBHJ66j1QticfBsMYZRoLBVhsaQlhthMWC55uNPwwtHdHWc8icImNKnW3XiakxRAZk/640?wx_fmt=jpeg&from=appmsg)

Burp Suite 几乎是 Web 安全圈的标配。

常见用途：

* 抓包
* 改请求参数
* 重放数据包
* 漏洞测试

如果你想学 SQL 注入、越权、XSS，这工具绕不过去。

---

# 3、Metasploit —— 漏洞利用框架

![https://images.openai.com/static-rsc-4/UyGevXvL1NG6nfWE6KsyZuAKJzbiBfbkoH2PZJUm4dq-96YEv4sqEF-VMDqNil2XZUA8olet5-UiBjRdPVC5EynShx1GnRwFpSnhka9fa2uzq6ucviC9ysm6bO7phplg6Ud2bgO-FIr2OyBETpG0FO_H6FCOquz57Bdy0uddIfsDfk8k-CRdbBuUDEznjMZK?purpose=fullsize](https://mmbiz.qpic.cn/mmbiz_jpg/r3TOKXsosZ8KJwRmVib2Wcp09eLpRJgFjZJSSmIvXTgWiaBBpaia1afsjatlJ2dibFngyticATucEYnuZOiaNiaBHge1I8xRSq2icFgOicoicYuwpoqhA/640?wx_fmt=jpeg&from=appmsg)

![https://images.openai.com/static-rsc-4/QoPDqxTWXll5uxlKpCNAOEKWBoinjjyCcEUTPcpTh-fLJlB5vZ7uI1hp0J1TMAe8Jx_BqTpNYAgAQiU-VlCrH0HyykABfDOrHz3SFIxQMP57r-wPBy51zSef9D-gvhScjwvMyf5pL8yTiKmWr93Bz7-qrNMsoL-Arlggm5-jhMG4-ylnLmXocNWHNk1qcuSo?purpose=fullsize](https://mmbiz.qpic.cn/sz_mmbiz_jpg/r3TOKXsosZ9bnKOrB27FJwMnxwKIH4XxjhIXSqJBeYiayibWibicichA6SJs85LogQJNxCRYcEiazGBNSBUaCiaFlhXKtibbg1M3ngoIBeahN9baaJ0/640?wx_fmt=jpeg&from=appmsg)

![https://images.openai.com/static-rsc-4/k4MFJKZJA5FsIhc0xKdwR81OexJJhngoXkjyAg3vIwBb94k4APPXolEDZElgvY2wu4ro8UbUeazfwBYfjmTsNQszNnj3MhQDU_90FUSlrKfuwK-rssI9m_jbI8Y2hap_WUjlGtPHqZ2796FbDPdhD9e2Wvdmwb7eQo5_jv-3CoW3uilDSVuNJUSOSpLpZS_R?purpose=fullsize](https://mmbiz.qpic.cn/mmbiz_jpg/r3TOKXsosZ8bYdTRWEjKhAwGaw3t53Ot3a3CAXI3BZm5JicOicuMs7B60XtlKPxYwER3QGUlQAWWHjymYjxhMDFz6NmUCKUjllhqsYw2u9ulI/640?wx_fmt=jpeg&from=appmsg)

Metasploit 是经典中的经典。

它适合学习：

* 漏洞利用流程
* Payload 使用方式
* 后渗透操作
* 安全测试思路

新手别把它当“一键入侵工具”，真正价值是学习攻击逻辑。

---

# 4、Wireshark —— 抓包分析天花板

![https://images.openai.com/static-rsc-4/EewJe2CrJObmBNB0gVIfXY8w3-fd5mDu5oh9d16fGgVw4L_XXgeGpXV2RC4yi6e4d0WiytI8o5Ha-cp8PaBoUOohEkA8daw99ax6eLTsk-7kwRLw0EifqJD0tY9EDRfNpkgOqaphAtTL2zVkZvnQAwvLU3uY7ygBe1EvCF-0lsugG7bgI8uZaNgGHEeIz5vS?purpose=fullsize](https://mmbiz.qpic.cn/sz_mmbiz_jpg/r3TOKXsosZibwIeU2cqYfZ3icOpesTFmZr3y3QMY4DcKfLNT05BoXZTRl0CVQxhDdLia2X6zA0iajujELtTCVQT9hDL944DiaqYVdIegZYyVZaO8/640?wx_fmt=jpeg&from=appmsg)

![https://images.openai.com/static-rsc-4/6_23CrGS7I85Gx5HLEtpzHoe64KwxpthVrCnGrA3GX3R_Ilq3AHNXYrNIU0sc8Q0IPLtKIuyOX632dzmm7WdOEY6TYqJ7tBocrRGzj56gUlsTzRFgJmnDkPpPMOQKAeUtBMfAplaiTSX1-wNgr3Xrweqpz0L4R5pEfU9mjP84Y3jgvnj6N1WJ6kG6RBSsEIN?purpose=fullsize](https://mmbiz.qpic.cn/sz_mmbiz_jpg/r3TOKXsosZ9KGvuJzRb...