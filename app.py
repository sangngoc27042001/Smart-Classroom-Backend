from flask import Flask
import threading
import time

app = Flask(__name__)
count=0
def thread_function(t):
    global count
    while True:
        time.sleep(t)
        count+=2
        print(f"OK {count}")


@app.route("/")
def index():
    return "Hello"

if __name__=="__main__":
    main_thread = threading.Thread(target=thread_function, args=(2,))
    main_thread.start()
    app.run(debug=True)