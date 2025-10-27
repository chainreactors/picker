---
title: 将多个图片合并为 PDF
url: https://h4ck.org.cn/2024/08/17865
source: obaby@mars
date: 2024-08-21
fetch_date: 2025-10-06T18:02:03.410568
---

# 将多个图片合并为 PDF

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

[Linux『Linux』](https://h4ck.org.cn/cats/xtxg/linux%E3%80%8Elinux%E3%80%8F)

# 将多个图片合并为 PDF

2024年8月20日
[31 条评论](https://h4ck.org.cn/2024/08/17865#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/08/WechatIMG1089.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/08/WechatIMG1089.jpg)

某个业务需要让用户下载文件盖章之后重新上传盖章版本，但是现在有个问题那就是操作基本都在手机端，通过手机端上传 pdf 的确是个问题。所以目前的方案是上传盖章版之后的图片。

然鹅，这个方法用户表示略微有点蛋疼，有的需要上传几十张图片，这些盖章的图片重新下载之后管理也是个问题。那个是哪个根本分不清楚，并且要想根据业务编号来管理盖章版文件也是个问题。

所以，就给出了一个方案，将上传的 图片重新转换为 pdf。

鉴于图片是放在 oss 上的，oss 本身倒是提供了图片转 pdf 的方法（https://help.aliyun.com/zh/imm/user-guide/convert-an-image-to-pdf）：

```
# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys
import os
from typing import List

from alibabacloud_imm20200930.client import Client as imm20200930Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_imm20200930 import models as imm_20200930_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> imm20200930Client:
        """
        使用AccessKey ID&AccessKey Secret初始化账号Client。
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret
        )
        # 填写访问的IMM域名。
        config.endpoint = f'imm.cn-zhangjiakou.aliyuncs.com'
        return imm20200930Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        # 阿里云账号AccessKey拥有所有API的访问权限，建议您使用RAM用户进行API访问或日常运维。
        # 强烈建议不要把AccessKey ID和AccessKey Secret保存到工程代码里，否则可能导致AccessKey泄露，威胁您账号下所有资源的安全。
        # 本示例通过从环境变量中读取AccessKey，来实现API访问的身份验证。如何配置环境变量，请参见https://help.aliyun.com/document_detail/2361894.html。
        imm_access_key_id = os.getenv("AccessKeyId")
        imm_access_key_secret = os.getenv("AccessKeySecret")
        client = Sample.create_client(imm_access_key_id, imm_access_key_secret)
        sources_0 = imm_20200930_models.CreateImageToPDFTaskRequestSources(
            uri='oss://test-bucket/test-object.jpg'
        )
        create_image_to_pdftask_request = imm_20200930_models.CreateImageToPDFTaskRequest(
            project_name='test-project',
            target_uri='oss://test-bucket/test-target-object.pdf',
            sources=[
                sources_0
            ]
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印API的返回值。
            client.create_image_to_pdftask_with_options(create_image_to_pdftask_request, runtime)
        except Exception as error:
            # 如有需要，请打印错误信息。
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        # 阿里云账号AccessKey拥有所有API的访问权限，建议您使用RAM用户进行API访问或日常运维。
        # 强烈建议不要把AccessKey ID和AccessKey Secret保存到工程代码里，否则可能导致AccessKey泄露，威胁您账号下所有资源的安全。
        # 本示例通过从环境变量中读取AccessKey，来实现API访问的身份验证。如何配置环境变量，请参见https://help.aliyun.com/document_detail/2361894.html。
        imm_access_key_id = os.getenv("AccessKeyId")
        imm_access_key_secret = os.getenv("AccessKeySecret")
        client = Sample.create_client(imm_access_key_id, imm_access_key_secret)
        sources_0 = imm_20200930_models.CreateImageToPDFTaskRequestSources(
            uri='oss://test-bucket/test-object.jpg'
        )
        create_image_to_pdftask_request = imm_20200930_models.CreateImageToPDFTaskRequest(
            project_name='test-project',
            target_uri='oss://test-bucket/test-target-object.pdf',
            sources=[
                sources_0
            ]
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印API的返回值。
            await client.create_image_to_pdftask_with_options_async(create_image_to_pdftask_request, runtime)
        except Exception as error:
            # 如有需要，请打印错误信息。
            UtilClient.assert_as_string(error.message)

if __name__ == '__main__':
    Sample.main(sys.argv[1:])
```

然而，项目里面已经引入了比较旧的 aliyun 的 sdk。这个新的再引用之后就需要修改之前的代码，这也就蛋疼了。

网上搜了一下，代码不少，但是不好用啊，这尼玛，就没人写个靠谱的代码吗？

最终通过PyMuPDF来解决了这个问题：

```
import fitz  # PyMuPDF

# Open an existing PDF or create a new one
pdf_document = fitz.open()  # Creates a new PDF

# Define the image file path
image_path = "path/to/your/image.jpg"

# Get the dimensions of the image
img = fitz.open(image_path)
img_rect = img[0].rect  # Get the rectangle of the first page of the image

# Create a new page with the same dimensions as the image
pdf_page = pdf_document.new_page(width=img_rect.width, height=img_rect.height)

# Insert the image into the new page
pdf_page.insert_image(pdf_page.rect, filename=image_path)

# Save the PDF to a file
pdf_document.save("output.pdf")
pdf_document.close()

```

实际的业务代码：

```
def converImageToPdf(img_list):
    # pdf = fitz.open() # PyMuPDF
    pdf_document = fitz.open()  # Creates a new PDF

    for img_url in img_list:
        img_local_file = download_image(img_url,'confirmd_images')
        img = fitz.open(img_local_file)
        img_rect = img[0].rect  # Get the rectangle of the first page of the image

        # Create a new page with the same dimensions as the image
        pdf_page = pdf_document.new_page(width=img_rect.width, height=img_rect.height)

        # Insert the image into the new page
        pdf_page.insert_image(pdf_page.rect, filename=img_local_file)
        img.close()
    file_name = random_file_name('pdf')
    if not os.path.exists('confirmd_receipt'):
        os.mkdir('confirmd_receipt')
    pdf_document.save(os.path.join('confirmd_receipt/') + file_name)
    pdf_document.close()
```

实际效果：

[![](https://h4ck.org.cn/wp-content/uploads/2024/08/Jietu20240820-151159-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/08/Jietu20240820-151159.jpg)

依赖：

```
PyMuPDFb      ==      1.24.9
```

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《将多个图片合并为 PDF》](https://h4ck.org.cn/2024/08/17865)
\* 本文链接：<https://h4ck.org.cn/2024/08/17865>
\* 短链接：<https://oba.by/?p=17865>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[PDF](https://h4ck.org.cn/tags/pdf)[PyMuPDF](https://h4ck.org.cn/tags/pymupdf)

[Previous Post](https://h4ck.org.cn/2024/08/17870)
[Next Post](https://h4ck.org.cn/2024/08/17856)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2021年1月20日

#### [Putty OpenSSH SSH-2 private key (old PEM format)](https://h4ck.org.cn/2021/01/7973)

2019年11月21日

#### [阿里云 EC2 CentOS 6.0 系统分区扩容](https://h4ck.org.cn/2019/11/6598)

2023年3月29日

#### [ubuntu下php扩展的曲线救国计划](https://h4ck.org.cn/2023/03/11695)

### 31 comments

1. ![](https://gg.lang.bi/avatar/425d58cce2af111638d437b07bad88d0be195...