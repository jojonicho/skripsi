FROM golang:1.17

WORKDIR /build
# install deps
COPY go.mod go.sum ./
RUN go mod download

# create executable binary ./server from ./main.go
COPY . ./
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o ./server ./main.go

FROM alpine:latest
WORKDIR /app
COPY --from=0 /build/ ./

# run the executable
CMD ["./server"]
