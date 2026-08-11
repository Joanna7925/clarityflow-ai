from flask import Flask

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ClarityFlow AI</title>

<style>
:root{
  --nav:#0b1739;
  --accent:#6f47e8;
  --accent-soft:#f1edff;
  --bg:#f5f7fb;
  --card:#ffffff;
  --text:#172033;
  --muted:#667085;
  --line:#e7eaf0;

  --red:#c62828;
  --red-soft:#fff1f1;

  --orange:#c76a00;
  --orange-soft:#fff7e8;

  --green:#0b7a4b;
  --green-soft:#ecfbf3;

  --blue:#3451b2;
  --blue-soft:#eef3ff;
}

*{
  box-sizing:border-box;
}

body{
  margin:0;
  font-family:Arial,Helvetica,sans-serif;
  background:var(--bg);
  color:var(--text);
}

button,
input,
select,
textarea{
  font:inherit;
}

.sidebar{
  position:fixed;
  left:0;
  top:0;
  bottom:0;
  width:240px;
  background:var(--nav);
  color:white;
  padding:22px 14px;
  z-index:30;
}

.brand{
  padding:0 10px 18px;
  border-bottom:1px solid rgba(255,255,255,.12);
  margin-bottom:16px;
}

.brand-title{
  font-size:24px;
  font-weight:bold;
}

.brand-title span{
  color:#b69fff;
}

.brand-sub{
  color:#aeb9d1;
  font-size:12px;
  margin-top:5px;
}

.nav-label{
  color:#8492b2;
  font-size:10px;
  font-weight:bold;
  letter-spacing:.12em;
  padding:12px 10px 6px;
}

.nav-btn{
  width:100%;
  border:0;
  background:transparent;
  color:#d9e1f2;
  text-align:left;
  padding:11px 12px;
  border-radius:9px;
  margin:3px 0;
  font-weight:bold;
}

.nav-btn.active{
  background:rgba(111,71,232,.25);
  color:white;
  box-shadow:inset 3px 0 0 #ad96ff;
}

.side-score{
  margin:22px 8px 0;
  border:1px solid rgba(255,255,255,.15);
  border-radius:14px;
  padding:14px;
  background:rgba(255,255,255,.04);
}

.score-label{
  color:#aeb9d1;
  font-size:10px;
  font-weight:bold;
}

.score-number{
  font-size:36px;
  font-weight:bold;
  margin-top:4px;
}

.main{
  margin-left:240px;
}

.topbar{
  position:sticky;
  top:0;
  z-index:20;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:12px;
  padding:14px 24px;
  background:white;
  border-bottom:1px solid var(--line);
}

.org{
  display:flex;
  align-items:center;
  gap:12px;
}

.org-icon{
  width:40px;
  height:40px;
  border-radius:10px;
  background:var(--accent-soft);
  color:var(--accent);
  display:grid;
  place-items:center;
  font-weight:bold;
}

.org-name{
  font-weight:bold;
}

.org-meta{
  color:var(--muted);
  font-size:12px;
  margin-top:2px;
}

.top-actions{
  display:flex;
  gap:8px;
  align-items:center;
}

.live{
  background:var(--green-soft);
  color:var(--green);
  padding:7px 10px;
  border-radius:999px;
  font-size:12px;
  font-weight:bold;
}

.btn{
  border:1px solid var(--line);
  background:white;
  color:var(--text);
  padding:9px 12px;
  border-radius:9px;
  font-weight:bold;
}

.btn.primary{
  background:var(--accent);
  color:white;
  border-color:var(--accent);
}

.btn.soft{
  background:var(--accent-soft);
  color:var(--accent);
  border-color:transparent;
}

.mobile-menu{
  display:none;
}

.content{
  padding:24px;
}

.section{
  display:none;
}

.section.active{
  display:block;
}

.page-head{
  display:flex;
  justify-content:space-between;
  gap:15px;
  align-items:flex-start;
  margin-bottom:18px;
}

.page-title{
  font-size:28px;
  font-weight:bold;
}

.page-sub{
  color:var(--muted);
  margin-top:5px;
  font-size:14px;
}

.period{
  color:var(--muted);
  font-size:13px;
}

.card,
.panel{
  background:white;
  border:1px solid var(--line);
  border-radius:14px;
  padding:16px;
}

.metric-label{
  color:var(--muted);
  font-size:11px;
  font-weight:bold;
}

.metric-value{
  font-size:28px;
  font-weight:bold;
  margin-top:9px;
}

.metric-foot{
  color:var(--muted);
  font-size:12px;
  margin-top:5px;
}

.red{
  color:var(--red);
}

.orange{
  color:var(--orange);
}

.green{
  color:var(--green);
}

.blue{
  color:var(--blue);
}

.queue-summary{
  display:grid;
  grid-template-columns:repeat(4,1fr);
  gap:10px;
  margin-bottom:14px;
}

.staff-toolbar{
  display:flex;
  justify-content:space-between;
  gap:12px;
  align-items:center;
  margin-bottom:14px;
}

.staff-toolbar-left{
  display:flex;
  flex-direction:column;
  gap:3px;
}

.filters{
  display:grid;
  grid-template-columns:1.3fr repeat(4,170px);
  gap:8px;
  margin:14px 0;
}

