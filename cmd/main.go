package main

import "fmt"
import "github.com/philhanna/freecellstats/freecell"

func main() {
	statString, _ := freecell.GetStatisticString()
	stat := freecell.NewStatisticsFromString(statString)
	lines := stat.StringLines()
	for _, s := range lines {
		fmt.Println(s)
	}
}
