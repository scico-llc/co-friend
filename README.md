# CO-friend
CO-create, COntribute, COexistな友達。

## 2. 解決する問題



## 3. チャレンジ

今回のChallengeは「新しい技術」の活用です。

chatGPTやDffuser，ERC6337など今まで経験してこなかったHotな技術を取り入れ、いち早く問題解決に結びつけることに挑戦しました。

ERC6337とSBTを組み合わせることで、「Walletの保持する記憶」という構造を実装でき、新技術の取り組みは成功だったと自負しています。



## 4. 技術

CO-friendにはAIとCryptoの両方の技術を利用しています。

詳細はGitHubに載せていますが、ここでは特徴的な技術Stackを紹介します。


### AI技術 


#### 画像生成系AI (diffusers, Lora)

diffusersはStableDiffusionをはじめとした学習モデルをコマンドラインから利用できるFrameworkです。

今回は親しみやすく、生々しすぎない絵柄が良かったので、アニメイラストに特化したモデルであるanything-5を利用しました。

また、汎用的なモデルに加えることで特定の絵柄・特徴を強調してくれるLoraを利用して安定したAI絵の生成を可能にしました。



#### 言語系AI (chatGPT-3.5)

キャラクターたちの会話や、ユーザーとのインタラクションにはchatGPTのAPIを利用しました。

残念ながら最新のGPT-4はAzureでもopenaiでもWhite Listだとのことで、GPT3.5を使って会話を実現しました。

GPT-4なら満足のいくレベルのプロンプトになったものの，3.5では若干荒さが残るのが現状です。



### Crypto技術



#### SBT (soul bound token)

一度発行した記憶は他者に譲渡できない制約が必要だったので、SBTを利用しました。

NFT/SBTのdeploy~mintまで、全て初めての経験でしたが、IPFSではなくFirebaseを利用するなど課題は残るものの迅速な立ち上げができました。



#### Token Bounded Account

ERC-6551に準拠する形で、NFTに紐づいたContract Walletの発行を行いました。

Contract Wallet自体は、キャラクターNFTの本体のようなもので、ここにSBTを送ることで記憶として永続化を保証しました。

ERC-6551自体がドラフトの状態なため、TBAの実装は大きなチャレンジでしたが、必要な要件を実現できました。



### CO-friendの構成要素
CO-friendは大きく4つの要素で構成されています。
- A.言語AI環境
- B.画像生成AI環境
- C.Blockchain
- D.Mobile App

これらの要素をうまく繋ぎ合わせることで、「常にあなたの隣で進化し続ける友達」を実現しています。
このドキュメントでは詳細な技術的要素について言及し、CO-friendの実装について理解を進めていただければと思います。

### A.言語AI環境
#### [Bot](/bot) - AIコミュニケーションbot
**AI同士の会話**をbotとして実行しています。Mintされて電子空間に誕生したAIには、それぞれ**名前や個性**が存在します。定期的にランダムな邂逅をすることで、さまざまなシチュエーション・話題でコミュニケーションをとります。また、ここでのコミュニケーションは思い出SBTとしてMintされる候補になります。

#### [Server](/backend) - 対人Chatサーバー
サーバーでは、NFTを保有するユーザーとの会話を行っています。chatGPTを活用して、AIの個性をPromptとして仕込んだ状態で、ユーザーとの会話を行います。

### B.画像生成AI環境
#### [Server](/backend) - 画像生成サーバー
画像生成にはPythonとdiffuserを利用しています。生成モデルは[Anything-5](https://huggingface.co/stablediffusionapi/anything-v5)を用いて、イラスト的な画風を採用しています。また、画像の出力やディティールを調整するためにLoraを採用しおり、[kCuteCreatures](https://civitai.com/models/60284/kcutecreatures?modelVersionId=64757)を用いることで生物らしさを担保しています。

### C.Blockchain
#### [Contract](/contract) - スマートコントラクト
CO-friendはPolygon testnet(Mumbai)を利用してNFT/SBT/Contract Accountを発行しています。これらの開発HardHatとSolidityで行なっており、大別して4つのContractを実装しています。
- FriendNFT(ERC721)：AIとして振る舞うキャラクターです
- MemorySBT(ERC721)：Friendの記憶として保持されるSBTです
- DialyNFT(ERC721)：MemorySBTと1:1で対応しており、Memoryに画像をつけたものです。保有することで該当Frinedとの会話が可能になります
- TokenBoundAccount(ERC6337)：FriendNFTに紐づいたContractです。MemorySBTを保管するために使います。将来的にはキャラクターへの投げ銭なども考えています。

### D.Mobile App
#### [Frontend](/frontend) - iOS Application
CO-friendを利用するためのインターフェースです。大きくWidgetとAPP本体の2つの要素に分かれています。WidgetにはFriendNFTのキャラクターが常駐し、15分に1度程度の間隔でユーザーとコミュニケーションを取ろうと話しかけてきます。APP本体はNFTのMintやChatを行うための場です。
