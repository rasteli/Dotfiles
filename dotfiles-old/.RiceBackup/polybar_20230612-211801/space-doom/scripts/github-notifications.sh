#!/bin/sh

USER="rasteli"
TOKEN=$(cat "$HOME/.tokens/github-notification.token")

notifications=$(echo "user = \"$USER:$TOKEN\"" | curl -sf -K- https://api.github.com/notifications | jq ".[].unread" | grep -c true)

if [ "$notifications" -gt 0 ]; then
    echo "%{F$primary}%{F-}  %{F$fore}$notifications%{F-}"
else
    echo "%{F$primary}%{F-}  %{F$fore}None%{F-}"
fi
