# webfortune
## To build & run locally:
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
flask run
```
If you would like to run the Flask server on a different port change `flask run` to `flask run --port=<port>` where <port> is your desired port.
After these commands are run a web server will be running on localhost port 5000.
### To kill the server:
`ctrl + c`
## To build and run Docker container:
```
docker build -t cowsay .
docker run cowsay
```
If you would like to run the docker container on a specific port change `docker run cowsay` to `docker run -dp <port>:5000 cowsay` where <port> is your desired port.
When you run these commands a flask server will be running on your IP on port 5000.
### To kill the server run:
```
docker ps
docker kill <name of container>
```
