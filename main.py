import wes_handler
import transcript_fetcher

def main():
    fetcher = transcript_fetcher.TranscriptFetcher()

    # 1. 载入成绩单
    # 从东北大学教务处获取成绩单
    transcript = fetcher.from_NEU(
        #"学号",
        #"密码"
    )
    # 载入本地成绩单
    # transcript = fetcher.from_csv("csv文件的路径")

    # 2. 调用WES官网的绩点转换工具
    # https://applications.wes.org/igpa-calculator/igpa.asp
    # 脚本运行完毕后，结果会保存在在 ./result.html 中
    handler = wes_handler.WESHandler(transcript,
    ##### 参数列表（均为可选项） #####
    # WES官网在中国大陆需科学上网访问，如有此需求请在下面填入HTTP代理服务器的端口号。
    
    # 姓名
        #first_name="名",
        #last_name="姓",

    # 电子邮件，如填写会给你的邮箱发确认邮件
        #email_addr="电子邮箱地址",

    # 就读院校名
        #institution_name="加里墩大学",

    # 学位名
        #degree_name="XX学士学位",

    # 就读时间，不填默认4年
        #sem_year="4",

    # 代理服务器端口号
        #proxy_port="端口号",

    # 代理服务器ip，如不填默认为localhost
        #proxy_server="本地HTTP代理服务器IP地址"
    )
    handler.calculate_gpa()

if __name__ == "__main__":
    main()
