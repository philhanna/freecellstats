package freecell

// Captures the wins, losses, and percentages
type Statistics struct {
	wins   int
	total  int
	best   int
	worst  int
	losses int
	pct    float64
}

// Constructor
func NewStatistics(wins, total, best, worst int) *Statistics{
	stats := new(Statistics)
	stats.wins = wins
	stats.total = total
	stats.best = best
	stats.worst = worst
	stats.losses = total - wins
	if total != 0 {
		stats.pct = float64(wins) / float64(total)
	}
	return stats
}