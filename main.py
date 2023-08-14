from bs4 import BeautifulSoup
import lxml
import requests
import smtplib

Amazon_url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
HEADER = {
    "Accept-Language": "en-US,en;q=0.9,zh;q=0.8,zh-CN;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

response = requests.get(Amazon_url,headers=HEADER)

soup = BeautifulSoup(response.content,"lxml")
# print(soup.prettify())

get_price = float(soup.find(class_="a-price-fraction").getText())
# print(get_price)

get_product = soup.find(id="productTitle").getText()

if get_price <= 90:
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:{get_product}price is decreasing!\n\n{Amazon_url}"
        )