.filters input,
.filters select{
  width:100%;
  border:1px solid var(--line);
  border-radius:9px;
  padding:10px;
  background:white;
}

.worklist{
  display:flex;
  flex-direction:column;
  gap:10px;
}

.work-card{
  background:white;
  border:1px solid var(--line);
  border-radius:12px;
  padding:14px;
  display:grid;
  grid-template-columns:105px 1.35fr 110px 125px 145px 1.2fr 105px;
  gap:12px;
  align-items:center;
}

.priority-pill,
.status-pill{
  display:inline-flex;
  padding:5px 8px;
  border-radius:999px;
  font-size:11px;
  font-weight:bold;
}

.Critical{
  background:var(--red-soft);
  color:var(--red);
}

.High{
  background:var(--orange-soft);
  color:var(--orange);
}

.Medium{
  background:var(--blue-soft);
  color:var(--blue);
}

.Low{
  background:var(--green-soft);
  color:var(--green);
}

.status-open{
  background:#f2f4f7;
  color:#475467;
}

.status-progress{
  background:var(--blue-soft);
  color:var(--blue);
}

.status-waiting{
  background:#f7f0ff;
  color:#7a3fc7;
}

.status-escalated{
  background:var(--orange-soft);
  color:var(--orange);
}

.status-resolved{
  background:var(--green-soft);
  color:var(--green);
}

.work-title{
  font-size:13px;
  font-weight:bold;
}

.work-sub{
  color:var(--muted);
  font-size:12px;
  margin-top:3px;
}

.money{
  font-weight:bold;
}

.owner{
  font-size:12px;
  font-weight:bold;
}

.due{
  font-size:12px;
  color:var(--muted);
}

.next-action{
  color:var(--muted);
  font-size:12px;
}

.ai-action{
  margin-top:4px;
  color:var(--accent);
  font-size:11px;
  font-weight:bold;
}

.callout{
  border:1px solid #ded7ff;
  background:#f7f4ff;
  border-radius:12px;
  padding:14px;
  margin-bottom:14px;
}

.callout strong{
  color:var(--accent);
}

.modal{
  position:fixed;
  inset:0;
  background:rgba(5,12,28,.58);
  display:none;
  align-items:center;
  justify-content:center;
  padding:18px;
  z-index:80;
}

.modal.open{
  display:flex;
}

.modal-card{
  width:min(900px,100%);
  max-height:92vh;
  overflow:auto;
  background:white;
  border-radius:16px;
}

.modal-head{
  display:flex;
  justify-content:space-between;
  align-items:center;
  padding:18px;
  border-bottom:1px solid var(--line);
}

.modal-title{
  font-size:20px;
  font-weight:bold;
}

.modal-body{
  padding:18px;
}

.case-grid{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:16px;
}

.detail-box{
  border:1px solid var(--line);
  border-radius:11px;
  padding:13px;
}

.detail-row{
  display:grid;
  grid-template-columns:125px 1fr;
  gap:8px;
  padding:7px 0;
  border-bottom:1px solid var(--line);
  font-size:13px;
}

.detail-row:last-child{
  border-bottom:0;
}

.detail-label{
  color:var(--muted);
}

.ai-recommendation{
  background:var(--accent-soft);
  border-radius:11px;
  padding:14px;
  margin-top:14px;
}

.ai-recommendation-title{
  color:var(--accent);
  font-weight:bold;
  font-size:13px;
}

.ai-recommendation-text{
  margin-top:5px;
  font-size:13px;
}

.history-item{
  padding:10px 0;
  border-bottom:1px solid var(--line);
}

textarea,
.field{
  width:100%;
  border:1px solid var(--line);
  border-radius:9px;
  padding:10px;
  background:white;
}

@media(max-width:1100px){

  .filters{
    grid-template-columns:1fr 1fr;
  }

  .work-card{
    grid-template-columns:100px 1fr 100px 110px;
  }

  .work-card .owner,
  .work-card .due,
  .work-card .next-action{
    grid-column:auto;
  }
}

@media(max-width:760px){

  .sidebar{
    transform:translateX(-100%);
    transition:.2s;
    width:245px;
  }

  .sidebar.open{
    transform:translateX(0);
  }

  .main{
    margin-left:0;
  }

  .mobile-menu{
    display:inline-block;
  }

  .topbar{
    padding:12px 14px;
  }

  .content{
    padding:15px;
  }

  .org-meta,
  .live{
    display:none;
  }

  .page-head{
    display:block;
  }

  .queue-summary{
    grid-template-columns:1fr 1fr;
  }

  .filters{
    grid-template-columns:1fr;
  }

  .staff-toolbar{
    display:block;
  }

  .work-card{
    grid-template-columns:1fr auto;
  }

  .work-card .money,
  .work-card .owner,
  .work-card .due,
  .work-card .status-cell,
  .work-card .next-action{
    grid-column:1/-1;
  }

  .case-grid{
    grid-template-columns:1fr;
  }
}

</style>
</head>

<body>

<aside class="sidebar" id="sidebar">

<div class="brand">

<div class="brand-title">
ClarityFlow <span>AI</span>™
</div>

<div class="brand-sub">
by Clarity Health Advisors
</div>

</div>

<div class="nav-label">
OVERVIEW
</div>

<button class="nav-btn" data-view="dashboard">
Executive Dashboard
</button>

