from playwright.sync_api import sync_playwright
import json

def main():
    with sync_playwright() as pw:
        # 啟動瀏覽器，headless=True (預設) 表示在背景執行，不會跳出視窗
        # 對於抓取，通常使用 True 以提高效能
        # 調試時可以設為 False 來看瀏覽器操作
        browser = pw.webkit.launch(headless=True) 
        page = browser.new_page()
        
        # 前往目標網址
        print("🚀 正在前往 http://quotes.toscrape.com ...")
        page.goto("http://quotes.toscrape.com")
        
        print("🔍 開始抓取名言...")

        # 步驟 1: 定位到所有包含名言的 "div.quote" 元素
        # .all() 會返回一個 Locators 列表，我們可以遍歷它
        quote_locators = page.locator("div.quote").all()

        scraped_data = []

        # 步驟 2: 遍歷 (Loop) 每個名言區塊
        for quote_locator in quote_locators:
            
            # 步驟 3: 在每個區塊內部，使用相對定位器
            # .locator(".text") 會在 "div.quote" 內部尋找 ".text"
            text = quote_locator.locator(".text").text_content()
            author = quote_locator.locator(".author").text_content()
            
            # 整理資料
            data = {
                "text": text.strip("“”"), # 清理多餘的引號
                "author": author.strip()
            }
            scraped_data.append(data)

        print(f"✅ 抓取完成！共 {len(scraped_data)} 則名言。")
        
        # 步驟 4: 儲存或打印結果
        print(json.dumps(scraped_data, indent=2, ensure_ascii=False))
        
        browser.close()

if __name__ == "__main__":
    main()