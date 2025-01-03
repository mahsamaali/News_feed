from pygooglenews import GoogleNews

gn = GoogleNews()

s = gn.search('NFT -bitcoin')

print(s['feed'].title)