---
title: 2023陇剑杯半决赛&决赛-流量分析
url: https://mp.weixin.qq.com/s/Hv3cLpjk3UKGf_qKG_BtPA
source: Doonsec's feed
date: 2026-01-19
fetch_date: 2026-01-20T03:33:13.508082
---

# 2023陇剑杯半决赛&决赛-流量分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUic7Se7C5FodvjZaXNqSKs9pdadCPAVTgASEHwFIa7X84AdC6a7KKQkw/0?wx_fmt=jpeg)

# 2023陇剑杯半决赛&决赛-流量分析

原创

北渚
北渚

南有禾木

![]()

在小说阅读器中沉浸阅读

# 前言

无意中搜到了2023陇剑杯半决赛和决赛的题目，看着质量还挺高，于是想拿来做一做，还是老规矩，只做流量分析的题目。

题目与附件来自：

```
https://mp.weixin.qq.com/s/j-EElCMu-q9WTdGKMFoHQw
```

# 半决赛

## 1、easy

题目附件：easy/easy.pcapng

### 1.1、登录的密码是多少，请输入md5加密的32位小写字符串

打开流量包就看到在进行FTP的登录：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUw0yNECzQzXVego9eOLqov2icOjyttOIiarGccC8W7ZYgicQexlDUaZl4A/640?wx_fmt=png&from=appmsg)

然后直接往下翻就行了，看到`Login successful`，51号流量包：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUia7cFlr7enTszOIhrS6R8HTfXcibYPkta7r9ibvOxAIbicaIiccAAQELtfg/640?wx_fmt=png&from=appmsg)

密码是：`test`，其md5的32位小写：`098f6bcd4621d373cade4e832627b4f6`

### 1.2、图片中隐藏的数字是多少

登录成功就该上传文件了，所以从51号包往下翻，翻到`tcp.stream eq 3`：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUVoMUmsx9nS8tGEZaGOEaibeucpeCENYSXiarNxoYec7ic5Zh9ZXYekRaQ/640?wx_fmt=png&from=appmsg)

看到`STOR 11.zip`，这个是127号流量包，但是这里没有传输数据，这是FTP协议的机制：

```
FTP 的 STOR 11.zip 只出现在“控制连接”里，真正的文件内容走的是“另一个 TCP 连接（数据连接）”，所以在当前 tcp.stream 里看不到文件数据

FTP 是一个双通道协议：控制连接，发送命令的长连接都是走的端口21。而数据连接，真正传文件是临时新建的TCP连接

所以：STOR 11.zip只是一句命令，11.zip的二进制内容不在这条 TCP 里

核心在这一句：227 Entering Passive Mode (192,168,220,129,82,109)

FTP PASV 的端口计算规则：端口 = p1 * 256 + p2
这里是：82,109
所以：82 * 256 + 109 = 21101
文件内容走的是：192.168.220.129:21101
```

这里理清楚了，所以接下来过滤`tcp.port eq 21101`：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaU5YVmW16GQbUVAeZK6GX57QjY9j3QlmialMfT0NIFQYGzlibLQtcunBZQ/640?wx_fmt=png&from=appmsg)

追踪TCP流，查看其文件内容：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUNtxlTwHx2VFT2qdXPDoncibY1y79HZ2icIY5mOF7plqY7Nxw64RF5saQ/640?wx_fmt=png&from=appmsg)

把文件导出来：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUCowicP7TewCmX8dvJfqaXRIfktK7yN7wnGpmpUG3bM2hwbEiajWlERuQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUia7mgVBhaYAOOOA4lDo4SrcwIkCwOMxxM14R2USbHEPhhMdCicscWL3w/640?wx_fmt=png&from=appmsg)

然后解压得到一个`11.bmp`：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUDk7LkWb6XyibPIxjBohOXBAr0iaOmxpTIDBUx3ok5gFAq80REvD7Vzsg/640?wx_fmt=png&from=appmsg)

