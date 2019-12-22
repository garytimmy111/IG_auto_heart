Instagram自動按愛心
=========

`此專案目的只為了學術技術分享，請勿拿來從事不法行為，違者自行負起法律責任`

Instagram自動按愛心，但還是必須要使用一個帳號，來做為機器人使用。雖然其中程式碼，已經盡量模仿人的行為，來避免被判定為機器人，但還是`請自行負擔被封鎖的可能`。


<img src="https://imgur.com/hrOvWEe.png"/>

目錄
=================
* [事前必要準備](#事前必要準備)
* [How to Use](#HowtoUse)
   * [變數tag](#變數tag)
   * [變數useEmail](#變數useEmail)
   * [變數usePass](#變數usePass)
   * [變數heart](#變數heart)
* [檔案說明](#檔案說明)
    * [Windows/chromedriver](#Windowschromedriver)
    * [Linux/chromedriver](#Linuxchromedriver)
    * [IG自動按愛心](#IG自動按愛心)
 
事前必要準備
=================
1. 必須要下載Chrome
2. 若是在DOS沒有圖形化介面，也必須要下載Chrome。
3. selenium工具的部分，還是要依照自己的OS做調整。
4. [phantomjs檔案過大放不上來，請自行下載。](https://phantomjs.org/download.html)
5. phantomjs下載完以後，請依照作業系統擺放，如下圖。
<img src="https://i.imgur.com/vxk2PXt.png"/>

How to Use
=================

### 變數tag

此變數用來控制你想要到哪個tag的網站，去裡面按愛心。

### 變數useEmail

使用者的Email，跟FB是一樣的。

### 變數usePass

使用者的密碼，因此這個檔案小心不要給別人，否則他就知道你的FB登入帳密了。

### 變數heart

設定總共要按多找張照片，沒有測試過能否一直執行，因此至少設定一個斷點，否則`被封鎖得不償失`。

檔案說明
=================

### Windows/chromedriver
Windows系統的chrome模擬器，64位元，若無法執行請自行另外做調整

### Linux/chromedriver
Linux系統的chrome模擬器，64位元，若無法執行請自行另外做調整

### IG自動按愛心
主程式部分
