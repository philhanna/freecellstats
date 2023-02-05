package freecell

import "testing"

func TestGetStatisticString(t *testing.T) {
	tests := []struct {
		name     string
		provider func() string
		want     string
	}{
		{"current",
			func() string {
				return `[Aisleriot Config]
ShowToolbar=true
ShowStatusbar=true
Sound=false
Animations=true
Recent=freecell;klondike;
Variation=freecell.scm
ClickToMove=false
Theme=gnomangelo_bitmap.svgz

[freecell.scm]
Statistic=4;9;144;208;

[klondike.scm]
Statistic=0;1;0;0;
			`
			},
			"4;9;144;208;"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			have, err := GetStatisticString(tt.provider)
			if err != nil {
				t.Error(err)
			}
			want := tt.want
			if have != want {
				t.Errorf("%s: have=%q, want=%q", tt.name, have, want)
			}
		})
	}
}
