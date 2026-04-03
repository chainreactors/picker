---
title: AntiDebug + 脚本实现自动测试Vue路由未授权
url: https://mp.weixin.qq.com/s/58OgKGQ6cYsqKetybJr82g
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:22:55.496978
---

# AntiDebug + 脚本实现自动测试Vue路由未授权

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVnd1p0Q43oYkFbXAG1cN2LymPJ0iaHN7ct9M510qTib3icsBlgq5Z2qN3z1B2s1z0aFlPuFjNzKoE8zDCyUs5iaBJO8QmibRkLrHBeU/0?wx_fmt=jpeg)

# AntiDebug + 脚本实现自动测试Vue路由未授权

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器中沉浸阅读

> 字数 622，阅读大约需 4 分钟

## 前言

前几天，有一位师傅看了`[用小程序跳转工具测未授权和越权思路](https://mp.weixin.qq.com/s?__biz=MzkxNjMwNDUxNg==&mid=2247489879&idx=1&sn=088cdfbe0902178124d84458cea8692b&scene=21#wechat_redirect)`问我，浏览器中的 Vue 也能用吗？

我当时的回答是不行。

今天做渗透测试的时候，又想起来这个问题。

真的不行吗？

还有一个原因是，我今天测的一个项目，Vue 的 path 有足足 500+。

而**AntiDebug Breaker**当前并没有自动跳转，一个个手动点，光是想想，腱鞘炎就要复发了。

既然没有，那就让大模型参考之前小程序的脚本写一个。

+ 前言
+ 演示
+ 脚本

## 演示

用到的 Python 脚本放在文章末尾了，需要自取。

Github在线地址：https://github.com/boqiqibo/securityScriptsPython/blob/main/txt2js\_router.py

![263d02228605e6d32d2652593d28879b.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlOMRsEBAbbP2k8gjn3AJcWoJHPa2nQXlmle3N9gW4Z17rZ4ZCEYkIbJ1GoFiavjtgEaXhJzY1ZW0mGOQu60j6BKvsKRPzxFnyw/640?from=appmsg "null")

263d02228605e6d32d2652593d28879b.png

点击复制所有路径，放在 txt 文件中。

比如
![21924c869a3d0a3a68f274413f344a24.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkwTjT5hEtmxva3ACjsptibruibzuJIFpibkZ8KoQKSRcAD5y3uDiasUdKbzHZ2uEI5MgDuiaa4R9ZEsKsvdpSZRcroTcKaIb4ZSB7k/640?from=appmsg "null")

21924c869a3d0a3a68f274413f344a24.png

命令行执行

```
python txt2js_router.py -f vuepath.txt
```

![88ace740dc8682d8a9fb2739bf8a0432.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnhdqklTgMtwNV3z0DpBxpU16jmg8I5hBXAgKm8bzY8EPictsChic0g0ShvXRyNM1oRiaDGjqXFYMecazgiavAEmVRdiaoyxicbcJs7s/640?from=appmsg "null")

88ace740dc8682d8a9fb2739bf8a0432.png

将生成的 JS 脚本复制到浏览器的 console 当中
![4e7f2583305aa5ae2a96ceaa9023c021.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlFPQrvGFFzjKibPejTTFiaiby3fosHWykIoYTMpMTdDhEiaQoE4hPKHAhy5raCFJGLjR48RITJr7fAibjpY9BMoOxAk5Yo2os41N5Y/640?from=appmsg "null")

4e7f2583305aa5ae2a96ceaa9023c021.png

**注意**
**AntiDebug Breaker** Vue 配置，不要勾选**清除跳转**，否则就失效了。
![4a4f76ad9fc43e991d4cb27fbfee3222.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnBPx3yEDcGSwSXHRt3RFwqVFiabBTZnnHanFJISSPFJIW04p1ZaYibV8yujjSFJiaw4w1n2y2MOLQ8UicwTqYdTHYxxicLV3Ql9FSc/640?from=appmsg "null")

4a4f76ad9fc43e991d4cb27fbfee3222.png

结果：每隔 3s 自动跳转到下一个 Vue path，相关页面访问时请求的 API 也会请求。

![2d035ce09e9c72d1cc80812acc4cc31b.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkdFHo7nCJic4rOcY9odDia3a5icj75YmWOqaqsQj1dAgyedTib9JNHRYDqKKFxXMNKujL0qiazTVm2y3YUavpKzBpWLJ5erEMG7ALw/640?from=appmsg "null")

2d035ce09e9c72d1cc80812acc4cc31b.png

chrome 代理到 Burpsuite 后，就可以在 Burpsuite 看未授权的流量了。

不需要手动跳转，只需要看着，直到出现自己感兴趣的页面就可以了。

## 脚本

```
import argparse

# 1. 解析命令行参数 -f xxx.txt
parser = argparse.ArgumentParser(description='txt路径 → 自动生成Vue路由跳转JS文件')
parser.add_argument('-f', '--file', required=True, help='指定存放路径的txt文件')
args = parser.parse_args()

try:
    # 2. 读取路径文本
    with open(args.file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 清洗路径（去空行、换行）
    path_list = []
    for line in lines:
        path = line.strip()
        if path:
            path_list.append(f'"{path}"')

    # 拼接数组字符串
    paths_str = ',\n  '.join(path_list)

    # 3. 完整的 JS 自动跳转代码（真正3秒一跳，不刷新）
    js_content = f'''// Vue 自动路由跳转脚本
// 生成时间：自动生成
let pages = [
  {paths_str}
];

let index = 0;
function navigateNext() {{
  if (index >= pages.length) {{
    console.log("✅ 所有路由遍历完成");
    return;
  }}
  const path = pages[index];
  console.log("⏩ 跳转：", path);

  try {{
    // Vue Router 无刷新跳转
    if (window.$router) {{
      window.$router.push(path);
    }} else if (document.querySelector('#app')?.__vue__?.$router) {{
      document.querySelector('#app').__vue__.$router.push(path);
    }} else {{
      window.location.href = path;
    }}

    index++;
    setTimeout(navigateNext, 3000);
  }} catch (err) {{
    console.error("❌ 跳转失败：", err);
  }}
}}

// 启动
navigateNext();
'''

    # 4. 保存到本地 JS 文件
    with open('auto_router.js', 'w', encoding='utf-8') as f:
        f.write(js_content)

    print('✅ 生成成功！')
    print('📄 输出文件：auto_router.js')
    print('🔗 使用方式：打开Vue项目 → F12控制台 → 粘贴整个文件运行')

except FileNotFoundError:
    print(f'❌ 错误：未找到文件 {args.file}')
except Exception as e:
    print(f'❌ 处理失败：{str(e)}')
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过