from pickletools import read_uint1
from xml import dom
import requests
import bs4
import re
import module_p

    
def main():
    print("Please enter URL: ")
    i_url = input()
    urls = []
    sub_domains = []
    redirects = []
    a_comment = []
    a_cookie = {}
    level = 's'
    domain = module_p.domain_finder(i_url)
    method = i_url.split(':')[0]+'://'
    module_p.robot_txt(i_url)
    module_p.adminp_finder(i_url, level)
    urls.append(i_url)
    for url in urls:
        if len(urls) >= 200:
            break
        else:
            res = requests.get(url)
            page = bs4.BeautifulSoup(res.text, 'html.parser')
            urls = module_p.crawler(page, urls, domain, method, sub_domains)
            #ciphers = module_p.base64_extractor(page, ciphers)
            #if (res.status_code >= 300) and (res.status_code <= 399):
            #    redirects = module_p.ear(res, redirects)
            a_cookie = module_p.cookies(res, a_cookie)
            a_comment = module_p.comments(page, a_comment)

    #temp part
    '''res = requests.get(i_url)
    page = bs4.BeautifulSoup(res.text, 'html.parser')
    urls = module_p.admin_panel(i_url)'''
    for x in urls:
        print(x)
    print("__________________________________________")
    for x in sub_domains:
        print(x)
    print("__________________________________________")
    for x in a_comment:
        print(x)
    print("__________________________________________")
    for k,v in a_cookie.items():
        print(v)
    
if __name__ == "__main__":
    main()