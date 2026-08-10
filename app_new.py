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
--nav:#081a37;
--purple:#7047eb;
--bg:#f6f7fb;
--text:#182230;
--muted:#667085;
--line:#e4e7ec;
--red:#d92d20;
--orange:#f79009;
--green:#039855;
}

*{box-sizing:border-box}

body{
margin:0;
font-family:Arial,Helvetica,sans-serif;
background:var(--bg);
color:var(--text);
}

.sidebar{
position:fixed;
left:0;
top:0;
width:235px;
height:100vh;
background:var(--nav);
color:white;
padding:24px 15px;
}

.logo{
font-size:25px;
font-weight:bold;
}

.logo span{color:#9b7cff}

.company{
font-size:12px;
opacity:.7;
margin:5px 0 28px;
}

.nav button{
width:100%;
border:0;
background:transparent;
color:white;
text-align:left;
padding:13px;
border-radius:9px;
margin-bottom:5px;
font-weight:bold;
cursor:pointer;
}

.nav button.active,
.nav button:hover{
background:#5e3ed2;
}

.score{
border:1px solid #36506e;
margin-top:28px;
padding:18px;
text-align:center;
border-radius:14px;
}

.score-number{
font-size:42px;
font-weight:bold;
}

.main{
margin-left:235px;
padding:25px;
}

.header{
display:flex;
justify-content:space-between;
align-items:center;
gap:15px;
flex-wrap:wrap;
}

.header h1{margin:0}

.subtitle{
color:var(--muted);
margin-top:5px;
}

.badge{
background:#ecfdf3;
color:#067647;
padding:8px 12px;
border-radius:20px;
font-weight:bold;
}

.notice{
margin:18px 0;
background:#eef4ff;
color:#3538cd;
padding:12px;
border-radius:10px;
}

.section{display:none}
.section.active{display:block}

.cards{
display:grid;
grid-template-columns:repeat(3,1fr);
gap:12px;
}

.card{
background:white;
border:1px solid var(--line);
border-radius:14px;
padding:18px;
}

.label{
color:var(--muted);
font-size:12px;
font-weight:bold;
}

.number{
font-size:28px;
font-weight:bold;
margin-top:9px;
}

.red{color:var(--red)}
.orange{color:var(--orange)}
.green{color:var(--green)}

.two-column{
display:grid;
grid-template-columns:1.2fr .8fr;
gap:12px;
margin-top:14px;
}

.three-column{
display:grid;
grid-template-columns:repeat(3,1fr);
gap:12px;
margin-top:14px;
}

.progress{
background:#edf0f5;
height:10px;
border-radius:20px;
overflow:hidden;
margin:7px 0 6px;
}

.progress div{
height:100%;
background:var(--purple);
}

.case{
padding:13px;
background:#fafafa;
margin-bottom:9px;
border-radius:10px;
border:1px solid #eee;
}

table{
width:100%;
border-collapse:collapse;
font-size:13px;
}

th,td{
padding:11px;
border-bottom:1px solid #e5e7eb;
text-align:left;
white-space:nowrap;
}

.table-wrap{overflow:auto}

.priority{
padding:5px 8px;
border-radius:15px;
font-size:11px;
font-weight:bold;
}

.Critical{
background:#fee4e2;
color:#b42318;
}

.High{
background:#fef0c7;
color:#b54708;
}

.Medium{
background:#fef7c3;
color:#7a5b00;
}

.Low{
background:#dcfae6;
color:#067647;
}

.btn{
background:white;
color:var(--text);
border:1px solid var(--line);
padding:8px 11px;
border-radius:8px;
font-weight:bold;
cursor:pointer;
}

.btn.primary{
background:var(--purple);
color:white;
border-color:var(--purple);
}

.filters{
display:flex;
gap:8px;
flex-wrap:wrap;
margin-bottom:12px;
}

.filters select,
.filters input,
.field,
textarea{
padding:10px;
border:1px solid var(--line);
border-radius:8px;
background:white;
}

.filters input{min-width:220px}

.ask-row{
display:flex;
gap:8px;
}

.ask-row input{
flex:1;
padding:12px;
border:1px solid var(--line);
border-radius:8px;
}

.answer{
margin-top:12px;
padding:14px;
background:#f4f0ff;
border-radius:10px;
min-height:70px;
}

.metric{
font-size:22px;
font-weight:bold;
margin-top:6px;
}

.modal{
position:fixed;
inset:0;
background:#0008;
display:none;
align-items:center;
justify-content:center;
padding:16px;
z-index:20;
}

.modal.open{display:flex}

.modal-card{
background:white;
border-radius:16px;
padding:20px;
max-width:800px;
width:100%;
max-height:90vh;
overflow:auto;
}

.modal-grid{
display:grid;
grid-template-columns:1fr 1fr;
gap:18px;
}

.history-item{
padding:10px 0;
border-bottom:1px solid var(--line);
}

.small{
font-size:12px;
color:var(--muted);
}

.actions{
display:flex;
gap:8px;
flex-wrap:wrap;
}

@media(max-width:850px){

.sidebar{
position:relative;
width:100%;
height:auto;
}

.main{
margin-left:0;
padding:15px;
}

.nav{
display:flex;
overflow-x:auto;
gap:5px;
}

.nav button{
min-width:155px;
}

.score{display:none}

.cards{
grid-template-columns:repeat(2,1fr);
}

.two-column,
.three-column,
.modal-grid{
grid-template-columns:1fr;
}

}
</style>
</head>

<body>

<div class="sidebar">

<div class="logo">
ClarityFlow <span>AI</span>™
</div>

<div class="company">
by Clarity Health Advisors
</div>

<div class="nav">

<button class="active"
onclick="showSection('dashboard',this)">
Executive Dashboard
</button>

<button onclick="showSection('queue',this)">
Smart Work Queue
</button>

<button onclick="showSection('auth',this)">
Prior Authorization
</button>

<button onclick="showSection('denials',this)">
Denial Recovery
</button>

<button onclick="showSection('ai',this)">
Ask Clarity AI
</button>

<button onclick="showSection('reports',this)">
Executive ROI
</button>

</div>

<div class="score">

<div>CLARITY RECOVERY SCORE</div>

<div class="score-number" id="scoreNumber">
73
</div>

<div id="scoreLabel">
/100 — Good
</div>

</div>

</div>


<div class="main">

<div class="header">

<div>

<h1>ClarityFlow AI</h1>

<div class="subtitle">
Healthcare revenue recovery intelligence
</div>

</div>

<div class="actions">

<span class="badge">
● SYSTEM LIVE
</span>

<button class="btn"
onclick="resetDemo()">
Reset Demo
</button>

<button class="btn"
onclick="exportCSV()">
Export Queue
</button>

</div>

</div>


<div class="notice">

DEMO MODE — Synthetic healthcare data only.
No real patient information should be entered into this demonstration.

</div>


<div id="dashboard"
class="section active">

<div class="cards">

<div class="card">

<div class="label">
REVENUE AT RISK
</div>

<div class="number red"
id="totalRisk">
$0
</div>

<div id="openCases">
0 open cases
</div>

</div>


<div class="card">

<div class="label">
PRIOR AUTHORIZATION
</div>

<div class="number orange"
id="authRisk">
$0
</div>

<div id="authCount">
0 cases
</div>

</div>


<div class="card">

<div class="label">
DENIAL RISK
</div>

<div class="number"
id="denialRisk">
$0
</div>

<div id="denialCount">
0 cases
</div>

</div>


<div class="card">

<div class="label">
TIMELY FILING
</div>

<div class="number"
id="filingRisk">
$0
</div>

<div id="filingCount">
0 cases
</div>

</div>


<div class="card">

<div class="label">
ELIGIBILITY ISSUES
</div>

<div class="number"
id="eligRisk">
$0
</div>

<div id="eligCount">
0 cases
</div>

</div>


<div class="card">

<div class="label">
RECOVERED REVENUE
</div>

<div class="number green"
id="recovered">
$0
</div>

<div id="resolvedCount">
0 resolved cases
</div>

</div>

</div>


<div class="two-column">

<div class="card">

<h2>Revenue Leak Detector</h2>

<div id="drivers"></div>

</div>


<div class="card">

<h2>Top Priority</h2>

<div id="topPriority"></div>

</div>

</div>


<div class="three-column">

<div class="card">

<div class="label">
CRITICAL CASES
</div>

<div class="metric red"
id="criticalCount">
0
</div>

</div>


<div class="card">

<div class="label">
AVERAGE $ AT RISK
</div>

<div class="metric"
id="avgRisk">
$0
</div>

</div>


<div class="card">

<div class="label">
RECOVERY RATE
</div>

<div class="metric green"
id="recoveryRate">
0%
</div>

</div>

</div>

</div>


<div id="queue"
class="section">

<div class="card">

<h2>Smart Work Queue</h2>

<div class="filters">

<select id="filterSeverity"
onchange="renderQueue()">

<option value="">
All priorities
</option>

<option>Critical</option>
<option>High</option>
<option>Medium</option>
<option>Low</option>

</select>


<select id="filterCategory"
onchange="renderQueue()">

<option value="">
All categories
</option>

<option>Authorization</option>
<option>Denial</option>
<option>Timely Filing</option>
<option>Eligibility</option>

</select>


<select id="filterStatus"
onchange="renderQueue()">

<option value="">
All statuses
</option>

<option>Open</option>
<option>In Progress</option>
<option>Escalated</option>
<option>Resolved</option>

</select>


<input
id="searchBox"
placeholder="Search account or payer"
oninput="renderQueue()">

</div>


<div class="table-wrap">

<table>

<thead>

<tr>

<th>Priority</th>
<th>Account</th>
<th>Payer</th>
<th>Issue</th>
<th>$ at Risk</th>
<th>Days</th>
<th>Status</th>
<th>Action</th>

</tr>

</thead>

<tbody id="queueBody"></tbody>

</table>

</div>

</div>

</div>


<div id="auth"
class="section">

<div class="card">

<h2>
Prior Authorization Command Center
</h2>

<div id="authList"></div>

</div>

</div>


<div id="denials"
class="section">

<div class="card">

<h2>
Denial Recovery Center
</h2>

<div id="denialList"></div>

</div>

</div>


<div id="ai"
class="section">

<div class="card">

<h2>Ask Clarity AI</h2>

<p>
Ask questions about the cases currently in this demo.
</p>

<div class="ask-row">

<input
id="question"
placeholder="Where are we losing the most money?">

<button
class="btn primary"
onclick="askClarity()">
Ask
</button>

</div>

<div class="answer"
id="answer">

Try:
“What should we work first?”,
“How much is tied to denials?”,
or
“Which payer has the most risk?”

</div>

</div>

</div>


<div id="reports"
class="section">

<div class="cards">

<div class="card">

<div class="label">
REVENUE IDENTIFIED
</div>

<div class="number"
id="roiIdentified">
$0
</div>

</div>


<div class="card">

<div class="label">
REVENUE RECOVERED
</div>

<div class="number green"
id="roiRecovered">
$0
</div>

</div>


<div class="card">

<div class="label">
OPEN OPPORTUNITY
</div>

<div class="number orange"
id="roiOpen">
$0
</div>

</div>

</div>


<div class="two-column">

<div class="card">

<h2>
Executive ROI Summary
</h2>

<div id="roiSummary"></div>

</div>


<div class="card">

<h2>
Top Payer Exposure
</h2>

<div id="payerSummary"></div>

</div>

</div>

</div>

</div>


<div class="modal"
id="caseModal">

<div class="modal-card">

<div class="header">

<h2 id="mTitle">
Case
</h2>

<button class="btn"
onclick="closeCase()">
Close
</button>

</div>


<div class="modal-grid">

<div>

<p>
<b>Payer:</b>
<span id="mPayer"></span>
</p>

<p>
<b>Issue:</b>
<span id="mIssue"></span>
</p>

<p>
<b>Priority:</b>
<span id="mSeverity"></span>
</p>

<p>
<b>Revenue at risk:</b>
<span id="mRisk"></span>
</p>

<p>
<b>Why flagged:</b>
<span id="mReason"></span>
</p>

</div>


<div>

<label>Status</label>

<select id="mStatus"
class="field">

<option>Open</option>
<option>In Progress</option>
<option>Escalated</option>
<option>Resolved</option>

</select>

<br><br>

<label>Case note</label>

<textarea
id="mNote"
rows="5"
class="field"
placeholder="Document payer call, missing information, appeal work, etc.">
</textarea>

<br><br>

<button
class="btn primary"
onclick="saveCase()">
Save Case Update
</button>

</div>

</div>


<h3 style="margin-top:20px">
Case History
</h3>

<div id="mHistory"></div>

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
reason:'Required authorization is incomplete before the scheduled MRI.'
},

