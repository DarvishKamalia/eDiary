package main

import (
	"os/exec"
	"strings"
	"os"
)

func main () {

	// list of md files
	out, _ := exec.Command("ls", "md").Output()
	mds := strings.Fields(string(out))

	// for each, generate site file
	for _, md := range mds {

		// title
		title, _ := os.Create("title.temp")
		temp := md[:len(md) - 3]
		title.Write([]byte(temp))
		title.Close()

		// body
		body, _ := os.Create("body.temp")
		mdown := exec.Command("perl", "/home/parthtoo/tools/Markdown.pl", "md/" + md)
		mdown.Stdout = body
		mdown.Run()
		body.Close()

		// cat everything
		full, _ := os.Create(temp + ".html")
		cat := exec.Command("cat", "html/head.html", "title.temp", "html/midd.html", "body.temp", "html/foot.html")
		cat.Stdout = full
		cat.Run()
		full.Close()
	}

	// cleanup
	exec.Command("rm", "title.temp", "body.temp").Run()
}