<button class="nav-btn active" data-view="workspace">
Staff Workspace
</button>

<div class="nav-label">
REVENUE RECOVERY
</div>

<button class="nav-btn" data-view="auth">
Prior Authorization
</button>

<button class="nav-btn" data-view="denials">
Denial Recovery
</button>

<button class="nav-btn" data-view="recovery">
Recovery Performance
</button>

<div class="nav-label">
INTELLIGENCE
</div>

<button class="nav-btn" data-view="ai">
Ask Clarity AI
</button>

<button class="nav-btn" data-view="reports">
Executive Reports
</button>

<div class="side-score">

<div class="score-label">
CLARITY RECOVERY SCORE
</div>

<div class="score-number">
73
</div>

<div class="brand-sub">
Good
</div>

</div>

</aside>
<main class="main">

<div class="topbar">

<div class="org">

<button class="btn mobile-menu" id="menuBtn">
☰
</button>

<div class="org-icon">
CH
</div>

<div>

<div class="org-name">
Clarity Demo Health System
</div>

<div class="org-meta">
Revenue Cycle Operations · Staff Workspace
</div>

</div>

</div>


<div class="top-actions">

<span class="live">
● System Live
</span>

<button class="btn" id="resetBtn">
Reset Demo
</button>

<button class="btn primary" id="exportBtn">
Export Queue
</button>

</div>

</div>


<div class="content">


<section id="workspace" class="section active">

<div class="page-head">

<div>

<div class="page-title">
Staff Work Queue
</div>

<div class="page-sub">
Prioritized daily revenue recovery work with recommended next actions.
</div>

</div>

<div class="period">
Tuesday · August 11, 2026
</div>

</div>


<div class="callout">

<strong>Clarity AI Priority Brief:</strong>
2 critical cases require action today.
Authorization and timely filing represent the most immediate preventable revenue risk.

</div>


<div class="queue-summary">

<div class="card">

<div class="metric-label">
MY OPEN CASES
</div>

<div class="metric-value" id="myOpen">
0
</div>

<div class="metric-foot">
Assigned work
</div>

</div>


<div class="card">

<div class="metric-label">
CRITICAL TODAY
</div>

<div class="metric-value red" id="criticalToday">
0
</div>

<div class="metric-foot">
Immediate action
</div>

</div>


<div class="card">

<div class="metric-label">
REVENUE AT RISK
</div>

<div class="metric-value orange" id="staffRisk">
$0
</div>

<div class="metric-foot">
Open assigned value
</div>

</div>


<div class="card">

<div class="metric-label">
RECOVERED THIS MONTH
</div>

<div class="metric-value green" id="staffRecovered">
$0
</div>

<div class="metric-foot">
Resolved case value
</div>

</div>

</div>


<div class="panel">

<div class="staff-toolbar">

<div class="staff-toolbar-left">

<div class="panel-title">
My Smart Work Queue
</div>

<div class="panel-sub">
Cases are prioritized by deadline, dollar value and operational risk.
</div>

</div>

<button class="btn soft" id="showCriticalBtn">
Show Critical Only
</button>

</div>


<div class="filters">

<input
id="searchBox"
placeholder="Search account or payer">


<select id="filterSeverity">

<option value="">
All priorities
</option>

<option>
Critical
</option>

<option>
High
</option>

<option>
Medium
</option>

<option>
Low
</option>

</select>


<select id="filterCategory">

<option value="">
All issue types
</option>

<option>
Authorization
</option>

<option>
Denial
</option>

<option>
Timely Filing
</option>

<option>
Eligibility
</option>

</select>


<select id="filterOwner">

<option value="">
All owners
</option>

<option>
J. Smith
</option>

<option>
M. Davis
</option>

<option>
R. Patel
</option>

<option>
L. Johnson
</option>

</select>


<select id="filterStatus">

<option value="">
All statuses
</option>

<option>
Open
</option>

<option>
In Progress
</option>

<option>
Waiting on Payer
</option>

<option>
Escalated
</option>

<option>
Resolved
</option>

</select>

</div>


<div class="worklist" id="worklist">
</div>

</div>

</section>


<section id="dashboard" class="section">

<div class="page-head">

<div>

<div class="page-title">
Executive Command Center
</div>

<div class="page-sub">
Financial exposure, recovery performance and operational priorities.
</div>

</div>

<div class="period">
Reporting period: Aug 1–11, 2026
</div>

</div>


<div class="queue-summary">

<div class="card">

<div class="metric-label">
REVENUE AT RISK
</div>

<div class="metric-value red" id="execRisk">
$0
</div>

<div class="metric-foot" id="execOpenCount">
0 open cases
</div>

</div>


<div class="card">

<div class="metric-label">
RECOVERED REVENUE
</div>

<div class="metric-value green" id="execRecovered">
$0
</div>

<div class="metric-foot">
Resolved opportunities
</div>

</div>


<div class="card">

<div class="metric-label">
RECOVERY RATE
</div>

<div class="metric-value blue" id="execRate">
0%
</div>

<div class="metric-foot">
Recovered ÷ identified
</div>

</div>


<div class="card">

<div class="metric-label">
CRITICAL CASES
</div>

<div class="metric-value orange" id="execCritical">
0
</div>

<div class="metric-foot">
Immediate attention
</div>

</div>

</div>


<div class="panel">