{
account:'A1002',
payer:'Aetna',
category:'Timely Filing',
issue:'Timely filing deadline',
risk:6750,
days:1,
status:'Open',
reason:'Claim filing deadline is tomorrow.'
},

{
account:'A1003',
payer:'United Healthcare',
category:'Denial',
issue:'Medical necessity denial',
risk:4900,
days:31,
status:'Open',
reason:'Denied claim requires documentation review and appeal decision.'
},

{
account:'A1004',
payer:'BCBS',
category:'Authorization',
issue:'Authorization expires before service',
risk:4300,
days:5,
status:'Open',
reason:'Authorization expiration precedes scheduled service date.'
},

{
account:'A1005',
payer:'Cigna',
category:'Eligibility',
issue:'Eligibility not verified',
risk:2100,
days:17,
status:'Open',
reason:'Coverage verification is incomplete before service.'
},

{
account:'A1006',
payer:'Humana',
category:'Authorization',
issue:'Authorization pending',
risk:8200,
days:10,
status:'Open',
reason:'Authorization remains pending close to service date.'
},

{
account:'A1007',
payer:'BCBS',
category:'Denial',
issue:'Denied claim – appeal recommended',
risk:9700,
days:22,
status:'Open',
reason:'High-dollar denial with appeal opportunity.'
},

