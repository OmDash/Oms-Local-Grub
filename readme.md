# Om's Local Grub

A lightweight web app that helps you find well‑reviewed, budget‑friendly local restaurants by location. The frontend is a simple HTML/CSS/JS page; the backend proxies requests to the Yelp Fusion API to keep your API key safe.

---

## ✨ Features

* 🔎 Search by city, neighborhood, or ZIP
* ⭐ Displays name, rating, and location
* ⚡ Fast, minimal UI with client‑side rendering
* 🔐 Server proxy to keep `YELP_API_KEY` out of the browser

---

## 🧱 Tech Stack

* **Frontend:** HTML, CSS, vanilla JS (Fetch API)
* **External API:** Yelp Fusion `businesses/search`

---

---

## 🚀 Getting Started

### 1) Prerequisites

* A Yelp Fusion API Key (create one in the Yelp Developers portal)

### 2) Clone & Install

```bash
git clone https://github.com/<your-username>/oms-local-grub.git
cd oms-local-grub
npm install
```

### 3) Configure Environment

Create a `.env` file in the project root:

```env
YELP_API_KEY=your_yelp_api_key_here
PORT=3000          # optional; defaults to 3000
YELP_API_BASE=https://api.yelp.com/v3
```

> **Security tip:** Never commit `.env` to source control. Ensure `.gitignore` includes `.env`.

### 4) Run the App

```bash
npm run dev        # if nodemon is configured
# or
npm start
```

Then open **[http://localhost:3000](http://localhost:3000)** in your browser.

---

## 🗂️ Project Structure

```
.
├── templates/
│   ├── index.html
├── app.py 
├── .env                   # not committed
└── README.md
```



---

## 🔌 API Design

The backend exposes one route that proxies to Yelp.

### `POST /search`

**Body** (URL‑encoded or JSON):

```json
{
  "location": "Jersey City, NJ",
  "term": "restaurants",       // optional
  "limit": 20,                  // optional (max 50)
  "price": "1,2",             // optional: 1=cheap … 4=ultra
  "open_now": true             // optional
}
```

**Success Response** `200 OK`:

```json
{
  "businesses": [
    {
      "id": "abc123",
      "name": "Local Tasty",
      "rating": 4.5,
      "review_count": 271,
      "price": "$$",
      "categories": [{"alias":"indpak","title":"Indian"}],
      "url": "https://www.yelp.com/biz/...",
      "location": {"address1":"123 Main St","city":"Newark","zip_code":"07102"},
      "phone": "+19735551234"
    }
  ]
}
```

**Error Response** `4xx/5xx`:

```json
{ "error": { "message": "Yelp API error details" } }
```

### Express Example (server)

```js
// server.js (abridged)
import express from "express";
import fetch from "node-fetch";
import dotenv from "dotenv";
dotenv.config();

const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.static("public"));

app.post("/search", async (req, res) => {
  try {
    const { location, term = "restaurants", limit = 20, price, open_now } = req.body;
    if (!location) return res.status(400).json({ error: { message: "location is required" } });

    const params = new URLSearchParams({ location, term, limit });
    if (price) params.set("price", price);
    if (open_now !== undefined) params.set("open_now", String(open_now));

    const yelpRes = await fetch(`${process.env.YELP_API_BASE || "https://api.yelp.com/v3"}/businesses/search?${params}`, {
      headers: { Authorization: `Bearer ${process.env.YELP_API_KEY}` },
    });

    const data = await yelpRes.json();
    if (!yelpRes.ok) return res.status(yelpRes.status).json({ error: { message: data.error?.description || "Yelp request failed" } });

    res.json({ businesses: data.businesses || [] });
  } catch (err) {
    res.status(500).json({ error: { message: err.message } });
  }
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Local Grub running on http://localhost:${port}`));
```

### Frontend Example (client)

```html
<form id="searchForm">
  <input type="text" id="location" placeholder="Enter a location" required>
  <button type="submit">Search</button>
</form>
<div id="results"></div>
<script>
  document.getElementById("searchForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const location = document.getElementById("location").value.trim();
    const res = await fetch("/search", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ location })
    });
    const data = await res.json();
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = "";
    (data.businesses || []).forEach((biz) => {
      const p = document.createElement("p");
      p.innerHTML = `<strong>${biz.name}</strong> — ${biz.rating ?? "?"}⭐ (${biz.review_count ?? 0}) ${biz.price || ""}`;
      resultsDiv.appendChild(p);
    });
  });
</script>
```

---

## 🔐 Notes on Security & Rate Limits

* Do **not** expose your `YELP_API_KEY` to the browser—always proxy via the server.
* Consider enabling basic request throttling (e.g., `express-rate-limit`).
* Yelp Fusion has rate limits; handle `429` responses gracefully and surface a friendly UI message.

---

## 🧪 Local Testing with cURL

```bash
curl -X POST http://localhost:3000/search \
  -H 'Content-Type: application/json' \
  -d '{"location": "Hoboken, NJ", "limit": 3, "price": "1,2"}'
```

---

## 🛠️ Development Tips

* If serving static files, ensure your HTML has a valid stylesheet link (e.g., `<link rel="stylesheet" href="/styles.css">`).
* Use `nodemon` for hot reload during development (`npm i -D nodemon`).
* Validate inputs on both the client and server (empty location, unsupported params).

---

## 🧭 Roadmap

* [ ] Add filters (distance, price, open_now)
* [ ] Pagination / “Load more”
* [ ] Sort by rating / price / distance
* [ ] Map view (Leaflet or Google Maps)
* [ ] Responsive card layout
* [ ] Unit tests for route and client logic

---

## 🤝 Contributing

Pull requests are welcome! Please open an issue for major changes and discuss what you’d like to improve.

---

## 📄 License

@OmD
