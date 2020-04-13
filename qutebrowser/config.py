config.load_autoconfig()
c.auto_save.session = False
c.content.cookies.accept = 'no-3rdparty'
c.content.cookies.store = False
c.content.javascript.enabled = True
c.content.images = True
c.editor.command = ['urxvt', '-e', '/usr/bin/vim', '{file}']
c.tabs.position = 'left'
c.url.auto_search = 'dns'
c.url.searchengines = {'DEFAULT': 'https://google.co.in/search?q={}'}
c.messages.timeout = 5000
config.bind(',x', 'c.tabs.position = top')
config.bind(',ej', 'spawn --userscript noscript_enable')
config.bind(',dj', 'spawn --userscript noscript_disable')

config.bind(',zl', 'spawn --userscript qute-pass --dmenu-invocation dmenu')
config.bind(',zul', 'spawn --userscript qute-pass --dmenu-invocation dmenu --username-only')
config.bind(',zpl', 'spawn --userscript qute-pass --dmenu-invocation dmenu --password-only')
config.bind(',zol', 'spawn --userscript qute-pass --dmenu-invocation dmenu --otp-only')

# Allow JS and cookies on own domain

# Fingerprinting protection
c.content.headers.accept_language = 'en-US,en;q=0.5'
c.content.headers.user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
c.content.headers.custom = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

# wayland
c.window.hide_decoration = True
# base16-qutebrowser (https://github.com/theova/base16-qutebrowser)
# Base16 qutebrowser template by theova
# Default Dark scheme by Chris Kempson (http://chriskempson.com)