{
account:'A1008',
payer:'Aetna',
category:'Authorization',
issue:'Authorization pending',
risk:3600,
days:6,
status:'Open',
reason:'Authorization remains pending close to service date.'
},

{
account:'A1009',
payer:'United Healthcare',
category:'Eligibility',
issue:'Coverage discrepancy',
risk:5600,
days:8,
status:'Open',
reason:'Eligibility response conflicts with registration data.'
},

{
account:'A1010',
payer:'BCBS',
category:'Denial',
issue:'Documentation denial',
risk:7400,
days:18,
status:'Resolved',
reason:'Additional documentation was required.'
}

];


let cases=
JSON.parse(
localStorage.getItem(
'clarityflow_cases_v11'
)||'null'
)
||
JSON.parse(
JSON.stringify(seedCases)
);


let histories=
JSON.parse(
localStorage.getItem(
'clarityflow_history_v11'
)||'{}'
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
'clarityflow_cases_v11',
JSON.stringify(cases)
);

localStorage.setItem(
'clarityflow_history_v11',
JSON.stringify(histories)
);

}


function showSection(id,button){

document.querySelectorAll('.section')
.forEach(
x=>x.classList.remove('active')
);

document.getElementById(id)
.classList.add('active');

document.querySelectorAll('.nav button')
.forEach(
x=>x.classList.remove('active')
);

button.classList.add('active');

}


