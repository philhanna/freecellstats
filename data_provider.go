package freecell

import (
	"os"
	"path/filepath"

	ini "github.com/ochinchina/go-ini"
)

const (
	CONFIG_FILE_NAME = ".config/gnome-games/aisleriot"
)

type DataProvider struct {
}


func DefaultConfigGetter() string {
	home, _ := os.UserHomeDir()
	configFile := filepath.Join(home, CONFIG_FILE_NAME)
	return configFile
}

// Loads the configuration from the default input file. This method can
// be replaced by a mock object in unit tests
func GetStatisticString() string {
	configFile := DefaultConfigGetter()
	config := ini.Load(configFile)
	section, _ := config.GetSection("freecell.scm")
	statisticString, _ := section.GetValue("Statistic")
	return statisticString
}
