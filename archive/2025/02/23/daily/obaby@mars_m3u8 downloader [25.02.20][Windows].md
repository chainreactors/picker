---
title: m3u8 downloader [25.02.20][Windows]
url: https://h4ck.org.cn/2025/02/19461
source: obaby@mars
date: 2025-02-23
fetch_date: 2025-10-06T20:35:55.016145
---

# m3u8 downloader [25.02.20][Windows]

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[业余爱好『Favourite』](https://h4ck.org.cn/cats/cxsj/%E4%B8%9A%E4%BD%99%E7%88%B1%E5%A5%BD%E3%80%8Efavourite%E3%80%8F)

# m3u8 downloader [25.02.20][Windows]

2025年2月22日
[24 条评论](https://h4ck.org.cn/2025/02/19461#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/02/20250222_090336312.png)](https://h4ck.org.cn/wp-content/uploads/2025/02/20250222_090336312.png)

图依然是AI的，预计周四去拍写真。

```
更新记录：
1.修复独狼说的那个网站的资源下载
2.修复https证书错误提示
```

```
参数说明：
Microsoft Windows [版本 10.0.22631.4890]
(c) Microsoft Corporation。保留所有权利。

C:\Users\obaby>E:\Pycharm_Projects\m3u8_downloader\dist\m3u8_downloader\m3u8_downloader.exe
****************************************************************************************************
       _           _             ____
  ___ | |__   __ _| |__  _   _  / __ \ _ __ ___   __ _ _ __ ___
 / _ \| '_ \ / _` | '_ \| | | |/ / _` | '_ ` _ \ / _` | '__/ __|
| (_) | |_) | (_| | |_) | |_| | | (_| | | | | | | (_| | |  \__ \
 \___/|_.__/ \__,_|_.__/ \__, |\ \__,_|_| |_| |_|\__,_|_|  |___/
                         |___/  \____/

m3u8 downloader by obaby
Verson: 25.02.20
m3u8_downloader -i <input m3u8 link> -o <output file> -p <out put path> -f <input file> -m <ffmpeg path>
Need Arguments:
         -i <input m3u8 link>
Option Arguments:
         -o <output file> -p <out put path> -f <input file>
         -m <ffmpeg path>
ffmpeg:E:\Pycharm_Projects\m3u8_downloader\dist\m3u8_downloader\bin/ffmpeg.exe
Blog: http://oba.by
      http://www.h4ck.org.cn
Source Code: http://h4ck.org.cn/2020/01/基于ffmpeg的m3u8下载/
****************************************************************************************************
```

下载效果：

```
****************************************************************************************************
[D] 下载文件......
[D] 文件路径:E:\Pycharm_Projects\m3u8_downloader\mp4\每日大赛之AI换脸明星明星已不是梦AI换脸让大家都完成儿时梦想--911爆料-红领巾吃瓜网成人黑料吃瓜每日大赛看片911blw.com-4.mp4
E:\Pycharm_Projects\m3u8_downloader\dist\m3u8_downloader\bin/ffmpeg.exe -protocol_whitelist "file,http,crypto,tcp,https,tls"  -i "https://hls.vdtuzv.com/videos4/55511a428b09e8266ccc4c26052c41fe/55511a428b09e8266ccc4c26052c41fe.m3u8?auth_key=1740233852-67b9dc7c50e1e-0-c642b03cbb6edc19f1607328047a21a0&v=3&time=0" -c copy "E:\Pycharm_Projects\m3u8_downloader\mp4\每日大赛之AI换脸明星明星被操已不是梦AI换脸让大家都完成儿时梦想--911爆料-红领巾吃瓜网成人黑料吃瓜每日大赛看片911blw.com-4.mp4"
ffmpeg version 4.3.1 Copyright (c) 2000-2020 the FFmpeg developers
  built with gcc 10.2.1 (GCC) 20200726
  configuration: --disable-static --enable-shared --enable-gpl --enable-version3 --enable-sdl2 --enable-fontconfig --enable-gnutls --enable-iconv --enable-libass --enable-libdav1d --enable-libbluray --enable-libfreetype --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libopus --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libsrt --enable-libtheora --enable-libtwolame --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libzimg --enable-lzma --enable-zlib --enable-gmp --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvo-amrwbenc --enable-libmysofa --enable-libspeex --enable-libxvid --enable-libaom --enable-libgsm --enable-librav1e --disable-w32threads --enable-libmfx --enable-ffnvcodec --enable-cuda-llvm --enable-cuvid --enable-d3d11va --enable-nvenc --enable-nvdec --enable-dxva2 --enable-avisynth --enable-libopenmpt --enable-amf
  libavutil      56. 51.100 / 56. 51.100
  libavcodec     58. 91.100 / 58. 91.100
  libavformat    58. 45.100 / 58. 45.100
  libavdevice    58. 10.100 / 58. 10.100
  libavfilter     7. 85.100 /  7. 85.100
  libswscale      5.  7.100 /  5.  7.100
  libswresample   3.  7.100 /  3.  7.100
  libpostproc    55.  7.100 / 55.  7.100
[hls @ 0000022cda7a4d00] Skip ('#EXT-X-VERSION:3')
[hls @ 0000022cda7a4d00] Opening 'https://tp3.numbyg.cn/videos4/55511a428b09e8266ccc4c26052c41fe/crypt.key?auth_key=1740235093-91-0-1d39415610ab0f6be656dcfc352f23ee' for reading
[hls @ 0000022cda7a4d00] Opening 'crypto+https://tp3.numbyg.cn/videos4/55511a428b09e8266ccc4c26052c41fe/55511a428b09e8266ccc4c26052c41fe0.ts?auth_key=1740235093-91-0-88a01d83c48b90308c2e746985315b7c' for reading
Input #0, hls, from 'https://hls.vdtuzv.com/videos4/55511a428b09e8266ccc4c26052c41fe/55511a428b09e8266ccc4c26052c41fe.m3u8?auth_key=1740233852-67b9dc7c50e1e-0-c642b03cbb6edc19f1607328047a21a0&v=3&time=0':
  Duration: 00:15:32.62, start: 1.433333, bitrate: 0 kb/s
  Program 0
    Metadata:
      variant_bitrate : 0
    Stream #0:0: Video: h264 (High) ([27][0][0][0] / 0x001B), yuv420p(tv, bt709), 1280x720, 30 fps, 30 tbr, 90k tbn, 180k tbc
    Metadata:
      variant_bitrate : 0
    Stream #0:1: Audio: aac (LC) ([15][0][0][0] / 0x000F), 44100 Hz, stereo, fltp
    Metadata:
      variant_bitrate : 0
Output #0, mp4, to 'E:\Pycharm_Projects\m3u8_downloader\mp4\每日大赛之AI换脸明星明星已不是梦AI换脸让大家都完成儿时梦想--911爆料-红领巾吃瓜网成人黑料吃瓜每日大赛看片911blw.com-4.mp4':
```

更新代码：

```
def get_bl05_m3u8_link(url):
    print('_' * 70)
    print('[A] 解析播放地址......')
    html_doc = get_url_source_code(url)
    bs = BeautifulSoup(html_doc, "html.parser")
    pattern = re.compile(r"var cms_player = {(.*?);$", re.MULTILINE | re.DOTALL)
    player_divs = bs.findAll('div', class_='dplayer')
    m3u8_list= []
    for p in player_divs:
        data_config = p.get('data-config')
        json_data = json.loads(data_config)
        if 'url' in json_data:
            m3u8_link = json_data['url']
        else:
            m3u8_link = json_data['video']['url']
        title = bs.title.string
        print('[A] 标题:' + title)
        print('[A] 播放地址:' + m3u8_link)
        m3u8_list.append({'title':title,
                          'link':m3u8_link})
        print('_' * 70)
    return m3u8_list
```

下载地址：

温馨提示: 此处隐藏内容需要[发表评论](#respond "发表评论")，并且审核通过后才能查看。
（发表评论请勾选 **在此浏览器中保存我的显示名称、邮箱地址和网站地址，以便下次评论时使用。**）
（请仔细检查自己的昵称和评论内容，以免被识别为垃圾评论而导致无法正常审核。）

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《m3u8 downloader [25.02.20][Windows]》](https://h4ck.org.cn/2025/02/19461)
\* 本文链接：<https://h4ck.org.cn/2025/02/19461>
\* 短链接：<https://oba.by/?p=19461>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[ffmpeg](https://h4ck.org.cn/tags/ffmpeg)[m3u8](https://h4ck.org.cn/tags/m3u8)[视频下载](https://h4ck.org.cn/tags/%E8%A7%86%E9%A2%91%E4%B8%8B%E8%BD%BD)

[Previous Post](https://h4ck.org.cn/2025/02/19463)
[Next Post](https://h4ck.org.cn/2025/02/19419)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2023年10月26日

#### [闺蜜圈APP（大姨妈记录） 安卓预览版1.1.6](https://h4ck.org.cn/2023/10/13928)

2022年1月22日

#### [秀人集爬虫 【22.1.20】【OS X】【m1版本】](https://h4ck.org.cn/2022/01/9791)

2021年5月5日

#### [妹子图爬虫](https://h4ck.org.cn/2021/05/8093)

### 24 comments

1. ![](https://gg.lang.bi/avatar/19a53855a6616e2ead18670b736d1917a8b5dbe3f22d629e637d9e3f384e451f?s=64&d=identicon&r=r) **[小彦](https://note-star.cn/)**说道：

   [2025年2月22日 23:53](https://h4ck.org.cn/2025/02/19461#comment-124029...