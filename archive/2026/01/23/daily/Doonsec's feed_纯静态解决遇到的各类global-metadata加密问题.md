---
title: 纯静态解决遇到的各类global-metadata加密问题
url: https://mp.weixin.qq.com/s/FKJiDmOYIetzkITMfk7ssg
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:28:36.680000
---

# 纯静态解决遇到的各类global-metadata加密问题

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HtVTxHNORrvxXgR3U5RGeG8CY5lYDJBmQmflsv1XUexDqjjgEANxgbhic2ZY0PS3oc7MtJSy7m0bQ/0?wx_fmt=jpeg)

# 纯静态解决遇到的各类global-metadata加密问题

rettozero
rettozero

看雪学苑

![]()

在小说阅读器中沉浸阅读

# 在通过Il2cppdumper工具尝试dump unity游戏的sdk时，经常会碰到一些加密的global-metadata.dat，导致无法成功dump。

#

搜索网上的文章或工具个人感觉最好用两种分别是。

1.动态dump解密后的metadata。

2.利用il2cpp\_api（未混淆）动态dump CS文件。

本文总共4个例子，有能用以上办法解决的，也有不能用以上方法解决的，全都是纯静态解决，按照从易到难的顺序。

##

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HtVTxHNORrvxXgR3U5RGeG3POkLSl7BfrJsAe1sRETrxCToMYmpSCU7s4htK84c8WvO9WU9kZwIg/640?wx_fmt=png&from=appmsg)

找不到解密逻辑，观察规律编写解密脚本

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HtVTxHNORrvxXgR3U5RGeG3POkLSl7BfrJsAe1sRETrxCToMYmpSCU7s4htK84c8WvO9WU9kZwIg/640?wx_fmt=png&from=appmsg)

既然要解密，肯定要先了解加密的位置在哪里。

通过github能下载到2020年的unity源码，找到MetadataCache.cpp中的il2cpp::vm::MetadataCache::Initialize函数，而这里也是大多数metadata解密的位置。

因考虑篇幅问题，一部分的代码都只会截取一部分。

```
bool il2cpp::vm::MetadataCache::Initialize()
{
    s_GlobalMetadata = vm::MetadataLoader::LoadMetadataFile("global-metadata.dat");
if (!s_GlobalMetadata)
return false;

    s_GlobalMetadataHeader = (const Il2CppGlobalMetadataHeader*)s_GlobalMetadata;
IL2CPP_ASSERT(s_GlobalMetadataHeader->sanity == 0xFAB11BAF);
IL2CPP_ASSERT(s_GlobalMetadataHeader->version == 24);
```

```
void* il2cpp::vm::MetadataLoader::LoadMetadataFile(const char* fileName)
{
    std::string resourcesDirectory = utils::PathUtils::Combine(utils::Runtime::GetDataDir(), utils::StringView<char>("Metadata"));

    std::string resourceFilePath = utils::PathUtils::Combine(resourcesDirectory, utils::StringView<char>(fileName, strlen(fileName)));
```

观看源码可以知道，我们可以利用global-metadata.dat或Metadata字符串去索引到具体的函数实现。而大多数的加密操作一般都在这两个函数。

让我们正式开始第一个案例吧！

先通过Metadata字符串索引到LoadMetadataFile函数。

```
__int64 __fastcall sub_35FC404(
  sub_361107C(&a11);
  a9 = "Metadata";
  a10 = 8;
  v19 = a11 >> 1;
if ( (a11 & 1) != 0 )
    v20 = a13;
else
    v20 = &a11 + 1;
if ( (a11 & 1) != 0 )
    v19 = a12;
  a17 = v20;
  a18 = v19;
  sub_35A26B0(&a14, &a17, &a9);
if ( (a11 & 1) != 0 )
operator delete(a13);
  v21 = strlen(a1);
if ( (a14 & 1) != 0 )
    v22 = a16;
else
    v22 = &a14 + 1;
if ( (a14 & 1) != 0 )
    v23 = a15;
else
    v23 = a14 >> 1;
  a9 = a1;
  a10 = v21;
  a17 = v22;
  a18 = v23;
  sub_35A26B0(&a11, &a17, &a9);
  LODWORD(a17) = 0;
  v24 = sub_35B18B0(&a11, 3, 1, 1, 0, &a17);
if ( a17 )
  {
if ( (a11 & 1) != 0 )
      v25 = a13;
else
      v25 = &a11 + 1;
    sub_35B31F4("ERROR: Could not open %s", v25);
  }
else
  {
    v26 = v24;
    v27 = sub_35B3380();
    sub_35B1AF0(v26, &a17);
if ( !a17 )
goto LABEL_22;
    sub_35B3390(v27);
  }
  v27 = 0;
LABEL_22:
if ( (a11 & 1) != 0 )
operator delete(a13);
if ( (a14 & 1) != 0 )
operator delete(a16);
return v27;
}
```

