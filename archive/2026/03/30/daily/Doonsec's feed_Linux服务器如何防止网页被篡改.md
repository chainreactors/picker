---
title: Linux服务器如何防止网页被篡改
url: https://mp.weixin.qq.com/s/ThBEPK5mtYcpAFWhRhPepg
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:33:40.471577
---

# Linux服务器如何防止网页被篡改

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jkQ8np17Vibj43GOUGxzxogiaZIUiak8lqCfja9ZjEOAria8wiaYPrRboia6y6PXrvdECYyPXnKzEd938gmZgVaJHn0Ldbw4rhQ9ZdUSXZDE5myho/0?wx_fmt=jpeg)

# Linux服务器如何防止网页被篡改

原创

护卫神
护卫神

网站安全说

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jkQ8np17Vibgibxv6JP2ibFwSSqhOicGADhrsqpwAuuuLibTANic5p4ic4bLX3d9R0vdNl1ZNqCMLehiaVZGcgnRIAoyfYbshibRiaX3sYanvbxXRI3Z4/640?wx_fmt=png&from=appmsg)

黑客入侵服务器后，为了利益最大化，多数都会对网站进行破坏，植入后门、植入非法页面、植入恶意代码等等。要防护黑客入侵，修复漏洞毫无疑问是最佳解决办法。然而梦想很美好，现实很残酷。很多时候我们根本不知道漏洞在哪里，就算知晓漏洞在哪里也无从下手，就算修复了漏洞也可能产生新的漏洞。为此对服务器做一些必要的防护措施，才是解决安全防护的上乘之道。防篡改，是防黑客入侵永远绕不开的话题，只要防住了篡改，就解决了大部分入侵问题。下面我们来讲讲如何在Linux上快速实现防篡改功能。

在 Linux服务器上防止网页被篡改，有三种简单办法：使用ACL策略、编写监测软件自动还原、使用专业的防篡改软件。下面我们分别介绍每种方法的实现方法及优缺点。

**1、 使用ACL策略**

即对文件设置只读权限，让黑客没法修改文件。有两种方法实现，一是设置444的权限，二是设置只读属性。推荐使用第二种，因为设置为444后，看起来只有读取权限，但所有者不受限制，仍然可以更改文件。

```
# 设置只读权限（对文件所有者无效）
chmod 444 -R /www/wwwroot/aa

# 设置只读属性
chattr -iR /www/wwwroot/aa
```

优点：简单

缺点：对于需要生成缓存文件或临时文件的网站，则会出现因为没有写权限导致网站无法运行，尤其是一些PHP网站。这种方法虽然防篡改效果很好，但如果影响网站访问那就不是好方法了。

**2、 编写监测软件，自动还原**

需要先将网站复制为一份副本（该副本是确定没有被篡改过的），然后写一个定期检查文件MD5值的脚本，对网站目录和副本目录的文件逐个进行比对，如果MD5值不一致，说明文件被篡改了，立即从副本复制文件进行覆盖。同时可以在该脚本里面排除掉缓存目录。具体脚本如下：

```
#!/bin/bash
# 监测文件，对比MD5的脚本

# 定义源目录和目标目录
SOURCE_DIR="/www/a.com"
BACKUP_DIR="/www/a.com_fuben"
EXCLUDE_DIR="caches"

# 创建临时文件存储文件列表
FILE_LIST=$(mktemp)

# 查找所有文件（排除caches目录）并保存到临时文件
find "$SOURCE_DIR" -type f -path "*/$EXCLUDE_DIR/*" -prune -o -print > "$FILE_LIST"

# 遍历文件列表
while IFS= read -r file; do
    # 计算相对路径（去掉SOURCE_DIR前缀）
    relative_path="${file#$SOURCE_DIR/}"

    # 跳过空路径（当file等于SOURCE_DIR时）
    if [ -z "$relative_path" ]; then
        continue
    fi

    # 构建备份文件的完整路径
    backup_file="$BACKUP_DIR/$relative_path"

    # 检查备份文件是否存在
    if [ ! -f "$backup_file" ]; then
        echo"警告: 备份文件不存在 - $backup_file"
        continue
    fi

    # 计算源文件和备份文件的MD5值
    source_md5=$(md5sum"$file" 2>/dev/null | awk '{print $1}')
    backup_md5=$(md5sum"$backup_file" 2>/dev/null | awk '{print $1}')

    # 比较MD5值
    if [ "$source_md5" != "$backup_md5" ]; then
        echo"发现差异: $file"
        echo"正在用备份文件覆盖..."

        # 创建目标目录（如果不存在）
        mkdir -p "$(dirname "$file")"

        # 覆盖文件
        cp -f "$backup_file""$file"

        # 检查操作是否成功
        if [ $? -eq 0 ]; then
            echo"覆盖成功: $file"
        else
            echo"错误: 无法覆盖 $file"
        fi
    fi
done < "$FILE_LIST"

# 删除临时文件
rm -f "$FILE_LIST"

echo "同步完成"
```

优点：实现简单

缺点：严格来说这算不上防篡改，只是还原文件，具有滞后性。同时后期维护网站比较麻烦，需要上传到副本目录。

**3、 使用防篡改软件**

前两种方法都能解决防篡改，但都有不小的缺点，也没法结合起来使用，因此使用防篡改软件成了必然之选。并非随便一款防篡改软件就能满足需求，有的防篡改软件非常简单，没法对子目录或文件单独设置防篡改规则，对于需要生成缓存文件或临时文件的网站，仍然会出现因为没有写权限导致网站无法运行的情况。推荐使用【护卫神.防入侵系统】，该软件的篡改防护模块非常强大，可以对每个子目录、文件或者文件类型分别设置强大的防篡改规则，能满足所有网站的防篡改需求。同时其内置CMS防篡改模板，可以轻松给网站设置复杂的防篡改规则，既能保证网站不被篡改，又不会产生副作用。

![强大的防篡改规则，设置cache目录允许写](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jkQ8np17VibiamfaWVMPmDl1W7Vib1ROm2jNMZo3D3YSticpePmC3jibSB8aiaa5vDVI4kFEmzrronsPKjESj2L7kKOjia819DWKrKBekMEJJjsQVY/640?wx_fmt=jpeg&from=appmsg "强大的防篡改规则，设置cache目录允许写")

*强大的防篡改规则，单独设置cache目录可写*

![一键添加CMS防篡改规则](https://mmbiz.qpic.cn/mmbiz_jpg/jkQ8np17VibhWcFn6ruhS0ucqWWIksBelcjXLEwkTHDAR9BIwKy8A22wD6ZY4KNXnvAia3WUKOQQ9f7znOBWKVMYYemPwaibicrYgD6ibhDW8FUk/640?wx_fmt=jpeg&from=appmsg "一键添加CMS防篡改规则")

*一键添加CMS防篡改规则*

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NV9GjS35LEh5QDfFonaZkRr55IgslibHfSR3vic4EUUyhRVqr2ic5cJx2IPtZm1T4icK3e2Qz8crIibdQAN3535f6kg/0?wx_fmt=png)

网站安全说

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NV9GjS35LEh5QDfFonaZkRr55IgslibHfSR3vic4EUUyhRVqr2ic5cJx2IPtZm1T4icK3e2Qz8crIibdQAN3535f6kg/0?wx_fmt=png)

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