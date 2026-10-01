---
title: "シリコーン造形シリーズ：その5 「造形する」"
slug: "silicone-series-casting"
date: 2026-10-01
draft: false
description: "シリコーン造形シリーズ第5回。前回印刷した樹脂型にシリコーンを流し込み、シリコーンボールを造形します。"
tags: ["シリコーン", "造形", "3Dプリンター"]
categories: ["趣味"]
series: ["シリコーン造形シリーズ"]
series_order: 6
---

## TL;DR

- [前回](/blog/silicone-series-making-mold/)印刷した型にシリコーンを流し込み、直径20mmほどのシリコーンボールを造形した
- 流れは「型をグルーガンで固定 → 体積を計算して計量・混合 → 脱泡して流し込む → 硬化 → 取り出してバリ取り」
- シリコーンの量は、アドオンで測ったマスターの体積に **カップに残る分として5mLほど** 足して計量する
- 今回は型の合わせ面で硬化不良が起きたので、**型は使う前に中性洗剤などで洗う** のがおすすめ
- 完成品はゴミが付きやすいので、**タルク系のベビーパウダー** をまぶしておく

## はじめに

みなさんこんにちは、GesonAnkoです。
今回は[前回](/blog/silicone-series-making-mold/)作って印刷した型に、実際にシリコーンを流し込んで造形していきます。

<figure style="margin: 1rem 0;">
  <img src="mold-halves.png" alt="PLAで印刷した左右の型" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">前回印刷した型</figcaption>
</figure>

## 型を固定する

