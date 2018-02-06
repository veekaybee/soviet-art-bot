import re

link = 'https://uploads8.wikiart.org/images/aleksandr-deyneka/winter-in-kursk-1916.jpg'
regex_search = re.search(r'[a-z-0-9]+.jpg', link)

print(regex_search)

if regex_search:
    regex = regex_search.group(0)
    print(regex)
