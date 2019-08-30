from notion.client import NotionClient
import secrets

client = NotionClient(token_v2=secrets.TOKEN)

url = 'https://www.notion.so/chicagochinese/4e06dc81541f439e841a665f9dd315bf?v=e3b7c01c8afc45389e520fd7b02872c5'

page = client.get_block(url)

print(page.title)

tv = client.get_collection_view(url, collection=page.collection)

# Print all rows in order:
for i, row in enumerate(tv.default_query().execute(), 1):
  print(f'{i:02d}. {row.title}')
  print('   ', row.date.start)
  print('   ', row.link)
