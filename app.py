from flask import Flask

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ClarityFlow AI</title>

<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    background: #f6f7fb;
    color: #182230;
}

.sidebar {
    position: fixed;
    left: 0;
    top: 0;
    width: 230px;
    height: 100vh;
    background: #081a37;
    color: white;
    padding: 24px 15px;
}

.logo {
    font-size: 25px;
    font-weight: bold;
    margin-bottom: 5px;
}

.logo span { color: #9b7cff; }

.company {
    font-size: 12px;
    opacity: .7;
    margin-bottom: 30px;
}

.nav button {
    width: 100%;
    border: none;
    background: transparent;
    color: white;
    text-align: left;
    padding: 13px;
    border-radius: 9px;
    margin-bottom: 5px;
    font-weight: bold;
}

.nav button:hover,
.nav button.active {
    background: #5e3ed2;
}

.score {
    border: 1px solid #36506e;
    margin-top: 30px;
    padding: 18px;
    text-align: center;
    border-radius: 14px;
}

.score-number {
    font-size: 42px;
    font-weight: bold;
    margin-top: 10px;
}

.main {
    margin-left: 230px;
    padding: 25px;
}

.header {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    flex-wrap: wrap;
    align-items: center;
}

.header h1 {
    margin: 0;
}

.subtitle {
    color: #667085;
    margin-top: 5px;
}

.badge {
    background: #ecfdf3;
    color: #067647;
    padding: 8px 12px;
    border-radius: 20px;
    font-weight: bold;
}

.notice {
    margin: 18px 0;
    background: #eef4ff;
    color: #3538cd;
    padding: 12px;
    border-radius: 10px;
}

.cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
}

.card {
    background: white;
    border: 1px solid #e4e7ec;
    border-radius: 14px;
    padding: 18px;
}

.label {
    color: #667085;
    font-size: 12px;
    font-weight: bold;
}

.number {
    font-size: 28px;
    font-weight: bold;
    margin-top: 9px;
}

