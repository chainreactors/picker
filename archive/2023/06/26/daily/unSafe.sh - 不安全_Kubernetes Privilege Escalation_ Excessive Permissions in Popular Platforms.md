---
title: Kubernetes Privilege Escalation: Excessive Permissions in Popular Platforms
url: https://buaq.net/go-170227.html
source: unSafe.sh - 不安全
date: 2023-06-26
fetch_date: 2025-10-04T11:44:56.325146
---

# Kubernetes Privilege Escalation: Excessive Permissions in Popular Platforms

<!DOCTYPE>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Kubernetes Privilege Escalation: Excessive Permissions in Popular Platforms</title>

    <meta content='https://unsafe.sh' name='twitter:domain' />
    <meta content='Kubernetes Privilege Escalation: Excessive Permissions in Popular Platforms' name='twitter:title' />
    <meta content='summary_large_image' name='twitter:card' />
    <meta content='https://unsafe.sh/go-170227.html' property='og:url' />
    <meta content='' name='twitter:image' />
    <meta content='' property='og:image' />
    <meta name="description" content="Kubernetes Privilege Escalation: Excessive Permissions in Popular Platforms">
    <meta name="keywords" content="000000,0000000000,65535,cmyk,00000">

    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="https://unsafe.sh">
    <meta property="og:title" content="Kubernetes Privilege Escalation: Excessive Permissions in Popular Platforms">

    <meta property="og:image" content="">
    <meta name="promote_title" content="Kubernetes Privilege Escalation: Excessive Permissions in Popular Platforms" />
    <meta name="promote_image" content="" />

    <meta name="weibo:article:url" content="https://unsafe.sh/go-170227.html" />
    <meta name="weibo:article:title" content="Kubernetes Privilege Escalation: Excessive Permissions in Popular Platforms" />

    <meta name="weibo:article:image" content="" />

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

<meta keywords="000000,0000000000,65535,cmyk,00000">
<link href="/static/css/content.css" rel="stylesheet">
<link href="/static/css/imagebox.css" rel="stylesheet">

<script>
    var banners = ['https://8aqnet.cdn.bcebos.com/0f0aa4e8701b61b94ee828a85bc7d6a8.jpg', 'https://8aqnet.cdn.bcebos.com/1375355fe3b3ebe88a250f39f46d9de0.jpg',
        'https://8aqnet.cdn.bcebos.com/bb7c59fa0a912c0d572f27af0ed2e289.jpg', 'https://8aqnet.cdn.bcebos.com/de131d126200a811d7d6d1684c065227.jpg',
        'https://8aqnet.cdn.bcebos.com/0c7530e197adfb561fd5e4445dc18c04.jpg', 'https://8aqnet.cdn.bcebos.com/ee983818be7c64358187fa539f924d4d.jpg',
        'https://8aqnet.cdn.bcebos.com/b7ed5a21a18f43594282985c6d5ef3c6.jpg', '...