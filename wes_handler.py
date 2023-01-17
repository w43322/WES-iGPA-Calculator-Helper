import requests

class WESHandler:
    def __init__(self, transcript, **kwargs):
        # constant info
        self.url = "https://applications.wes.org/igpa-calculator/igpa.asp"

        # personal info
        self.first_name = kwargs.get("first_name") if "first_name" in kwargs else "John"
        self.last_name = kwargs.get("last_name") if "last_name" in kwargs else "Doe"
        self.email_addr = kwargs.get("email_addr") if "email_addr" in kwargs else "john.doe@example.com"
        self.institution_name = kwargs.get("institution_name") if "institution_name" in kwargs else "Garyton University"
        self.degree_name = kwargs.get("degree_name") if "degree_name" in kwargs else "Bachlor of Science in Memeology"
        self.sem_years = kwargs.get("sem_years") if "sem_years" in kwargs else "4"

        # transcript
        self.transcript = transcript

        # proxy
        if "proxy_port" in kwargs:
            ip_addr = kwargs.get("proxy_ip") if "proxy_ip" in kwargs else "127.0.0.1"
            proxy_str = "http://" + ip_addr + ":" + kwargs.get("proxy_port")
            self.proxy = {
                "http": proxy_str,
                "https": proxy_str
            }
        else:
            self.proxy = {}
    

    def get_data_1(self):
        return {
            "frm_last_name": self.last_name,
            "frm_first_name": self.last_name,
            "frm_lst_ctry_residence": "42",
            "frm_email": self.email_addr,
            "frm_email2": self.email_addr,
            "hdnGoMain": "1"
        }
    
    
    def get_data_2(self):
        return {
            "ctry_holder": "42",
            "grad_holder": "20029",
            "sys_holder:": "Applicant",
            "semyear_holder": self.sem_years,
            "name_holder": self.degree_name,
            "inst_nm_holder": self.institution_name,
            "frm_stud_nm": self.degree_name,
            "frm_inst_nm": self.institution_name,
            "frm_lst_ctry": "42",
            "frm_lst_numyearsem": self.sem_years,
            "terms_ckbox": "on",
            "sub_btn_continue": "Continue"
        }
    

    def get_data_3(self):
        res = {
            "ctry_holder": "42",
            "grad_holder": "20029",
            "row_holder": str(len(self.transcript)),
            "sys_holder": "Applicant",
            "semyear_holder": self.sem_years,
            "name_holder": self.degree_name,
            "inst_nm_holder": self.institution_name,
            "sub_btn_getIgpa": "Calculate GPA"
        }
        for i, course in enumerate(self.transcript, 1):
            res["title" + str(i)] = course[0]
            res["credit" + str(i)] = course[1]
            res["grade" + str(i)] = course[2]
        return res
    

    def calculate_gpa(self):
        s = requests.Session()
        r = s.post(self.url, self.get_data_1(), proxies=self.proxy)
        r = s.post(self.url, self.get_data_2(), proxies=self.proxy)
        r = s.post(self.url, self.get_data_3(), proxies=self.proxy)
        f = open("result.html", "w")
        f.write(r.text)
        f.close()

