package main

import "testing"

func TestExpandUser(t *testing.T) {
	testCases := []struct {
		path string
		want string
	}{
		{"~", "/home/saspeh"},
		{"~/bogus", "/home/saspeh/bogus"},
	}

	for _, tc := range testCases {
		have := expandUser(tc.path)
		want := tc.want
		if want != have {
			t.Errorf(`"%s": have="%s", want="%s"`, tc.path, have, want)
		}
	}
}