<div class="panel-title">
Executive Risk Summary
</div>

<div class="panel-sub">
Open exposure by workflow category
</div>

<div id="execRiskSummary" style="margin-top:14px">
</div>

</div>

</section>


<section id="auth" class="section">

<div class="page-head">

<div>

<div class="page-title">
Prior Authorization Work Center
</div>

<div class="page-sub">
Prevent authorization-related revenue loss before service dates.
</div>

</div>

</div>


<div class="callout">

<strong>Recommended focus:</strong>
work authorization cases with the closest service date and highest expected reimbursement first.

</div>

<div class="worklist" id="authWorklist">
</div>

</section>


<section id="denials" class="section">

<div class="page-head">

<div>

<div class="page-title">
Denial Recovery Center
</div>

<div class="page-sub">
Prioritize appeal opportunities by financial impact and deadline.
</div>

</div>

</div>


<div class="callout">

<strong>Clarity AI:</strong>
high-dollar denials should be grouped by payer and root cause before appeal work is assigned.

</div>

<div class="worklist" id="denialWorklist">
</div>

</section>


<section id="recovery" class="section">

<div class="page-head">

<div>

<div class="page-title">
Recovery Performance
</div>

<div class="page-sub">
Track recovered revenue and remaining opportunity.
</div>

</div>

</div>


<div class="queue-summary">

<div class="card">

<div class="metric-label">
TOTAL IDENTIFIED
</div>

<div class="metric-value" id="identifiedTotal">
$0
</div>

</div>


<div class="card">

<div class="metric-label">
RECOVERED
</div>

<div class="metric-value green" id="recoveredTotal">
$0
</div>

</div>


<div class="card">

<div class="metric-label">
OPEN OPPORTUNITY
</div>

<div class="metric-value orange" id="openOpportunity">
$0
</div>

</div>


<div class="card">

<div class="metric-label">
RESOLVED CASES
</div>

<div class="metric-value blue" id="resolvedCount">
0
</div>

</div>

</div>


<div class="panel">

<div class="panel-title">
Recovery by Workflow
</div>

<div id="recoveryByCategory" style="margin-top:12px">
</div>

</div>

</section>


<section id="ai" class="section">

<div class="page-head">

<div>

<div class="page-title">
Ask Clarity AI
</div>

<div class="page-sub">
Operational intelligence from the current revenue recovery work queue.
</div>

</div>

</div>


<div class="panel">

<div class="panel-title">
Ask an operational question
</div>

<div class="panel-sub">
Try: “What should I work first?” or “Which payer has the most revenue at risk?”
</div>


<div style="display:flex;gap:8px;margin-top:14px">

<input
id="aiQuestion"
placeholder="What should I work first?"
style="
flex:1;
border:1px solid var(--line);
border-radius:9px;
padding:11px;
">

<button
class="btn primary"
id="askBtn">

Ask Clarity

</button>

</div>


<div class="ai-recommendation" id="aiAnswer">

<div class="ai-recommendation-title">
Clarity AI
</div>

<div class="ai-recommendation-text">
Ask a question about the current demo work queue.
</div>

</div>

</div>

</section>


<section id="reports" class="section">

<div class="page-head">

<div>

<div class="page-title">
Executive Reports
</div>

<div class="page-sub">
Leadership-ready revenue recovery summary.
</div>

</div>

</div>


<div class="panel">

<div class="panel-title">
Leadership Summary
</div>

<div id="reportSummary" style="margin-top:12px">
</div>

</div>

</section>


</div>

</main>


<div class="modal" id="caseModal">

<div class="modal-card">

<div class="modal-head">

<div>

<div class="modal-title" id="caseTitle">
Case Workspace
</div>

<div class="panel-sub">
Operational case management and recovery documentation
</div>

</div>


<button
class="btn"
id="closeCaseBtn">

Close

</button>

</div>


<div class="modal-body">


<div class="case-grid">


<div class="detail-box">

<div class="detail-row">

<div class="detail-label">
Account
</div>

<div id="caseAccount">
</div>

</div>


<div class="detail-row">

<div class="detail-label">
Payer
</div>

<div id="casePayer">
</div>

</div>


<div class="detail-row">

<div class="detail-label">
Issue
</div>

<div id="caseIssue">
</div>

</div>


<div class="detail-row">

<div class="detail-label">
Priority
</div>

<div id="casePriority">
</div>

</div>


<div class="detail-row">

<div class="detail-label">
Revenue at Risk
</div>

<div id="caseRisk">
</div>

</div>


<div class="detail-row">

<div class="detail-label">
Owner
</div>

<div id="caseOwner">
</div>

</div>


<div class="detail-row">

<div class="detail-label">
Due Date
</div>

<div id="caseDue">
</div>

</div>


<div class="detail-row">

<div class="detail-label">
Why Flagged
</div>

<div id="caseReason">
</div>

</div>

</div>


<div class="detail-box">

<label class="metric-label">
ASSIGNED TO
</label>

<select
id="caseOwnerSelect"
class="field"
style="margin-top:6px">

<option>
J. Smith
</option>

<option>
M. Davis
</option>

<option>
R. Patel
</option>

<option>
L. Johnson
</option>

</select>


<label
class="metric-label"
style="display:block;margin-top:14px">

STATUS

</label>

<select
id="caseStatus"
class="field"
style="margin-top:6px">

