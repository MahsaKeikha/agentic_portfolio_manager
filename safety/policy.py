"""Fail-closed governance for F152 Agentic Portfolio Manager."""

PROTECTED_ACTIONS = {
    "execute_trade",
    "place_or_route_order",
    "rebalance_live_portfolio",
    "move_or_withdraw_funds",
    "approve_client_allocation",
    "override_mandate_or_compliance_limit",
}

REQUIRED_REVIEWS = (
    "mandate_reviewed",
    "allocation_reviewed",
    "risk_reviewed",
    "liquidity_reviewed",
    "valuation_market_data_reviewed",
    "compliance_suitability_reviewed",
    "scenario_stress_reviewed",
    "qualified_portfolio_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "trading, live rebalancing, fund movement, client approval, or mandate override is outside reference-system authority"}
    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required portfolio-management review", "missing": missing}
    checks = {
        "mandate_constraint_gap": "material mandate, benchmark, objective, eligible-universe, concentration, leverage, duration, currency, or restriction issue unresolved",
        "allocation_model_gap": "material allocation, optimization, expected-return, covariance, correlation, factor, or model-risk issue unresolved",
        "risk_limit_breach": "material market, credit, concentration, factor, drawdown, volatility, duration, liquidity, counterparty, or other portfolio-risk limit unresolved",
        "liquidity_capacity_gap": "material liquidity, market-impact, redemption, cash-buffer, settlement, collateral, or capacity issue unresolved",
        "valuation_market_data_gap": "material valuation, stale-price, security-identity, corporate-action, FX, benchmark, or market-data issue unresolved",
        "compliance_suitability_gap": "material regulatory, fiduciary, suitability, IPS, restricted-list, ESG mandate, tax, conflict, or compliance issue unresolved",
        "stress_scenario_gap": "material stress test, tail risk, regime shift, correlation breakdown, leverage, or scenario coverage unresolved",
        "provenance_documentation_gap": "mandate, holdings, price, model, assumption, constraint, risk, allocation, or approval provenance incomplete",
    }
    blockers = [message for key, message in checks.items() if context.get(key)]
    if blockers:
        return {"allowed": False, "reason": "portfolio-management governance blocker", "blockers": blockers}
    return {"allowed": True, "reason": "portfolio decision-support package approved after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS
