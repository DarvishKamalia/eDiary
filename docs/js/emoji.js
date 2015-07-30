var md = require('markdown-it')();
var emoji = require('markdown-it-emoji');

md.use(emoji [, options]);

var twemoji = require('twemoji')

md.renderer.rules.emoji = function(token, idx) {
		  return twemoji.parse(token[idx].content);
};
