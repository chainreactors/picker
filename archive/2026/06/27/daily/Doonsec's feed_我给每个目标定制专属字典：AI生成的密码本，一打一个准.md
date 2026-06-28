---
title: 我给每个目标定制专属字典：AI生成的密码本，一打一个准
url: https://mp.weixin.qq.com/s/8pLF_Jj4MsUHuIitH6g0GQ
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:11:16.533338
---

# 我给每个目标定制专属字典：AI生成的密码本，一打一个准

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3oR6eMARh6yrr1pmkJiczJ5Dt59TviaONpA0URQAPkwcBAOO3JoTiaEZQ2j8Wmt2ibmD29f0zDicbryVXVHZ2gna4jia6ApSMS7ho8maRgnndGD24/0?wx_fmt=jpeg)

# 我给每个目标定制专属字典：AI生成的密码本，一打一个准

原创

逍遥
逍遥

昆仑AI安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

我入行头几年，爆破后台全凭一个300万行的“超级字典”。跑一次大半天，运气好能撞出几个弱口令，运气不好毛都没有。后来我慢慢发现一个问题：那些被我撞出来的密码，往往和目标的域名、业务、人名高度相关——比如域名`xiaoxiang`的口令是`Xiaoxiang@2024`，或者HR邮箱密码是公司名加123。通用的字典根本不会覆盖这些组合，因为它是给所有人用的。

去年我开始用AI给每个目标单独生成字典。不是让AI去猜密码，而是把目标的域名、业务关键词、员工信息全扔给AI，让它把这些元素排列组合成可能的密码变体。命中率直接翻了三倍以上。以前打一个目标平均撞出2-3个弱口令，现在经常能撞出七八个，甚至一次直接撞出了管理员后台的密码。

这篇文章把整个方法拆开，从信息收集到AI Prompt设计，到脚本自动化，全给你。

**一、传统字典为什么命中率低？**

通用密码字典，不管是Rockyou还是国内的Top1000，都是基于历史泄露数据库统计出来的高频密码。它只覆盖了`admin123`、`password`、`123456`这种“普适弱口令”。

但现实中的企业员工和管理员，他们的密码大多和这家公司有关联。我统计过自己过去两年爆破成功的200多个口令，超过60%包含以下元素之一：

* 公司域名：如`hongxing` → `Hongxing@2024`
* 业务缩写：如`OA`、`ERP`、`CRM`
* 产品名：如`clouddesk`、`smartpark`
* 员工姓名/工号：如`zhangsan123`、`wangli_2023`
* 默认密码变体：如`admin` → `Admin123`、`adm123`

通用字典里没有这些，因为它是“通用”的。但AI可以快速生成这些定制化的组合，这就是命中率提升的根源。

**二、我的做法：信息收集→喂给AI→生成字典**

流程很简单，分三步走。

**第一步：收集目标的“基因信息”**

不需要入侵，全部来自公开渠道：

* **域名和子域名**：从主域名里提取品牌名。比如`www.redstar-logistics.com`，关键词就是`redstar`、`logistics`。
* **业务系统名**：从网页title、footer、登录页面抓取。比如“红星空运物流管理系统”、“RedStar ERP”。
* **公司名和缩写**：天眼查、企查查直接看，比如“红星空运物流有限公司”，缩写可能是`RSL`、`HXKY`。
* **员工姓名**：脉脉、LinkedIn搜公司名，找几个公开的员工姓名。不需要多，三五个就够。
* **技术特征**：网站框架（如Tomcat、WebLogic）、编程语言（Java、PHP），这些也会影响默认密码。

我每次测试前花15分钟整理一份“目标档案”，大概长这样：

```
目标名称：红星空运域名：redstar-logistics.com缩写：RSL, redstar产品名：RedStar ERP, 星云物流平台员工姓名：张伟, 李娜, 王强技术栈：Java, Tomcat, MySQL年份：2024, 2025
```

这份档案就是AI的“原料”。

**第二步：用AI生成密码变体**

我把这些原料扔给AI，让它基于常见的人类设定密码习惯，生成密码候选词。

我的Prompt如下（经过多次优化）：

```
你是一个密码破解专家，擅长根据目标信息推断可能的密码。现在有一个目标，信息如下：域名：redstar-logistics.com品牌名：RedStar, 红星空运缩写：RSL, redstar, hxky产品名：RedStar ERP, 星云物流平台员工姓名：张伟, 李娜, 王强常见年份：2024, 2025, 2026常见特殊字符：@, #, !, ., _
请根据以上信息，结合以下常见的人类设定密码习惯，生成100个可能的密码候选：1. 品牌名+年份/特殊字符/数字（如RedStar@2024, RedStar2025, redstar123）2. 缩写+年份/特殊字符/数字（如RSL@2024, rsl2025）3. 产品名+年份/特殊字符/数字（如RedStarERP@2024）4. 员工姓名+特殊字符/数字（如zhangwei@123, zhangwei2025, ZhangWei!2024）5. 常见默认密码变体（如admin123, Admin@123, password, P@ssw0rd）6. 结合技术栈（如tomcat, weblogic1, manager）7. 大小写变体、首字母大写、全大写8. 键盘序列变体（如qwer, asdf）
要求：- 不要生成通用弱口令（如123456, password），这些我会另外加。- 密码长度限制在6-16位。- 直接输出密码列表，一行一个，不要序号，不要解释。
```

AI输出的密码列表长这样：

