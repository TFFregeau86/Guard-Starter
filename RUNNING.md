Running Provenance Guard

This guide explains how to set up, run, and test the local Provenance Guard web service.

Requirements
Python installed on your computer.
Git Bash or another terminal.
The project repository downloaded locally.
Dependencies listed in requirements.txt.

The project uses a local GPT-2 model. The first model download is approximately 550 MB. No API key is required for the local detector.

First-Time Setup

Run these commands from the project directory in Git Bash:

bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
python test.py


If .venv already exists, you do not need to create it again. Activate it and run the environment check:

bash
source .venv/Scripts/activate
python test.py


In Windows PowerShell, activate the environment with:

powershell
.\.venv\Scripts\Activate.ps1


The environment is ready when python test.py passes.

Verified: The latest recorded environment check passed all nine checks, including Python, the virtual environment, dependencies, PyTorch, Flask, the detector model, and the service.

Start the Service

Use two terminals.

Terminal 1 — Run Flask

From the project directory, activate the virtual environment if necessary, then run:

bash
source .venv/Scripts/activate
python app.py


Leave this terminal open while making requests.

The service normally runs at:

text
http://127.0.0.1:5000

Terminal 2 — Send Requests

Open another terminal in the project directory. Activate the virtual environment:

bash
source .venv/Scripts/activate


Use this terminal to run the following tests while Flask remains running in Terminal 1.

Test the Service
1. Test /ping
bash
curl.exe -X POST http://127.0.0.1:5000/ping \
  -H "Content-Type: application/json" \
  -d "{\"message\":\"hello\"}"


Expected response:

json
{
  "ok": true,
  "service": "provenance-guard",
  "you_sent": "hello"
}


Verified: The endpoint returns HTTP 200 and the expected JSON response.

2. Check /health
bash
curl.exe http://127.0.0.1:5000/health


The response includes the detector model, whether it is loaded, whether rate limiting is enabled, and the number of audit log entries.

The detector may initially report "detector_loaded": false. The model is loaded when the detector is first used, so this alone does not indicate an error.

3. Submit Writing
bash
curl.exe -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"The rain fell softly on the empty street.\",\"creator_id\":\"writer-001\"}"


The working route returns a JSON response containing:

content_id
creator_id
guess
confidence
label
model_score
style_score
combined_score
text_length

The confidence field currently contains the combined score. It is not a calibrated probability that the classification is correct.

Verified: The submission route calls both detector.model_signal(text) and stylometry.style_signal(text), combines their scores, assigns a classification, creates a unique content ID, and records the decision.

The configured thresholds are:

Human: combined score from 0.00 to 0.35, inclusive.
Unsure: combined score greater than 0.35 and less than 0.65.
AI: combined score from 0.65 to 1.00, inclusive.

These classifications indicate heuristic writing patterns, not verified authorship.

4. Check the Audit Log
bash
curl.exe "http://127.0.0.1:5000/log?limit=5"


A successful submission should add an entry containing all nine required decision fields:

timestamp
content_id
creator_id
guess
model_score
style_score
combined_score
label
status

The initial decision status is decided.

The audit log also records rejected requests and appeals.

To display the configured audit-log path, run:

bash
python -c "import config; print(config.AUDIT_LOG)"


The audit writer creates the log directory and file when an entry is written.

5. Test an Appeal

First, submit writing using /submit and copy the actual content_id from its response.

Then run the following command, replacing the example ID with the ID returned by your submission:

bash
curl.exe -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d "{\"content_id\":\"PASTE_ACTUAL_CONTENT_ID_HERE\",\"reasoning\":\"I wrote this text myself and would like the decision reviewed.\"}"


Expected response for an existing decision:

json
{
  "content_id": "YOUR_ACTUAL_CONTENT_ID",
  "message": "Your appeal has been recorded. This submission is now under review.",
  "ok": true,
  "status": "under_review"
}


Replace the placeholder with the actual ID before running the command.

Verified: A valid appeal returned HTTP 200 and recorded an under_review audit entry. An appeal using a nonexistent content ID returned HTTP 404.

