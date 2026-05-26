# ⚡ OpsAutopsy AI — Grid Guard Failure Analysis Terminal

**OpsAutopsy AI** is an enterprise-grade industrial operations and incident diagnostic platform engineered for power grid substation engineers, electrical maintenance crews, and railway track infrastructure dispatchers.

The terminal serves as a high-reliability visual and analytical diagnostics compiler, pairing advanced machine learning with localized reference guides to reconstruct equipment outages, track component wear, and secure compliance during critical system maintenance.

---

## 🎨 Enterprise Design System & Usability

The application UI is designed to reduce strain during extended monitoring shifts in low-light environments:

*   **High-Contrast Claymorphic Layout (`.clay-card`):** Provides subtle visual separation, clear shadow boundaries, and optimized typography for quick reading under high-stress incident scenarios.
*   **Dual-Theme Ingress:** Includes standard dark operational mode and high-contrast light mode to accommodate varying outdoor ambient light conditions during field maintenance.
*   **Unified UI Elements:** Utilizes clean icons from `lucide-react` paired with descriptive, non-sensational labeling to support standard control-room workflows.
*   **Touch and Desktop Responsiveness:** Built on mobile-first responsive guidelines ensuring accessible 44px tap targets on tablet and rug-ruggedized field terminals.

---

## 🚀 Key Operations & Diagnostic Modules

1.  **Optical Field Inspection Intake**
    *   Initialize localized rear-lens camera streams or drag-and-drop reference photography of mechanical damage (such as transformer bushing leaks, relay soot deposition, or contact wire wear).
2.  **Voice Observation Logger**
    *   Provides hands-free audio recording to log verbal observations and automatically append transcribed structural details directly to the active intake card.
3.  **Failure Sequence Reconstruction**
    *   Provides a structured mechanical-electrical fault timeline, estimates critical risk metrics, and rates fault severities using standardized industry classifications (Critical, Warning, Low).
4.  **Lockout-Tagout (LOTO) & SOP Compliance**
    *   Generates context-aware LOTO safety checklists. Technicians can check off completed isolates and sign off digitally before starting live repairs.
5.  **Equipment Dispatch & Inventory Allocations**
    *   Enables parts reservation logging (such as cooling fans, oil gaskets, or high-density electrical relays) with trackable stock ETAs and dispatch flags.
6.  **Supervisor Escalations**
    *   Provides escalation pathways to dispatch managers and generates formal structured incident records (`INC-2026-X`).
7.  **Shift Report Compilation & PDF Export**
    *   Compiles analytical findings, LOTO compliance percentages, technician credentials, and temporary track/speed restrictions into structured, printable PDF logs.

---

## ⚙️ Core Architecture (Local & Connected Operating States)

To ensure field reliability during grid disconnection, the terminal features a resilient dual-state architecture:
*   **Connected Mode (Gemini AI Service):** Powered by the official `@google/genai` SDK on the backend. This handles live image analysis, processes field reports, and matches issues against historic equipment indices.
*   **Local Mode (Fallback Handbooks):** Instantly runs standard pre-loaded failure diagnostic configurations locally if network connections are lost.

---

## 💻 Local Quickstart

### Prerequisites:
*   **Node.js 18+** installed on the deployment machine.

### Step 1: Install Package Dependencies
```bash
npm install
```

### Step 2: Configure Environment Variables
Create a `.env` file in the project's root folder and add your Gemini credentials:
```env
GEMINI_API_KEY=your_secure_google_studio_api_key_here
```

### Step 3: Run the Development Server
Execute the concurrent Vite and Express builder on port 3000:
```bash
npm run dev
```

### Step 4: Production Compilation & Run
Compile the TypeScript backend server to optimized CommonJS and bundle the React web assets:
```bash
# Build the client and compile the server bundle to CJS
npm run build

# Boot the production web server
npm run start
```

---

## 📂 Project Structure

```text
├── .env.example       # Example development environment keys
├── .gitignore         # Exclusions for production artifacts and packages
├── vercel.json        # Single Page Application path forwarding config
├── package.json       # Node package manager scripts and declarations
├── server.ts          # Express web server & lazy-loaded Gemini client
├── src/
│   ├── App.tsx        # Base React UI shell and core diagnostic routes
│   ├── index.css      # Custom Tailwind styling directives & theme setup
│   ├── main.tsx       # Standard entry node for the client framework
│   ├── scenarios.ts   # Blueprints for local offline scenario simulations
│   └── types.ts       # Type interfaces for logs, telemetry, and diagnostics
```

---

*OpsAutopsy AI Diagnostic Platform — Operational integrity and predictive maintenance for transit and utility grid infrastructure.*
