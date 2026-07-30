---
title: 2026黄鹤杯网络安全人才创新大赛学生组(失序货栈）
url: https://mp.weixin.qq.com/s/2EFp3vX5SOKBlEIj_d_SAQ
source: Doonsec's feed
date: 2026-07-29
fetch_date: 2026-07-30T04:48:49.539893
---

# 2026黄鹤杯网络安全人才创新大赛学生组(失序货栈）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PJbxG8icSWialxesY4b4sHHEiaRqeSYt84774estP4gUxiaZLNz2Ouc7ImmfvT2Uh6o9DLjoYIUGGDSjg6Wib8wXbf5OibOfg7yLPBYqnX7h5ZxaI/0?wx_fmt=jpeg)

# 2026黄鹤杯网络安全人才创新大赛学生组(失序货栈）

赛查查

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于沙家小狗
，作者Aphr0d1t3

![](https://wx.qlogo.cn/mmhead/DmTSLTdleeupQib52xvIicwNXI0icTK7ibxfwic1NbBdwvicr0aIOfw3n8zQFIwsStMVVvCWIU133vmqI/0)

**沙家小狗**

下载附件后解压是一堆没有后缀名的文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PJbxG8icSWiakiaricEib7fGPMJTmw8LZSCh4wvY5f5cXncg9m2jusNAFeOQibSAu1pCxUAwhscNAWp8BleBov9asiaiaViaZfFY5Cfk4N3gIEWWWz0g/640?wx_fmt=png&from=appmsg)

在010看发现是压缩包

![](https://mmbiz.qpic.cn/mmbiz_png/PJbxG8icSWiakR1O3b92gB52EntPGn6NPcbAX5H3ELPQlSNGjxU01BiadqUvOfZAq4Pk3YKQlRt8SruoDjY9knxYI50tMwPc8OzBHaKmZuAML0/640?wx_fmt=png&from=appmsg)

解压发现这些压缩包都被加密了

![](https://mmbiz.qpic.cn/mmbiz_png/PJbxG8icSWian6zR61wy8vQMblL8tGVrmvXC6KjnFb2COpqNxxNZcKj0qFflO2viaia16yvibhxmMBibBBCXkIiaG1oiceYjTbk0PjhqyDdgaas1GJc/640?wx_fmt=png&from=appmsg)

而且发现这些压缩包的大小都很小

那么就试一下crc爆破

![](https://mmbiz.qpic.cn/mmbiz_png/PJbxG8icSWiakl1YXN546EwBrT3gKJicmgDrmO8RKxllJu2nbL3MicIzowevBzK0j2J0U2OUDSIQgL1jpstSS0YB1K4TjjYuNQ5BXRpAhxrr9H0/640?wx_fmt=png&from=appmsg)

就当我美滋滋查看1.txt的时候发现居然是

![](https://mmbiz.qpic.cn/mmbiz_png/PJbxG8icSWiamoGgUicesJQXL0jCuBGb94SVXbz5w3lzW6Dp2vahI01ekyByu6REPhp2ZXibmjib4jKH0RFclwb1Afdib3ENicSzjny48mJpY2Z4P0/640?wx_fmt=png&from=appmsg)

气晕了

既然这样，在010看了又不是伪加密，那我只能爆破一下了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PJbxG8icSWianlk942tUxASHC6GWiaOApMol92P72tb0xgoeUyWrcHEU6P2iaeUL2E4ciaWGO4OL2SE1zbs5xW45YWpwX3sKAMibqe2jbia8HnEObQ/640?wx_fmt=png&from=appmsg)

我多爆破了几个发现密码就是文件编号

我突然想起来之前我师哥出题的时候就直接用文件名当过密码

打开txt观察发现里面有base32编码的内容，末尾还有crc32,众所周知crc32是传输数据中用来校验数据是否正确的，

所以说明要选出crc32与前面data的crc32一致的BOX

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PJbxG8icSWiakc3DpyXkCVnhK7vq9BCqtibrySCIynpUUlSvJYFlw5e3BMdzDZnzeDZJ2RMsnNqQqXEyPhJ78yib9Q2s31k6plzUjgwJeSMy1zo/640?wx_fmt=png&from=appmsg)

那么接下来先批量解压缩

```
import os
import re
import shutil
import pyzipper
import rarfile
import py7zr

# ==================== 配置区 ====================
SOURCE_DIR = r"./"          # 压缩包所在文件夹路径
OUTPUT_DIR = r"./output"    # 解压目标文件夹路径
# ================================================

# 文件头签名映射 (Magic Bytes)
MAGIC_BYTES = {
    b'PK\x03\x04': 'zip',
    b'PK\x05\x06': 'zip',   # 空ZIP归档
    b'Rar!\x1a\x07\x00': 'rar',      # RAR4
    b'Rar!\x1a\x07\x01\x00': 'rar',  # RAR5
    b'7z\xbc\xaf\x27\x1c': '7z',
}

def detect_format(filepath):
    """通过读取文件头判断压缩格式"""
    with open(filepath, 'rb') as f:
        header = f.read(8)
    for magic, fmt in MAGIC_BYTES.items():
        if header.startswith(magic):
            return fmt
    return None

def extract_file(filepath, password, output_dir):
    """根据格式选择对应库进行解密解压"""
    fmt = detect_format(filepath)
    pwd_bytes = str(password).encode('utf-8')

    if fmt == 'zip':
        with pyzipper.AESZipFile(filepath) as zf:
            zf.extractall(path=output_dir, pwd=pwd_bytes)
    elif fmt == 'rar':
        with rarfile.RarFile(filepath) as rf:
            rf.extractall(path=output_dir, pwd=str(password))
    elif fmt == '7z':
        with py7zr.SevenZipFile(filepath, mode='r', password=str(password)) as sz:
            sz.extractall(path=output_dir)
    else:
        raise ValueError(f"无法识别的文件格式")

    return fmt

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 匹配 BOX-数字编号 格式
    pattern = re.compile(r'^BOX-(\d+)$')
    files = [f for f in os.listdir(SOURCE_DIR) if os.path.isfile(os.path.join(SOURCE_DIR, f))]

    success, fail = 0, 0
    for filename in sorted(files):
        match = pattern.match(filename)
        if not match:
            print(f"[跳过] {filename} - 文件名不符合 BOX-数字 格式")
            continue

        password = match.group(1)
        filepath = os.path.join(SOURCE_DIR, filename)

        try:
            fmt = extract_file(filepath, password, OUTPUT_DIR)
            print(f"[成功] {filename} | 密码: {password} | 格式: {fmt}")
            success += 1
        except Exception as e:
            print(f"[失败] {filename} | 密码: {password} | 错误: {e}")
            fail += 1

    print(f"\n{'='*40}")
    print(f"处理完成: 成功 {success} 个, 失败 {fail} 个")

if __name__ == '__main__':
    main()
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PJbxG8icSWiamd3xUvt8ibicfBSFiapRoracrz39T8y4QEEpibickv5Ohiap63iaicpYU8AniccRWmc69JVFEcXrhSYiaSFUmMvmnOyYc0USaOibDQreaogY/640?wx_fmt=png&from=appmsg)

接下来筛选出校验crc成功的文件

```
import os
import re
import base64
import zlib

def calc_crc32(raw_bytes: bytes) -> str:
    """计算标准CRC32，返回小写十六进制字符串"""
    crc_int = zlib.crc32(raw_bytes) & 0xFFFFFFFF
    return f"{crc_int:x}"

def safe_base32decode(b32_str: str) -> bytes:
    """自动补填充符，兼容不带=的base32"""
    padding = (8 - len(b32_str) % 8) % 8
    padded = b32_str + "=" * padding
    return base64.b32decode(padded, casefold=True)

def check_file(filepath: str):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        match_data = re.search(r"data=([0-9A-Z]+)", content, re.IGNORECASE)
        match_crc = re.search(r"crc32=([0-9a-fA-F]+)", content)
        if not match_data or not match_crc:
            return None, "无法提取data或crc32字段"

        b32_data = match_data.group(1)
        target_crc = match_crc.group(1).lower()

        decoded = safe_base32decode(b32_data)
        real_crc = calc_crc32(decoded)
        return real_crc == target_crc, f"计算:{real_crc} 目标:{target_crc}"
    except Exception as e:
        return None, f"异常: {str(e)}"

if __name__ == "__main__":
    work_dir = os.getcwd()
    matched_files = []       # 校验相等（通过）
    mismatch_files = []      # CRC不相等（失败）
    error_files = []         # 无法完成校验（解析异常、解码失败等）

    for filename in os.listdir(work_dir):
        if filename.startswith("BOX-"):
            full_path = os.path.join(work_dir, filename)
            if not os.path.isfile(full_path):
                continue

            ok, info = check_file(full_path)
            if ok is True:
                print(f"✅ 校验通过 | {filename} | {info}")
                matched_files.append(filename)
            elif ok is False:
                print(f"❌ 校验不匹配 | {filename} | {info}")
                mismatch_files.append(filename)
            else:
                print(f"⚠️ 校验失败(异常) | {filename} | {info}")
                error_files.append(filename)

    print("\n==================== 统计汇总 ====================")
    print(f"✅ CRC校验相符文件数量：{len(matched_files)}")
    print(f"❌ CRC校验不相符文件数量：{len(mismatch_files)}")
    print(f"⚠️ 未能完成校验的文件数量：{len(error_files)}")
    print("===================================================")

    print("\n【校验通过文件名清单】")
    for name in matched_files:
        print(name)

    # 可选：写入清单文件
    with open("valid_box_list.txt", "w", encoding="utf-8") as fw:
        fw.write("===== 校验通过 =====\n")
        fw.write("\n".join(matched_files))
        fw.write("\n\n===== CRC不匹配 =====\n")
        fw.write("\n".join(mismatch_files))
        fw.write("\n\n===== 校验异常文件 =====\n")
        fw.write("\n".join(error_files))
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PJbxG8icSWiamdsgoak8RGiaQzA5BSrZBxdIthiaOZC68oDGFChVz31e1ORCjFQOO133J8qibRTjd5H4QJnuS1dkKbVMicQfvoV4gGerbTAT2xOXs/640?wx_fmt=png&from=appmsg)

但是我们可以看到除了校验成功的校验失败的，还有未完成校验的，我们的代码一共就定义了3个函数，检查文件的函数肯定不会有这样的报错，那么推测是有的data不能正常进行base32解密的

当我观察这些通过文件名清单时我突然有了个惊人的发现，1kb的文件中除了我用红色笔圈起来的文件，其他文件都是校验通过的文件![](https://mmbiz.qpic.cn/sz_mmbiz_png/PJbxG8icSWiamn1ZdfNtBN9HrMBMaNoHlA0w0ibQcK8Sxicw6Tdn6B20ggribibvuGicOK4UCaeBjHzicQ2jXIsRvpoDevgic7X1vfUCf391f1HR4h2g/640?wx_fmt=png&from=appmsg)

而且这些文件都是base32计算正常的

**这时候就要思考一下这个题究竟想让我干什么，然后我就在一瞬间顿悟了**

crc是用来校验的，而这些base32解码正常完完全全是因为校验失败的文件都只有1kb,那么这不正提示着我继续用之前失败的crc爆破，我之前的直觉没有错，只是用错了地方

接下来就是考虑怎么用crc爆破

data数据按常规想肯定是传输过程中出现了损坏，如果把数据想象为若干部分肯定是某个部分数据有误，所以导致crc校验失败，而我只需要修正这一小部分就行，也就是说我只需要修改对这一小部分crc校验就正确了，而我修改这一小部分的手段就是暴力枚举，既然要暴力枚举我就得尽量把数据分成的若干部分控制的尽量小，（**还有在传输过程是二进制数据，所以爆破的对象是字节不是base32字符**）所以我就假设是一字节错误，如果分为1字节不行，我们再进行扩大，2字节....3字节.....

先手动把红笔圈起来的文件复制到一个单独的文件夹

![](https://mmbiz.q...