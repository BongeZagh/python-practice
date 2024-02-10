import whois

def get_country_from_whois(url):
    domain = url.split('//')[-1].split('/')[0]
    
    try:
        w = whois.whois(domain)
        country = w.country
        return country
    except Exception as e:
        print(f"Whois查询出错：{str(e)}")
        return None

# 测试示例
url = "http://www.sinochip-ic.com/"
country = get_country_from_whois(url)
if country:
    print(f"The website {url} is located in {country}.")
else:
    print("无法获取国家信息。")
