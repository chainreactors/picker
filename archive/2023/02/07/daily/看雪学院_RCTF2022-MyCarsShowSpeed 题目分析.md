---
title: RCTF2022-MyCarsShowSpeed 题目分析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458493925&idx=1&sn=9205954527b62f7dd04a028bbd3e401f&chksm=b18e936f86f91a79d37166f1ed5761ba4e58818b56919a9edec5b0b4b9add032ae6ca32e76ba&scene=58&subscene=0#rd
source: 看雪学院
date: 2023-02-07
fetch_date: 2025-10-04T05:52:23.486224
---

# RCTF2022-MyCarsShowSpeed 题目分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0Fz5dVvBzAX0b4TZjGDNGqwjIUxg21DJhZwbkRwXWMWj3AvYvDe2RbaA/0?wx_fmt=jpeg)

# RCTF2022-MyCarsShowSpeed 题目分析

xi@0ji233

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FFTKHuYl4m64TguMuXbDyzKtHoYvXbKMic9xux3hWAuWIoyQ6GoQ2WUw/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：xi@0ji233

title: RCTF2022-MyCarsShowSpeed
date: 2022-12-12 05:00:00
tags:
comments: true
categories:

##

## **- [ctf,pwn]**

做到一道好题，mark一下。

##

```
一

正向分析
```

这一步是可以看看程序具体实现了一个什么逻辑，运行出现一个菜单，并且是多级的。

1. 开始一把游戏
2. 查看信息
3. 拜访商店
4. 切换卡车
5. 输出一句话
6. 退出

其中拜访商店又有一个新的菜单。

1. 买东西
2. 卖东西
3. 修车
4. 取车
5. 退回上一级

我们可以去商店买车，买汽油，买安全带（没有实际用处）和flag，当然 flag 比较贵，那么我们一定要寻找赚钱的途径，把车买了再卖了是得到一半的价格。修车根据时间来算价格，增加车的 health，车有 health，fuel，stability这几个属性，fuel是汽油，health 是血条吧可以理解为，另一个查一查单词意思是稳定性，不过也不知道具体是什么意思。

我们修车的时候不能卖车，估计是防止我们通过这个不停地卖车刷钱。

有了车我们可以去跟一个 bot pk，赢了的话得到 10 块钱，但是跑一次会损耗汽油和 health，然后又要去买，而且只赚 10 块，目测不行，但是通过正向的分析我们很浅显地知道了程序大概逻辑，具体实现需要分析它给的源码。

##

##

```
二

源码分析
```

###

### **基本分析**

看到 .h 文件的一些结构体定义：

```
//store.hstruct game{    void        (*printRules)();    void        (*showCars)(game_t *_this);    void        (*showInfo)(game_t *_this);    int         (*checkCar)(game_t *_this);    void        (*startGame)(game_t *_this);    void        (*switchCars)(game_t *_this);    void        (*compete)(game_t *_this);    void        (*visitStore)(game_t *_this);    void        (*menu)(void);    void        (*printBanner)();    void        (*readInput)(game_t *_this);    void        (*finishGame)(game_t *_this);     store_t     *store;    road_t      *road;    car_t       *userCar;    car_t       *botCar;    carList_t   *carList;    uint32_t    money;    int         winCol;    uint32_t    winTimes;};
```

游戏的具体实现采用函数指针的方式去调用，game 这个结构体有两个重要的参数，一个是 money，另一个是 wintimes，就是金钱和赢得次数。

###

### **money 分析**

在 vscode 中 Ctrl+点击 可以做到类似 IDA 的交叉引用，我们看看什么行为会修改我们的 money。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EgaKMSgcwVu7q4s7HpJur2mkiatibQSfhet4NLXUNzvTUXz8ksWB80z5rVL4yVib6UYOnKSmKbRHkkg/640?wx_fmt=png)

在 game.c 中的三处引用，第一个是初始化 120，第二个是 printinfomation 的时候会用到，第三个是没赢一盘给你加 10 点，这个我们在正向分析的时候没有太大问题，问题应该不会直接出现在这些代码上。

