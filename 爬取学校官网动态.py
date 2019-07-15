from selenium import webdriver
import time
import json


def main():
    list = []
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    }
    driver = webdriver.Chrome(executable_path=r'D:\py\chromedriver.exe')  # 使用selenium代理打开页面
    try:
        driver.get('http://www.ecjtu.jx.cn/')
        try:
            comments = driver.find_element_by_xpath('//*[@id="wp_news_w3"]/table/tbody')
            print(comments.text,'\n')
            time.sleep(10)
            comments = driver.find_element_by_xpath('//*[@id="wp_news_w3"]/table/tbody')
            print(comments.text)
        except Exception as e:
            print('点击失败'+e)
    except Exception as e:
        print('失败'+ e)
        #driver.close()
    #driver.close()
    #driver.close()#关闭窗口
    print("窗口已经关闭！")

if __name__ == '__main__':
    main()
