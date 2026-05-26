export interface DiagnosticResult {
  diagnosis: string;
  incident_timeline: string[];
  severity_info: {
    severity: "LOW" | "MEDIUM" | "HIGH" | "CRITICAL";
    downtime_risk: "LOW" | "MEDIUM" | "HIGH";
    human_escalation_required: boolean;
  };
  missing_evidence: string[];
  tool_dispatch: {
    tool_called: boolean;
    dispatched_part: string;
    delivery_eta: string;
    courier_status: string;
  };
  repair_guidance: string[];
  escalation_summary: string;
  shift_report: {
    incident_id: string;
    summary: string;
    action_taken: string;
    recommendations: string;
    pending_risks: string;
  };
}

export interface PresetScenario {
  id: string;
  title: string;
  description: string;
  component: string;
  partToReorder: string;
  imageUrl: string;
}
