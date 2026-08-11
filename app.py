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

* { box-sizing:border-box; }

body{
  margin:0;
  font-family:Arial,Helvetica,sans-serif;
  background:var(--bg);
  color:var(--text);
}

button,input,select,textarea{
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

.kpis{
  display:grid;
  grid-template-columns:repeat(4,1fr);
  gap:12px;
}

.card,
.panel{
  background:white;
  border:1px solid var(--line);
  border-radius:14px;
  padding:16px;
}

.metric-top{
  display:flex;
  justify-content:space-between;
  align-items:center;
}

.metric-label{
  color:var(--muted);
  font-size:11px;
  font-weight:bold;
}

.metric-icon{
  width:34px;
  height:34px;
  border-radius:10px;
  display:grid;
  place-items:center;
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

.red{ color:var(--red); }
.orange{ color:var(--orange); }
.green{ color:var(--green); }
.blue{ color:var(--blue); }

.red-bg{ background:var(--red-soft); color:var(--red); }
.orange-bg{ background:var(--orange-soft); color:var(--orange); }
.green-bg{ background:var(--green-soft); color:var(--green); }
.blue-bg{ background:var(--blue-soft); color:var(--blue); }

.dashboard-grid{
  display:grid;
  grid-template-columns:1.35fr .85fr;
  gap:14px;
  margin-top:14px;
}

.bottom-grid{
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:14px;
  margin-top:14px;
}

.panel-title{
  font-weight:bold;
}

.panel-sub{
  color:var(--muted);
  font-size:12px;
  margin-top:3px;
}

.panel-head{
  display:flex;
  justify-content:space-between;
  align-items:center;
  margin-bottom:14px;
}

.risk-row{
  display:grid;
  grid-template-columns:150px 1fr 110px;
  gap:12px;
  align-items:center;
  margin:14px 0;
}

.risk-name{
  font-size:13px;
  font-weight:bold;
}

.track{
  height:10px;
  background:#eef1f6;
  border-radius:999px;
  overflow:hidden;
}

.fill{
  height:100%;
  background:var(--accent);
}

.risk-value{
  font-size:12px;
  color:var(--muted);
  text-align:right;
}

.priority-item{
  display:grid;
  grid-template-columns:auto 1fr auto;
  gap:10px;
  padding:11px;
  border:1px solid var(--line);
  border-radius:11px;
  margin-bottom:9px;
}

.priority-dot{
  width:9px;
  height:9px;
  border-radius:50%;
  margin-top:5px;
}

.priority-title{
  font-size:13px;
  font-weight:bold;
}

.priority-sub{
  color:var(--muted);
  font-size:12px;
  margin-top:3px;
}

.priority-money{
  font-weight:bold;
  font-size:13px;
}

.mini-btn{
  border:0;
  background:var(--accent-soft);
  color:var(--accent);
  border-radius:8px;
  padding:7px 9px;
  font-size:12px;
  font-weight:bold;
  margin-top:6px;
}

.info-row{
  display:grid;
  grid-template-columns:1fr auto;
  gap:10px;
  padding:9px 0;
  border-bottom:1px solid var(--line);
}

.info-row:last-child{
  border-bottom:0;
}

.info-label{
  font-size:12px;
  color:var(--muted);
}

.info-value{
  font-size:13px;
  font-weight:bold;
}

.queue-summary{
  display:grid;
  grid-template-columns:repeat(4,1fr);
  gap:10px;
  margin-bottom:12px;
}

.filters{
  display:grid;
  grid-template-columns:1.2fr repeat(3,180px);
  gap:8px;
  margin:14px 0;
}

.filters input,
.filters select,
textarea,
.field{
  width:100%;
  border:1px solid var(--line);
  border-radius:9px;
  padding:10px;
  background:white;
}

.worklist{
  display:flex;
  flex-direction:column;
  gap:9px;
}

.work-card{
  background:white;
  border:1px solid var(--line);
  border-radius:12px;
  padding:13px;
  display:grid;
  grid-template-columns:110px 1.4fr 110px 120px 1fr 100px;
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

.work-sub,
.next-action{
  font-size:12px;
  color:var(--muted);
  margin-top:3px;
}

.money{
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

.roi-grid{
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:12px;
}

.ai-grid{
  display:grid;
  grid-template-columns:1fr .8fr;
  gap:14px;
}

.ask-box{
  display:flex;
  gap:8px;
  margin-top:12px;
}

.ask-box input{
  flex:1;
  border:1px solid var(--line);
  border-radius:9px;
  padding:11px;
}

.answer{
  background:var(--accent-soft);
  border-radius:10px;
  padding:13px;
  margin-top:12px;
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
  width:min(860px,100%);
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

.history-item{
  padding:10px 0;
  border-bottom:1px solid var(--line);
}

@media(max-width:1100px){

  .kpis{
    grid-template-columns:repeat(2,1fr);
  }

  .dashboard-grid,
  .bottom-grid,
  .ai-grid{
    grid-template-columns:1fr;
  }

  .filters{
    grid-template-columns:1fr 1fr;
  }

  .work-card{
    grid-template-columns:100px 1fr 100px 100px;
  }

  .next-action{
    grid-column:1/-1;
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

  .period{
    margin-top:8px;
  }

  .kpis{
    grid-template-columns:1fr 1fr;
  }

  .metric-value{
    font-size:24px;
  }

  .filters{
    grid-template-columns:1fr;
  }

  .queue-summary{
    grid-template-columns:1fr 1fr;
  }

  .work-card{
    grid-template-columns:1fr auto;
  }

  .work-card .money,
  .work-card .status-cell,
  .work-card .next-action{
    grid-column:1/-1;
  }

  .case-grid{
    grid-template-columns:1fr;
  }

  .roi-grid{
    grid-template-columns:1fr;
  }

  .risk-row{
    grid-template-columns:105px 1fr 85px;
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

<div class="nav-label">OVERVIEW</div>

<button class="nav-btn active" data-view="dashboard">
Executive Dashboard
</button>

<button class="nav-btn" data-view="workspace">
Staff Workspace
</button>

<div class="nav-label">REVENUE RECOVERY</div>

<button class="nav-btn" data-view="auth">
Prior Authorization
</button>

<button class="nav-btn" data-view="denials">
Denial Recovery
</button>

<button class="nav-btn" data-view="recovery">
Recovery Performance
</button>

<div class="nav-label">INTELLIGENCE</div>

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

<div class="score-number" id="sideScore">
73
</div>

<div class="brand-sub" id="sideScoreLabel">
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
Revenue Cycle Operations · Orlando Region
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


<section id="dashboard" class="section active">

<div class="page-head">

<div>

<div class="page-title">
Executive Command Center
</div>

<div class="page-sub">
Financial risk, recovery performance and operational priorities in one view.
</div>

</div>

<div class="period">
Reporting period: <strong>Aug 1–10, 2026</strong>
</div>

</div>


<div class="kpis">

<div class="card">

<div class="metric-top">

<div class="metric-label">
REVENUE AT RISK
</div>

<div class="metric-icon red-bg">
$
</div>

</div>

<div class="metric-value red" id="riskTotal">
$0
</div>

<div class="metric-foot" id="riskCount">
0 open cases
</div>

</div>


<div class="card">

<div class="metric-top">

<div class="metric-label">
RECOVERED REVENUE
</div>

<div class="metric-icon green-bg">
✓
</div>

</div>

<div class="metric-value green" id="recoveredTotal">
$0
</div>

<div class="metric-foot" id="recoveredCount">
0 resolved cases
</div>

</div>


<div class="card">

<div class="metric-top">

<div class="metric-label">
RECOVERY RATE
</div>

<div class="metric-icon blue-bg">
%
</div>

</div>

<div class="metric-value blue" id="recoveryRate">
0%
</div>

<div class="metric-foot">
Recovered ÷ total identified
</div>

</div>


<div class="card">

<div class="metric-top">

<div class="metric-label">
CRITICAL CASES
</div>

<div class="metric-icon orange-bg">
!
</div>

</div>

<div class="metric-value orange" id="criticalCount">
0
</div>

<div class="metric-foot">
Require immediate action
</div>

</div>

</div>


<div class="dashboard-grid">

<div class="panel">

<div class="panel-head">

<div>

<div class="panel-title">
Revenue Leak Analysis
</div>

<div class="panel-sub">
Open financial exposure by workflow category
</div>

</div>

<div class="panel-sub" id="openExposureLabel">
$0 open
</div>

</div>

<div id="riskDrivers"></div>

</div>


<div class="panel">

<div class="panel-title">
Today's Priorities
</div>

<div class="panel-sub">
Highest-value cases needing attention
</div>

<div id="priorityList" style="margin-top:14px"></div>

</div>

</div>


<div class="bottom-grid">

<div class="panel">

<div class="panel-title">
Payer Exposure
</div>

<div class="panel-sub">
Open risk by payer
</div>

<div id="payerExposure" style="margin-top:10px"></div>

</div>


<div class="panel">

<div class="panel-title">
Operational Health
</div>

<div class="panel-sub">
Work queue distribution
</div>

<div id="operationalHealth" style="margin-top:10px"></div>

</div>


<div class="panel">

<div class="panel-title">
Recovery Snapshot
</div>

<div class="panel-sub">
Executive ROI summary
</div>

<div id="recoverySnapshot" style="margin-top:10px"></div>

</div>

</div>

</section>


<section id="workspace" class="section">

<div class="page-head">

<div>

<div class="page-title">
Staff Workspace
</div>

<div class="page-sub">
Prioritized daily worklist with clear next actions.
</div>

</div>

</div>


<div class="queue-summary">

<div class="panel">
<div class="metric-label">OPEN</div>
<div class="metric-value" id="wsOpen">0</div>
</div>

<div class="panel">
<div class="metric-label">IN PROGRESS</div>
<div class="metric-value blue" id="wsProgress">0</div>
</div>

<div class="panel">
<div class="metric-label">ESCALATED</div>
<div class="metric-value orange" id="wsEscalated">0</div>
</div>

<div class="panel">
<div class="metric-label">RESOLVED</div>
<div class="metric-value green" id="wsResolved">0</div>
</div>

</div>


<div class="panel">

<div class="panel-title">
Smart Work Queue
</div>

<div class="panel-sub">
Sorted by urgency, financial impact and time remaining.
</div>


<div class="filters">

<input
id="searchBox"
placeholder="Search account or payer">

<select id="filterSeverity">

<option value="">
All priorities
</option>

<option>Critical</option>
<option>High</option>
<option>Medium</option>
<option>Low</option>

</select>


<select id="filterCategory">

<option value="">
All categories
</option>

<option>Authorization</option>
<option>Denial</option>
<option>Timely Filing</option>
<option>Eligibility</option>

</select>


<select id="filterStatus">

<option value="">
All statuses
</option>

<option>Open</option>
<option>In Progress</option>
<option>Escalated</option>
<option>Resolved</option>

</select>

</div>

<div class="worklist" id="worklist"></div>

</div>

</section>


<section id="auth" class="section">

<div class="page-head">

<div>

<div class="page-title">
Prior Authorization Command Center
</div>

<div class="page-sub">
Track high-risk authorization cases before service dates are missed.
</div>

</div>

</div>

<div class="callout">

<strong>Focus:</strong>
prioritize authorizations tied to upcoming service dates and high expected reimbursement.

</div>

<div class="worklist" id="authWorklist"></div>

</section>


<section id="denials" class="section">

<div class="page-head">

<div>

<div class="page-title">
Denial Recovery Center
</div>

<div class="page-sub">
Prioritize denial recovery opportunities by value and urgency.
</div>

</div>

</div>

<div class="callout">

<strong>Recovery strategy:</strong>
work high-dollar denials first, then group by root cause and payer pattern.

</div>

<div class="worklist" id="denialWorklist"></div>

</section>


<section id="recovery" class="section">

<div class="page-head">

<div>

<div class="page-title">
Recovery Performance
</div>

<div class="page-sub">
Track identified opportunity, recovered revenue and open work.
</div>

</div>

</div>


<div class="roi-grid">

<div class="card">

<div class="metric-label">
IDENTIFIED
</div>

<div class="metric-value" id="recIdentified">
$0
</div>

</div>


<div class="card">

<div class="metric-label">
RECOVERED
</div>

<div class="metric-value green" id="recRecovered">
$0
</div>

</div>


<div class="card">

<div class="metric-label">
OPEN OPPORTUNITY
</div>

<div class="metric-value orange" id="recOpen">
$0
</div>

</div>

</div>


<div class="dashboard-grid">

<div class="panel">

<div class="panel-title">
Recovery by Category
</div>

<div id="recoveryCategory" style="margin-top:12px"></div>

</div>


<div class="panel">

<div class="panel-title">
Leadership Summary
</div>

<div id="leadershipSummary" style="margin-top:12px"></div>

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
Ask operational questions using the data currently loaded in this demo.
</div>

</div>

</div>


<div class="ai-grid">

<div class="panel">

<div class="panel-title">
Ask a question
</div>

<div class="ask-box">

<input
id="question"
placeholder="Where are we losing the most money?">

<button
class="btn primary"
id="askBtn">

Ask

</button>

</div>

<div class="answer" id="answer">

Clarity will answer from the current demo cases.

</div>

</div>


<div class="panel">

<div class="panel-title">
Suggested Questions
</div>

<div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:12px">

<button class="btn soft suggestion">
What should we work first?
</button>

<button class="btn soft suggestion">
Which payer has the most risk?
</button>

<button class="btn soft suggestion">
How much is tied to denials?
</button>

<button class="btn soft suggestion">
How much have we recovered?
</button>

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
Leadership-ready financial and operational summary.
</div>

</div>

</div>


<div class="roi-grid">

<div class="card">

<div class="metric-label">
TOTAL IDENTIFIED
</div>

<div class="metric-value" id="reportIdentified">
$0
</div>

</div>


<div class="card">

<div class="metric-label">
RECOVERED
</div>

<div class="metric-value green" id="reportRecovered">
$0
</div>

</div>


<div class="card">

<div class="metric-label">
OPEN
</div>

<div class="metric-value orange" id="reportOpen">
$0
</div>

</div>

</div>


<div class="dashboard-grid">

<div class="panel">

<div class="panel-title">
Executive Summary
</div>

<div id="reportSummary" style="margin-top:12px"></div>

</div>


<div class="panel">

<div class="panel-title">
Top Payer Exposure
</div>

<div id="reportPayers" style="margin-top:12px"></div>

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
Case
</div>

<div class="panel-sub">
Revenue recovery case detail
</div>

</div>

<button class="btn" id="closeCaseBtn">
Close
</button>

</div>


<div class="modal-body">

<div class="case-grid">


<div class="detail-box">

<div class="detail-row">

<div class="detail-label">
Payer
</div>

<div id="casePayer"></div>

</div>


<div class="detail-row">

<div class="detail-label">
Issue
</div>

<div id="caseIssue"></div>

</div>


<div class="detail-row">

<div class="detail-label">
Priority
</div>

<div id="casePriority"></div>

</div>


<div class="detail-row">

<div class="detail-label">
Revenue at Risk
</div>

<div id="caseRisk"></div>

</div>


<div class="detail-row">

<div class="detail-label">
Days Remaining
</div>

<div id="caseDays"></div>

</div>


<div class="detail-row">

<div class="detail-label">
Recommended Action
</div>

<div id="caseAction"></div>

</div>


<div class="detail-row">

<div class="detail-label">
Why Flagged
</div>

<div id="caseReason"></div>

</div>

</div>


<div class="detail-box">

<label class="metric-label">
CASE STATUS
</label>

<select
id="caseStatus"
class="field"
style="margin-top:6px">

<option>Open</option>
<option>In Progress</option>
<option>Escalated</option>
<option>Resolved</option>

</select>


<label
class="metric-label"
style="display:block;margin-top:14px">

CASE NOTE

</label>

<textarea
id="caseNote"
rows="5"
placeholder="Document payer call, missing information, appeal work, owner handoff, etc."
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


<div class="panel"
style="margin-top:14px">

<div class="panel-title">
Case History
</div>

<div id="caseHistory"
style="margin-top:10px">
</div>

</div>

</div>

</div>

</div>


<script>

const money=n=>
new Intl.NumberFormat(
'en-US',
{
style:'currency',
currency:'USD',
maximumFractionDigits:0
}
).format(n||0);


const seedCases=[

{
account:'A1001',
payer:'BCBS',
category:'Authorization',
issue:'Authorization missing',
risk:12850,
days:3,
status:'Open',
reason:'Required authorization is incomplete before the scheduled MRI.',
action:'Verify authorization status today and obtain missing payer documentation.'
},

{
account:'A1002',
payer:'Aetna',
category:'Timely Filing',
issue:'Timely filing deadline',
risk:6750,
days:1,
status:'Open',
reason:'Claim filing deadline is tomorrow.',
action:'Submit claim immediately and document confirmation.'
},

{
account:'A1003',
payer:'United Healthcare',
category:'Denial',
issue:'Medical necessity denial',
risk:4900,
days:31,
status:'Open',
reason:'Denied claim requires documentation review and appeal decision.',
action:'Review denial reason and prepare appeal if supported.'
},

{
account:'A1004',
payer:'BCBS',
category:'Authorization',
issue:'Authorization expires before service',
risk:4300,
days:5,
status:'In Progress',
reason:'Authorization expiration precedes scheduled service date.',
action:'Request authorization extension before service.'
},

{
account:'A1005',
payer:'Cigna',
category:'Eligibility',
issue:'Eligibility not verified',
risk:2100,
days:17,
status:'Open',
reason:'Coverage verification is incomplete before service.',
action:'Re-verify coverage and reconcile registration data.'
},

{
account:'A1006',
payer:'Humana',
category:'Authorization',
issue:'Authorization pending',
risk:8200,
days:10,
status:'Open',
reason:'Authorization remains pending close to service date.',
action:'Contact payer for status and escalate if documentation is outstanding.'
},

{
account:'A1007',
payer:'BCBS',
category:'Denial',
issue:'Denied claim – appeal recommended',
risk:9700,
days:22,
status:'Escalated',
reason:'High-dollar denial with appeal opportunity.',
action:'Escalate to denial specialist and prepare appeal package.'
},

{
account:'A1008',
payer:'Aetna',
category:'Authorization',
issue:'Authorization pending',
risk:3600,
days:6,
status:'Open',
reason:'Authorization remains pending close to service date.',
action:'Follow up with payer and confirm records were received.'
},

{
account:'A1009',
payer:'United Healthcare',
category:'Eligibility',
issue:'Coverage discrepancy',
risk:5600,
days:8,
status:'Open',
reason:'Eligibility response conflicts with registration data.',
action:'Resolve coverage discrepancy before billing.'
},

{
account:'A1010',
payer:'BCBS',
category:'Denial',
issue:'Documentation denial',
risk:7400,
days:18,
status:'Resolved',
reason:'Additional documentation was required.',
action:'Completed.'
}

];


let cases=
JSON.parse(
localStorage.getItem('clarityflow_v12_cases')
||
'null'
)
||
JSON.parse(
JSON.stringify(seedCases)
);


let histories=
JSON.parse(
localStorage.getItem('clarityflow_v12_history')
||
'{}'
);


let currentAccount=null;


function priority(c){

if(c.days<=2 || c.risk>=10000)
return 'Critical';

if(c.days<=8 || c.risk>=5000)
return 'High';

if(c.days<=14)
return 'Medium';

return 'Low';

}


function persist(){

localStorage.setItem(
'clarityflow_v12_cases',
JSON.stringify(cases)
);

localStorage.setItem(
'clarityflow_v12_history',
JSON.stringify(histories)
);

}


function metrics(){

cases.forEach(
c=>c.severity=priority(c)
);

const open=
cases.filter(
c=>c.status!=='Resolved'
);

const recovered=
cases
.filter(
c=>c.status==='Resolved'
)
.reduce(
(s,c)=>s+c.risk,
0
);

const identified=
cases.reduce(
(s,c)=>s+c.risk,
0
);

const openRisk=
open.reduce(
(s,c)=>s+c.risk,
0
);

return{
open,
recovered,
identified,
openRisk,
rate:
identified
?
Math.round(
recovered/identified*100
)
:
0
};

}


function categoryTotal(cat){

return metrics()
.open
.filter(
c=>c.category===cat
)
.reduce(
(s,c)=>s+c.risk,
0
);

}


function largestCategory(){

return[
'Authorization',
'Denial',
'Timely Filing',
'Eligibility'
]
.map(
x=>[
x,
categoryTotal(x)
]
)
.sort(
(a,b)=>b[1]-a[1]
)[0];

}


function payerMap(){

const map={};

metrics()
.open
.forEach(
c=>
map[c.payer]
=
(map[c.payer]||0)
+
c.risk
);

return Object.entries(map)
.sort(
(a,b)=>b[1]-a[1]
);

}


function score(){

const m=
metrics();

return Math.max(
0,
Math.min(
100,
100-
Math.round(
m.open.length/
Math.max(cases.length,1)
*45
)
)
);

}


function statusClass(status){

if(status==='Resolved')
return 'status-resolved';

if(status==='Escalated')
return 'status-escalated';

if(status==='In Progress')
return 'status-progress';

return 'status-open';

}


function renderDashboard(){

const m=
metrics();

const s=
score();

const largest=
largestCategory();


document.getElementById('riskTotal')
.textContent=
money(m.openRisk);


document.getElementById('riskCount')
.textContent=
m.open.length+
' open cases';


document.getElementById('recoveredTotal')
.textContent=
money(m.recovered);


document.getElementById('recoveredCount')
.textContent=
cases.filter(
c=>c.status==='Resolved'
).length+
' resolved cases';


document.getElementById('recoveryRate')
.textContent=
m.rate+'%';


document.getElementById('criticalCount')
.textContent=
m.open.filter(
c=>c.severity==='Critical'
).length;


document.getElementById('sideScore')
.textContent=
s;


document.getElementById('sideScoreLabel')
.textContent=
s>=85
?
'Excellent'
:
s>=70
?
'Good'
:
s>=55
?
'Needs Attention'
:
'At Risk';


document.getElementById('openExposureLabel')
.textContent=
money(m.openRisk)
+
' open';


document.getElementById('riskDrivers')
.innerHTML=
[
'Authorization',
'Denial',
'Timely Filing',
'Eligibility'
]
.map(
cat=>{

const value=
categoryTotal(cat);

const pct=
m.openRisk
?
Math.round(
value/m.openRisk*100
)
:
0;

return`

<div class="risk-row">

<div class="risk-name">
${cat}
</div>

<div class="track">

<div
class="fill"
style="width:${pct}%">
</div>

</div>

<div class="risk-value">
${money(value)} · ${pct}%
</div>

</div>

`;

}
).join('');


const ordered=
[...m.open]
.sort(
(a,b)=>
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
b.risk-a.risk
)
.slice(
0,
5
);


document.getElementById('priorityList')
.innerHTML=
ordered.map(
c=>`

<div class="priority-item">

<div
class="priority-dot"
style="background:${
c.severity==='Critical'
?
'var(--red)'
:
c.severity==='High'
?
'var(--orange)'
:
'var(--blue)'
}">
</div>

<div>

<div class="priority-title">
${c.account} · ${c.payer}
</div>

<div class="priority-sub">
${c.issue} · ${c.days} days remaining
</div>

</div>

<div style="text-align:right">

<div class="priority-money">
${money(c.risk)}
</div>

<button
class="mini-btn open-case"
data-account="${c.account}">

Open

</button>

</div>

</div>

`
).join('');


document.getElementById('payerExposure')
.innerHTML=
payerMap()
.slice(
0,
5
)
.map(
([payer,value])=>`

<div class="info-row">

<div class="info-label">
${payer}
</div>

<div class="info-value">
${money(value)}
</div>

</div>

`
).join('');


const statuses={
Open:0,
'In Progress':0,
Escalated:0,
Resolved:0
};


cases.forEach(
c=>
statuses[c.status]
=
(statuses[c.status]||0)
+
1
);


document.getElementById('operationalHealth')
.innerHTML=
Object.entries(statuses)
.map(
([status,count])=>`

<div class="info-row">

<div class="info-label">
${status}
</div>

<div class="info-value">
${count} cases
</div>

</div>

`
).join('');


document.getElementById('recoverySnapshot')
.innerHTML=

`

<div class="info-row">

<div class="info-label">
Identified
</div>

<div class="info-value">
${money(m.identified)}
</div>

</div>


<div class="info-row">

<div class="info-label">
Recovered
</div>

<div class="info-value green">
${money(m.recovered)}
</div>

</div>


<div class="info-row">

<div class="info-label">
Open
</div>

<div class="info-value orange">
${money(m.openRisk)}
</div>

</div>


<div class="info-row">

<div class="info-label">
Top driver
</div>

<div class="info-value">
${largest[0]}
</div>

</div>

`;

}


function workCards(list){

if(!list.length)
return '<div class="panel-sub">No matching cases.</div>';


return list.map(
c=>`

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


<div class="next-action">
${c.action}
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

const statuses={
Open:0,
'In Progress':0,
Escalated:0,
Resolved:0
};


cases.forEach(
c=>
statuses[c.status]
=
(statuses[c.status]||0)
+
1
);


document.getElementById('wsOpen')
.textContent=
statuses.Open;


document.getElementById('wsProgress')
.textContent=
statuses['In Progress'];


document.getElementById('wsEscalated')
.textContent=
statuses.Escalated;


document.getElementById('wsResolved')
.textContent=
statuses.Resolved;


const severity=
document.getElementById('filterSeverity')
.value;


const category=
document.getElementById('filterCategory')
.value;


const status=
document.getElementById('filterStatus')
.value;


const query=
document.getElementById('searchBox')
.value
.toLowerCase();


const list=
cases.filter(
c=>

(!severity || c.severity===severity)

&&

(!category || c.category===category)

&&

(!status || c.status===status)

&&

(
!query
||
c.account.toLowerCase().includes(query)
||
c.payer.toLowerCase().includes(query)
)

);


document.getElementById('worklist')
.innerHTML=
workCards(list);


wireButtons();

}


function renderOther(){

document.getElementById('authWorklist')
.innerHTML=
workCards(
cases.filter(
c=>c.category==='Authorization'
)
);


document.getElementById('denialWorklist')
.innerHTML=
workCards(
cases.filter(
c=>c.category==='Denial'
)
);


const m=
metrics();


const largest=
largestCategory();


document.getElementById('recIdentified')
.textContent=
money(m.identified);


document.getElementById('recRecovered')
.textContent=
money(m.recovered);


document.getElementById('recOpen')
.textContent=
money(m.openRisk);


document.getElementById('recoveryCategory')
.innerHTML=
[
'Authorization',
'Denial',
'Timely Filing',
'Eligibility'
]
.map(
cat=>`

<div class="info-row">

<div class="info-label">
${cat}
</div>

<div class="info-value">
${money(categoryTotal(cat))}
</div>

</div>

`
).join('');


document.getElementById('leadershipSummary')
.innerHTML=

`

<div class="info-row">

<div class="info-label">
Recovery rate
</div>

<div class="info-value">
${m.rate}%
</div>

</div>


<div class="info-row">

<div class="info-label">
Largest open driver
</div>

<div class="info-value">
${largest[0]}
</div>

</div>


<div class="info-row">

<div class="info-label">
Critical cases
</div>

<div class="info-value">
${m.open.filter(
c=>c.severity==='Critical'
).length}
</div>

</div>


<div class="info-row">

<div class="info-label">
Highest payer exposure
</div>

<div class="info-value">
${payerMap()[0]?.[0]||'—'}
</div>

</div>

`;


document.getElementById('reportIdentified')
.textContent=
money(m.identified);


document.getElementById('reportRecovered')
.textContent=
money(m.recovered);


document.getElementById('reportOpen')
.textContent=
money(m.openRisk);


document.getElementById('reportSummary')
.innerHTML=

`

<p>
<strong>${money(m.openRisk)}</strong>
remains at risk across
<strong>${m.open.length}</strong>
open cases.
</p>

<p>
Current recovery rate is
<strong>${m.rate}%</strong>.
</p>

<p>
The largest open workflow driver is
<strong>${largest[0]}</strong>
at
<strong>${money(largest[1])}</strong>.
</p>

<p>
Recommended focus:
work critical and high-dollar cases with the closest deadlines first.
</p>

`;


document.getElementById('reportPayers')
.innerHTML=
payerMap()
.slice(
0,
5
)
.map(
([payer,value],index)=>`

<div class="info-row">

<div class="info-label">
${index+1}. ${payer}
</div>

<div class="info-value">
${money(value)}
</div>

</div>

`
).join('');


wireButtons();

}


function renderAll(){

cases.forEach(
c=>c.severity=priority(c)
);

renderDashboard();

renderWorkspace();

renderOther();

persist();

wireButtons();

}


function wireButtons(){

document.querySelectorAll('.open-case')
.forEach(
button=>{

button.onclick=
()=>openCase(
button.dataset.account
);

}
);

}


function showView(id){

document.querySelectorAll('.section')
.forEach(
section=>
section.classList.toggle(
'active',
section.id===id
)
);


document.querySelectorAll('.nav-btn')
.forEach(
button=>
button.classList.toggle(
'active',
button.dataset.view===id
)
);


document.getElementById('sidebar')
.classList.remove('open');

}


function openCase(account){

currentAccount=
account;


const c=
cases.find(
x=>x.account===account
);


if(!c)
return;


document.getElementById('caseTitle')
.textContent=
'Case '+c.account;


document.getElementById('casePayer')
.textContent=
c.payer;


document.getElementById('caseIssue')
.textContent=
c.issue;


document.getElementById('casePriority')
.textContent=
c.severity;


document.getElementById('caseRisk')
.textContent=
money(c.risk);


document.getElementById('caseDays')
.textContent=
c.days;


document.getElementById('caseAction')
.textContent=
c.action;


document.getElementById('caseReason')
.textContent=
c.reason;


document.getElementById('caseStatus')
.value=
c.status;


document.getElementById('caseNote')
.value='';


renderHistory();


document.getElementById('caseModal')
.classList.add('open');

}


function renderHistory(){

const history=
histories[currentAccount]
||
[];


document.getElementById('caseHistory')
.innerHTML=
history.length
?
history
.slice()
.reverse()
.map(
item=>`

<div class="history-item">

<div class="work-title">
${item.status}
</div>

<div class="work-sub">
${item.note}
</div>

<div class="work-sub">
${item.time}
</div>

</div>

`
).join('')
:
'<div class="panel-sub">No case history yet.</div>';

}


function saveCase(){

const c=
cases.find(
x=>x.account===currentAccount
);


if(!c)
return;


c.status=
document.getElementById('caseStatus')
.value;


const note=
document.getElementById('caseNote')
.value
.trim();


histories[currentAccount]
=
histories[currentAccount]
||
[];


histories[currentAccount]
.push(
{

status:c.status,

note:
note
||
'Status updated.',

time:
new Date()
.toLocaleString()

}
);


document.getElementById('caseNote')
.value='';


renderAll();

renderHistory();

}


function askClarity(){

const query=
document.getElementById('question')
.value
.toLowerCase();


const m=
metrics();


let response='';


if(!m.open.length){

response=
'There are no open cases to analyze.';

}


else if(
query.includes('denial')
){

const denials=
m.open.filter(
c=>c.category==='Denial'
);

response=
`

There are
${denials.length}
open denial cases representing
${money(
denials.reduce(
(s,c)=>s+c.risk,
0
)
)}
in revenue exposure.

`;

}


else if(
query.includes('auth')
){

const auth=
m.open.filter(
c=>c.category==='Authorization'
);

response=
`

Authorization issues represent
${money(
auth.reduce(
(s,c)=>s+c.risk,
0
)
)}
across
${auth.length}
open cases.

`;

}


else if(
query.includes('payer')
){

const top=
payerMap()[0];


response=
`

${top[0]}
currently has the largest open payer exposure at
${money(top[1])}.

`;

}


else if(
query.includes('first')
||
query.includes('priority')
){

const c=
[...m.open]
.sort(
(a,b)=>
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
b.risk-a.risk
)[0];


response=
`

Work
${c.account}
first:

${c.issue},

${money(c.risk)}
at risk,

${c.days}
days remaining.

Recommended action:
${c.action}

`;

}


else if(
query.includes('recover')
){

response=
`

${money(m.recovered)}
has been marked recovered.

${money(m.openRisk)}
remains open.

Current recovery rate:
${m.rate}%.

`;

}


else{

const largest=
largestCategory();


response=
`

${money(m.openRisk)}
is currently at risk across
${m.open.length}
open cases.

The largest workflow driver is
${largest[0]}
at
${money(largest[1])}.

`;

}


document.getElementById('answer')
.textContent=
response;

}


function resetDemo(){

if(
confirm(
'Reset all demo cases and history?'
)
){

cases=
JSON.parse(
JSON.stringify(seedCases)
);

histories={};

renderAll();

}

}


function exportCSV(){

const headers=
[
'priority',
'account',
'payer',
'category',
'issue',
'risk',
'days',
'status',
'recommended_action',
'reason'
];


const lines=
[
headers.join(',')
]
.concat(
cases.map(
c=>
[
c.severity,
c.account,
c.payer,
c.category,
c.issue,
c.risk,
c.days,
c.status,
c.action,
c.reason
]
.map(
value=>
`"${String(value).replaceAll('"','""')}"`
)
.join(',')
)
);


const blob=
new Blob(
[
lines.join('\n')
],
{
type:'text/csv'
}
);


const a=
document.createElement('a');


a.href=
URL.createObjectURL(blob);


a.download=
'clarityflow_work_queue.csv';


a.click();

}


document.querySelectorAll('.nav-btn')
.forEach(
button=>
button.addEventListener(
'click',
()=>showView(
button.dataset.view
)
)
);


document.getElementById('menuBtn')
.addEventListener(
'click',
()=>document.getElementById('sidebar')
.classList.toggle('open')
);


document.getElementById('closeCaseBtn')
.addEventListener(
'click',
()=>document.getElementById('caseModal')
.classList.remove('open')
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


document.getElementById('question')
.addEventListener(
'keydown',
event=>{

if(event.key==='Enter')
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
exportCSV
);


[
'searchBox',
'filterSeverity',
'filterCategory',
'filterStatus'
]
.forEach(
id=>
document.getElementById(id)
.addEventListener(
id==='searchBox'
?
'input'
:
'change',
renderWorkspace
)
);


document.querySelectorAll('.suggestion')
.forEach(
button=>
button.addEventListener(
'click',
()=>{

document.getElementById('question')
.value=
button.textContent.trim();

askClarity();

}
)
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
