package main

import "testing"
import (
    "bytes"
    "io"
    "os"
    "syscall"
)

func TestHelloWorld(t *testing.T) {
    expected := "Hello World"
    if got := captureOutput(main); got != expected+"\n" {
        t.Errorf("Expected %q but got %q", expected, got)
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