.red { color: #d92d20; }
.orange { color: #f79009; }
.green { color: #039855; }

.two-column {
    display: grid;
    grid-template-columns: 1.2fr .8fr;
    gap: 12px;
    margin-top: 14px;
}

h2 {
    margin-top: 0;
}

.progress {
    background: #edf0f5;
    height: 10px;
    border-radius: 20px;
    overflow: hidden;
    margin: 7px 0 16px;
}

.progress div {
    height: 100%;
    background: #7047eb;
}

table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
}

th, td {
    text-align: left;
    padding: 11px;
    border-bottom: 1px solid #e5e7eb;
}

.priority {
    padding: 5px 8px;
    border-radius: 15px;
    font-size: 11px;
    font-weight: bold;
}

.critical {
    background: #fee4e2;
    color: #b42318;
}

.high {
    background: #fef0c7;
    color: #b54708;
}

.review {
    background: #7047eb;
    color: white;
    border: none;
    padding: 7px 11px;
    border-radius: 7px;
}

.section {
    display: none;
}

.section.active {
    display: block;
}

.case {
    padding: 13px;
    background: #fafafa;
    margin-bottom: 9px;
    border-radius: 10px;
    border: 1px solid #eee;
}

.ask-row {
    display: flex;
    gap: 8px;
}

.ask-row input {
    flex: 1;
    padding: 12px;
    border-radius: 8px;
    border: 1px solid #ddd;
}

.ask-row button {
    background: #7047eb;
    border: none;
    color: white;
    padding: 12px 18px;
    border-radius: 8px;
}

.answer {
    margin-top: 12px;
    padding: 14px;
    background: #f4f0ff;
    border-radius: 10px;
}

@media (max-width: 850px) {

    .sidebar {
        position: relative;
        width: 100%;
        height: auto;
    }

    .main {
        margin-left: 0;
        padding: 15px;
    }

    .nav {
        display: flex;
        overflow-x: auto;
        gap: 5px;
    }

    .nav button {
        min-width: 160px;
    }

    .score {
        display: none;
    }

    .cards {
        grid-template-columns: repeat(2, 1fr);
    }

    .two-column {
        grid-template-columns: 1fr;
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

</div>

<div class="score">
<div>CLARITY RECOVERY SCORE</div>
<div class="score-number">73</div>
<div>/100 — Good</div>
</div>

</div>


<div class="main">

<div class="header">

<div>
<h1>Executive Dashboard</h1>
<div class="subtitle">
Revenue intelligence at a glance
</div>
</div>

<div class="badge">
● SYSTEM LIVE
</div>

</div>

<div class="notice">
DEMO MODE — Synthetic healthcare data only.
No patient information is stored in this demonstration.
</div>


<div id="dashboard" class="section active">

<div class="cards">

<div class="card">
<div class="label">REVENUE AT RISK</div>
<div class="number red">$247,850</div>
<div>37 cases need attention</div>
</div>

<div class="card">
<div class="label">PRIOR AUTHORIZATION</div>
<div class="number orange">$81,400</div>
<div>12 high-risk cases</div>
</div>

<div class="card">
<div class="label">DENIAL RISK</div>
<div class="number">$96,750</div>
<div>18 denied claims</div>
</div>

<div class="card">
<div class="label">TIMELY FILING</div>
<div class="number">$34,200</div>
<div>6 deadlines approaching</div>
</div>

<div class="card">
<div class="label">ELIGIBILITY ISSUES</div>
<div class="number">$21,500</div>
<div>9 verification issues</div>
</div>

<div class="card">
<div class="label">RECOVERED REVENUE</div>
<div class="number green">$94,700</div>
<div>Month to date</div>
</div>

</div>


<div class="two-column">

<div class="card">

<h2>Revenue Leak Detector</h2>

<b>Authorization</b>
<div class="progress">
<div style="width:33%"></div>
</div>

<b>Medical Necessity Denials</b>
<div class="progress">
<div style="width:25%"></div>
</div>

<b>Documentation Issues</b>
<div class="progress">
<div style="width:17%"></div>
</div>

<b>Timely Filing</b>
<div class="progress">
<div style="width:14%"></div>
</div>

<p>
<strong>Largest opportunity:</strong>
Prior authorization delays represent approximately
<strong>$81,400</strong> in revenue exposure.
</p>

</div>


<div class="card">

<h2>Critical Cases</h2>

<div class="case">
🔴 Authorization missing<br>
<b>$12,850 at risk</b><br>
MRI scheduled in 3 days
</div>

<div class="case">
🔴 Filing deadline<br>
<b>$6,750 at risk</b><br>
Deadline tomorrow
</div>

<div class="case">
🟠 Denied claim<br>
<b>$9,700 at risk</b><br>
Appeal recommended
</div>

</div>

</div>

</div>


<div id="queue" class="section">

<div class="card">

<h2>Smart Work Queue</h2>

<table>

<tr>
<th>Priority</th>
<th>Account</th>
<th>Payer</th>
<th>Issue</th>
<th>$ at Risk</th>
<th>Action</th>
</tr>

<tr>
<td><span class="priority critical">Critical</span></td>
<td>A1001</td>
<td>BCBS</td>
<td>Authorization Missing</td>
<td>$12,850</td>
<td><button class="review">Review</button></td>
</tr>

<tr>
<td><span class="priority critical">Critical</span></td>
<td>A1002</td>
<td>Aetna</td>
<td>Filing Deadline</td>
<td>$6,750</td>
<td><button class="review">Review</button></td>
</tr>

<tr>
<td><span class="priority high">High</span></td>
<td>A1007</td>
<td>BCBS</td>
<td>Denied Claim</td>
<td>$9,700</td>
<td><button class="review">Review</button></td>
</tr>

<tr>
<td><span class="priority high">High</span></td>
<td>A1006</td>
<td>Humana</td>
<td>Authorization Pending</td>
<td>$8,200</td>
<td><button class="review">Review</button></td>
</tr>

</table>

</div>

</div>


<div id="auth" class="section">

<div class="card">

<h2>Prior Authorization Command Center</h2>

<div class="case">
A1001 — BCBS<br>
Authorization missing<br>
<strong>$12,850 at risk</strong>
</div>

<div class="case">
A1006 — Humana<br>
Authorization pending<br>
<strong>$8,200 at risk</strong>
</div>

<div class="case">
A1008 — Aetna<br>
Authorization pending<br>
<strong>$3,600 at risk</strong>
</div>

</div>

</div>


<div id="denials" class="section">

<div class="card">

<h2>Denial Recovery Center</h2>

<div class="case">
A1007 — BCBS<br>
Medical necessity denial<br>
<strong>$9,700 recovery opportunity</strong>
</div>

<div class="case">
A1003 — United Healthcare<br>
Denied claim requiring review<br>
<strong>$4,900 recovery opportunity</strong>
</div>

</div>

</div>


<div id="ai" class="section">

<div class="card">

<h2>Ask Clarity AI</h2>

<p>
Ask questions about your organization's revenue performance.
</p>

<div class="ask-row">

<input
id="question"
placeholder="Where are we losing the most money?">

<button onclick="askClarity()">
Ask
</button>

</div>

<div class="answer" id="answer">

Try asking:
“Where are we losing the most money?”
or
“What should we work first?”

</div>

</div>

</div>

</div>


<script>

function showSection(id, button) {

document.querySelectorAll('.section')
.forEach(section => section.classList.remove('active'));

document.getElementById(id)
.classList.add('active');

document.querySelectorAll('.nav button')
.forEach(btn => btn.classList.remove('active'));

button.classList.add('active');

}


function askClarity() {

let q =
document.getElementById('question')
.value.toLowerCase();

let answer =
document.getElementById('answer');

if (q.includes('denial')) {

answer.innerHTML =
"<strong>Denial analysis:</strong><br>" +
"$96,750 is currently associated with denied claims. " +
"Medical necessity and documentation are the largest drivers.";

}

else if (q.includes('authorization') || q.includes('auth')) {

answer.innerHTML =
"<strong>Prior authorization analysis:</strong><br>" +
"$81,400 is currently at risk. " +
"Start with cases that have upcoming service dates.";

}

else if (q.includes('first') || q.includes('priority')) {

answer.innerHTML =
"<strong>Highest priority:</strong><br>" +
"Account A1001 has $12,850 at risk because authorization is missing " +
"and the service is scheduled in 3 days.";

}

else {

answer.innerHTML =
"<strong>Revenue analysis:</strong><br>" +
"Total revenue currently at risk is $247,850. " +
"Prior authorization is the largest identified workflow opportunity.";

}

}

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return HTML

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