<option>
Open
</option>

<option>
In Progress
</option>

<option>
Waiting on Payer
</option>

<option>
Escalated
</option>

<option>
Resolved
</option>

</select>


<label
class="metric-label"
style="display:block;margin-top:14px">

CASE NOTE

</label>

<textarea
id="caseNote"
rows="5"
placeholder="Document payer call, missing information, appeal work, handoff or resolution."
style="margin-top:6px">
</textarea>


<button
class="btn primary"
id="saveCaseBtn"
style="margin-top:12px">

Save Case Update

</button>

</div>

</div>


<div class="ai-recommendation">

<div class="ai-recommendation-title">
✦ AI Recommended Next Action
</div>

<div
class="ai-recommendation-text"
id="caseAIAction">

</div>

</div>


<div class="panel"
style="margin-top:14px">

<div class="panel-title">
Case History
</div>

<div
id="caseHistory"
style="margin-top:10px">

</div>

</div>


</div>

</div>

</div>

<script>

const money = n =>
new Intl.NumberFormat(
'en-US',
{
style:'currency',
currency:'USD',
maximumFractionDigits:0
}
).format(n || 0);


const seedCases = [

{
account:'A1001',
payer:'BCBS',
category:'Authorization',
issue:'Authorization missing',
risk:12850,
days:3,
owner:'J. Smith',
due:'Aug 14, 2026',
status:'Open',
reason:'Required authorization is incomplete before the scheduled MRI.',
action:'Verify authorization status today and obtain missing payer documentation.',
ai:'Contact BCBS today. Confirm the authorization request is active, identify any missing clinical documentation, and escalate if approval cannot be obtained before the service date.'
},

{
account:'A1002',
payer:'Aetna',
category:'Timely Filing',
issue:'Timely filing deadline',
risk:6750,
days:1,
owner:'M. Davis',
due:'Aug 12, 2026',
status:'Open',
reason:'Claim filing deadline is tomorrow.',
action:'Submit claim immediately and document confirmation.',
ai:'Treat this as the highest deadline risk. Submit the claim today, retain submission confirmation, and document any payer portal response.'
},

{
account:'A1003',
payer:'United Healthcare',
category:'Denial',
issue:'Medical necessity denial',
risk:4900,
days:31,
owner:'R. Patel',
due:'Sep 11, 2026',
status:'In Progress',
reason:'Denied claim requires documentation review and appeal decision.',
action:'Review denial reason and prepare appeal if supported.',
ai:'Compare the denial rationale with the medical record. If documentation supports medical necessity, prepare an appeal with the clinical evidence and payer policy reference.'
},

{
account:'A1004',
payer:'BCBS',
category:'Authorization',
issue:'Authorization expires before service',
risk:4300,
days:5,
owner:'J. Smith',
due:'Aug 16, 2026',
status:'In Progress',
reason:'Authorization expiration precedes scheduled service date.',
action:'Request authorization extension before service.',
ai:'Contact BCBS and request an extension or revised authorization that covers the scheduled service date.'
},

{
account:'A1005',
payer:'Cigna',
category:'Eligibility',
issue:'Eligibility not verified',
risk:2100,
days:17,
owner:'L. Johnson',
due:'Aug 28, 2026',
status:'Open',
reason:'Coverage verification is incomplete before service.',
action:'Re-verify coverage and reconcile registration data.',
ai:'Re-run eligibility verification and compare the payer response with the registration record. Correct demographic or coverage discrepancies before billing.'
},

{
account:'A1006',
payer:'Humana',
category:'Authorization',
issue:'Authorization pending',
risk:8200,
days:10,
owner:'J. Smith',
due:'Aug 21, 2026',
status:'Waiting on Payer',
reason:'Authorization remains pending close to service date.',
action:'Contact payer for status and escalate if documentation is outstanding.',
ai:'Confirm Humana received the clinical documentation. If the case is pending medical review, document the expected determination date and escalate if it approaches the service date.'
},

{
account:'A1007',
payer:'BCBS',
category:'Denial',
issue:'Denied claim – appeal recommended',
risk:9700,
days:22,
owner:'R. Patel',
due:'Sep 2, 2026',
status:'Escalated',
reason:'High-dollar denial with appeal opportunity.',
action:'Escalate to denial specialist and prepare appeal package.',
ai:'Prioritize this high-value denial for appeal. Validate the denial code, gather supporting documentation, and assign the completed appeal package to the denial specialist.'
},

{
account:'A1008',
payer:'Aetna',
category:'Authorization',
issue:'Authorization pending',
risk:3600,
days:6,
owner:'M. Davis',
due:'Aug 17, 2026',
status:'Open',
reason:'Authorization remains pending close to service date.',
action:'Follow up with payer and confirm records were received.',
ai:'Contact Aetna to confirm receipt of the authorization request and supporting records. Document the payer reference number and expected response date.'
},

{
account:'A1009',
payer:'United Healthcare',
category:'Eligibility',
issue:'Coverage discrepancy',
risk:5600,
days:8,
owner:'L. Johnson',
due:'Aug 19, 2026',
status:'Open',
reason:'Eligibility response conflicts with registration data.',
action:'Resolve coverage discrepancy before billing.',
ai:'Validate the member ID, plan effective dates, and coordination of benefits. Correct the registration record before the claim is created.'
},

{
account:'A1010',
payer:'BCBS',
category:'Denial',
issue:'Documentation denial',
risk:7400,
days:18,
owner:'R. Patel',
due:'Aug 29, 2026',
status:'Resolved',
reason:'Additional documentation was required.',
action:'Completed.',
ai:'No additional action is required. Preserve the resolution details as a reference for similar documentation denials.'
}

];


