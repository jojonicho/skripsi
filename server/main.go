package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/gomodule/redigo/redis"
)

type createTodoReq struct {
	Title string `json:"title"`
}

func main() {
	redisHost := os.Getenv("REDIS_HOST")
	if redisHost == "" {
		panic("REDIS_HOST not set")
	}
	redisPort := os.Getenv("REDIS_PORT")
	if redisPort == "" {
		panic("REDIS_PORT not set")
	}
	port := os.Getenv("PORT")
	if port == "" {
		panic("PORT environment variable is not set")
	}

	redisAddress := fmt.Sprintf("%s:%s", redisHost, redisPort)

	pool := redis.Pool{
		MaxIdle:     3,
		IdleTimeout: 240 * time.Second,
		Dial:        func() (redis.Conn, error) { return redis.Dial("tcp", redisAddress) },
	}
	router := gin.Default()
	// hello world for /
	router.GET("/", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"message": "Hello World!"})
	})

	todoGroup := router.Group("/todos")
	todoGroup.GET("", func(c *gin.Context) {
		conn := pool.Get()
		defer conn.Close()

		fmt.Printf("GET /todos\n")
		rawTodos, err := redis.Values(conn.Do("LRANGE", "todos", 0, -1))
		if err != nil {
			fmt.Printf("Error: %s\n", err)
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
			return
		}
		var todos []string
		redis.ScanSlice(rawTodos, &todos)

		c.JSON(http.StatusOK, todos)
	})

	todoGroup.POST("", func(c *gin.Context) {
		conn := pool.Get()
		defer conn.Close()

		var req createTodoReq
		if err := c.ShouldBindJSON(&req); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}

		todo := req.Title
		fmt.Printf("POST /todos: %s\n", todo)

		if err := conn.Send("LPUSH", "todos", todo); err != nil {
			fmt.Printf("Error: %s\n", err)
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
			return
		}
		if err := conn.Flush(); err != nil {
			fmt.Printf("Error: %s\n", err)
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
			return
		}

		c.JSON(http.StatusCreated, todo)
	})

	if err := router.Run(); err != nil {
		log.Fatalf("Failed starting http server: %v", err)
	}

	fmt.Printf("Server listening on port %s\n", port)
}
