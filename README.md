# 房源数据分析与个性化推荐系统

一个基于 Flask、MySQL 和 ECharts 的房源信息展示与推荐系统。项目围绕租房/房源数据提供房源检索、列表分页、详情展示、用户登录注册、收藏管理、浏览记录、个性化推荐、房价可视化分析和简单价格趋势预测等功能。

> 当前仓库未包含数据库初始化脚本和示例数据，运行前需要先准备 MySQL 数据库及对应表数据。

## 功能特性

- 房源首页：展示房源总量、最新房源和热门房源。
- 房源检索：支持按地区、小区或户型等字段进行搜索，并通过 Ajax 返回搜索建议。
- 列表分页：支持最新房源、热门房源分页浏览。
- 房源详情：展示价格、户型、面积、朝向、租住类型、区域、小区、交通、配套设施、房东联系方式等信息。
- 用户系统：支持注册、登录、退出登录和个人资料修改。
- 收藏管理：支持收藏房源、取消收藏，并在用户中心集中查看。
- 浏览记录：登录用户访问详情页时自动记录浏览历史，支持清空记录。
- 个性化推荐：根据用户浏览行为写入评分数据，通过 Pearson 相似度推荐其他相似用户关注过的房源。
- 数据可视化：通过 ECharts 展示户型占比、小区房源数量 Top20、价格趋势等图表。
- 价格预测：基于历史均价数据使用 scikit-learn 线性回归模型生成短期趋势预测。

## 技术栈

- 后端：Python、Flask、Flask Blueprint、Flask-SQLAlchemy、PyMySQL
- 数据库：MySQL
- 前端：HTML、CSS、Jinja2、Bootstrap、jQuery、Ajax
- 可视化：ECharts
- 算法与数据分析：Pearson 相似度、协同过滤、scikit-learn、NumPy
- 状态管理：Cookie

## 项目结构

```text
.
|-- README.md
|-- .gitattributes
`-- house/
    |-- app.py                  # Flask 应用入口，注册各业务蓝图
    |-- settings.py             # Flask 与数据库配置
    |-- models.py               # SQLAlchemy 数据模型
    |-- index_page.py           # 首页与搜索建议接口
    |-- list_page.py            # 房源搜索结果、最新/热门列表分页
    |-- detail_page.py          # 房源详情、推荐、图表数据接口
    |-- user.py                 # 注册、登录、用户中心、收藏、浏览记录
    |-- templates/              # Jinja2 页面模板
    |   |-- index.html
    |   |-- list.html
    |   |-- search_list.html
    |   |-- detail_page.html
    |   `-- user_page.html
    |-- static/                 # CSS、JS、图片、字体和前端依赖
    `-- utils/
        |-- con_to_db.py        # PyMySQL 查询工具
        |-- pearson_recommend.py# Pearson 协同过滤推荐
        `-- regression_data.py  # 线性回归价格预测
```

## 数据库说明

项目默认连接本地 MySQL：

```python
mysql://root:root@127.0.0.1:3306/house
```

如果本地数据库账号、密码、主机、端口或库名不同，需要同步修改：

- `house/settings.py`
- `house/utils/con_to_db.py`

核心数据表：

| 表名 | 用途 |
| --- | --- |
| `house_info` | 存储房源标题、户型、面积、价格、朝向、区域、商圈、小区、交通、配套、浏览量、房东信息等房源基础数据 |
| `user_info` | 存储用户名、密码、邮箱、地址、收藏房源 ID、浏览记录 ID |
| `house_recommend` | 存储用户与房源的浏览评分数据，用于 Pearson 推荐 |

## 本地运行

### 1. 克隆仓库

```bash
git clone https://github.com/qisili-66/house.git
cd house
```

### 2. 创建虚拟环境

```bash
python -m venv .venv
```

Windows PowerShell：

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS / Linux：

```bash
source .venv/bin/activate
```

### 3. 安装依赖

仓库目前没有提供 `requirements.txt`，可以先手动安装运行所需依赖：

```bash
pip install flask flask-sqlalchemy pymysql scikit-learn numpy
```

### 4. 准备数据库

创建数据库：

```sql
CREATE DATABASE house DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

根据 `house/models.py` 中的模型创建数据表，并导入房源数据。项目依赖 `house_info`、`user_info`、`house_recommend` 三张核心表。

### 5. 启动应用

```bash
cd house
python app.py
```

启动后访问：

```text
http://127.0.0.1:5000/
```

## 主要路由

| 方法 | 路由 | 说明 |
| --- | --- | --- |
| `GET` | `/` | 首页 |
| `POST` | `/search/keyword/` | 搜索建议 |
| `GET` | `/query` | 搜索结果页 |
| `GET` | `/list/pattern/<page>` | 最新房源列表 |
| `GET` | `/list/hot_house/<page>` | 热门房源列表 |
| `GET` | `/house/<hid>` | 房源详情页 |
| `GET` | `/get/piedata/<block>` | 区域户型占比数据 |
| `GET` | `/get/columndata/<block>` | 小区房源数量 Top20 数据 |
| `GET` | `/get/scatterdata/<block>` | 均价预测图表数据 |
| `GET` | `/get/brokenlinedata/<block>` | 不同户型价格走势数据 |
| `POST` | `/register` | 用户注册 |
| `POST` | `/login` | 用户登录 |
| `GET` | `/logout` | 退出登录 |
| `GET` | `/user/<name>` | 用户中心 |
| `POST` | `/modify/userinfo/<option>` | 修改用户资料 |
| `GET` | `/add/collection/<hid>` | 添加收藏 |
| `POST` | `/collect_off` | 取消收藏 |
| `POST` | `/del_record` | 清空浏览记录 |

## 代码模块说明

- `app.py`：创建 Flask 应用，加载配置并注册首页、列表页、详情页和用户模块蓝图。
- `models.py`：定义 `House`、`User`、`Recommend` 三个 SQLAlchemy 模型。
- `index_page.py`：处理首页展示和搜索关键词建议。
- `list_page.py`：处理搜索结果页、最新房源列表和热门房源列表。
- `detail_page.py`：处理房源详情、浏览记录写入、个性化推荐和图表接口。
- `user.py`：处理用户注册登录、资料修改、收藏和浏览记录管理。
- `utils/pearson_recommend.py`：根据用户浏览评分计算 Pearson 相似度并生成推荐房源。
- `utils/regression_data.py`：使用线性回归模型预测房源均价趋势。

## 发布前注意事项

- 当前项目使用明文密码和 Cookie 保存登录状态，仅适合学习、课程设计或内部演示；生产环境应改为密码哈希、Session 管理和更严格的权限校验。
- 数据库连接信息写在源码中，公开发布或部署前建议改为环境变量配置。
- 仓库包含前端静态依赖文件，体积较大；如需长期维护，建议引入包管理器或 CDN。
- 当前仓库未包含数据库 SQL 文件，其他开发者运行项目前需要自行准备结构和数据。

## License

仓库暂未声明开源许可证。公开视频前请根据实际用途补充 LICENSE 文件。
