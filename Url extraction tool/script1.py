from urllib.request import urlopen

page = urlopen("https://www.google.com")
print(page.headers)
