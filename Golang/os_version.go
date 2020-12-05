package main

import (
	"fmt"
	"os/exec"
	"strings"
	"runtime"
)

func main() {
	os_type := runtime.GOOS
	switch os_type {
    case "windows":
        command := "(Get-ComputerInfo).WindowsProductName"
        out, _ := exec.Command("powershell", "-Command", command).Output()
		os_name := string(out)
		fmt.Print(os_name)
	case "darwin":
		out, _ := exec.Command("bash", "-c", "sw_vers -productName").Output()
		os_name := strings.Split(string(out), "\n")
		out_2, _ := exec.Command("bash", "-c", "sw_vers -productVersion").Output()
		os_version := string(out_2)
		fmt.Print(os_name[0] + " " + os_version)
	case "linux":
		out, _ := exec.Command("bash", "-c", ". /etc/os-release; echo $PRETTY_NAME").Output()
		os_name := string(out)
		fmt.Print(os_name)
	default:
		fmt.Print("%s.\n", os_type)
	}
}