那就看看 store.c，七处引用，第一个是在买东西的时候判断当前金钱是否大于等于物品金钱，第二个第三个是买完商品对应给你扣钱。这两个地方需要注意一下，虽然最后我们知道这里没有问题，但是往往最容易忽略的是这里的逻辑问题，我们需要严格判断有没有可能把我们的金钱减到负数然后把钱变得很多，然后判断有没有可能用整数溢出的方式绕过。

第四个地方是 game->money += car->cost / 2 + car->performance \* 2;，应该是在卖车的时候，因为这里有一个把车的价格除 2 给我们，后面加了一个 performance \* 2，不过我们还不知道这个 performance 是啥，也不用管。

五六七都在一起了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EgaKMSgcwVu7q4s7HpJur2EJyFmlR2rO2ywe04ic6HRNXsrZVQ3XN03kxx0tuEibibNPD7IOUdHyDTA/640?wx_fmt=png)

判断如果花费 > 我们当前的金钱那么就让花费等于我们当前的金钱然后减掉，这里导致的一个问题就是我可以实现零元修车，但是对于我们刷钱来说还是没啥用。

往上面看可以发现它在修车的时候会记录你的时间戳，但是不是时间戳直接减，而是直接取出时分秒然后算个一天的时间，再相减，最容易想到的方法当然是 零点之前放车，然后零点之后取车，这样的话能实现花费为负数刷到大量的钱。

本地调试一下看看。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EgaKMSgcwVu7q4s7HpJur2icIbtdljkqjQ9L8FacmQ95Ef6jQHycUX9lu8z1w2NApP8y1QQjOl1SQ/640?wx_fmt=png)

那么效果是达到了，可是当尝试买 flag 的时候，发现没有得到 flag，于是我们跑到 store.c 里面看看关于 flag 那边代码的描述。

```
else if(strcmp(goods->name, "flag") == 0){    if(game->winTimes < 1000)    {         puts("No! You cheated in this game! Where did your money come from?\n");        puts("Punish for cheaters!\nYour cars are confiscated!");        carList_t *curCar = game->carList;        while(curCar)        {            car_t *car = curCar->car;            if(car)            {                free(car);                curCar->car = NULL;            }            curCar = curCar->next;        }        game->carList->carNums = 0;        game->userCar = NULL;    }    else    {        int fd;        char buf[64];        puts("You've earned it!");        puts("Here is your flag!");        fd = open("./flag", O_RDONLY);        if(fd >= 0)        {            read(fd, buf, 64);            write(1, buf, 64);        }    }    return; }
```

发现那个分支里面，还要判断你赢 1000 次才可以获得 flag。如果没有赢 1000 次就买 flag 还会强制没收你的车。但是我们正向分析的时候可以得到，修车的时候不能卖车，那么我们如果让它修车的时候买 flag，车被强制回收还会 free 一次，那么我们还可以把车取回来，再买一次 flag，再 free 一遍，造成 uaf 漏洞，我们这样可以去写 wintimes 字段。

有源码的好处是我们可以强制把我们初始化的钱改成 99999，因为我们已经掌握了刷钱的方法，剩下的我们只需要去刷次数即可，经过测试发现甚至可以直接 double free，在 2.31 中，check 没有很严格，tcache 分配不检查 size，但是检查 count，如果tcache count 为 0 即使指针不为 NULL 也不会分配。

经过尝试，我们可以很轻松地泄露出堆的地址，那么我们要绕过 2.31 的 check count 的检测可以采用三次 free 的方法去绕过，第一次分配写上目标堆块地址，也就是 heap\_addr+0x330，这个地方是 wintimes 的地址。第二次 free 取出原来的堆块，第三次分配拿到目标堆块去随便写几个字符串，超过 1000 就行了，于是我们很轻松地写出了这一题。

###

### **performance分析**

但是问题来了，难道只有零点能刷钱？这也太不友好了，我们之前留下了一下悬念，比如汽车的 performance 可以让我们提升卖车的价值，我们对它交叉引用一下看看。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EgaKMSgcwVu7q4s7HpJur26cBVBb8eEPKLxOSxbFIcQdiaVwnWCl4epxXZpMGpHRub4mP78dqzjCg/640?wx_fmt=png)

比较简单，也没有什么地方调用了它，除了刚刚的卖的时候可以价钱，再就是在 finishGameImpl 函数中让它的价值增加了。

