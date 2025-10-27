---
title: 某多多anti-ceontent核心算法
url: https://forum.90sec.com/t/topic/2225
source: 90Sec - 最新话题
date: 2023-03-07
fetch_date: 2025-10-04T08:46:19.070760
---

# 某多多anti-ceontent核心算法

[90Sec](/)

# [某多多anti-ceontent核心算法](/t/topic/2225)

[账号审核](/c/account/11)

[yizhiyan](https://forum.90sec.com/u/yizhiyan)

2023 年3 月 6 日 13:47

1

某多多的ant-content核心算法解密版本，耗时4天3夜，并非网上直接把代码扣下来的。完全解密版本

### 解密方法和代码

代码是用ast来解密的。利用babel处理，解密一部分+手动修复代码。
AST相关的教程和文档

```
https://steakenthusiast.github.io/
https://evilrecluse.top/Babel-traverse-api-doc/
https://astexplorer.net/
```

以下代码不适用于所有加密

```
const fs = require("fs");
const { parse } = require("@babel/parser");
const traverse = require("@babel/traverse").default;
const generator = require("@babel/generator").default;
const t = require("@babel/types");
const beautify = require("js-beautify");

const jscode = fs.readFileSync("./pdd_ant2.js").toString("utf-8")

let ast = parse(jscode);

function node_eq(node, node2) {
    if (node2.type == "VariableDeclarator") {
        node2 = node2.init;
    }
    return node.start == node2.start && node.end == node2.end;
}

function var_get_referencePaths(nodePath) {
    const context = nodePath.parentPath.get("left").context;
    const bindings = context.scope.bindings[nodePath.parent.left.name];
    return bindings.referencePaths;
}
function get_scope_binding(path) {
    if (["callee", "MemberExpression"].includes(path.key) || path.get("object").node) {
        return path.scope.getBinding(path.get("object").node.name)
    } else if (path.node.name) {
        return path.scope.getBinding(path.node.name)
    } else if (path.get("id").node) {
        return path.scope.getBinding(path.get("id").node.name)
    } else {
        console.log("没有binding")
    }
}

//查找当前变量所有使用的地方
function relyon_var(referencePaths, codes = new Map()) {
    //作用域
    for (let i = 0; i < referencePaths.length; i++) {
        //使用的path
        const nodePath = referencePaths[i];
        //在当前方法内直接返回不管
        // if (node_eq(nodePath.node, node)) {
        //     continue;
        // }
        //说明是一个赋值操作 var n=u;
        if (["right"].includes(nodePath.key)) {
            //抽离关于n的代码
            const varScope = var_get_referencePaths(nodePath);
            relyon_var(varScope);
            // const id2 = nodePath.node.start + "_" + nodePath.node.end;
            // codes.set(id2, nodePath)
            // //查找当前nodepath使用的引用
            // const context = nodePath.parentPath.get("left").context;
            // const bindings = context.scope.bindings[nodePath.parent.left.name];
            // const referencePaths = bindings.referencePaths;
            // //引用
            // for (let index = 0; index < array.length; index++) {
            //     const element = array[index];

            // }
            // console.log(binds.referencePaths)
        }
    }
}

function encode1(arg1, arg2) {
    var u = ["fSohrCk0cG==", "W4FdMmotWRve", "W7bJWQ1CW6C=", "W5K6bCooW6i=", "dSkjW7tdRSoB", "jtxcUfRcRq==", "ALj2WQRdQG==", "W5BdSSkqWOKH", "lK07WPDy", "f8oSW6VcNrq=", "eSowCSkoaa==", "d8oGW7BcPIO=", "m0FcRCkEtq==", "qv3cOuJdVq==", "iMG5W5BcVa==", "W73dVCo6WPD2", "W6VdKmkOWO8w", "zueIB8oz", "CmkhWP0nW5W=", "W7ldLmkSWOfh", "W5FdIqdcJSkO", "aCkBpmoPyG==", "l27dICkgWRK=", "s05AWR7cTa==", "bttcNhdcUW==", "gJldK8kHFW==", "W5Sso8oXW4i=", "FgC0W7hcNmoqwa==", "xmkPhdDl", "e14kWRzQ", "BNFcVxpdPq==", "z1vadK0=", "W7yOiCk2WQ0=", "qLb7lg0=", "t8o6BwhcOq==", "gmk6lYD9WPdcHSoQqG==", "oqldGmkiCq==", "rmo+uKlcSW==", "dSoIWOVdQ8kC", "iXSUsNu=", "W5ipW4S7WRS=", "WPtcTvOCtG==", "A3CcAmoS", "lCotW6lcMba=", "iuGzWPLz", "WQVdPmoKeSkR", "W4ydoCkqWQ4=", "jCobW47cNXC=", "W4tdJCkNWOCJ", "hCo/W7ZcSJ8=", "BNuZW6NcMG==", "b8kFW6hdN8oN", "W4SpoCkXWQK=", "cXddOmkDFa==", "W63dHSoyWQft", "W6ldSmk0WRj4", "A2bHWOtcHeeMyq==", "f3VcSSk/xG==", "qg1u", "ftyivga=", "DCkhpsfe", "WR3cKmo3oMWEw8kK", "yev3", "W4xdMKSejbm=", "W797WOL7W4m=", "W6xdOCkKWQXw", "gcCUye0=", "W7WXkmomb8kT", "c8kIesD0", "WOTpEW==", "ySo3E8oVWPy=", "iNyhW5lcNLNcG8kYWQu=", "W7JdMSkfWRnD", "FfijW5tcHW==", "xCokW54Zzq==", "W77dUsi=", "W5FdHfa6eq==", "E1FcQvVdSG==", "eZ/dNCo4AG==", "CgPmWQZdKa==", "A8oLECoJWPS=", "oCoSW7VcTJC=", "mCoADa==", "W7DXuSouDq==", "ic3dQCo8ua==", "rN3cIa==", "W6/dJ8kPWRGQ", "W4xdLYlcPmkc", "F3JcPvZdLa==", "xCk8iHn4", "qg15", "W5/dL8oOWPr4", "hW41C3C=", "sSoZzwxcPW==", "ywdcUvNdUW==", "t0TzWQpdIG==", "lv7dJSoIjq==", "W5Tzxq==", "W6DnWQK=", "W5mGaCkFWRC=", "W6LmWO5+W6C=", "WR7dQmoJa8k+", "emkFW4ddOmob", "imk8imoNEa==", "W4ZdP8kaWPvc", "F8k4WO40W4e=", "cSoHE8k9cG==", "jw4TW5dcSW==", "wuJcOKRdTa==", "swNcQx/dGG==", "aCkSiCoMEq==", "W6pdS8owWQTH", "WRFdQmonjmkT", "cKBdGCkpWOm=", "oCoWW4VcPIa=", "WQddSSoUjmks", "c8kdW5JdM8oE", "W7b0AGvl", "sCk4WOylW60=", "nXNdSmkXvW==", "W67dRSkjWOqj", "W44EcCohW6O=", "W6ddPmkpWRHN", "W7tdVIVcOSkR", "qg3dVG==", "W7Ofcmofda==", "WRDmW5VcLq==", "CSoRW4W4Aq==", "mmo0WP3dVmkj", "i8omW6ZcPd8=", "CSkaWQyvW4m=", "ACkMWQCLW4q=", "W5pdOCk0WRv3", "W7yDW44SWP8=", "WRP8W5dcNmkd", "ymkNaID5", "cfeTWRT6", "W6WdbmkmWO0=", "eSo3WQldVCkU", "W5flwZrl", "WPVcTe4tWQu=", "DuCPumok", "hLpcKCksqXe=", "g3hdUCkoWRu=", "sL0sW6JcPW==", "lf7dL8oOpG==", "w8k4WPWJW7u=", "i08mW5dcUW==", "kb/dU8klsW==", "WOhcMSoW", "W5LnfG==", "F8kJWQmxW6m=", "W5ldU0CDca==", "eKRdKmkoWPG=", "tmouW60=", "gSkrW7JdVSor", "WPNcP8oc", "DhLAmLW=", "sSo0EfdcQq==", "W6ygW689WQq=", "W6CPimkIWQa=", "WRJdLmoynSkY", "W5iimCkDWRa=", "oMhdN8kPWRHV", "eNqQWQHn", "bmkakSoHW4u=", "W4PxEbvN", "WQhcQxSWyW==", "xCoKEW==", "guBcISk2yG==", "nviRW4BcSq==", "m3tcVmkXCJ9YWQyXd8kuWQfJW71fWPmnWRj+WR1tW6WbW4PDdCkrkLbDs8ozWR4gySoyv20rWO3dJJpdIh9DWPhcGCoctKFcN8kTW6nHvbLRkg9MeKhdHCoP", "W7iZfmolW4q=", "p1JdGSk4WPW=", "ns3cTuhcMSk6u8kj", "q8kmhr5p", "lWCxtKW=", "pmk+hSoYFG==", "bdFdKmkIwa==", "WR/cMSoL", "csCy", "W7BdKCkmWPfO", "tCkeWPyXW70=", "smkVWRK=", "dNFdQSokiq==", "W5OyoCoLW5O=", "W4RcIZ0xW5hdPCkaWPddO0aoE8oCwXVcSgbVtWbqW6u=", "iKNdK8khWRa=", "WQtdQCommSkg", "W6ddU8k1WQ94", "ASoXAMRcHG==", "gMhdKCoBna==", "eCk5mSoEW6K2v8octbK=", "pmo+Fmkfea==", "f3y8WPL0Ex4=", "oSkmm8oczq==", "W7ldK8oWWRnrW6WtqMG0W7/cMxbU", "W7uwdmofbG==", "A8oqyudcPG==", "s8oHt3FcTq==", "a8okBCkAdq==", "W7mvg3OI", "E8kLWR0dW7i=", "W78qhKSF", "W6XMWRHsW6K=", "hCoyzSk7fa==", "WQNcKSoHp1S=", "oCkaiCocW6i=", "bSoEW5ZcVXq=", "W5pdVCkHWRj3", "eehdNSoGhG==", "W4VdTmkhWRO=", "W73dMte=", "bqBcJelcTG==", "WOpcKLXWBa==", "W7uRa0OKnwpdRmoq", "WO3cKSoHW7C4", "WPRcOCofl0i=", "BxvOWPhcSa==", "hwK0W7tcJq==", "BMOjW5lcGq==", "cmouWONdUmk8", "E8k9WQyjW7NdNa==", "WRNcQSoFi0S=", "zLTHWPpcUW==", "WRPjW7BcLCkB", "BLRcLMddLW==", "s8kzWOiiW5m=", "W40mW4uqWP8=", "i13cMCk7Ea==", "WQBcLMupWOu=", "x8o2xmoD", "hCkBcCoLvW==", "FmkEWRShW5q=", "W58ikmo+W7K=", "W4KehmkSWOG=", "WQZcLCod", "WQtcHgXHCa==", "W4ldRbpcSmkY", "r8oKW5ukr0e+gW==", "dSkjW4FdLCoY", "cGa6Ee4=", "W69pymoVuW==", "WQRcSCo7i0i=", "W5RdICoWWQPaW70ode4=", "cfiNWODs", "W7rzWPr/W4u=", "ySkuecz+", "W4qsW70WWOq=", "W5VdS8kmWPXz", "W44jW7W=", "pxRcGW==", "ye5hngpdUa==", "WRRcQfT0va==", "WQxcImouW7CY", "qLRcJKddTa==", "p8o6q8kUdW==", "W4nlWRLvW6W=", "p3hdQ8kzWOe=", "W4eFeCojW5W=", "W43dNCoMWRG=", "nNCqW7lcQW==", "FCoqw3dcUq==", "W4BdGSkKWQ8+", "rmo8q1/cKW==", "D0assmov", "f0eQWODU", "nJXVfCo5W6VcVIniWPKKcCkpWO0fW63dNI4fWPziiSkWEmowWO12AKqNWQvPyCkMmb8aCConW7ddQCkmxs3cG3xdJuuMW7FdJCoqWQndsmk9WQzzW5mgWP/cUHmx", "pCoRymkabCoqta==", "i2xdImk+", "owFdVSkkWOm=", "WPNcK1H+Ca==", "W4FdKJxcICkP", "W4hdNSkuWO4=", "W7Gol8oAW6O=", "W61RWRrOW4y=", "W7qAn8ksWQK=", "WPVcRvWNWOG=", "xmoyrwFcQW==", "WOz7W4hcRSkB", "l1yQW5RcSW==", "zvJcQvZdNa==", "W4hdPSobWPvy", "nWldKCoIvG==", "CeTyh3K=", "pa/cVexcLG==", "cmk0W6JdUSoK", "AwSxW5ZcHq==", "jIpcKfdcOW==", "W5r5WQXpW74=", "n8k1mmoHW4G=", "xe4JW7FcMW==", "hmolw8kViW==", "gfutW6hcSG==", "hflcVSkzrW==", "jZpcRN/cRq==", "W7tdV8kF", "ig0UW7VcLW==", "b03dGCkBWP0=", "nYFcPW==", "W4ueW6StWP0=", "W4BdN8ogWR9D", "qe89qCo3", "W68dgmkSWR4=", "Ae0FsmoD", "pSoVECkojG==", "W6aplSoBfG==", "mq/dR8omya==", "amkMiCojW40=", "xN5GWPVcJa==", "W67dJmk4WQji", "fxRcVCk7yG==", "fSkLoSoLW7a=", "a8oCWPJdP8kt", "e8o0WRxdI8kv", "ChO3W6NcMa==", "awVdPmkGWO0=", "nCk0W6pdMCod", "W4xdP8kOWO5J", "lSowxSk0fW==", "js/cPwVcTW==", "WOJdRmo9amkt", "nsRcULdcUmkH", "gCkIW4FdLmoF", "DmovW7erzG==", "cSoFD8kfeq==", "WR...