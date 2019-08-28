from notion.client import NotionClient
import secrets

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
client = NotionClient(token_v2=secrets.TOKEN)

url = 'https://www.notion.so/chicagochinese/19367d1bc800405fbfa5698679eec62c?v=e838eab67c3a48d1b6d47c6fe11a1e1b'

cv = client.get_collection_view(url)

# Print all rows (in no particular order):
# for row in cv.collection.get_rows():
#   print(row.title)

# Print all rows in order:
for i, row in enumerate(cv.default_query().execute(), 1):
  print(f'{i}. {row.title}')
  print('   ', row.chinese_title if row.chinese_title else 'n/a')
