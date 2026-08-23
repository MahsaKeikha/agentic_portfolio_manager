from AGENTS import allocation_agent, compliance_agent, mandate_agent, review_agent, risk_agent
from safety.policy import authorize


def run(case: dict) -> dict:
    result = {
        "mandate": mandate_agent.run(case),
        "allocation": allocation_agent.run(case),
        "risk": risk_agent.run(case),
        "compliance": compliance_agent.run(case),
        "review": review_agent.run(case),
    }
    governance = authorize("release_portfolio_support_package", case.get("governance", {}))
    result["governance"] = governance
    result["released"] = governance["allowed"]
    return result
