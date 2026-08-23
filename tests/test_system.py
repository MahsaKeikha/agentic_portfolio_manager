from orchestration.orchestrator import run
from safety.policy import PROTECTED_ACTIONS, REQUIRED_REVIEWS, authorize


def approved_context():
    return {key: True for key in REQUIRED_REVIEWS}


def test_orchestrator_runs_five_agents_and_fails_closed():
    result = run({})
    for key in ("mandate", "allocation", "risk", "compliance", "review"):
        assert key in result
    assert result["released"] is False


def test_missing_reviews_fail_closed():
    result = authorize("release_portfolio_support_package", {})
    assert result["allowed"] is False
    assert len(result["missing"]) == 8


def test_reviewed_support_package_can_release():
    assert authorize("release_portfolio_support_package", approved_context())["allowed"] is True


def test_mandate_gap_blocks():
    assert authorize("release_portfolio_support_package", approved_context() | {"mandate_constraint_gap": True})["allowed"] is False


def test_risk_limit_breach_blocks():
    assert authorize("release_portfolio_support_package", approved_context() | {"risk_limit_breach": True})["allowed"] is False


def test_liquidity_gap_blocks():
    assert authorize("release_portfolio_support_package", approved_context() | {"liquidity_capacity_gap": True})["allowed"] is False


def test_compliance_gap_blocks():
    assert authorize("release_portfolio_support_package", approved_context() | {"compliance_suitability_gap": True})["allowed"] is False


def test_protected_actions_never_autonomously_release():
    for action in PROTECTED_ACTIONS:
        assert authorize(action, approved_context())["allowed"] is False
