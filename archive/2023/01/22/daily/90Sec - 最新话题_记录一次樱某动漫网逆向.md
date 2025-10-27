---
title: 记录一次樱某动漫网逆向
url: https://forum.90sec.com/t/topic/2215
source: 90Sec - 最新话题
date: 2023-01-22
fetch_date: 2025-10-04T04:32:16.324690
---

# 记录一次樱某动漫网逆向

[90Sec](/)

# [记录一次樱某动漫网逆向](/t/topic/2215)

[账号审核](/c/account/11)

[Sword](https://forum.90sec.com/u/Sword)

2023 年1 月 21 日 15:46

1

### 前言

寒假闲来无事,无聊看看动漫,想着看樱某也有好几年了,就研究一下

[![99999](https://forum.90sec.com/uploads/default/optimized/2X/3/334d8016c97e79668ac66fa352fc18b2a92bf52f_2_689x440.jpeg)

999991290×824 159 KB](https://forum.90sec.com/uploads/default/original/2X/3/334d8016c97e79668ac66fa352fc18b2a92bf52f.jpeg "99999")

\99999.png)

### 绕过无限debugger

随机点进一个视频,打开`f12`看到下图

[![image](https://forum.90sec.com/uploads/default/original/2X/2/24501e8daf659b6837ea515de0826b88fcda0812.png)

image1126×176 14.9 KB](https://forum.90sec.com/uploads/default/original/2X/2/24501e8daf659b6837ea515de0826b88fcda0812.png "image")

可以看到这是一个无限`debugger`,它会阻止你看他代码不断的产生不可回收的对象，占据你的*内存*，造成*内存*泄漏，没过多久*浏览器*就会卡顿

这个debugger是从这个构造器这边进来的

[![image](https://forum.90sec.com/uploads/default/optimized/2X/b/b93a500a89dc2ea424aacea8692af45962c94434_2_690x225.png)

image1313×429 33.7 KB](https://forum.90sec.com/uploads/default/original/2X/b/b93a500a89dc2ea424aacea8692af45962c94434.png "image")

绕过`debugger`的方式有很多种,如

* 全局/局部禁用断点
* `fd`中间人替换
* 置空关键函数

​ 这里直接在debugger右键禁用局部断点就好,然后在上一个堆栈的`409`行以及`411`行打上断点,这个时候就可以成功绕过这个`debugger`了.....

接着因为是视频是通过`ts`文件传输的,所以先找一下`m3u8` 的地址

介绍一下`m3u8文件`

`M3U8`是一种用于播放网络媒体的文件格式，它是一种轻量级的播放列表文件，使用UTF-8编码。 M3U8文件通常包含一组媒体文件的URL，这些文件可以是音频或视频流。

`M3U8`文件通常用于实现流媒体播放，例如在线视频和音频。它们可以用来实现分段加载，这样可以在网络环境较差的情况下提高播放质量。

[![image](https://forum.90sec.com/uploads/default/optimized/2X/d/d5f43ad97cba3202015c9354d8c690229a952fad_2_690x214.png)

image1756×547 164 KB](https://forum.90sec.com/uploads/default/original/2X/d/d5f43ad97cba3202015c9354d8c690229a952fad.png "image")

可以看到请求`m3u8` 的地址形如

```
https://www.xxxxx.me/tmm3p/index.m3u8?path=%2Ftmm3p%2Ffabf72a50836ffa29443abd5d187d1b4.m3u8&t=1674229096&dpvt=93013199994611210910010412146119119119
```

先下一个`xhr`断点,成功断下后分析调用堆栈,当前是在`send`栈

[![image](https://forum.90sec.com/uploads/default/optimized/2X/d/de6cde9551a344a853f12345a1fc5d4e453d7efe_2_690x167.png)

image1422×346 33.4 KB](https://forum.90sec.com/uploads/default/original/2X/d/de6cde9551a344a853f12345a1fc5d4e453d7efe.png "image")

往下找到`__getset_play`这个栈

![image](https://forum.90sec.com/uploads/default/original/2X/8/86e0d5efdf6c439c24a4e2308be37067a234a503.png)

在第`174`行找到了`m3u8`的地址生成,接下来就是查看`vurl`是怎么构造出来的,

[![image](https://forum.90sec.com/uploads/default/optimized/2X/2/24897c27af28061c345e83201d6498c0ac5917e3_2_690x285.png)

image1761×728 272 KB](https://forum.90sec.com/uploads/default/original/2X/2/24897c27af28061c345e83201d6498c0ac5917e3.png "image")

跟进`__getplay_rev_data()`函数发现如下内容,可以直接将其扣出就好~

[![image-20230121020058204](https://forum.90sec.com/uploads/default/original/2X/0/092436751f527e0588468b2e4146f72545a8cce1.png)

image-202301210200582041172×173 7.47 KB](https://forum.90sec.com/uploads/default/original/2X/0/092436751f527e0588468b2e4146f72545a8cce1.png "image-20230121020058204")

```
function __getplay_rev_data(_in_data){
  if(_in_data.indexOf('{') < 0){
    ;var encode_version = 'jsjiami.com.v5', unthu = '__0xb5aef',  __0xb5aef=['wohHHQdR','dyXDlMOIw5M=','dA9wwoRS','U8K2w7FvETZ9csKtEFTCjQ==','wo7ChVE=','VRrDhMOnw6I=','wr5LwoQkKBbDkcKwwqk='];(function(_0x22b97e,_0x2474ca){var _0x5b074e=function(_0x5864d0){while(--_0x5864d0){_0x22b97e['push'](_0x22b97e['shift']());}};_0x5b074e(++_0x2474ca);}(__0xb5aef,0x1ae));var _0x2c0f=function(_0x19a33a,_0x9a1ebf){_0x19a33a=_0x19a33a-0x0;var _0x40a3ce=__0xb5aef[_0x19a33a];if(_0x2c0f['initialized']===undefined){(function(){var _0x4d044c=typeof window!=='undefined'?window:typeof process==='object'&&typeof require==='function'&&typeof global==='object'?global:this;var _0x1268d6='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';_0x4d044c['atob']||(_0x4d044c['atob']=function(_0x2993de){var _0x467e1d=String(_0x2993de)['replace'](/=+$/,'');for(var _0x22a01d=0x0,_0x1ee2a1,_0x2cf5ea,_0x3a84f7=0x0,_0x5c0e64='';_0x2cf5ea=_0x467e1d['charAt'](_0x3a84f7++);~_0x2cf5ea&&(_0x1ee2a1=_0x22a01d%0x4?_0x1ee2a1*0x40+_0x2cf5ea:_0x2cf5ea,_0x22a01d++%0x4)?_0x5c0e64+=String['fromCharCode'](0xff&_0x1ee2a1>>(-0x2*_0x22a01d&0x6)):0x0){_0x2cf5ea=_0x1268d6['indexOf'](_0x2cf5ea);}return _0x5c0e64;});}());var _0x3c81da=function(_0x457f21,_0x6cb980){var _0x133a9b=[],_0x749ec5=0x0,_0x3ceeee,_0x1df5a4='',_0x35a2a6='';_0x457f21=atob(_0x457f21);for(var _0x9a0e47=0x0,_0x4a71aa=_0x457f21['length'];_0x9a0e47<_0x4a71aa;_0x9a0e47++){_0x35a2a6+='%'+('00'+_0x457f21['charCodeAt'](_0x9a0e47)['toString'](0x10))['slice'](-0x2);}_0x457f21=decodeURIComponent(_0x35a2a6);for(var _0x2ef02e=0x0;_0x2ef02e<0x100;_0x2ef02e++){_0x133a9b[_0x2ef02e]=_0x2ef02e;}for(_0x2ef02e=0x0;_0x2ef02e<0x100;_0x2ef02e++){_0x749ec5=(_0x749ec5+_0x133a9b[_0x2ef02e]+_0x6cb980['charCodeAt'](_0x2ef02e%_0x6cb980['length']))%0x100;_0x3ceeee=_0x133a9b[_0x2ef02e];_0x133a9b[_0x2ef02e]=_0x133a9b[_0x749ec5];_0x133a9b[_0x749ec5]=_0x3ceeee;}_0x2ef02e=0x0;_0x749ec5=0x0;for(var _0xa5d5ef=0x0;_0xa5d5ef<_0x457f21['length'];_0xa5d5ef++){_0x2ef02e=(_0x2ef02e+0x1)%0x100;_0x749ec5=(_0x749ec5+_0x133a9b[_0x2ef02e])%0x100;_0x3ceeee=_0x133a9b[_0x2ef02e];_0x133a9b[_0x2ef02e]=_0x133a9b[_0x749ec5];_0x133a9b[_0x749ec5]=_0x3ceeee;_0x1df5a4+=String['fromCharCode'](_0x457f21['charCodeAt'](_0xa5d5ef)^_0x133a9b[(_0x133a9b[_0x2ef02e]+_0x133a9b[_0x749ec5])%0x100]);}return _0x1df5a4;};_0x2c0f['rc4']=_0x3c81da;_0x2c0f['data']={};_0x2c0f['initialized']=!![];}var _0x4222af=_0x2c0f['data'][_0x19a33a];if(_0x4222af===undefined){if(_0x2c0f['once']===undefined){_0x2c0f['once']=!![];}_0x40a3ce=_0x2c0f['rc4'](_0x40a3ce,_0x9a1ebf);_0x2c0f['data'][_0x19a33a]=_0x40a3ce;}else{_0x40a3ce=_0x4222af;}return _0x40a3ce;};var panurl=_in_data;var hf_panurl='';const keyMP=0x100000;const panurl_len=panurl['length'];for(var i=0x0;i<panurl_len;i+=0x2){var mn=parseInt(panurl[i]+panurl[i+0x1],0x10);mn=(mn+keyMP-(panurl_len/0x2-0x1-i/0x2))%0x100;hf_panurl=String[_0x2c0f('0x0','1JYE')](mn)+hf_panurl;}_in_data=hf_panurl;;(function(_0x5be96b,_0x58d96a,_0x2d2c35){var _0x13ecbc={'luTaD':function _0x478551(_0x58d2f3,_0x3c17c5){return _0x58d2f3!==_0x3c17c5;},'dkPfD':function _0x52a07f(_0x5999d5,_0x5de375){return _0x5999d5===_0x5de375;},'NJDNu':function _0x386503(_0x39f385,_0x251b7b){return _0x39f385+_0x251b7b;},'mNqKE':'版本号，js会定期弹窗，还请支持我们的工作','GllzR':'删除版本号，js会定期弹窗'};_0x2d2c35='al';try{_0x2d2c35+=_0x2c0f('0x1','s^Zc');_0x58d96a=encode_version;if(!(_0x13ecbc[_0x2c0f('0x2','(fbB')](typeof _0x58d96a,_0x2c0f('0x3','*OI!'))&&_0x13ecbc[_0x2c0f('0x4','8iw%')](_0x58d96a,'jsjiami.com.v5'))){_0x5be96b[_0x2d2c35](_0x13ecbc[_0x2c0f('0x5','(fbB')]('删除',_0x13ecbc['mNqKE']));}}catch(_0x57623d){_0x5be96b[_0x2d2c35](_0x13ecbc[_0x2c0f('0x6','126j')]);}}(window));;encode_version = 'jsjiami.com.v5';

  }
  return _in_data;
}
```

然后`_json_obj`的来源于`JSON.parse(_in_data)`,`_in_data` 是一个`get`请求成功时的回调参数,根据这个`_getplay_url` 的路径可以看到该请求地址形如:

> www.xxxx.cc/\_getplay?aid=23104&playindex=1&epindex=0&r=0.02312744250345955

[![image](https://forum.90sec.com/uploads/default/original/2X/6/64eb4a1655e27d1098917d553c0f44a74eda9279.png)

image1239×441 31.4 KB](https://forum.90sec.com/uploads/default/original/2X/6/64eb4a1655e27d1098917d553c0f44a74eda9279.png "image")

[![image](https://forum.90sec.com/uploads/default/optimized/2X/2/214d48380f2084e58997d7b7f055a8a620c385f2_2_690x224.jpeg)

image1700×553 129 KB](https://forum.90sec.com/uploads/default/original/2X/2/214d48380f2084e58997d7b7f055a8a620c385f2.jpeg "image")

接下来跟踪`_getplay_url`变量,看一下它这个地址是如何生成的,

[![image](https://forum.90sec.com/uploads/default/original/2X/6/616794b8194a91ddc9fa239d308b17ced6e4749c.png)

image783×209 13.1 KB](https://forum.90sec.com/uploads/default/original/2X/6/616794b8194a91ddc9fa239d308b17ced6e4749c.png "image")

可以看到其实`_getplay_url`来源于`cb_getplay_url()`;

直接跟进`cb_getplay_url`扣下代码就好,`cb_getplay_url`函数如下图

[![image](https://forum.90sec.com/uploads/default/original/2X/5/59be7ee6e088b86d5518c3e00221dcbc176fe48a.png)

image1026×174 7.59 KB](https://forum.90sec.com/uploads/default/original/2X/5/59be7ee6e088b86d551...