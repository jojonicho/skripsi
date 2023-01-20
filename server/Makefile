build:
	docker build -t a2-server .
run:
	docker run --name a2-server \
	-e REDIS_HOST=a2-redis-server \
	-e REDIS_PORT=6379 \
	-e PORT=8080 \
	--network a2-net \
	--rm \
	-p 8001:8080 \
	a2-server