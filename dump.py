'''
# DASHBOARD
def on_button_6_click():
    print("button_6 clicked")
    window.destroy()

# MAIN BUTTONS
def on_button_5_click():
    print("button_5 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "ProfilePage.py"], shell=True)
    process.wait()

def on_button_7_click():
    print("button_7 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "ViewEstab.py"], shell=True)
    process.wait()

def on_button_8_click():
    print("button_8 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "ViewFood.py"], shell=True)
    process.wait()

def on_button_4_click():
    print("button_4 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "ViewReview.py"], shell=True)
    process.wait()

# BACK

def on_button_3_click():
    print("button_3 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "ViewReview.py"], shell=True)
    process.wait()

'''

# DASHBOARD