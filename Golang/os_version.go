package main

import (
	"fmt"
	"os/exec"
	// "os"
	"runtime"
)

func main() {
	os_type := runtime.GOOS
	switch os_type {
    case "windows":
        command := "(Get-ComputerInfo).WindowsProductName"
        out, err := exec.Command("powershell", "-Command", command).Output()
		os_name := string(out)
		if err != nil {
			fmt.Println(err)
		}
		fmt.Println(os_name)
	case "darwin":
        out, err := exec.Command("bash", "-c", "sw_vers -productName").Output()
		os_name := string(out)
		if err != nil {
			fmt.Println(err)
        }
        output, errors := exec.Command("bash", "-c", "sw_vers -productVersion").Output()
		os_version := string(output)
		if err != nil {
			fmt.Println(errors)
		}
		fmt.Println(os_name + os_version)
	case "linux":
		out, err := exec.Command("bash", "-c", ". /etc/os-release; echo $PRETTY_NAME").Output()
		os_name := string(out)
		if err != nil {
			fmt.Println(err)
		}
		fmt.Println(os_name)
	default:
		fmt.Printf("%s.\n", os_type)
	}
}