function totals(){

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

const openRisk=
open.reduce(
(s,c)=>s+c.risk,
0
);

const identified=
cases.reduce(
(s,c)=>s+c.risk,
0
);

return {
open,
recovered,
openRisk,
identified
};

}


function categoryTotal(cat){

return totals()
.open
.filter(
c=>c.category===cat
)
.reduce(
(s,c)=>s+c.risk,
0
);

}


function categoryCount(cat){

return totals()
.open
.filter(
c=>c.category===cat
).length;

}


function render(){

const t=totals();

document.getElementById('totalRisk')
.textContent=money(t.openRisk);

document.getElementById('openCases')
.textContent=t.open.length+' open cases';

document.getElementById('authRisk')
.textContent=
money(categoryTotal('Authorization'));

document.getElementById('denialRisk')
.textContent=
money(categoryTotal('Denial'));

document.getElementById('filingRisk')
.textContent=
money(categoryTotal('Timely Filing'));

document.getElementById('eligRisk')
.textContent=
money(categoryTotal('Eligibility'));

document.getElementById('authCount')
.textContent=
categoryCount('Authorization')+' cases';

document.getElementById('denialCount')
.textContent=
categoryCount('Denial')+' cases';

document.getElementById('filingCount')
.textContent=
categoryCount('Timely Filing')+' cases';

document.getElementById('eligCount')
.textContent=
categoryCount('Eligibility')+' cases';

document.getElementById('recovered')
.textContent=
money(t.recovered);

document.getElementById('resolvedCount')
.textContent=
cases.filter(
c=>c.status==='Resolved'
).length+
' resolved cases';


const crit=
t.open.filter(
c=>c.severity==='Critical'
).length;

document.getElementById('criticalCount')
.textContent=crit;


document.getElementById('avgRisk')
.textContent=
money(
t.open.length
?
t.openRisk/t.open.length
:
0
);


const rate=
t.identified
?
Math.round(
t.recovered/t.identified*100
)
:
0;


document.getElementById('recoveryRate')
.textContent=
rate+'%';


const score=
Math.max(
0,
Math.min(
100,
100-
Math.round(
t.open.length/
Math.max(cases.length,1)
*45
)
)
);


document.getElementById('scoreNumber')
.textContent=score;


document.getElementById('scoreLabel')
.textContent=
'/100 — '+
(
score>=85
?
'Excellent'
:
score>=70
?
'Good'
:
score>=55
?
'Needs Attention'
:
'At Risk'
);


const cats=[
'Authorization',
'Denial',
'Timely Filing',
'Eligibility'
];


document.getElementById('drivers')
.innerHTML=
cats.map(
cat=>{

const v=
categoryTotal(cat);

const pct=
t.openRisk
?
Math.round(
v/t.openRisk*100
)
:
0;

return `
<b>${cat}</b>

<div class="progress">
<div style="width:${pct}%"></div>
</div>

<div class="small">
${money(v)} · ${pct}% of open exposure
</div>

<br>
`;

}
).join('');


const ordered=
[...t.open]
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
);


