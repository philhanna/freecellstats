package freecell

import "testing"

func TestGetStatisticString(t *testing.T) {
	tests := []struct {
		name string
		want string
	}{
		{"good", "124;153;88;363;"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetStatisticString(); got != tt.want {
				t.Errorf("GetStatisticString() = %v, want %v", got, tt.want)
			}
		})
	}
}
