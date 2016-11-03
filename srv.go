package main

import (
	"fmt"
	"net/http"
	"os"
	"strconv"
	"time"
)

func handler(w http.ResponseWriter, r *http.Request) {
	select {
	case <-time.After(time.Millisecond * 100):
		fmt.Fprintf(w, "Hi there, I love %s!", r.URL.Path[1:])
	}
}

func main() {
	args := os.Args
	fmt.Println(len(args), args)

	if len(args) == 1 || args[1] == "runserver" {
		fmt.Println("Starting server on http://localhost:8080")
		http.HandleFunc("/", handler)
		http.ListenAndServe(":8080", nil)
	} else {
		n, err := strconv.Atoi(args[2])

		if err != nil {
			fmt.Println("Error converting n")
		}

		start := time.Now()

		fmt.Println("Benching urls: ", n)

		fetchURLs(n)

		fmt.Println("Benching took: ", time.Since(start))
	}
}
