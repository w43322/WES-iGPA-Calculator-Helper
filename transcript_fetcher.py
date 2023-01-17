import csv
import requests
from bs4 import BeautifulSoup

class TranscriptFetcher:
    def from_csv(self, path):
        with open(path) as file:
            return list(tuple(row) for row in csv.reader(file)) 

    def from_NEU(self, uname, pword):
        # webvpn
        # url = "https://webvpn.neu.edu.cn/http/77726476706e69737468656265737421a2a618d275613e1e275ec7f8/eams/teach/grade/course/person!historyCourseGrade.action?projectType=MAJOR"

        def get_data(txt, uname, pword):
            def get(txt, name):
                query_str = 'name="' + name + '" value="'
                start = txt.find(query_str) + len(query_str)
                end = txt.find('"', start)
                return txt[start:end]

            d = {
                "ul": "8",
                "pl": "16",
                "lt": get(txt, "lt"),
                "execution": get(txt, "execution"),
                "_eventId": get(txt, "_eventId")
            }
            d["rsa"] = uname + pword + d["lt"]
            
            return d

        s = requests.Session()
        r = s.get("http://219.216.96.4/eams/teach/grade/course/person!historyCourseGrade.action?projectType=MAJOR")
        r = s.post("https://pass.neu.edu.cn/tpass/login?service="
                   "http%3A%2F%2F219.216.96.4%2Feams%2Fteach%2Fgrade%2Fcourse"
                   "%2Fperson%21historyCourseGrade.action%3FprojectType%3DMAJOR", get_data(r.text, uname, pword))

        res = []
        soup = BeautifulSoup(r.text, features="html.parser")
        rows = soup.find("table").find("tbody").find_all("tr")

        for row in rows:
            cells = row.find_all("td")
            course_status = cells[-1].get_text().strip()
            if course_status != "正常":
                continue
            course_name = cells[3].get_text().strip()
            course_credit = cells[6].get_text().strip()
            course_gpa = str(int(10 * (float(cells[-2].get_text().strip()) + 5)))
            res.append((course_name, course_credit, course_gpa))
        
        return res

