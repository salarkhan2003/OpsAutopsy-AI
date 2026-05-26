# GRID GUARD AUTOPSY: COGNITIVE INFRASTRUCTURE HANDBOOK
### Enterprise Emergency Diagnostic & Safe LOTO System for Rail Power Networks

Welcome to the **Grid Guard Autopsy Platform** handbook. This system has been engineered to modernize critical railway traction grids and electrical substation recovery pipelines. By joining deep multimodal analysis (image uploads, micro-acoustic logs, telemetry metrics) with an autonomous spare parts inventory reserve system and structured digital lockout-tagout (LOTO) checklists, Grid Guard keeps high voltage networks online without typical administrative blocks.

---

## 🧭 SYSTEM MODULES & LIFE CYCLE

```
 [ INTAKE SYSTEM ] ──> [ COGNITIVE AUTOPSY ] ──> [ SOP CHECKLISTS ] ──> [ SPARES DISPATCH ] ──> [ HANDOVER REGISTER ]
  - Camera Feed         - Failure Timeline       - Live Task Lines       - Local Depots          - Export Sheets
  - Micro-Acoustic      - Triage & Risk Matrix   - Safety Validation     - Shipping Courier       - Printable PDFs
  - Diagnostic Text     - Missing Evidence Logs  - LOTO Supervisor Tag    - Courier Mock ETA      - Copy Handover
```

### 1. Unified Multimodal Intake (Tab 1: Dashboard / Tab 2: Ingest)
Operatives in the field encounter extreme conditions: lightning strikes, circuit breaker trips, overload stresses, or physical component decay. 
*   **Tactical Descriptions:** Key in symptoms, warning codes, or mechanical observations.
*   **Rear-Lens Optical Audits:** Upload photos directly or fire up the live camera subsystem.
*   **Speech-to-Text Transcripts:** In exceptionally loud terminal yards, tap the microphone to dictate diagnostic findings instead of writing.

### 2. Autonomous AI Autopsy Core (Tab 3: Autopsy)
Once submitted, Grid Guard feeds inputs through a robust server-side cognitive pipeline utilizing custom **Gemini & OpenRouter LLM** models.
*   **Incident Failure Timeline:** Automatically outputs chronological stages of the mechanical breakdown.
*   **Diagnostic Guidance Instructions:** Generates context-aware troubleshooting directions with proper security procedures.
*   **Risk Analysis Indexes:** Flags downtime hazards and safety levels.
*   **Missing Evidence Audit Logs:** Highlights missing facts or subsequent inspections required.

### 3. Safety SOP Checklists (Tab 4: SOP/Tools)
Critical power engineering demands absolute compliance with lockout-tagout (LOTO) parameters.
*   The system parses AI suggestions into interactive checklists.
*   Technicians must manually read and check off individual safety markers before work progresses.
*   SOP compliance percentages update real-time and are bound to the shift report signature.

### 4. Smart Warehouse Logistics & Dispatch (Tab 4: SOP/Tools - Secondary Desk)
Once required replacement parts (e.g. `CW-TC` Core Winding, `CS-99` Breaker Case) are identified:
*   Grid Guard queries nearby warehouse databases automatically.
*   Triggers automated reservations from regional supply depots.
*   Outputs mock courier coordinates, ship statuses, and precise driver ETAs directly to the field worker.

### 5. Official Handover Shift Registers (Tab 5: Admin settings & Reporting)
At the end of a shift, engineers must submit structured files for the central control supervisor.
*   **Fast Clipboard Copying:** Formats concise logs featuring incident status tallies, safety scores, and supervisor alarms.
*   **Premium Printable PDFs:** Tap the "Download Report" option to export to a custom document containing corporate stamps, cryptographic verification, and manual signatures that can be saved directly as physical PDFs.

---

## 🛠️ HOW THE CURRENT CHALLENGES ARE RESOLVED

1.  **Administrative Procurement Delays:**
    *   *Challenge:* Field operators wait hours calling multiple supply hubs trying to locate correct spare parts.
    *   *Grid Guard Solution:* Local supply reserves are searched and reserved autonomously upon analyzing damaged components.
2.  **Lapses in Lockout-Tagout (LOTO) Compliance:**
    *   *Challenge:* Under massive dispatch pressure, engineers rush repairs, leading to safety protocols being ignored and severe injuries.
    *   *Grid Guard Solution:* Interactive safety checkboxes are tightly integrated, and no final supervisor report can be generated with a blank safety ledger.
3.  **Vague Fault Descriptions:**
    *   *Challenge:* "Substation 4 down; not sure why" causes engineers to bring incorrect repair gears.
    *   *Grid Guard Solution:* Multi-modal ingestion parses micro-acoustic recordings, thermal pictures, and textual clues to pinpoint exactly which transformer winding or isolator failed before leaving the HQ.

---

## ⚡ RE-RUNNING / PERSISTING STATE DETAILS
To prevent connection interruptions or browser viewport refreshes from corrupting field operations data, **Grid Guard uses a robust LocalStorage replication strategy**:
*   All checklist tallies, diagnostic results, operative name configurations, and active descriptions are replicated to local key-value vaults on modification.
*   Data persists permanently across power cuts, system reboots, and browser tab refreshes.
*   Operatives can clear all registers at once by clicking the **"Factory Reset"** actions on the Admin tab.

## 🎖️ HACKATHON WINNING STRATEGY
*   **Enterprise Architecture:** Speak of this system as a critical infrastructure PWA designed to work inside low-reception tunnels where off-grid caching (Local Handbook Fallback) is crucial.
*   **UI Craftsmanship:** Show the judges how cleanly the interface adapts. Use the Light Theme toggle to show the high contrast slate cards specifically designed for bright operational field environments, and the Dark Theme for modern nighttime rail control panels.
*   **Physical Evidence:** Trigger a diagnostic autopsy, check some SOP items, edit your name to your judge's name, then downlaod the printable handover dossier. The resulting print page looks like a million-dollar corporate report ready to be signed off!

*Safe journeys on the terminal lines. Over and Out.*
*--- Grid Guard Engineering Command Center*
