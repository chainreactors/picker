---
title: BVES 虚拟逆向：从 Opcode 到 Flag 的完整分析
url: https://mp.weixin.qq.com/s/101wIRDPG8mIYDoLIkVLTA
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:13:30.718262
---

# BVES 虚拟逆向：从 Opcode 到 Flag 的完整分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZMyIuHTOaaq1RIRCHevjme0s4FWqYPy1TUjbF50gpE8h2jjrmDNicIJuTPsaWjAuHKdpJqkCHPkEWYp5ll675tUf8PfIkKnRCnexMGTL1OiaE/0?wx_fmt=jpeg)

# BVES 虚拟逆向：从 Opcode 到 Flag 的完整分析

原创

小张
小张

网络安全研习社

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> **免责声明：**涉及到的所有技术仅用来学习交流，严禁用于非法用途，未经授权请勿非法渗透，否则产生的一切后果自行承担，如有侵权，请及时联系删帖！

一、前言

下载链接：https://crackmes.one/crackme/69ffdc47d7ff92e1214c0079

二、正文

这道题给了我们两个文件，一个exe一个bvs文件。作者也给了提示如下：

使用bvessel可执行文件运行随附的.bvs 文件。接下来我们执行一下

![](https://mmbiz.qpic.cn/mmbiz_png/ZMyIuHTOaaqh8aavib5G1Z72M0qzZbI01icRoAW1CcIE4LCcSnEcUrqguo0p4icd2AsDbLV7054paDGjKBXX2a8jaGchug4zicplHagiaT9DJDibE/640?wx_fmt=png&from=appmsg)

通过运行给出了很明显的提示in.txt，以及三个变量

我们用ida查看exe，010查看bvs文件，如下：

![](https://mmbiz.qpic.cn/mmbiz_png/ZMyIuHTOaarh5Sut8NIz7vx60s7spI9Ku7AGVnDMDgj2mmjV2TcA6hYqDic99T7E9tVllSibiaRv41dXkvhictzgsHABqgRfeQp1Bau3wx3fmrI/640?wx_fmt=png&from=appmsg)

该程序中没有main函数，且start函数看着不像如下：

```
__int64 sub_140001075(){  signed __int64 StackBase_2; // rcx  signed __int64 *v1; // rdx  int v3; // [rsp+3Ch] [rbp-54h] BYREF  __int64 v4; // [rsp+40h] [rbp-50h]  signed __int64 *v5; // [rsp+48h] [rbp-48h]  __int64 v6; // [rsp+50h] [rbp-40h]  signed __int64 StackBase_1; // [rsp+58h] [rbp-38h]  signed __int64 *v8; // [rsp+60h] [rbp-30h]  struct _TEB *v9; // [rsp+68h] [rbp-28h]  int n48; // [rsp+70h] [rbp-20h]  int Code; // [rsp+74h] [rbp-1Ch]  PVOID StackBase; // [rsp+78h] [rbp-18h]  signed __int64 StackBase_3; // [rsp+80h] [rbp-10h]  int v14; // [rsp+8Ch] [rbp-4h]   StackBase_3 = 0;  n48 = 48;  v9 = NtCurrentTeb();  StackBase = v9->NtTib.StackBase;  v14 = 0;  Code = 0;  while ( 1 )  {    v8 = &qword_140010098;    StackBase_1 = (signed __int64)StackBase;    v6 = 0;    StackBase_2 = (signed __int64)StackBase;    v1 = &qword_140010098;    StackBase_3 = _InterlockedCompareExchange64(&qword_140010098, (signed __int64)StackBase, 0);    if ( !StackBase_3 )      break;    if ( (PVOID)StackBase_3 == StackBase )    {      v14 = 1;      break;    }    Sleep(0x3E8u);  }  if ( n2 == 1 )    amsg_exit(31);  if ( n2 )  {    dword_14001001C = 1;  }  else  {    n2 = 1;    sub_1400023B0();    qword_140010110 = (__int64)SetUnhandledExceptionFilter((LPTOP_LEVEL_EXCEPTION_FILTER)&lpTopLevelExceptionFilter_);    sub_1400095C0(sub_140001000);    sub_140002A80();    dword_140010018 = sub_140001398();    if ( unk_1400100D0 )      _set_app_type(_crt_gui_app);    else      _set_app_type(_crt_console_app);    *(_DWORD *)sub_140009470() = unk_140010100;    *(_DWORD *)sub_140009480() = unk_1400100C0;    Code = sub_140001990();    if ( Code < 0 )      amsg_exit(8);    if ( unk_14000A060 == 1 )      sub_1400024CA(sub_140001AA0);    if ( unk_14000A040 == -1 )      sub_140009600(0xFFFFFFFFLL);    if ( (unsigned int)sub_140009410(&unk_14000C928, &unk_14000C930) )      return 255;    v3 = unk_1400100A0;    Code = _getmainargs(&dword_140010004, &qword_140010008, &qword_140010010, unk_14000A030, &v3);    if ( Code < 0 )      amsg_exit(8);    Code = sub_14000149C((unsigned int)dword_140010004, &qword_140010008);    if ( Code )      amsg_exit(8);    initterm(&First_, &Last_);    sub_140001967();    n2 = 2;  }  if ( !v14 )  {    v5 = &qword_140010098;    v4 = 0;    v1 = (signed __int64 *)_InterlockedExchange64(&qword_140010098, 0);  }  if ( TlsCallback_0 )    TlsCallback_0(0, 2, 0);  *(_QWORD *)sub_140009490(StackBase_2, v1) = qword_140010010;  Code = sub_140009820((unsigned int)dword_140010004, qword_140010008, qword_140010010);  if ( !dword_140010018 )    exit(Code);  if ( !dword_14001001C )    cexit();  return (unsigned int)Code;}
```

不像主逻辑，当然除了看函数还可以看导入表跟string表，同时我们通过bvs中可以看到读取文件的操作，可以通过fopen（）也来追踪。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZMyIuHTOaaqaPMvicKoQkq4oVZfHRcG10MGeL1cwQbnDwKSdROZj1ztSIzcgmqDmHYjutPZXF1OwQI2C2JIjiaUEibQLsOk3wmKpHdSlvAwLk0/640?wx_fmt=png&from=appmsg)

其中这个里面很明显的主程序字符串--debug/IMPEXT/invalid bvs等，跟进快速定位到函数

```
__int64 sub_140009820(){  int n3_1; // ecx  int n3; // ebx  __int64 v2; // rdx  __int64 v3; // rsi  _DWORD *v4; // rdi  __int64 i; // rcx  Stream *Stream; // rsi  unsigned int v7; // edi  __int64 v8; // rax  _BYTE *v9; // r14  int n_3; // r13d  int n62; // r15d  __int64 j; // r12  int j_1; // ebp  int n62_1; // eax  unsigned __int64 n512_1; // rbp  unsigned __int64 n512; // r12  size_t Size; // rdx  _DWORD *v18; // rcx  __int64 k; // rax  char *v20; // rax  __int64 v21; // r15  char v22; // cl  char *v23; // rdx  __int64 m; // r14  __int64 v25; // rdx  int n_8; // ebp  char *v27; // rdx  int n_6; // esi  __int64 (__fastcall *psub_140009620)(); // r13  __int64 v30; // rax  int n_7; // r8d  _BYTE *v32; // rsi  const char *mutable; // r14  __int64 v34; // r15  __int64 v35; // rax  const char *v36; // r9  int v37; // r8d  const char *v38; // rbx  int n; // esi  __int64 n_4; // rsi  __int64 v41; // rsi  char *FileName; // r15  Stream *Stream_1; // rax  Stream *Stream_2; // r14  size_t v45; // rax  __int16 v46; // ax  __int64 v47; // r13  __int64 v48; // rsi  char *Destination; // rcx  __int64 v50; // rax  __int64 v51; // r8  __int64 n6; // r8  __int64 n_5; // rdx  const char *v54; // r8  int n_1; // edx  unsigned __int16 Buffer_; // [rsp+3Ah] [rbp-7F86Eh] BYREF  _BYTE Buffer[4]; // [rsp+3Ch] [rbp-7F86Ch] BYREF  _BYTE v59[8]; // [rsp+40h] [rbp-7F868h] BYREF  _BYTE v60[522224]; // [rsp+48h] [rbp-7F860h] BYREF  int n_2; // [rsp+7F838h] [rbp-70h]  char *v62; // [rsp+7F840h] [rbp-68h]  unsigned __int64 n512_2; // [rsp+7F848h] [rbp-60h]  unsigned __int64 n512_3; // [rsp+7F850h] [rbp-58h]  int n_9; // [rsp+7F858h] [rbp-50h]  int v66; // [rsp+7F85Ch] [rbp-4Ch]  _BYTE v67[40]; // [rsp+7F860h] [rbp-48h] BYREF   sub_140002F40();  n3 = n3_1;  v3 = v2;  sub_140001967();  if ( n3 <= 1 )  {    return 1;  }  else  {    v4 = v59;    for ( i = 130568; i; --i )      *v4++ = 0;    if ( n3 == 3 && !strcmp(*(const char **)(v3 + 16), "--debug") )      v66 = 1;    Stream = fopen(*(const char **)(v3 + 8), "rb");    if ( fread(Buffer, 1u, 4u, Stream) != 4 || (v7 = memcmp(Buffer, "BVES", 4u)) != 0 )    {      v8 = psub_140009620();      sub_140002F80(v8, "bvessel error: %s\n", "invalid bvs");      exit(1);    }    v9 = v59;    n_3 = 0;    v59[0] = fgetc(Stream);    fgetc(Stream);    n_2 = (unsigned __int8)fgetc(Stream) >> 1;    while ( n_3 < n_2 )    {      n62 = 0;      for ( j = 0; ; v9[j + 7] = n62_1 )      {        j_1 = j;        n62_1 = fgetc(Stream);        if ( n62_1 == -1 )          break;        if ( n62 == 62 && n62_1 == 62 )        {          j_1 = j - 1;          v67[4112 * n_3 - 522265 + (int)j] = 0;          break;        }        ++j;        n62 = n62_1;      }      ++n_3;      v9 += 4112;      *((_QWORD *)v9 - 1) = j_1;    }    n512_1 = 0;    n512 = 512;    v62 = (char *)malloc(0x3800u);    while ( fread(&Buffer_, 2u, 1u, Stream) == 1 )    {      if ( n512_1 >= n512 )      {        Size = 56 * n512;        n512 *= 2LL;        v62 = (char *)realloc(v62, Size);      }      v18 = &unk_14000B180;      for ( k = 0; k != 14; ++k )      {        if ( *v18 == Buffer_ )        {          v20 = (char *)&unk_14000B180 + 16 * k;          goto LABEL_29;        }        v18 += 4;      }      v20 = 0;LABEL_29:      v21 = 28 * n512_1;      v22 = 0;      v23 = &v62[28 * n512_1];      *(_DWORD *)v23 = Buffer_;      if ( v20 )        v22 = v20[4];      v23[4] = v22;      for ( m = 0; (unsigned __int8)v62[v21 + 4] > (int)m; ++m )      {        v25 = 2 * m;        fread(&v62[v21 + 6 + v25], 2u, 1u, Stream);      }      ++n512_1;    }    n512_2 = n512_1;    fclose(Stream);    while ( 1 )    {      n_8 = n_9;      if ( n_9 || n512_3 >= n512_2 )        break;      v27 = &v62[28 * n512_3++];      if ( !*((_DWORD *)v27 + 6) )      {        switch ( *(_DWORD *)v27 )        {          case 1:            n_9 = 1;            goto LABEL_47;          case 2:            n_4 = *((_WORD *)v27 + 3) & 0x7FFF;            if ( (int)n_4 < n_2 )            {              v41 = 4112 * n_4;              if ( !v60[v41 + 4104] )              {                FileName = &v59[4112 * (*((_WORD...