# aumtomated_api
Automated API

Steps:

1. Run install script
```bash
./install.sh
```
** running install script will install all dependencies

2. Run run.sh to make api live.
```bash
cd automatedApi/
./run.sh
```
3. Add Your api configrations into json file.
your api configration is stored in automatedApi/ServerData.json

### How to add an api

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

you can later check you api on
`http://localhost:8081/'

