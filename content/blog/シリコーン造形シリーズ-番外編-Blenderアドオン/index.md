---
title: "シリコーン造形シリーズ：番外編 「樹脂型を作るBlenderアドオンを作った」"
slug: "silicone-series-blender-addon"
date: 2026-09-29
draft: false
description: "シリコーン造形シリーズ番外編。マスターモデルから3Dプリント用の樹脂型を作るBlenderアドオン「Silicone Casting」を紹介します。"
tags: ["シリコーン", "造形", "Blender", "3Dプリンター"]
categories: ["趣味"]
series: ["シリコーン造形シリーズ"]
series_order: 4
---

<figure style="margin: 1rem 0;">
  <img src="overview.png" alt="Silicone Casting のサイドバーと、分割した型のモデル" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">Silicone Casting のサイドバーと、分割した型</figcaption>
</figure>

## TL;DR

- シリコーン造形用の**樹脂型をBlender上で作るアドオン「Silicone Casting」**を公開しました
- マスターモデルから、壁付け・分割・ダボ・空気孔・STL出力までをサイドバーから操作できる
- 体積の計測、A剤・B剤の配合計算、着色剤の滴数から色を予測する機能もある
- Blender 5.1以上で動作。[GitHub](https://github.com/Geson-anko/silicone-casting)から無料でダウンロードできる

## はじめに

みなさんこんにちは、GesonAnkoです。
今回はシリコーン造形シリーズの番外編として、自作したBlenderアドオンを紹介します。

[第2回](/blog/silicone-series-what-you-need/)で「Blenderで樹脂型を設計する方法はそれだけでシリーズ記事になるボリューム」と書きましたが、実際に型を作るたびに同じ手作業を繰り返すのが大変でした。
マスターモデルに厚みを付けて、割って、合わせ位置を作って、空気の逃げ道を開けて...という作業を毎回手でやるのは骨が折れます。

そこで、この一連の作業をまとめてBlenderのアドオンにしました。

- [GitHub: Geson-anko/silicone-casting](https://github.com/Geson-anko/silicone-casting)

## Silicone Casting でできること

アドオンの機能は大きく3つのパネルに分かれています。

| パネル          | 内容                                                               |
| --------------- | ------------------------------------------------------------------ |
| **Measurement** | マスターの体積計測と、A剤・B剤の配合計算                           |
| **Coloring**    | 着色剤の滴数から、仕上がりの色と透明度を予測                       |
| **Processing**  | 型の形を作る処理（壁、Boolean、分割、ダボ、空気孔、分離、STL出力） |

型づくりの流れはこのようになります。

<figure style="margin: 1rem 0;">
  <img src="workflow.png" alt="マスター、壁、分割、ダボ、空気孔、STL出力の順に型ができていく流れの図" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">型づくりの流れ</figcaption>
</figure>

1. マスターモデル（閉じたメッシュ）を用意する
2. マスターの体積を測り、シリコーンの配合と着色を決める
3. **Inherit Shape** でマスターの形を参照するオブジェクトを作り、**Solidify** で壁を付ける
4. 必要なら **Boolean** で注ぎ口などを加工する
5. **Surface Cut** で型を曲面で割る
6. **Separate Loose Parts** で割れた塊を別々のオブジェクトにする
7. **Registration Keys** で合わせ位置のダボを付ける
8. **Air Vents** で空気孔を開ける
9. **Export STL** でパーツごとにSTLを書き出す

以下、主な機能を紹介していきます。

### 体積の計測と配合計算

**Measure Volume** で選択したメッシュの体積をmL単位で計測できます。マスターの体積＝型の空洞の体積なので、これがそのまま必要なシリコーンの量になります。

**Mixture Calculator** に体積を入力すると、A剤・B剤それぞれの体積と重量を計算してくれます。

<figure style="margin: 1rem 0;">
  <img src="mixture-calculator.png" alt="Mixture Calculator の画面" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">Mixture Calculator</figcaption>
</figure>

[第3回](/blog/silicone-series-coloring/)では「10Aシリコーンの比重は1.08g/mLなので、A剤とB剤をそれぞれ5.4gずつ計量すると10mL」と手計算していましたが、Density（密度）に1.08、Ratio（重量比）に1:1を入れておけば自動で計算されます。
パーツごとに行を分けられるので、複数の型に一度に流し込むときも便利です。

#### 実は重要⚠️: 壁を測ると樹脂の量になる

Solidifyで壁を付けたオブジェクトを測ると、**壁だけの体積**（＝印刷する樹脂の量）が出ます。シリコーンの量を測るときは、マスターを選び直してから計測しましょう。

### 着色シミュレーション

**Color Mixing Simulator** では、着色剤の色と滴数から、仕上がりの色と透明度を予測できます。

<figure style="margin: 1rem 0;">
  <img src="color-simulator.png" alt="Color Mixing Simulator の画面" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">Color Mixing Simulator</figcaption>
</figure>

着色剤ごとに **Calibration Drops / mL**（その色に見える濃度＝シリコーン1mLあたりの滴数）を設定します。
第3回の結果でいえば、「まさる」は10mLあたり5滴で十分に発色したので、0.5くらいが目安になります。

予測した色は **Apply to Selected** でマテリアルとしてモデルに適用できるので、塗る前に完成イメージを確認できます。配合と色のレシピはJSONで保存・読み込みできます。

### 壁を付ける（Inherit Shape / Solidify）

**Inherit Shape** は、マスターに手を加えずに同じ形のオブジェクト（`<マスター名>.inherit`）を作る機能です。マスターを編集すると `.inherit` も追従するので、後から形を直しても型を作り直す必要がありません。

この `.inherit` に **Solidify** で厚みを付けると、型の壁になります。

### 型を割る（Surface Cut / Separate Loose Parts）

型を取り出すには、型を割る必要があります。**Draw Surface Cut** では、型の表面に線を描くだけで曲面の切断面を作れます。

<figure style="margin: 1rem 0;">
  <img src="draw-surface-cut.png" alt="Draw Surface Cut で型の表面に線を描いている画面" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">Draw Surface Cut で分割線を描く</figcaption>
</figure>

平面で割れない複雑な形でも、分割線を自由に決められるのがポイントです。
切断はモディファイアとして付くので、切断面は後から調整できます。形が決まったら **Separate Loose Parts** で別々のオブジェクトに分けます。

### ダボを付ける（Registration Keys）

割った型を組み合わせるときの位置合わせ用に、凸（ピン）と凹（穴）のダボを付けます。クリックした位置に1組ずつ追加でき、ドラッグで移動もできます。

<figure style="margin: 1rem 0;">
  <img src="registration-keys-placing.png" alt="Registration Keys ツールでダボを配置している画面" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">Registration Keys でダボを配置する</figcaption>
</figure>

円柱・先細り・角形の3種類から選べます。穴はピンより少し大きく作られるので（既定では片側0.15mm）、3Dプリントしてもはめ込みやすくなっています。

### 空気孔を開ける（Air Vents）

シリコーンを流し込むとき、型の中に空気が残ると気泡や欠けの原因になります。**Air Vents** では、線を描いた場所に円い管状の空気孔を開けられます。

<figure style="margin: 1rem 0;">
  <img src="air-vents-drawing.png" alt="Air Vents で空気孔の線を描いている画面" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">Air Vents で空気孔を描く</figcaption>
</figure>

### STL出力

最後に **Export STL** で3Dプリンター用のSTLを書き出します。モディファイアを適用した形がmm単位で出力されるので、そのままスライサーに読み込めます。

#### 注目👀: 全選択に注意

切断面や空気孔の管、Booleanに使ったオブジェクトはシーンに残ります。**A** キーで全選択してから書き出すと、それらもSTLに混ざってしまいます。書き出すパーツだけを選んでからExport STLを押しましょう。

## インストール方法

動作要件は **Blender 5.1以上**（Windows / macOS / Linux）です。

1. [GitHubのReleasesページ](https://github.com/Geson-anko/silicone-casting/releases)から `silicone_casting-<バージョン>.zip` をダウンロードする（**zipは解凍しない**）
2. Blenderで **Edit > Preferences** を開き、左の一覧から **Get Extensions** を選ぶ
3. 右上の **∨** メニューから **Install from Disk...** を選び、ダウンロードしたzipを指定する

<figure style="margin: 1rem 0;">
  <img src="install-extension.png" alt="Preferences の Get Extensions から Install from Disk を選ぶ画面" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">Install from Disk... からインストール</figcaption>
</figure>

インストール後は、3D Viewportで **N** キーを押してサイドバーを開き、**Silicone Casting** タブを選ぶと使えます。

<figure style="margin: 1rem 0;">
  <img src="sidebar-tab.png" alt="3D Viewport のサイドバーに表示された Silicone Casting タブ" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">サイドバーの Silicone Casting タブ</figcaption>
</figure>

各機能の詳しい使い方は、リポジトリの[docs](https://github.com/Geson-anko/silicone-casting/tree/main/docs)にまとめています。

## まとめ

[第2回](/blog/silicone-series-what-you-need/)で、シリコーン造形は機材に加えて樹脂型の設計スキルも必要になるのがハードルだと書きました。
このアドオンで、少しでもそのハードルが下がればうれしいです。

まだ v0.1.0 なので、不具合や要望があれば [GitHubのIssue](https://github.com/Geson-anko/silicone-casting/issues) で教えてください。

### リンク

- [Silicone Casting（GitHub）](https://github.com/Geson-anko/silicone-casting)
- [Releases（ダウンロード）](https://github.com/Geson-anko/silicone-casting/releases)
- シリコーン造形シリーズ
  - [その1 「シリコーンゴムを選ぶ」](/blog/silicone-series-choosing-silicone-rubber/)
  - [その2 「シリコーン造形に必要なもの」](/blog/silicone-series-what-you-need/)
  - [その3 「シリコーンに着色する」](/blog/silicone-series-coloring/)
