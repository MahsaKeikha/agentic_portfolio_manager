# F152 | Agentic Portfolio Manager | L3 Gold Standard | v1.0

A governed five-agent reference architecture for portfolio-management decision support across mandate interpretation, asset allocation, portfolio construction, risk, liquidity, compliance, suitability, stress testing, monitoring, rebalancing analysis, provenance, and qualified human approval.

F152 is decision-support infrastructure. It is not a broker, adviser, fiduciary, custodian, order-management system, execution-management system, or autonomous portfolio manager. It cannot execute trades, place or route orders, rebalance a live portfolio, move or withdraw funds, approve a client allocation, or override a mandate or compliance limit.

## Portfolio-management lifecycle

```text
Mandate and Investment Policy
        -> Strategic and Tactical Allocation Analysis
        -> Portfolio Construction
        -> Risk, Liquidity, and Stress Review
        -> Compliance and Suitability Review
        -> Qualified Portfolio Approval
        -> Human-Controlled Trading and Administration
```

The workflow fails closed when required reviews are missing or when material mandate, allocation-model, risk-limit, liquidity, valuation, market-data, compliance, suitability, stress, or provenance issues remain unresolved.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Mandate Agent | Structures objectives, benchmark, eligible universe, restrictions, horizon, liquidity needs, risk tolerance, concentration, currency, tax, leverage, and governance | What is the portfolio legally and contractually allowed and intended to do? |
| Allocation Agent | Develops strategic and tactical allocation options, expected-return assumptions, diversification, factor exposures, optimization, and scenario comparisons | How can capital be allocated within the mandate without hiding model uncertainty? |
| Risk Agent | Reviews market, credit, factor, concentration, drawdown, duration, liquidity, leverage, counterparty, tail, and scenario risks | What could cause unacceptable loss, forced selling, or mandate failure? |
| Compliance Agent | Checks investment-policy constraints, suitability, restrictions, fiduciary issues, conflicts, restricted lists, ESG constraints, tax considerations, and approvals | Is the proposed portfolio consistent with applicable rules and client or institutional constraints? |
| Review Agent | Synthesizes allocation, risk, compliance, liquidity, valuation, uncertainty, tradeoffs, and unresolved issues for qualified human approval | Is the portfolio-support package ready for authorized human decision making? |

Agents support portfolio managers, investment committees, wealth-management teams, institutional investors, advisers, risk teams, compliance teams, asset owners, and research organizations. They do not replace regulated professionals, fiduciaries, trustees, compliance officers, traders, custodians, tax professionals, legal counsel, or client decision makers.

## Repository structure

