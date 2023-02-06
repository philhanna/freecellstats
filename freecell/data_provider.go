package freecell

import (
	"os"
	"path/filepath"

	ini "github.com/ochinchina/go-ini"
)

const (
	CONFIG_FILE_NAME = ".config/gnome-games/aisleriot"
)

// A ConfigFileProvider is a function returning either:
//  1. A file name (such as the actual configuration file)
//  2. A string containing the contents of a configuration file
// The default configuration file provider gets the name of
// the actual AisleRiot configuration file in the home directory.
type ConfigFileProvider func() string

// Loads the configuration from the default input file. This method can
// be replaced by a mock object in unit tests
func GetStatisticString(provider ...ConfigFileProvider) (string, error) {

	// Get a function that will provide the contents of the config file
	var configFileProvider func() string
	if len(provider) == 0 {
		configFileProvider = func () string {
			home, _ := os.UserHomeDir()
			configFile := filepath.Join(home, CONFIG_FILE_NAME)
			return configFile
		}		
	} else {
		configFileProvider = provider[0]
	}

	// Use that function to load the configuration .ini file
	configFile := configFileProvider()
	config := ini.Load(configFile)

	// Get the freecell section and the statistic string from it
	var statisticString string
	section, err := config.GetSection("freecell.scm")
	if err == nil {
		statisticString, err = section.GetValue("Statistic")
	}
	return statisticString, err
}
