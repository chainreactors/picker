---
title: Blue Water CTF 2024 re OORM wp 模拟执行爆破+剪枝
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458580027&idx=1&sn=3a019b5ef2ad366a5aa8003889756c90&chksm=b18dc4b186fa4da77db1f7c4d3b6155282bead7f8fd480cffbcdf1f9903594f2d13c022b0948&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-11-03
fetch_date: 2025-10-06T19:15:44.577587
---

# Blue Water CTF 2024 re OORM wp 模拟执行爆破+剪枝

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HagHlk4zibwq7tOTETbicdgjs4kaHoXynFSpZWbHpzXvic2hntIHYQM2urrZfpxZsETMf1zswibuicsPA/0?wx_fmt=jpeg)

# Blue Water CTF 2024 re OORM wp 模拟执行爆破+剪枝

wx\_御史神风

看雪学苑

##

```
一

re OORM
```

如果patch或者插桩之类的方法，代替模拟执行的话，可能速度会更快，不过这题规模还能接受，就用模拟执行跑了，这个方便一点，切个片段出来就能直接执行。

需要注意的是避免用unicorn的单步，指定until会快很多；然后unicorn不知道为什么emu\_start多次后会报一个OS Error什么访问-1指针异常啥的，得隔一定次数重新new一个Uc。

##

```
二

main
```

main：

输入100个hex，然后每一个hex，转int，接着按位拆分，存进QWORD[400]数组unk\_214EE0，unk\_214260中，低位在数组低地址。

接着轮询800个函数，总共需要执行800次。

```
times = 0;
  do
  {
    for ( i = 0LL; i != 400; ++i )
    {
      keyA = keyAs_2135E0[i];
      if ( runA )
      {
        ++times;
        funcs_A_211CA0[i](keyA, input_in_bits_A_214EE0[i]);
        keyAs_2135E0[i] = 0LL;
      }
      keyB = keyBs_212960[i];
      if ( keyB )
      {
        ++times;
        funcs_B_211020[i](keyB, input_in_bits_B_214260[i]);
        keyBs_212960[i] = 0LL;
      }
    }
  }
  while ( times <= 799 );
```

最后需要dword\_212940 == 40

##

```
三

800个函数分析
```

那800个函数的定义：void (\_\_fastcall  \*)(\_\_int64 key, \_\_int64 input\_bit)，keyAs\_2135E0、keyBs\_212960初始化地方sub\_6160，好像是什么PHT里引用了这个函数。

keyAs、keyBs分别初始了20个非0元素，dump出这两个数组。funcs\_A[0](key, input\_bit)大致逻辑，根据keyAs[0]和input\_bit[0]，给keyAs[20]赋值：

```
void funcs_A_0(__int64 key, __int64 input_bit) {
    x = input_bit | (key<< 1);
    y = hashA0(x);
    // 48 89 3D B7 C5                 mov     cs:keyAs_2135E0+0A0h, rdi
    keyAs[20] = y;
}
```

funcs\_A[1](key, input\_bit)大致逻辑，根据keyAs[1]和input\_bit[1]，给keyAs[21]赋值：

```
void funcs_A_1(__int64 key, __int64 input_bit) {
    x = input_bit | (key<< 1);
    y = hashA1(x);
    // 48 89 3D FF BA                 mov     cs:keyAs_2135E0+0A8h, rdi
    keyAs[21] = y;
}
```

funcs\_A[399](key, input\_bit)大致逻辑，根据keyAs[399]和input\_bit[399]，给dwCheck\_212940赋值：

```
void funcs_A_399(__int64 key, __int64 input_bit) {
    x = input_bit | (key<< 1);
    y = hashA399(x);
    if ( y == 21961 || y == 27098 )
        ++dwCheck_212940;
}
```

`fA_0~fA_19`生成`fA_20~fA_39`的key，然后`fA_20~fA_39`生成`fA_40~fA59`的key

直到`fA_380~fA_399`是检验。

整体大概是这么个顺序：

fA\_0 ⇒ fA\_20 … fA\_360，fA\_380校验

