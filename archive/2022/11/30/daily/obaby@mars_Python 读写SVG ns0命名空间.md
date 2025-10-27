---
title: Python 读写SVG ns0命名空间
url: https://h4ck.org.cn/2022/11/python-%e8%af%bb%e5%86%99svg-ns0%e5%91%bd%e5%90%8d%e7%a9%ba%e9%97%b4/
source: obaby@mars
date: 2022-11-30
fetch_date: 2025-10-04T00:03:41.904371
---

# Python 读写SVG ns0命名空间

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

[物联网『IoT』](https://h4ck.org.cn/cats/cxsj/internet-of-things)

# Python 读写SVG ns0命名空间

2022年11月29日
[4 条评论](https://h4ck.org.cn/2022/11/10789#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/273ab8934aceb738d0ca74cf4fbaf9d9-1024x683.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2022/11/273ab8934aceb738d0ca74cf4fbaf9d9.jpg)

最近再做一个项目的时候需要处理svg文件：

> SVG是一种图形文件格式，它的英文全称为Scalable Vector Graphics，意思为可缩放的矢量图形。它是基于XML（Extensible Markup Language），由World Wide Web Consortium（W3C）联盟进行开发的。严格来说应该是一种开放标准的矢量图形语言，可让你设计激动人心的、高分辨率的Web图形页面。用户可以直接用代码来描绘图像，可以用任何文字处理工具打开SVG图像，通过改变部分代码来使图像具有交互功能，并可以随时插入到HTML中通过浏览器来观看。

上面是百度百科的介绍，网上的svg处理的代码基本都是基于xml.etree.ElementTree，参考链接：https://blog.csdn.net/u010841775/article/details/102365829

具体代码：

```
import xml.etree.ElementTree as ET

tree = ET.ElementTree(file="../../source_data/test.svg")
# 根节点
root = tree.getroot()
# 标签名
print('root_tag:', root.tag)
# gs = root.findall('g')
for stu in root.iter('{http://www.w3.org/2000/svg}g'):
    # 属性值
    print("stu_name:", stu.attrib["name"])
    if stu.tag == '{http://www.w3.org/2000/svg}g':
        print(stu.text)
        print(stu.tag)
tree.write(r'../../source_data/update.svg',encoding='utf-8', xml_declaration=True)
```

上面的代码获取文件内容以及各个节点没问题，但是在写入文件之后文件就会增加ns0， ns1等各个节点。

原始的文件如下：

```
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="1600"
   height="800"
   viewBox="0 0 423.33332 211.66666"
   version="1.1"
   id="svg8"
   inkscape:version="0.92.4 (5da689c313, 2019-01-14)"
   sodipodi:docname="欣晶玻璃模拟图.svg">
  <defs
     id="defs2" />
  <sodipodi:namedview
     id="base"
     pagecolor="#000000"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0"
     inkscape:pageshadow="2"
     inkscape:zoom="0.92409204"
     inkscape:cx="793.72599"
     inkscape:cy="-174.99653"
     inkscape:document-units="px"
     inkscape:current-layer="layer1"
     showgrid="false"
     inkscape:window-width="1920"
     inkscape:window-height="1018"
     inkscape:window-x="-8"
     inkscape:window-y="-8"
     inkscape:window-maximized="1"
     units="px"
     inkscape:pagecheckerboard="0"
     inkscape:snap-global="true"
     inkscape:snap-bbox="false"
     inkscape:bbox-paths="false"
     inkscape:snap-page="false"
     inkscape:snap-text-baseline="false"
     inkscape:snap-center="false" />
  <metadata
     id="metadata5">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1"
     transform="translate(0,470.99997)">
</g>
</svg>
```

文件处理之后丢给前段，前端告诉我文件不能解析了，看了一下处理之后的文件变成了下面的样子（添加了ns0，ns1，ns2）：

```
<?xml version='1.0' encoding='utf-8'?>
<ns0:svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:ns0="http://www.w3.org/2000/svg" xmlns:ns1="http://www.inkscape.org/namespaces/inkscape" xmlns:ns2="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:ns4="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" width="1600" height="800" viewBox="0 0 423.33332 211.66666" version="1.1" id="svg8" ns1:version="0.92.4 (5da689c313, 2019-01-14)" ns2:docname="欣晶玻璃模拟图.svg">
  <ns0:defs id="defs2" />
  <ns2:namedview id="base" pagecolor="#000000" bordercolor="#666666" borderopacity="1.0" ns1:pageopacity="0" ns1:pageshadow="2" ns1:zoom="0.92409204" ns1:cx="793.72599" ns1:cy="-174.99653" ns1:document-units="px" ns1:current-layer="layer1" showgrid="false" ns1:window-width="1920" ns1:window-height="1018" ns1:window-x="-8" ns1:window-y="-8" ns1:window-maximized="1" units="px" ns1:pagecheckerboard="0" ns1:snap-global="true" ns1:snap-bbox="false" ns1:bbox-paths="false" ns1:snap-page="false" ns1:snap-text-baseline="false" ns1:snap-center="false" />
  <ns0:metadata id="metadata5">
    <rdf:RDF>
      <ns4:Work rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title />
      </ns4:Work>
    </rdf:RDF>
  </ns0:metadata>
  <ns0:g ns1:label="Layer 1" ns1:groupmode="layer" id="layer1" transform="translate(0,470.99997)">
  </ns0:g>
</ns0:svg>
```

这尼玛就很蛋疼了。

要解决这个问题其实是需要重新定义namespace， 添加以下代码：

```
ET.register_namespace("","http://www.w3.org/2000/svg") # svg 默认namespace 为空
ET.register_namespace("sodipodi","http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd") # 根据源文件重新定义namespace
ET.register_namespace("inkscape","http://www.inkscape.org/namespaces/inkscape")# 根据源文件重新定义namespace
```

添加以上内容之后，重新写入文件就一切ok了（ns0虽然前端不能解析，但是浏览器是可以正常预览的）。

[![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/搜狗截图20221129221201-1024x475.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2022/11/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20221129221201.jpg)

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《Python 读写SVG ns0命名空间》](https://h4ck.org.cn/2022/11/10789)
\* 本文链接：<https://h4ck.org.cn/2022/11/10789>
\* 短链接：<https://oba.by/?p=10789>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Python](https://h4ck.org.cn/tags/python)[SVG](https://h4ck.org.cn/tags/svg)[XML](https://h4ck.org.cn/tags/xml)

[Previous Post](https://h4ck.org.cn/2022/12/10820)
[Next Post](https://h4ck.org.cn/2022/11/10782)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2023年6月12日

#### [性感美女 爬虫<重构版> [Windows] [23.05.21]](https://h4ck.org.cn/2023/06/12314)

2021年1月5日

#### [Ganlinmu Spider](https://h4ck.org.cn/2021/01/7962)

2024年10月30日

#### [Python 解析 DLT645 协议数据](https://h4ck.org.cn/2024/10/18421)

### 4 comments

1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r) **[dujun](https://dujun.io)**说道：

   [2022年11月29日 22:36](https://h4ck.org.cn/2022/11/10789#comment-89506)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Google Chrome 107](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 107") Google Chrome 107 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   你的图片在 RSS 阅读器里不显示。如果也是用 CDN 加了防盗链的话，要增加一个判断条件是 Referer > 0 才阻断...