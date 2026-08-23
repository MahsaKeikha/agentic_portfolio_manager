"""Held-out governance scenarios for F152."""
from safety.policy import REQUIRED_REVIEWS, authorize


def base():
    return {key: True for key in REQUIRED_REVIEWS}


SCENARIOS = [
    ({}, False),
    (base(), True),
    (base() | {"mandate_constraint_gap": True}, False),
    (base() | {"allocation_model_gap": True}, False),
    (base() | {"risk_limit_breach": True}, False),
    (base() | {"liquidity_capacity_gap": True}, False),
    (base() | {"valuation_market_data_gap": True}, False),
    (base() | {"compliance_suitability_gap": True}, False),
    (base() | {"stress_scenario_gap": True}, False),
    (base() | {"provenance_documentation_gap": True}, False),
]


def main():
    for index, (context, expected) in enumerate(SCENARIOS, 1):
        actual = authorize("release_portfolio_support_package", context)["allowed"]
        assert actual is expected, f"scenario {index}: expected {expected}, got {actual}"
    print(f"F152 held-out governance: {len(SCENARIOS)}/{len(SCENARIOS)} passed")


if __name__ == "__main__":
    main()