型は使う前に、中性洗剤などで一度洗っておくことをおすすめします。今回は洗わずに使ったところ、合わせ面で硬化不良が起きました（[後述](#硬化不良について)）。

よく乾かしたら、左右の型をダボで合わせます。

<figure style="margin: 1rem 0;">
  <img src="mold-assembled.png" alt="左右を合わせた型" style="width: 100%; max-width: 500px;">
  <figcaption style="text-align: center; font-size: 0.9em;">左右を合わせた型</figcaption>
</figure>

合わせたら、合わせ目に沿って[グルーガン][glue-gun]で固定します。
このとき、隙間が残らないように気をつけてください。ここが甘いと、流し込んだあとにシリコーンが漏れ出て大惨事になります。

<div style="display: flex; gap: 1rem;">
  <figure style="flex: 1; margin: 0;">
    <img src="glue-side.png" alt="型の側面の合わせ目に沿って付けたグルー" style="width: 100%;">
    <figcaption style="text-align: center; font-size: 0.9em;">側面の合わせ目</figcaption>
  </figure>
  <figure style="flex: 1; margin: 0;">
    <img src="glue-bottom.png" alt="型の底面に付けたグルー" style="width: 100%;">
    <figcaption style="text-align: center; font-size: 0.9em;">底面</figcaption>
  </figure>
</div>

注ぎ口の縁から台座まで、合わせ目をぐるっと埋めました。

<figure style="margin: 1rem 0;">
  <img src="glue-done.png" alt="グルーで合わせ目を埋めた型" style="width: 100%; max-width: 500px;">
  <figcaption style="text-align: center; font-size: 0.9em;">固定した型</figcaption>
</figure>

## シリコーンを計量する

### 必要な量を計算する

[番外編](/blog/silicone-series-blender-addon/)で紹介したアドオンの **Measure Volume** で、マスターモデル（Target）の体積を測ります。
直径20mmほどの球なので、4.12mLでした。

実際に混ぜるときはカップや注ぎ口にも残るので、その分として **Extra** に5mLほど追加しておきます。
**Mixture Calculator** に密度と配合比を入れると、A剤・B剤それぞれの重さが分かります。今回は合計9.12mL、A剤・B剤ともに4.92gです。
この計算結果は、前回配布した[サンプル型.blend][sample-blend]に保存してあります。

<figure style="margin: 1rem 0;">
  <img src="volume-calc.png" alt="Measure VolumeとMixture Calculatorで体積と重さを計算した画面" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">体積と配合の計算</figcaption>
</figure>

### 用意するもの

シリコーンは今回、[SANAAAの5A][sanaaa-5a]を使いました。硬度の選び方は[第1回](/blog/silicone-series-choosing-silicone-rubber/)を参照してください。

そのほか、ニトリル手袋、マドラー、30mLのカップ、[0.1g精度の秤][scale]を用意します（写真には誤って60mLのカップが写っています）。

<figure style="margin: 1rem 0;">
  <img src="tools.png" alt="ニトリル手袋、カップ、マドラー、型、SANAAAのシリコーン" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">用意したもの</figcaption>
</figure>

### 混ぜて脱泡する

A剤とB剤をそれぞれ4.92gずつ計量し、マドラーでよく混ぜます。
混ぜたあと、[真空脱泡器][vacuum]にかけて気泡を抜いたものがこちらです。

<figure style="margin: 1rem 0;">
  <img src="mixed-silicone.png" alt="混ぜて脱泡したシリコーン" style="width: 100%; max-width: 500px;">
  <figcaption style="text-align: center; font-size: 0.9em;">混ぜて脱泡したシリコーン</figcaption>
</figure>

## 流し込んで硬化させる

脱泡したシリコーンを、注ぎ口から少しずつ流し込みます。

<figure style="margin: 1rem 0;">
  <img src="poured.png" alt="注ぎ口までシリコーンを流し込んだ型" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">流し込んだ型</figcaption>
</figure>

室温で硬化させる場合、冬なら丸1日、夏なら3〜4時間ほどで型から取り出せます。
私は[テスコムのコンベクションオーブン][oven]を使い、40度で4時間加熱しています。

## 取り出して仕上げる

硬化したら、グルーを剥がして型をぱかっと開け、中身を取り出します。

<figure style="margin: 1rem 0;">
  <img src="mold-opened.png" alt="開けた型。片方にシリコーンボールが残り、合わせ面がシリコーンで濡れたように光っている" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">型を開けたところ</figcaption>
</figure>

注ぎ口や合わせ面の部分にバリができるので、ニッパーや小バサミで切り取ります。
私は[Cloverのカットワークはさみ115][scissors]を愛用しています。

### 硬化不良について

写真をよく見ると、型の合わせ面がテカテカと光っています。これは合わせ面に漏れ出たシリコーンが硬化せず、ベタベタのまま残ったものです。
型の内側のボールは硬化していたので、合わせ面に何かが付いていて、それが硬化を妨げたのではないかと考えています。

プラチナ付加型のシリコーンは、硫黄やアミンなどが触れると硬化不良を起こします（[第1回](/blog/silicone-series-choosing-silicone-rubber/)を参照）。
3Dプリントした型にも、印刷後の取り扱いの中で何かが付いている可能性があ流ので、型を使う前に中性洗剤などで一度洗っておくとよいでしょう。

## 完成

<figure style="margin: 1rem 0;">
  <img src="finished-ball.png" alt="完成した半透明のシリコーンボール" style="width: 100%; max-width: 500px;">
  <figcaption style="text-align: center; font-size: 0.9em;">完成したシリコーンボール</figcaption>
</figure>

シリコーンボールが完成しました。

シリコーンは表面にゴミやほこりが付きやすいので、完成品にはベビーパウダーをまぶしておくのがおすすめです。ベビーパウダーにはタルク系がおすすめです。

## まとめ

前回作った型にシリコーンを流し込み、シリコーンボールを造形しました。
型の固定で隙間を残さないこと、体積から必要な量を計算して少し多めに計量すること、そして型を使う前に洗っておくことが、失敗を減らすポイントです。

### 商品リンク

- シリコーンゴム：[SANAAA 5A][sanaaa-5a]
- [グルーガン][glue-gun]
- [精密電子はかり][scale]
- [真空脱泡器][vacuum]
- [テスコム コンベクションオーブン][oven]
- [Clover カットワークはさみ115][scissors]

[sample-blend]: /blog/silicone-series-making-mold/サンプル型.blend
[sanaaa-5a]: https://amzn.asia/d/0fYC0FIt
[glue-gun]: https://amzn.asia/d/03nwGloD
[scale]: https://amzn.asia/d/0bANlSBX
[vacuum]: https://amzn.asia/d/0gFM0hSD
[oven]: https://www.tescom-japan.co.jp/products/tsf61a
[scissors]: https://onlineshop.clover.co.jp/products/detail/61
