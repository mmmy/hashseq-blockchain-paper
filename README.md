# hashseq-blockchain

[English](./README.md) | [简体中文](./README.zh-CN.md)

A reproducible example repository for generating deterministic number sequences from blockchain hash values.

## Contents
- Original paper manuscripts
- Python implementation
- Double Color Ball example
- Unit tests

## Install
```bash
python -m pip install -e .
```

## Quick Start
```bash
python -m hashseq.example --hash 0000000000000000000f
```

## Notes
- The input must be a hexadecimal hash string.
- The output is deterministic; this repository does not prove true randomness by itself.
- The blockchain, block height or time rule, and confirmation policy must be defined at the protocol layer before use.
- The English paper currently reuses the original Chinese figures. Key charts can be redrawn in English later.

## Original Manuscripts
- [paper/基于区块链hash值生成数列的系统与方法V2.docx](./paper/基于区块链hash值生成数列的系统与方法V2.docx)
- [paper/基于区块链hash值生成数列的系统与方法2/](./paper/基于区块链hash值生成数列的系统与方法2)

## Chinese Markdown Paper
- [paper-md/基于区块链hash值生成数列的系统与方法V2.md](./paper-md/基于区块链hash值生成数列的系统与方法V2.md)

## English Paper
- [paper-en/blockchain-hash-sequence-generation-system-and-method-v2.md](./paper-en/blockchain-hash-sequence-generation-system-and-method-v2.md)
