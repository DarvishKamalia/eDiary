package main

import (
	"os/exec"
	"io/ioutil"
	"strings"
	"github.com/russross/blackfriday"
)

func main () {

	// list of md files
	out, _ := exec.Command("ls", "md").Output()
	mds := strings.Fields(string(out))

	// for each, generate site file
	for _, md := range mds {

		// title
		temp := md[:len(md) - 3]
		ioutil.WriteFile("title.temp", []byte(temp), 0666)

		// body
		in, _ := ioutil.ReadFile("md/" + md)
		out = blackfriday.MarkdownBasic(in)
		ioutil.WriteFile("body.temp", out, 0666)

		// cat everything
		out, _ = exec.Command("cat", "html/head.html", "title.temp", "html/midd.html", "body.temp", "html/foot.html").Output()
		ioutil.WriteFile(temp + ".html", out, 0666)
	}

	// cleanup
	exec.Command("rm", "title.temp", "body.temp").Run()
}
