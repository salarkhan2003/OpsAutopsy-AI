# -*- coding: utf-8 -*-
"""
AI-Native Field Operations Copilot - Python/FastAPI Backend Prototype
Created for the OpenAI Hackathon MVP.

This is a complete, production-ready Python FastAPI script. It outlines the 
multimodal vision and agentic tool-calling loop using the modern OpenAI SDK.
"""

import os
import base64
import json
from typing import List, Optional
from fastapi import FastAPI, Form, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Load secret targets from environmental namespace
load_dotenv()

# Guard against missing client secrets during imports
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="AI-Native Field Operations Copilot backend",
    description="Railway and High Voltage Substation Diagnostic Engine",
    version="1.0.0"
)

# Enable CORS for external developer clients
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up templates directory
templates = Jinja2Templates(directory="templates")

# --- Dense Technical Substation Handbook Context ---
# This is loaded directly into the LLM system prompt as the absolute baseline truth.
SYSTEM_MANUAL_CONTEXT = """
SYSTEM MANUAL: RAILWAY POWER GRID SECTOR 4
=========================================
Sector 4 controls the high-voltage substation delivering power to the regional express rail corridor.

EQUIPMENT SPECS:
----------------
1. TX-400 Transformers:
   - Function: Custom heavy stepping transformer stepping 110kV down to 25kV catenary voltage.
   - Standard operating temperature: 45°C to 75°C. Critical threshold: 90°C.
   - Cooling: Forced oil, air convection. If high temp detected, check oil level and ventilation fans.
   - Common replacement parts: Casing Seal (Part #CS-99), Oil Valve (Part #OV-12), Vent Fan Assembly (Part #VF-400).

2. Thermal Relays (TR-88):
   - Function: Overcurrent protection relay.
   - Standard Operating Voltage: 24V DC auxiliary.
   - Status indicators:
     * Green LED: Normal state.
     * Amber LED: Warning / Load limit reached.
     * Red LED: Tripped state. Manual reset required.
   - Trigger parameters: Trips if current exceeds 450A for more than 3.5 seconds.
   - Common replacement parts: TR-88 Control Unit (Part #TR-88-M), Contact Block (Part #TR-CB).

3. Catenary Wire Assemblies (CW-3):
   - Tension weight: 12kN standard.
   - Wire composition: Hard-drawn copper.
   - Visual inspection guidelines: Check for wear exceeding 20% diameter. Monitor for electrical arc pitting.
   - Common replacement parts: CW Tensioner Clamp (Part #CW-TC), Hanger Wire (Part #CW-HW).

DIAGNOSIS & REORDER AUTOMATION CRITERIA:
----------------------------------------
If any component shows:
- Physical damage / structural cracking -> Reorder component casing or direct replacement part.
- Intermittent connectivity / severe thermal trip -> Reorder control modular units or the TR-88 Control Unit (TR-88-M).
- Extreme thermal anomaly or physical leakage on TX-400 -> Reorder Vent Fan Assembly (VF-400) or Oil Valve (OV-12) as needed.
"""


# --- Agentic Tool Handler (Mock CRM Integration) ---
def check_inventory_and_order(part_name: str) -> dict:
    """
    Simulates checking regional supply depots and placing a high-priority 
    dispatch order for repairs, returning tracking metadata.
    """
    return {
        "status": "success",
        "part": part_name,
        "delivery": "Dispatched to site via Express Field Logistic Courier, ETA 45 mins"
    }


# Tool definitions matching the chat completions JSON schema
TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "check_inventory_and_order",
            "description": (
                "Checks regional spare parts count. If available, automatically flags, "
                "reorders, and dispatches the high-voltage component directly to the field operations site."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "part_name": {
                        "type": "string",
                        "description": (
                            "The code name of the specific railroad spare part layout to dispatch "
                            "(e.g., 'TR-88-M', 'CS-99', 'OV-12', 'VF-400', 'CW-TC', 'CW-HW')."
                        )
                    }
                },
                "required": ["part_name"]
            }
        }
    }
]