fA\_1 ⇒ fA\_21 … fA\_361，fA\_381校验

…

fB\_0 ⇒ fB\_1 … fB\_18，fB\_19校验

fB\_20 ⇒ fB\_21 … fB\_38，fB\_39校验

…

相当于输入是20\*20的值只能为0、1的矩阵

fA系列函数是做列校验

fB系列函数是做行校验

##

```
四

模拟执行爆破+剪枝
```

使用fA\_0、fA\_20、...、fA\_380爆破第一列，有很多结果：

```
[0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1] 32766
[0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1] 32766
[0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1] 32766
[0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1] 32766
[0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1] 32766
[0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1] 32766
[0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1] 32766
[0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0] 3090
...
[1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1] 32766
[1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0] 3090
[1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0] 3090
...
```

模拟执行fA爆破列的脚本（使用fB爆破行的脚本也差不多）：

```
from capstone import *
from unicorn import *
from unicorn.x86_const import *
from elftools.elf.elffile import ELFFile

keyAs = [9644, 31494, 15772, ..., 0, 0, 0, ...]

f = open('main', 'rb')
elff = ELFFile(f)

def rva_to_offset(elff, rva):
    for segment in elff.iter_sections():
        if rva >= segment['p_vaddr'] and rva < segment['p_vaddr'] + segment['p_memsz']:
            return rva - segment['p_vaddr'] + segment['p_offset']
    raise ValueError('RVA not within any segment')

def read_elf_content_by_rva(elff, rva, size):
    for segment in elff.iter_segments():
        # 检查RVA是否在当前段的范围内
        if rva >= segment['p_vaddr'] and rva < segment['p_vaddr'] + segment['p_memsz']:
            foa = rva - segment['p_vaddr']
            content = segment.data()[foa : foa + size]
            return content

# 收集函数的地址

funcs_A = [int.from_bytes(read_elf_content_by_rva(elff, 0x211CA0 + i * 8, 8), 'little') for i in range(400)]

funcs_A.append(0x106430)

endAs = [ 28866, 31618, 34242, ...]
tyAs = [ 39, 39, 39, ..., (35, 32766, 3090), (35, 6485, 4159), (35, 14535, 24449), ...]

def sim2(uc: Uc, i, j, key, input_bit):
    # func arg
    idx = i + j * 20
    uc.reg_write(UC_X86_REG_RDI, key)
    uc.reg_write(UC_X86_REG_RSI, input_bit)
    uc.emu_start(funcs_A[idx], endAs[idx], 0, 0)
    if j != 19:
        return uc.reg_read(tyAs[idx]), 0, 0
    else:
        return uc.reg_read(tyAs[idx][0]), tyAs[idx][1], tyAs[idx][2]

uc = Uc(UC_ARCH_X86, UC_MODE_64)

# code
for segment in elff.iter_segments():
    if segment['p_vaddr'] == 0x6000:
        uc.mem_map(segment['p_vaddr'], segment['p_memsz']//0x1000*0x1000 + 0x1000)
        uc.mem_write(segment['p_vaddr'], segment.data())

# 执行funcA[i + j * 20](key, 0) 和 funcA[i + j * 20](key, 1)
def dfsA(i, j, key) -> bool:
    global path, uc

    if j == 3: # unicron的bug，得隔一定次数重新创建一个Uc
        uc = Uc(UC_ARCH_X86, UC_MODE_64)
        for segment in elff.iter_segments():
            if segment['p_vaddr'] == 0x6000:
                uc.mem_map(segment['p_vaddr'], segment['p_memsz']//0x1000*0x1000 + 0x1000)
                uc.mem_write(segment['p_vaddr'], segment.data())

    if j == 6:
        print(path)

    if j == 19:
        new_key, t0, t1 = sim2(uc, i, j, key, 0)
        if new_key == t0 or new_key == t1:
            print('path', path + [0], new_key)

        new_key, t0, t1 = sim2(uc, i, j, key, 1)
        if new_key == t0 or new_key == t1:
            print('path', path + [1], new_key)
    else:
        new_key, _, _ = sim2(uc, i, j, key, 0)
        path.append(0)
        dfsA(i, j + 1, new_key)
        path.pop()

        new_key, _, _ = sim2(uc, i, j, key, 1)
        path.append(1)
        dfsA(i, j + 1, new_key)
        path.pop()

path = []
dfsA(0, 0, keyAs[0])

f.close()
```

