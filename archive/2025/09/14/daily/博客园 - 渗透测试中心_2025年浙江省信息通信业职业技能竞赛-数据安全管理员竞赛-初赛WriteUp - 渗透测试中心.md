---
title: 2025年浙江省信息通信业职业技能竞赛-数据安全管理员竞赛-初赛WriteUp - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/19089841
source: 博客园 - 渗透测试中心
date: 2025-09-14
fetch_date: 2025-10-02T20:09:07.043914
---

# 2025年浙江省信息通信业职业技能竞赛-数据安全管理员竞赛-初赛WriteUp - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [2025年浙江省信息通信业职业技能竞赛-数据安全管理员竞赛-初赛WriteUp](https://www.cnblogs.com/backlion/p/19089841 "发布于 2025-09-13 23:12")

数据传输-网恋需谨慎：

你是一个管理员，在一个名为orwell.freenode.net的服务器上结识了用户RiotCard85，RiotCard85主动联系了你，询问近况并提到他最近在做一个项目想让你看看。项目中隐藏了一些有趣的信息和内容，不幸的是黑客截获了你们的的网恋聊天记录，请分析找出RiotCard85留下的有趣的信息，帮助他尽快消除这些隐私泄露，SSH账号密码为ctf/123456，flag为flag{md5(题目中获取的有效flag信息)}，md5默认为32位小写。

首先是Web端的提示告诉了密码和压缩包名称

