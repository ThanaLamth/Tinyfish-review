#!/usr/bin/env bash
# run_wallet_flow.sh
# Ubuntu wrapper: starts Xvfb virtual display then runs capture_wallet_flow.py
# Usage:
#   ./run_wallet_flow.sh --url https://kyberswap.com
#   ./run_wallet_flow.sh --url https://kyberswap.com --out screenshots/kyberswap/wallet-flow

set -euo pipefail

DISPLAY_NUM="${XVFB_DISPLAY:-99}"
XVFB_RESOLUTION="${XVFB_RES:-1440x900x24}"

# Start Xvfb if not already running
if ! pgrep -x Xvfb > /dev/null 2>&1; then
    echo "[xvfb] Starting Xvfb :${DISPLAY_NUM} (${XVFB_RESOLUTION})..."
    Xvfb ":${DISPLAY_NUM}" -screen 0 "${XVFB_RESOLUTION}" &
    XVFB_PID=$!
    sleep 1
    CLEANUP_XVFB=1
fi

export DISPLAY=":${DISPLAY_NUM}"

echo "[wallet-flow] Running capture_wallet_flow.py $*"
python tools/capture_wallet_flow.py "$@"
STATUS=$?

# Clean up Xvfb only if we started it
if [ "${CLEANUP_XVFB:-0}" = "1" ]; then
    echo "[xvfb] Stopping Xvfb PID ${XVFB_PID}"
    kill "${XVFB_PID}" 2>/dev/null || true
fi

exit "${STATUS}"