明显是修改高度了，直接扔给PuzzleSolver：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUVX5KqmPTHyPjQFKQ6xL9wu98XKsc0EnveVqcXiaTSgLjNnkTwNeGmOw/640?wx_fmt=png&from=appmsg)

然后得到了三张图片：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaU6bBY87xCBR7iaaEoib7zFX9qF7e9zMeOPPmScur9NvxdO08X5PgyfiaSg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUj9icaEYCKQsGnmEWOtMMLDQbWIBAlGtZkFobQs6PSRgzibrLUSfL8wKA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUibC0BDSB7dOfzcHF9ichnibQfCGibSaz5hicNFDr1nrF4kEovcn7ib0h4j2g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUgNGILLMWxEOxNtia33tdSQttvUyJVgtZmhdLV0kulVusu6prdwSBjTQ/640?wx_fmt=png&from=appmsg)

比较清楚的就是图片3了：`20230101`

### 1.3、被加密的字符串是多少

还是`tcp.stream eq 3`中，看到上传了`py.txt`文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUJBB77lMhJjDSr4zXdmpmCIKGCbJ7X0tJyZxEC0WEDwPDbxcj2N1PFw/640?wx_fmt=png&from=appmsg)

数据传输的端口是`82*256+108=21100`，所以`tcp.port eq 21100`:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUnR7oj9OpHG0vVWDx8EB4SxSSHWX0GfVG1q84W6oNNC3ZKiasmjkBic5w/640?wx_fmt=png&from=appmsg)

追踪流，是`tcp.stream eq 11`，看到`py.txt`文件内容：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUs1VZXjSYbRyc9QFKs4PrZvgkUAcV0ibBwtMu75HBx94FNjaJibpwKN0g/640?wx_fmt=png&from=appmsg)

然后公钥和私钥也都通过ftp上传了，还是一样的思路和方法，提取出来：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUL6WJ8d6aoHkekdDbsz0NUBst02YANhFxoaQfYRdABlicTOsZ8Pic4rsQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUhWwlrhAChSrdEu3x5Riam5Y5ibT9L1MlJ5xalXqZ5fFrxksqqWiac8Kew/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaU0ibryMVEzDKicukXTfYOfRCojy0ibiciafMPDg19z6d2Ixm6UDtrXUvcoVQ/640?wx_fmt=png&from=appmsg)

在FTP执行的命令的最后看到上传了`encrypted.txt`：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUD9iaZiavdJ4ToJUEHt4lW8gWEFKuY1icmhkUKWgQOT9sVGmUFjt1405gQ/640?wx_fmt=png&from=appmsg)

端口是`82*256+112=21104`，过滤端口`tcp.port eq 21104`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUlXAFBBTJmIibDG1hssvc2IL69fsTibIqHVlsMMsnPP9oMsVpBKqcibSTQ/640?wx_fmt=png&from=appmsg)

然后追踪流：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUUtIZGJxxPoyhrypQPdL86ooHkK1783McUlEjdF6MIYwYYmRytld5nw/640?wx_fmt=png&from=appmsg)

这应该就是加密的字符串了，加密算法，公钥私钥都有了，让GPT搞个脚本解密就行了：

```
#!/usr/bin/env python3
# rsa_decrypt_hex.py

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import argparse
import sys

def decrypt_message_hex(encrypted_hex, private_key_path):
    """
    使用 RSA 私钥解密十六进制编码的密文
    """
    try:
        # 读取私钥
        with open(private_key_path, 'rb') as f:
            private_key = RSA.import_key(f.read())

        # 创建 OAEP 解密器
        cipher = PKCS1_OAEP.new(private_key)

        # hex 转 bytes
        encrypted_bytes = bytes.fromhex(encrypted_hex)

        # 解密
        decrypted_bytes = cipher.decrypt(encrypted_bytes)

        # 返回明文
        return decrypted_bytes.decode()
    except Exception as e:
        print(f"[!] 解密失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RSA 私钥解密脚本（支持十六进制密文）")
    parser.add_argument("-k", "--key", required=True, help="RSA 私钥文件路径")
    parser.add_argument("-c", "--cipher", required=True, help="十六进制密文")
    args = parser.parse_args()

    plaintext = decrypt_message_hex(args.cipher, args.key)
    print("[+] 解密结果:")
    print(plaintext)
```