const top=ordered[0];


document.getElementById('topPriority')
.innerHTML=
top
?
`

<div class="case">

<span class="priority ${top.severity}">
${top.severity}
</span>

<h3 style="margin:10px 0 5px">

${top.account}
—
${top.issue}

</h3>

<b class="red">
${money(top.risk)} at risk
</b>

<p>
${top.days} days remaining
</p>

<p class="small">
${top.reason}
</p>

<button
class="btn primary"
onclick="openCase('${top.account}')">

Review Case

</button>

</div>

`
:
'<div class="case">No open cases.</div>';


document.getElementById('authList')
.innerHTML=
caseCards(
cases.filter(
c=>c.category==='Authorization'
)
);


document.getElementById('denialList')
.innerHTML=
caseCards(
cases.filter(
c=>c.category==='Denial'
)
);


document.getElementById('roiIdentified')
.textContent=
money(t.identified);


document.getElementById('roiRecovered')
.textContent=
money(t.recovered);


document.getElementById('roiOpen')
.textContent=
money(t.openRisk);


document.getElementById('roiSummary')
.innerHTML=
`

<p>
<b>Recovery rate:</b>
${rate}%
</p>

<p>
<b>Resolved cases:</b>
${cases.filter(
c=>c.status==='Resolved'
).length}
</p>

<p>
<b>Open cases:</b>
${t.open.length}
</p>

<p>
<b>Largest risk category:</b>
${largestCategory()}
</p>

`;


document.getElementById('payerSummary')
.innerHTML=
payerSummaryHTML();


renderQueue();

persist();

}


function caseCards(list){

return list.length
?
list.map(
c=>
`

<div class="case">

<b>${c.account}</b>
·
${c.payer}

<br>

${c.issue}

<br>

<b class="red">
${money(c.risk)}
</b>

·
${c.status}

<br>

<button
class="btn"
style="margin-top:8px"
onclick="openCase('${c.account}')">

Review

</button>

</div>

`
).join('')
:
'<div class="case">No cases.</div>';

}


function largestCategory(){

const values=
[
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
);

return
values[0][0]
+
' ('
+
money(values[0][1])
+
')';

}


function payerSummaryHTML(){

const map={};

totals()
.open
.forEach(
c=>
map[c.payer]
=
(map[c.payer]||0)
+
c.risk
);

const rows=
Object.entries(map)
.sort(
(a,b)=>b[1]-a[1]
);

return rows.length
?
rows.map(
([p,v],i)=>
`

<p>

<b>
${i+1}. ${p}
</b>

—
${money(v)}

</p>

`
).join('')
:
'<p>No open payer exposure.</p>';

}


function renderQueue(){

const sev=
document.getElementById(
'filterSeverity'
).value;

const cat=
document.getElementById(
'filterCategory'
).value;

const status=
document.getElementById(
'filterStatus'
).value;

const q=
document.getElementById(
'searchBox'
).value.toLowerCase();


cases.forEach(
c=>c.severity=priority(c)
);


const list=
cases
.filter(
c=>
(!sev || c.severity===sev)
&&
(!cat || c.category===cat)
&&
(!status || c.status===status)
&&
(
!q
||
c.account.toLowerCase().includes(q)
||
c.payer.toLowerCase().includes(q)
)
)
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
);


