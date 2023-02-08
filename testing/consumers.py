import re, json

from channels.generic.websocket import AsyncWebsocketConsumer




class Testing(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
 
     
           
    


      
    async def receive(self, text_data):
        completions = []
        f = open('/home/dev/start-project/server/testing/data.json')
        data_json = json.load(f)
        for item in data_json:
            for key, value in item.items():
                if re.findall(text_data.lower(), value.lower()):
                    completions.append(item)
                    break    
                    
        await self.send(text_data = json.dumps(completions))
      
