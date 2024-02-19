package handlers

import (
	"encoding/json"
	"html/template"
	"log"
	"net/http"
	"piedra_papel_tijera/rps"
	"strconv"
)

// Player structure
type Player struct {
	Name string
}

var player Player

// Home controller
func Home(w http.ResponseWriter, r *http.Request) {
	restartValue()
	renderTemplate(w, "home.html", nil)
}

// New game controller
func NewGame(w http.ResponseWriter, r *http.Request) {
	restartValue()
	renderTemplate(w, "new-game.html", nil)
}

// Game controller
func Game(w http.ResponseWriter, r *http.Request) {

	if r.Method == "POST" {
		// Read data from form
		err := r.ParseForm()
		if err != nil {
			http.Error(w, "Error parsing form", http.StatusBadRequest)
			return
		}

		player.Name = r.Form.Get("name")
	}

	// Avoid play without player name
	if player.Name == "" {
		http.Redirect(w, r, "/new", http.StatusFound)
	}

	renderTemplate(w, "game.html", player)
}

// Play controller
func Play(w http.ResponseWriter, r *http.Request) {
	playerChoice, _ := strconv.Atoi(r.URL.Query().Get("c"))
	result := rps.PlayRound(playerChoice)

	out, err := json.MarshalIndent(result, "", "    ")
	if err != nil {
		log.Println(err)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	w.Write(out)
}

// About controller
func About(w http.ResponseWriter, r *http.Request) {
	restartValue()
	renderTemplate(w, "about.html", nil)
}

// Errors manager
var errorTemplates = template.Must(template.ParseGlob("templates/**/*.html"))

func handlerError(w http.ResponseWriter, name string, status int) {
	w.WriteHeader(status)
	errorTemplates.ExecuteTemplate(w, name, nil)
}

func NotFoundHandler(w http.ResponseWriter, r *http.Request) {
	// Return personalized error
	handlerError(w, "404", http.StatusNotFound)
}

const baseDir = "templates/"

func renderTemplate(w http.ResponseWriter, name string, data any) {
	templates := template.Must(template.ParseFiles(baseDir+"base.html", baseDir+name))
	w.Header().Set("Content-Type", "text/html")

	err := templates.ExecuteTemplate(w, "base", data)
	if err != nil {
		handlerError(w, "500", http.StatusInternalServerError)
	}
}

// Restart values
func restartValue() {
	player.Name = ""
	rps.ComputerScore = 0
	rps.PlayerScore = 0
}
