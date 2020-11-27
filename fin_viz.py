from utils.FFManager import FFManager


with FFManager('https://finviz.com/news.ashx') as ff_browser:
    data = ff_browser.find_element_by_xpath('//div[@class="news"]/table/tbody/tr[2]/td/table/tbody/tr[1]')

    # print(data.get_attribute("innerHTML"))

    news_content = data.find_element_by_class_name('nn-tab-link')

    title = news_content.text
    link = news_content.get_attribute('href')
    long_title = str(data.find_element_by_xpath('td[3]').get_attribute('title'))
    long_title = ((long_title.split("tab'>"))[1].split('</td>')[0])


print(title)
print(long_title)
print(link)


