import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from time_utils import TimeUtils
try:
   
    # webDriver를 설정
    chrome_options = webdriver.ChromeOptions()
    # 창 안뜨게 추가
    chrome_options.headless =True
    driver = webdriver.Chrome('../chromedriver.exe', options=chrome_options)
    #driver = webdriver.Chrome('../chromedriver.exe', chrome_options=chrome_options)
    # DeprecationWarning: use options instead of chrome_options 경고 떠서 바꿈
    driver.implicitly_wait(3)
    url = 'http://www.naver.com'

    banner_list = []
    for index in range(0,3):
        # url으로 이동
        driver.get(url)
        #오른쪽 롤링배너 frame 찾아냄
        driver.switch_to.frame('da_iframe_rolling')
        find_elem = driver.find_element_by_id('addiv').find_elements_by_tag_name('img')
        
        print('find_elem', find_elem)
       
        for elem in find_elem:
            print('elem alt', elem.get_attribute('alt'))
            print('elem img', elem.get_attribute('src'))
            dupCheck = False
            #중복체크
            for img in banner_list:
                if 'alt' in img:
                    #print(' in >>>>' , img['alt'])
                    if elem.get_attribute('alt') in img['alt']:
                        dupCheck = True
                        
            if not dupCheck:
                image = {
                    'alt' : elem.get_attribute('alt'),
                    'src' : elem.get_attribute('src')
                }
                banner_list.append(image)      
    #닫음
    driver.quit()
    # print(banner_list)
    if len(banner_list)>0 :
        dataframe = pd.DataFrame(banner_list)
        dataframe.columns=['alt', 'src']
        print('dataframe >>' , dataframe)
        time_utils = TimeUtils()
        print(time_utils.get_today_string())
        flie_name = 'naver_crawling_banner_'+time_utils.get_today_string()+'.csv'
        dataframe.to_csv(flie_name, header=True, index=False,  encoding='euc-kr')
    
except Exception as e:
    print("raise Exception : " + str(e))
