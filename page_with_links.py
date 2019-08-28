from notion.client import NotionClient
import secrets

client = NotionClient(token_v2=secrets.TOKEN)

url = 'https://www.notion.so/chicagochinese/Translations-f19fbfaa306340b18490fbdff9181993'

page = client.get_block(url)

print(page.title)

for child in page.children:
  print(child.title)
  print(child.get_browseable_url())
