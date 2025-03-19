import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time

driver = webdriver.Chrome()
base_url = "https://kr.investing.com/economic-calendar"
sub_url = "samsung-electronics-co-ltd"

driver.get(base_url)

soup = bs(driver.page_source, 'html.parser')

table = soup.find(id_="economicCalendarData")

# # div 태그 중 class가 news_section이라는 태그를 추출 
# div_data = soup.find(
#     'div', 
#     attrs = {
#         'class' : 'news_section'
#     }
# )

# li_list = div_data.find_all('li')

# # href의 속성 값을 이용하여 새로운 리스트 생성
# href_list = []

# for li_data in li_list:
#     # li_data에서 첫번째 a태그를 추출 -> href 속성의 값을 추출
#     data = li_data.find('a')['href']
#     # href_list에 추가 
#     href_list.append(data)
   
# print(href_list)
 
# result = []

# for href in href_list:
#     try:
#         driver.get(base_url + href)
#         news_soup = bs(driver.page_source, 'html.parser')
#         time.sleep(2)
        
#         news_title = news_soup.find(
#             'h2',
#             attrs={
#                 'id' : 'title_area'
#             }
#         ).get_text()
        
#         news_content = news_soup.find(
#             'div',
#             attrs={
#                 'id' : 'newsct_article'
#             }
#         ).get_text().replace('\n','').replace('\t','')
        
#         news_dict = {
#             'title' : news_title,
#             'content' : news_content
#         }
        
#         result.append(news_dict)
#         print(news_title)
#     except:
#         continue
    
# df = pd.DataFrame(result)
# df.to_csv(f'naver_{code}.csv', index=False)