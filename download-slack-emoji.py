#!/usr/bin/env python

import os, sys, re
try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve

def main():
    urllist = 'emojiURLs.txt'
    outdir = 'emoji-downloads'
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    with open(urllist) as f:
        for line in f:
            # https://a.slack-edge.com/ URLs appear to be built-in emoji
            for url in re.findall(r'''https://emoji[^ ,"'{}\[\]\r\n]*''', line):
                # in case the browser console put in some extra characters
                url = re.sub(r'\\[rnt]', '', url).replace('\\', '')
                # infer emoji name from URL path
                match = re.search(r'''^.*/([^/]*)/[^./]*([.][^./]*)$''', url)
                emojifile = match.group(1) + match.group(2)
                sys.stderr.write('Downloading '+emojifile+'\n')
                urlretrieve(url, os.path.join(outdir, emojifile));

if __name__ == '__main__':
    main()

