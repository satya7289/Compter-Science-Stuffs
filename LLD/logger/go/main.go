package main

import (
	"fmt"
	"logger/pkg/logger"
)

func main() {
	fmt.Println("Logging System")

	log := logger.NewLogger(logger.DEBUG)
	log.Log(logger.DEBUG, "Debug logged")
	log.Log(logger.INFO, "Info logged")
	log.Log(logger.WARN, "Warn logged")
	log.Log(logger.ERROR, "Error logged")
	log.Log(logger.FETAL, "Fetal logged")
}
