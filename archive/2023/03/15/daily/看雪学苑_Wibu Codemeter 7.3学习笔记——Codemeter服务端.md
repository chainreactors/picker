---
title: Wibu Codemeter 7.3学习笔记——Codemeter服务端
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458498157&idx=2&sn=d295747280e88965238498a6c0c222d9&chksm=b18e84e786f90df1453f9ee399c34a59949623cf76e83a10035091ea556c8fb40412da47cbac&scene=58&subscene=0#rd
source: 看雪学苑
date: 2023-03-15
fetch_date: 2025-10-04T09:36:00.346848
---

# Wibu Codemeter 7.3学习笔记——Codemeter服务端

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F10jT0NrZZuuZBqXnrsyJ0ypt6Pr3j5UwYn0RUGicIZkLdEib6EuD06JrRnmHuNRias2aQdO0Aic65sQ/0?wx_fmt=jpeg)

# Wibu Codemeter 7.3学习笔记——Codemeter服务端

ericyudatou

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FCU79d5iaZe0vCYDibMcYUBoXdvYXtrFluiaLazl4aK6eicX06AeaQDRuorkT5HgIA77nM3bo5Cgr7Vw/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：ericyudatou

```
一

准备
```

1. CodeMeter.exe Win32 v7.30
2. IDA Pro

```
二

初见——反调试
```

之前我说Codemeter的反调试很猛，我收回。Scylla Hide调至VMP档，运行后将爆出的几个错误全部Pass to the Application && Do not suspend or log即可。

```
三

初见——从何入手(通信协议部分)
```

有了前面分析的经验，感觉还是从通信协议入手比较好，顺便看看咱跟人家写的有什么差距。

根据前面的分析，我们知道了Codemeter私有协议中最终要的两个函数就是encrypt\_telegram和decrypt\_telegram。服务器接受到客户端的请求那就必定调用decrypt\_telegram解密，向客户端回复数据必定通过encrypt\_telegram解密。

因此我们第一步就需要确定这两个函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FCU79d5iaZe0vCYDibMcYUBosiaDobNZ1536LqRxD9wjc4cZOg9L4OyQV9xdOggibpRwhna163CVuaZw/640?wx_fmt=png)

用Bindiff就可以轻而易举的解决这个问题。

先对decrypt\_telegram下断，跑起来看看谁调用她。然后我们就轻而易举的找的了这个函数。

```
char __thiscall decrypt_package(void *this, int a2, unsigned __int8 a3, int pbuf, _BYTE *plen, int flag){  char v6; // dl  char result; // al   v6 = 1;  if ( a3 == 160 )  {    if ( (*plen & 0xF) != 0 )                   // len 应当是16的倍数      return 0;    return (*(int (__fastcall **)(void *, char, int, _BYTE *, int))(*(_DWORD *)this + 16))(this, 1, pbuf, plen, flag);// decrypt_telegram  }  else if ( a3 == 161 || a3 == 163 )  {    if ( (*plen & 0xF) == 0 )    {      result = (*(int (__fastcall **)(int, char, int, _BYTE *, _DWORD))(*(_DWORD *)a2 + 16))(a2, 1, pbuf, plen, 0);      *(_DWORD *)plen = *(_DWORD *)(*(_DWORD *)plen + pbuf - 4);      return result;    }    return 0;  }  return v6;}
```

对encrypt\_telegram下断，断在这里：

```
char __thiscall encrypt_package(struct_communication *this, int a2, unsigned __int8 a3, int buf, int *length, int flag){  char result; // al  int v8; // ecx  int v9; // eax  char v10; // bl  int v11; // [esp+10h] [ebp-18h] BYREF  int v12[5]; // [esp+14h] [ebp-14h] BYREF   v12[0] = a2;  result = 1;  if ( a3 == 160 )  {    v12[0] = 0;    sub_219A20(dword_800FC4 + 268);    v9 = *(_DWORD *)this->gap0;    v12[4] = 0;    v10 = (*(int (__thiscall **)(struct_communication *, int, int *, int))(v9 + 12))(this, buf, length, flag);// encrypt_telegram    sub_219A90(v12);    return v10;  }  else if ( a3 == 161 || a3 == 163 )  {    v11 = *length;    sub_3578E0(buf, length, 0);    v8 = *length;    *(_DWORD *)(buf + v8 - 8) = v11;    v11 = v8 - 4;    return (*(int (__thiscall **)(int, int, int *, _DWORD))(*(_DWORD *)v12[0] + 12))(v12[0], buf, &v11, 0);  }  return result;}
```

