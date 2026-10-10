---
title: "シリコーン造形シリーズ：その6 「型の表面処理」"
slug: "silicone-series-mold-surface-finishing"
date: 2026-10-10
draft: false
description: "シリコーン造形シリーズ第6回。FDM方式の3Dプリンターで印刷した型の積層痕を、レジン・やすりがけ・サーフェイサーで消してマットや光沢に仕上げます。"
tags: ["シリコーン", "造形", "3Dプリンター"]
categories: ["趣味"]
series: ["シリコーン造形シリーズ"]
series_order: 8
---

## TL;DR

- FDM方式で印刷した型の積層痕を、**レジン塗り → やすりがけ → サーフェイサー** の順で消した
- シリコーンには型の表面の質感がそのまま写るので、型の段階で表面を整えておくことが大切
- テストピースで「やすりがけの有無」と「つや消し / 光沢」の4パターンを比べたところ、**レジンのあとにやすりがけをした方が** 滑らかに仕上がった
- サーフェイサーを吹いたあとはゴミが付きやすいので、乾くまで保護しておくとよい

## はじめに

みなさんこんにちは、GesonAnkoです。
今回は、FDM方式の3Dプリンターで印刷した型の表面処理を紹介します。

シリコーンは型の表面の質感がそのまま転写されます。
[その4](/blog/silicone-series-making-mold/)のように0.08mmピッチで印刷すればかなり綺麗になりますが、それでも勾配が緩やかな場所などには段々ができてしまいます。
シリコーンは硬化したあとに追加工しにくいので、型の段階で表面処理をしておくことが重要です。

今回は、仕上がりの違う **マット（つや消し）** と **光沢** の2種類を紹介します。
なお、やすりがけ以降の工程は光造形方式で印刷した型にも使えます。小さい造形物なら、最初から光造形方式の3Dプリンターで型を作った方がよいかもしれません。

## 必要なもの

- 耐水やすり：120番、240番、400番、600番（コーナンオリジナルのLIFELEXを使いました）
  - さらに滑らかにしたい場合は、800番や1000番もあるとよいです
- 2液性のエポキシレジン：今回は[SANAAAのエポキシレジン液][sanaaa-resin]を使いました
- 30mLのプラスチックカップ
- 使い捨ての筆
- サーフェイサー：GSIクレオスの Mr.スーパークリアー（つや消し / 光沢）
- ニトリル手袋、保護メガネ、マスク

## テストピースを用意する

今回は効果を確かめるために、50mm × 50mm × 5mmの板をPLAのブラックで印刷しました。
ブラック系は、やすりの跡が見やすいのでおすすめです。

積層痕が分かりやすいよう、板を立てた向きで、あえて0.2mmピッチで印刷しています。

<figure style="margin: 1rem 0;">
  <img src="print-direction.png" alt="積層痕の横縞が見えるPLAの板" style="width: 100%; max-width: 500px;">
  <figcaption style="text-align: center; font-size: 0.9em;">立てた向きで印刷した板の積層痕</figcaption>
</figure>

「レジンのあとにやすりがけをする / しない」と「つや消し / 光沢」の組み合わせで4パターンを比べるため、4枚印刷しました。

<figure style="margin: 1rem 0;">
  <img src="test-plates.png" alt="印刷した4枚のテストピース" style="width: 100%; max-width: 500px;">
  <figcaption style="text-align: center; font-size: 0.9em;">4枚のテストピース</figcaption>
</figure>

## レジンを塗る

### 下地を荒らす

まず120番の一番荒いやすりで表面を削ります。レジンの食いつきをよくするためです。
積層方向に沿って擦るとよいです。

<figure style="margin: 1rem 0;">
  <img src="sanding-120.png" alt="120番のやすりで表面を荒らした4枚の板" style="width: 100%; max-width: 500px;">
  <figcaption style="text-align: center; font-size: 0.9em;">120番で荒らした表面</figcaption>
</figure>

### レジンを混ぜて塗る

レジンの主剤と硬化剤を混ぜます。テストピース4枚なら、2mLくらいの少量で足ります。

<figure style="margin: 1rem 0;">
  <img src="resin-mixing.png" alt="少量のレジンを入れたカップと筆" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">混ぜたレジンと筆</figcaption>
</figure>

混ぜたレジンを、筆で薄く均一に塗ります。レジンは肌や目に付かないよう、ニトリル手袋と保護メガネを着けて作業しましょう。

