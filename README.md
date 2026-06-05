# 房源数据分析与个性化推荐系统

这是一个基于 Flask + MySQL 的房源信息展示与推荐系统，面向租房/二手房场景提供房源检索、详情展示、用户收藏、浏览记录、个性化推荐、房价趋势分析和价格预测等功能。项目后端采用 Flask Blueprint 拆分业务模块，前端使用 Bootstrap、jQuery、Ajax 与 ECharts 完成页面交互和数据可视化。

## 技术栈

- 后端：Python、Flask、Flask Blueprint、Flask-SQLAlchemy、PyMySQL
- 数据库：MySQL
- 前端：HTML、CSS、Jinja2、Bootstrap、jQuery、Ajax
- 可视化：ECharts
- 算法与数据分析：Pearson 相似度协同过滤、scikit-learn 线性回归、NumPy
- 状态管理：Cookie

## 主要功能

- 房源首页：展示房源总数、最新房源、热门房源。
- 房源列表：支持最新房源和热门房源分页浏览。
- 智能搜索：支持按地区、小区、商圈和户型搜索，并通过 Ajax 返回搜索建议。
- 房源详情：展示价格、户型、面积、朝向、租住类型、房东电话、交通条件、配套设施等信息。
- 用户系统：支持注册、登录、退出登录和个人资料修改。
- 收藏管理：支持收藏房源、取消收藏，并在用户中心集中展示。
- 浏览记录：用户访问房源详情时自动记录浏览历史，支持清空记录。
- 个性化推荐：根据用户浏览行为生成房源评分，使用 Pearson 相似度计算相似用户，并推荐相似用户关注过的房源。
- 数据可视化：通过 ECharts 展示区域户型占比、小区房源数量 TOP20、房价走势和不同户型价格走势。
- 价格预测：基于历史房源均价数据，使用线性回归模型预测短期价格趋势。

## 项目结构

```text
.
├── house/
│   ├── app.py                  # Flask 应用入口，注册蓝图
│   ├── settings.py             # 数据库和应用配置
│   ├── models.py               # SQLAlchemy 数据模型
│   ├── index_page.py           # 首页和搜索建议接口
│   ├── list_page.py            # 房源列表与分页
│   ├── detail_page.py          # 房源详情、推荐和图表数据接口
│   ├── user.py                 # 用户登录、注册、收藏、浏览记录
│   ├── templates/              # Jinja2 页面模板
│   ├── static/                 # CSS、JS、图片和前端依赖
│   └── utils/
│       ├── con_to_db.py        # MySQL 查询工具
│       ├── pearson_recommend.py# Pearson 协同过滤推荐
│       └── regression_data.py  # 线性回归价格预测
└── README.md
```

## 数据库说明

项目默认连接本地 MySQL：

```python
mysql://root:root@127.0.0.1:3306/house
```

核心数据表：

- `house_info`：房源基础信息，包括标题、户型、面积、价格、区域、配套设施、浏览量等。
- `user_info`：用户信息，包括用户名、密码、邮箱、地址、收藏房源 ID、浏览记录 ID。
- `house_recommend`：用户浏览评分记录，用于个性化推荐。

如果本地数据库账号、密码或库名不同，需要修改 `house/settings.py` 和 `house/utils/con_to_db.py` 中的数据库配置。

## 本地运行

1. 安装 Python 依赖：

```bash
pip install flask flask-sqlalchemy pymysql scikit-learn numpy
```

2. 准备 MySQL 数据库：

```sql
CREATE DATABASE house DEFAULT CHARACTER SET utf8mb4;
```

3. 根据 `house/models.py` 创建对应数据表，并导入房源数据。

4. 启动项目：

```bash
cd house
python app.py
```

5. 浏览器访问：

```text
http://127.0.0.1:5000/
```

## 核心接口

- `GET /`：首页
- `POST /search/keyword/`：搜索建议
- `GET /query`：搜索结果列表
- `GET /list/pattern/<page>`：最新房源分页
- `GET /list/hot_house/<page>`：热门房源分页
- `GET /house/<hid>`：房源详情
- `GET /get/piedata/<block>`：区域户型占比数据
- `GET /get/columndata/<block>`：小区房源数量 TOP20 数据
- `GET /get/scatterdata/<block>`：价格预测数据
- `GET /get/brokenlinedata/<block>`：户型价格走势数据
- `POST /register`：用户注册
- `POST /login`：用户登录
- `GET /logout`：退出登录
- `GET /add/collection/<hid>`：添加收藏
- `POST /collect_off`：取消收藏
- `POST /del_record`：清空浏览记录

## 项目亮点

- 使用 Flask Blueprint 将首页、列表页、详情页和用户中心按业务模块拆分，提升代码可维护性。
- 基于 SQLAlchemy 完成房源查询、聚合统计、排序、分页和用户行为数据持久化。
- 使用 Ajax 实现搜索建议、收藏、浏览记录删除、图表数据加载等异步交互。
- 使用 Pearson 相似度实现基于用户行为的协同过滤推荐，提升房源推荐的个性化程度。
- 使用 ECharts 将房源数量、户型分布和价格趋势可视化，增强数据分析表达能力。
- 使用 scikit-learn 线性回归模型对房源均价走势进行简单预测，为用户提供价格参考。