let cases =
JSON.parse(
localStorage.getItem('clarityflow_v13_cases') || 'null'
)
||
JSON.parse(
JSON.stringify(seedCases)
);


let histories =
JSON.parse(
localStorage.getItem('clarityflow_v13_history') || '{}'
);


let currentAccount = null;


function priority(c){

if(c.days <= 2 || c.risk >= 10000)
return 'Critical';

if(c.days <= 8 || c.risk >= 5000)
return 'High';

if(c.days <= 14)
return 'Medium';

return 'Low';

}


function persist(){

localStorage.setItem(
'clarityflow_v13_cases',
JSON.stringify(cases)
);

localStorage.setItem(
'clarityflow_v13_history',
JSON.stringify(histories)
);

}


function metrics(){

cases.forEach(
c => c.severity = priority(c)
);

const open =
cases.filter(
c => c.status !== 'Resolved'
);

const recovered =
cases
.filter(
c => c.status === 'Resolved'
)
.reduce(
(sum,c) => sum + c.risk,
0
);

const identified =
cases.reduce(
(sum,c) => sum + c.risk,
0
);

const openRisk =
open.reduce(
(sum,c) => sum + c.risk,
0
);

return {
open,
recovered,
identified,
openRisk,
rate:
identified
?
Math.round(
recovered / identified * 100
)
:
0
};

}


function statusClass(status){

if(status === 'Resolved')
return 'status-resolved';

if(status === 'Escalated')
return 'status-escalated';

if(status === 'Waiting on Payer')
return 'status-waiting';

if(status === 'In Progress')
return 'status-progress';

return 'status-open';

}


function categoryTotal(category){

return metrics()
.open
.filter(
c => c.category === category
)
.reduce(
(sum,c) => sum + c.risk,
0
);

}


function payerExposure(){

const map = {};

metrics()
.open
.forEach(
c => {

map[c.payer] =
(map[c.payer] || 0)
+
c.risk;

}
);

return Object.entries(map)
.sort(
(a,b) => b[1] - a[1]
);

}


function renderStaffSummary(){

const m = metrics();

document.getElementById('myOpen')
.textContent =
m.open.length;


document.getElementById('criticalToday')
.textContent =
m.open.filter(
c => c.severity === 'Critical'
).length;


document.getElementById('staffRisk')
.textContent =
money(m.openRisk);


document.getElementById('staffRecovered')
.textContent =
money(m.recovered);

}


function workCards(list){

if(!list.length){

return `
<div class="panel-sub">
No cases match the selected filters.
</div>
`;

}


return list.map(
c => `

<div class="work-card">

<div>

<span class="priority-pill ${c.severity}">
${c.severity}
</span>

</div>


<div>

<div class="work-title">
${c.account} · ${c.payer}
</div>

<div class="work-sub">
${c.issue}
</div>

</div>


<div class="money">
${money(c.risk)}
</div>


<div class="status-cell">

<span class="status-pill ${statusClass(c.status)}">
${c.status}
</span>

</div>


<div>

<div class="owner">
${c.owner}
</div>

<div class="due">
Due ${c.due}
</div>

</div>


<div class="next-action">

${c.action}

<div class="ai-action">
✦ AI guidance available
</div>

</div>


<button
class="btn primary open-case"
data-account="${c.account}">

Open Case

</button>

</div>

`
).join('');

}


function renderWorkspace(){

renderStaffSummary();


const severity =
document.getElementById('filterSeverity')
.value;


const category =
document.getElementById('filterCategory')
.value;


const owner =
document.getElementById('filterOwner')
.value;


const status =
document.getElementById('filterStatus')
.value;


const query =
document.getElementById('searchBox')
.value
.toLowerCase();


let list =
cases.filter(
c =>

(!severity || c.severity === severity)

&&

(!category || c.category === category)

&&

(!owner || c.owner === owner)

&&

(!status || c.status === status)

&&

(
!query
||
c.account.toLowerCase().includes(query)
||
c.payer.toLowerCase().includes(query)
||
c.issue.toLowerCase().includes(query)
)

);


list =
list.sort(
(a,b) =>

(
{
Critical:0,
High:1,
Medium:2,
Low:3
}[a.severity]
-
{
Critical:0,
High:1,
Medium:2,
Low:3
}[b.severity]
)

||

a.days - b.days

||

b.risk - a.risk

);


document.getElementById('worklist')
.innerHTML =
workCards(list);


wireCaseButtons();

}


function renderExecutive(){

const m = metrics();

document.getElementById('execRisk')
.textContent =
money(m.openRisk);


document.getElementById('execOpenCount')
.textContent =
m.open.length
+
' open cases';


document.getElementById('execRecovered')
.textContent =
money(m.recovered);


document.getElementById('execRate')
.textContent =
m.rate + '%';


document.getElementById('execCritical')
.textContent =
m.open.filter(
c => c.severity === 'Critical'
).length;


document.getElementById('execRiskSummary')
.innerHTML =

[
'Authorization',
'Denial',
'Timely Filing',
'Eligibility'
]
.map(
category => `

<div class="detail-row">

<div class="detail-label">
${category}
</div>

<div>
<strong>
${money(categoryTotal(category))}
</strong>
</div>

</div>

`
)
.join('');

}


