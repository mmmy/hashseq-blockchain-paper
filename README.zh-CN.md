# hashseq-blockchain

[English](./README.md) | 简体中文

基于区块链 hash 值生成数列的可复现示例仓库。

## 内容
- 原始论文稿件
- Python 实现
- 双色球示例
- 单元测试

## 安装
```bash
python -m pip install -e .
```

## 快速开始
```bash
python -m hashseq.example --hash 0000000000000000000f
```

## 说明
- 输入必须是十六进制 hash 字符串
- 结果是确定性的，不等于证明真正随机
- 具体使用哪条链、哪个区块、多少确认数，需要在协议层先定义
- 英文论文版本目前复用原始中文图片；关键图表后续可以重制为英文版

## 原稿
- [paper/基于区块链hash值生成数列的系统与方法V2.docx](./paper/基于区块链hash值生成数列的系统与方法V2.docx)
- [paper/基于区块链hash值生成数列的系统与方法2/](./paper/基于区块链hash值生成数列的系统与方法2)

## Markdown 论文
- [paper-md/基于区块链hash值生成数列的系统与方法V2.md](./paper-md/基于区块链hash值生成数列的系统与方法V2.md)

## English Paper
- [paper-en/blockchain-hash-sequence-generation-system-and-method-v2.md](./paper-en/blockchain-hash-sequence-generation-system-and-method-v2.md)

