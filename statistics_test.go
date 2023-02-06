package freecell

import (
	"math"
	"testing"
)

func getTestData() *Statistics {
	stat := NewStatisticsFromString("99;150;144;208;")
	return stat
}

func TestNewStatistics(t *testing.T) {
	type args struct {
		wins  int
		total int
		best  int
		worst int
	}
	tests := []struct {
		name string
		args args
		want *Statistics
	}{
		{"current", args{124, 153, 88, 363}, nil},
	}
	for _, tt := range tests {
		want := Statistics{
			wins:   124,
			total:  153,
			best:   88,
			worst:  363,
			losses: 29,
			pct:    81,
		}
		have := *NewStatistics(tt.args.wins, tt.args.total, tt.args.best, tt.args.worst)

		wantString := want.String()
		haveString := have.String()

		if wantString != haveString {
			t.Errorf("%v: want=%v,have=%v", tt.name, wantString, haveString)
		}
	}
}

func TestPercent(t *testing.T) {
	type args struct {
		wins   int
		losses int
	}
	tests := []struct {
		name string
		args args
		want float64
	}{
		{"good", args{99, 150}, 40},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Percent(tt.args.wins, tt.args.losses); math.Round(got) != tt.want {
				t.Errorf("Percent() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestStatistics_WinsToNextHigher(t *testing.T) {
	tests := []struct {
		name   string
		statString string
		want   int
	}{
		{"Normal", "99;150;144;208;", 3},
		{"No losses", "99;99;144;208;", 0},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			stat := NewStatisticsFromString(tt.statString)
			have := stat.WinsToNextHigher()
			want := tt.want
			if have != want {
				t.Errorf("have=%d,want=%d", have, want)
			}	
		})
	}
}

func TestStatistics_LossesToNextLower(t *testing.T) {
	tests := []struct {
		name   string
		statString string
		want   int
	}{
		{"Normal", "99;150;144;208;", 2},
		{"No losses", "99;99;144;208;", 0},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			stat := NewStatisticsFromString(tt.statString)
			have := stat.LossesToNextLower()
			want := tt.want
			if have != want {
				t.Errorf("have=%d,want=%d", have, want)
			}	
		})
	}
}
