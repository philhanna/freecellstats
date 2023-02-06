package freecell

import (
	"fmt"
	"math"
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
func (stat Statistics) String() string {
	sb := fmt.Sprintf("wins:%d, total:%d, best:%d, worst:%d, losses:%d, pct:%f.0",
		stat.wins, stat.total, stat.best, stat.worst, stat.losses, stat.pct)
	return sb
}
