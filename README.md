# 造个博客

## 前端
一个开源的vue3+ts项目，拷贝自:
- REPO
[biaochenxuying
/
blog-vue-typescript](https://github.com/biaochenxuying/blog-vue-typescript)
- BRANCH
  master
- COMMIT
  b753f0b32001e6f19221ed7a53573de61c75d57c

### 部署
直接生产模式部署，生成dist用于Flask加载即可
```bash
cd blog-vue-typescript-master
npm install
npm run build    
```
## 后端
Flask + MySQL 试水，不定期更新（工作繁重）

1. 代码lint工具 - flake8
```bash
flake8 . --exclude=venv,blog-vue-typescript-master
```