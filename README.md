# discord-project
#環境和套件要求  
pyhton3  
beautifulsoup4  
request  
json  
discord.py   
re  
openpyxl  
pandas


# 軟體基本功能  
此軟體的使用方法有兩種
1.使用由開發者host的discord chatbot  
  透過連結:https://discord.com/api/oauth2/authorize?client_id=857974617909886986&permissions=0&scope=bot  
  將chatbot加入你的discord sever  
2.創建屬於自己的discord chatbot帳號
  登入discord網站創建自己的chatbot帳號之後取得其token  
  在bot.py中最後加入程式  bot.run('token')即可運行自己的discord chatbot
 
完成機器人的加入或創建後，以下是關於指令的說明 

使用方法:

注意: 課程名稱 教師 中間需有空白

首先先使用指令!connect連上資料庫才能使用其他的command

若超過30分鐘都沒指令，機器人會要求再次!connect

!connet :連結網路資料庫

!show 課程網網址: 從課程網取得課程資訊同時取得NTUcourse連結 ex:https://nol.ntu.edu.tw/nol/coursesearch/print_table.php?course_id=901%2032500&class=&dpt_code=9010&ser_no=25078&semester=109-2&lang=CH

!find  課程名稱 教師 : 提供查詢過的課程之一的完整資訊

!show_all : 將所有查詢過的課程以讚和倒讚來排序並一一列出基本資訊

!liked 課程名稱 教師 : 點讚

!disliked 課程名稱 教師 : 點倒讚

!comment 課程名稱 教師 comment內容 : 為課程新增註解，教師和comment內容中間也需要空白 

!clear 課程名稱 教師 : 刪除user對課程的所有註解，不會刪除其他user的註解

!add_to_schedule 課程名稱 教師 : 將課程加入課表，若發生衝堂則會以最新add的課程為主，並移除被衝堂課程

!delete_from_schedule 課程名稱 教師 : 將指定課程從課表中移除

!show_schedule : 於聊天室顯示課表以及總學分

!disconnect : 將所有資料上傳至網路資料庫，同時取消與網路資料庫的連結，若沒執行!disconnect則無法存檔

# 程式碼結構說明

Hash

    insert:傳入爬蟲爬到的資料，並整理加入hash table中
  
    search:輸入課程名稱+教師名稱，從hash table取得資料並回傳
  
    list_all:使用get_all_node得到所有node，用sort將node排序，以string將整理好的資訊回傳
  
    get_all_node:以list回傳所有node
  
    add_comment:輸入ctx(discord context 物件)、課程名稱+教師名稱+comment內容，更新node中的init資訊
  
    clear_comment:輸入ctx(discord context 物件)、課程名稱+教師名稱，刪除user的所有comment更新node中的init資訊
  
    great_points:輸入課程名稱+教師名稱，更新node中的init資訊
  
    disliked_points:輸入課程名稱+教師名稱，更新node中的init資訊
  
    save_data:將所有node資料寫入文件
  
Linked_list:

    push:輸入node，並連結上一個node

    show:將所有連結同一個root的node的資料以string輸出

node:

    init:儲存爬蟲所獲取的資料以及Linked_list中下一個連結的node
  
    output:以string輸出node的資訊
 
ClassSchedule:

    creat:輸入discord使用者名稱，創造課表
  
    add:輸入課程名稱+教師名稱、課表、discord使用者名稱，將課程加入課表
  
    delete:輸入課程名稱+教師名稱、課表、discord使用者名稱，將課程從課表刪除
  
    show:輸入discord使用者名稱，輸出課表
  
    show_credit:輸入discord使用者名稱，輸出目前使用者之選課學分
Save_data:  
    class Data: 創建一個自定義的Data物件，儲存不同伺服器創建的hash  
    save:透過傳入的ctx物件，判斷要儲存的data，並透過request模組和jsonstorage互動，將data轉為json檔並更新  
    load:透過傳入的ctx物件，判斷要讀取的data，並透過request模組和jsonstorage互動，將資料取下並insert進hash讓使用者可以access  
Web:
    show_info:傳入課程網連結，透過request模組爬取課程資料，以str形式回傳資料
  
