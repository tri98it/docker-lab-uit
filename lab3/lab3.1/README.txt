docker build -t lab3docker .

Node0: docker run -itd --rm --name=node0 lab3docker -s
Node1: docker run -itd --rm --name=node1 --link node0 lab3docker -c node0
Node2: docker run -itd --rm --name=node2 --link node0 lab3docker -c node0
Với các tham số
-d detach // chạy ngầm tiến trình
--name // đặt tên cho container
--link // nối giữa 2 container qua hostname
lab3docker // images đã được tạo từ Dockerfile
-s // server Iperf3
-c // client Iperf3
