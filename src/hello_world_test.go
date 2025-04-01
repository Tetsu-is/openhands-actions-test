package main

import (
    "testing"
    "os/exec"
    "strings"
)

func TestHelloWorld(t *testing.T) {
    cmd := exec.Command("go", "run", "hello_world.go")
    output, err := cmd.CombinedOutput()
    if err != nil {
        t.Fatalf("Failed to run hello_world.go: %v", err)
    }
    if strings.TrimSpace(string(output)) != "Hello World" {
        t.Fatalf("Expected 'Hello World' but got %s", output)
    }
}
