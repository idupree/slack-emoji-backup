
Go to https://(your-team-name).slack.com/customize/emoji

In your browser's dev console, run:

```
[].map.call(document.querySelectorAll('[data-original]'), function(s){return s.dataset.original}).join('\n')
```

Then copy that text to a text file named emojiURLs.txt that you put next to
download-slack-emoji.py.

Then run ./download-slack-emoji.py
(it will default to looking for a file named emojiURLs.txt)
and it will save emoji to emoji-downloads/


