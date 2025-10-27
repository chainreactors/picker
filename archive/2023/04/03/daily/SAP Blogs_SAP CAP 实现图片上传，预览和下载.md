---
title: SAP CAP 实现图片上传，预览和下载
url: https://blogs.sap.com/2023/04/02/sap-cap-%e5%ae%9e%e7%8e%b0%e5%9b%be%e7%89%87%e4%b8%8a%e4%bc%a0%ef%bc%8c%e9%a2%84%e8%a7%88%e5%92%8c%e4%b8%8b%e8%bd%bd/
source: SAP Blogs
date: 2023-04-03
fetch_date: 2025-10-04T11:30:22.204531
---

# SAP CAP 实现图片上传，预览和下载

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP CAP 实现图片上传，预览和下载

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163275&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP CAP 实现图片上传，预览和下载](/t5/technology-blog-posts-by-sap/sap-cap-%E5%AE%9E%E7%8E%B0%E5%9B%BE%E7%89%87%E4%B8%8A%E4%BC%A0-%E9%A2%84%E8%A7%88%E5%92%8C%E4%B8%8B%E8%BD%BD/ba-p/13566622)

![lucky_li](https://avatars.profile.sap.com/0/9/id0954a5448f523384eb73fb88b6a6dfd35f1389a166ab57482085656e15b2475a_small.jpeg "lucky_li")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[lucky\_li](https://community.sap.com/t5/user/viewprofilepage/user-id/184808)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163275)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163275)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566622)

‎2023 Apr 02
5:57 AM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163275/tab/all-users "Click here to see who gave kudos to this post.")

1,347

* SAP Managed Tags
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (1)

文件的上传，预览和下载是一个很常见的需求。最近参与的一个项目正好也需要实现一个图片的上传和浏览的功能。该项目基于 SAP CAP 实现， 本文对此做一个简单的说明，希望能对大家有一点点帮助和启发。

### **1. 需求**