如果是十分熟悉这两个函数的师傅，一眼就可以知道这个函数里没有进行解密操作，接着索引到Initialize函数。

```
bool __fastcall sub_35D25D8(_DWORD *a1, int *a2)
  v4 = (sub_35FC404)("global-metadata.dat");
  v5 = v4;
  unk_873B968 = v4;
if ( v4 )
  {
    unk_873B970 = v4;
    v6 = *(v4 + 172);
    *a1 = v6 / 0x28;
    unk_873B978 = v6 / 0x28;
    *a2 = *(v4 + 180) >> 6;
    unk_873B980 = (sub_35B3354)((v6 / 0x28), 24);
    unk_873B988 = (sub_35B3354)(*(unk_873B960 + 48LL), 8);
    unk_873B990 = (sub_35B3354)(*(unk_873B970 + 164LL) / 0x58uLL, 8);
    unk_873B950 = (sub_35B3354)(*(unk_873B970 + 52LL) / 0x24uLL, 8);
}
```

if ( v4 )后的伪代码已经是将metadata的结构头和一些值填入到内存中了，按理说应该在sub\_35FC404读取metadata后进行解密操作。

既然没找到，那就查看一下metadata的数据。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HtVTxHNORrvxXgR3U5RGeGHjoqUWWOVCzd7pRJgDwNZOSRHVz5MzCTWD2KIZL7BkJBzeoU8P15qQ/640?wx_fmt=other&from=appmsg)![]()

如果有观察了解过metadata结构头，或是对数字比较敏感的师傅，一眼就能看出来，这个metadata的加密十分规律。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HtVTxHNORrvxXgR3U5RGeGGTOu1oH0IexFkhWtpicm5ztBqgXjfUjW7sZz5MFEUYhiaxOp795z7yfg/640?wx_fmt=other&from=appmsg)![]()

拿一个正常的结构头，会更加直观，因为metadata存储的多是各个参数的偏移和数量，因此很少有数据大于0xffffff（小端序）

因此通过观察03 07 0b 0f等偏移，可以观察出一定的加减规律。

再细致可以观察出这个规律是呈16一轮，这是我们在观察0x100这个偏移，这里存储的是关于windows相关的数据，apk是用不到的，因此多是不变的。

因此我们只需要提取0x100的十六个字节，并且对偏移0x8的数据异或0x1，即可得到一个异或表。

```
def decrypt_metadata(encrypted_file_path, output_file_path):
with open(encrypted_file_path, 'rb') as f:
        encrypted_data = f.read()

# 初始化密钥表
    key_table = [0x70,0x2c,0xe8,0xa4,0x60,0x1c,0xd8,0x94,0x51,0x0c,0xc8,0x84,0x40,0xfc,0xb8,0x74]
    key_table[8] ^=0x1
    decrypted_data = bytearray()

for i in range(len(encrypted_data)):
# 使用当前密钥表位置进行异或
        key_index = i % 16
        temp = encrypted_data[i] ^ key_table[key_index]

# 重要：将解密后的数据写回密钥表
        key_table[key_index] = (key_table[key_index] - 0x40) & 0xFF

        decrypted_data.append(temp)

with open(output_file_path, 'wb') as f:
        f.write(decrypted_data)

# 使用示例
decrypt_metadata('global-metadata.dat', 'global-metadata-decrypted.dat')
```

随便找一个ai写一个脚本即可
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HtVTxHNORrvxXgR3U5RGeG1fDLERWPJuXia31N3ibcRON8CHtXFdw56C49CZia71G04fbwASknsTfcQ/640?wx_fmt=other&from=appmsg)![]()

可以看到我们得到了一个很干净的metadata，只需要把头部修复一下即可。

##

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HtVTxHNORrvxXgR3U5RGeG3POkLSl7BfrJsAe1sRETrxCToMYmpSCU7s4htK84c8WvO9WU9kZwIg/640?wx_fmt=png&from=appmsg)

metadata改名且加密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HtVTxHNORrvxXgR3U5RGeG3POkLSl7BfrJsAe1sRETrxCToMYmpSCU7s4htK84c8WvO9WU9kZwIg/640?wx_fmt=png&from=appmsg)

