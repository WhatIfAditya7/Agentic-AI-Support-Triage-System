import pandas as pd
import json

from llm_triage import triage_with_llm
from tools.escalate import create_maintenance_ticket

def main():
    print("Loading tickets...")
    df = pd.read_csv("data/tickets.csv")

    print("\nAgentic Triage results:\n")

    for _, row in df.iterrows():
        ticket_id = row["id"]
        text = row["text"]

        result = triage_with_llm(text)

        print(f"\n--- Ticket {ticket_id} ---")
        print(json.dumps(result, indent=2))

        if result["recommended_path"] == "self_help":
            print("\nSelf-help steps:")
            for i, step in enumerate(result["self_help_steps"], start=1):
                print(f"{i}. {step}")
        else:
            maintenance = create_maintenance_ticket(
                summary=result["summary"],
                category=result["category"],
                priority=result["priority"],
            )
            print("\nEscalated to maintenance:")
            print(json.dumps(maintenance, indent=2))

if __name__ == "__main__":
    main()
