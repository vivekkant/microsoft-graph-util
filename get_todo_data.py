from azure.identity import InteractiveBrowserCredential
from msgraph.core import GraphClient

browser_credential = InteractiveBrowserCredential(client_id='8080c8b7-28c4-4b46-8cc3-a8de06d50044')
client = GraphClient(credential=browser_credential)
result = client.get('/consumers')
print(result.json())

