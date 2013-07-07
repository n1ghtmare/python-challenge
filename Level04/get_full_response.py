import requests

def get_full_response(param):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    for i in range(400):
        res = requests.get(url + str(param)).text
        segments = res.split(' ')
        param = segments[len(segments) - 1]
        print "Current iteration: " + str(i) + " | Response: " + res + " | Next parameter: " + str(param)

if __name__ == "__main__":
    print get_full_response("8022")