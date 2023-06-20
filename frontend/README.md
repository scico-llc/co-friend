# CO-friend iOS App

## 概要
- CO-friend iOSアプリのリポジトリです。アプリからキャラクターの生成や会話が楽しめるほか、ウィジェットを使ったインタラクションも可能なアプリです。

## 開発環境
- Xcode 14.3.1

## 構成
- UIの実装: SwiftUI
- アーキテクチャ: MVP

## セットアップ
1. 以下の手順でアプリを導入します
```
git clone git@github.com:scico-llc/co-friend.git
cd frontend/Cofriend/
open Cofriend.xcodeproj
```
2. Constants.swift に 各種Key を設定します


## 使用ライブラリとライブラリの管理
Swift Package Mangerにて下記のライブラリを導入しています。

- Alamofire - APIとの通信に利用
- Firebase - FirebaseFirestoreとの通信に利用
- Kingfisher - チャット画面の画像のキャッシュに利用
