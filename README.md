# WebGLGameServer
Simple websocket server for WebGLGame  
The game itself: https://github.com/core2duo/WebGLGame  
Required Python 3.5+

## Run
Install the requirements:
```bash
pip install -r requirements.txt
```

Run the server:
```bash
python server.py [host] [port]
```

Example:
```bash
python server.py 127.0.0.1 1234
```


## Docker
You can also run a docker container:
```bash
docker pull core3duo/webglgameserver && docker run -p [port]:3000 core3duo/webglgameserver
```
