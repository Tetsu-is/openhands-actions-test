package main

import (
    "testing"
    "bytes"
    "os"
)

func TestHelloWorld(t *testing.T) {
    // Capture the output of the main function
    out := os.Stdout
    r, w, _ := os.Pipe()
    os.Stdout = w

    defer func() {
        os.Stdout = out
        w.Close()
    }()

    main()

    w.Close()
    var buf bytes.Buffer
    buf.ReadFrom(r)
    defer func() { os.Stdout = out }()

    main()

    expected := "Hello World\n"
    if buf.String() != expected {
        t.Errorf("expected %q but got %q", expected, buf.String())
    }
}