<figure style="margin: 1rem 0;">
  <img src="resin-coating.png" alt="レジンを塗った4枚の板" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">レジンを塗ったところ</figcaption>
</figure>

#### 実は重要⚠️: なぜPLAにレジンを塗るのか

積層痕をすべてやすりで消すのは、現実的には不可能です。そこで、レジンで表面全体を覆って段差を埋めます。
また、PLAは硬いので、そのまま削り続けるのはかなり大変です。レジンの層があれば、細かい番手でも表面を整えやすくなります。

### 硬化させる

1日ほど置いて硬化させたものがこちらです。

<figure style="margin: 1rem 0;">
  <img src="resin-cured.png" alt="レジンが硬化した4枚の板" style="width: 100%; max-width: 500px;">
  <figcaption style="text-align: center; font-size: 0.9em;">硬化したレジン</figcaption>
</figure>

積層痕は埋まりましたが、塗りムラによる凹凸が残っています。

## やすりをかける

比較のため、4枚のうち2枚だけにやすりをかけました。
240番 → 400番 → 600番の順に番手を上げています。

<figure style="margin: 1rem 0;">
  <img src="resin-sanded.png" alt="やすりがけした2枚の板" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">600番までやすりがけした板</figcaption>
</figure>

## サーフェイサーを吹く

レジンを塗っただけの板とやすりがけした板に、つや消しと光沢のサーフェイサーをそれぞれ吹きます。

- 天気のよい日に、屋外で作業する
- 1回吹いたら30分待ち、もう一度吹いて2度塗りにする
- 保護メガネとマスクを必ず着ける

### 結果

4パターンの仕上がりがこちらです。

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0;">
  <figure style="margin: 0;">
    <img src="result-resin-matte.png" alt="レジン塗りのみでつや消しにした板。表面に凹凸が残っている" style="width: 100%;">
    <figcaption style="text-align: center; font-size: 0.9em;">レジンのみ + つや消し</figcaption>
  </figure>
  <figure style="margin: 0;">
    <img src="result-sanded-matte.png" alt="やすりがけしてつや消しにした板。表面が滑らか" style="width: 100%;">
    <figcaption style="text-align: center; font-size: 0.9em;">やすりがけ + つや消し</figcaption>
  </figure>
  <figure style="margin: 0;">
    <img src="result-resin-gloss.png" alt="レジン塗りのみで光沢にした板。反射に凹凸が見える" style="width: 100%;">
    <figcaption style="text-align: center; font-size: 0.9em;">レジンのみ + 光沢</figcaption>
  </figure>
  <figure style="margin: 0;">
    <img src="result-sanded-gloss.png" alt="やすりがけして光沢にした板。表面が滑らか" style="width: 100%;">
    <figcaption style="text-align: center; font-size: 0.9em;">やすりがけ + 光沢</figcaption>
  </figure>
</div>

やすりがけした方が表面が滑らかになり、仕上がりがよくなりました。
レジンを塗っただけの板は、塗りムラの凹凸がそのまま残っています。

また、どの板にも小さなゴミが付いてしまいました。サーフェイサーを吹いたあとは、乾くまでゴミが付かないよう保護しておくとよいです。

## 実際の型に使う

同じ手順で、実際の型も表面処理しました。

マット加工した型がこちらです。

<figure style="margin: 1rem 0;">
  <img src="mold-matte-1.png" alt="マット加工した型" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">マット加工した型</figcaption>
</figure>

<figure style="margin: 1rem 0;">
  <img src="mold-matte-2.png" alt="マット加工した顔の型" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">マット加工した顔の型</figcaption>
</figure>

光沢加工した型がこちらです。

<figure style="margin: 1rem 0;">
  <img src="mold-gloss.png" alt="光沢加工した手の型" style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">光沢加工した手の型</figcaption>
</figure>

## まとめ

FDM方式で印刷した型の積層痕を、レジン・やすりがけ・サーフェイサーで消しました。
レジンで段差を埋め、やすりで凹凸を整えてからサーフェイサーを吹くと、滑らかな表面に仕上がります。
作りたいシリコーンの質感に合わせて、つや消しと光沢を選んでみてください。

### 商品リンク

- [SANAAA エポキシレジン液][sanaaa-resin]

[sanaaa-resin]: https://amzn.asia/d/0cNRl9T5
