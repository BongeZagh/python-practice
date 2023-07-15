import subprocess

# 定义要测试的域名
domain = "papals.org"

# 定义要测试的DNS服务器地址和备注信息
dns_servers = [
  ("8.8.8.8", "Google DNS"),
  ("1.1.1.1", "Cloudflare DNS"),
  ("208.67.222.222", "OpenDNS"),
  ("61.132.163.68", "安徽电信 DNS"),
  ("61.128.192.68", "重庆电信 DNS"),
  ("218.85.152.99", "福建电信 DNS"),
  ("202.100.64.68", "甘肃电信 DNS"),
  ("202.96.128.86", "广东电信 DNS"),
  ("202.96.134.33", "广东电信 DNS"),
  ("202.103.225.68", "广西电信 DNS"),
  ("202.98.192.67", "贵州电信 DNS"),
  ("222.88.88.88", "河南电信 DNS"),
  ("219.147.198.230", "黑龙江电信 DNS"),
  ("202.103.24.68", "湖北电信 DNS"),
  ("222.246.129.80", "湖南电信 DNS"),
  ("218.2.2.2", "江苏电信 DNS"),
  ("61.147.37.1", "江苏电信 DNS"),
  ("202.101.224.69", "江西电信 DNS"),
  ("219.148.162.31", "内蒙古电信 DNS"),
  ("219.146.1.66", "山东电信 DNS"),
  ("218.30.19.40", "陕西电信 DNS"),
  ("202.96.209.133", "上海电信 DNS"),
  ("202.96.209.5", "上海电信 DNS"),
  ("61.139.2.69", "四川电信 DNS"),
  ("219.150.32.132", "天津电信 DNS"),
]

# 循环测试每个DNS服务器
for dns_server, dns_name in dns_servers:
    print("Testing DNS server:", dns_name, "({})".format(dns_server))
    
    # 使用subprocess模块运行dig命令测试DNS服务器
    cmd = ["dig", "+short", "@" + dns_server, domain]
    output = subprocess.check_output(cmd).decode().strip()
    
    # 输出测试结果
    if output == "":
        print("DNS server returned no result")
    else:
        print(output)
    
    print("")