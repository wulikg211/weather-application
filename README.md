## 服务介绍
本服务可以查询1个中国城市最近7天的天气情况

## 安装指南
1. 安装python3.6
2. pipenv安装虚拟环境：pipenv --python 3.6
3. 安装依赖库：pipenv install
4. 配置文件：app/app_config.py，后续可改成读取yaml格式的配置文件
5. 启动本机服务：进入虚拟环境后在项目根目录执行python run.py
6. linux服务器启动服务：项目根目录执行run.sh

## api文档
1. 启动服务后浏览器访问/apidocs地址，如http://127.0.0.1/apidocs/

## 使用指南
1. 浏览器访问web服务首页，如http://127.0.0.1:5050/，输入中国城市名进行筛选，然后从筛选结果中点击一个城市即可其展示未来7天天气

## 测试用例
1. pytest测试脚本存放在根目录test文件夹

## 其他说明
由于没有一台有公网IP的服务器以及免费域名，所以没有将服务改成https

