# Tinyfish Review — Auto Article Writer

Toolkit tự động viết bài review/tutorial cho các DEX/CEX/Web3 site. 
Chụp screenshot thực tế trên 3 thiết bị → research bằng TinyFish → sinh bài Markdown.

## Stack
- **Python 3.10+**
- **Playwright** — browser automation + screenshot
- **TinyFish CLI** — web search, fetch, remote CDP browser
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

## Download MetaMask extension (Ubuntu)

```bash
MM_VERSION="13.48.0"
wget "https://github.com/MetaMask/metamask-extension/releases/download/v${MM_VERSION}/metamask-chrome-${MM_VERSION}.zip"
unzip metamask-chrome-${MM_VERSION}.zip -d /opt/metamask
# Then set in .env: MM_EXT_PATH=/opt/metamask
```

## Wallet Setup (chạy 1 lần duy nhất)

```bash
# Setup MetaMask + lưu profile vào ~/.tinyfish-review/mm-profile/
# Chỉ cần chạy 1 lần. Profile tồn tại vĩnh viễn qua các lần reboot.
Xvfb :99 -screen 0 1440x900x24 &
DISPLAY=:99 python tools/setup_wallet_once.py
```

Script sẽ:
- Nhập seed phrase từ `WALLET_MNEMONIC` trong `.env`
- Đặt password `WALLET_PASSWORD`
- Lưu profile vào `~/.tinyfish-review/mm-profile/`
- Ghi `~/.tinyfish-review/wallet_ready.flag` (chạy lần 2 sẽ skip tự động)
- Auto-append `USER_DATA_DIR` vào `.env`

Sau khi setup xong, mọi lần chạy tiếp chỉ cần `--reuse`:

```bash
./run_wallet_flow.sh --url https://kyberswap.com --reuse
# MetaMask chỉ unlock bằng password — không cần nhập lại seed
```

## Workflow bình thường (sau setup)

```bash
# Chụp 3 thiết bị (desktop/tablet/phone) — không cần MetaMask
python tools/capture_devices.py https://kyberswap.com --out ./screenshots/kyberswap

# Chụp full wallet connect flow (MetaMask đã setup sẵn)
./run_wallet_flow.sh --url https://kyberswap.com --reuse

# Viết bài hoàn chỉnh (research + generate)
python tools/write_article.py \
 --url https://kyberswap.com \
 --type dex \
 --slug kyberswap-review-2026
```

## Chạy nhanh (all-in-one)

```bash
SITE=https://uniswap.org
SLUG=uniswap-review-2026

python tools/capture_devices.py $SITE
./run_wallet_flow.sh --url $SITE --reuse
python tools/write_article.py --url $SITE --type dex --slug $SLUG --no-screenshots
```

## Cấu trúc repo

```
tools/
 setup_wallet_once.py # Chạy 1 lần — setup MetaMask + lưu session
 capture_devices.py # Screenshot 3 device via TinyFish CDP
 capture_wallet_flow.py # MetaMask connect flow (dùng --reuse sau setup)
 write_article.py # Research + generate Markdown article
templates/
 dex_review_template.md # Article template (DEX/swap)
articles/
 kyberswap-review-2026.md # Example output
screenshots/
 kyberswap/ # Example screenshots
 desktop.png / tablet.png / phone.png
 tutorial/ # Step-by-step captures
 wallet-flow/ # MetaMask connect captures
run_wallet_flow.sh # Ubuntu Xvfb wrapper for wallet flow
```

## Biến môi trường (.env)

```
TINYFISH_API_KEY=sk-tinyfish-...
PROXY_HOST=103.82.22.77
PROXY_PORT=12775
PROXY_USER=29dt
PROXY_PASS=29dt
MM_EXT_PATH=/opt/metamask
USER_DATA_DIR=~/.tinyfish-review/mm-profile # auto-set by setup_wallet_once.py
WALLET_MNEMONIC=word1 word2 ... word12
WALLET_PASSWORD=Demo@Wallet2026!
```

## Session / Cookie được lưu ở đâu?

Playwright `launch_persistent_context` lưu toàn bộ trạng thái trình duyệt 
(cookies, localStorage, extension state, MetaMask keyring) vào `USER_DATA_DIR`.

| File/Folder | Nội dung |
|---|---|
| `~/.tinyfish-review/mm-profile/` | Chromium profile đầy đủ — MetaMask đã unlock |
| `~/.tinyfish-review/wallet_ready.flag` | JSON flag — setup đã xong |
| `~/.tinyfish-review/setup-shots/` | Screenshots từ lần setup ban đầu |

Khi dùng `--reuse`, script chỉ mở lại profile cũ và gõ password để unlock — 
**không nhập lại seed phrase**.

## Workflow tự động (cron / Ubuntu service)

```bash
# Viết 1 bài mỗi ngày lúc 8am
0 8 * * * cd /path/to/Tinyfish-review && \
 python tools/write_article.py --url https://newsite.com --type dex \
 >> logs/cron.log 2>&1
```


---

## Duplicate Prevention (registry.py)

Mỗi bài viết được ghi vào `articles/registry.json` ngay sau khi xuất file.

```bash
# Xem toàn bộ bài đã viết
python tools/registry.py list

# Kiểm tra một URL trước khi chạy pipeline
python tools/registry.py check https://uniswap.org

# Xoá entry để viết lại (hoặc dùng --force)
python tools/registry.py remove https://kyberswap.com

# Đánh dấu đã push git
python tools/registry.py add https://site.com --slug site-review-2026 --type dex --path articles/site-review-2026.md
```

`write_article.py` tự động kiểm tra registry trước khi chạy.  
Nếu URL đã tồn tại → exit với thông báo. Thêm `--force` để viết đè.

---

## Deep Research (deep_research.py)

Thay thế pipeline research cũ, thêm:

| Nguồn | Dữ liệu |
|-------|---------|
| **DeFiLlama API** | TVL, chains, 24h volume (DEX/DeFi) |
| **CoinGecko API** | Giá token, market cap, rank |
| **TinyFish search** | Reviews, fees, referral, security, Reddit sentiment |
| **TinyFish fetch** | Homepage, docs, fees page |

Tất cả data được đưa vào prompt cho AI để sinh bài chi tiết hơn.
