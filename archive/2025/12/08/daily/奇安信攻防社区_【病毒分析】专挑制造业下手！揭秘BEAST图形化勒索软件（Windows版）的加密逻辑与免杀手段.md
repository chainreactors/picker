---
title: 【病毒分析】专挑制造业下手！揭秘BEAST图形化勒索软件（Windows版）的加密逻辑与免杀手段
url: https://forum.butian.net/share/4666
source: 奇安信攻防社区
date: 2025-12-08
fetch_date: 2025-12-09T03:15:36.240188
---

# 【病毒分析】专挑制造业下手！揭秘BEAST图形化勒索软件（Windows版）的加密逻辑与免杀手段

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 【病毒分析】专挑制造业下手！揭秘BEAST图形化勒索软件（Windows版）的加密逻辑与免杀手段

* [漏洞分析](https://forum.butian.net/topic/48)

Beast Ransomware（别称 Monster）最早于 2022年3月 首次被发现。同年6月，一名代号为 "MNSTR" 的威胁行为者在俄语黑客论坛 "Ramp" 上正式发布了该家族的 勒索软件即服务（RaaS） 推广贴，寻找合作伙伴。

1.背景与家族溯源
---------
### 1.1 BEAST家族前世今生
Beast Ransomware（别称 Monster）最早于 \*\*2022年3月\*\* 首次被发现。同年6月，一名代号为 \*\*"MNSTR"\*\* 的威胁行为者在俄语黑客论坛 "Ramp" 上正式发布了该家族的 \*\*勒索软件即服务\\*\*\*\\*（RaaS）\\*\\* 推广贴，寻找合作伙伴。
作为一个相对\*\*老牌\*\*的 RaaS 组织，Beast 经历了多次技术迭代：
- \*\*初期版本：\*\* 采用 Delphi 语言开发。
- \*\*后期演进：\*\* 核心模块转为 C 语言和 Go 语言开发，以提升运行效率和跨平台能力。
- \*\*跨平台支持：\*\* 目前已覆盖 Windows、Linux、ESXi 甚至 NAS 系统。
\*\*值得一提的是\*\*，该组织在 2024 年 6 月的一则招聘贴中，为了招募更多的\*\*盟友\*\*，竟然使用了 \*\*俄语、英语、中文\*\* 三种语言发布广告。虽然其打着“\*\*诚邀合作、优惠条件\*\*”的旗号，但其本质依然是网络犯罪。
![1.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-5df12d6732d1de53de91aff82cf5088af034d8a4.png)
\*\*图1 Beast中文招聘贴\*\*
初期发布的加密器版本仅只有 Windows 勒索生成器版本，后续推出了一个名为 Beast Ransomware 的增强版本，包括了多个版本的恶意软件生成器如 Windows GUI、Windows CLI、Linux、NAS、ESXI，甚至包括离线勒索软件生成器。
![2.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-50a3190f3338e36b4f7555ddc398892262caea3a.png)
\*\*图2 Beast Builder\*\* \*\*GUI\*\* \*\*界面\*\*
![3.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-a2ab9f1938ae115baf397f54467d43eebe534801.png)
\*\*图3 Beast Offline Builder 界面\*\*
### 1.2 运营模式与攻击偏好
Beast 宣称采用“\*\*完全去中心化\*\*”的合作模式，承诺不干涉合作伙伴的谈判，并提供低利息和动态费用结算。
- \*\*攻击目标：\*\* 截至 2025 年，该组织已攻击了超过 40 家企业。受害者主要集中在 \*\*制造业、医疗保健、建筑\*\* 等实体行业。
- \*\*地缘特征：\*\* 拥有典型的“\*\*俄语系\*\*”勒索软件特征——\*\*严格避开独联体国家\*\*（如俄罗斯、白俄罗斯等）。
![4.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-5a03c5f0613fb538c1e160937e779ad489ac90cc.png)
\*\*图4 受害者行业统计图\*\*
![5.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-8a1cd10d0f46e9662805f719d9fa2daab57392db.png)
\*\*图5 Beast 泄露站点界面\*\*
2.攻击手法 (TTPs)
-------------
Beast 家族采用常见的勒索软件策略，形成了一套成熟的攻击链：
1. \*\*初始入侵：\*\* 广泛利用 \*\*钓鱼邮件\*\* 投递恶意载荷，暴力破解 RDP 口令，以及利用已知系统漏洞获取立足点。
2. \*\*双重勒索：\*\* 采用“\*\*窃取数据 + 加密文件\*\*”的组合拳。在初步入侵后，攻击者会在网络内进行侦察。
3. \*\*横向移动：\*\* 泄露凭证或通过暴力破解密码进行横向移动，利用有效账户进一步入侵其他服务器以及应用，随后进行加密。
3.样本基础信息
--------
我们捕获并分析了 BEAST 针对 Windows 平台的加密器样本，其基本画像如下：
### 3.1 恶意文件基础信息
| \*\*文件名\*\* | `encrypter-windows-x86.exe` |
|---|---|
| \*\*大小\*\* | 1.13 MB |
| \*\*操作系统\*\* | Windows |
| \*\*架构\*\* | x86-64 (32位模式) |
| \*\*编译语言\*\* | C/C++ |
| \*\*MD5\*\* | `3b5950325efd4aa6865a776daed6a515` |
| \*\*SHA1\*\* | `8762c334f461ca8e058ff2ccedd8468801111f8b` |
| \*\*SHA256\*\* | `97de86078c7dedda1791ce2f3b7f2d3907b46bcbe4722c43cb6889dff12533f6` |
### 3.2 感染症状
一旦遭受感染，系统中的文件将被加密并追加特定后缀。
- \*\*加密后缀示例：\*\* `.{620E6797-67ED-8F7A-8533-7CE58E9D2FC6}.BEASET`
- \*\*勒索信文件名：\*\* `readme.txt`
> \*\*勒索信内容摘要：\*\* "YOUR FILES ARE ENCRYPTED... You are not able to decrypt it by yourself!... We have been in your network for a long time..." 攻击者极具挑衅地宣称已在网络中潜伏已久，并威胁若不联系将公开数据。
YOUR FILES ARE ENCRYPTED
​
Your files, documents, photos, databases and other important files are encrypted.
​
You are not able to decrypt it by yourself! The only method of recovering files is to purchase an unique private key.
Only we can give you this key and only we can recover your files.
​
To be sure we have the decryptor and it works you can send an email: edatax@airmail.cc and decrypt one file for free.
But this file should be of not valuable!
​
​
Do you really want to restore your files?
Write to email: edatax@airmail.cc
​
YOUR PERSONAL ID: 896F70DF-1E6B-FF95-8533-7CE58E9D2FC6
​
Attention!
\\* Do not rename encrypted files.
\\* Do not try to decrypt your data using third party software, it may cause permanent data loss.
\\* Decryption of your files with the help of third parties may cause increased price (they add their fee to our) or you can become a victim of a scam.
\\* We have been in your network for a long time. We know everything about your company most of your information has already been downloaded to our server. We recommend you to do not waste your time if you dont wont we start 2nd part.
\\* You have 24 hours to contact us.
\\* Otherwise, your data will be sold or made public.
### 3.3 加密测试
我们使用一个名为 `sierting.txt` 的文件进行加密测试。
![6.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-a55770779518e856a914c170fdce3fea37465825.png)
\*\*图6 sierting.txt 原始内容\*\*
![7.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-6f86ee72084b090dc56f04c44675f21848c840d2.png)
\*\*图7 原始文件的十六进制视图\*\*
经过加密后，文件内容变得不可读，且头部结构发生了明显变化。
![8.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-eddd4de396c7f004b5d0264fc6c627f9fa93c715.png)
\*\*图8 加密后文件的十六进制视图\*\*
4.逆向分析：拆解加密流程
-------------
通过对样本的深入逆向分析，我们还原了 BEAST 在 Windows 环境下的完整执行逻辑。其行为模式严谨且具有针对性。
### 4.1 程序执行流程图
在正式加密前，样本会执行一系列环境检查和系统破坏操作：
![9.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-50c89b00e47f7b0fad5aa05bd6a290df87d77f1e.png)
\*\*图9 程序执行流程图\*\*
### 4.2 详细行为分析
#### 4.2.1 地区白名单检查 (Region Check)
程序运行伊始，首先通过 `GetLocaleInfoW` 获取受害主机的系统语言信息。随后，它会对解密出的白名单国家代码进行比对。
![10.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-6e5c3a52b5e2c803df7d7ca5d5e3bb1d63370e13.png)
\*\*图10 GetLocaleInfoW 代码视图\*\*
进行对资源解密操作，解密出字符串：
![11.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-16a0dedab0ffeea4287eefe5ba98b23bb7af10b7.png)
\*\*图11 字符串解密代码视图\*\*
- \*\*关键逻辑：\*\* 如果受害主机属于以下列表中的国家/地区，\*\*病毒将直接退出，不执行加密\*\*。
- \*\*白名单列表（CIS国家为主）：\*\*
- `AM` (亚美尼亚), `AZ` (阿塞拜疆), `BY` (白俄罗斯)
- `CY` (塞浦路斯), `GE` (格鲁吉亚), `KZ` (哈萨克斯坦)
- `KG` (吉尔吉斯斯坦), `MD` (摩尔多瓦), `RU` (俄罗斯)
- `TJ` (塔吉克斯坦), `TM` (土库曼斯坦), `UA` (乌克兰)
- `UZ` (乌兹别克斯坦), `VN` (越南)
![12.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-aabd9ed713719fc258fa05e252f64749b9fa2295.png)
\*\*图12 地区判断循环代码视图\*\*
#### 4.2.2 权限维持 (Persistence)
为了确保系统重启后仍能继续运行，BEAST 会修改注册表。
- \*\*操作：\*\* 将自身路径添加到 `SOFTWARE\Microsoft\Windows\CurrentVersion\Run`。
- \*\*目的：\*\* 实现开机自启动，确保持久化驻留。
![13.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-fddf5776ecc2b071dfeecd085c4be362a368e35d.png)
\*\*图13 RegSetValueExW 写入注册表代码视图\*\*
#### 4.2.3 初始化窗口控件
样本中包含了一段逻辑——初始化通用控件 (`InitCommonControls`) 并创建一个窗口类名为 `!UU` 的隐形窗口。
![14.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-2ee185969a28cd42e071fc0fcf690b48d5211780.png)
\*\*图14 InitCommonControls 代码视图\*\*
创建窗体后，程序注册了全局热键并设置了定时器，这可能是为了处理某些特定的交互或反调试逻辑。
![15.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-147f55db64582373233e1cdfe8e9f3ffa319d693.png)
![16.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-8ce11fd8bc156703515126b371b54dfed8b13a2f.png)
\*\*图15 CreateWindowExW 和 RegisterHotKey 代码视图\*\*
#### 4.2.4 清空回收站 (Anti-Forensics)
为了阻碍受害者恢复数据，样本调用 `SHEmptyRecycleBinW` 函数，强制清空回收站。
- \*\*目的：\*\* 彻底删除用户可能临时存放的文件，增加数据恢复难度。
![17.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-1a631c3c6a00615d2176f7611f7478b2b724c56c.png)
\*\*图16 SHEmptyRecycleBinW 代码视图\*\*
#### 4.2.5 终止指定进程
为了解除文件占用，确保能顺利加密关键文件（如数据库、备份服务），BEAST 会遍历系统进程快照。
- \*\*获取版本号与权限判断：\*\* 首先获取系统版本，并检查当前用户权限。
![18.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-f43e4ea34c37cbe3527851ece6aaa21a5e354f5f.png)
\*\*图17 GetVersionExW 代码视图\*\*
![19.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-e3f2802edb1e1e8a776e8e7ebdecbf18069283fb.png)
\*\*图18 CheckTokenMembership 代码视图\*...