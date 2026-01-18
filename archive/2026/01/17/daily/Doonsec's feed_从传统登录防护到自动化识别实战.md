---
title: 从传统登录防护到自动化识别实战
url: https://mp.weixin.qq.com/s/0cMFq4LcAOe2qbL7SAKwMw
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:37:01.983413
---

# 从传统登录防护到自动化识别实战

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BwqHlJ29vcqBL5UuTn3iaibIaG1XbkQzRv1whUqrYSYdl2VuOjKU4U7Bt2WLlQm7ONCIA0IhpeQx1RW1jAEriaAmw/0?wx_fmt=jpeg)

# 从传统登录防护到自动化识别实战

原创

zkaq-newugly
zkaq-newugly

掌控安全EDU

![]()

在小说阅读器中沉浸阅读

扫码领资料

获网安教程

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

# 本文由掌控安全学院 - **我会发着呆 投稿**

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（ https://bbs.zkaq.cn  **）****

# 一、前言

在日常渗透测试过程中，登录框几乎是绕不开的核心入口。无论是 Web 应用、管理后台，还是各类业务系统，认证逻辑的安全性往往直接决定了系统整体的防护水平。实际测试中可以发现，登录模块的防护形态虽然看似多样，但归纳下来，无非集中在几种典型场景。

第一类场景是既不存在验证码，也没有登录失败次数限制。在这种情况下，系统几乎不具备任何有效的防护能力，攻击者可以直接对账号和密码进行自动化爆破，风险最为直观。

第二类场景是不存在验证码，但存在登录失败次数锁定机制。表面上看，这类系统具备一定防护能力，但在实际测试中，如果攻击者掌握了高质量的账号字典，仍然可以通过密码喷洒等方式进行尝试，往往会获得意想不到的收获。

第三类场景是引入了验证码，但未对登录失败次数进行限制，且验证码存在复用问题。这类设计在现实系统中并不少见，攻击者可以通过拦截并复用验证码相关的数据包，从而实现自动化爆破，验证码形同虚设。

而最后一类，也是防护看似最为“完善”的场景：验证码无法直接绕过，且系统未设置明确的登录次数限制。这类系统通常被认为具备较高安全性，但随着 AI 图像识别技术的发展，这种认知正在被逐步打破。通过引入自动化验证码识别技术，例如基于现成 OCR 工具或自行训练专属模型，验证码本身也不再是不可逾越的障碍。

# 二、ddddocr

ddddocr 是一款基于深度学习的轻量级 OCR 工具，主要用于图片验证码的自动化识别。

它内置训练好的识别模型，使用者无需自行训练，即可对常见的数字、字母类验证码进行快速识别。

三、ddddocr初识

pip install ddddocr        通过创建 py 文件

```
# example.pyimport ddddocr
ocr = ddddocr.DdddOcr()
image = open("15.jpg", "rb").read()result = ocr.classification(image)print(result)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqBL5UuTn3iaibIaG1XbkQzRv5tm9OT8nWtW85XyMQRsdZduicz6wmelfddqz7iahlbGByb8CchxbvCrw/640?wx_fmt=png&from=appmsg)

将下载好的验证码图片放入脚本目录，通过 Python 运行即可完成识别。

在实际测试中可以发现，对于非扭曲、干扰较少的验证码，识别成功率非常高。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqBL5UuTn3iaibIaG1XbkQzRvxzAVYm9JkBCoEtCtr5XNmlDqsSiak2O7SSMNRbtH7eZFkZt90mVKApg/640?wx_fmt=png&from=appmsg)

通过测试可以发现，ddddocr 自带的模型库在以下场景中效果有限：

* 强扭曲字体验证码
* 算术型验证码（如若依框架）
* 字体变化频繁、背景复杂的验证码

以若依系统为例，其验证码采用了扭曲的算术图片，默认模型识别成功率较低。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqBL5UuTn3iaibIaG1XbkQzRvdWcG8icf95AeTCicxLoJAwkIicRawJib6pmh4EbExSaDmO0KUUHFz0SneQ/640?wx_fmt=png&from=appmsg)

四、训练专属ddddocr模型

遇到特殊验证码，我们可以针对系统验证码做指定的模型训练

第一步

下载项目到本地

`git clone https://github.com/sml2h3/dddd_trainer.git`

