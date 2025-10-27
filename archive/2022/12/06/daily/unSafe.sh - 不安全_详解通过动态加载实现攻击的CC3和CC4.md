---
title: 详解通过动态加载实现攻击的CC3和CC4
url: https://buaq.net/go-138663.html
source: unSafe.sh - 不安全
date: 2022-12-06
fetch_date: 2025-10-04T00:32:42.378473
---

# 详解通过动态加载实现攻击的CC3和CC4

<!DOCTYPE>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>unSafe.sh - 不安全</title>

    <link rel="shortcut icon" href="/static/icon.png">
    <link href="/static/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>
        body {

            padding-top: 7rem;
        }

        .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            user-select: none;
        }

        @media (min-width: 768px) {
            .bd-placeholder-img-lg {
                font-size: 3.5rem;
            }
        }

        .navbar {
            padding-bottom: 10px
        }

        a {
            text-decoration: none;
        }
    </style>

</head>

<body>

    <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
        <div class="container-fluid">
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
<span class="navbar-toggler-icon"></span>
    </button>
            <div class="collapse navbar-collapse" id="navbarCollapse">
                <ul class="navbar-nav me-auto mb-2 mb-md-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="https://unsafe.sh">unSafe.sh - 不安全</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/user/collects">我的收藏</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/?hot=true">今日热榜</a>
                    </li>

                    <li class="nav-item">
                        <a class="nav-link" href="/?gzh=true">公众号文章</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/nav/index">导航</a>
                    </li>

                    <li class="nav-item">
                        <a class="nav-link" href="/cve">Github CVE</a>
                    </li>

                    <li class="nav-item">
                        <a class="nav-link" href="/tools">Github Tools</a>
                    </li>

                    <li class="nav-item">
                        <a class="nav-link" href="/encode">编码/解码</a>
                    </li>

                    <li class="nav-item">
                        <a class="nav-link" href="/share/index">文件传输</a>
                    </li>

                    <li class="nav-item">
                        <a class="nav-link " href="https://twitter.com/buaqbot">Twitter Bot</a>
                    </li>

                    <li class="nav-item">
                        <a class="nav-link " href="https://t.me/aqinfo">Telegram Bot</a>
                    </li>

                    <li class="nav-item">
                        <a class="nav-link " href="/search/search">
                            <font color='red'>Search</font>
                        </a>
                        </a>
                    </li>

                </ul>

                <a class="nav-link " style="color: white" href="/rss.xml">Rss</a></a>
                <div class="form-check d-flex form-switch">

                    <input onchange="switchmodeBtn();" class="form-check-input" type="checkbox" role="switch" name="darkmode" id="darkmode">
                    <label style="color:#fff" class="form-check-label" for="flexSwitchCheckDefault">黑夜模式</label>
                </div>
            </div>
        </div>
    </nav>
    <script src="/static/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
    <script>
        var uri = location.href;
        var hour = new Date().getHours();

        function includeCss(filename) {
            var head = document.getElementsByTagName('head')[0];
            var link = document.createElement('link');
            link.href = filename;
            link.rel = 'stylesheet';
            link.type = 'text/css';
            head.appendChild(link)
        }

        function switchmode(mode) {
            if (uri.indexOf("go-") != -1) {
                includeCss("/static/css/" + mode + "_content.css?ver=0.03")
            } else if (uri.indexOf("/search/search") != -1) {
                includeCss("/static/css/search_" + mode + ".css?ver=0.03")
            } else {
                includeCss("/static/css/" + mode + ".css?ver=0.03")
            }
        }

        function AutoMode() {
            var mode = localStorage.getItem("mode") ? localStorage.getItem("mode") : 'dark';
            if (mode) {
                if (mode == 'light') {
                    $("#darkmode").prop('checked', false)
                } else {
                    $("#darkmode").prop('checked', true)
                }

                switchmode(mode);
                return;
            }
            if (hour > 18 || hour < 8) {
                switchmode("dark");
            } else {
                switchmode("light");
            }
        }
        AutoMode();

        function switchmodeBtn() {
            console.log("switch mode btn")
            var mode = localStorage.getItem("mode") ? localStorage.getItem("mode") : "dark";
            if (mode == 'light') {
                $("#darkmode").prop('checked', true)
                mode = "dark"
            } else {
                $("#darkmode").prop('checked', false)
                mode = "light"
            }
            localStorage.setItem("mode", mode);
            location.reload()
            console.log("change mode ", mode)

        }
    </script>

<div class="list-group list-group-checkable">
    <div class="container">
        <div class="row">
            <div class="col-md-4"></div>
            <div class="col-md-4">
                <br><br>
                <h1>跳转中</h1><br>
                <h3 id="redirect">Redirect.</h3>
            </div>
            <div class="col-md-4"></div>

        </div>
    </div>
</div>
<script src="/addview?id=138663"></script>
<script>
    setTimeout(() => {
        window.location.href = "https:\/\/xz.aliyun.com\/t\/11923";
    }, 5000);
    setInterval(function() {
        $('#redirect').html($('#redirect').html() + '.')
    }, 750)
</script>
<script charset="UTF-8" id="LA_COLLECT" src="//sdk.51.la/js-sdk-pro.min.js"></script>
<script>LA.init({id:"KiRUVDOwqCVHgDgf",ck:"KiRUVDOwqCVHgDgf"})</script>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/vcd15cbe7772f49c399c6a5babf22c1241717689176015" integrity="sha512-ZpsOmlRQV6y907TI0dKBHq9Md29nnaEIPlkf84rnaERnq6zvWvPUqr2ft8M1aS28oN72PdrCzSjY4U6VaAw1EQ==" data-cf-beacon='{"version":"2024.11.0","token":"9f0d2ce46e3f46df9a41e510c66656c6","r":1,"server_timing":{"name":{"cfCacheStatus":true,"cfEdge":true,"cfExtPri":true,"cfL4":true,"cfOrigin":true,"cfSpeedBrain":true},"location_startswith":null}}' crossorigin="anonymous"></script>
