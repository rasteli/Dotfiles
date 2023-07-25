#!/bin/sh

www="$HOME/www"
portfolio="$www/Portfolio"
rocketseat="$www/Rocketseat"
ignite_react="$rocketseat/Ignite/reactjs"

icons_path="$HOME/.config/xmenu/icons"

xmenu <<EOF | sh &
Applications
	IMG:$icons_path/web.png	Google Chrome	google-chrome-stable
	IMG:$icons_path/gimp.png	GIMP	gimp
	IMG:$icons_path/discord.png	Discord	discord
	IMG:$icons_path/vscode.png	Visual Studio Code	code
	IMG:$icons_path/insomnia.png	Insomnia	insomnia
	IMG:$icons_path/file.png	Thunar	thunar
	IMG:$icons_path/notes.png	Trilium	trilium
	IMG:$icons_path/lorien.png	Lorien	lorien
	IMG:$icons_path/notes.png	Xournal	xournalpp
Code
	Dotfiles	code "$www/Dotfiles"
	stellar-whiteboard	code "$www/stellar-whiteboard"
	Ignite
		fundamentos	code "$ignite_react/01-fund-reactjs-ts"
		timer	code "$ignite_react/02-ignite-timer"
		dt-money	code "$ignite_react/03-dt-money"
	Portfolio
		Budget	code "$portfolio/BudgetWebsite"
		Cryptovio	code "$portfolio/Cryptovio"
		XBShop	code "$portfolio/XBShop"
	Rocketseat
		nlw
			esports
				server	code "$rocketseat/nlw/esports/backend"
				web	code "$rocketseat/nlw/esports/web"
			setup
				server	code "$rocketseat/nlw/setup/server"
				web	code "$rocketseat/nlw/setup/web"
				mobile	code "$rocketseat/nlw/setup/mobile"

Shutdown		poweroff
Reboot			reboot
EOF
