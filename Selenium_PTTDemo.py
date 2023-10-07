# -------------------------------------------------------------------載入相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# -------------------------------------------------------------------設定Chrome Driver 的執行檔案路徑
# Chrome 114版載點 : https://google-chrome.cn.uptodown.com/windows/download/104298869
options = Options()
options.executable_path = "D:\Selenium\chromedriver.exe"
options.add_argument("--auto-open-devtools-for-tabs")  # 開啟F12

# -------------------------------------------------------------------建立Driver 物件實體，用程式操作 瀏覽器 運作
driver = webdriver.Chrome(options=options)
driver.maximize_window() # 視窗最大化

# -------------------------------------------------------------------指定存取網址
url="https://www.ptt.cc/bbs/HatePolitics/index4078.html"
driver.get(url)
time.sleep(1)


# -------------------------------------------------------------------抓到最新按鍵 並點擊
NewBTN = driver.find_element(By.LINK_TEXT, '最新')
NewBTN.click()
time.sleep(2)

# -------------------------------------------------------------------滾動至底部
n=0
while n<1:
    n=n+1
    # 捲動視窗並載入更多內容
    # windows.scrollTo() : js滾動功能()中應填入座標，document.body.scrollHeight=底部
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(1)

# -------------------------------------------------------------------抓到想要文章標題 並點擊
GetArticle = driver.find_element(By.LINK_TEXT, '[公告] 政黑板主 參選進度')
GetArticle.click()
time.sleep(2)

# -------------------------------------------------------------------印出留言
getMSG = driver.find_elements(By.CLASS_NAME,'push')
for printMSG in getMSG:
    print(printMSG.text)

# -------------------------------------------------------------------滾動至底部
n=0
while n<1:
    n=n+1
    # 捲動視窗並載入更多內容
    # windows.scrollTo() : js滾動功能()中應填入座標，document.body.scrollHeight=底部
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(1)

# -------------------------------------------------------------------截圖
driver.save_screenshot("123.png")

# -------------------------------------------------------------------關閉此次執行的WebDriver
driver.close()


# 屬性定位方法：
# By.ID：使用元素的 ID 屬性進行定位。
# By.NAME：使用元素的 name 屬性進行定位。
# By.CLASS_NAME：使用元素的 class 屬性進行定位。
# By.TAG_NAME：使用元素的標籤名稱進行定位。
# By.LINK_TEXT：使用元素的鏈接文本進行定位。
# By.PARTIAL_LINK_TEXT：使用元素的部分鏈接文本進行定位。
# By.CSS_SELECTOR：使用 CSS 選擇器進行定位。
# By.XPATH：使用 XPath 表達式進行定位。

# 方法定位方式：
# find_element(by, value)：定位單個元素。
# find_elements(by, value)：定位多個元素。
