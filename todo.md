# Tank War (Battle City, 坦克大战)

## 游戏简介

[简介](https://zhuanlan.zhihu.com/p/54181691)

[Wiki](https://strategywiki.org/wiki/Battle_City/How_to_play)

## 资源

[贴图资源](https://www.spriters-resource.com/nes/batcity/)

[参考实现](https://github.com/CharlesPikachu/Games/tree/master/cpgames/core/games/tankwar)和[效果展示](https://zhuanlan.zhihu.com/p/97269434)

[其他介绍](https://zhuanlan.zhihu.com/p/111243310)

[通关视频(单人)](https://www.bilibili.com/video/BV1UW411z791)
[通关视频(双人)](https://www.bilibili.com/video/BV1vt411k7FV)

## 需求

1. 复刻游戏坦克大战核心游戏性
2. 贴图和音效
3. 地图生成器和编辑器
4. 更智能的AI (optional)

## 细节

1. 基本元素和surface的渲染
   1. 坦克
      1. 己方
      2. 敌方
         1. 普通
         2. 轻装甲
         3. 重装甲
      3. 不同等级
      4. 不同状态
   2. 子弹
      1. 不同等级
   3. 地图元素
      1. 砖墙
      2. 钢板 (3级以上子弹才能摧毁)
      3. 河流
      4. 草地 (敌方不可见)
   4. 基地
      1. 己方, 敌方
   5. 各种技能
      1. 子弹等级
         1. 射速
         2. 弹速
         3. 攻击力
      2. 命
      3. 无敌状态
      4. 基地护甲
      5. 过河
      6. 其他技能
         1. 特殊子弹
            1. 范围伤害子弹
            2. 短时间高射速
            3. 减速子弹
         2. 提高速度但是不能攻击
2. 玩家输入控制
   1. 上下左右移动
   2. 炮塔旋转
   3. 开火
   4. 使用技能
3. 计分板
   1. 玩家状态
   2. 得分
4. 音效播放
   1. 移动
      1. 普通地面
      2. 草地
      3. 水面
   2. 子弹发射
   3. 子弹命中
      1. 墙体: 砖墙, 钢板
      2. 地图边界
      3. 敌人
   4. 技能获取
   5. 技能释放
5. 物理引擎
   1. 碰撞检测
      1. pygame
   2. 物体运动
      1. 坦克
         1. 直走
         2. 拐弯
            1. 拐弯机制
         3. 旋转炮塔
         4. 墙体阻挡
      2. 子弹
         1. 炮口发射
         2. 和墙体的碰撞
         3. 和敌军的碰撞
         4. 和友军的碰撞
         5. 子弹之间的碰撞
   3. 地图改变
      1. 墙体破坏
      2. 基地护甲升级
6. 地图设计
   1. 自动生成地图
   2. 玩家自定义地图
7. 坦克AI (trivial)
   1. 生成
   2. 寻路
   3. 攻击
   4. 躲避
   5. 合作
   6. 守护

## 算法实现

1. 
