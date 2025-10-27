---
title: Galgame汉化中的逆向：动态汉化分析-以AZsystem引擎为例
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458496413&idx=1&sn=04fb33a23d7f577e89ba9d3e316c4824&chksm=b18e9d1786f914017fb4236de7c8e5911c736db390fdb1cb71d1e6c704b473565ddc82eb9159&scene=58&subscene=0#rd
source: 看雪学院
date: 2023-03-06
fetch_date: 2025-10-04T08:45:32.928502
---

# Galgame汉化中的逆向：动态汉化分析-以AZsystem引擎为例

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOSoeia6CibZNoPoSYjAnyZF3JlhX8PJD61GQYuibEhppJwa6zH3c7r7hQMqgmbribEziawOaichGrbskA/0?wx_fmt=jpeg)

# Galgame汉化中的逆向：动态汉化分析-以AZsystem引擎为例

devseed

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOSoeia6CibZNoPoSYjAnyZFvpe6vwhCVcKnldpsiaexVb3JYKGuJwh3zeqq4VG6RPvVicdPsdODCgibg/640?wx_fmt=jpeg)

本文为看雪论坛精华文章

看雪论坛作者ID：devseed

#

本贴代码开源详见我的github: GalgameReverse（*https://github.com/YuriSizuku/GalgameReverse*）, ReverseUtil（*https://github.com/YuriSizuku/ReverseUtil*）。

上篇链接：Galgame汉化中的逆向：动态汉化分析-以MAJIROv3引擎为例（*https://bbs.kanxue.com/thread-268508.htm*）

##

##

```
0

前言
```

上节 Galgame汉化中的逆向（六）：动态汉化分析\_以MAJIROv3引擎为例，我们介绍了动态汉化。动态汉化不用分析封包结构，不用分析opcode，看上去很方便，但是动态汉化解决同步问题会很麻烦，比如说改完文本后backlog文本仍是日文、返回主界面再载入文本没有变动等问题。动态汉化也有可能出现莫名其妙的崩溃bug，且这些bug不容易被调试。

针对动态汉化的上述缺点，本节我们将介绍一种这种半动态汉化的方案。与上节的方法不同，本节不进行文本级替换，而是文件级别的替换。即去hook相关函数，动态将解密后的缓冲区替换为我们汉化后的文件。适合于那种封包与加密特别麻烦或复杂的游戏。

本文将以azsystem为例，来分析：

引擎如何加载游戏脚本，如何定位关键点提取脚本。

引擎如何加载图片，如何解压各通道数据，如何将图片数据送入帧缓存渲染。

汉化如何用inline hook对加载后的内容进行替换。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FZfAJlzgym2qq3cobb79jlkicvLa24Y7icibQKpLiaFgpelBlewY8ZU7yQWqavXBdNteFxSU4WuVe8GQ/640?wx_fmt=jpeg)

##

##

```
一

脚本文件分析与提取
```

###

### **(1) asb文件的分析**

和上节相同，第一步先分析文件，无论静态分析算法还是动态dump缓冲区，先把文件提取出来。

由于方法差不多，这里不再详细展开了。

这个游戏封包为.arc文件，用文件长度哈希值来作为加密密钥，里面有若干个.asb脚本文件。IDA里面直接搜.asb字符串就能找到相关函数了，读取脚本文件函数如下：

```
int __thiscall sub_43112A(_DWORD *this, char *script_name){  char *raw_data; // edi  int v4; // eax  unsigned int v5; // ecx  _DWORD *v7[4]; // [esp+8h] [ebp-34h] BYREF  int v8; // [esp+18h] [ebp-24h] BYREF  unsigned int compressed_size; // [esp+1Ch] [ebp-20h]  unsigned int raw_size; // [esp+20h] [ebp-1Ch]  int v11; // [esp+24h] [ebp-18h]  int (__thiscall **v12)(void *, char); // [esp+28h] [ebp-14h]  char *compressed_data; // [esp+2Ch] [ebp-10h]  int v14; // [esp+38h] [ebp-4h]   v7[0] = off_460A6C;  sub_40BD95(v7);  v14 = 1;  v12 = &off_462CDC;  v11 = 0;  sub_430FC9((int)this);  if ( fopen_40C102(v7, script_name, 0x80000000) != 1 )  {    logprintf_407C41("CScript::Create", byte_4679CC, script_name);    goto LABEL_13;  }  readfile_40C03E(v7, (char *)&v8, 0xC);  if ( v8 == 0x1A425341 ) // asb\x1a  {    compressed_data = (char *)operator new(compressed_size);    raw_data = (char *)operator new(raw_size);    readfile_40C03E(v7, compressed_data, compressed_size);    if ( sub_430F6A(compressed_data, compressed_size, raw_size) )    {      v4 = decompress_40AB65(compressed_data, compressed_size, raw_data, raw_size);// decompress      v5 = raw_size;      if ( v4 == raw_size )      {        this[4] = 0;        this[1] = raw_data;        this[2] = v5;        this[3] = raw_data;        this[5] = raw_data;        v11 = 1;LABEL_10:        if ( compressed_data )          j__free(compressed_data);        goto LABEL_13;      }      logprintf_407C41("CScript::Create", byte_467A38, script_name);    }    else    {      logprintf_407C41("CScript::Create", byte_467A0C, script_name);// error    }    if ( raw_data )      j__free(raw_data);    goto LABEL_10;  }LABEL_13:  v14 = -1;  v12 = &off_462CDC;  v7[0] = off_460A6C;  sub_40BFDD(v7);  return v11;}
```

简单分析后，我们可以得到asb的文件头结构、校验文本函数、解压函数以下结论，具体如下：

