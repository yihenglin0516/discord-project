# discord-project
#環境和套件要求  
pyhton3  
beautifulsoup4  
request  
json  
discord.py 
re'\n'
openpyxl\n
pandas\n

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

!find  課程名稱 教師:提供查詢過的課程之一的完整資訊

!show_all : 將所有查詢過的課程以讚和倒讚來排序並一一列出基本資訊

!liked 課程名稱 教師: 點讚

!disliked 課程名稱 教師: 點倒讚

!comment 課程名稱 教師 comment內容:為課程新增註解，教師和comment內容中間也需要空白 

!clear 課程名稱 教師: 刪除user對課程的所有註解，不會刪除其他user的註解

!add_to_schedule 課程名稱 教師:將課程加入課表，若發生衝堂則會以最新add的課程為主，並移除被衝堂課程

!show_schedule :於聊天室顯示課表以及總學分

!disconnect :將所有資料上傳至網路資料庫，同時取消與網路資料庫的連結，若沒執行!disconnect則無法存檔

# 程式碼結構說明


