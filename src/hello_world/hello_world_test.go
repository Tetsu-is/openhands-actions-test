package main

import (
    "bytes"
    "io"
    "os"
    "syscall"
    "testing"
)

func TestHelloWorld(t *testing.T) {
    expected := "Hello World"
    if result := captureOutput(main); result != expected+"\n" {
        t.Errorf("Expected %q but got %q", expected, result)
    }
}

func captureOutput(f func()) string {
    r, w, _ := os.Pipe()
    os.Stdout = w

    f()

    w.Close()
    var buf bytes.Buffer
    io.Copy(&buf, r)
    os.Stdout = os.NewFile(uintptr(syscall.Stdout), "/dev/stdout")

    return buf.String()
}
