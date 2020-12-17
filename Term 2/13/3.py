import requests
# in nazashte budid
from bs4 import BeautifulSoup
url = "https://bama.ir/car/peykan/all-models/all-trims?page=1"

# data = requests.get(url+str(i))
data = requests.get(url)
soup = BeautifulSoup(data.text, "html.parser")
p_tags = soup.find_all('p', class_ = "shortdesc removeEmoji")
# for p_tag in p_tag:
for p_tag in p_tags:
    print (p_tag.text)