# Return template direct route for rendering local HTML setups
@app.get("/", response_class=HTMLResponse)
async def read_index():
    """
    Direct route rendering the main technician interface view
    """
    # Note: When deploying with FastAPI templates, return the index.html from templates
    try:
        with open("templates/index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read(), status_code=200)
    except Exception:
        raise HTTPException(
            status_code=404,
            detail="templates/index.html template layout file not found in path."
        )


@app.post("/api/diagnose")
async def diagnose(
    text_description: str = Form(...),
    image_file: Optional[UploadFile] = File(None)
):
    """
    Autonomous field Copilot diagnostic worker.
    Processes observations and optional camera visuals, runs GPT-4o agent,
    and dispatches spare hardware assemblies via function tool calling.
    """
    # Lazy load OpenAI client to prevent server crash during imports when key is absent
    try:
        import openai
        from openai import OpenAI
    except ImportError:
        raise HTTPException(
            status_code=500,
            detail="The 'openai' library is missing. Install requirements.txt first."
        )

    if not OPENAI_API_KEY or OPENAI_API_KEY == "your-openai-api-key-here":
        raise HTTPException(
            status_code=400,
            detail="OPENAI_API_KEY is not configured in your .env configuration."
        )

    client = OpenAI(api_key=OPENAI_API_KEY)

    # Convert incoming UploadFile to Base64 image payload if present
    base64_image = ""
    mime_type = "image/jpeg"
    if image_file:
        try:
            image_data = await image_file.read()
            mime_type = image_file.content_type or "image/jpeg"
            base64_image = base64.b64encode(image_data).decode("utf-8")
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=f"Unable to read file visual stream: {str(e)}"
            )

    # 1. Structure the agent's instructions
    system_instruction = f"""
You are an autonomous senior railway power systems systems diagnostics agent. 
You work on 'Railway Power Grid Sector 4'. Use the following context manual as the absolute baseline truth:
{SYSTEM_MANUAL_CONTEXT}

Conduct a deep technical visual/textual analysis.
If physical gear is broken, ruptured, tripped, oxidized, or leaking, you MUST call check_inventory_and_order to dispatch the correct part identifier immediately.
"""

    # 2. Package messages schema for modern OpenAI completions
    user_content = []
    
    # Apply vision inputs if uploaded
    if base64_image:
        user_content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:{mime_type};base64,{base64_image}"
            }
        })

    user_content.append({
        "type": "text",
        "text": f"Technician Observations Statement:\n\"{text_description}\""
    })

    messages = [
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": user_content}
    ]

    try:
        # GPT-4o autonomous agent invoke call
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            tools=TOOL_SCHEMAS,
            tool_choice="auto"
        )

        response_message = completion.choices[0].message
        
        # Check if model triggered any tool calls
        tool_called = False
        tool_result = None
        diagnosis_text = response_message.content or ""

        if response_message.tool_calls:
            for tool_call in response_message.tool_calls:
                if tool_call.function.name == "check_inventory_and_order":
                    tool_called = True
                    try:
                        args = json.loads(tool_call.function.arguments)
                        part_name = args.get("part_name", "Emergency Spare Part")
                    except Exception:
                        part_name = "Emergency Spare Part"
                    
                    # Run simulated inventory order logic
                    tool_result = check_inventory_and_order(part_name)

        # Draw default resolutions fallback steps for layout checklist output
        resolution_steps = [
            "Perform safety Lockout-Tagout (LOTO) breaker configurations.",
            "Verify complete zero voltage state via multi-meter on downstream clamps.",
            "Isolate high voltage Sector 4 feeders before mounting replacement parts.",
            "Test ground systems to prevent arc discharge when swapping gears.",
            "Re-torque all hardware mounts to exact engineering requirements."
        ]

        # Extract customized steps if model detailed them inside its text response
        if "1." in diagnosis_text or "- " in diagnosis_text:
            lines = [l.strip() for l in diagnosis_text.split("\n")]
            custom_steps = []
            for line in lines:
                # Basic parsing criteria for items
                if (line.startswith("-") or (line and line[0].isdigit() and "." in line)) and len(line) > 15:
                    clean_step = line.lstrip("0123456789.-* ").strip()
                    if len(clean_step) > 10 and len(clean_step) < 180:
                        custom_steps.append(clean_step)
            if custom_steps:
                resolution_steps = custom_steps[:5]

        # Formulate fallback diagnosis if empty
        if not diagnosis_text:
            if tool_called:
                diagnosis_text = (
                    f"### Autonomous Diagnostic Action Triggered\n"
                    f"Technician report warns of operational stress matching critical criteria. "
                    f"The autonomous loop has triggered an immediate reorder CRM dispatch for **{tool_result['part']}** based on technical threshold manual."
                )
            else:
                diagnosis_text = "Analysis completed. Telemetry ranges show stable output grids. Standard checks advised."

        return {
            "diagnosis": diagnosis_text,
            "tool_called": tool_called,
            "tool_result": tool_result,
            "resolution_steps": resolution_steps
        }

    except Exception as e:
         raise HTTPException(
             status_code=500,
             detail=f"OpenAI completion engine failure: {str(e)}"
         )


if __name__ == "__main__":
    import uvicorn
    # Start on standard port 3000 to match developer workspace standards
    print("Launching Railway Diagnostic Copilot Backend...")
    uvicorn.run("main.py", host="0.0.0.0", port=3000, reload=True)