Appeals are appended to the audit log. They do not overwrite the original decision or automatically determine whether that decision was correct.

6. Test Input Validation

An empty text submission should be rejected:

bash
curl.exe -i -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"\",\"creator_id\":\"writer-001\"}"


A submission missing creator_id should also be rejected:

bash
curl.exe -i -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"A sample sentence.\"}"


Invalid JSON should be rejected:

bash
curl.exe -i -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d "not-json"


Expected behavior:

Empty or whitespace-only text returns HTTP 400 with invalid_text.
A missing or invalid creator ID returns HTTP 400 with invalid_creator_id.
Invalid JSON returns HTTP 400 with invalid_request.

Verified: These three rejection cases have been tested, and /ping continued to return HTTP 200 afterward.

The complete ten-case invalid-input evaluation remains to be documented.

7. Test the Scoring Module

Run:

bash
python scoring.py


This prints the label ranges, representative classification tests, and the signal-combination test.

To test representative scores directly:

bash
python -c "import scoring; print(scoring.score_to_label(0.20)); print(scoring.score_to_label(0.50)); print(scoring.score_to_label(0.80))"


To verify the human threshold boundary:

bash
python -c "import scoring; print(scoring.score_to_label(0.35)); print(scoring.score_to_label(0.34))"


Verified: The three representative score tests and both human-threshold boundary tests returned the expected classifications and reader-facing messages.

8. Test the Detector Independently

To score a sample directly from the terminal:

bash
python detector.py "The rain fell softly on the empty street."


To test the function used by the Flask route:

bash
python -c "import detector; print(detector.model_signal('The rain fell softly on the empty street.'))"


The first model use can take longer because the model must be loaded. Later requests are generally faster while the model remains loaded.

A warning about loss_type=None may appear from the installed model libraries. A warning alone does not indicate failure; check whether the detector returns a score and whether the request completes successfully.

Current Milestone Status
Implemented and Tested
Flask service starts locally.
/ping, /health, and /log respond.
/submit validates request data.
The GPT-2 detector produces a model score.
stylometry.style_signal(text) produces a style score.
scoring.combine_signals() combines the signals.
scoring.score_to_label() assigns classifications and reader-facing messages.
The configured label ranges and representative boundaries have been tested.
Successful submissions receive unique content IDs.
The audit log records decisions with all nine required fields.
Rejected requests are recorded in the audit log.
/appeal records valid appeals and marks them under_review.
Nonexistent content IDs are rejected for appeals.
The environment check passed all nine checks in the activated virtual environment.
Remaining Evaluation and Submission Work
Test ten known human-written samples and record the false-positive count.
Compare five human-written and five AI-generated samples using their mean combined scores.
Record a real submission classified as human; actual submissions have already demonstrated unsure and ai.
Complete and document the ten invalid-input tests.
Preserve the required evaluation evidence.
Confirm and complete the Git commits required by the assignment.

These are remaining evaluation and submission tasks, not missing core route implementations.

Troubleshooting
Symptom	What to check
Connection refused	Confirm python app.py is running in Terminal 1.
Connection reset	Check the Flask terminal for a traceback or unexpected process termination.
/ping works but /submit fails	Inspect the Flask terminal and verify the detector and stylometry functions.
Detector model is not loaded	Submit a test request or run python detector.py directly.
/log returns zero entries	Submit a request, then inspect the configured audit path.
Empty text is rejected	Expected behavior. Submit a non-empty string.
Missing creator ID is rejected	Expected behavior. Include a non-empty creator_id.
ModuleNotFoundError	Activate .venv and install dependencies with pip install -r requirements.txt.
Appeal returns 404	Check that the supplied content ID belongs to a successful submission.
Important

Keep the same repository for both course units. Commit your work regularly, and preserve the audit logs and evaluation results required by the assignment.

Provenance Guard is an experimental writing-pattern analysis service. Its classifications do not establish authorship, and the unsure result should be treated as a legitimate outcome rather than proof of misconduct.