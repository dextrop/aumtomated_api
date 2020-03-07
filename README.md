# aumtomated_api
Automated API

Steps:

1. run install.sh script. This script will install all related rependencies.
2. cd automatedApi/
3. run run.sh. This will make you api live

you can later check you api on
`http://localhost:8081/'

your api configration is stored in automatedApi/ServerData.json

How to add an api

If you wanna add a get api add new object inside getObject in json file.
```
  "GET": {
    "welcome/" : {
      "json_response": {"message":  "Automated Sample API", "payload":  "Get API Config working successful"}, # json response
      "headers": {"Content-type": "application/json"}
    }
    ..
    ...
    
  },
  ```

