import os
import time
import requests
import sys

def retrieve_html():
    for year in range(2013,2019):
        for month in range(1,13):
            if month<10:
                
                url="https://en.tutiempo.net/climate/0{}-{}/ws-432950.html".format(month, year)
            else:
                url="https://en.tutiempo.net/climate/{}-{}/ws-432950.html".format(month, year)
            texts= requests.get(url)
            text_utf=texts.text.encode('utf=8')
            if not os.path.exists('Data/html_data/{}'.format(year)):
                os.makedirs('Data/html_data/{}'.format(year))
            with open('Data/html_data/{}/{}.html'.format(year,month),'wb') as output:
                output.write(text_utf)
        sys.stdout.flush()

        sys.stdout.flush()
if __name__=='__main__':
    start=time.time()
    retrieve_html()
    stop= time.time()
    print('time taken: {}'.format(stop-start))