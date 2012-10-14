__author__ = 'harshit'

from BeautifulSoup import BeautifulSoup
from pyGTrends import pyGTrends
import urllib2
import csv
from csv import DictReader

def count_seo_result():

    reader_path = '/home/harshit/workspace/seo_script/uploads/'
    variable_csv = open( reader_path + 'keyword.csv', 'rb')
    folder_path = '/home/harshit/workspace/seo_script/downloads/'
    blog_search = csv.writer( open( folder_path + 'blog_search_result.csv', 'wb' ) )
    news_search = csv.writer( open( folder_path + 'news_search_result.csv', 'wb' ) )

    search_keywords = variable_csv.read().split(',')

    for keyword in search_keywords:
        __keyword = keyword.replace(' ','+')
        address_blog = "https://www.google.com/search?q=%s&tbs=blg:1,cdr:1,cd_min:1/2005,cd_max:1/2005&nav=m" % __keyword
        request_blog = urllib2.Request(address_blog, None, {'User-Agent':'Mosilla/5.0 '
                                                               '(Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
        html_data_blog = urllib2.urlopen(request_blog).read()
        soup_blog = BeautifulSoup(html_data_blog)
        blog_result_per_variable = str(soup_blog.findAll('div',attrs={'id':'resultStats'})[0]).split('About ')[1].split('results')[0]
        blog_search.writerow( [keyword,blog_result_per_variable] )


        address_news = "https://www.google.com/search?q=%s&tbs=nws:1,cdr:1,cd_min:1/2005,cd_max:1/2005&nav=m" % __keyword
        request = urllib2.Request(address_news, None, {'User-Agent':'Mosilla/5.0 '
                                                               '(Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})

        html_data_news = urllib2.urlopen(request).read()
        soup_news = BeautifulSoup(html_data_news)
        news_result_per_variable = str(soup_news.findAll('div',attrs={'id':'resultStats'})[0]).split('About ')[1].split('results')[0]
        news_search.writerow( [keyword,news_result_per_variable] )

def trend_csv_download():
    r = pyGTrends('my email', 'passwd')
    r.download_report(('spain', 'wine'))### read it from csv file
    print DictReader(r.csv().split('\n'))
trend_csv_download()