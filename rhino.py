from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

class ScrollBar:
    def __init__(self, name):
        self.name = name
        self.value = 5
        self.color = self.get_color()
        self.timestamp = datetime.now().strftime("%I:%M %p")

    def get_color(self):
        # Calculate the color based on the value
        red = min(int((self.value / 10) * 255), 255)
        blue = min(int(((10 - self.value) / 10) * 255), 255)
        return f"rgb({red}, 0, {blue})"

scroll_bars = {
    "first": ScrollBar("first"),
    "second": ScrollBar("second")
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        bar = request.form["bar"]
        value = int(request.form["value"])
        scroll_bars[bar].value = value
        scroll_bars[bar].color = scroll_bars[bar].get_color()
        scroll_bars[bar].timestamp = datetime.now().strftime("%I:%M %p")
        if scroll_bars["first"].value == 10 and scroll_bars["second"].value == 10:
            return render_template("text_box.html")
    return render_template("index.html", scroll_bars=scroll_bars)

if __name__ == "__main__":
    app.run(debug=True)
