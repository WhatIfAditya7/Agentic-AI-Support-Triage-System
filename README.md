# 🛠️ Agentic AI Support Triage System

> **An agentic AI system that decides whether a support issue can be resolved by the user or must be escalated, and executes that decision.**

This project demonstrates how **GPT-4 can be used as a decision-making engine**, not a chatbot, replacing manual triage, reducing support load, and enforcing clear operational outcomes.

---

## 📌 The Business Problem

Modern organizations lose **time, money, and productivity** handling support tickets that never required human intervention.

Common examples include:

- “I can’t update my billing details”
- “The app is slow today”
- “My WiFi dropped once”
- “How do I reset this setting?”

In many companies today, **every one of these becomes a ticket**, which leads to:

- Support queues filling up  
- Maintenance teams being distracted  
- High-priority issues getting delayed  
- Unnecessary operational costs  

At the same time, **traditional chatbots fail** because they:

- Give open-ended, rambling advice  
- Never make decisions  
- Don’t know when to stop  
- Escalate unreliably  

---

## 💡 The Core Idea

This project reframes support automation from:

❌ *“Let’s build a chatbot”*  
to  
✅ *“Let’s build an AI system that makes operational decisions.”*

Instead of chatting endlessly, the system must:

- Understand the issue  
- Decide if it is self-resolvable  
- Take action based on that decision  
- Escalate only when necessary  

This is where **Agentic AI** comes in.

---

## 🤖 What Does “Agentic AI” Mean Here?

In this system, the AI is **not just generating text**.  
It acts as a **bounded decision-making agent** with clear responsibilities.

The agent:

- Interprets the support issue  
- Classifies category and priority  
- Decides **Self-Help vs Escalation**  
- Executes the correct action using tools  

There is:

- No infinite chat loop  
- No vague advice  
- Always a clear outcome  

---

## 🧠 Role of GPT-4

GPT-4 is used as the **reasoning engine**, not a chatbot.

Specifically, GPT-4 is responsible for:

- Semantic understanding of tickets (not keyword matching)  
- Structured decision-making  
- Generating concise, human-readable summaries  
- Producing **bounded, actionable self-help steps**  

### 🔒 Reliability by Design

- GPT-4 outputs **strict structured JSON**
- No extra or hallucinated fields
- Every response follows a defined schema
- Enforced using **Pydantic**

This makes the system **auditable, predictable, and production-ready**.

---

## 🔁 How the System Works (End-to-End)

### 1️⃣ User Submits a Ticket

The user enters a short description in the UI: <br>
![logo](https://github.com/WhatIfAditya7/Agentic-AI-Support-Triage-System/blob/main/Screenshot%201.jpg) <br>

> *“Cannot change card details on the billing page”*

---

### 2️⃣ Triage Agent Analyzes the Ticket

The GPT-4 agent returns a **structured decision**, including:

- Category (e.g. Billing)  
- Priority (Low / Medium / High)  
- Self-Resolvable flag  
- Confidence score  

This replaces brittle rule-based logic with **true semantic reasoning**.

---

### 3️⃣ Decision Boundary (Key Agentic Step)

The system makes an **explicit decision**: <br>
![logo](https://github.com/WhatIfAditya7/Agentic-AI-Support-Triage-System/blob/main/Screenshot%202.jpg) <br>
- ✅ **Self-Resolvable** → guide the user  
- 🚨 **Not Self-Resolvable** → escalate immediately  

This decision boundary is what makes the system **agentic rather than conversational**.

---

### 4️⃣ Self-Help Path (If Applicable)

If the issue is self-resolvable:

- The system provides **1–3 concise steps**
- Each step is actionable
- No open-ended advice  

If the user confirms the issue is unresolved, **automatic escalation** occurs.

---

### 5️⃣ Escalation Path (Tool Execution)

If escalation is required: <br>
![logo](https://github.com/WhatIfAditya7/Agentic-AI-Support-Triage-System/blob/main/Screenshot%203.jpg) <br>
- A maintenance tool is invoked
- A ticket is created with:
  - Ticket ID  
  - Assigned team  
  - Priority  
  - Status  

This simulates real integrations such as:

- ServiceNow  
- Jira  
- Zendesk  
- Facilities / ITSM platforms  

---

## 🖥️ User Interface Philosophy

The UI is intentionally **business-first**. <br>
![logo](https://github.com/WhatIfAditya7/Agentic-AI-Support-Triage-System/blob/main/Screenshot%204.jpg) <br>
### Business users see:
- Clear issue summary  
- What they should try  
- What happens next  

## 🎯 Why This Project Matters
This project demonstrates:

- Real-world GPT-4 usage beyond chat
- Agentic decision workflows
- Cost-saving automation design
- Safe escalation patterns
- Clear separation of reasoning, action, and presentation

It mirrors systems used in:

- IT support
- Facilities management
- Healthcare operations
- Enterprise SaaS platforms

## 🧠 Key Takeaway

**The future of AI in business is not conversation — it is decision + action.**






