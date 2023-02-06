package freecell

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

// -------------------------------------------------------------
// Type definitions
// -------------------------------------------------------------

// Captures the wins, losses, and percentages
type Statistics struct {
	wins   int
	total  int
	best   int
	worst  int
	losses int
	pct    float64
}

// -------------------------------------------------------------
// Constructors
// -------------------------------------------------------------

// Creates a new Statistics object from the basic integer values
// that AisleRiot keeps:
//  - wins
//  - total
//  - best
//  - worst
// It then calculates the other two values:
//  - losses
//  - percentage of wins
func NewStatistics(wins, total, best, worst int) *Statistics {
	stats := new(Statistics)
	stats.wins = wins
	stats.total = total
	stats.best = best
	stats.worst = worst
	stats.losses = total - wins
	if total != 0 {
		stats.pct = math.Round(100.0 * float64(wins) / float64(total))
	}
	return stats
}

// Creates a new Statistics object from the string representation
// that is in the configuration file, e.g., "99;150;144;208;"
func NewStatisticsFromString(statString string) *Statistics {
	tokens := strings.Split(statString, ";")[:4]
	fmt.Printf("Number of tokens = %d\n", len(tokens))
	wins, _ := strconv.Atoi(tokens[0])
	total, _ := strconv.Atoi(tokens[1])
	best, _ := strconv.Atoi(tokens[2])
	worst, _ := strconv.Atoi(tokens[3])
	return NewStatistics(wins, total, best, worst)
}

// -------------------------------------------------------------
// Static functions
// -------------------------------------------------------------

// Finds the value of the winning percentage
func Percent(wins int, losses int) float64 {
	numer := float64(wins) * 100.0
	denom := float64(wins + losses)
	pct := numer / denom
	return pct
}

// -------------------------------------------------------------
// Methods
// -------------------------------------------------------------

// Returns a string representation of the structure
func (stat *Statistics) String() string {
	sb := fmt.Sprintf("wins:%d, total:%d, best:%d, worst:%d, losses:%d, pct:%f.0",
		stat.wins, stat.total, stat.best, stat.worst, stat.losses, stat.pct)
	return sb
}

// Returns the number of wins needed to raise the winning percentage one point
func (stat *Statistics) WinsToNextHigher() int {
	if stat.losses == 0 {
		return 0
	}
	wins := stat.wins
	losses := stat.losses
	current := math.Round(Percent(wins, losses))
	next_pct := current + 1
	moves := 0
	for current < next_pct {
		moves += 1
		wins += 1
		current = math.Round(Percent(wins, losses))
	}
	return moves
}

// Returns the number of losses needed to lower the winning percentage one point
func (stat *Statistics) LossesToNextLower() int {
	if stat.losses == 0 {
		return 0
	}
	wins := stat.wins
	losses := stat.losses
	current := math.Round(Percent(wins, losses))
	next_pct := current - 1
	moves := 0
	for current > next_pct {
		moves += 1
		losses += 1
		current = math.Round(Percent(wins, losses))
	}
	return moves
}