function renderRecovery(){

const m = metrics();

document.getElementById('identifiedTotal')
.textContent =
money(m.identified);


document.getElementById('recoveredTotal')
.textContent =
money(m.recovered);


document.getElementById('openOpportunity')
.textContent =
money(m.openRisk);


document.getElementById('resolvedCount')
.textContent =
cases.filter(
c => c.status === 'Resolved'
).length;


document.getElementById('recoveryByCategory')
.innerHTML =

[
'Authorization',
'Denial',
'Timely Filing',
'Eligibility'
]
.map(
category => `

<div class="detail-row">

<div class="detail-label">
${category}
</div>

<div>
<strong>
${money(categoryTotal(category))}
</strong>
open exposure
</div>

</div>

`
)
.join('');

}


function renderSpecialty(){

document.getElementById('authWorklist')
.innerHTML =
workCards(
cases
.filter(
c => c.category === 'Authorization'
)
.sort(
(a,b) => a.days - b.days
)
);


document.getElementById('denialWorklist')
.innerHTML =
workCards(
cases
.filter(
c => c.category === 'Denial'
)
.sort(
(a,b) => b.risk - a.risk
)
);


wireCaseButtons();

}


function renderReports(){

const m = metrics();

const topPayer =
payerExposure()[0];


const topCategory =
[
'Authorization',
'Denial',
'Timely Filing',
'Eligibility'
]
.map(
category => [
category,
categoryTotal(category)
]
)
.sort(
(a,b) => b[1] - a[1]
)[0];


document.getElementById('reportSummary')
.innerHTML = `

<div class="detail-row">

<div class="detail-label">
Revenue identified
</div>

<div>
<strong>
${money(m.identified)}
</strong>
</div>

</div>


<div class="detail-row">

<div class="detail-label">
Revenue recovered
</div>

<div>
<strong class="green">
${money(m.recovered)}
</strong>
</div>

</div>


<div class="detail-row">

<div class="detail-label">
Open opportunity
</div>

<div>
<strong class="orange">
${money(m.openRisk)}
</strong>
</div>

</div>


<div class="detail-row">

<div class="detail-label">
Recovery rate
</div>

<div>
<strong>
${m.rate}%
</strong>
</div>

</div>


<div class="detail-row">

<div class="detail-label">
Largest workflow risk
</div>

<div>
<strong>
${topCategory[0]}
</strong>
·
${money(topCategory[1])}
</div>

</div>


<div class="detail-row">

<div class="detail-label">
Highest payer exposure
</div>

<div>
<strong>
${topPayer ? topPayer[0] : '—'}
</strong>

${topPayer ? ' · ' + money(topPayer[1]) : ''}

</div>

</div>

`;

}


function renderAll(){

cases.forEach(
c => c.severity = priority(c)
);

renderWorkspace();

renderExecutive();

renderRecovery();

renderSpecialty();

renderReports();

persist();

wireCaseButtons();

}


function wireCaseButtons(){

document.querySelectorAll('.open-case')
.forEach(
button => {

button.onclick =
() => openCase(
button.dataset.account
);

}
);

}


function openCase(account){

currentAccount = account;


const c =
cases.find(
item => item.account === account
);


if(!c)
return;


document.getElementById('caseTitle')
.textContent =
'Case ' + c.account;


document.getElementById('caseAccount')
.textContent =
c.account;


document.getElementById('casePayer')
.textContent =
c.payer;


document.getElementById('caseIssue')
.textContent =
c.issue;


document.getElementById('casePriority')
.textContent =
c.severity;


document.getElementById('caseRisk')
.textContent =
money(c.risk);


document.getElementById('caseOwner')
.textContent =
c.owner;


document.getElementById('caseDue')
.textContent =
c.due;


document.getElementById('caseReason')
.textContent =
c.reason;


document.getElementById('caseAIAction')
.textContent =
c.ai;


document.getElementById('caseOwnerSelect')
.value =
c.owner;


document.getElementById('caseStatus')
.value =
c.status;


document.getElementById('caseNote')
.value = '';


renderHistory();


document.getElementById('caseModal')
.classList.add('open');

}


function renderHistory(){

const history =
histories[currentAccount]
||
[];


document.getElementById('caseHistory')
.innerHTML =

history.length

?

history
.slice()
.reverse()
.map(
item => `

<div class="history-item">

<div class="work-title">
${item.status}
</div>

<div class="work-sub">
Owner: ${item.owner}
</div>

<div class="work-sub">
${item.note}
</div>

<div class="work-sub">
${item.time}
</div>

</div>

`
)
.join('')

:

`

<div class="panel-sub">
No case history yet.
</div>

`;

}


