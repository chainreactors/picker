---
title: 【Web逆向】某OF网站的OB解密及DRM过校验思路(上)
url: https://mp.weixin.qq.com/s?__biz=MjM5Mjc3MDM2Mw==&mid=2651140842&idx=1&sn=f53fa138714cf11b8a935f2f3e3114be&chksm=bd50a2be8a272ba8c990f6f62e2525037deef2b4418714d707d4ef692ee7d4c6b36438a73bad&scene=58&subscene=0#rd
source: 吾爱破解论坛
date: 2024-07-06
fetch_date: 2025-10-06T17:43:50.868459
---

# 【Web逆向】某OF网站的OB解密及DRM过校验思路(上)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJl9l1BVE6U8uVxzjq9IQgOjZgt6xR1ia5pFV8BUia4w0Q9ccBmDT4Mcu8ogCtddvqFJaxP2CueMMIA/0?wx_fmt=jpeg)

# 【Web逆向】某OF网站的OB解密及DRM过校验思路(上)

原创

吾爱pojie

吾爱破解论坛

**作者****论****坛账号：李恒道**

# 前言

感谢videohelp论坛larley大神的解答！
感谢吾爱破解论坛@涛之雨大神的帮助

# 正文

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJl9l1BVE6U8uVxzjq9IQgOBh24bicxpIWpeUIpbKCeQnZ0OVGptibMSYsbK2VfOuUicHhNac1icjxy9Q/640?wx_fmt=png&from=appmsg)

首先第一层是标准的OB加密
我们先大概规整一下代码

```
 复制代码 隐藏代码
    traverse(ast, {
        CallExpression(path) {
            if (path.node.arguments.length === 2) {
                const type0 = path.node.arguments[0].type
                const type1 = path.node.arguments[1].type
                const isLikelyNumber = (type) => {
                    return type === 'UnaryExpression' || type === 'NumericLiteral'
                }
                if ((type0 === 'StringLiteral' && isLikelyNumber(type1)) || (type1 === 'StringLiteral' && isLikelyNumber(type0))) {
                    const funcBinding = path.scope.getBinding(path.node.callee.name)
                    const funcNode = funcBinding.path.node
                    if (funcNode?.params?.length !== 2) {
                        return
                    }
                    if (funcNode.body.body.length !== 1) {
                        return
                    }
                    if (funcNode.body.body[0].type !== 'ReturnStatement') {
                        return
                    }
                    const funcArgs0 = funcNode.params[0].name
                    const funcArgs1 = funcNode.params[1].name
                    const bodyCallArgs = funcNode.body.body[0].argument.arguments
                    let isSwap = false
                    for (let index = 0; index < bodyCallArgs.length; index++) {
                        const item = bodyCallArgs[index];
                        if (item.type === 'Identifier') {

                            if (item.name === funcArgs0 && index === 1) {
                                isSwap = true
                            } else if (item.name === funcArgs1 && index === 0) {
                                isSwap = true
                            }
                            break;
                        }
                    }
                    const handleExpression = (bodyExpress, argsIdentifier) => {
                        if (bodyExpress.type !== 'BinaryExpression') {
                            return argsIdentifier
                        }
                        const handleIdentifier = (item) => {
                            if (item.type !== 'Identifier') {
                                return item
                            } else {
                                return argsIdentifier
                            }
                        }
                        const numAst = types.binaryExpression(bodyExpress.operator, handleIdentifier(bodyExpress.left), handleIdentifier(bodyExpress.right))
                        const numResult = eval(generator(numAst).code)
                        return types.numericLiteral(numResult)
                    }
                    const firstIdentifier = path.node.arguments[0]
                    const secondIdentifier = path.node.arguments[1]
                    let newCalleeArgs = [handleExpression(bodyCallArgs[0], isSwap ? secondIdentifier : firstIdentifier), handleExpression(bodyCallArgs[1], isSwap ? firstIdentifier : secondIdentifier)]
                    let newNode = types.callExpression(funcNode.body.body[0].argument.callee, newCalleeArgs);
                    path.replaceInline(newNode)
                }
            }
        },
    });
```

然后获取解密的函数，这里因为比较偷懒，所以直接使用了正则表达式计算关键函数

```
 复制代码 隐藏代码
function generatorHandleCrackStringFunc(text) {
    const matchResult = text.match(/\d{4,}\);\s?(function.*),\s?[A-Za-z].[A-Za-z]\s?=\s?[A-Za-z]/)
    if (matchResult.length !== 2) {
        throw new Error('代码解析失败！')
    }
    const funcName = matchResult[1].match(/function ([A-Za-z])\([A-Za-z],\s?[A-Za-z]\).*(?=abc)/)[1]
    return {
        crackName: funcName,
        crackCharFunc: new Function([], matchResult[1] + ';return function(num,char){return ' + funcName + '(num, char)}')()
    }
}
```

然后调用解密函数

```
 复制代码 隐藏代码
    traverse(ast, {
        CallExpression(path) {
            if (path.node.arguments.length === 2) {
                if (path.node.callee.name !== name) {
                    return
                }
                if (path.node.arguments[0].type !== 'NumericLiteral') {
                    return;
                }
                if (path.node.arguments[1].type !== 'StringLiteral') {
                    return;
                }
                const nodeResult = handleStringFunc(path.node.arguments[0].value, path.node.arguments[1].value)
                path.replaceInline(types.stringLiteral(nodeResult))
            }
        },
    });
```

然后对解密后的字符串和数字等做一下合并

```
 复制代码 隐藏代码
    const handleObfs = {
        CallExpression: {
            exit(outerPath) {
                const node = outerPath.node.callee
                const parentPath = outerPath
                if (node?.object?.type === 'Identifier' && node?.property?.type === 'StringLiteral') {
                    const objBinding = outerPath.scope.getBinding(node.object.name)
                    if (objBinding === undefined) {
                        return;
                    }
                    const objNode = objBinding.path.node
                    const funcList = objNode.init?.properties ?? []
                    const funcInstance = funcList.find((item) => {
                        const keyName = item.key.name
                        return keyName === node.property.value
                    })
                    if (funcInstance) {
                        const parentNode = parentPath.node

                        let replaceAst = null
                        if (funcInstance.value.type === 'FunctionExpression') {
                            const originNode = funcInstance.value.body.body[0].argument
                            //函数
                            if (originNode.type === 'CallExpression') {
                                replaceAst = types.callExpression(parentNode.arguments[0], [...parentNode.arguments].splice(1))
                            } else if (originNode.type === 'BinaryExpression') {
                                replaceAst = types.binaryExpression(originNode.operator, parentNode.arguments[0], parentNode.arguments[1])
                            }
                        } else {
                            //字符串
                            debugger
                            replaceAst = types.stringLiteral(funcInstance.value.value)
                        }
                        if (replaceAst) {
                            parentPath.replaceWith(replaceAst)

                        }

                    }
                }
            }
        },
        MemberExpression: {
            enter(path) {
                const node = path.node
                if (node?.object?.type === 'Identifier' && node?.property?.type === 'StringLiteral') {
                    const objBinding = path.scope.getBinding(node.object.name)
                    if (objBinding === undefined) {
                        return;
                    }
                    const objNode = objBinding.path.node
                    const funcList = objNode.init?.properties ?? []
                    const funcInstance = funcList.find((item) => {
                        const keyName = item.key.name
                        return keyName === node.property.value
                    })
                    if (funcInstance) {
                        let replaceAst = null
                        if (funcInstance.value.type === 'StringLiteral') {
                            replaceAst = types.stringLiteral(funcInstance.value.value)
                        }
                        if...