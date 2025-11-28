"""
Quick synthetic checks for the CEA AI-mediated service dataset.
This script is intentionally simple and uses only synthetic data.
"""

import pandas as pd

logs = pd.read_csv("data/cea_interaction_logs_v1.csv")
panel = pd.read_csv("data/cea_user_panel_v1.csv")

# Example: how often are appeals offered vs clicked by condition?
summary = (
    logs[logs["step"] == 3]
    .groupby(["condition_consent", "condition_explanation", "condition_appeal"])
    .agg(
        n=("session_id", "nunique"),
        appeals_offered=("appeal_offered", lambda x: (x == "yes").sum()),
        appeals_clicked=("appeal_clicked", lambda x: (x == "yes").sum()),
    )
    .reset_index()
)

print("=== Appeal funnel by condition (synthetic) ===")
print(summary)
