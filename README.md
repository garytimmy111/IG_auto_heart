Instagram自動按愛心
=========

<img src="https://imgur.com/hrOvWEe.png"/>

此專案目的只為了學術技術分享，請勿拿來從事不法行為，違者自行負起法律責任

```
貼心提醒：

刑法第三百五十八條：「 無故輸入他人帳號密碼、破解使用電腦之保護措施或利用電腦系統之漏洞，而入侵他人之電腦或其相關設備者，處三年以下有期徒刑、拘役或科或併科十萬元以下罰金。 」 刑法第三百六十三條：「第三百五十八條至第三百六十條之罪，須告訴乃論。」
```

Instagram自動按愛心，但還是必須要使用一個帳號，來做為機器人使用。雖然其中程式碼，已經盡量模仿人的行為，來避免被判定為機器人，但還是`請自行負擔被封鎖的可能`。




目錄
=================
* [事前必要準備](#事前必要準備)
* [範例](#範例)
* [檔案說明](#檔案說明)
    * [Windows/chromedriver.exe](#Windowschromedriverexe)
    * [Windows/phantomjs.exe](#Windowsphantomjsexe)
    * [Linux/chromedriver](#Linuxchromedriver)
    * [Linux/phantomjs](#Linuxphantomjs)
    * [IG自動按愛心.py](#IG自動按愛心py)
 
事前必要準備
=================
1. 必須要下載Chrome，若是在DOS沒有圖形化介面，也必須要下載Chrome。
2. [ChromeDriver請依照自己Chrome的版本進行下載](https://chromedriver.chromium.org/downloads)，若不知道自己Chrome，可以[到這裡進行查看](https://chromedriver.storage.googleapis.com/LATEST_RELEASE)。
4. [phantomjs若版本不合，請自行下載。](https://phantomjs.org/download.html)
5. phantomjs下載完以後，請依照作業系統擺放，如下圖。
<img src="https://i.imgur.com/vxk2PXt.png"/>

範例
=================

1. cd到IG自動按愛心.py的目錄上，執行檔案。

```
python IG自動按愛心.py
```

2. 輸入您的IG帳號密碼、FB帳號密碼、想發送的tag，即可開始自動按愛心。FB帳號密碼的部分依照您的帳號，若您的IG登入只需要本身的IG帳號，不需要再切換到FB再登入一次的話，FB帳號密碼的部分可以不打，直接按Enter跳過。tag的部分為想按讚的關鍵字，譬如我想要到#guitar、#music這兩個tag下面按讚，則須輸入「guitar music」，以空白做間格。


檔案說明
=================

### Windows/chromedriver.exe
Windows系統的chrome模擬器，64位元，若無法執行請自行另外做調整[下載](https://chromedriver.chromium.org/downloads)。

### Windows/phantomjs.exe
Windows系統的phantomjs，64位元，若無法執行請自行另外做調整[下載](https://phantomjs.org/download.html)。

### Linux/chromedriver
Linux系統的chrome模擬器，64位元，若無法執行請自行另外做調整[下載](https://chromedriver.chromium.org/downloads)。

### Linux/phantomjs
Linux系統的phantomjs，64位元，若無法執行請自行另外做調整[下載](https://phantomjs.org/download.html)。


### IG自動按愛心.py
主程式部分
