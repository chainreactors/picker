---
title: 用Python实现基于Flask的简单Web应用：从零开始构建个人博客
url: https://blog.csdn.net/nokiaguy/article/details/142714761
source: 一个被知识诅咒的人
date: 2024-10-07
fetch_date: 2025-10-06T18:48:58.674368
---

# 用Python实现基于Flask的简单Web应用：从零开始构建个人博客

# 用Python实现基于Flask的简单Web应用：从零开始构建个人博客

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-10-06 10:30:00 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量2k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

46

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
41

CC 4.0 BY-SA版权

分类专栏：
[Python杂谈](https://blog.csdn.net/nokiaguy/category_12800257.html)
文章标签：
[python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[flask](https://so.csdn.net/so/search/s.do?q=flask&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[前端](https://so.csdn.net/so/search/s.do?q=%E5%89%8D%E7%AB%AF&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/142714761>

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Python杂谈
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12800257.html "Python杂谈")

390 篇文章

订阅专栏

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

### 前言

在现代Web开发中，Python因其简洁、易用以及丰富的库生态系统，成为了许多开发者的首选编程语言。Flask作为一个轻量级的Python Web框架，以其简洁和灵活性深受开发者喜爱，特别适合构建小型Web应用或原型项目。本文将通过详细的步骤，讲解如何使用Flask从零构建一个简单的Web应用——个人博客。我们将介绍Flask的基本功能，如路由、模板渲染、表单处理、数据库集成等，并最终实现一个可以发布和管理文章的博客平台。

### 目录

1. Flask简介及其特点
2. 环境搭建与Flask安装
3. 构建基础Flask应用
4. 使用HTML模板渲染博客页面
5. 表单处理与文章发布功能
6. 数据库集成：使用SQLite存储博客文章
7. 用户认证与登录系统
8. 部署Flask应用
9. 总结与展望

---

### 1. Flask简介及其特点

Flask是一个基于Python的微框架，所谓“微”并不意味着功能不强大，而是它的设计哲学是“只提供基础功能，其他的交给开发者自行选择扩展”。相比于像Django这样的全功能框架，Flask更适合于那些需要定制化的项目或快速原型开发。其核心特点包括：

* **轻量级**：Flask只提供必要的Web功能，如路由和请求处理，其他功能通过扩展实现。
* **灵活性强**：开发者可以根据项目需求自由选择数据库、模板引擎等技术栈。
* **易于学习**：Flask简单明了的API使其非常适合初学者。

---

### 2. 环境搭建与Flask安装

在开始开发之前，我们首先需要搭建Python开发环境，并安装Flask库。步骤如下：

#### 2.1 安装Python

确保你已经安装了Python 3.x，可以通过以下命令检查版本：

```
python --version
```

如果尚未安装Python，可前往[Python官网](https://www.python.org/)下载安装包。

#### 2.2 创建虚拟环境

为了避免依赖冲突，我们建议为Flask项目创建一个独立的虚拟环境。虚拟环境可以通过以下命令创建：

```
python -m venv venv
```

激活虚拟环境：

* Windows:

```
venv\Scripts\activate
```

* macOS/Linux:

```
source venv/bin/activate
```

#### 2.3 安装Flask

在虚拟环境中使用`pip`安装Flask：

```
pip install flask
```

通过`flask --version`命令检查Flask是否成功安装：

```
Flask 2.x.x
```

---

### 3. 构建基础Flask应用

在成功安装Flask之后，我们可以开始构建一个简单的Flask应用。Flask应用的核心是通过路由（Route）机制将URL映射到函数，处理用户请求并返回响应。

#### 3.1 创建项目结构

首先，创建一个Flask项目的基本目录结构：

```
flask_blog/
    ├── app.py
    ├── static/
    ├── templates/
    ├── venv/
```

#### 3.2 编写第一个Flask应用

在`app.py`中编写最简单的Flask应用：

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "欢迎来到我的个人博客！"

if __name__ == '__main__':
    app.run(debug=True)
```

* **`app = Flask(__name__)`**：初始化Flask应用。
* **`@app.route('/')`**：定义一个路由，将URL `/` 映射到 `home` 函数。
* **`app.run(debug=True)`**：以调试模式运行服务器。

运行该应用：

```
python app.py
```

浏览器中访问`http://127.0.0.1:5000`，即可看到返回的“欢迎来到我的个人博客”消息。这就是一个最简单的Flask应用！

#### 3.3 使用Jinja2模板引擎

Flask默认使用Jinja2模板引擎来渲染HTML页面。我们将HTML文件放在`templates`目录下，并通过Flask渲染这些模板。

创建一个名为`index.html`的模板文件：

```
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>个人博客</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ description }}</p>
</body>
</html>
```

修改`app.py`文件，让Flask渲染这个模板：

```
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="我的个人博客", description="欢迎来到我的博客平台！")

if __name__ == '__main__':
    app.run(debug=True)
```

#### 3.4 静态文件处理

静态文件（如CSS、JavaScript、图片等）应该放在`static`目录下。Flask会自动从该目录中查找静态资源。

创建`static/style.css`文件：

```
/* static/style.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    color: #333;
}
```

在`index.html`中引用该CSS文件：

```
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

刷新浏览器，可以看到样式已经应用到网页上。

---

### 4. 表单处理与文章发布功能

个人博客的核心功能之一就是发布文章。我们将通过HTML表单让用户提交博客文章，并使用Flask处理表单数据。

#### 4.1 创建文章发布表单

在`templates`目录下创建一个`new_post.html`文件，用于发布文章的表单页面：

```
<!-- templates/new_post.html -->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>发布新文章</title>
</head>
<body>
    <h1>发布新文章</h1>
    <form action="/add_post" method="POST">
        <label for="title">标题:</label>
        <input type="text" id="title" name="title"><br><br>
        <label for="content">内容:</label>
        <textarea id="content" name="content"></textarea><br><br>
        <button type="submit">发布文章</button>
    </form>
</body>
</html>
```

#### 4.2 处理表单提交

我们将在`/add_post`路由中处理用户提交的文章数据：

```
from flask import Flask, render_template, request

app = Flask(__name__)

posts = []  # 用于保存发布的文章

@app.route('/')
def home():
    return render_template('index.html', title="我的个人博客", description="欢迎来到我的博客平台！")

@app.route('/new_post')
def new_post():
    return render_template('new_post.html')

@app.route('/add_post', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    posts.append({'title': title, 'content': content})
    return render_template('index.html', title="我的个人博客", description="文章已发布", posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
```

在这个例子中，我们使用`request.form`来获取表单数据，将其存储在`posts`列表中，并在主页上显示已发布的文章。

#### 4.3 显示文章列表

在`index.html`中，显示所有发布的文章：

```
<body>
    <h1>{{ title }}</h1>
    <p>{{ description }}</p>

    <h2>博客文章</h2>
    <ul>
        {% for post in posts %}
            <li>
                <h3>{{ post.title }}</h3>
                <p>{{ post.content }}</p>
            </li>
        {% endfor %}
    </ul>
</body>
```

---

### 5. 数据库集成：使用SQLite存储博客文章

在实际的Web应用中，数据通常存储在数据库中。Flask支持多种数据库的集成，如SQLite、MySQL、PostgreSQL等。为了简单起见，我们使用SQLite数据库来存储博客文章。

#### 5.1 设置数据库

首先，安装Flask的SQLAlchemy扩展库：

```
pip install flask_sqlalchemy
```

修改`app.py`，配置数据库并创建模型：

```
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI

'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

# 定义文章模型
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

# 初始化数据库
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    posts = Post.query.all()
    return render_template('index.html', title="我的个人博客", description="欢迎来到我的博客平台！", posts=posts)

@app.route('/new_post')
def new_post():
    return render_template('new_post.html')

@app.route('/add_post', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    new_post = Post(title=title, content=content)
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
```

在这里，我们使用SQLAlchemy ORM定义了`Post`模型，包含`id`、`title`和`content`字段。每次启动应用时，`create_tables`函数会自动创建数据库表。

---

### 6. 用户认证与登录系统

为了保护博客的管理功能，我们可以为应用添加用户认证功能。用户必须登录后才能发布文章或进行管理操作。

#### 6.1 安装Flask-Login

首先安装`Flask-Login`库：

```
pip install flask-login
```

然后在`app.py`中集成用户登录功能：

```
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

ap...