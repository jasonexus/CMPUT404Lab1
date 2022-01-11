import requests
print(requests.__version__)
url = "https://www.google.com/"
res = requests.get(url)
my_url = "https://raw.githubusercontent.com/jasonexus/CMPUT404Lab1/master/404lab1.py"
r = requests.get(my_url)
source_code = r.text
print(source_code)