第二步

安装依赖

`pip install -r requirements.txt -i https://pypi.douban.com/simple`

第三步

创建新的项目

`python app.py create {project_name}`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqBL5UuTn3iaibIaG1XbkQzRvjSEsTQfJwjMoSz6jK5u3OheEn1t8pXP5vDvQ1T6MNxvONKic4XaSbRQ/640?wx_fmt=png&from=appmsg)

第四步

准备数据，我们需要大量的数据集来训练我们的模型，针对不同系统的验证码可以指定不同的数据集来训练

根据我实测将你的数据集命名为：验证码结果 \_ 随机 hash 值.jpg

将它放到一个文件夹下面，除法可以使用 z 代替，乘法使用 x 代替，到后面我们可以在 py 文件中定义来达到算数将结果导出

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqBL5UuTn3iaibIaG1XbkQzRvoB750icZiaIEChzT6AKge23pIh6BcEZJMQynwgYGvBZRaRlHRO7LZ9Wg/640?wx_fmt=png&from=appmsg)

大部分数据集需要购买例如若依，但是我们可以通过编写脚本来获取大量的验证码图片

已知它是通过/prod-api/captchaImage 接口来获取验证码图片

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqBL5UuTn3iaibIaG1XbkQzRvDEKvIKo0jZWR1wciaaEaiaOiaY3PNJ33gG7KqTYocRc8hHRyTvMIZO5Mg/640?wx_fmt=png&from=appmsg)

编写专属若依系统自动下载验证码+修改图片文件名代码（其他系统可能也可以，只要获取图片不复杂）

```
# -*- coding: utf-8 -*-import requestsimport base64import osimport timeimport uuidimport hashlibimport re
IMAGE_EXTS = (".jpg", ".jpeg", ".png", ".bmp", ".webp")
def extract_number(filename):    m = re.search(r'\d+', filename)    return int(m.group()) if m else 0
def download_captcha():    print("=" * 50)    print(" 第一步：下载验证码 ")    print("=" * 50)
    base_url = input("请输入系统地址（如 https://example.com）：").strip()    api_path = input("请输入验证码接口路径（如 /prod-api/captchaImage）：").strip()    total = int(input("请输入需要下载的验证码数量：").strip())    save_dir = input("请输入验证码保存目录：").strip('"')
    headers = {        "User-Agent": "Mozilla/5.0",        "Accept": "application/json"    }
    if not os.path.exists(save_dir):        os.makedirs(save_dir)
    print(f"\n[+] 验证码将保存到：{save_dir}")    print("[+] 开始下载...\n")
    for i in range(1, total + 1):        try:            url = base_url.rstrip("/") + api_path            resp = requests.get(url, headers=headers, timeout=10)            resp.raise_for_status()
            data = resp.json()            img_base64 = data.get("img")
            if not img_base64:                print(f"[!] 第 {i} 次未获取到 img")                continue
            img_bytes = base64.b64decode(img_base64)            file_path = os.path.join(save_dir, f"{i}.jpg")
            with open(file_path, "wb") as f:                f.write(img_bytes)
            print(f"[+] 保存 {i}.jpg")            time.sleep(0.2)
        except Exception as e:            print(f"[!] 第 {i} 次失败：{e}")
    print("\n 验证码下载完成\n")    return save_dir

def rename_images(save_dir):    print("=" * 50)    print(" 第二步：根据 txt 重命名 ")    print("=" * 50)
    txt_path = input("请输入 txt 文件路径（一行对应一张图）：").strip('"')
    if not os.path.isfile(txt_path):        print("错误!! txt 文件不存在")        input("按回车退出")        return
    with open(txt_path, "r", encoding="utf-8") as f:        txt_lines = [line.strip() for line in f if line.strip()]
    images = [        img for img in os.listdir(save_dir)        if img.lower().endswith(IMAGE_EXTS)    ]    images.sort(key=extract_number)
    if len(txt_lines) != len(images):        print("错误!! 数量不匹配")        print("txt 行数：", len(txt_lines))        print("图片数量：", len(images))        input("按回车退出")        return
    print("\n[+] 开始重命名...\n")
    for i, img in enumerate(images):        name = txt_lines[i]        h = hashlib.md5(uuid.uuid4().hex.encode()).hexdigest()[:8]        ext = os.path.splitext(img)[1]
        old_path = os.path.join(save_dir, img)        new_name = f"{name}_{h}{ext}"        new_path = os.path.join(save_dir, new_name)
        os.rename(old_path, new_path)        print(f"{img} -> {new_name}")
    print("\n 重命名完成")    input("按回车退出")

if __name__ == "__main__":    img_dir = download_captcha()    rename_images(img_dir)
```

