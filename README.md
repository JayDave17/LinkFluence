# Linkfluence 🚀

**Linkfluence** is a modern platform connecting creators with businesses for impactful marketing campaigns. It serves as a bridge between influencers looking for brand deals and companies seeking authentication promotion.

![Linkfluence Banner](https://via.placeholder.com/1200x600?text=Connect.+Create.+Grow.)

## ✨ Features

### For Creators 🎨
- **Profile Management**: Create a professional profile showcasing bio, stats, and social links.
- **Service Packages**: Define custom service packages (e.g., "Instagram Post", "YouTube Integration") with pricing.
- **Discovery**: Find businesses actively looking for creators.
- **Direct Messaging**: Communicate directly with businesses about opportunities.

### For Businesses 💼
- **Campaign Management**: Create and manage marketing campaigns with budgets and descriptions.
- **Creator Discovery**: Search and filter creators by category (Tech, Lifestyle, etc.) and follower count (Nano, Micro, Macro).
- **Analytics**: View creator stats like follower count and engagement rates.
- **Application Management**: Review applications from creators and initiate conversations.

### General 🌟
- **Dark Mode**: Fully supported dark/light theme toggle.
- **Responsive Design**: Optimized for desktop and mobile devices.
- **Secure Authentication**: Robust login and registration system.

## 🛠️ Tech Stack

- **Frontend**: React.js, Vite, Tailwind CSS
- **Backend**: Python, Flask
- **Database**: MongoDB
- **State Management**: React Hooks

## 🚀 Getting Started

### Prerequisites
- Node.js (v16+)
- Python (v3.8+)
- MongoDB running locally or a connection string

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Heavenly-Demon-0835/LinkFluence.git
   cd LinkFluence
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   # source venv/bin/activate
   pip install -r requirements.txt
   cp .env.example .env   # then edit MONGO_URI
   python app.py
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## 📦 Deployment

Production runs as two services: the **Flask API on Railway**, the **React app on Vercel**,
with **MongoDB Atlas** behind both.

### 1. MongoDB Atlas

1. Create a free **M0** cluster.
2. **Database Access** → add a user with *Read and write to any database*.
3. **Network Access** → allow `0.0.0.0/0`. Railway does not publish static
   egress IPs on the trial/hobby plans, so an allowlist of specific addresses will
   not work.
4. Copy the connection string and **append the database name to the path**:

   ```
   mongodb+srv://USER:PASS@cluster.mongodb.net/linkfluence?retryWrites=true&w=majority
                                               ^^^^^^^^^^^ required
   ```

   Both the API and the seeder resolve the database name from this URI. Omit it and
   they fall back to guessing, which is how the two end up in different databases.

### 2. Backend → Railway

1. **New Project** → *Deploy from GitHub repo* → pick this repository.
2. **Settings → Root Directory: `backend`.** This is the one setting that is not in
   version control and the deploy will fail without it — the repository root has no
   `requirements.txt`, so the builder cannot detect a Python app.
3. Add the variables under **Variables**:

   | Variable | Value |
   |---|---|
   | `MONGO_URI` | the Atlas string from step 1 |
   | `PYTHONUNBUFFERED` | `1` — stream logs instead of buffering them |
   | `PYTHONIOENCODING` | `utf-8` — the startup logs contain emoji |
   | `SEED_ON_STARTUP` | `false` (see step 5) |

   Do **not** set `PORT`; Railway injects it and `railway.json` binds Gunicorn to it.
4. **Settings → Networking → Generate Domain** to get a public URL. Confirm it:

   ```bash
   curl https://YOUR-APP.up.railway.app/health
   ```

5. To load the demo accounts, set `SEED_ON_STARTUP=true`, let it redeploy once, then
   **set it back to `false`**. The seeder is idempotent, but it otherwise re-runs on
   every worker boot.

Build and runtime settings live in [`backend/railway.json`](backend/railway.json)
and [`backend/.python-version`](backend/.python-version) — no dashboard start
command needed.

### 3. Frontend → Vercel

1. Import the repository and set the **Root Directory** to `frontend`.
2. Add an environment variable **`VITE_API_BASE_URL`** = your Railway URL, with **no
   trailing slash** (`https://YOUR-APP.up.railway.app`). Vite inlines this at *build*
   time, so changing it later requires a redeploy, not just a restart.
3. Deploy. `vercel.json` already rewrites all routes to `index.html` for React Router.

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License
This project is licensed under the MIT License.
