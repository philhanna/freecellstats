package freecell

import (
	"os"
	"path/filepath"

	ini "github.com/ochinchina/go-ini"
)

const (
	CONFIG_FILE_NAME = ".config/gnome-games/aisleriot"
)


// Loads the configuration from the default input file. This method can
// be replaced by a mock object in unit tests
//
// A configuration file provider is a function returning either:
//  1. A file name (such as the actual configuration file)
//  2. A string containing the contents of a configuration file
// The go-ini package will accept either one.
//
// The default configuration file provider gets the name of
// the actual AisleRiot configuration file in the home directory.
func GetStatisticString(provider ...func() string) (string, error) {

	// Get a function that will provide the contents of the config file
	var configFileProvider func() string

	// If no alternate provider was found, use the one relative to
	// the actual home directory.  Otherwise, use the provider specified
	// on the command line
	switch {
	case len(provider) == 0:
		configFileProvider = func() string {
			home, _ := os.UserHomeDir()
			configFile := filepath.Join(home, CONFIG_FILE_NAME)
			return configFile
		}
	default:
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
