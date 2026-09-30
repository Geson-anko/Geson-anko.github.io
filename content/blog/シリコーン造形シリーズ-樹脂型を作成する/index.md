---
title: "シリコーン造形シリーズ：その4 「樹脂型を作成する」"
slug: "silicone-series-making-resin-mold"
date: 2026-09-30
draft: false
description: "シリコーン造形シリーズ第4回。Blenderアドオン「Silicone Casting」を使って、シリコーンボール用の樹脂型を作ります。"
tags: ["シリコーン", "造形", "Blender", "3Dプリンター"]
categories: ["趣味"]
series: ["シリコーン造形シリーズ"]
series_order: 5
---

## TL;DR

- [番外編](/blog/silicone-series-blender-addon/)で紹介したBlenderアドオン「Silicone Casting」で、**直径20mmほどのシリコーンボール用の樹脂型** を作った
- 流れは「マスターに壁を付ける → 注ぎ口と穴をBooleanで加工 → 型を割る → ダボを付ける → STL出力」
- 操作の細かい流れは動画にまとめたので、記事では各工程のポイントを紹介する
- 完成品のBlender・STL・スライサーのファイルも配布している

## はじめに

みなさんこんにちは、GesonAnkoです。
[前回の番外編](/blog/silicone-series-blender-addon/)で、Blenderで樹脂型を作りやすくするためのアドオンを作成しました。
今回はそれを使って、実際に樹脂型を作っていきます。

今回作るのは、直径20mmほどのシリコーンボールの型です。
球は形が単純なので、型づくりの流れを一通り確認するのにちょうどよい題材です。

作業の様子は動画にまとめました。Blenderの基本的な操作は動画を見ていただくのが分かりやすいので、記事では各工程で何をしているかを中心に説明します。

{{< youtube 5eRpyAMvDLQ >}}

アドオンのインストール方法は[番外編](/blog/silicone-series-blender-addon/)を参照してください。

### 配布ファイル

完成品のファイルはこちらです。手元で中身を確認したり、そのまま印刷したりできます。

- [サンプル型.blend](サンプル型.blend)（Blenderファイル）
- [Target.Left.stl](Target.Left.stl) / [Target.Right.stl](Target.Right.stl)（型のSTL）
- [サンプル型.3mf](サンプル型.3mf)（Bambu Studioのプロジェクトファイル）

## 型の構成

今回の型は、次の4つのオブジェクトを組み合わせて作ります。

| オブジェクト | 役割                                             |
| ------------ | ------------------------------------------------ |
| **Target**   | マスターの球。Solidifyで壁を付けて型の本体にする |
| **Base**     | 台座。型を平らな面に置けるようにする             |
| **Input**    | 注ぎ口。シリコーンを流し込む漏斗                 |
| **Hole**     | 注ぎ口と球の空洞をつなぐ穴                       |

最後に型を左右2つに割り、ダボで位置合わせできるようにします。

## 樹脂型を作る

### 1. マスターと台座を作る

UV球を追加して名前を **Target** にし、これをマスターにします。
続いて立方体を追加して **Base** とし、編集モードで薄く平たくして球の下に置きます。

Targetを選んだ状態で、サイドバー（**N** キー）の Silicone Casting タブから **Solidify** を押すと、球の外側に厚みが付いて型の壁になります。形が決まったら **Apply Solidify** で確定します。

<figure style="margin: 1rem 0;">
  <img src="step-master.png" alt="球のマスターと平たい台座" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">球のマスター（Target）と台座（Base）</figcaption>
</figure>

### 2. 注ぎ口を作る

円錐を追加し、上下を反転して漏斗の形にします。名前は **Input** としました。
注ぎ口にも **Solidify** で厚みを付けます。このとき **Flip Direction** にチェックを入れると、厚みが内側に付きます。

<figure style="margin: 1rem 0;">
  <img src="step-input.png" alt="球の上に置いた漏斗形の注ぎ口" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">漏斗形の注ぎ口（Input）</figcaption>
</figure>

### 3. 注ぎ口と空洞をつなぐ穴を作る

