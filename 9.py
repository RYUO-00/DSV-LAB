import urllib.request
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import ssl

# Ignore certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.geeksforgeeks.org/how-to-automate-an-excel-sheet-in-python/?ref=feed"

html = urllib.request.urlopen(url, context=ctx)

htmlParse = BeautifulSoup(html, "html.parser")

p = htmlParse.find("p").get_text()
print(p)


def cvc(text):
    vowels = 'AEIOUaeiou'
    vowelcount = 0
    consonantcount = 0

    for char in text:
        if char in vowels:
            vowelcount += 1
        elif char.isalpha():
            consonantcount += 1

    return vowelcount, consonantcount


vowelcount, consonantcount = cvc(p)

categories = ['Vowels', 'Consonants']
values = [vowelcount, consonantcount]
print(values)

plt.pie(values, labels=categories, autopct='%1.1f%%')
plt.show()