```
typedef struct {        s8 magic[4];                        /* "ASB" */        u32 comprlen;        u32 uncomprlen;        u32 unknown;} asb_header_t; typedef struct {        s8 magic[4];                        /* "ASB\x1a" 通过此magic来定位*/        u32 comprlen;        u32 uncomprlen;} asb1a_header_t; // CScript.constructor, 这里不再自己构造了，在游戏调用的时候记录下this指针void *__thiscall sub_43277F(_DWORD *this) // check_validBOOL __stdcall sub_430F6A(char *compressed_data, int compressed_size, int raw_size) // decompresssub_40AB65(char *compressed_data, int compressed_len, char *raw_data, int raw_len) 0043112A    | B8 9EE54500  | mov eax,lamune.45E59E |load_script(char* name) 004311D4    | FF75 E4  | push dword ptr ss:[ebp-1C]  | raw_len004311D7    | 8D4D EC  | lea ecx,dword ptr ss:[ebp-14]004311DA    | 57         | push edi  | raw_data004311DB    | FF75 E0    | push dword ptr ss:[ebp-20] | compressed_len004311DE    | FF75 F0    | push dword ptr ss:[ebp-10] | compressed_data004311E1    | E8 7F99FDFF| call lamune.40AB65| decompress
```

###

### **(2) asb文件的解密与提取**

提取只需要hooksub\_40AB65，frida代码如下：

```
/*        for lamune.exe v1.0        open the game to title, then        frida -l lamune_hook.js -n lamune.exe        next go to the prologue to dump all asbs*/function install_decompress_hook(outdir='./dump'){       // hook decompress function to dump       const addr_decompress = ptr(0x40AB65);       var raw_asbname = "";       var raw_asbdata = ptr(0);       var raw_asbsize = 0;       Interceptor.attach(addr_decompress, {           onEnter: function(args){               raw_asbdata = ptr(args[2]);               raw_asbsize = args[3].toUInt32();               raw_asbname = ptr(this.context.ebp).add(8).                               readPointer().readAnsiString();           },           onLeave: function(retval){               //var asbname = asbname_buf.readAnsiString();               var asbname = raw_asbname;               console.log(asbname,                   ", raw_asbdata addr at", raw_asbdata,                   ", raw_asbsize ", raw_asbsize)               try{                   var fp = new File(outdir+"/"+asbname, 'wb');                   fp.write(raw_asbdata.readByteArray(raw_asbsize));                   fp.close();               }               catch(e)               {                   console.log("file error!", e);               }            }       })} function dump_asbs(names, outdir="./dump"){    const addr_loadscript = ptr(0x43112A);    const load_script = new NativeFunction(addr_loadscript,         'void', ['pointer', "pointer"], 'thiscall');    console.log("load_script at:", load_script)     // use this to store c++ context    var pthis = ptr(0)    Interceptor.attach(addr_loadscript, {        onEnter: function(args){            pthis = ptr(this.context.ecx)        }    })    install_decompress_hook(outdir)     // wait for c++ context    while(!pthis.toInt32())    {        Thread.sleep(0.2);    }     // dump all scripts    var name_buf = Memory.alloc(0x100);    for(var i=0;i<names.length;i++)    {        console.log("try to dump", names[i], ", this=",pthis);        name_buf.writeAnsiString(names[i]);        load_script(pthis, name_buf);    }    console.log("dump asbs finished!\n");} function dump_scenario(){    var names_v103 = ["00suzuk.asb"]    dump_asbs(names_v103)}
```

用其他工具如arc unpack可以得到arc封包的文件名，把文件名录入frida脚本，即可dump出全部asb脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FZfAJlzgym2qq3cobb79jlDjX0fYFHXIkJoia8XJAy0KxvbedoWVEBX0g6maPPeictbsr69ZJMC7Cg/640?wx_fmt=jpeg)

##

##

```
二

动态替换脚本文件
```

###

### **(1) 替换解密的asb缓冲区**

结合上面文件分析，我们可以在004311E1| E8 7F99FDFF| call lamune.40AB65| decompress进行inlinehook，在此直接加载我们已经解密并汉化的asb文件。解密的缓冲区是前面new出来的，我们还需要修改缓冲区大小。另外还要nop掉缓冲区crc校验的函数。

上节我们用了detours，这期我们来手动inlinehook，步骤如下：

① 在需要hook的位置用5字节call(E9)或 jmp(E8) 进行相对跳转到我们的函数上，机器码为E8 XXXXXXXX, E9 XXXXXXXX。XXXXXXXX为相对于下一条指令的偏移，即targetva - (va + 5)。

② 执行完后hook的函数后，结尾手动修复一下被我们修改5字节破坏的代码，跳转到下个指令处。

动态替换解密后的缓冲区脚本代码如下：

```
/* for hook new decompressed buffer0043119A   | FF75 E0   | push dword ptr ss:[ebp-20]0043119D   | E8 A1510000  | call lamune.436343 | new004311A2   | FF75 E4    | push dword ptr ss:[ebp-1C]  | [ebp-1c] raw_size004311A5   | 8945 F0  | mov dword ptr ss:[ebp-10],eax004311A8   | E8 96510000         | call lamune.436343  | new raw_buf*/const DWORD g_newrawbufi_4311A2 = 0x4311A2;const DWORD g_newrawbufo_4311A8 = 0x4311A8; /* for hook decompress asb.text:004311D4 FF 75 E4          push    [ebp+raw_size]  ; raw_len.text:004311D7 8D 4D EC          lea     ecx, [ebp+var_14].text:004311DA 57                push    edi             ; raw_data.text:004311DB FF 75 E0    push [ebp+compressed_size] ; compressed_len.text:004311DE FF 75 F0    push [ebp+compressed_data] ; compressed_data.text:004311E1 E8 7F 99...