from playwright.sync_api import sync_playwright
import os
from time import sleep

def main():
    with sync_playwright() as p:
        # 啟動瀏覽器（有頭模式）
        browser = p.chromium.launch(headless=False,slow_mo=500)
        page = browser.new_page()

        # 取得當前檔案的絕對路徑
        current_dir = os.path.dirname(os.path.abspath(__file__))
        html_file = os.path.join(current_dir,"form_demo.html")
        # print(f"file://{html_file}")

        # 訪問本地 HTML 檔案
        page.goto(f"file://{html_file}")

        # 填寫表單
        page.fill("input#name","張三")
        page.fill("input#email","zhang@example.com")
        page.select_option("select#country","Taiwan")
        page.check("input#subscribe")

        # 點擊提交按鈕
        page.click("button#submit")

        # 等待導航完成
        page.wait_for_load_state("networkidle") # 等待頁面完全載入

        # 等待一下讓使用者看到結果
        page.wait_for_timeout(2000) # 等待網路閒置

        # 關閉瀏覽器
        browser.close()


if __name__ == "__main__":
    main()

# 這個範例會自動開啟 form_demo.html 測試頁面，並執行表單填寫與提交的完整流程。