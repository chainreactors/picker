---
title: DOM-Clobbering入门到实战
url: https://forum.butian.net/share/4553
source: 奇安信攻防社区
date: 2025-09-19
fetch_date: 2025-10-02T20:21:12.364367
---

# DOM-Clobbering入门到实战

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### DOM-Clobbering入门到实战

* [CTF](https://forum.butian.net/topic/52)

常见的XSS有很多，大多数都是通过控制js来进行攻击，但是这次，我们可以只需要HTML即可完成攻击，是不是很好玩？

DOM与Window的关系
=============
当你在HTML设定了一个带有id的元素之后，你可以用window来得到他
```html
<html>
<head></head>
<body>
<button id=Test>click me!</button>
<script>
console.log(window.Test)
</script>
</body>
</html>
```
所以，比如说我要让他弹窗，正常来讲我们可以加一个EventListener，然后触发，像这样子
```js
<script>
document.getElementById("Test")
.addEventListener('click',()=>{
alert(1)
})
</script>
```
但是现在我们可以用一个最短的方式
```js
Test.onclick=()=>alert(1)
```
除了id可以这么用，其实还有另外一些标签也可以，可以看到spec
[html spec](https://html.spec.whatwg.org/multipage/window-object.html#named-access-on-the-window-object)
![Pasted image 20250826130157.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-5d132e462929d341658f5b57d8debba274075472.png)
所以除了id，还有img，form，embed和object可以这么去用。
```php
<embed name="a"></embed>
<form name="b"></form>
<img name="c" />
<object name="d"></object>
```
![Pasted image 20250826131542.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-8044e1e3b5b69e6fe804332a93b06056537c06e1.png)
所以，就是我们可以通过HTML去影响JS
DOM clobbering
==============
这里举一个攻击场景
```html
<html>
<body>
<h1>留言板</h1>
<div>
你的留言：Hello DOM clobbering
</div>
<script>
if (window.TEST\_MODE) {
// load test script
var script = document.createElement('script')
script.src = window.TEST\_SCRIPT\_SRC
document.body.appendChild(script)
}
</script>
</body>
</html>
```
这里假设所有的xss代码都不起作用，只能更改html的情况下，如何才能攻击呢？
我们前面提到我们可以通过id等信息去直接拿到window，所以我们只需要更改html对下面的值进行覆盖即可。
比如说这样子
```html
<div>
你的留言：<div id= "TEST\_MODE"></div>
<a id="TEST\_SCRIPT\_SRC" href="my\_evil\_script"></a>
</div>
```
应该都看得懂，他就会把script的src读进来，那么比如我在本地写一个js，让他弹窗，我们可以试试
![Pasted image 20250826164122.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-1e532680c76f64787ffbc28a97c868c32f223d04.png)
但是这里要注意一点，就是比如我要用console去把这个div的id拼接一个`''`可以看到他的输出就变为了：
![Pasted image 20250826164740.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-77210b05b034b67416a98a1203ccb039a8ced7dd.png)
看到输出的竟然不是字符串而是HTMLDivElement，原因是因为他并没有tostring的方法可以返回字符串，而我们可以查阅一下
![Pasted image 20250826165630.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-feb551f1a2b5059d2f71e5ebd01e02e54304939f.png)
看到只有a和href标签会有这个tostring，所以我们可以总结一下dom clobbering的使用场景是在：
- HTML可控并且JS中有利用到window之类的东西
- 用`<a>`搭配href 以及id 让元素`toString`之后变成我们想要的值
多层级 DOM clobbering
------------------
上面的例子是我们覆盖了单层的dom，那么是否可以覆盖多层的呢？
这里的意思就我们可不可以这样子`window.config.Test`来覆盖Test呢
答案是可以的，我们这里用到了`form`标签即可
```html
<form id="config">
<input name = "IsTest" />
<button id="IsTest2">click me!</button>
</form>
<script>
console.log(window.config.IsTest)
console.log(window.config.IsTest2)
</script>
```
但是注意这里是没有a标签可以用的，所以如果tostring的话，就没办法利用了，所以得搭配点东西利用，这个后面会说
除了利用HTML 本身的层级以外，还可以利用另外一个特性：`HTMLCollection`。
我们可以尝试这样子写(Firefox中只会输出第一个，所以我们用Chrome来看)
```html
<a id="config">aaaa</a>
<a id ="config"></a>
<script>
console.log(window.config)
</script>
```
![Pasted image 20250827015310.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-83642fc587da21659c0fde174a558b97b55eb392.png)
那有了`HTMLCollection`之后可以做什么呢？在[4.2.10.2. Interface HTMLCollection](https://dom.spec.whatwg.org/#interface-htmlcollection)中有写到，可以利用name 或是id 去拿`HTMLCollection`里面的元素。
![Pasted image 20250827020027.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-c3aa4401b49069afe699a9d1ba414adf540539fc.png)
就像这样子，也可以和前面的造成一个结果，但是在firefox下是没办法这样子用的，要注意一下，
然后这里只有两层，如果要三层的话可以用form
```html
<html>
<body>
<form id="config"></form>
<form id="config" name="prod">
<input name="apiUrl" value="123" />
</form>
<script>
console.log(config.prod.apiUrl.value) //123
</script>
</body>
</html>
```
如果你需要もっともっと层级，这个时候就可以用到万能iframe了
```js
<html>
<body>
<iframe name="config" srcdoc='
<a id="apiUrl"></a>
'></iframe>
<script>
setTimeout(() => {
console.log(config.apiUrl) // <a id="apiUrl"></a>
}, 500)
</script>
</body>
</html>
```
这里记得要加上一个setTimeout因为iframe加载需要时间
如果你需要更多层级的话，可以使用这个好用的工具：[DOM Clobber3r](https://splitline.github.io/DOM-Clobber3r/)
利用Document攻击
============
直接上例子吧
```html
<html lang="en">
<head>
<meta charset="utf-8">
</head>
<body>
<img name=cookie>
<form id=test>
<input name=lastElementChild>
<div>I am last child</div>
</form>
<embed name=getElementById></embed>
<script>
console.log(document.cookie) // <img name="cookie">
console.log(document.querySelector('#test').lastElementChild) // <input name=lastElementChild>
console.log(document.getElementById) // <embed name=getElementById></embed>
</script>
</body>
</html>
```
我们利用了HTML 元素影响到了document，原本`document.cookie`应该是要显示cookie 的，现在却变成了`<img name=cookie>`这个元素，而`lastElementChild`原本应该要回传的是最后一个元素，却因为form 底下的name 会优先，因此抓到了同名的元素。
最后的`document.getElementById`也可以被DOM 覆盖，如此一来呼叫`document.getElementById()`时就会出错，可以让整个页面crash。
ok那么我们现在可以打两个lab试试
PortSwigger1
============
我们进来可以看到这里有一个留言区，可以用html的格式
![Pasted image 20250827025450.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-3258840b432af01261cea8fc45eb423d055df5bc.png)
比如我们留一个h1的标签
![Pasted image 20250827025602.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-d28f12a02a771bf9acbe900527cb354164ec4bb1.png)
可以看到是可以的，那么现在我们需要得到flag，如何利用dom clobbering呢？我们可以在源代码处看见
```js
function loadComments(postCommentPath) {
let xhr = new XMLHttpRequest();
xhr.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
let comments = JSON.parse(this.responseText);
displayComments(comments);
}
};
xhr.open("GET", postCommentPath + window.location.search);
xhr.send();
function escapeHTML(data) {
return data.replace(/[<>'"]/g, function(c){
return '&#' + c.charCodeAt(0) + ';';
})
}
function displayComments(comments) {
let userComments = document.getElementById("user-comments");
for (let i = 0; i < comments.length; ++i)
{
comment = comments[i];
let commentSection = document.createElement("section");
commentSection.setAttribute("class", "comment");
let firstPElement = document.createElement("p");
let defaultAvatar = window.defaultAvatar || {avatar: '/resources/images/avatarDefault.svg'}
let avatarImgHTML = '<img class="avatar" src="' + (comment.avatar ? escapeHTML(comment.avatar) : defaultAvatar.avatar) + '">';
let divImgContainer = document.createElement("div");
divImgContainer.innerHTML = avatarImgHTML
if (comment.author) {
if (comment.website) {
let websiteElement = document.createElement("a");
websiteElement.setAttribute("id", "author");
websiteElement.setAttribute("href", comment.website);
firstPElement.appendChild(websiteElement)
}
let newInnerHtml = firstPElement.innerHTML + DOMPurify.sanitize(comment.author)
firstPElement.innerHTML = newInnerHtml
}
if (comment.date) {
let dateObj = new Date(comment.date)
let month = '' + (dateObj.getMonth() + 1);
let day = '' + dateObj.getDate();
let year = dateObj.getFullYear();
if (month.length < 2)
month = '0' + month;
if (day.length < 2)
day = '0' + day;
dateStr = [day, month, year].join('-');
let newInnerHtml = firstPElement.innerHTML + " | " + dateStr
firstPElement.innerHTML = newInnerHtml
}
firstPElement.appendChild(divImgContainer);
commentSection.appendChild(firstPElement);
if (comment.body) {
let commentBodyPElement = document.createElement("p");
commentBodyPElement.innerHTML = DOMPurify.sanitize(comment.body);
commentSection.appendC...