爆破列校验发现有多解，检查列的所有解，如果某一位在该列的所有解中全为0或1可以确认该位为0或1，一次列验证确认结果如下：

```
_, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, 1, 1, _, _, _
_, 1, _, 1, 1, _, _, _, _, _, 1, _, _, 1, _, 1, 1, _, _, _
_, _, _, 1, _, _, 1, 1, _, _, 1, _, _, 0, _, 0, 1, _, _, _
_, _, _, 1, _, 1, _, 1, _, _, 1, _, _, 1, _, 1, 0, _, _, _
_, 1, _, _, 1, 1, _, _, 1, _, 1, _, _, 1, _, 1, 1, _, _, 1
_, _, 1, _, 1, 1, _, _, _, _, 1, _, 1, 0, _, 1, 0, _, _, _
_, _, _, 1, 1, 1, _, _, _, _, 1, _, 1, 1, _, 0, 1, _, _, _
_, 1, _, 1, 1, 1, _, 1, _, _, 1, _, 1, 1, 1, 1, 1, _, 1, _
1, 1, _, 1, 1, 1, 1, 1, _, _, 1, _, _, 1, 1, 1, 1, _, _, 1
_, 1, 1, _, 1, 1, 1, 1, _, _, 1, _, _, 1, 1, 1, 1, _, _, 1
_, 1, 1, _, _, 1, 1, 1, _, 1, _, 1, _, 1, 1, 1, 1, _, _, 1
_, _, 1, 1, _, _, 1, _, _, 1, _, 1, _, 1, _, 1, 1, _, _, 1
_, _, 1, 1, 1, _, 1, _, _, 1, 1, 1, _, 0, _, 0, 1, _, 1, 1
_, 1, 1, 1, 1, _, 1, _, _, 1, _, _, _, 1, _, 1, 0, _, 1, 1
_, 1, 1, 1, 1, _, 1, _, _, 1, _, _, _, 1, _, 1, 1, _, _, 1
1, 1, 1, 1, _, _, _, _, _, _, 1, _, _, 1, _, 1, 1, _, _, 1
_, 1, 1, 1, _, _, _, _, 1, _, 1, _, _, 1, _, 0, 1, _, _, 1
_, 1, 1, _, 1, _, _, 1, 1, _, _, _, _, 1, 1, 1, 1, _, _, 1
_, 1, _, _, 1, _, _, _, _, _, _, _, _, 1, _, 1, 1, _, _, _
_, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, 1, 1, _, _, _
```

然后用这个确认的结果，对爆破做剪枝加速，继续跑一次行验证、一次列验证、一次行验证（每次跑完验证都按前面的思路更新这个确认的结果），就出来完整结果了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Gg00pteL01boyHHAZkxpDPgicYEbic99Tq1lev88UuPADEIvUA4PyumGaibOeY8kMCs9FbEnbouZ58g/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

看雪ID：wx\_御史神风

*https://bbs.kanxue.com/user-home-1000123.htm*

\*本文为看雪论坛优秀文章，由 wx\_御史神风 原创，转载请注明来自看雪社区

# 往期推荐

1、[PWN入门-SROP拜师](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579476&idx=2&sn=4f9adc1e7d61c7357bdc85ba654f24cb&chksm=b18dc29e86fa4b88c483a581131de043b076918cd7c7436a82e9bb56bc37c8f1edf6c87d8350&scene=21#wechat_redirect)

2、[一种apc注入型的Gamarue病毒的变种](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579387&idx=1&sn=9d6fbf25f11b3d99c92c5ac8de0587d5&chksm=b18dc13186fa4827ae7a7bf909e0d2b9490c6df4417c1d7eebc...