第二个案例，我在so中无法搜索到metadata相关的字符串,查看assets资源文件，发现文件路径名和文件名都被修改成无意义命名。

但好在LoadMetadataFile函数中还有一个ERROR: Could not open %s 字符串

```
__int64 __fastcall sub_12C6E34(constchar *a1){
sub_12E2F9C(v14);
  v12 = "gloxinia";
  v13 = 8;
  v2 = LOBYTE(v14[0]) >> 1;
if ( (v14[0] & 1) != 0 )
    v3 = v15;
else
    v3 = v14 + 1;
if ( (v14[0] & 1) != 0 )
    v2 = v14[1];
  v18 = v3;
  v19 = v2;
sub_122C950(v16, &v18, &v12);
if ( (v14[0] & 1) != 0 )
operator delete(v15);
  v4 = strlen(a1);
if ( (v16[0] & 1) != 0 )
    v5 = v17;
else
    v5 = v16 + 1;
if ( (v16[0] & 1) != 0 )
    v6 = v16[1];
else
    v6 = LOBYTE(v16[0]) >> 1;
  v12 = a1;
  v13 = v4;
  v18 = v5;
  v19 = v6;
sub_122C950(v14, &v18, &v12);
LODWORD(v18) = 0;
  v7 = sub_12E1F00(v14, 3, 1, 1, 0, &v18);
if ( v18 )
  {
if ( (v14[0] & 1) != 0 )
      v8 = v15;
else
      v8 = v14 + 1;
sub_12F631C("ERROR: Could not open %s", v8);
  }
else
  {
    v9 = v7;
    v10 = sub_12F64F4();
sub_12E2140(v9, &v18);
if ( !v18 )
goto LABEL_22;
sub_12F6504(v10);
  }
  v10 = 0;
LABEL_22:
if ( (v14[0] & 1) != 0 )
operator delete(v15);
if ( (v16[0] & 1) != 0 )
operator delete(v17);
return v10;
}
```

找到函数后，发现路径名字被改为gloxinia，再向上索引，发现解密函数操作。

```
__int64 __fastcall sub_12C6D60(constchar *a1){
  result = sub_12C6E34(a1);
if ( result )
  {
    v2 = result;
    v3 = sub_12F64A0();
    v4 = sub_12F647C(1, v3);
    v7 = v4;
if ( v4 )
    {
memcpy(v4, v2, v3);
      v8 = &v7;
      *(sub_1277C3C(&qword_2CE6568, &v7, &unk_A414F3, &v8, &v6) + 40) = v2;
LODWORD(v8) = 0;
      v5 = 0;
      v6 = 0;
sub_12C6FDC(v7, 256, &v8, &v6, &v5);
sub_12C6FDC(v7, (v7[63] + v7[62]), &v8, &v6, &v5);
return v7;
    }
else
    {
sub_12F631C("ERROR: Could not malloc %ld", v3);
return 0;
    }
  }
return result;
}
```

我们再向上索引，成功找到我们的Initialize函数，我的metadata名字叫做feast\_plaint\_knight。

```
bool __fastcall sub_12645CC(_DWORD *a1, int *a2){
  v4 = sub_12C6D60("feast_plaint_knight");
  v5 = v4;
  qword_2CE58C0 = v4;
if ( v4 )
  {
    qword_2CE58C8 = v4;
    v6 = *(v4 + 172);
    *a1 = v6 / 0x28;
    dword_2CE58D0 = v6 / 0x28;
    *a2 = *(v4 + 180) >> 6;
    qword_2CE58D8 = sub_12F647C((v6 / 0x28), 24);
    qword_2CE58E0 = sub_12F647C(*(qword_2CE58B8 + 48), 8);
    qword_2CE58E8 = sub_12F647C(*(qword_2CE58C8 + 164) / 0x58uLL, 8);
    qword_2CE58A8 = sub_12F647C(*(qword_2CE58C8 + 52) / 0x24uLL, 8);
    v7 = sub_12F647C(*(qword_2CE58B8 + 64), 8);
}
```

拉进010查看，这个metadata初看大概也是一个循环异或的规律。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HtVTxHNORrvxXgR3U5RGeG5J87G0loJMdXE3IbFmZP7qtiaDmtGoxKiaSyONJvX64icxxjXPbEd15Jg/640?wx_fmt=other&from=appmsg)![]()

但老是写解密脚本显然不是我这种懒狗的思路。这里当然要使用出我们的顶级解密工具Unidbg！

动态dump的原理除...