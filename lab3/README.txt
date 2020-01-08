docker build -t <tên_container_image> <đường dẫn tới build context>
ex:
docker build -t my_http_server .

docker run -d -p 80:80 my_web_server 
-d hay –detach

docker-compose -f docker-compose.yml build

docker-compose -f docker-compose.yml up 
hoặc
docker-compose -f docker-compose.yml up -d (detach mode)