![image.png](https://img2024.cnblogs.com/blog/1049983/202509/1049983-20250913231237057-387331412.png)

![image.png](https://img2024.cnblogs.com/blog/1049983/202509/1049983-20250913231238315-987188320.png)

ssh连接下载第一个包，进行分析

![image.png](https://img2024.cnblogs.com/blog/1049983/202509/1049983-20250913231239026-1180904992.png)

因为给的提示是.7z最后搜文件头

![图片](https://img2024.cnblogs.com/blog/1049983/202509/1049983-20250913231239824-232864934.png)

![图片](https://img2024.cnblogs.com/blog/1049983/202509/1049983-20250913231240635-119606799.png)

输入密码：MarioRulez1985

得到一个flag.nes文件

解法1：

strings 直接一把嗦哈

![image.png](https://img2024.cnblogs.com/blog/1049983/202509/1049983-20250913231241381-1977992160.png)

解法2：

放入16进制编辑器，找到关键信息。

![图片](https://img2024.cnblogs.com/blog/1049983/202509/1049983-20250913231242212-1411637213.png)

解法3：

拖到nes模拟器，得到flag

![图片](https://img2024.cnblogs.com/blog/1049983/202509/1049983-20250913231242895-2062894357.png)

Flag：NESted\_in\_a\_PCAP

![图片](https://img2024.cnblogs.com/blog/1049983/202509/1049983-20250913231243490-48269250.png)

```
flag{993f09e2be95e2a3073b819f2ef24585}
```

勒索病毒数据恢复场景：

通过初步排查，发现存在大量SSH登录日志，请筛查SSH日志，找出境外攻击者的IP。SSH登录信息：ctf/123456 提交格式为flag{md5(ip)}

ps：ssh登不了没提供服务，只能web访问

直接登入在log路径下发现日志

笨办法一个一个试，或者搜归属更好判断

![ea6a44c74c9d83787cc66b89f8d4b851.png](https://img2024.cnblogs.com/blog/1049983/202509/1049983-20250913231244251-1944017868.png)

38.180.105.69个是黑客ip md5加密一下

![图片](https://img2024.cnblogs.com/blog/1049983/202509/1049983-20250913231244868-161263459.png)

```
flag{17be68c6011ca57cbe87b3256e65702f}
```

数据加密解密-损坏的签名也不能泄露：

题目描述：在计算机飞速发展的情况下，数据安全变得尤为重要，我们采用更为安全的非对称加密对数据进行处理，这使得对于私钥的管理变得更为严格，意外泄露私钥签名，会带来巨大的数据安全隐患。

first blood

这题一血，吐槽一下设计的不合理这么难才50分！

题目给出完整的私钥文件，可以直接读取文件，得到`n,e,d`。然后找一个网上已知`n,e,d`分解`n`的模板进行分解即可得到：

```
p = 101847683421654680716375842695034943233474607295920357073189009241656737716914371690243711460398867127651266347312129924919977661218999208063330343536013922323662312399299474655370999029196885945932836549374793299266781427165928628878598475537865329482879199651690967937724199458455481792004282475605823232563
```

```
q = 163210729062940435641851566626943305331251877830909198443806240864198682758985962110875675836580622882438335913592229471847355588617787116228491327914590616301603257385538591488022620864955374260532671790453204386239739135973102414175524438716221979798897211790763739046103381955260186638088754228604073920479
```

![图片](https://img2024.cnblogs.com/blog/1049983/202509/1049983-20250913231245788-1339880847.png)

得到w：

取出$\omega*{0,0},\omega*{1,1}$这样的元素，在模$p$下开5次方即可得到$seeds\_i$然后爆破即可恢复seed

```
from hashlib import md5
```

```
import json
```

```
import gmpy2
```

```

```

```
def obscure_calculation(p, enc, x, y, z):
```

```
    # Initialize structures with meaningless names
```

```
    Omega = [[0]*100 for _ in range(100)]
```

```
    Theta = [0]*100
```

```

```

```
    for j_prime in range(100):
```

```
        # ---- Phase 1: Obfuscated Sj calculation ----
```

```
        temp_list = [gmpy2.mpz(v) for v in x[j_prime]]
```

```
        sigma = sum(temp_list)
```

```
        delta = gmpy2.mpz(enc[j_prime]) - sigma
```

```
        Theta[j_prime] = int(delta % p) if p else 0
```

```

```

```
        # ---- Phase 2: Confusing counting ----
```

```
        occurrence_matrix = [[0]*10 for _ in ' '*10]
```

```
        for pair in zip(y[j_prime], z[j_prime]):
```

```
            occurrence_matrix[pair[0]][pair[1]] += 1
```

```

```

```
        # ---- Phase 3: Nonlinear column filling ----
```

```
        position_counter = 0
```

```
        for first_dim in range(10):
```

```
            for second_dim in range(10):
```

```
                Omega[j_prime][position_counter] = int(
```

```
                    occurrence_matrix[first_dim][second_dim]
```

```
                )
```

```
                position_counter += 1
```

```
                if position_counter >= 100:
```

```
                    break
```

```
            if position_counter >= 100:
```

```
                break
```

```

```

```
    return Omega, Theta
```

```

```

```
p = 101847683421654680716375842695034943233474607295920357073189009241656737716914371690243711460398867127651266347312129924919977661218999208063330343536013922323662312399299474655370999029196885945932836549374793299266781427165928628878598475537865329482879199651690967937724199458455481792004282475605823232563
```

```
q = 163210729062940435641851566626943305331251877830909198443806240864198682758985962110875675836580622882438335913592229471847355588617787116228491327914590616301603257385538591488022620864955374260532671790453204386239739135973102414175524438716221979798897211790763739046103381955260186638088754228604073920479
```

```

```

```
f = open('out.json','rb').read()
```

```
data = json.loads(f)
```

```
x = data['x']
```

```
y = data['y']
```

```
z = data['z']
```

```
enc = data['enc']
```

```

```

```
A_matrix = matrix(Zmod(p),A)
```

```
S_vector = vector(Zmod(p),S)
```

```
W = A_matrix.solve_right(S_vector)
```

```

```

```
seeds = []
```

```
for i in range(10):
```

```
    R.<x> = PolynomialRing(Zmod(p))
```

```
    f = x^5 - W[10*i + i]
```

```
    seeds.append(int(f.roots()[0][0]))
```

```

```

```
recover_seed = []
```

```
hex_table = b"0123456789abfedf"
```

```
low_table = [i for i in range(1000)]
```

```

```

```
def get_seed(c):
```

```
    for low in low_table:
```

```
        for f in hex_table:
```

```
            i = c - f + low
```

```
            if (i % 1000) == low:
```

```
                recover_seed.append(chr(f))
```

```
                return
```

```

```

```
for i in range(10):
```

```
    get_seed(seeds[i])
```

```
seed = ''.join(recover_seed)...