#!/bin/bash
DEFAULT_REFRESH=300
REFRESH=$DEFAULT_REFRESH
FILE_PATH="/home/colossuspi/Documents/refresh_rate.txt"

# Read the refresh rate value from the file
if [ -f "$FILE_PATH" ]; then
  BROWSER_REFRESH_RATE=$(<"$FILE_PATH")
fi

if [[ -z "${BROWSER_REFRESH_RATE}" ]] || [[ "${BROWSER_REFRESH_RATE}" -eq 0 ]]; then # if BROWSER_REFRESH_RATE is null or 0
  echo "Browser refresh rate (\$BROWSER_REFRESH_RATE) is not set, default is every ${REFRESH} seconds."
else
  REFRESH=$BROWSER_REFRESH_RATE
  echo "Browser refresh rate is set to ${REFRESH} seconds."
fi

while true; # run forever
do
  # Read the refresh rate value from the file
  if [ -f "$FILE_PATH" ]; then
    BROWSER_REFRESH_RATE=$(<"$FILE_PATH")
  else
    BROWSER_REFRESH_RATE=$DEFAULT_REFRESH
  fi

  if [[ "${BROWSER_REFRESH_RATE}" -ne "${REFRESH}" ]]; then # REFRESH needs to be updated
    if [[ -z "${BROWSER_REFRESH_RATE}" ]] || [[ "${BROWSER_REFRESH_RATE}" -eq 0 ]]; then
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