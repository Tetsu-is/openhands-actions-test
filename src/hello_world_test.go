package main

import "testing"
import "os/exec"
import "bytes"

func TestHelloWorld(t *testing.T) {
    cmd := exec.Command("go", "run", "hello_world.go")
    var out bytes.Buffer
    cmd.Stdout = &out
    err := cmd.Run()
    if err != nil {
        t.Fatalf("Failed to run hello_world.go: %v", err)
    }
    expected := "Hello World\n"
    if out.String() != expected {
        t.Errorf("Expected %q but got %q", expected, out.String())
    }
}
