# coding=utf-8
import requests
import json
import argparse

parser = argparse.ArgumentParser(description='LangSearch API')

parser.add_argument('--query', '-q', default='Highlights of Apple\'s 2024 ESG Report', help='The user`s search query.')
parser.add_argument('--freshness', '-f', default='noLimit', help='''
                    - oneDay: Results from the past 24 hours.
- oneWeek: Results from the past week.
- oneMonth: Results from the past month.
- oneYear: Results from the past year.
- noLimit: No time filter (default).
                    
                    ''')
parser.add_argument('--summary', '-s', action='store_true', default=True, help='Whether to show long text summaries for results.')
parser.add_argument('--count', '-c', type=int, default=10, help='The number of results to return. Possible range: 1-10 (default is 10).')














args = parser.parse_args()

url = "https://api.langsearch.com/v1/web-search"

payload = json.dumps({
   "query": args.query,
   "freshness": args.freshness,
   "summary": args.summary,
   "count": args.count
})

headers = {
   'Authorization': 'sk-0df7fa57cb5d45d3b864eb57a6400081',
   'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)