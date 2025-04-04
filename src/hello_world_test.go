package main

import "testing"
import "bytes"
import "os"

func TestHelloWorld(t *testing.T) {
    // Capture the output of the main function
    old := os.Stdout
    r, w, _ := os.Pipe()
    os.Stdout = w

    main()

    w.Close()
    os.Stdout = old

    var buf bytes.Buffer
    buf.ReadFrom(r)

    got := buf.String()
    want := "Hello World\n"

    if got != want {
        t.Errorf("got %q, want %q", got, want)
    }
}