```
RedStar@2024RedStar2025redstar123RSL@2024rsl2025RedStarERP@2024zhangwei@123ZhangWei!2024lina2025wangqiang_2024admin123Admin@123tomcatmanagerredstar!@#hxky2024hxky@123StarLogistics2024...
```

这100条密码，加上我自己的基础弱口令字典（如`admin`, `123456`, `password`, `111111`），再结合目标默认密码（如`admin/admin`, `root/root`），就构成了一份高度定制化的爆破字典。

**第三步：用脚本自动化生成**

我把这个过程写成了Python脚本，输入目标档案，自动调用AI API生成字典：

```
import requests
def generate_custom_dict(target_info):    prompt = f"""    你是一个密码破解专家...（上面的Prompt）    目标信息：    {target_info}    """    resp = requests.post(        "https://api.deepseek.com/v1/chat/completions",        headers={"Authorization": "Bearer sk-xxx"},        json={            "model": "deepseek-chat",            "messages": [{"role": "user", "content": prompt}],            "temperature": 0.8  # 提高随机性，生成更多样        },        timeout=120    )    output = resp.json()["choices"][0]["message"]["content"]    passwords = [line.strip() for line in output.split('\n') if line.strip()]    # 去重，并去除可能混入的通用弱口令    return list(set(passwords))
# 示例：生成100条+基础字典custom = generate_custom_dict(target_info)with open('custom_dict.txt', 'w') as f:    for pwd in custom + basic_passwords:        f.write(pwd + '\n')
```

跑一次成本几分钱，几秒钟出结果。

**三、实战案例：AI字典连下三城**

**案例1：撞出某物流公司SSH密码**

目标是一家物流公司，域名`speed-cargo.cn`。我用AI生成了200条定制密码，加上100条基础弱口令，对它们的一台暴露SSH的服务器做爆破。不到十分钟，用户`root`的密码被撞出：`SpeedCargo@2024`。

这个密码就是品牌名`SpeedCargo`加年份加特殊字符的组合。通用字典里根本没有`SpeedCargo`这个词。我拿到密码后登进去，发现这台服务器连接着他们的内部物流系统，订单数据一览无余。高危漏洞，赏金4000元。

**案例2：撞出某政务系统后台管理员**

目标是一个智慧社区管理系统，域名`zhsq.bjxxx.gov.cn`，缩写`zhsq`（智慧社区）。AI生成的字典里有`zhsq@2024`、`zhsq123`、`Zhsq2025`等变体。最终撞出管理员密码就是`zhsq2024`，直接进入后台，能看到辖区内所有居民信息。严重漏洞，赏金8000元。

**案例3：撞出某企业VPN密码**

目标是一家制造企业，域名`jinshan-machinery.com`。我从脉脉上扒了几个员工的姓名，AI字典里包含了`jinshan@2025`、`Jinshan123`、`zhangwei@jinshan`等。最后撞出VPN账号`zhangwei`的密码是`Jinshan@2024`，直接连入内网。高危漏洞，赏金6000元。

**四、AI字典 vs 通用字典，命中率到底差多少？**

我统计了最近50次授权测试的数据：

* **通用字典**（300万条）：平均命中率约5%（50个目标中，成功爆破弱口令的只有2-3个）。
* **AI定制字典**（200条+基础弱口令）：平均命中率约18%（50个目标中，成功爆破弱口令的有9个）。

命中率提升了3倍多。而且AI字典体积小（几百条），爆破速度快，十分钟就能跑完，不像通用字典动辄跑半天。更重要的是，AI生成的密码更贴近目标，撞出的往往是高权限账号的关键密码，危害更大。

**五、不止字典，AI还能帮你判断“谁可能用了弱口令”**

进阶用法：把目标员工的信息也扔给AI，让它判断哪些人可能用了弱口令，再重点爆破。比如AI会提示：“此人入职不满半年，可能还在用初始密码”、“此人岗位是行政，密码可能是公司名加123”、“此人英文名加生日可能性大”。

然后你就有了一个优先级排序的爆破目标列表，效率再次提升。

**六、防御建议：怎么防这种定制化字典攻击？**

这种攻击的核心不是破解加密算法，而是利用了人类设定密码的习惯。防御也不复杂：

1. **强制密码复杂度**：要求至少8位，包含大小写、数字、特殊字符，且不能包含公司名、用户名等。
2. **定期弱口令自查**：用公司域名、品牌名、员工信息生成字典，内部爆破一次，把弱口令揪出来。
3. **多因素认证**：就算密码被撞，还有第二层保护。
4. **登录失败策略**：连续5次失败锁定账号或延迟响应，别让攻击者无限爆破。

**七、写在最后**

AI生成定制字典这事，技术含量不高，成本极低，但效果拔群。它本质上不是AI有多聪明，而是它帮你做了“信息收集→组合排列”的体力活，让你能快速覆盖人类设定密码的所有可能性。

下次打目标，别急着上几十G的超级字典。先花十分钟做个目标档案，丢给AI，生成一份几百条的专属字典。你会惊喜地发现，那个管理员，又在用公司的缩写当密码。而你，就是他这个习惯的收割者。

**严正声明**
本文所述技术仅用于合法授权的安全测试。任何未经授权的爆破、入侵行为均属违法。所有案例均已脱敏，仅保留技术原理供学习参考。安全之路，始于授权。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6zxPsSBiaTT0QiaBjibScxViciathof2tlahJCticqia6DncZNe4Fiatd1zWxPQKdTAqnyRPFWmxviaJJm5R8JLbEAURJnZRMiaKa1quLS8k/0?wx_fmt=png)

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