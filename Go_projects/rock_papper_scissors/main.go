package main

import (
	"log"
	"net/http"
	"piedra_papel_tijera/handlers"
)

func main() {
	// Router
	router := http.NewServeMux()

	// Manage static files
	fs := http.FileServer(http.Dir("static"))
	router.Handle("/static/", http.StripPrefix("/static/", fs))

	// Endpoints
	router.HandleFunc("/", handlers.Home)
	router.HandleFunc("/new", handlers.NewGame)
	router.HandleFunc("/game", handlers.Game)
	router.HandleFunc("/play", handlers.Play)
	router.HandleFunc("/about", handlers.About)

	// Start server
	port := ":8085"
	log.Printf("Server listen in http://localhost%s", port)
	log.Fatal(http.ListenAndServe(port, router))

}