输入要下载验证码的系统的地址，再输入获取验证码的接口，输入要下载的数量，输入验证码要保存的目录，它会自动下载

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqBL5UuTn3iaibIaG1XbkQzRvw1jpDACGUG14A7c58s8uVkUuicW23LGicNicSEGxVEyrVI9W8I6YGqicnA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqBL5UuTn3iaibIaG1XbkQzRvz6P1Kj5bMicChNWb0hgYc43p7NqJ79uAefyibVaiaiaQskiaJEIsajWzz6g/640?wx_fmt=png&from=appmsg)

然后这一步就很鸡肋了，需要自己手打正确的验证码，要求一行一个验证码，行数和图片的命名一致

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqBL5UuTn3iaibIaG1XbkQzRvSYvEXcLjCd6UNjx2DkA0pExyXnUHMpz876wRFZEMkOpibOXuqJbxicZw/640?wx_fmt=png&from=appmsg)

再输入 txt 的地址输入，它会自动将验证码重命名

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqBL5UuTn3iaibIaG1XbkQzRvDhWzlyq1ljmwPqCZxialxl90s9qwTMWBn9ZquQmfgIDIpdNUiaYo3ATg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqBL5UuTn3iaibIaG1XbkQzRvGZ6kL7j7vVlhIZnzF7GvQrVRWfBdqWwKKDV32EicLfxsYKr14hbENOQ/640?wx_fmt=png&from=appmsg)

第五步

缓存数据

`python app.py cache {project_name} ./images/`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqBL5UuTn3iaibIaG1XbkQzRvicAKnicbfcX7Bh0eLmeEhmpEtNzC5etjtIDPdTdGZJZeAY6rJshdkkKw/640?wx_fmt=png&from=appmsg)

第六步

开始训练

`python app.py train {project_name}`

如果出现这样的报错要去修改 \projects\ruoyi2\config.yaml，将 GPU 改为 false，让他用 cpu去训练

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqBL5UuTn3iaibIaG1XbkQzRv5h0VmjQI2Vq0icDWpOrTWpkqurys69YsJBVkwejIUtrml0l5QCl7IdA/640?wx_fmt=png&from=appmsg)

正常训练

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcqBL5UuTn3iaibIaG1XbkQzRv2IELxhHUeiaYzLRKncNX09aao2Xs3t1GodNaicUZHsibeM4n2WKjf1mIw/640?wx_fmt=png&from=appmsg)

第七步

训练好的模型会被放在\projects\ruoyi2\models（onnx文件和charsets.json）

由于我这里数据集太少了，最少要几千张去训练，只有训练好才会产生onnx文件和charsets.json

目前数据集还在收集

如果训练成功可以用自己训练好的 ddddocr 模型去识别验证码

```
import ddddocr
# 验证码图片路径test_pic_path = r'./test/1.png'
# 初始化 OCR（加载自训练模型）ocr = ddddocr.DdddOcr(    charsets_path=r'./model/charsets.json',    import_onnx_path=r'./model/captcha.onnx...