* 管理员 (需要登录）：能够对图片上传，下载，预览，查找 （图片描述），修改和删除 。

* 一般用户 （无需登录）：只能预览图片或者下载图片, 不能看到任何其它信息比如图片的描述和文件名，不能做一般的增删改查。

### **2. 相关协议**

* HTTP 有关header

  + content-type  用于图片展示，比如 image/jpg

  + content-disposition 用于文件下载

    - 格式为：  type; filename="your\_file\_name"

    - type:  inline | attachment.

      * + 当为 inline 时，浏览器会根据 content-type 直接展示文件内容

        + 当为 attachment 时，浏览器会根据 filename 直接保持该文件

* OData (v4) 相关知识

  + Edm.Stream 表明该数据类型为二进制的媒体类型： <Property Name="media" Type="Edm.Stream"/&gt;

  + 该类型有一些特殊性：

    - 因为媒体类型的二进制数据不能用一般的JSON数据格式展示 （OData不会自动Base64编解码），所以它不会出现在 Entity 中，相应的增删改查都需要特殊处理。

    - 怎样获取该值

      * 直接用该属性名来获取，比如 media/Media(id)/media,  HTTP协议会直接返回该二进制文件，具体媒体类型通过 content-type 来标识

      * 其他的数据类型直接访问属性 media/Media(id)/fileName 时返回值如下所示，content-type 为 application/json

```
{

    "@odata.context": "../$metadata#Media(ae86a20e-015b-4766-82c6-a1a97001a432)/fileName",

    "value": "bird.jpg"

}
```

如果要返回具体的值，则类似 media/Media(id)/fileName/$value， 返回值如下，content-type 为 text/plain, 返回值为文本

```
bird.jpg
```

### **3. CAP 对 media的支持**

具体支持请参考 <https://cap.cloud.sap/docs/guides/media-data>

* @Core.MediaType： 表明该元素类型为 Edm.Stream， 具体的媒体类型可以直接指定值或者通过过另外一个属性来间接指定

* @Core.IsMediaType : true：表明该元素为一个具体的 MIME 类型

* @Core.ContentDisposition.Filename ： 会自动产出  http header：content-disposition：filename

* @Core.ContentDisposition.Type：inline 或者 attachment

### **4. 项目实现**

这是一个典型的BTP 应用，前端基于UI5 FreeStyle， 后端基于CAP NodeJS, 用标准的ODataV4 协议。为支持用户登录，使用了app-router, 前端代码放在resources目录下面，绑定一个xsuaa实例，通过一个destination调用后端的服务。用mta支持部署到btp。

*注：具体代码请参见附录, 文中只对重要部分加以解释。*

#### **4.1 后端实现**

##### **4.1.1 DB CDS**

*media*存放具体的图片，用来支持预览。

*mediaDownload*用来支持下载，它不会重复存放具体的媒体数据，所以需要用 virutal 修饰（不会生成数据库的字段），它会使用*media*指向的数据

```
entity Media : cuid, managed {

        @Core.MediaType   : mediaType

        media   : LargeBinary;

        @Core.IsMediaType : true

        mediaType : String(50);  //map to mine

        url:  String(1000); //full URL of the image. for easy consume by front-end

        desc:   String(200);

        @Core.MediaType   : mediaType

        @Core.ContentDisposition.Filename: fileName

        @Core.ContentDisposition.Type: 'attachment'   //inline

        virtual mediaDownload   : LargeBinary;   //share the same content as the media

        fileName: String(200);

};
```

##### 4.1.2 srv CDS 和具体实现

service CDS比较简单。 因为没有办法通过 @restrict 来赋予普通用户访问单个属性的权利，我们用 JavaScript代码来实现。

```
service MediaService {

    entity Media as projection on schema.Media actions {

        //current we can't find good way to directly return the Edm.Stream format

        function download() returns LargeBinary;

    }

}
```

我还定义了一个 download() 的 function 用来演示下载文件的其他可能实现方法。但是没有找到怎样定义直接返回  Edm.Stream 的方法，只能临时定义返回 LargeBinary, CAP 会自动把该数据变成 Base64编码，所以如果直接调用  media/Media(id)/download() 会返回如下格式的数据，所以该方法暂时行不通。如果谁有解决方案，麻烦告诉我。

```
{

  "@odata.context":"../$metadata#Edm.Binary",

  "value": "base_64_format_data"

}
```

* 权限检查

```
//Only the Admin can access the Images. for read, will check in the on("READ")

    this.before(['CREATE', 'UPDATE', 'DELETE'], Media, req =>

        req.user.is('Admin') || req.reject(403)

    );
```

* 自动生成 URL （为了方便前端访问）和对媒体数据的格式转换: 为了一次性发送所有数据，前端会对媒体文件 进行base64编码，所以后端收到后需要转码。在数据库中直接存储二进制格式数据效率更高。

```
//for the update, manually set the url and decode media from base64

    this.before(["CREATE", "UPDATE"], Media, async (req) => {

        let ID = req.data.ID;

        if (!req.data.url) {

            req.data.url = `${SRV_URL}/media/Media(${ID})/media`;

        }

        //the media content passed from front-end is base64 encode, just convert into binary

        if (req.data.media) {

            req.data.media = new Buffer.from(

                req.data.media,

                "base64"

            );

        }

    });
```

* 媒体内容的处理和权限检查。针对 media 的访问由 CAP自动支持。

```
/**

     * Handler method called on mediaDownload

     **/

    this.on("READ", Media, async (req, next) => {

        if (!req.data.ID) {

            //for the normal read, need Admin scope

            req.user.is('Admin') || req.reject(403)

            return next();

        }

        const url = req._.req.path;

        if (url.includes("/mediaDownload")) {

            return await downloadMedia(Media, req);

        } else if (url.includes("/media")) {

            //for read the media, let it  public

            return next();

        } else {

            //for the normal read, need Admin scope

            req.user.is('Admin') || req.reject(403)

            return next();

        }

    });
```

针对 mediaDownload需要我们来实现：从数据库查找相应的内容即可。

```
async function downloadMedia(Media, req, forFunction = false) {

    //!!for read the image content, let it public for simple

    let ID = req.data.ID;

    if (!ID) {

        //like the Media(ee4087ee-9af9-46cd-9d2d-c393bb415ff5)/download()

        let match = /Media\((.*)\)\/download/.exec(req._.req.url);

        if (match) {

            ID = match[1];

        }

    }

    let tx = cds.transaction(req);

    // Fetch the media obj from database

    let mediaObj = await tx.run(

        SELECT.one.from(Media, ["media", "mediaType", "fileName"]).where(

            "ID =",

            ID

        )

    );

    if (!mediaObj) {

        req.reject(501, `"Internal error. Can't get the object with ID ${ID} from DB`);

        return;

    }

    if (!mediaObj.media || mediaObj.length <= 0) {

        req.reject(404, "Media not found for the ID " + ID);

        return;

    }

    //when add the 'virtual', then we need to s...