package main

import (
    "testing"
    "bytes"
    "os"
)

func TestHelloWorld(t *testing.T) {
    // Capture the output of the main function
    buf := new(bytes.Buffer)
    out := os.Stdout
    os.Stdout = buf
    defer func() { os.Stdout = out }()

    main()

    expected := "Hello World\n"
    if buf.String() != expected {
        t.Errorf("expected %q but got %q", expected, buf.String())
    }
}
