---
title: "プロジェクト"
description: "開発プロジェクト一覧"
showTableOfContents: true
showDate: false
showAuthor: false
showWordCount: false
---

## P-AMI\<Q> エコシステム

好奇心ベースの自律機械知能「P-AMI\<Q>」を実現するための統合システム群：

- [**pamiq-core**](https://github.com/MLShukai/pamiq-core): 推論と学習のリアルタイム非同期処理を実現し、機械学習モデルの継続的学習を可能にします。（[**第 43 回日本ロボット学会学術講演会（RSJ2025）**](https://ac.rsj-web.org/2025/)で発表しました！）
- [**pamiq-io**](https://github.com/MLShukai/pamiq-io): 映像や音声の入出力を担当するライブラリ。

  - [**pamiq-vrchat**](https://github.com/MLShukai/pamiq-vrchat): pamiq-core および pamiq-io を用いた VRChat 用インターフェイス、PAMIQ のサンプル実装。

    <iframe width="320" height="200" src="https://www.youtube.com/embed/hYjet0v17rY?si=KeSHOR9LG-o-j5Ff" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

- [**pamiq-recorder**](https://github.com/MLShukai/pamiq-recorder): 観測データ収集と行動ログ記録のためのツール群。

## ROS2

- [**ROS2 NDArray Messages**](https://github.com/Geson-anko/numpy_ndarray_msgs): 多次元配列を効率的に送受信するためのメッセージライブラリ。機械学習と連携したロボティクスシステムに不可欠なデータ構造をサポートします。
  - Python utility: [ros2-ndarray-msg-utils](https://pypi.org/project/ros2-ndarray-msg-utils/)
- [**ROS2 UV Template**](https://github.com/Geson-anko/ros2_uv_template): [**uv**](https://docs.astral.sh/uv/)を用いた最新の ROS2 プロジェクトテンプレート。依存関係管理と開発環境設定を効率化し、ROS の Python プロジェクトをモダンなテイストに仕上げます。
  - [解説ブログはこちら](https://qiita.com/GesonAnko/items/510eeade1f8ada302b9b)

## Python

- [**Python UV Template**](https://github.com/Geson-anko/python-uv-template): Python プロジェクトのプロフェッショナルな開発環境テンプレート。テスト、型チェック、CI/CD など、品質を担保するための一連のツールを統合しています。

## Contributions

- [**inputtino の完全な Python バインディング**](https://github.com/games-on-whales/inputtino?tab=readme-ov-file#using-the-python-bindings): Linux の入力デバイスを Python から完全に制御可能にするライブラリの拡張。エージェントのゲーム連携を容易にします。

- [**Typst 版バーチャル学会論文要旨テンプレート**](https://github.com/Geson-anko/vconf24_template_typst): バーチャル学会の論文要旨を Typst というモダンなツールで記述可能にします。

- [**soundfile の型ヒントの実装**](https://github.com/bastibe/python-soundfile/pull/462): 音声ファイルの IO ライブラリに型ヒントを追加し、型システムを導入したプログラミングを可能にします。
