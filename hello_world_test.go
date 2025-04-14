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
    expected := "Hello World\n"
    if !strings.Contains(string(output), expected) {
        t.Errorf("Expected %q but got %q", expected, output)
    }
}
