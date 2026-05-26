# ⚡ OpsAutopsy AI — Grid Guard Terminal

**OpsAutopsy AI** represents a next-generation, high-performance tactical diagnostics and incident intelligence application engineered for Railway Power Grid Sector 4 control rooms, transmission substations, and rapid field responders. 

The terminal utilizes a state-of-the-art hybrid telemetry analyzer that automatically bridges live multimodal Gemini models with real-time offline-first handbooks. If a physical malfunction, thermal spike, or structural failure is detected, OpsAutopsy parses field inputs and instantly dispatches emergency orders to sector warehouses.

---

## 🎨 Professional Craft & Design System

OpsAutopsy is built with an ultra-premium, eye-safe **Tactile Dark Theme** engineered for prolonged focus in critical low-light dispatch chambers.

*   **Tactile Claymorphism (`.clay-card`, `.clay-card-inset`):** Visual depths mimic military physical flight hardware, establishing clear spatial hierarchy through top-edge light highlights and soft inner inset shadows.
*   **Active Telemetry Scanner Line (`.animate-scan`):** A custom sweeping horizontal lasers-glow line indicating steady-state diagnostic compilation processes.
*   **Bespoke SVG Icon Pairing:** Clean, professional micro-indicators imported exclusively from `lucide-react` provide real-time status telemetry without visual pollution.

---

## 🚀 Key Modules & Capabilities

1.  **Direct Optical Field Camera / Rear-Lens Stream**
    *   Initiate real-time rear inspector camera streams directly within your browser. 
    *   Take high-resolution visual snapshot grabs of mechanical wear, arc-burn pitting, or fluid leakage.
2.  **Acoustic Dictation Transcoder**
    *   A high-gain virtual micro-acoustic transcoder filters out heavy rail locomotive rumble, translating vocal descriptions into clear technician diagnostic notes.
3.  **Autonomous Spares Checkout Engine**
    *   Automatically decodes systemic issues to trigger part reservations (e.g., *VF-400 Ventilation Fans*, *OV-12 Oil Valves*, or *TR-88 Auxiliary Control Units*) with live ETA tracking.
4.  **Standard Operating Procedures (SOP) Hardening**
    *   Compiles custom, context-specific lock-out tag-out (LOTO) checklists to guarantee complete compliance.
5.  **Supervisor Shift Logs**
    *   Outputs instantly exportable high-precision shift briefs including critical ticket index codes (`INC-2026-X`), action parameters, recommendations, and temporary speed restrictions.

---

## 🛠️ Unified Dual-Mode Architecture (Online/Offline)

To prevent operational stalls in dead-signal tunnels, the system is engineered with a **Zero-Latency Fallback Core**:
*   **Online Mode (Gemini 3.5 Flash SDK):** Powered via `@google/genai`. It cross-probes live diagrams, recognizes mechanical parts, and references structural guidelines to outputs schema-hardened diagnostics.
*   **Offline Mode (Local Handbooks):** Instantly triggers if API keys are absent, there is cloud latency, or cellular signal fails, generating highly accurate simulation runs based on exact railway substation blueprints.

---

## 💻 Local Quickstart

### Prerequisites:
*   Ensure **Node.js 18+** is installed on your local workstation.

### Step 1: Install Dependencies
```bash
npm install
```

### Step 2: Configure Environment Variables
Create a `.env` file in the root directory and append your secure Gemini Credentials:
```env
GEMINI_API_KEY=your_secure_google_studio_api_key_here
```

### Step 3: Run Dev Server
Launch your dual-mode Express API and Vite React frontend concurrently on port 3000:
```bash
npm run dev
```

### Step 4: Production Build & Run locally
Compile Express handlers to optimized CommonJS and bundle assets:
```bash
# Build Vite client assets + server bundles
npm run build

# Start production server
npm run start
```

---

## 🌐 Deploying to Vercel (Flawless SPA Redirections)

OpsAutopsy comes pre-configured with a custom `vercel.json` file to support Single Page Application routes, preventing annoying `404 Not Found` messages upon browser refreshes:

### Method A: Git Push (Recommended)
1.  Initialize a new Git repository, commit files, and push to **GitHub/GitLab/Bitbucket**:
    ```bash
    git init
    git add .
    git commit -m "feat: deploy OpsAutopsy terminal"
    git branch -M main
    git remote add origin YOUR_REPO_URL
    git push -u origin main
    ```
2.  Navigate to [Vercel](https://vercel.com) and click **"Add New Project"**.
3.  Import the repository and click **Deploy**. Vercel automatically detects the Vite React frame and compiles static assets to the cloud edge.
4.  *(Optional)* Enter your `GEMINI_API_KEY` in Vercel's **Environment Variables** manager to activate real-time intelligence queries.

### Method B: Vercel CLI (Quick Command)
Deploy directly from your machine terminal in seconds:
```bash
# Install Vercel CLI globally
npm install -g vercel

# Log in and deploy
vercel
```

---

## 📂 Project Structure

```text
├── .env.example       # Example development environment keys
├── .gitignore         # Configured git exclusions (Vercel & Cache excluded)
├── vercel.json        # Unified Vercel route rewrites
├── package.json       # Script and dependency packages
├── server.ts          # Express API endpoint & lazy-loaded Gemini handler
├── src/
│   ├── App.tsx        # High-Fidelity UI, Telemetry, and Lens components
│   ├── index.css      # Styling Sheet, claymorphic matrices, custom `@theme`
│   ├── main.tsx       # Standard Vite React Entry Assembly
│   ├── scenarios.ts   # Substations, Catenaries, and Overload Pre-loads
│   └── types.ts       # Type schemas and Diagnostic structures
```

---

*OpsAutopsy AI Diagnostic Platform — Engineered with precision security for heavy track infrastructures.*
