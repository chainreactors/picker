---
title: 第二届数据安全大赛“数信杯”数据安全大赛 WP - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/18314066
source: 博客园 - 渗透测试中心
date: 2024-07-21
fetch_date: 2025-10-06T17:41:21.033858
---

# 第二届数据安全大赛“数信杯”数据安全大赛 WP - 渗透测试中心

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

# [第二届数据安全大赛“数信杯”数据安全大赛 WP](https://www.cnblogs.com/backlion/p/18314066 "发布于 2024-07-21 02:05")

### 1.**pyc**

使用pyc在线反编译得到python源码：

```
 #!/usr/bin/env python
 # visit https://tool.lu/pyc/ for more information
 # Version: Python 3.8

 import random

 def encrypt_file(file_path):
     random.seed(114514)

 # WARNING: Decompyle incomplete

 file_path = "./flag"
 encrypt_file(file_path)
```

然后使用AI分析可得到它对应的解密脚本

```
 import random
 import os

 def decrypt_data(encrypted_data):
     random.seed(114514)
     decrypted_data = bytearray()
     for byte in encrypted_data:
         key = random.randint(0, 128)
         decrypted_data.append(byte ^ key)
     return decrypted_data
 def read_file(file_path, mode='rb'):
     with open(file_path, mode) as file:
         return file.read()
 def write_file(file_path, data, mode='wb'):
     with open(file_path, mode) as file:
         file.write(data)
 def decrypt_file(encrypted_file_path, output_file_path):
     encrypted_data = read_file(encrypted_file_path)
     decrypted_data = decrypt_data(encrypted_data)
     write_file(output_file_path, decrypted_data)
 if __name__=='__main__':
     encrypted_file_path = 'flag.enc'
     output_file_path = 'flag_decrypted.txt'
     decrypt_file(encrypted_file_path, output_file_path)
     #flag{U_R_g00d_at_do1n_pyc}
```

### 2.**MWatch**

提示：数据安全研究员在分析智能设备实时采集的数据时，检测到有一台设备使用者曾出现过某数值过高的情况，请你协助分析该数值最高是多少。flag{md5(数据采集设备名称*数据接收设备名称*数值)}

多次出现Heart Rate，结合题目描述应该就是找这个，只查看Heart Rate相关

