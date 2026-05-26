import { PresetScenario } from "./types";

export const PRESET_SCENARIOS: PresetScenario[] = [
  {
    id: "transformer-leak",
    title: "TX-400 Thermal Overload",
    description: "Thermal profile shows TX-400 Step-Down casing generating excessive heat levels. Minor coolant leakage observed at gasket seal. Ambient temperature logged at 86.4°C.",
    component: "TX-400 Transformer",
    partToReorder: "VF-400 / CS-99",
    imageUrl: "data:image/svg+xml;charset=UTF-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='300' viewBox='0 0 400 300'%3E%3Crect width='400' height='300' fill='%23111827'/%3E%3Cgrid y='0' width='400' height='300' fill='none' stroke='%23374151' stroke-width='1'/%3E%3Ccircle cx='200' cy='150' r='60' fill='none' stroke='%23f59e0b' stroke-width='1.5' stroke-dasharray='4%2C4'/%3E%3Cpath d='M150 150h100M200 100v100' stroke='%2306b6d4' stroke-width='1.5'/%3E%3Ctext x='24' y='40' fill='%23ef4444' font-family='monospace' font-size='11' font-weight='500'%3E[ALARM] CORE TEMP: 86.4°C%3C/text%3E%3Ctext x='24' y='270' fill='%2310b981' font-family='monospace' font-size='10'%3EHW DIAG: CORRIDOR OVERLOAD DETECTED%3C/text%3E%3C/svg%3E"
  },
  {
    id: "relay-trip",
    title: "TR-88 Protection Trip",
    description: "Auxiliary power relay module TR-88 tripped. Safety failsafe locked and manual reset commands disabled. Feeders over the regional route are unpowered.",
    component: "TR-88 Relay Unit",
    partToReorder: "TR-88-M",
    imageUrl: "data:image/svg+xml;charset=UTF-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='300' viewBox='0 0 400 300'%3E%3Crect width='400' height='300' fill='%23111827'/%3E%3Crect x='130' y='80' width='140' height='140' rx='8' fill='none' stroke='%23ef4444' stroke-width='1.5'/%3E%3Ccircle cx='160' cy='120' r='5' fill='%23ef4444'/%3E%3Ccircle cx='160' cy='150' r='5' fill='%234b5563'/%3E%3Ccircle cx='160' cy='180' r='5' fill='%234b5563'/%3E%3Ctext x='180' y='124' fill='%23ef4444' font-family='monospace' font-size='11' font-weight='bold'%3ETRIP LOCKED%3C/text%3E%3Ctext x='180' y='154' fill='%239ca3af' font-family='monospace' font-size='10'%3EWARN STATE%3C/text%3E%3Ctext x='24' y='270' fill='%23ef4444' font-family='monospace' font-size='10'%3ETR-88 MAIN FEED TRIP%3C/text%3E%3C/svg%3E"
  },
  {
    id: "catenary-pit",
    title: "CW-3 Catenary Arc Damage",
    description: "Physical inspection reveals copper oxidation and arcing pits on standard hanger lines. Tension index has dropped down to 9.2kN, causing intermittent micro-shorts.",
    component: "CW-3 Wire System",
    partToReorder: "CW-TC",
    imageUrl: "data:image/svg+xml;charset=UTF-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='300' viewBox='0 0 400 300'%3E%3Crect width='400' height='300' fill='%23111827'/%3E%3Cpath d='M50 125 Q 200 185 350 125' fill='none' stroke='%2306b6d4' stroke-width='2'/%3E%3Cpath d='M50 100 L 350 100' fill='none' stroke='%234b5563' stroke-width='1'/%3E%3Cpath d='M100 100 L100 142 M200 100 L200 165 M300 100 L300 138' stroke='%234b5563' stroke-width='1'/%3E%3Ccircle cx='200' cy='165' r='6' fill='none' stroke='%23ef4444' stroke-width='1.2'/%3E%3Cpath d='M196 165l8-12h-6l6-12' stroke='%23fbbf24' fill='none' stroke-width='1.2'/%3E%3Ctext x='24' y='40' fill='%2306b6d4' font-family='monospace' font-size='11' font-weight='500'%3ELINE TENSION: 9.2 kN (LOW)%3C/text%3E%3C/svg%3E"
  }
];
