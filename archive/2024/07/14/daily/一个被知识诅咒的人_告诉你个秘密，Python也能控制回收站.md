---
title: 告诉你个秘密，Python也能控制回收站
url: https://blog.csdn.net/nokiaguy/article/details/140401001
source: 一个被知识诅咒的人
date: 2024-07-14
fetch_date: 2025-10-06T17:40:37.551798
---

# 告诉你个秘密，Python也能控制回收站

# 告诉你个秘密，Python也能控制回收站

原创
已于 2024-07-15 21:54:01 修改
·
1.4k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

11

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

11
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2024-07-13 15:43:30 首次发布

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756923.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

奇妙的Python
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12728628.html "奇妙的Python")

3 篇文章

订阅专栏

本文选自[《奇妙的Python：神奇代码漫游之旅》](https://item.jd.com/14027503.html "《奇妙的Python：神奇代码漫游之旅》")。

       本文介绍了如何用Python控制回收站（macOS称为废纸篓），主要内容包括删除回收站中的文件、清空回收站中的文件和恢复回收站中的文件。由于Windows、macOS和Linux操作回收站的API和方式不同，所以本节会分别介绍这3种操作系统操作回收站的API和背后的原理，并通过相应的API将这3个操作系统平台用于操作回收站的API放到一个Python脚本文件中，所以本文提供的Python代码都是跨平台的。

#### 1. 将删除的文件和目录放入回收站

    Python并没有将文件和目录放入回收站的API，所以需要使用第三方的send2trash模块，如果读者未安装这个库，可以执行下面的命令安装send2trash。

pip install send2trash

    send2trash是跨平台的，可以在Windows、macOS和Linux上使用。
     send2trash模块有一个send2trash函数，该函数只有一个paths参数，用于指定移入回收站的一个或多个文件（目录），如果指定一个文件或目录，可以直接使用字符串，如果指定多个文件和目录，需要使用列表，代码如下：

send2trash(['some\_file1', 'some\_file2'])

       下面的代码首先创建了目录和文件，然后使用send2trash函数将这些目录和文件移到回收站（macOS上叫废纸篓），原来的文件和目录就会被删除。

```
from send2trash import  send2trash
import os
# 创建目录
os.makedirs('my_directory', exist_ok=True)

# 创建文件
with open('my_file.txt', 'w') as f:
    f.write('Hello World!')

# 创建多层目录
if not os.path.exists('my_directory/subdirectory/subsubdirectory'):
    os.makedirs('my_directory/subdirectory/subsubdirectory')

# 创建文件
with open('my_directory/subdirectory/subsubdirectory/my_file.txt', 'w') as f:
    f.write('世界你好!')

# 将文件放入回收站
send2trash('my_file.txt') # 将名为'file.txt'的文件放入回收站

# 将名为'my_directory'的目录放入回收站，包括其内部的所有文件和子目录
send2trash('my_directory')
```

#### 2. 清空回收站中的文件

   清空回收站（macOS叫废纸篓）的操作，Windows、macOS和Linux各不相同。下面分别讲解如何清空这3个操作系统中的回收站。

（1）清空Windows回收站

  使用winshell模块中的recycle\_bin函数可以返回一个ShellRecycleBin对象，利用该对象的empty方法可以清空回收站。empty方法的原型如下：

```
empty(confirm=False, show_progress=False, sound=False)
```

参数含义如下：

* confirm：如果为True，则在清空回收站之前显示确认对话框。默认值为False。
* show\_progress：如果为True，则在清空回收站时显示进度条。默认值为False。
* sound：如果为True，则在清空回收站时播放声音。默认值为False。

 如果没有安装winshell模块，需要使用下面的命令安装winshell模块。

pip install winshell

（2）清空macOS废纸篓

   废纸篓也是目录，只不过是特殊的目录，所以只要得到废纸篓的目录，就可以利用1.5节的讲的函数删除废纸篓中的所有文件和目录。macOS废纸篓的目录是“~/.Trash”，其中“~”表示当前用户的子目录，但操作废纸篓需要绝对路径，所以可以使用os.path.expanduser函数将“~/.Trash”转换为绝对目录，代码如下：

```
print(os.path.expanduser("~/.Trash"))
```

执行这行代码，会输出如下的目录：

/Users/lining/.Trash

其中lining是macOS当前登录的用户名。

   得到废纸篓的绝对路径后，可以使用glob.glob函数查找废纸篓中的文件和目录，然后删除所有找到的文件和目录。

glob.glob函数的原型如下：

```
glob.glob(pathname, recursive = False)
```

参数含义如下：

* pathname：要匹配的文件路径名模式。可以是绝对路径或相对路径。
* recursive：如果为True，则递归地查找所有子目录。默认值为False。

（3） 清空Linux回收站

  清空Linux回收站与清空macOS废纸篓类似，同样是找到Linux回收站的相对路径，然后使用os.path.expanduser函数转换为绝对路径，最后使用glob.glob函数查找回收站中的每一个文件和目录，并删除这些找到的文件和目录。Linux回收站的相对路径是“~/.local/share/Trash/files”。

下面的代码根据不同的操作系统采用不同的方式清空回收站。

```
import os
import shutil
import platform
# 清空回收站
def empty_recycle_bin():
    os_name = platform.system()
    if os_name == "Windows":
        # 清空Windows回收站
        try:
            from winshell import recycle_bin
            recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        except ImportError as e:
            print(e)
    elif os_name == "Darwin":
       # 清空macOS废纸篓
        try:
            import glob
            for file in glob.glob(os.path.expanduser("~/.Trash/*")):
                print(file)
                if os.path.isdir(file):
                    shutil.rmtree(file)
                else:
                    os.unlink(file)
        except OSError as e:
            print(e)

    elif os_name == "Linux":
        # 清空Linux回收站
        try:
            import glob
            for file in glob.glob(os.path.expanduser("~/.local/share/Trash/files/*")):
                print(file)
                if os.path.isdir(file):
                    shutil.rmtree(file)
                else:
                    os.unlink(file)
        except OSError as e:
            print(e)

if __name__ == "__main__":
    # 清空回收站
    empty_recycle_bin()
```

运行程序，会发现回收站中的所有文件和目录都消失了。

#### 3. 恢复回收站中的文件

 恢复回收站中的文件的方式可分为如下3步：

* 获取回收站中文件的原始路径
* 将回收站中的文件复制到原始路径
* 删除回收站中的文件

  其实这个过程与剪切文件的方式类似，只是源目录是回收站目录。由于恢复目录与恢复文件的方式类似，所以本节就只提及恢复文件。

      Windows、macOS和Linux在恢复回收站中文件的方式上略有不同，但大同小异，不管是使用第三方API，还是直接使用内建API，都是遵循前面提到的3步。下面分别讲解如何在这3个平台恢复回收站中的文件。

（1）恢复windows回收站中的文件

  在windows中可以使用winshell模块中相关的API恢复回收站中的文件，可以使用下面两种方式：

【1】使用前面提到的3个步骤。通过winshell.recycle\_bin函数可以获取回收站中所有的文件和目录，然后对recycle\_bin函数的返回值进行迭代（假设item为每一个迭代项），可以使用item.filename函数获取文件在回收站中的绝对路径，使用item.original\_filename函数获取文件在被放入回收站之前的路径。获取这两个路径后，使用shutil.copy函数将文件或目录从回收站复制到原始路径，最后使用os.unlink函数删除回收站中的文件和目录，实现代码如下：

```
for item in recycle_bin():
shutil.copy(item.filename(), item.original_filename())
os.unlink(item.filename())
```

【2】使用winshell.undelete函数恢复回收站中的文件，该函数需要将文件的原始路径作为参数传入，实现代码如下：

```
for item in recycle_bin():
winshell.undelete(item.original_filename())
```

（2）恢复macOS废纸篓中的文件

     macOS废纸篓的绝对路径是“/Users/用户名/.Trash”，其中“用户名”是当前登录的用户名，加上用户名是great，那么macOS废纸篓的绝对路径是“/Users/great/.Trash”。在路径下有一个.DS\_Store文件，该文件存储了当前目录的元数据，对于废纸篓来说，就存储了废纸篓中所有文件和目录的相关信息，如原始路径，被删除时间等，但由于.DS\_Store文件的格式苹果公司并未公开，也没有提供任何可以读取.DS\_Store文件的API，而且.DS\_Store文件用的是二进制格式存储。所以通过正常的手段是无法读取.DS\_Store文件内容的，自然也就无法获取废纸篓中文件的原始目录了。因此，在macOS下恢复废纸篓中的文件，只能通过osascript命令了。osascript 是 macOS 上执行 AppleScript 的命令行工具。AppleScript 是一种脚本语言，用于自动化 macOS 应用程序的操作。使用 osascript 命令可以在终端中运行 AppleScript 脚本，也可以在脚本中使用 AppleScript 来发送系统通知。以下是一个发送系统通知的例子：

```
osascript -e 'display notification "Hello World!" with title "Greetings"'
```

在终端执行这行命令，将在屏幕右上角显示一个如图1所示的通知。

![](https://i-blog.csdnimg.cn/direct/98a7692480794810aa992ab2e3596b49.png)

```
-- 打开Finder应用程序
tell application "Finder"
  -- 激活Finder窗口
  activate
  -- 获取垃圾桶中已删除文件的数量
  set file_count to count of (trash's items)
  -- 重复以下步骤，直到所有文件都被恢复
  repeat file_count times
    -- 调用recoverMyFile()函数来恢复文件
    recoverMyFile() of me
  end repeat
end tell

-- 定义recoverMyFile()函数来恢复单个文件
on recoverMyFile()
  -- 打开System Events应用程序
  tell application "System Events"
    -- 将Finder窗口置于最前面
    set frontmost of process "Finder" to true
    -- 打开垃圾桶窗口并选择第一个文件
    tell application "Finder"
      open trash
      select the first item of front window
    end tell
    -- 使用键盘快捷键“Command + Delete”来恢复文件
    tell process "Finder"
      key code 51 using command down
      delay 2 -- 延迟2秒
    end tell
  end tell
end recoverMyFile
```

      将这段代码保存在apple.script文件中，然后执行osascript apple.script即可将废纸篓中的所有文件和目录放回原处。

在执行apple.script文件时，有可能出现下面的错误：

execution error: “System Events”遇到一个错误：“osascript”不允许发送按键。 (1002)

  这个错误通常出现在使用macOS自带的Script Editor（脚本编辑器）应用程序时，它试图向某些应用程序发送按键信号但被系统阻止。

  请使用下面的步骤解决这个问题：

* 在System Preferences中找到“安全性与隐私”，然后切换到“隐私”选项卡。
* 在左侧菜单中选择“辅助功能”，然后点击右侧的锁形图标以进行更改。
* 输入管理员密码以解锁更改，并将Script Editor从列表中添加到允许应用程序列表中，如下图2所示。
* 如果问题仍然存在，请尝试退出并重新启动Script Editor应用程序。
  + ![](https://i-blog.csdnimg.cn/direct/2c939a23623044148cbe7aa4bbcf4eae.png)

           如果要想用Python完成这一切，只需要用Python自动生成apple.script文件，然后执行该文件即可，或者干脆直接在Python中执行这段代码。不过由于这段代码较长，需要分段执行，所以推荐生成apple.script文件，然后再用Python执行的方式。

    (3) 恢复Linux回收站中的文件

        Linux回收站的路径是“~/.local/share/Trash”，而回收站中每一个文件和目录都在“~/.local/share/Trash/info”目录中有一个元数据文件，文件名是filename.trashinfo，其中filename表示回收站中的文件或目录名。例如，如果回收站中有一个abc.txt文件，那么对应的元数据文件是abc.txt.trashinfo。

        元数据文件是纯文本格式，里面保存了回收站文件中的原始路径，已经被移入...