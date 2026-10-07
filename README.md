# 🤖 MF_Virtual_Assistant: Multi-Agent Workflow PoC

A Proof of Concept (PoC) demonstrating a **Multi-Agent System** architecture using the OpenAI Agents SDK. This project explores the critical design pattern of separating "Planning/Reasoning" from "Execution" to build safer, more predictable AI automation workflows.

## 🏗️ Architecture & Engineering Focus
As an AI Agent Developer with a background in Operations and Product Management, my goal with this PoC was to design a system that prioritizes reliability and structured data flow over simple text generation.

**Core Mechanisms Implemented:**
1. **Multi-Agent Handoff:** 
   * **Planner Agent (Temperature 0.5):** Equipped with read-only tools to analyze requests, formulate strategies, and decide if physical execution is required.
   * **Executor Agent (Temperature 0.0):** A strictly deterministic agent that receives precise instructions from the Planner and triggers functional tools (e.g., drafting emails).
2. **Structured Outputs (Pydantic):** Forcing the LLM to return strictly typed data (Booleans, Strings) instead of conversational text, ensuring predictable programmatic behavior in the `if/else` execution flow.
3. **Mocking & Cost Optimization:** Developed a local mock engine for tools (like saving email drafts locally) to test the workflow logic, latency, and agent reasoning without burning API tokens or setting up complex OAuth flows during the initial design phase.

## ⚙️ Tech Stack
* **Framework:** OpenAI Agents SDK (Preview)
* **Data Validation:** Pydantic
* **Language:** Python 3.11
* **Core Concepts:** Agentic Workflows, Tool Calling, Structured Outputs, Chain of Thought constraints.

## 🚀 Future Roadmap
- [ ] Integrate actual Gmail API (Google Cloud OAuth) for live email dispatching.
- [ ] Transition from OpenAI Default models to `gpt-4o-mini` using `ModelSettings` for fine-grained temperature control.
- [ ] Implement an Evaluator-Optimizer loop to auto-correct execution errors.

*Note: This project is part of my active transition into AI Agent Development.*
