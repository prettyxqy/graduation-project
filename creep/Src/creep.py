import requests
from bs4 import BeautifulSoup
from policy import Policy

if __name__ == "__main__":

  policies = []

  zx_res = requests.get("http://www.gov.cn/zhengce/zuixin.htm")
  zx_res.encoding = 'utf-8'
  zx_doc = BeautifulSoup(zx_res.text, features="lxml")
  latest_policies = zx_doc.select("body > div.main > div > div > div.news_box > div > ul > li > h4")
  # print(latest_policies)
  for lp in latest_policies:
    a = lp.find('a')
    s = lp.find('span')
    
    link = a['href'].strip()
    print(link)
    if not link.startswith("http://www.gov.cn"):
      link = "http://www.gov.cn" + link

    res = requests.get(link)
    res.encoding = 'utf-8'
    doc = BeautifulSoup(res.text, features="lxml")
    content = doc.select_one("#UCAP-CONTENT").get_text()

    policy = Policy()
    policy.set_metadata(title=a.get_text().strip(), time=s.get_text().strip(), category="not known")
    policy.set_content(content)
    policies.append(policy)

  # 打印最后一条政策，查看效果
  print(policies[-1])
