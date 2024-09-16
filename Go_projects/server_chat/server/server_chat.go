package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"net"
)

// Definition for clients
type Client chan<- string

var (
	port = flag.Int("p", 3090, "port")           // In the console --port=<int>
	host = flag.String("h", "localhost", "host") // In the console --host=<string>
)

var (
	incomingClients = make(chan Client) // Incoming clients in our chat
	leavingClients  = make(chan Client) // leaving clients in our chat
	chatMessages    = make(chan string) // chat messages
)

// Client1 -> Server -> HandleConnection(Client1)
// Function to manage the connection
func HandleConnection(conn net.Conn) {

	defer conn.Close()

	clientMessage := make(chan string)   // Client messages
	go MessageWrite(conn, clientMessage) // Write client messages

	clientName := conn.RemoteAddr().String() // Retrieves name of client, example: server.com:port
	clientMessage <- fmt.Sprintf("Welcome to the server, your name %s\n", clientName)
	chatMessages <- fmt.Sprintf("New client is here %s\n", clientName) // Notify to all chat

	incomingClients <- clientMessage // Send channel to the incoming clients channel

	// Read input message from client
	// When the user type ctrl + C or close the app, the connection will be broken
	inputMessage := bufio.NewScanner(conn)
	for inputMessage.Scan() {
		chatMessages <- fmt.Sprintf("%s: %s", clientName, inputMessage.Text())
	}

	leavingClients <- clientMessage
	chatMessages <- fmt.Sprintf("%s said good bye!!", clientName)

}

// Iterates over all client messages
func MessageWrite(conn net.Conn, messagesClient <-chan string) {

	for messageClient := range messagesClient {
		fmt.Fprintln(conn, messageClient)
	}
}

func Broadcast() {

	clients := make(map[Client]bool)
	for {
		select {
		case message := <-chatMessages: // receive and send new message trough chat channel to all clients

			for client := range clients {
				client <- message
			}

		case newClient := <-incomingClients: // New client connection

			clients[newClient] = true

		case leavingClient := <-leavingClients: // A client leave the server
			delete(clients, leavingClient)
			close(leavingClient)
		}
	}
}

func main() {

	listener, err := net.Listen("tcp", fmt.Sprintf("%s:%d", *host, *port)) // lsiten for default port
	if err != nil {
		log.Fatal(err)
	}

	go Broadcast()
	for {
		conn, err := listener.Accept() // Accept connecrtion
		if err != nil {
			log.Print(err)
			continue
		}
		go HandleConnection(conn) // Manage connection
	}
}