このままでは注ぎ口と球の空洞がつながっていないので、円柱を追加して **Hole** とし、注ぎ口の底から球の空洞まで届く位置に置きます。
X線表示（**Alt + Z**）にすると、内側の位置関係を確認しながら調整できます。

<figure style="margin: 1rem 0;">
  <img src="step-hole.png" alt="X線表示で注ぎ口と空洞の間に置いた円柱" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">注ぎ口と空洞をつなぐ穴（Hole）</figcaption>
</figure>

### 4. Booleanでまとめる

Targetにサブディビジョンサーフェスを追加して球を滑らかにしたあと、Silicone Casting の **Boolean** パネルで各パーツをTargetにまとめます。

- Base を **Union**（結合）
- Input を **Union**（結合）
- Hole を **Difference**（くり抜き）

どれもモディファイアとして追加されるので、元のオブジェクトを動かせば後から形を調整できます。

<figure style="margin: 1rem 0;">
  <img src="step-boolean.png" alt="Booleanモディファイアで台座と注ぎ口をまとめたTarget" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">Booleanでまとめた型</figcaption>
</figure>

### 5. 型を割る

型からシリコーンを取り出せるように、型を左右に割ります。
今回は球なので、平面で真ん中から割れば十分です。平面を追加して90°回転し、型の中心に置きます。

**Surface Cut** パネルで平面を切断面に指定し、**Add Surface Cut** を押すとTargetに切断が追加されます。

<figure style="margin: 1rem 0;">
  <img src="step-surface-cut.png" alt="型の中心に置いた切断用の平面" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">切断面にする平面</figcaption>
</figure>

**Separate Loose Parts** を押すと、割れた型が別々のオブジェクトに分かれます。名前は **Target.Left** / **Target.Right** としました。

<figure style="margin: 1rem 0;">
  <img src="step-separate.png" alt="左右に割った型の断面。球の空洞と注ぎ口が見える" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">割った型の断面</figcaption>
</figure>

### 6. ダボを付ける

割った型を合わせるときの位置合わせ用に、**Registration Keys** でダボを付けます。
今回は先細りの **Tapered Dowel**（直径3mm）を選びました。片方の型の断面をクリックすると、その型にピン（凸）、もう片方にソケット（凹）が作られます。

<figure style="margin: 1rem 0;">
  <img src="step-registration-keys.png" alt="型の断面にダボを配置している画面" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">断面をクリックしてダボを配置</figcaption>
</figure>

空洞を囲むように3か所に配置しました。

<figure style="margin: 1rem 0;">
  <img src="step-keys-placed.png" alt="3か所にダボを配置した型" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">3か所に配置したダボ</figcaption>
</figure>

### 7. STLを書き出す

最後に、Target.Left と Target.Right をそれぞれ選んで **Export STL** で書き出します。
書き出すパーツだけを選んでから押すのがポイントです（[番外編](/blog/silicone-series-blender-addon/)の「全選択に注意」も参照してください）。

## スライスする

書き出したSTLをBambu Studioに読み込み、Bambu Lab P2SとPLA Basicで印刷します。
型の内側の面はそのままシリコーンの表面になるので、積層痕を目立たせないよう積層ピッチ **0.08mm High Quality** で印刷しました。

<figure style="margin: 1rem 0;">
  <img src="slicer.png" alt="Bambu Studioに左右の型を並べた画面" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">Bambu Studioでのスライス設定</figcaption>
</figure>

## 印刷結果

印刷した型がこちらです。

<figure style="margin: 1rem 0;">
  <img src="printed-mold.png" alt="PLAで印刷した左右の樹脂型。注ぎ口と球の空洞が見える" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">印刷した樹脂型</figcaption>
</figure>

注ぎ口から球の空洞までつながった、左右の型を印刷できました。

## まとめ

アドオンを使って、シリコーンボール用の樹脂型を作りました。
マスターに壁を付けて、注ぎ口と穴を足して、割ってダボを付ける、という流れは他の形でも同じなので、まずは球のような単純な形で試してみるのがおすすめです。
