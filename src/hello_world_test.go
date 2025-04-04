package main

import "testing"
import "bytes"
import "os"

func TestHelloWorld(t *testing.T) {
    old := os.Stdout
    r, w, _ := os.Pipe()
    os.Stdout = w

    main()

    w.Close()
    var buf bytes.Buffer
    buf.ReadFrom(r)
    os.Stdout = old

    if buf.String() != "Hello World\n" {
        t.Errorf("Expected 'Hello World' but got %s", buf.String())
    }
}