先拿到密文的原始数据：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaU72hRFBjmdzc6gGgZMwyQ4Y8Rt4ziaLfTPUVSThmHWBpOSHRJWrMB9rg/640?wx_fmt=png&from=appmsg)

然后解密：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaU7orWOvpzia9rdPNgFeE2RuosIS1dlFiaUlefuPiauAMARhicUToe5Qh9mw/640?wx_fmt=png&from=appmsg)

被加密的字符串：`8dhn3edfna93rAPN`

用cyberchef也可以：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUXaOJdlcQLj9vHicr6jauiaIHkJaElPVdSLkTlA8ofrwbAW0V2f7dBVZA/640?wx_fmt=png&from=appmsg)

## 2、easyshiro

题目附件： easyshiro/log.json

### 2.1、请给出该应用的 shiro key 如flag{KPH+blxk5D2deZtlxcaaaA=}

shiro的流量解密，用`希潭实验室`的蓝队分析研判工具箱，把`log.json`中最后一次出现的rememberMe扔进去解密：（为什么最后一次？因为前边都是攻击者在爆破，最后一次才是爆破成功）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7O0aO9k0dtaB5um5DD9JibaUv3VHTytA3OMcnlFVdK06NZibicf5RdibFicAHqiaJzmibe9TAjga4mwUgzjw/640?wx_fmt=png&from=appmsg)

```
{"endTime":1692555708782,"httpStatus":200,"requestBody":"","requestHeaders":{"cookie":"rememberMe=Iz28dfd1Q2KBHV3bp493g/dIgDRG87zOZl7rAKQJSM+ptHCQIeGzILfiHlXhnPqei3MiKPERiwUH1TglxC4iS5dG+nbDJGPvtfi5Dr4Dj9hLVlRB/FRqE10l7FdauaHDJlXNtOvevfswEwkvjYD45nYqccCF9hEBrsiVUlHzV1RWJUZsjbm7boWY/4betAffdCDIlPC7faMyMVM13GCp8ItIU+QfaALIiAK0L/xZNzgSJ9YIuPgz3V0dQ+1LHR8AV+zfTaQx9ks1CY+VJA5Q77g7M1DEqUeH8lWXDKJENxwdgjRhZI1dJb4jg6domlvqYDYfvY8t6Zf4NVXSirj8Fk8huuV/UQQUt3Xh6iels+zb7O+zA6RQZMoDKSrkFhcvJTCfWsVjQypMsYyEx5A10a1A2TPgp1t/b9DYfbLuCkGvUVKHatMMNuvkNfzoGKiWu76AKPVV3xPzBpKh6iCCgu7LC78SURz+h59SNS3984CbV2aoAzwookmHCxLG0OJ+8w76qEiMyuYmnrGxdRyANkT6zYxUTa84reXX8fVVb3L1IeMa7Jt2vc8vY1bG1yMaplDiA9Cy3M/jnHCi+D63RHXAAxyxXAOA4N2OPXUWSjfG4ZL+bwWryc70sx+Jvc2kvnEkK1bpFTGhxwzDjkiZ1FSXa1L3jMu896yF3YJ9pWQXdAkzgX/DAfifNhww6Mot/Zl3q7FxNRVzH1zm3VHpRex+hrhO1qs30eOZ/OGEq9OLleV8oBT11/pGD3BZz9UXPNEWFCXVVb9+a+UIrjwzSMqDuvalGlgHyjGhtfQi3m50Ii2mbJkaUrZwuWTlulydij03o0DeJ3KaXt+3qaLJgFU47dwLT8NXuBb7mUIH7+QqrktcinQ4ZlvPrQOiFy7CZnL06eBDcyxvL4tOsBQIbH...