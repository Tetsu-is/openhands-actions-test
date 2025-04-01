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
    expected := "Hello World"
    if !strings.Contains(string(output), expected) {
        t.Errorf("Expected output to contain %q, got %q", expected, string(output))
    }
}
