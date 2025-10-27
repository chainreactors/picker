---
title: GitHub Actionsにおける設定ミスに起因したGitHubスタッフのアクセストークン漏洩
url: https://blog.ryotak.net/post/github-actions-staff-access-token/
source: RyotaK's Blog
date: 2023-04-23
fetch_date: 2025-10-04T11:32:07.706210
---

# GitHub Actionsにおける設定ミスに起因したGitHubスタッフのアクセストークン漏洩

[RyotaK's Blog](https://blog.ryotak.net/)
技術的な話とか

## [GitHub Actionsにおける設定ミスに起因したGitHubスタッフのアクセストークン漏洩](https://blog.ryotak.net/post/github-actions-staff-access-token/)

2023-04-22
 3841 字
 [GitHub](/tags/github) [脆弱性](/tags/%E8%84%86%E5%BC%B1%E6%80%A7) [GitHub Actions](/tags/github-actions) [Supply Chain](/tags/supply-chain)

(You can read this article in [English here](/post/github-actions-staff-access-token-en/).)

## 免責事項

GitHubはBug Bountyプログラムを実施しており、その一環として脆弱性の診断行為を[セーフハーバー](https://docs.github.com/en/site-policy/security-policies/github-bug-bounty-program-legal-safe-harbor)により許可しています。
本記事は、そのセーフハーバーの基準を遵守した上で調査を行い、その結果発見した脆弱性に関して解説したものであり、無許可の脆弱性診断行為を推奨することを意図したものではありません。
GitHub上で脆弱性を発見した場合は、[GitHub Bug Bounty](https://hackerone.com/github?type=team)へ報告してください。

## 要約

GitHub Actionsのランナーのソースコードをホストする[actions/runner](https://github.com/actions/runner)リポジトリにおいて、セルフホストランナーの使用方法に不備があり、結果としてGitHub Actionsに登録されているPersonal Access Tokenの窃取が可能だった。
このトークンはGitHubスタッフのアカウントに紐づいていたため、当該のスタッフとして各種操作を行うことができた。
これにより、潜在的に[actions/checkout](https://github.com/actions/checkout)や[actions/cache](https://github.com/actions/cache)といったようなリポジトリに対して悪意あるコードを挿入できる可能性が存在した。

## セルフホストランナーとは

セルフホストランナーとは、名前の通りGitHub Actionsのランナーをユーザーが所有するサーバー等で実行することができる機能であり、主にハードウェア的な要件が存在するCI等で使用されているケースが多い。
この機能はGitHub Actionsのランナーをユーザーの環境にインストールすることで実現されているのだが、このランナーは実行毎に環境の隔離を行わないため、別途ユーザーが環境の隔離などを行わない限り、ジョブ間でシステムの状態が共有されるという仕様となっている。これは、信頼されているワークフローのみが実行される状況であればセキュリティ上の問題とはならない。

## pull\_requestトリガー

しかしながら、GitHub Actionsには`pull_request`と呼ばれるワークフローのトリガーが存在する。
これは、プルリクエストに関連したイベントが発生した際にGitHub Actions上でコードを実行するトリガーなのだが、このトリガーは実行するワークフローの定義ファイルをフォークしたリポジトリから読み取り[1](#fn:1)、ベースリポジトリのコンテキストで、コンテンツに対する読み取り権限のみが付与されたトークンを渡された状態で実行される。
つまり、公開リポジトリにおいては、フォークしたリポジトリから任意のワークフローを実行できるということになる。[2](#fn:2)

![pull_requestトリガーの挙動を示す図](/img/github-actions-pull-request-trigger.svg)

GitHubがホストするランナーを使用している際はワークフロー実行毎に環境が初期化されるため何ら問題ない挙動なのだが、セルフホストランナーを利用しているケースにおいては実行毎に環境が初期化されないため、プルリクエスト内のワークフロー定義ファイルで、セルフホストランナーを実行環境として指定することで任意のコードを実行し、環境を汚染することができる。
これにより、後にそのセルフホストランナーが機密情報(例: 書き込み権限を持ったGitHubのトークン等)を受け取ったタイミングでその情報を窃取することが可能となる。

この挙動に関しては[GitHubのドキュメントにも明示的に記載](https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners#self-hosted-runner-security)されており、セルフホストランナーはパブリックリポジトリで使用するべきではないとされている。

## 脆弱性が存在したワークフロー

さて、ここまでの前提を踏まえた上で、実際に脆弱性が存在したワークフローの内容を見ていく。
[actions/runner](https://github.com/actions/runner)には、[e2etest.yml](https://github.com/actions/runner/blob/a9be5f65578a8225c6a024799f572ad2066c4fd8/.github/workflows/e2etest.yml)と呼ばれるE2Eテスト用のワークフローが存在した。[3](#fn:3)

このワークフローは、要約すると以下のような処理を行う:

1. 現在リポジトリに登録されているセルフホストランナーの一覧を取得し、それらを全て削除する。
2. ランナーを異なるアーキテクチャ及びOS(Linux/Windows/macOS)向けにそれぞれビルドする。
3. 以下の処理を行うスクリプトを非同期に実行する。
   　1. 現在リポジトリに登録されているセルフホストランナーの一覧を取得する。
   　2. 取得した一覧から、E2Eテストに使用されるべきランナーを探し、ランナー上でOSに対応するテストを実行する。
   　3. テスト実行対象のランナーが全て見つかったら、処理を終了する。そうでなければ処理を続行。
   　4. APIレートリミットを避けるため、10秒間スリープする。
   　5. 手順3-1に戻る。
4. セルフホストランナーを起動するため、それぞれのアーキテクチャ及びOSの組み合わせに対して、以下のような処理を実行する。
   　1. 手順2でビルドした実行可能ファイルをダウンロードする。
   　2. セルフホストランナーを設定し、actions/runnerリポジトリへ登録する。
   　3. 手順3で実行されたスクリプトからジョブが実行されるのを待つ。
   　4. 受信したジョブを実行する。
   　5. actions/runnerリポジトリからセルフホストランナーを削除。
   　6. テスト結果をアップロードする。
5. テストが全て終了したら、アップロードされたテスト結果を解析する。

一見すると、このワークフローはセルフホストランナーを使用した後、再利用していないため前述の攻撃は不可能であるように思える。
しかしながら、これらの手順には不備があり、ここで使用されているセルフホストランナー上で任意のコードを実行することが可能だった。

## このワークフローの問題点

前述した手順において、手順3でスクリプトが非同期に実行されるのを覚えているだろうか。
このスクリプトはAPIのレートリミットを避けるため、登録されたセルフホストランナーの一覧を取得する度に10秒間スリープするという仕様となっていた。
つまり、手順4-2でセルフホストランナーが登録されてから、手順3-2でランナーに対してジョブが送信されるまでに、最大で10秒強の遅延がある。

`セルフホストランナーとは`セクションで解説した通り、セルフホストランナーはプルリクエストから任意のジョブを実行することができるため、この10秒間の遅延の間に悪意あるプルリクエストを送信することで、セルフホストランナー上で任意のコードを実行し、後続の処理を汚染されたランナー上で実行することが可能だった。
さて、ここで後続の処理の内容を見ると、手順4-5でactions/runnerリポジトリからセルフホストランナーを削除している。
通常、GitHub Actionsでランナーに渡されるGitHub Tokenはセルフホストランナーを操作する権限を持たないため、以下のようにGitHubのPersonal Access Tokenを利用してセルフホストランナーの登録/削除を行っていた。

[.github/workflows/e2etest.yml 165行目～178行目](https://github.com/actions/runner/blob/a9be5f65578a8225c6a024799f572ad2066c4fd8/.github/workflows/e2etest.yml#L165-L178)

```
      - name: Configure Runner
        env:
          unique_runner_name: linux-x64-${{needs.init.outputs.unique_runner_label}}
        run: |
          ./config.sh --url ${{github.event.repository.html_url}} --unattended --name $unique_runner_name --pat ${{secrets.PAT}} --labels $unique_runner_name --replace
      - name: Start Runner and Wait for Job
        timeout-minutes: 5
        run: |
          ./run.sh --once
      - name: Remove Runner
        if: always()
        continue-on-error: true
        run: |
          ./config.sh remove --pat ${{secrets.PAT}}
```

ジョブを実行するのは`Start Runner and Wait for Job`という名前のステップであるため、後続の`Remove Runner`においては既にランナーを汚染することができている。
つまり、`./config.sh remove --pat ${{secrets.PAT}}` で渡されている`secrets.PAT`の中身を窃取することが可能となっていた。

## 影響

さて、ここで`secrets.PAT`の中身は誰に紐づいているのか、という点が問題となってくる。
幸いにも、このトークンは別の箇所でワークフローの実行に使用されていたため、容易にトークンの所有者を特定することができた。

![実行者の名前を黒塗りにしたワークフローの実行履歴画面](/img/github-actions-runner-pat-owner.png)

そこで、当該のユーザーのプロフィールを確認したところ、[@actions](https://github.com/actions)だけではなく[@github](https://github.com/github)にも所属していることが確認できた。
前述の通り、このトークンは複数の目的に利用されているため、最低でも`public_repo`スコープを持っていることが推察できる。
そのため、この脆弱性を悪用し、トークンの窃取を行うことで、[@actions](https://github.com/actions)及び[@github](https://github.com/github)の公開リポジトリに対する書き込み権限を得ることができたものと思われる。
これは、[actions/checkout](https://github.com/actions/checkout)や[actions/cache](https://github.com/actions/cache)といったようなリポジトリを含んでいたため、これらのリポジトリに対して変更を加えることで、膨大な数のGitHubリポジトリに対して影響が及ぶ可能性があった。

## まとめ

今回の記事では、GitHub Actionsの設定ミスがどのようにして深刻なサプライチェーンへのリスクへ繋がるのかについて解説を行いました。
脆弱性を報告してからこの記事を執筆し始めるまで1年以上かかってしまいましたが、以前から公開したいと考えていた記事だったため、楽しんでいただけましたら幸いです。

本記事に関する質問/感想はTwitter([@ryotkak](https://twitter.com/ryotkak))またはMisskey([@[email protected]](https://misskey.io/%40ryotak))までお願いいたします。

## タイムライン

| 日付 (日本時間) | 出来事 |
| --- | --- |
| 2021/06/19 | 脆弱性の発見/報告 |
| 2021/06/19 | 一時対応完了 |
| 2021/06/22 | 対応完了 |
| 2022/12/18 | 記事の執筆を開始 |
| 2023/04/11 | 記事の公開許可が出る |
| 2023/04/22 | 本記事の公開 |

---

1. より詳しく言うと、プルリクエストのマージコミット時点のワークフローの定義ファイルを使用します。 [↩︎](#fnref:1)
2. 正確には、GitHubが加えた[この変更](https://github.blog/changelog/2021-04-22-github-actions-maintainers-must-approve-first-time-contributor-workflow-runs/)により、最低一度対象のリポジトリに対してコントリビュートをしていないと、自動でワークフローが実行されません。 [↩︎](#fnref:2)
3. 合計で300行以上あるためコードの記載は行いませんが、ワークフローの内容はこちらから確認できます: <https://github.com/actions/runner/blob/a9be5f65578a8225c6a024799f572ad2066c4fd8/.github/workflows/e2etest.yml> [↩︎](#fnref:3)

### ページ

* [Home](/)
* [Archives](/archives/)
* [About](/about/)
* [Search](/search/)
* [RSS](/index.xml)

### リンク

* [Twitter](https://twitter.com/ryotkak)
* [GitHub](https://github.com/Ry0taK)
* [Website](https://ryotak.net)

### タグ

[Brute Force](/tags/brute-force/)
[Bug Bounty](/tags/bug-bounty/)
[Cdnjs](/tags/cdnjs/)
[Cloudflare](/tags/cloudflare/)
[CTF](/tags/ctf/)
[Definitely Typed](/tags/definitely-typed/)
[Deno](/tags/deno/)
[Fleet](/tags/fleet/)
[GitHub](/tags/github/)
[GitHub Actions](/tags/github-actions/)
[Go](/tags/go/)
[Homebrew](/tags/homebrew/)
[IDOR](/tags/idor/)
[IX2105](/tags/ix2105/)
[MAP-E](/tags/map-e/)
[Microsoft](/tags/microsoft/)
[NVR500](/tags/nvr500/)
[Privilege Escalation](/tags/privilege-escalation/)
[PyPI](/tags/pypi/)
[Python](/tags/python/)
[RCE](/tags/rce/)
[Ruby](/tags/ruby/)
[SECCON](/tags/seccon/)
[Supply Chain](/tags/supply-chain/)
[Timing Attack](/tags/timing-attack/)
[Twitter](/tags/twitter/)
[TypeScript](/tags/typescript/)
[VSCode](/tags/vscode/)
[Vulnerability](/tags/vulnerability/)
[Web](/tags/web/)
[Writeup](/tags/writeup/)
[ホームゲートウェイ](/tags/%E3%83%9B%E3%83%BC%E3%83%A0%E3%82%B2%E3%83%BC%E3%83%88%E3%82%A6%E3%82%A7%E3%82%A4/)
[脆弱性](/tags/%E8%84%86%E5%BC%B1%E6%80%A7/)

### ページ

* [Home](/)
* [Archives](/archives/)
* [About](/about/)
* [Search](/search/)
* [RSS](/index.xml)

### リンク

* [Twitter](https://twitter.com/ryotkak)
* [GitHub](https://github.com/Ry0taK)
* [Websit...