package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"sync"
)

func fetchURL(url string) []byte {
	resp, err := http.Get(url)
	if err != nil {
		fmt.Println("error getting url!", err, url)
	}

	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)

	if err != nil {
		fmt.Println("error getting body!", err)
	}

	fmt.Println("Fetched url: ", url)

	return body
}

func fetchURLs(n int) {
	var wg sync.WaitGroup

	url := "http://localhost:8080/%d"

	for i := 1; i < 1000; i++ {
		wg.Add(1)

		go func(n int) {
			defer wg.Done()
			fetchURL(fmt.Sprintf(url, n))
		}(i)

		// close(res)
	}
	wg.Wait()
}
