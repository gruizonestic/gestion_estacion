package main

import (
	"encoding/json"
	"io"
	"io/ioutil"
	"log"
	"net/http"
)

type billete struct {
	Numero string
}

func test(rw http.ResponseWriter, req *http.Request) {
	body, err := ioutil.ReadAll(req.Body)
	if err != nil {
		panic(err)
	}
	log.Println(string(body))
	var b billete
	err = json.Unmarshal(body, &b)
	if err != nil {
		panic(err)
	}
	log.Println(b.Numero)
	io.WriteString(rw, "Billete validado: "+b.Numero)
}

func main() {
	http.HandleFunc("/validar", test)
	log.Fatal(http.ListenAndServe(":5207", nil))
}
