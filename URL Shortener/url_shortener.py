import pyshorteners

url = input("Enter a link: ")

print("URL after shortening: ", pyshorteners.Shortener().tinyurl.short(url))