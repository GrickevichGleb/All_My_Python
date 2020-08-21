#Here 'yield' is used instead of 'return'
#It makes this function act as 'function-generator'
#Now it will return data 'value by value' (tuple by tuple)
#And can interact with external cycle

#When 'yield' its not return from the function
#It pauses, and 'function-generator' waits for external iterator cycle
#to return next value

import requests


def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url
    
