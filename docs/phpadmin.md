## sdf1_login插件php后端介绍

## 目录
- [玩家端](php.md)
- 管理员端(当前)

## php管理员后端
- 默认登录密码ypshidifu2026<br>
- 概览，数据看板。展示实时在线玩家数据、注册用户总数、24小时活跃玩家总数、债券总和&今日注册总数。<br>
![](https://img.ypshidifu.cn/i/2026/07/19/1784474244/6a5cea84d3000.png)<br>
- 债券管理，查验、扣除/充值(人工充值，仅记录玩家到账数据)玩家债券<br>
![](https://img.ypshidifu.cn/i/2026/07/19/1784474245/6a5cea853061d.png)<br>
- 商品管理，可以管理商品库存等数据。<br>
![](https://img.ypshidifu.cn/i/2026/07/19/1784474248/6a5cea8802304.png)<br>
- CDK管理，生成新的CDK。支持盲盒金额类型，比如100-200<br>
![](https://img.ypshidifu.cn/i/2026/07/19/1784474256/6a5cea90a04fe.png)<br>
- 流水记录，查询玩家在Java、php的交易消费记录<br>
![](https://img.ypshidifu.cn/i/2026/07/19/1784474246/6a5cea86a8a94.png)
- 用户管理，查询所有在Java/php注册的玩家信息。可查询范围包括：玩家名字、是否封禁、最后登录时间、积分、在线时长、绑定邮箱、ip地址和ip归属地(内置太平洋网络接口、夏柔Api、百度和ip9免费版).搜索框支持参数：today、yesterday、玩家名、ip段(比如192.168.1.1)、省、市、todayreg、yesterdayreg、ban和temp版<br>
![](https://img.ypshidifu.cn/i/2026/07/19/1784474247/6a5cea873ee8f.png)<br>
- 今日债券，查看今日债券营收数据看板，可以直观地展示今日每一位玩家的债券收益、债券支出和净利润<br>
![](https://img.ypshidifu.cn/i/2026/07/19/1784474249/6a5cea896ee78.png)<br>
- 在线曲线，查看每小时玩家在线数据情况。<br>
![](https://img.ypshidifu.cn/i/2026/07/19/1784474253/6a5cea8dddbcb.png)
- 工单管理，查看所有玩家提报的工单，服务商完结处理的工单。工单语法全面支持markdown格式<br>
![](https://img.ypshidifu.cn/i/2026/07/19/1784474250/6a5cea8adfa25.png)<br>
- 领地管理，查看所有的领地数据，可操纵过户和删除
![](https://img.ypshidifu.cn/i/2026/07/19/1784474251/6a5cea8b858b4.png)<br>
- 用户组管理，编辑好用户组后，玩家可以付费购买并加入该用户组。<br>
![](![php_admin11.png](https://img.ypshidifu.cn/i/2026/07/19/1784474251/6a5cea8b858b4.png))
- 充值对账，全部付费充值订单数据，可与易支付后台一起对账
![](https://img.ypshidifu.cn/i/2026/07/19/1784474256/6a5cea9006361.png)
- 充值商店配置，配置多少钱给多少债券。配置用户端的充值商店数据<br>
![](https://img.ypshidifu.cn/i/2026/07/19/1784474245/6a5cea855fb55.png)