![image-20240428205017240](https://img2023.cnblogs.com/blog/1049983/202407/1049983-20240721020506163-391095009.png)

![image-20240428205017240](https://img2023.cnblogs.com/blog/1049983/202407/1049983-20240721020507067-1206138483.png)

flag{md5(Mi Smart Band 5\_Redmi K40\_128)}

flag{453d8feda5adb6e7b4d54f71a9ce9e14}

### 3.**BabyRSA**

提示：某员工有一个生成素数的初始值，这个算法他跑了很长时间。程序不小心终端，还不小心删了了初始值，还能恢复明文吗

源码：

```
 #task.py
 #!/usr/bin/env python3
 # -*- coding: utf-8 -*-

 from secret import flag,init
 from Crypto.Util.number import *
 from sage.all import *
 from gmpy2 import iroot
 m = bytes_to_long(flag.encode())
 r = getPrime(128)

 p = init
 # for i in range(r-1):
 #     p += next_prime(init)

 # assert iroot(p,3)[1] == 1
 q = getPrime(12)
 # N = p*q*r
 N = r**4*q
 e = getPrime(17)
 c = pow(m,e,N)
 print(f"r = {r}")
 print(f"e = {e}")
 print(f"c = {c}")

 # r = 287040188443069778047400125757341514899
 # e = 96001
 # c = 7385580281056276781497978538020227181009675544528771975750499295104237912389096731847571930273208146186326124578668216163319969575131936068848815308298035625
```

爆破12比特的素数得到q，然后解密即可

```
 from Crypto.Util.number import long_to_bytes, inverse

 r = 287040188443069778047400125757341514899
 e = 96001
 c = 7385580281056276781497978538020227181009675544528771975750499295104237912389096731847571930273208146186326124578668216163319969575131936068848815308298035625

 # Assuming the modulus for the exponentiation should indeed be r**4
 n = r**4

 # Compute the modular inverse of e mod φ(n), where φ(n) could be a function of r, like (r-1)*(r**3)
 # We need the correct value of φ(n) for the RSA decryption formula m = c^d mod n, where d = e^(-1) mod φ(n)
 # Here, assuming φ(n) = r^4 - r^3 as a simplification, you might need to adjust this based on actual RSA setup
 phi_n = r**4 - r**3
 d = inverse(e, phi_n)

 # Decrypt message
 m = pow(c, d, n)

 # Convert number to bytes
 message = long_to_bytes(m)
 print(message)
 #flag{3b0ce326141ea4f6b5bf2f37efbd1b42}
```

### 4.**Backpack**

背包加密，用BKZ算法可以求解到一组基

```
 #!/usr/bin/env python3
 # -*- coding: utf-8 -*-

 from sage.all import *
 from secret import flag
 from Crypto.Util.number import *
 from math import log2

 class Knapsack:
     def __init__(self,n,m):
         self.M = []
         self.n = n
         self.m = self.pre(m)
         self.A = 0
         self.B = 0
     def pre(self,m):
         tmp_m = bin(m)[2:]
         t = []
         for tmp in tmp_m:
             t.append(int(tmp))
         return t
     def get_M(self):
         seq = [randint(2**34,2**35) for _ in range(self.n)]
         self.M = seq
     def calc_density(self):
         t = log2(max(self.M))
         d = self.n/t
         print(d)

     def enc(self):
         self.get_M()
         self.calc_density()
         C = 0
         for t in range(len(self.m)):
             C += self.m[t] * self.M[t]
         print(f"C = {C}")
         print(f"M = {self.M}")
 if __name__=="__main__":
     m = bytes_to_long(flag.encode())
     n = m.bit_length()
     k = Knapsack(n,m)
     k.enc()

 # C = 231282844744
 # M = [27811518167, 19889199464, 19122558731, 19966624823, 25670001067, 30690729665, 23936341812, 31011714749, 30524482330, 21737374993, 17530717152, 19140841231, 33846825616, 17334386491, 28867755886, 29354544582, 21758322019, 27261411361, 31465376167, 26145493792, 27075307455, 33514052206, 25397635665, 21970496142, 30801229475, 22405695620, 18486900933, 27071880304, 17919853256, 18072328152, 21108080920]
```

sagemath中执行：

```
from Crypto.Util.number import long_to_bytes

 C = 231282844744
 M = [27811518167, 19889199464, 19122558731, 19966624823, 25670001067, 30690729665,
      23936341812, 31011714749, 30524482330, 21737374993, 17530717152, 19140841231,
      33846825616, 17334386491, 28867755886, 29354544582, 21758322019, 27261411361,
      31465376167, 26145493792, 27075307455, 33514052206, 25397635665, 21970496142,
      30801229475, 22405695620, 18486900933, 27071880304, 17919853256, 18072328152,
      21108080920]

 L = block_matrix([[1, matrix(ZZ, M).T], [0, C]]).LLL()

 for row in L:
     if row[-1] == 0 and len(set(row[:-1])) == 1:
         # Assuming all elements in the row, except the last one, are the same
         ans = [abs(i) for i in row[:-1]]
         ans = int(''.join(map(str, ans)), 2)
         print(long_to_bytes(ans))
```

### 5.**定向数据采集**

```

```

```
import openpyxl
 import requests
 import time
 from urllib.parse import urlencode
 burp0_url = "http://121.40.65.125:23328/submit"

 def separate_name_and_id(input_file, output_file):
     wb = openpyxl.load_workbook(input_file)
     ws = wb.active

     for row in ws.iter_rows(m...