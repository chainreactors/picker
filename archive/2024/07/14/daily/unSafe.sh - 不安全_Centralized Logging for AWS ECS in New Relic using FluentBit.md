---
title: Centralized Logging for AWS ECS in New Relic using FluentBit
url: https://buaq.net/go-250430.html
source: unSafe.sh - 不安全
date: 2024-07-14
fetch_date: 2025-10-06T17:40:49.045090
---

# Centralized Logging for AWS ECS in New Relic using FluentBit

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

![](https://8aqnet.cdn.bcebos.com/4588562f088d7e869e547f8b496c5ead.jpg)

Centralized Logging for AWS ECS in New Relic using FluentBit

In this article, I want to share my experience setting up logging for our project. We transitioned f
*2024-7-13 23:47:25
Author: [hackernoon.com(查看原文)](/jump-250430.htm)
阅读量:9
收藏*

---

In this article, I want to share my experience setting up logging for our project. We transitioned from using ELK to New Relic for log storage. I'll explain how we chose our log delivery method, the options we considered, and why we settled on our current solution. I want to emphasize that this is not an advertisement for New Relic—you can use any log storage you prefer. The main focus will be on configuring Fluent Bit, which we used for log forwarding.

In our AWS ECS project, we manage a dozen EC2 instances running various microservices. We use Sentry to collect errors from all applications. Until recently, we used an rsyslog-logstash-ELK stack for log collection. However, we encountered several issues: ELK was deployed on a separate instance and eventually stopped working due to resource shortages and insufficient configuration. Logstash often stopped under high load due to memory leaks. Additionally, this stack is not suitable for use with Fargate after transitioning from EC2.

We needed a solution that could effectively work on both EC2 and Fargate, be easy to configure, and support sending logs to New Relic. Rsyslog does not support integration with New Relic, and Fluentd needs to be run on each instance. As a result, we chose the lightweight and versatile Fluent Bit.

My solution looks as follows: each ECS service in the task definition is paired with a log router container. This container is configured to forward logs to a specific storage and collects logs only from the specific service. Thus, each service has its own log router.

![](https://hackernoon.imgix.net/images/cSVX7SdKsnY4bRV3KgKzzDctKvD2-ju933g3.png?auto=format&fit=max&w=1080)

This method of log forwarding is essentially described in the documentation. However, none of the suggested options fully met my requirements, so I decided to document my solution in this article. The requirements for implementation were as follows:

1. Simple integration with the service and log capture.
2. Easy configuration of Fluent Bit that would apply to all log routers at once.
3. Centralized storage of log storage authorization information.

> The following two parts are not necessary if you do not plan to configure parsers for Fluent Bit. I configured them so that Fluent Bit would combine multiline logs into a single message, which required creating a custom Fluent Bit image. For information on using the base image and a configuration stored on AWS S3, you can refer to [this guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/firelens-taskdef.html?ref=hackernoon.com).

### Setting Up the Fluent Bit Docker Image

Let's start with the Fluent Bit Docker image, which we will add to the task definition configuration. According to the official [New Relic documentation](https://docs.newrelic.com/docs/logs/forward-logs/aws-firelens-plugin-log-forwarding/?ref=hackernoon.com), the task definition configuration needs to include a specific Fluent Bit image configured for New Relic and specify the AWS region, such as us-east-2. For my image, I used the image from the documentation for a specific region, although you can also use the official image from Docker Hub: [amazon/aws-for-fluent-bit](https://hub.docker.com/r/amazon/aws-for-fluent-bit?ref=hackernoon.com).

```
FROM .../logging-firelens-fluentbit

COPY fluent-bit.conf /fluent-bit/alt/fluent-bit.conf
COPY parsers.conf /fluent-bit/etc/

CMD ["/fluent-bit/bin/fluent-bit", "-e", "/fluent-bit/bin/out_newrelic.so", "-c", "/fluent-bit/alt/fluent-bit.conf"]
```

I created the following Dockerfile. Here, we inherit from one of the base images, copy our configurations and parsers (which will be discussed below), and in the startup command, we connect the plugin for New Relic.

### Configuring and Creating Parsers for Fluent Bit

Now, we need to configure Fluent Bit. This is done using the `fluent-bit.conf` and `parsers.conf` files.

fluent-bit.conf

```
[SERVICE]
    Flush        1
    Grace        30
    Log_Level    debug
    parsers_file /fluent-bit/etc/parsers.conf

[INPUT]
    Name forward
    unix_path /var/run/fluent.sock
    Mem_Buf_Limit 27MB

[INPUT]
    Name forward
    Listen 0.0.0.0
    Port 24224
    Mem_Buf_Limit 27MB

[INPUT]
    Name tcp
    Tag firelens-healthcheck
    Listen 127.0.0.1
    Port 8877
    Mem_Buf_Limit 27MB

[OUTPUT]
    Name null
    Match firelens-healthcheck

[OUTPUT]
    Name newrelic
    Match *
    apiKey ${apiKey_0}

[FILTER]
    Name modify
    Match *
    Add environment ${CLUSTER}
    Add app ${APP}

[FILTER]
    Name                multiline
    Match               *
    multiline.key_content log
    multiline.parser    python-multiline-ssl

[FILTER]
    Name            grep
    Match           *
    Exclude         log ^.*SSL with verify_certs=False.*$
```

parsers.conf

```
[MULTILINE_PARSER]
    Name            python-multiline-ssl
    Type            regex
    flush_timeout   1000
    rule "start_state" "/^.*(http_urllib3.py).*(verify_certs=False).*/" "cont"
    rule "cont" "/^.*SSL.*$/" "cont"
```

I mainly copied the settings from the [Fluent Bit documentation](https://docs.fluentbit.io/manual/administration/configuring-fluent-bit/classic-mode/configuration-file?ref=hackernoon.com), adjusting only for loading parser files, sending logs to New Relic, and setting up filters. Let me explain the filters in more detail. In my case, they are used for:

1. Adding metadata to the log, such as environment and app. These data are taken from environment variables, which I will pass when configuring the task definition.
2. Defining multiline outputs. With parsers, you can determine that several lines of a log belong to one message, such as a multiline warning/error output from Python.
3. Ignoring messages that contain a specific set of data.

The `parsers.conf` file contains rules for determining that multiple lines of a log belong to one message. Here, we define a named parser, which is then connected to the multiline filter.

Next, we build the image with the `docker build` command and push it to the Docker repository with the `docker push` command, tagging it as `latest`. Now, this image can be used in the task definition.

### Configuring the AWS ECS Task Definition

The last step is to configure the task definition.

```
{
    "essential": true,
    "name": "app",
		"logConfiguration": {
		    "logDriver": "awsfirelens",
		    "options": {
		        "Name": "newrelic"
		    },
		    "secretOptions": [
		        {
		            "name": "apiKey",
		            "valueFrom": "arn:aws:secretsmanager:xxxxxx"
		        }
		    ]
		}
},
{
		"essential": true,
    "name": "app-log-router",
    "image": "your_repo/fluent-bit:latest",
    "cpu": 0,
    "memoryReservation": 50,
    "environment": [
        {
            "name": "CLUSTER",
            "value": "prod"
        },
        {
            "name": "APP",
            "value": "cms"
        }
    ],
    "firelensConfiguration": {
        "type": "fluentbit"
    }
}
```

Within this task definition, there are two containers that run together. If either container fails to start, the entire service does not start, which is logically sound. The New Relic API key for access is passed through AWS Secret Manager. Additionally, environment variables are populated with metadata added earlier in the Fluent Bit ...