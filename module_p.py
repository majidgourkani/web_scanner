from pickletools import read_uint1
from tkinter.messagebox import NO
from xml import dom
import requests
import bs4
import re

def domain_finder(s):
    exp = r'\bhttps?://(?:www\.|ww2\.)?((?:[\w-]+\.){1,}\w+)\b'
    r = re.compile(exp, re.M)
    if r.findall(s) == None:
        return False
    else:
        return r.findall(s)[0]

def has_same_domain(domain, s, sub_domains):
    n_domain = domain_finder(s)
    if n_domain == domain:
        return True
    else:
        if (domain in n_domain) and (n_domain not in sub_domains):
            sub_domains.append(n_domain)
        return False


def crawler(page, urls, domain, method, sub_domains):
    tmp_urls = []
    tags = page.find_all('a')
    for i in tags:
        tmp_urls.append(str(i.get('href')))
    for u in tmp_urls:
        if (u != '') and (u != None): 
            if u[0] == "/":
                u = method+domain+u
                if (u not in urls) and (has_same_domain(domain,u,sub_domains)):
                    urls.append(u)
            elif (u[0] == 'h'):
                if (u not in urls) and (has_same_domain(domain,u,sub_domains)):
                    urls.append(u)
            else:
                pass
    
    return urls

def base64_extractor(page, ciphers):
    pass

def hiden_form():
    pass

def header_info():
    pass

def admin_panel(url):
    fh = open('uniq_paths.txt', 'r')
    for l in fh.readlines():
        t_res = requests.get(url+l.replace('\n',''))
        if t_res.status_code == 200:
            print(url+l.replace('\n',''))

def comments(page, a_comment):
    comment = page.find_all(string=lambda text: isinstance(text, bs4.Comment))
    for c in comment:
        if c not in a_comment:
            a_comment.append(c)
    return a_comment

def cookies(res, a_cookie):
    cookies = list(res.cookies)
    for c in cookies:
        if c.name not in a_cookie.keys():
            a_cookie[c.name] = "name: {}\t, secure: {}\t, expire: {}\t, Value: {}".format(c.name, c.secure, c.expires, c.value)
        # httpOnly: {},
        #c._rest['HttpOnly']
    return a_cookie

def robot_txt(url):
    dis_a = []
    l_a = []
    res = requests.get(url+'/robots.txt')
    if res.status_code == 200:
        links = res.content.decode().split('\n')
        for x in links:
            if 'Disallow' in x:
                dis_a.append(x.split(':')[1].strip())
            elif 'Allow' in x:
                l_a.append(x.split(':')[1].strip())
    if len(l_a) == 0:
        print("There is no Allowed Linke in robots.txt")
    else:
        print("Allowed Links:")
        for x in l_a:
            print(url+x)
    if len(dis_a) == 0:
        print("There is no Disallowed Linke in robots.txt")
    else:
        print("Disallowed Links:")
        for x in dis_a:
            print(url+x)
            
def adminp_finder(url,l):
    if l == "c":
        f_handler = open('paths.txt', 'r')
    else:
        f_handler = open('list.txt', 'r')
    session = requests.session()
    print("Prabable admin page is: ")
    for x in f_handler.readlines():
        res=session.get(url+x)
        if res.status_code == 200:
            print(url+x)