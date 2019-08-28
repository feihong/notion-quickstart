from notion.client import NotionClient
import secrets

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
client = NotionClient(token_v2=secrets.TOKEN)

url = 'https://www.notion.so/chicagochinese/19367d1bc800405fbfa5698679eec62c?v=e838eab67c3a48d1b6d47c6fe11a1e1b'

page = client.get_block(url)

print(page.title)

for row in page.collection.get_rows():
  print(row.title)
  print(row.chinese_title)
  # print(row.get_all_properties())
