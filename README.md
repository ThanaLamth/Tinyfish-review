# Tinyfish Review — Auto Article Writer

Toolkit tự động viết bài review/tutorial cho các DEX/CEX/Web3 site.  
Chụp screenshot thực tế trên 3 thiết bị → research bằng TinyFish → sinh bài Markdown.

## Stack
- **Python 3.10+**
- **Playwright** — browser automation + screenshot
- **TinyFish CLI** — web search, fetch, remote CDP browser
- **eth-account / mnemonic** — tạo ví demo
- **MetaMask v13** extension — demo wallet connection flow

## Cài đặt (Ubuntu)

```bash
# 1. System deps
sudo apt-get update && sudo apt-get install -y \
    nodejs npm xvfb \
    libgbm-dev libnss3 libatk-bridge2.0-0 libdrm2 libxcomposite1 \
    libxdamage1 libxrandr2 libgtk-3-0 libasound2

# 2. TinyFish CLI
npm install -g @tiny-fish/cli

# 3. Python deps
pip install -r requirements.txt

# 4. Playwright browsers
playwright install chromium

# 5. Env
cp .env.example .env
# Edit .env: set TINYFISH_API_KEY
```

## Chạy nhanh

```bash
# Chụp 3 thiết bị (desktop/tablet/phone)
python tools/capture_devices.py https://kyberswap.com --out ./screenshots/kyberswap

# Chụp full MetaMask wallet flow
python tools/capture_wallet_flow.py --url https://kyberswap.com --out ./screenshots/kyberswap/wallet-flow

# Viết bài hoàn chỉnh
python tools/write_article.py \
    --url https://kyberswap.com \
    --type dex \
    --out ./articles/kyberswap-review-2026.md
```

## Cấu trúc repo

```
tools/
  capture_devices.py       # Screenshot 3 device via TinyFish CDP
  capture_wallet_flow.py   # MetaMask setup + DEX connect flow
  write_article.py         # Research + generate Markdown article
templates/
  dex_review_template.md   # Article template (DEX/swap)
articles/
  kyberswap-review-2026.md # Example output
screenshots/
  kyberswap/               # Example screenshots
    desktop.png / tablet.png / phone.png
    tutorial/              # Step-by-step captures
    wallet-flow/           # MetaMask connect captures
```

## Biến môi trường (.env)

```
TINYFISH_API_KEY=sk-tinyfish-...
PROXY_HOST=103.82.22.77
PROXY_PORT=12775
PROXY_USER=29dt
PROXY_PASS=29dt
MM_EXT_PATH=/opt/metamask          # path to extracted MetaMask extension
USER_DATA_DIR=/tmp/pw-mm-demo      # Playwright persistent profile
```

## Ubuntu headless (Xvfb)

Wallet flow cần hiển thị (MetaMask extension không chạy headless).  
Dùng Xvfb:

```bash
Xvfb :99 -screen 0 1440x900x24 &
export DISPLAY=:99
python tools/capture_wallet_flow.py --url https://kyberswap.com
```

Hoặc dùng script có sẵn:

```bash
./run_wallet_flow.sh https://kyberswap.com
```

## Download MetaMask extension (Ubuntu)

```bash
# Download MetaMask v13 từ GitHub releases
MM_VERSION="13.48.0"
wget "https://github.com/MetaMask/metamask-extension/releases/download/v${MM_VERSION}/metamask-chrome-${MM_VERSION}.zip"
unzip metamask-chrome-${MM_VERSION}.zip -d /opt/metamask
```

## Workflow tự động (cron / Ubuntu service)

```bash
# Viết 1 bài mỗi ngày lúc 8am
0 8 * * * cd /path/to/Tinyfish-review && python tools/write_article.py --url https://newsite.com --type dex >> logs/cron.log 2>&1
```
