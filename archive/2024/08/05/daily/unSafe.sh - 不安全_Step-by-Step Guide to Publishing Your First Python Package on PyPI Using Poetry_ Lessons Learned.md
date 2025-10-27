---
title: Step-by-Step Guide to Publishing Your First Python Package on PyPI Using Poetry: Lessons Learned
url: https://buaq.net/go-254203.html
source: unSafe.sh - 不安全
date: 2024-08-05
fetch_date: 2025-10-06T18:00:04.320496
---

# Step-by-Step Guide to Publishing Your First Python Package on PyPI Using Poetry: Lessons Learned

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Step-by-Step Guide to Publishing Your First Python Package on PyPI Using Poetry: Lessons Learned

BackstoryRecently, I decided to create my first Python package and publish it to PyPI. After a mont
*2024-8-4 20:45:12
Author: [hackernoon.com(查看原文)](/jump-254203.htm)
阅读量:40
收藏*

---

### Backstory

Recently, I decided to create my first Python package and publish it to PyPI. After a month of writing and testing code, I finally prepared everything for publication. Because this was new for me, I encountered several pitfalls along the way, so I decided to share the steps on how you can do the same.

You can check my package on [GitHub](https://github.com/ViAchKoN/dataclass-sqlalchemy-mixins?ref=hackernoon.com) or [Pypi](https://pypi.org/project/dataclass-sqlalchemy-mixins/?ref=hackernoon.com).

**Note**: In this article, I will discuss how to create and prepare a package for publication using Poetry. Poetry automates many tasks for you. If you prefer to manually prepare the package, you can refer to the [guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/?ref=hackernoon.com).

### Prepare an Account on PyPi

First things first. You need an account. Go to [https://pypi.org/](https://pypi.org/?ref=hackernoon.com) to create the account and finish its setup.

### Generate an API Token on PyPi

To publish a package on PyPI, you will need to generate a token for your account.

Once you are registered on PyPI, go to your [account page](https://pypi.org/manage/account/?ref=hackernoon.com), scroll down to the API tokens section, and click the **Generate API token** button. Choose a name and the scope for the token.

If you don't have any projects on PyPI, you will only be able to create an account-scoped API token, which will be used to publish new packages. Save the API token. We will need it later.

### Prepare a Project

First, create a folder where the package files will be stored. Next, create a Python virtual environment. I prefer to create the virtual environment in the project's folder, but `poetry` provides the option to create it in `{cache-dir}/virtualenvs`.

```
python3 -m venv .venv

source .venv/bin/activate
```

After creating the virtual environment, we need to install and initialize `poetry`.

```
pip install poetry

poetry init
```

`Poetry` will ask you to set several settings during the initialization, which you can change later manually. As a result, a file called `pyproject.toml` will be generated.

This is the most important file, responsible for the project's operation and dependency management.

It should look something like this:

```
[tool.poetry]
name = "pypi-poetry-publish-example"
version = "0.1.0"
description = ""
authors = ["Author <[email protected]>"]
readme = "README.md"
packages = [{include = "pypi_poetry_publish_example"}]

[tool.poetry.dependencies]
python = "^3.10"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

Let's explain some fields in the file:

* `name` - is the name of the project. By default, it is the name of the folder where poetry was initialized.

* `version` - project's version. It will be used for versioning when the package will be published.

* `python` - python version required for the project.

* `build-system` - the system that is used for building source distributions or wheels from them.

* `readme` - a filename that will be used for package description. If it is set here, you need to create it in the root.

After we have prepared `poetry,` we will create a new folder called `pypi_poetry_publish_example` where package files will be stored. Inside the folder, we will create a file `core.py`.

**Important**: The name of the folder where the package files are stored should be the same as the name set in `pyproject.toml`, written in camel case.

In our case: *pypi-poetry-publish-example*(`pyproject.toml`) -> *pypi\_poetry\_publish\_example* (`folder name`)

```
# core.py
PREPEND_STR = 'prepend_'

def modify_str(string: str) -> str:
    return f'{PREPEND_STR}{string}'
```

Additionally, it is a good idea to add a `LICENSE` file. The MIT license is commonly used.

Finally, we need to save what versions of packages have been installed:

```
poetry lock
```

As a result, the project structure should look like this:

```
pypi-poetry-publish-example/
├── LICENSE
├── poetry.lock
├── pyproject.toml
├── README.md
├── pypi_poetry_publish_example/
       ├── __init__.py
       └── core.py
```

### Build and Publish the Package

Our project is ready to be published, but before that, we need to build the source and wheel archives.

To do this, we use the following command:

```
poetry build
```

Before we publish the package, we need to set the API token:

```
poetry config pypi-token.pypi pypi-XXXXXXXX
```

where `pypi-XXXXXXXX` is the API token generated in your account.

This will create the required files to be published; to upload them to Pypi, use:

```
poetry publish
```

Congratulations! Your package has been uploaded, and it can be verified by visiting the [projects page](https://pypi.org/manage/projects/?ref=hackernoon.com).

Now, it can be installed using:

```
pip install pypi-poetry-publish-example
```

There were no dependencies added in the example.

Dependencies can be added using Poetry if needed.

After installation, they will be added to `tool.poetry.dependencies` and will be required by the package.

You might have seen commands like `pip install somepackage[extra]`. This parameter will install the `extra` optional features which won't be automatically added if only the command `pip install somepackage` is applied.

To do this in your project, you need to add the `optional` flag to the dependency you want to make optional, and add it to `[tool.poetry.extras]`. The `pyproject.toml` with the optional package `pydantic` will look like this:

```
[tool.poetry]
name = "pypi-poetry-publish-example"
version = "0.1.0"
description = ""
authors = ["Author <[email protected]>"]
readme = "README.md"
packages = [{include = "pypi_poetry_publish_example"}]

[tool.poetry.dependencies]
python = "^3.10"
pydantic = {version=">=1.9", optional = true}

[tool.poetry.extras]
pydantic = ["pydantic"]

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

文章来源: https://hackernoon.com/step-by-step-guide-to-publishing-your-first-python-package-on-pypi-using-poetry-lessons-learned?source=rss
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)