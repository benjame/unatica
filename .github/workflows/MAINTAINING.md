# 维护指南

## 发布新版本

1. 更新版本号

   - package.json
   - electron-builder.yml
   - src/package.json

2. 提交更改

   ```bash
   git add .
   git commit -m "Bump version to x.y.z"
   git tag v0.0.1
   ```

3. 等待 GitHub Actions 完成发布
   - 生成新版本的安装包
   - 发布到 GitHub Release

4. 更新 Homebrew Formula
   - 获取新版本 .dmg 文件的 SHA256
   - 更新 Formula 文件
   - 提交更改到 homebrew-tools 仓库

5. 测试安装

```bash
brew update
brew upgrade unatica
```

## 依赖更新

1. 检查依赖更新

   ```bash
   pnpm outdated
   ```

2. 更新依赖版本

   - package.json
   - pnpm-lock.yaml

3. 测试兼容性

   ```bash
   pnpm install
   pnpm test
   ```
