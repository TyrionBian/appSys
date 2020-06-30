# 控制流程序
功能：
1. 初始化存储
2. flask api
3. pyJWT

## 结构
manage.py为程序管理脚本，可参见  
https://flask-migrate.readthedocs.io/en/latest/

Makefile为make执行命令
requirements.txt为程序依赖python包

app为程序入口, 包括：  
main主程序，test测试配置

main中主要包括三部分：  
·controller  
·model  
·service

model是应用对象
service是应用对象的服务
controller其实是封装的api

具体可参考各自依赖包的文档，都比较详细