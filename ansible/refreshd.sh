#!/bin/bash
REFRESH=300

if [[ -z "${BROWSER_REFRESH_RATE}" ]]; then # if BROWSER_REFRESH_RATE is null
  echo "Browser refresh rate (\$BROWSER_REFRESH_RATE) is not set, default is every ${REFRESH} seconds."
else
  REFRESH=$BROWSER_REFRESH_RATE
  echo "Browser refresh rate is set to ${REFRESH} seconds."
fi

while true; # run forever
do
sleep $REFRESH # refresh time in seconds
xdotool key "ctrl+r" & # send keypress to refresh
done