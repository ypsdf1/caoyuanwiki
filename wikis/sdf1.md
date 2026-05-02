# Sdf1插件说明文档
## 功能介绍
sdf1插件是由草原探险服务器定制插件，主要作用是cdk激活兑换游戏币

## 指令介绍
- /sdf1 主指令，打开会话窗口
- /sdf1 reload 重新加载插件
- /sdf1 update 更新插件
- /sdf1 import 导入cdk
- /import 导入cdk
- /sdf1 undo 撤销导入

## 使用方法：
第一步：安装插件<br>
第二步：使用原版计分板创建指令`/scoreboard objectives add name dummy`创建一个计分板<br>
第三步：修改配置文件：<br>
```txt
//上半部分
计分板:
  口令库: "abc" #这里是口令库，改成存储口令的计分板名字
  查重板: "def"  # 改这里为你的存储查重的计分板名字
//下半部分
```
第四步：重载插件，输入指令`/sdf1 reload`<br>
第五步：进入游戏，输入`/sdf1`<br>
第六步：等待提示开启监听，输入口令<br>
第七步：完成，自动发放游戏币

## 必装依赖
- EssentialsX(经济系统)

## 批量导入方法
第一步：在插件配置文件目录下，新建一个txt文件，文件名任意，例如`cdk.txt`<br>
第二步：在txt文件中有几种格式：
```txt
/* 格式1：短杠分割 */

1分：
cdk1
cdk2
--
2分：
cdk1
cdk2
```
```json
/* 格式2：json格式 */
{
  1分：
  cdk1
  cdk2
  cdk3
}
{
  2分：
  cdk1
  cdk2
  cdk3

}
```
```txt
/* 一行一个分值 */
cdk1 1分
cdk2 2分
```
第三步：文件写好以后，游戏内/控制台执行/import 文件名.txt，进行导入

### 如果导入错误(如分值错误或其它类型错误)
导入错误时，您可使用/sdf1 undo撤销导入，将其修正后重新导入即可

## 注意事项
- 本插件为免费插件，请勿商业转发
- 本插件为草原探险服务器定制插件，体验最新版、内测版建议您游玩草原探险服务器或加入我们的[官方群981954292](http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=ftGx3Ac2pd8IbWV5WZmoIrVHRXgGUb2a&authKey=DLTKLbiInzZe0pegvDtXbTVXeLJ6TAaPtHd3ol8p5adiljTSzzEp8hHU%2BLA4kBT4&noverify=0&group_code=981954292)获取。

## 下载地址：
[官方下载](https://pan.ypshidifu.cn/s/Ygc0) 提取码：sdf1<br>
[bbsmc分流](https://bbsmc.net/plugin/sdf1money)

## 插件源码：
- [github](https://github.com/ypsdf1/sdf1_plugn)
- [gitee](https://gitee.com/nihaoshidifu/sdf1_plugn)