document.getElementById('queueBody')
.innerHTML=
list.map(
c=>
`

<tr>

<td>

<span class="priority ${c.severity}">
${c.severity}
</span>

</td>

<td>
${c.account}
</td>

<td>
${c.payer}
</td>

<td>
${c.issue}
</td>

<td>
<b>${money(c.risk)}</b>
</td>

<td>
${c.days}
</td>

<td>
${c.status}
</td>

<td>

<button
class="btn"
onclick="openCase('${c.account}')">

Review

</button>

</td>

</tr>

`
).join('');

}


window.openCase=
account=>{

currentAccount=account;

const c=
cases.find(
x=>x.account===account
);

if(!c)return;


document.getElementById('mTitle')
.textContent=
'Case '+c.account;


document.getElementById('mPayer')
.textContent=c.payer;


document.getElementById('mIssue')
.textContent=c.issue;


document.getElementById('mSeverity')
.textContent=c.severity;


document.getElementById('mRisk')
.textContent=money(c.risk);


document.getElementById('mReason')
.textContent=c.reason;


document.getElementById('mStatus')
.value=c.status;


document.getElementById('mNote')
.value='';


renderHistory();


document.getElementById('caseModal')
.classList.add('open');

};


function closeCase(){

document.getElementById('caseModal')
.classList.remove('open');

}


function saveCase(){

const c=
cases.find(
x=>x.account===currentAccount
);

if(!c)return;


const newStatus=
document.getElementById('mStatus')
.value;


const note=
document.getElementById('mNote')
.value.trim();


c.status=
newStatus;


histories[currentAccount]
=
histories[currentAccount]
||
[];


histories[currentAccount]
.push(
{

status:newStatus,

note:
note
||
'Status updated.',

time:
new Date().toLocaleString()

}
);


document.getElementById('mNote')
.value='';


render();

renderHistory();

}


function renderHistory(){

const list=
histories[currentAccount]
||
[];


document.getElementById('mHistory')
.innerHTML=
list.length
?
list
.slice()
.reverse()
.map(
h=>
`

<div class="history-item">

<b>
${h.status}
</b>

<br>

${h.note}

<div class="small">
${h.time}
</div>

</div>

`
).join('')
:
'<div class="small">No case history yet.</div>';

}


function askClarity(){

const q=
document.getElementById('question')
.value.toLowerCase();


const t=
totals();


if(!t.open.length){

document.getElementById('answer')
.innerHTML=
'There are no open cases to analyze.';

return;

}


let reply='';


if(q.includes('denial')){

const xs=
t.open.filter(
c=>c.category==='Denial'
);

reply=
`

<b>Denial analysis:</b>

<br>

${xs.length}
open denial cases represent
${money(
xs.reduce(
(s,c)=>s+c.risk,
0
)
)}
in revenue exposure.

`;

}


else if(q.includes('auth')){

const xs=
t.open.filter(
c=>c.category==='Authorization'
);

reply=
`

<b>Prior authorization analysis:</b>

<br>

${xs.length}
open authorization cases represent
${money(
xs.reduce(
(s,c)=>s+c.risk,
0
)
)}
at risk.

`;

}


else if(q.includes('payer')){

const map={};

t.open.forEach(
c=>
map[c.payer]
=
(map[c.payer]||0)
+
c.risk
);

const top=
Object.entries(map)
.sort(
(a,b)=>b[1]-a[1]
)[0];

reply=
`

<b>Payer exposure:</b>

<br>

${top[0]}
currently has the largest open exposure at
${money(top[1])}.

`;

}


else if(
q.includes('first')
||
q.includes('priority')
){

const ordered=
[...t.open]
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
);


const c=
ordered[0];


reply=
`

<b>Highest priority:</b>

<br>

Work
${c.account}
first:

${c.issue},

${money(c.risk)}
at risk,

${c.days}
days remaining.

`;

}


else if(
q.includes('recover')
){

reply=
`

<b>Recovery performance:</b>

<br>

${money(t.recovered)}
has been marked recovered.

${money(t.openRisk)}
remains open.

`;

}


else{

reply=
`

<b>Revenue analysis:</b>

<br>

${money(t.openRisk)}
is currently at risk across
${t.open.length}
open cases.

The largest category is
${largestCategory()}.

`;

}


document.getElementById('answer')
.innerHTML=
reply;

}


function resetDemo(){

if(
confirm(
'Reset all demo cases and notes?'
)
){

cases=
JSON.parse(
JSON.stringify(seedCases)
);

histories={};

persist();

render();

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
c.reason
]
.map(
v=>
`"${String(v).replaceAll('"','""')}"`
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


render();

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return HTML

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
