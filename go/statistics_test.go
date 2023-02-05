package freecell

import "testing"
import "math"

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
