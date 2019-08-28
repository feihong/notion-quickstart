from notion.client import NotionClient
import secrets

client = NotionClient(token_v2=secrets.TOKEN)

url = 'https://www.notion.so/chicagochinese/19367d1bc800405fbfa5698679eec62c?v=e838eab67c3a48d1b6d47c6fe11a1e1b'

page = client.get_block(url)

print(page.title)

tv = client.get_collection_view(url, collection=page.collection)

# Print all rows in order:
for i, row in enumerate(tv.default_query().execute(), 1):
  print(f'{i}. {row.title}')
  print('   ', row.chinese_title if row.chinese_title else 'n/a')