再交叉引用一下发现在 startGameImpl 函数中调用了它。

```
void startGameImpl(game_t *_this){    int ch;    if(_this->checkCar(_this) == 0)        return ;    initBoard();    _this->userCar->col = USER_COL;    _this->botCar->col = BOT_COL;    road_t *road = _this->road;    if(road != NULL)    {        road->buildRoad(road, ROAD_BLOCKS);        road->printEnd(road);    }    _this->printBanner();    _this->userCar->printCar(_this->userCar);    _this->botCar->printCar(_this->botCar);    while(1)    {        ch = getch();        if(ch == 'q' || ch == 'Q')            goto End;        if(ch == ' ')            break;    }    _this->compete(_this); End:    _this->finishGame(_this);    clear();    endwin();}
```

并且我们很容易可以看出来，如果我们进来直接退出，也会调用这个 finishGame 函数，也可能触发一次 performance++，既然不开始游戏的话我们短时间内还是可以操作很多次的。

我们发现其中两个分支会在某辆车到达终点的时候才会进入的，其它时候根本不会进入。

有一个分支会可能会进入。

```
if(isSlip(p)){    char msg[] = "You are luck!\nYour car's perfomrance increased!";    mvprintw(MSG_ROW + 1, (winCol - strlen(msg)) / 2, "%s", msg);    steps += 0.1;    if(steps == 1.0)    {        steps = 0;        _this->userCar->step += 1;    }    if(_this->userCar->stability < 100)        _this->userCar->stability++;     _this->userCar->performance++;}
```

isSlip是一个随机性函数，也就是 p% 的概率为 1。这里 p=10，也就是 10% 的概率，但是这个有点不太够看，算期望的话，我们 1000 次也就多 200 块，刷的效率还是比较低的。

但是其它地方确确实实没问题了，在这个 new\_game 当中，没有任何办法可以通过正常手段去改这个 iswon 和 wintimes 了。

止步不前了，我们回到刚刚分析金钱的地方。

还是发现了端倪。

它在算时间戳的时候，会让取出时间乘上一个 difficulty。

```
fetchTime = fetchHour * 3600 +  fetchMin * 60 + fetchSec * fixDifficulty;// 0fixTime   = fixHour * 3600 + fixMin * 60 + fixSec;
```

并且给了一个注释 0。

###

### **difficulty分析**

那么这里我们分析一下这个 difficulty 的字段。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EgaKMSgcwVu7q4s7HpJur2iasGoj3FXhYVQrR1qygKK0KiceapNicKbugcNKXLzQiaQAZz1qfZsl05jw/640?wx_fmt=png)

从上到下，第一个是初始化，difficulty 为 1，第二个是定义，第三个是刚刚的 finish game 的时候 ++，最后一个是我们在修车的时候赋值，又是 finishGame ，我们继续跳到里面分析。

```
void finishGameImpl(game_t *_this){    car_t *car = _this->userCar;    int fuelCost, healthCost;    int p = 10;    static double steps;     fuelCost = car->col / 10;    healthCost = car->col / 5;    car->health -= healthCost;    car->fuel -= fuelCost;    if(car->health < 0)        car->health = 0;    if(car->fuel < 0)        car->fuel = 0;    car->fixDifficulty++;     if(isSlip(p))    {        char msg[] = "You are luck!\nYour car's perfomrance increased!";        mvprintw(MSG_ROW + 1, (winCol - strlen(msg)) / 2, "%s", msg);        steps += 0.1;        if(steps == 1.0)        {            steps = 0;            _this->userCar->step += 1;        }        if(_this->userCar->stability < 100)        _this->userCar->stability++;         _this->userCar->performance++;    }     attron(COLOR_PAIR(1));    if(_this->botCar->isWon)    {        int ch;        char msg[] = "You lose! Press enter to quit...";        _this->botCar->isWon = 0;        if(car->stability < _this->botCar->stability)        {            car->stability += 5;            car->performance ++;        }         mvprintw(BANNER_ROW + 3, (winCol - strlen(msg)) / 2, "%s", msg);        while((ch = getch()) != '\n');    }    else if(_this->userCar->isWon)    {        int ch;        _this->winTimes++;        _this->userCar->isWon = ...