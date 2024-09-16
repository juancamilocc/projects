package main

import (
	"flag"
	"fmt"
	"io"
	"log"
	"net"
	"os"
)

var (
	port = flag.Int("p", 3090, "port")           // In the console --port=<int>
	host = flag.String("h", "localhost", "host") // In the console --host=<string>
)

func main() {

	flag.Parse() // parsers the flag variables

	conn, err := net.Dial("tcp", fmt.Sprintf("%s:%d", *host, *port)) // Creates a connection with a server using tcp protocol
	if err != nil {
		log.Fatal(err)
	}

	done := make(chan struct{}) // Defines a channel that allow us to detect when the request was donde
	go func() {
		io.Copy(os.Stdout, conn) // Copy in stdout console our connection
		done <- struct{}{}       // Here a way to notify our connection was successful
	}()
	CopyContent(conn, os.Stdin) // Here is contrary, copies the stdin console to our connection
	conn.Close()                // Close our connection
	<-done                      // wait until the program has been finished
}

func CopyContent(dst io.Writer, src io.Reader) {

	_, err := io.Copy(dst, src)
	if err != nil {
		log.Fatal(err)
	}
}