查看decrypt\_package和encrypt\_package的交叉引用，有一个函数同时引用这两个函数。

```
void __thiscall cm_client_encrypt_req(        _DWORD *this,        _DWORD *message_buf,        unsigned __int8 a3,        unsigned int final_len,        unsigned int a5){  int v6; // ecx  unsigned int v7; // eax  size_t v8; // esi  void *v9; // eax  size_t v10; // ecx  size_t v11; // eax  size_t v12; // esi  _BYTE *buf_1; // esi  int v14; // ecx  int v15; // ecx  size_t v16; // edx  int v17; // eax  int v18; // ecx  char v19; // al  int v20; // ecx  int v21; // ecx  _DWORD *v22; // ecx  unsigned int v23; // edx  _BYTE *v24; // eax  void *p_Block; // edx  _DWORD *v26; // eax  _DWORD *v27; // esi  void *v28; // eax  int v29; // eax  int v30; // eax  int v31; // eax  int v32; // eax  int v33; // eax  int v34; // eax  int v35; // [esp-10h] [ebp-298h]  int v36; // [esp-10h] [ebp-298h]  int v37; // [esp-Ch] [ebp-294h]  int v38; // [esp-Ch] [ebp-294h]  int v39; // [esp-8h] [ebp-290h]  int v40; // [esp-8h] [ebp-290h]  int v41; // [esp-4h] [ebp-28Ch]  int v42; // [esp-4h] [ebp-28Ch]  int v43; // [esp-4h] [ebp-28Ch]  int v44; // [esp-4h] [ebp-28Ch]  int v45; // [esp+0h] [ebp-288h]  char pExceptionObject[140]; // [esp+Ch] [ebp-27Ch] BYREF  char *v47; // [esp+98h] [ebp-1F0h]  int buf; // [esp+9Ch] [ebp-1ECh]  unsigned int v49; // [esp+A4h] [ebp-1E4h]  int v50; // [esp+A8h] [ebp-1E0h]  size_t v51; // [esp+ACh] [ebp-1DCh]  _DWORD *v52; // [esp+B0h] [ebp-1D8h]  char v53; // [esp+B7h] [ebp-1D1h]  char v54[160]; // [esp+B8h] [ebp-1D0h] BYREF  char v55[160]; // [esp+158h] [ebp-130h] BYREF  void **v56; // [esp+1F8h] [ebp-90h] BYREF  __int128 v57; // [esp+1FCh] [ebp-8Ch]  __int128 v58; // [esp+20Ch] [ebp-7Ch]  int v59; // [esp+21Ch] [ebp-6Ch]  int v60; // [esp+220h] [ebp-68h] BYREF  void **v61; // [esp+224h] [ebp-64h] BYREF  void *Block; // [esp+228h] [ebp-60h] BYREF  int v63; // [esp+238h] [ebp-50h]  unsigned int v64; // [esp+23Ch] [ebp-4Ch]  size_t Size[4]; // [esp+240h] [ebp-48h] BYREF  int v66; // [esp+250h] [ebp-38h]  __int128 v67; // [esp+254h] [ebp-34h]  int v68; // [esp+264h] [ebp-24h] BYREF  int v69; // [esp+268h] [ebp-20h] BYREF  unsigned int len_1; // [esp+26Ch] [ebp-1Ch] BYREF  int len; // [esp+270h] [ebp-18h] BYREF  char v72; // [esp+276h] [ebp-12h] BYREF  char v73; // [esp+277h] [ebp-11h] BYREF  int v74; // [esp+284h] [ebp-4h]   v52 = message_buf;  v57 = 0i64;  v56 = &YS0076::YS0306::`vftable';  v58 = 0i64;  v59 = 0;  v74 = 0;  sub_EB4620(v55);  v6 = this[63];  LOBYTE(v74) = 1;  (*(void (__thiscall **)(int, char *))(*(_DWORD *)v6 + 64))(v6, v55);  sub_ECA0E0(v55);  sub_ECA3F0(v41);  v47 = v55;  v7 = a5;  HIDWORD(v67) = 0;  if ( a5 < 0x1000 )    v7 = 4096;  *(_OWORD *)Size = 0i64;  if ( final_len > v7 )    v7 = final_len;  Size[0] = (size_t)&YS0073::YS0080<unsigned char>::`vftable';  memset(&Size[1], 0, 12);  v66 = 1;  v49 = ((v7 + 39) & 0xFFFFFFF0) + 1;  v8 = ((v7 + 39) & 0xFFFFFFF0) + 17;  v51 = v8;  v67 = xmmword_126CA30;  LOBYTE(v74) = 3;  v9 = (void *)unknown_libname_56(v8);  Size[3] = v8;  v10 = (size_t)v9;  Size[1] = (size_t)v9;  Size[2] = v8;  if ( (_DWORD)v67 == 1 )  {    memset(v9, 0, v8);    v11 = Size[2];    v10 = Size[1];  }  else  {    v11 = v51;  }  v12 = 0;  LOBYTE(v74) = 4;  if ( v11 )    v12 = v10;  buf_1 = (_BYTE *)(v12 + 15);  if ( a3 == 0xA2 )    (*(void (__thiscall **)(_DWORD))(*(_DWORD *)this[63] + 20))(this[63]);  v51 = 0;  v53 = 1;  while ( 1 )  {    if ( !(*(unsigned __int8 (__thiscall **)(_DWORD))(*(_DWORD *)this[63] + 84))(this[63]) )    {      sub_EB4620(v54);      v14 = this[63];      LOBYTE(v74) = 5;      (*(void (__thiscall **)(int, char *))(*(_DWORD *)v14 + 64))(v14, v54);      v15 = this[63];      LOBYTE(v50) = a3 != 0xA2;      (*(void (__thiscall **)(int))(*(_DWORD *)v15 + 100))(v15);      sub_DB90E0(this, v54, 3500, v50, 1);      if ( !(*(unsigned __int8 (__thiscall **)(_DWORD))(*(_DWORD *)this[63] + 84))(this[63]) )      {        v32 = sub_D6E030(v45);        v33 = sub_D6E030(v32);        v34 = sub_D6E030(v33);        v36 = sub_D6E030(v34);        sub_D70090(100, v36, v38, v40, v44);        goto LABEL_70;      }      LOBYTE(v74) = 4;      sub_EB4790(v54);    }    v69 = 0;    sub_D79A20(this + 1);    v16 = 0;    len = final_len;    if ( Size[2] )      v16 = Size[1];    len_1 = v49;    LOBYTE(v74) = 6;    v17 = *v52;    buf = v16 + 16;    if ( !(*(unsigned __int8 (__stdcall **)(size_t, int *))(v17 + 4))(v16 + 16, &len) || len != final_len )    {      v52[2] = 100;LABEL_67:      LOBYTE(v74) = 4;      sub_D79A90(&v69);LABEL_68:      v29 = sub_D6E030(v45);      v30 = sub_D6E030(v29);      v31 = sub_D6E030(v30);      v35 = sub_D6E030(v31);      sub_D70090(v52[2], v35, v37, v39, v43);LABEL_70:      _CxxThrowException(pExceptionObject, (_ThrowInfo *)&_TI2_AVException_wbs__);    }    if ( !encrypt_package((int *)&v56, (int)(this + 2), a3, buf, &len, 0) )    {      v52[2] = 302;      goto LABEL_67;    }    ++len;    *buf_1 = a3;    v68 = 0;    v63 = 0;    v64 = 15;    LOBYTE(Block) = 0;    v61 = &wbs::StringBase<char>::`vftable';    v18 = this[63];    LOBYTE(v74) = 7;    v19 = (*(int (__thiscall **)(int, _BYTE *, int, _DWORD, int *, void ***))(*(_DWORD *)v18 + 28))(            v18,            buf_1,            len,            0,            &v68,            &v61);    if ( v19 == 1 )    {      if ( len )      {        *(_QWORD *)(dword_1360FC4 + 520) += (unsigned int...