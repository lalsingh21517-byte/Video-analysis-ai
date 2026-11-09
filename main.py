import os
import time
import uuid
from flask import Flask, request, jsonify
from google import genai

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024  # 50 MB

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
MODEL = "gemini-1.5-flash"

PROMPT = (
    "इस वीडियो को ध्यान से देखो और बताओ कि इसमें जो दावा किया गया है "
    "वह असली है या नकली/बढ़ा-चढ़ाकर बताया गया है। "
    "हिंदी में छोटा और साफ़ विश्लेषण दो।"
)

PAGE = """
<h3>वीडियो जाँच टेस्ट</h3>
<input type="file" id="v" accept="video/*"><br><br>
<button onclick="go()">जाँचो</button>
<pre id="out" style="white-space:pre-wrap"></pre>
<script>
async function go() {
  const f = document.getElementById('v').files[0];
  if (!f) return;
  const out = document.getElementById('out');
  out.textContent = 'जाँच चल रही है, इंतज़ार करें...';
  const fd = new FormData();
  fd.append('video', f);
  const r = await fetch('/analyze-video', {method: 'POST', body: fd});
  const j = await r.json();
  out.textContent = j.analysis || j.error;
}
</script>
"""


@app.route("/")
def home():
    return PAGE


@app.route("/analyze-video", methods=["POST"])
def analyze_video():
    if "video" not in request.files:
        return jsonify({"error": "वीडियो फ़ाइल ज़रूरी है"}), 400

    path = f"/tmp/{uuid.uuid4().hex}.mp4"
    request.files["video"].save(path)
    gfile = None
    try:
        gfile = client.files.upload(file=path)
        for _ in range(60):
            if gfile.state.name != "PROCESSING":
                break
            time.sleep(2)
            gfile = client.files.get(name=gfile.name)
        if gfile.state.name != "ACTIVE":
            return jsonify({"error": "वीडियो प्रोसेस नहीं हो पाई"}), 500

        resp = client.models.generate_content(
            model=MODEL, contents=[gfile, PROMPT]
        )
        return jsonify({"status": "success", "analysis": resp.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if os.path.exists(path):
            os.remove(path)
        if gfile is not None:
            try:
                client.files.delete(name=gfile.name)
            except Exception:
                pass


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
