FROM alpine:latest
COPY hello_jazmin.sh /app/hello_jazmin.sh
WORKDIR /app
CMD ["sh", "hello_jazmin.sh", "World"]