```text
AGENTS/
├── mandate_agent.py
├── allocation_agent.py
├── risk_agent.py
├── compliance_agent.py
└── review_agent.py

SKILLS/
├── mandate_reasoning.py
├── allocation_reasoning.py
├── risk_reasoning.py
├── compliance_reasoning.py
└── review_reasoning.py

TOOLS/
├── mandate_registry.py
├── allocation_matrix.py
├── constraint_checker.py
├── stress_tester.py
└── approval_gate.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

## Mandate architecture

The executable policy requires `mandate_reviewed`. `mandate_constraint_gap` blocks release when material mandate, benchmark, objective, eligible-universe, concentration, leverage, duration, currency, or restriction issues remain unresolved.

`TOOLS/mandate_registry.py` can preserve mandate identifier, client or fund type, benchmark, investment objective, horizon, liquidity need, eligible assets, prohibited assets, concentration limits, leverage limits, currency limits, duration limits, ESG constraints, tax constraints, reporting requirements, approval authority, effective date, and version.

## Investment policy statement

An investment policy statement can define objectives, risk tolerance, horizon, liquidity needs, constraints, governance, benchmarks, rebalancing expectations, permitted assets, prohibited activities, and delegated authority.

F152 should never infer client authority or investment discretion from incomplete documentation.

## Objectives

Objectives can include capital preservation, income, total return, inflation protection, liability matching, growth, diversification, liquidity, or mission-related requirements. Conflicting objectives should be surfaced as tradeoffs.

## Time horizon

Time horizon affects acceptable volatility, liquidity, duration, drawdown tolerance, and asset selection. Short-term obligations should not be funded using assumptions suitable only for long-term capital.

## Liquidity needs

Expected withdrawals, benefit payments, capital calls, operating needs, redemptions, taxes, margin, collateral, and contingencies should be incorporated into portfolio analysis.

## Eligible universe

The eligible universe should identify permitted asset classes, instruments, geographies, currencies, ratings, sectors, structures, derivatives, private assets, and other restrictions.

## Prohibited investments

Prohibitions can arise from law, mandate, client preference, organizational policy, sanctions, restricted lists, ESG rules, concentration rules, liquidity policy, or fiduciary constraints.

## Benchmark architecture

Benchmarks should match the portfolio objective closely enough to support meaningful evaluation. A benchmark can serve as performance reference, risk reference, policy anchor, or combination of these roles.

Benchmark choice can materially affect perceived alpha, beta, tracking error, and attribution.

## Strategic asset allocation

Strategic allocation defines long-term policy weights or ranges based on objectives, liabilities, capital-market assumptions, risk tolerance, and constraints.

Strategic allocation should not be treated as permanent when objectives, liabilities, market structure, or mandate conditions materially change.

## Tactical allocation

Tactical allocation can express shorter-horizon deviations from strategic weights. Tactical views should have explicit rationale, size limits, expected horizon, risk contribution, and exit or review criteria.

## Allocation architecture

The executable policy requires `allocation_reviewed`. `allocation_model_gap` blocks release when material allocation, optimization, expected-return, covariance, correlation, factor, or model-risk issues remain unresolved.

`TOOLS/allocation_matrix.py` can preserve asset, current weight, target weight, permitted range, expected return, risk estimate, factor exposure, liquidity class, currency, contribution to risk, and scenario behavior.

## Capital-market assumptions

Expected returns, volatility, correlations, yields, spreads, inflation, growth, and currency assumptions are uncertain inputs rather than observed truths.

Assumptions should include source, date, horizon, methodology, range, and review status.

## Diversification

Diversification depends on economic drivers, not merely number of holdings. Assets that appear different can become highly correlated during stress.

## Correlation

Historical correlation can be unstable. Regime changes, liquidity shocks, leverage, common funding sources, or macro events can cause correlations to rise when diversification is most needed.

## Factor exposures

Portfolios can carry equity beta, duration, credit, inflation, value, growth, momentum, quality, size, commodity, currency, volatility, liquidity, and other systematic exposures.

Factor labels should not replace security-level understanding.

## Mean-variance optimization

Optimization can be highly sensitive to expected-return and covariance assumptions. F152 should avoid presenting mathematically precise weights as uniquely optimal when inputs are uncertain.

## Robust optimization

Robust techniques can constrain sensitivity to estimation error, but they do not eliminate model risk. Results should still be stress tested and reviewed against practical constraints.

## Risk parity

Risk-parity approaches allocate by estimated risk contribution rather than capital weight. Their behavior can change materially with leverage, volatility estimation, correlation shifts, and rate regimes.

## Liability-aware portfolios

Pensions, insurers, endowments, foundations, and other institutions can require explicit consideration of liabilities, spending needs, funding status, duration, inflation exposure, and cash-flow timing.

## Risk architecture

The executable policy requires `risk_reviewed`. `risk_limit_breach` blocks release when material market, credit, concentration, factor, drawdown, volatility, duration, liquidity, counterparty, or other portfolio-risk limits remain unresolved.

## Market risk

Market risk includes equity, interest-rate, spread, currency, commodity, volatility, and cross-asset exposures. Portfolio behavior should be evaluated under multiple regimes.

## Volatility

Volatility is only one risk measure. Low measured volatility can coexist with severe liquidity, leverage, credit, or tail risk.

## Drawdown

Drawdown analysis can include historical peak-to-trough loss, recovery time, scenario drawdown, and consequences for spending, redemptions, leverage, and investor behavior.

## Value at risk

VaR and related measures can summarize modeled loss distributions but depend on assumptions about distributions, correlations, liquidity, and time horizon. They should not be treated as maximum-loss guarantees.

## Expected shortfall

Expected shortfall can provide information about tail losses beyond a VaR threshold, but it remains model dependent.

## Concentration

Concentration can occur by issuer, sector, industry, country, currency, factor, strategy, counterparty, liquidity source, funding source, or economic theme.

## Credit risk

Credit risk can include default, downgrade, spread widening, recovery, seniority, collateral, covenant, and concentration effects.

## Duration and rate risk

Fixed-income and liability-sensitive portfolios should distinguish modified duration, key-rate duration, convexity, floating-rate exposure, inflation sensitivity, and yield-curve risk where appropriate.

## Currency risk

Currency exposure can arise from security denomination, economic exposure, hedging, derivatives, cash flows, and liabilities. Hedging itself creates cost, basis, counterparty, and liquidity risk.

## Counterparty risk

Derivatives, securities lending, swaps, repos, prime brokerage, deposits, and other arrangements can create counterparty and collateral exposure.

## Leverage

Leverage can arise through borrowing, derivatives, short positions, financing, embedded product structures, and liabilities. Gross and net exposure alone may not capture all leverage risk.

## Short positions

Short positions can have theoretically unlimited loss, borrow costs, recalls, squeeze risk, corporate-action complexity, and liquidity constraints.

## Derivatives

Derivatives can be used for hedging, efficient exposure, duration management, currency management, or other permitted purposes. They can also create nonlinear risk, margin needs, basis risk, counterparty risk, and leverage.

F152 does not autonomously execute derivatives transactions.

## Options

Option exposures can include delta, gamma, vega, theta, skew, term structure, jump risk, liquidity, and assignment or exercise considerations.

## Private assets

Private equity, venture, private credit, real estate, infrastructure, and other illiquid assets can involve stale valuations, capital calls, distribution uncertainty, limited transparency, long lockups, and appraisal smoothing.

## Liquidity architecture

The executable policy requires `liquidity_reviewed`. `liquidity_capacity_gap` blocks release when material liquidity, market-impact, redemption, cash-buffer, settlement, collateral, or capacity issues remain unresolved.

## Market liquidity

Market liquidity depends on instrument, size, venue, market conditions, time of day, volatility, dealer balance sheets, and position size.

## Funding liquidity

Funding liquidity concerns the ability to meet cash needs, collateral calls, redemptions, operating expenses, and other obligations without forced selling.

## Cash buffers

Cash buffers can protect against forced sales but create opportunity cost and benchmark drag. Required levels should reflect actual obligations and stress scenarios.

## Capacity

A strategy can become less effective as assets grow because of market impact, limited opportunity set, liquidity, crowding, or implementation costs.

## Market impact

Large transactions can move prices. Portfolio support may estimate implementation sensitivity, but trade execution remains outside F152 authority.

## Stress testing

The executable policy requires `scenario_stress_reviewed`. `stress_scenario_gap` blocks release when material stress tests, tail risks, regime shifts, correlation breakdowns, leverage, or scenario coverage remain unresolved.

`TOOLS/stress_tester.py` can support deterministic scenario definitions and output comparisons.

## Historical stress

Historical scenarios can include market crises, rate shocks, inflation shocks, credit events, liquidity events, currency crises, commodity shocks, and other episodes relevant to the portfolio.

Historical repetition should not be assumed.

## Hypothetical stress

Hypothetical scenarios can combine shocks that have not occurred together historically but remain economically plausible.

## Reverse stress testing

Reverse stress testing asks what combination of events would cause a mandate breach, liquidity failure, unacceptable drawdown, margin problem, or inability to meet obligations.

## Tail risk

Tail-risk analysis should include nonlinear exposures, leverage, liquidity, concentration, gap risk, and model failure rather than relying only on normal-distribution assumptions.

## Valuation and market data architecture

The executable policy requires `valuation_market_data_reviewed`. `valuation_market_data_gap` blocks release when material valuation, stale-price, security-identity, corporate-action, FX, benchmark, or market-data issues remain unresolved.

## Pricing

Public securities, derivatives, private assets, thinly traded securities, and structured products may require different pricing sources and valuation methods.

## Stale prices

Stale prices can understate volatility and distort weights, risk, performance, and liquidity estimates.

## Corporate actions

Splits, dividends, mergers, spinoffs, tender offers, conversions, rights, delistings, and other corporate actions can affect holdings and benchmarks.

## Security identity

Identifiers, tickers, share classes, exchanges, currencies, and instrument types should be resolved precisely before aggregation or constraint checking.

## Compliance architecture

The executable policy requires `compliance_suitability_reviewed`. `compliance_suitability_gap` blocks release when material regulatory, fiduciary, suitability, IPS, restricted-list, ESG mandate, tax, conflict, or compliance issues remain unresolved.

`TOOLS/constraint_checker.py` can support deterministic review of encoded mandate constraints. Passing software checks does not constitute legal or compliance approval.

## Suitability

Client-specific suitability can depend on objectives, financial circumstances, experience, tax situation, liquidity needs, horizon, risk tolerance, legal restrictions, and other factors.

F152 cannot make a binding suitability determination.

## Fiduciary duty

Where fiduciary duties apply, authorized humans must consider governing law, mandate, loyalty, care, prudence, diversification, cost, conflicts, documentation, and beneficiary or client interests.

## Investment-policy compliance

Portfolio proposals should be checked against permitted ranges, issuer limits, asset-class limits, ratings, maturities, currencies, leverage, derivatives rules, liquidity, prohibited assets, and other applicable constraints.

## Restricted lists

Restricted, watch, blackout, sanctions, personal-trading, issuer, and other compliance lists should be enforced by authorized organizational systems.

## Conflicts of interest

Conflicts can arise from compensation, affiliates, proprietary products, personal holdings, research relationships, counterparties, soft dollars, banking relationships, or other incentives.

## ESG and mission constraints

ESG, sustainability, responsible-investment, faith-based, mission-related, or exclusionary mandates require explicit definitions and evidence. Provider ratings should not be treated as equivalent when methodologies differ.

## Tax awareness

Tax considerations can affect turnover, realization of gains and losses, location of assets, distributions, withholding, and after-tax returns. F152 can support analysis but does not replace tax professionals.

## Wash-sale and jurisdiction rules

Tax rules can vary by jurisdiction and change over time. Automated portfolio suggestions should not be treated as tax advice or legal determination.

## Rebalancing

Rebalancing analysis can compare current and target exposures, drift, risk contribution, taxes, transaction costs, liquidity, and mandate ranges.

`rebalance_live_portfolio` is protected. F152 can prepare a rebalancing support package but cannot change a live account.

## Threshold rebalancing

Threshold approaches can trigger review when weights or risks move outside predefined bands. Triggering analysis does not authorize a trade.

## Calendar rebalancing

Calendar-based review can provide governance discipline but may ignore rapid changes in risk, liquidity, or mandate conditions.

## Transaction costs

Expected transaction costs can include commissions, spread, market impact, taxes, fees, financing, borrow costs, and implementation delay.

## Turnover

Turnover can create cost, tax, operational complexity, and deviation from long-term policy. Higher activity should require a clear expected benefit.

## Portfolio monitoring

Monitoring can cover mandate drift, risk limits, cash, liquidity, exposures, factor concentrations, credit events, corporate actions, manager changes, benchmarks, model changes, and compliance status.

Monitoring alerts remain decision support, not execution authority.

## Performance measurement

Performance should preserve return period, currency, benchmark, cash flows, fees, valuation sources, and calculation methodology.

## Time-weighted return

Time-weighted return can reduce the effect of external cash-flow timing and is often used for manager evaluation.

## Money-weighted return

Money-weighted return reflects timing and magnitude of cash flows and can be more relevant to an investor's realized experience.

## Attribution

Performance attribution can decompose allocation, selection, factor, currency, duration, yield-curve, credit, or other effects depending on portfolio type and methodology.

Attribution is model dependent and should reconcile to total performance within documented tolerances.

## Risk attribution

Risk attribution can identify which positions, factors, sectors, currencies, strategies, or asset classes contribute most to estimated portfolio risk.

## Benchmark-relative risk

Tracking error, active share, beta, factor differences, and concentration relative to benchmark can be useful, but a benchmark itself may not represent the portfolio's true objective.

## Active risk budget

Active risk budgets can allocate tracking error or other risk across strategies or managers. Risk contributions can change rapidly under market stress.

## Manager selection

Multi-manager portfolios may evaluate process, people, performance, risk, capacity, liquidity, fees, operations, compliance, style consistency, and organizational stability.

Past performance should not be treated as proof of future skill.

## Funds and ETFs

Portfolio analysis can consider holdings, methodology, fees, liquidity, tracking, tax structure, securities lending, derivatives, concentration, index rules, and operational structure.

## Cash management

Cash management can include liquidity tiers, operating cash, collateral, short-term instruments, counterparty exposure, yield, maturity, and settlement needs.

## Currency hedging

Currency-hedging policy should consider liabilities, strategic objective, cost, carry, basis, liquidity, collateral, and governance.

## Inflation risk

Inflation can affect nominal bonds, real assets, equities, liabilities, spending, wages, commodities, and currencies differently across regimes.

## Regime analysis

Portfolio behavior can change across inflationary, deflationary, growth, recession, tightening, easing, crisis, and recovery regimes. Regime labels are analytical tools, not certain forecasts.

## Scenario probability

Scenario probabilities should not be fabricated simply to create a weighted portfolio recommendation. When probability estimates are weak, ranges and conditional analysis may be more appropriate.

## Model risk

Portfolio models can fail due to stale data, changing correlations, estimation error, structural breaks, hidden leverage, liquidity assumptions, benchmark mismatch, or implementation constraints.

## Optimization governance

Optimization outputs should preserve objective function, constraints, inputs, solver state, sensitivity, infeasibility conditions, and comparison with simpler alternatives.

## Human judgment

Qualified human portfolio professionals retain authority over mandate interpretation, allocation decisions, client suitability, fiduciary judgment, exceptions, portfolio approval, and implementation.

## Trade execution boundary

`execute_trade` and `place_or_route_order` are protected. F152 cannot send an order, choose an execution venue, interact with a broker, modify an open order, or execute a transaction.

## Fund movement boundary

`move_or_withdraw_funds` is protected. F152 cannot initiate wires, withdrawals, transfers, collateral movements, or custody instructions.

## Client allocation boundary

`approve_client_allocation` is protected. Passing portfolio analysis does not constitute client approval, suitability approval, or fiduciary authorization.

## Mandate override boundary

`override_mandate_or_compliance_limit` is protected. Constraints cannot be bypassed because an optimizer finds a higher expected return.

## Provenance

`provenance_documentation_gap` blocks release when mandate, holdings, prices, models, assumptions, constraints, risk, allocation, or approval provenance is incomplete.

F152 must never fabricate holdings, mandate terms, prices, benchmark values, client objectives, compliance status, risk limits, portfolio approvals, transaction status, or custody information.

## Memory and state

The `memory/` layer can preserve mandates, holdings snapshots, cash, benchmark versions, market data, allocation proposals, assumptions, risk states, compliance findings, stress scenarios, approvals, and unresolved issues.

It should distinguish live holdings, delayed holdings, proposed holdings, simulated allocations, approved target allocations, and executed positions.

## Observability

The `observability/` layer supports traceability across mandate state, holdings, market-data timestamps, allocation assumptions, risk limits, liquidity, stress tests, compliance checks, approvals, and protected-action attempts.

Useful telemetry includes constraint breaches, stale prices, concentration flags, liquidity gaps, stress losses, model changes, benchmark changes, compliance blockers, approval state, and attempted live actions.

## Required reviews

The executable policy requires all eight conditions:

```text
mandate_reviewed
allocation_reviewed
risk_reviewed
liquidity_reviewed
valuation_market_data_reviewed
compliance_suitability_reviewed
scenario_stress_reviewed
qualified_portfolio_approval
```

Missing any condition fails closed.

## Fail-closed governance

The implemented policy blocks release when:

- mandate, benchmark, objective, eligible universe, concentration, leverage, duration, currency, or restrictions remain unresolved
- allocation, optimization, expected-return, covariance, correlation, factor, or model-risk issues remain unresolved
- market, credit, concentration, factor, drawdown, volatility, duration, liquidity, counterparty, or other risk limits remain unresolved
- liquidity, market-impact, redemption, cash-buffer, settlement, collateral, or capacity issues remain unresolved
- valuation, stale-price, security-identity, corporate-action, FX, benchmark, or market-data issues remain unresolved
- regulatory, fiduciary, suitability, IPS, restricted-list, ESG, tax, conflict, or compliance issues remain unresolved
- stress tests, tail risks, regime shifts, correlation breakdowns, leverage, or scenario coverage remain unresolved
- mandate, holdings, prices, models, assumptions, constraints, risk, allocation, or approval provenance is incomplete
- any required review is missing
- qualified portfolio approval is missing

The system exposes blockers instead of manufacturing suitability, compliance clearance, mandate authority, valuation certainty, execution authority, or client approval.

## Protected actions

The safety policy permanently protects:

```text
execute_trade
place_or_route_order
rebalance_live_portfolio
move_or_withdraw_funds
approve_client_allocation
override_mandate_or_compliance_limit
```

These remain outside autonomous authority even after all required reviews are satisfied.

## Explicit failure states

```text
MANDATE REVIEW REQUIRED
ALLOCATION REVIEW REQUIRED
RISK REVIEW REQUIRED
LIQUIDITY REVIEW REQUIRED
VALUATION AND MARKET DATA REVIEW REQUIRED
COMPLIANCE AND SUITABILITY REVIEW REQUIRED
SCENARIO AND STRESS REVIEW REQUIRED
QUALIFIED PORTFOLIO APPROVAL REQUIRED
MANDATE CONSTRAINT GAP
ALLOCATION MODEL GAP
RISK LIMIT BREACH
LIQUIDITY OR CAPACITY GAP
VALUATION OR MARKET DATA GAP
COMPLIANCE OR SUITABILITY GAP
STRESS OR SCENARIO GAP
PROVENANCE DOCUMENTATION GAP
TRADE EXECUTION PROHIBITED
ORDER PLACEMENT OR ROUTING PROHIBITED
LIVE REBALANCING PROHIBITED
FUND MOVEMENT PROHIBITED
CLIENT ALLOCATION APPROVAL PROHIBITED
MANDATE OR COMPLIANCE OVERRIDE PROHIBITED
```

## End-to-end reference workflow

1. Load and verify mandate, investment-policy statement, objective, benchmark, horizon, liquidity, restrictions, authority, and effective date.
2. Load holdings, cash, benchmark, prices, FX, corporate actions, security identifiers, and data timestamps.
3. Build strategic or tactical allocation options using explicit capital-market and model assumptions.
4. Evaluate diversification, factors, concentration, leverage, duration, currency, credit, liquidity, counterparty, and implementation constraints.
5. Run historical, hypothetical, tail, reverse-stress, and regime scenarios appropriate to the mandate.
6. Review transaction costs, capacity, cash needs, market impact, settlement, collateral, and rebalancing consequences.
7. Check mandate, IPS, suitability, fiduciary, restricted-list, ESG, tax, conflict, and other compliance requirements.
8. Compare proposals against current portfolio, benchmark, target ranges, risk budget, and unresolved constraints.
9. Preserve provenance for holdings, prices, assumptions, models, constraints, risk, stress results, compliance findings, and approvals.
10. Apply fail-closed governance and require qualified portfolio approval.
11. Produce a decision-support package with alternatives, tradeoffs, blockers, uncertainty, and required human actions.
12. Keep execution, order routing, live rebalancing, fund movement, client approval, and mandate overrides outside autonomous authority.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test mandate interpretation, allocation reasoning, model sensitivity, diversification, risk limits, liquidity, stress coverage, market-data quality, compliance, suitability boundaries, provenance, and governance behavior.

The behavioral verification layer includes direct governance tests and a 10-scenario held-out suite covering missing review, approved support release, mandate gaps, allocation-model gaps, risk-limit breaches, liquidity gaps, valuation or market-data gaps, compliance or suitability gaps, stress-scenario gaps, and provenance gaps.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed behavior, held-out governance scenarios, and execution of the governed portfolio-support workflow.

## Reproducibility

Reproducible portfolio analysis requires preserving mandate version, holdings snapshot, cash, benchmark version, price timestamp, FX, corporate actions, capital-market assumptions, covariance inputs, allocation model, risk model, liquidity assumptions, stress scenarios, compliance checks, approvals, and unresolved issues.

## Extension points

Organization-specific implementations can add governed integrations for portfolio accounting, market-data vendors, risk systems, optimization engines, mandate repositories, compliance systems, custodians, performance systems, research platforms, scenario engines, and investment-committee workflows.

Any integration capable of changing live holdings, routing orders, transferring funds, changing mandate records, clearing compliance exceptions, or affecting client accounts should remain behind explicit authorization, least privilege, segregation of duties, audit logging, compliance controls, and human-controlled execution.

## Example applications

Potential governed uses include strategic asset allocation, tactical allocation review, model-portfolio analysis, institutional portfolio review, liquidity analysis, risk-budget review, stress testing, concentration review, manager-allocation analysis, rebalancing support, benchmark analysis, performance attribution, risk attribution, and investment-committee preparation.

F152 is not an autonomous portfolio manager, investment adviser, fiduciary, trader, broker, custodian, compliance officer, trustee, tax adviser, or client-approval authority.

## Design principles

1. Begin with an authoritative mandate, exact holdings state, benchmark, and current market data.
2. Separate policy constraints, assumptions, forecasts, optimization output, and human decisions.
3. Treat expected returns, volatilities, correlations, and factor exposures as uncertain estimates.
4. Evaluate concentration, leverage, liquidity, counterparty, implementation, and tail risk alongside expected return.
5. Never allow an optimizer to override mandate, compliance, suitability, fiduciary, or liquidity constraints.
6. Never fabricate holdings, prices, mandate terms, client circumstances, risk limits, compliance status, approvals, or transaction status.
7. Preserve provenance and reproducibility for portfolio data, models, scenarios, constraints, risk, and approvals.
8. Fail closed when mandate, allocation, risk, liquidity, valuation, market data, compliance, suitability, stress, provenance, or approval is incomplete.
9. Keep client decisions, fiduciary judgment, trade execution, order routing, fund movement, live rebalancing, and constraint overrides under authorized human control.

## Scope statement

F152 demonstrates a governed multi-agent architecture for portfolio-management decision support. It combines specialized mandate, allocation, risk, compliance, and review agents with deterministic mandate, allocation, constraint, stress, and approval tools, observability, held-out evaluation, and fail-closed governance while preserving strict human authority over suitability, fiduciary decisions, compliance exceptions, client allocations, trading, order routing, fund movement, and live portfolio changes.

Author: Mahsa Keikha
