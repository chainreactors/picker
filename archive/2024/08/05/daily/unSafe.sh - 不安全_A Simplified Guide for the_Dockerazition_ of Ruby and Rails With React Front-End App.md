---
title: A Simplified Guide for the"Dockerazition" of Ruby and Rails With React Front-End App
url: https://buaq.net/go-254202.html
source: unSafe.sh - 不安全
date: 2024-08-05
fetch_date: 2025-10-06T18:00:00.405350
---

# A Simplified Guide for the"Dockerazition" of Ruby and Rails With React Front-End App

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

![](https://8aqnet.cdn.bcebos.com/29d2bd4d35c033741d8d4219d06f4d56.jpg)

A Simplified Guide for the"Dockerazition" of Ruby and Rails With React Front-End App

Dockerizing your Ruby on Rails with a React front-end application can dramatically improve your dev
*2024-8-4 22:0:14
Author: [hackernoon.com(查看原文)](/jump-254202.htm)
阅读量:8
收藏*

---

![](https://hackernoon.imgix.net/images/5KaAW2aPoBW6JARCP3Gc0MjAqGf2-db82sup.png?auto=format&fit=max&w=1920)

Dockerizing your Ruby on Rails with a React front-end application can dramatically improve your development workflow and deployment process. By creating a standardized environment for your app, you ensure consistent behavior across different stages of development, testing, production, and even across different systems. In fact, it is designed to minimize issues related to system differences. This guide will walk you through the essential steps to get your Rails and React app running smoothly in Docker containers.

![Docker to the rescue](https://hackernoon.imgix.net/images/5KaAW2aPoBW6JARCP3Gc0MjAqGf2-da92s8c.png?auto=format&fit=max&w=2048)

## **Why Dockerize an Application?**

* **Consistency Across Environments**:
  + Docker ensures that the application runs the same way regardless of where it is deployed, whether on a developer's machine, a testing environment, or a production server. This consistency is achieved by containerizing all dependencies and configurations.
* **Dependency Management**:
  + Docker containers include all necessary dependencies for the application to run. This means that variations in system libraries or missing dependencies on different systems do not affect the application's functionality.
* **Isolation**:
  + Docker containers run in isolation from each other and from the host system. This isolation prevents conflicts between different applications and their dependencies on the same system.
* **Portability**:
  + Docker containers can be easily moved and run on any system that supports Docker, whether it is a local machine, a cloud service, or a dedicated server. This makes the application highly portable and flexible in terms of deployment.

NB: [A knowledge of Docker syntax is required](https://docs.docker.com/reference/dockerfile/?ref=hackernoon.com#parser-directives)

Dockerization involves two key concepts: images and containers. Images serve as blueprints for containers, containing all the necessary information to create a container, including dependencies and deployment configurations. A container is a runtime instance of an image, comprising the image itself, an execution environment, and runtime instructions. Docker in general, establishes a standard for shipping software.

To explain Docker with a simple analogy: think of containers as the shipping containers in a yard, images as the items placed inside these containers, and the shipping vessel as the system on which the containers run.

Whenever you set up and build your application, certain environment configurations are necessary. For example, you cannot run a Rails application without a Ruby environment installed on your system. Similarly, you cannot run a React application without `Node.js`, and you cannot install React packages without a Node package manager like `npm` or `Yarn` etc.

Since the container runs in isolation from the user’s system, we are going to make all these packages available in our container just like we would have done in case we built it directly on our system, thus, the container will act as a system on it own, like a virtual machine. There are differences between docker and virtual machine but this example is just to explain further.

Now, let’s go ahead and dockerize the Rails application. To do this, we will need three files in our Rails application: a `Dockerfile`, a `docker-compose.yml`, and a `bin/docker-entrypoint`. Let’s examine each of these files in detail.

**NB:** [A knowledge of Docker syntax is required](https://docs.docker.com/reference/dockerfile/?ref=hackernoon.com#syntax)

## **Dockerfile**

The `Dockerfile` is a blueprint for creating a Docker container. It contains a series of instructions that Docker uses to build an image, which can then be used to run containers. Let's break down a `Dockerfile` for a Ruby on Rails and React application:

### . Base Image

```
ARG RUBY_VERSION=3.1.4
FROM ruby:$RUBY_VERSION
```

* `ARG RUBY_VERSION=3.1.4`: Defines a build argument named `RUBY_VERSION` with a default value of `3.1.4`. This can be overridden at build time.

* `FROM ruby:$RUBY_VERSION`: Uses the `ruby` base image with the version specified by `RUBY_VERSION`. This sets up the container with the Ruby runtime. Just like I mentioned earlier, to run a Rails application, you need to have Ruby installed.

### 2. Install Dependencies

```
RUN apt-get update -qq && \
    apt-get install -y build-essential libvips bash bash-completion libffi-dev tzdata postgresql curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man
```

* `apt-get update -qq`: Updates the package list from the repositories, with `-qq` for quiet output.

* `apt-get install -y` **...**: Installs various packages:
  + `build-essential`: Essential packages for building software (like GCC).
  + `libvips`: Library for image processing.
  + `bash`, `bash-completion`: Bash shell and its auto-completion.
  + `libffi-dev`: Foreign Function Interface library.
  + `tzdata`: Time zone data.
  + `postgresql`: PostgreSQL database client.
  + `curl`: Tool to transfer data from URLs.
* `apt-get clean`: Cleans up the local repository of retrieved package files.

* `rm -rf /var/lib/apt/lists/ /usr/share/doc /usr/share/man`: Removes package lists and documentation to reduce image size.

### 3. Install Node.js and Yarn

```
RUN curl -fsSL https://deb.nodesource.com/setup_current.x | bash - && \
    apt-get install -y nodejs && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update && \
    apt-get install -y yarn
```

* `curl -fsSL https://deb.nodesource.com/setup_current.x | bash -`: Downloads and runs the NodeSource setup script to install Node.js.

* `apt-get install -y nodejs`: Installs Node.js.

* `curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -`: Adds the Yarn GPG key to verify its packages.

* `echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list`: Adds Yarn's repository to the list of sources.

* `apt-get update && apt-get install -y yarn`: Updates the package list and installs Yarn.

### 4. Environment Variables

```
ENV NODE_OPTIONS=--openssl-legacy-provider
```

* `ENV NODE_OPTIONS=--openssl-legacy-provider`: Sets an environment variable to enable legacy OpenSSL support for Node.js.

### 5. Set Working Directory

```
WORKDIR /rails
```

* `WORKDIR /rails`: Sets the working directory for subsequent instructions to `/rails`.

### 6. Build Arguments and Environment Variables

```
ARG RAILS_ENV
ENV RAILS_ENV=$RAILS_ENV
```

* `ARG RAILS_ENV`: Defines a build argument named `RAILS_ENV` for specifying the Rails environment (like `development`, `test`, `production`).

* `ENV RAILS_ENV=$RAILS_ENV`: Sets the environment variable `RAILS_ENV` to the value of the build argument.

### 7. Install Application Gems

```
COPY Gemfile Gemfile.lock ./
RUN bundle install
```

* `COPY Gemfile Gemfile.lock ./`: Copies the `Gemfile` and `Gemfile.lock` to the working directory.

* `RUN bundle install`: Installs Ruby gems specified in the `Gemfile`.

### 8. Ins...