function saveCase(){

const c =
cases.find(
item => item.account === currentAccount
);


if(!c)
return;


c.owner =
document.getElementById('caseOwnerSelect')
.value;


c.status =
document.getElementById('caseStatus')
.value;


const note =
document.getElementById('caseNote')
.value
.trim();


histories[currentAccount] =
histories[currentAccount]
||
[];


histories[currentAccount]
.push(
{

owner:c.owner,

status:c.status,

note:
note
||
'Case assignment or status updated.',

time:
new Date()
.toLocaleString()

}
);


document.getElementById('caseNote')
.value = '';


renderAll();

renderHistory();


document.getElementById('caseOwner')
.textContent =
c.owner;

}


function askClarity(){

const q =
document.getElementById('aiQuestion')
.value
.toLowerCase();


const m =
metrics();


let response = '';


if(
q.includes('first')
||
q.includes('priority')
){

const c =
[...m.open]
.sort(
(a,b) =>

(
{
Critical:0,
High:1,
Medium:2,
Low:3
}[a.severity]
-
{
Critical:0,
High:1,
Medium:2,
Low:3
}[b.severity]
)

||

a.days - b.days

||

b.risk - a.risk

)[0];


response =

`

Work ${c.account} first.

${c.issue}

Revenue at risk:
${money(c.risk)}

Due:
${c.due}

Recommended action:
${c.action}

`;

}


else if(
q.includes('payer')
){

const top =
payerExposure()[0];


response =

top

?

`

${top[0]} currently has the highest open payer exposure at ${money(top[1])}.

`

:

'There is no open payer exposure.';

}


else if(
q.includes('denial')
){

const denials =
m.open.filter(
c => c.category === 'Denial'
);


response =

`

There are ${denials.length} open denial cases representing ${money(
denials.reduce(
(sum,c) => sum + c.risk,
0
)
)} in revenue exposure.

`;

}


else if(
q.includes('authorization')
||
q.includes('auth')
){

const auth =
m.open.filter(
c => c.category === 'Authorization'
);


response =

`

Authorization-related risk totals ${money(
auth.reduce(
(sum,c) => sum + c.risk,
0
)
)} across ${auth.length} open cases.

`;

}


else if(
q.includes('recover')
){

response =

`

${money(m.recovered)} has been recovered.

${money(m.openRisk)} remains open.

Current recovery rate is ${m.rate}%.

`;

}


else{

response =

`

There are ${m.open.length} open cases representing ${money(m.openRisk)} in revenue at risk.

Use the Staff Work Queue to prioritize cases by deadline, value and workflow risk.

`;

}


document.getElementById('aiAnswer')
.innerHTML =

`

<div class="ai-recommendation-title">
Clarity AI
</div>

<div class="ai-recommendation-text">
${response}
</div>

`;

}


function showView(id){

document.querySelectorAll('.section')
.forEach(
section => {

section.classList.toggle(
'active',
section.id === id
);

}
);


document.querySelectorAll('.nav-btn')
.forEach(
button => {

button.classList.toggle(
'active',
button.dataset.view === id
);

}
);


document.getElementById('sidebar')
.classList.remove('open');

}


function exportQueue(){

const headers = [

'priority',
'account',
'payer',
'issue',
'category',
'revenue_at_risk',
'owner',
'due_date',
'status',
'recommended_action'

];


const lines =
[
headers.join(',')
];


cases.forEach(
c => {

lines.push(

[
c.severity,
c.account,
c.payer,
c.issue,
c.category,
c.risk,
c.owner,
c.due,
c.status,
c.action
]
.map(
value =>
`"${String(value).replaceAll('"','""')}"`
)
.join(',')

);

}
);


const blob =
new Blob(
[
lines.join('\n')
],
{
type:'text/csv'
}
);


const link =
document.createElement('a');


link.href =
URL.createObjectURL(blob);


link.download =
'clarityflow_staff_work_queue.csv';


link.click();

}


function resetDemo(){

if(
confirm(
'Reset all ClarityFlow demo cases and case history?'
)
){

cases =
JSON.parse(
JSON.stringify(seedCases)
);


histories = {};


renderAll();

}

}


document.querySelectorAll('.nav-btn')
.forEach(
button => {

button.addEventListener(
'click',
() =>
showView(
button.dataset.view
)
);

}
);


document.getElementById('menuBtn')
.addEventListener(
'click',
() => {

document.getElementById('sidebar')
.classList.toggle('open');

}
);


document.getElementById('closeCaseBtn')
.addEventListener(
'click',
() => {

document.getElementById('caseModal')
.classList.remove('open');

}
);


document.getElementById('saveCaseBtn')
.addEventListener(
'click',
saveCase
);


document.getElementById('askBtn')
.addEventListener(
'click',
askClarity
);


document.getElementById('aiQuestion')
.addEventListener(
'keydown',
event => {

if(event.key === 'Enter')
askClarity();

}
);


document.getElementById('resetBtn')
.addEventListener(
'click',
resetDemo
);


document.getElementById('exportBtn')
.addEventListener(
'click',
exportQueue
);


document.getElementById('showCriticalBtn')
.addEventListener(
'click',
() => {

document.getElementById('filterSeverity')
.value =
'Critical';

renderWorkspace();

}
);


[
'searchBox',
'filterSeverity',
'filterCategory',
'filterOwner',
'filterStatus'
]
.forEach(
id => {

document.getElementById(id)
.addEventListener(
id === 'searchBox'
?
'input'
:
'change',
renderWorkspace
);

}
);


renderAll();

</script>

</body>

</html>

"""

@app.route("/")
def home():
    return HTML

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
