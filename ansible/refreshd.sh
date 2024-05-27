#!/bin/bash
DEFAULT_REFRESH=300
REFRESH=$DEFAULT_REFRESH

# Read the refresh rate value from the file
if [ -f "/home/colossuspi/Documents/refresh_rate.txt" ]; then
  BROWSER_REFRESH_RATE=$(</home/colossuspi/Documents/refresh_rate.txt)
fi

if [[ -z "${BROWSER_REFRESH_RATE}" ]]; then # if BROWSER_REFRESH_RATE is null
  echo "Browser refresh rate (\$BROWSER_REFRESH_RATE) is not set, default is every ${REFRESH} seconds."
else
  REFRESH=$BROWSER_REFRESH_RATE
  echo "Browser refresh rate is set to ${REFRESH} seconds."
fi

while true; # run forever
  do
  # Read the refresh rate value from the file
  if [ -f "/home/colossuspi/Documents/refresh_rate.txt" ]; then
    BROWSER_REFRESH_RATE=$(</home/colossuspi/Documents/refresh_rate.txt)
  else
    BROWSER_REFRESH_RATE=$DEFAULT_REFRESH
  fi

  if [[ "${BROWSER_REFRESH_RATE}" -ne "${REFRESH}" ]]; then # REFRESH needs to be updated
    if [[ -z "${BROWSER_REFRESH_RATE}" ]]; then
      REFRESH=$DEFAULT_REFRESH
      echo "Browser refresh rate is set to ${REFRESH} seconds."
    else
      REFRESH=$BROWSER_REFRESH_RATE
      echo "Browser refresh rate is set to ${REFRESH} seconds."
    fi
  fi
  sleep $REFRESH # refresh time in seconds
  xdotool key "ctrl+r" & # send keypress to refresh
done