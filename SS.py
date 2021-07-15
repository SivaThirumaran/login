import time

def screenshot(d):
    folder = "C:\\New folder\\seleniumdata\\Logs\\screenshot"
    time_string = time.asctime().replace(":"," ")
    file_name = folder + time_string + ".png"
    d.save_screenshot(file_name)
