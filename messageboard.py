from time import sleep
import xlwt
import datetime
import os
import sys
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def my_fuction():
    print("正在配置环境，请耐心等待......")
    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["pageLoadStrategy"] = "none"
    chrome_options = Options()
    options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automat on'])
    chrome_options.add_argument('--headless')
    s = Service("chrome/chromedriver")
    bro = webdriver.Chrome(service=s, options=chrome_options)
    bro.maximize_window()
    bro.implicitly_wait(1)
    datalists = []
    print("环境配置结束")

    bro.get('http://liuyan.people.com.cn/index')
    sleep(2)

    website = input("爬取中央留言板还是地方留言板？请输入'中央'或'地方'")

    if website == "中央":
        def centre():
            leader = bro.find_elements(By.XPATH, '//ul[@class="leadersul"]/li')

            print("正在爬取，请耐心等待......")
            sleep(1)

            for item in range(len(leader)):
                link = leader[item].find_element(By.XPATH, "./div/button[1]")
                bro.execute_script('arguments[0].click()', link)
                sleep(1)

                while True:
                    try:
                        load = bro.find_element(By.XPATH, "//div[@class='mordList']")
                        bro.execute_script('arguments[0].click()', load)
                        sleep(0.2)
                    except:
                        break

                sleep(1)
                itemlist = bro.find_elements(By.XPATH, "//ul[@class='replyList']/li")
                for content in itemlist:
                    windows = bro.window_handles
                    bro.switch_to.window(windows[0])
                    sleep(1)
                    datalist = []
                    content_link = content.find_element(By.XPATH, './div/h1')
                    bro.execute_script('arguments[0].click()', content_link)
                    windows = bro.window_handles
                    bro.switch_to.window(windows[-1])
                    sleep(2)

                    try:
                        object = bro.find_element(By.XPATH, '//div[@class="replyObject fl"]/span').text
                    except:
                        object = "无"

                    try:
                        title = bro.find_element(By.XPATH, '//h1[@class="fl"]').text
                    except:
                        title = "无"

                    try:
                        time = bro.find_element(By.XPATH, '//li[@class="replyMsg"]/span[2]').text
                    except:
                        time = "无"

                    try:
                        main = bro.find_element(By.XPATH, '//p[@id="replyContentMain"]').text
                    except:
                        main = "无"

                    datalist.append(object)
                    datalist.append(title)
                    datalist.append(time)
                    datalist.append(main)

                    bro.close()

                    datalists.append(datalist)

                windows = bro.window_handles
                bro.switch_to.window(windows[0])
                sleep(1)
                back = bro.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div[2]/div/div[1]/p')
                bro.execute_script('arguments[0].click()', back)
                sleep(1)
                leader = bro.find_elements(By.XPATH, '//ul[@class="leadersul"]/li')
                sleep(1)
                print("已经爬取" + str((item + 1) / len(leader) * 100) + "%")

            bro.close()
            bro.quit()

            def saveToexcel(savepath, datalists):
                workbook = xlwt.Workbook(encoding="utf-8")
                worksheet = workbook.add_sheet("sheet1", cell_overwrite_ok=True)
                name_sheet = ("留言对象", "留言标题", "留言时间", "留言内容")
                for i in range(len(name_sheet)):
                    worksheet.write(0, i, name_sheet[i])

                for i in range(len(datalists)):
                    li = datalists[i]

                    for j in range(len(li)):
                        worksheet.write(i + 1, j, li[j])
                workbook.save(savepath)

            def path_file():
                nowday = str(datetime.datetime.now()).replace(":", "-")[:10]
                borad_name = input("请输入留言板数据的文件名")
                file_name = borad_name + nowday + ".xls"
                saveToexcel(file_name, datalists)
                filepath = r"城市留言板"
                if not os.path.exists(filepath):
                    print(filepath + "文件夹不存在，正在创建.....")
                    os.makedirs(filepath)
                    print(filepath + "文件夹创建成功")
                target_path = filepath
                aa = os.getcwd()
                file_path = os.path.join(aa, file_name)
                try:
                    shutil.move(file_path, target_path)
                except:
                    print(file_name + "的数据已存在！")
                    print("文件已存在！")
                    ask = input("是否重新出入文件名？请输入是或否")
                    if ask == "是":
                        path_file()
                    if ask == "否":
                        sys.exit()
                    else:
                        path_file()

        centre()

    if website == "地方":
        def local():
            website_click = bro.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div[2]/div[1]/div[1]/div[2]")
            bro.execute_script('arguments[0].click()', website_click)
            sleep(2)

            rank = input("爬取什么层级的留言板？请输入'省级'或'市级'")

            if rank == "省级":
                def major_leader():
                    bro.find_element(By.XPATH,
                                     '/html/body/div[1]/div[2]/main/div/div/div[2]/div[1]/div[3]/div[2]/div[1]/div/span').click()
                    province = input("请输入想要爬取的省份、直辖市或自治区")
                    sleep(1)
                    try:
                        link_province = bro.find_element(By.XPATH, f'//span[text()= "{format(province)}"]')
                        bro.execute_script('arguments[0].click()', link_province)
                        sleep(1)
                    except:
                        print("输入错误，请重新输入")
                        sleep(0.1)
                        major_leader()
                    leader = bro.find_elements(By.XPATH, '//ul[@class="leadersul"]/li')

                    print("正在爬取，请耐心等待......")
                    sleep(1)

                    for item in range(len(leader)):
                        link = leader[item].find_element(By.XPATH, "./div[2]/button[1]")
                        bro.execute_script('arguments[0].click()', link)
                        sleep(1)

                        while True:
                            try:
                                load = bro.find_element(By.XPATH, "//div[@class='mordList']")
                                bro.execute_script('arguments[0].click()', load)
                                sleep(0.2)
                            except:
                                break
                        sleep(1)

                        itemlist = bro.find_elements(By.XPATH, "//ul[@class='replyList']/li")
                        for content in itemlist:
                            windows = bro.window_handles
                            bro.switch_to.window(windows[0])
                            sleep(1)
                            datalist = []
                            content_link = content.find_element(By.XPATH, './div/h1')
                            bro.execute_script('arguments[0].click()', content_link)
                            windows = bro.window_handles
                            bro.switch_to.window(windows[-1])
                            sleep(2)

                            try:
                                object = bro.find_element(By.XPATH, '//div[@class="replyObject fl"]/span').text
                            except:
                                object = "无"

                            try:
                                title = bro.find_element(By.XPATH, '//h1[@class="fl"]').text
                            except:
                                title = "无"

                            try:
                                typename = bro.find_element(By.XPATH, '//p[@class="typeNameD"]').text
                            except:
                                typename = "无"

                            try:
                                domain = bro.find_element(By.XPATH, '//p[@class="domainName"]').text
                            except:
                                domain = "无"

                            try:
                                state = bro.find_element(By.XPATH, '//p[@class="stateInfo"]').text
                            except:
                                state = "无"

                            try:
                                time = bro.find_element(By.XPATH, '//li[@class="replyMsg"]/span[2]').text
                            except:
                                time = "无"

                            try:
                                main = bro.find_element(By.XPATH, '//p[@id="replyContentMain"]').text
                            except:
                                main = "无"

                            try:
                                reply = bro.find_element(By.XPATH, '//div[@id="mainContainerDetail1"]/h3').text
                            except:
                                reply = "无"

                            try:
                                handle = bro.find_element(By.XPATH, '//div[@class="replyHandleMain fl"]/div/h4').text
                            except:
                                handle = "无"

                            try:
                                replytime = bro.find_element(By.XPATH,
                                                             '//div[@class="replyHandleMain fl"]/div/div[@class="handleTime"]').text
                            except:
                                replytime = "无"

                            try:
                                replycontent = bro.find_element(By.XPATH,
                                                                '//div[@class="replyHandleMain fl"]/div/p[@class="handleContent noWrap sitText"]').text
                            except:
                                replycontent = "无"

                            try:
                                replysatisfy = bro.find_element(By.XPATH, '//h4[@class="satisfied"]').text
                            except:
                                replysatisfy = "无"

                            datalist.append(object)
                            datalist.append(title)
                            datalist.append(typename)
                            datalist.append(domain)
                            datalist.append(state)
                            datalist.append(time)
                            datalist.append(main)
                            datalist.append(reply)
                            datalist.append(handle)
                            datalist.append(replytime)
                            datalist.append(replycontent)
                            datalist.append(replysatisfy)

                            bro.close()

                            datalists.append(datalist)

                        windows = bro.window_handles
                        bro.switch_to.window(windows[0])
                        sleep(1)

                        type_button2 = bro.find_element(By.XPATH, '//div[@role="tablist"]/div[3]')
                        bro.execute_script('arguments[0].click()', type_button2)

                        sleep(1)

                        while True:
                            try:
                                load = bro.find_element(By.XPATH, "//div[@class='mordList']")
                                bro.execute_script('arguments[0].click()', load)
                                sleep(0.2)
                            except:
                                break

                        sleep(1)

                        itemlist = bro.find_elements(By.XPATH, "//ul[@class='replyList']/li")
                        for content in itemlist:
                            windows = bro.window_handles
                            bro.switch_to.window(windows[0])
                            sleep(1)
                            datalist = []
                            content_link = content.find_element(By.XPATH, './div/h1')
                            bro.execute_script('arguments[0].click()', content_link)
                            windows = bro.window_handles
                            bro.switch_to.window(windows[-1])
                            sleep(2)

                            try:
                                object = bro.find_element(By.XPATH, '//div[@class="replyObject fl"]/span').text
                            except:
                                object = "无"

                            try:
                                title = bro.find_element(By.XPATH, '//h1[@class="fl"]').text
                            except:
                                title = "无"

                            try:
                                typename = bro.find_element(By.XPATH, '//p[@class="typeNameD"]').text
                            except:
                                typename = "无"

                            try:
                                domain = bro.find_element(By.XPATH, '//p[@class="domainName"]').text
                            except:
                                domain = "无"

                            try:
                                state = bro.find_element(By.XPATH, '//p[@class="stateInfo"]').text
                            except:
                                state = "无"

                            try:
                                time = bro.find_element(By.XPATH, '//li[@class="replyMsg"]/span[2]').text
                            except:
                                time = "无"

                            try:
                                main = bro.find_element(By.XPATH, '//p[@id="replyContentMain"]').text
                            except:
                                main = "无"

                            try:
                                reply = bro.find_element(By.XPATH, '//div[@id="mainContainerDetail1"]/h3').text
                            except:
                                reply = "无"

                            try:
                                handle = bro.find_element(By.XPATH, '//div[@class="replyHandleMain fl"]/div/h4').text
                            except:
                                handle = "无"

                            try:
                                replytime = bro.find_element(By.XPATH,
                                                             '//div[@class="replyHandleMain fl"]/div/div[@class="handleTime"]').text
                            except:
                                replytime = "无"

                            try:
                                replycontent = bro.find_element(By.XPATH,
                                                                '//div[@class="replyHandleMain fl"]/div/p[@class="handleContent noWrap sitText"]').text
                            except:
                                replycontent = "无"

                            try:
                                replysatisfy = bro.find_element(By.XPATH, '//h4[@class="satisfied"]').text
                            except:
                                replysatisfy = "无"

                            datalist.append(object)
                            datalist.append(title)
                            datalist.append(typename)
                            datalist.append(domain)
                            datalist.append(state)
                            datalist.append(time)
                            datalist.append(main)
                            datalist.append(reply)
                            datalist.append(handle)
                            datalist.append(replytime)
                            datalist.append(replycontent)
                            datalist.append(replysatisfy)

                            bro.close()

                            datalists.append(datalist)

                        sleep(1)

                        type_button3 = bro.find_element(By.XPATH, '//div[@role="tablist"]/div[4]')
                        bro.execute_script('arguments[0].click()', type_button3)

                        sleep(1)

                        while True:
                            try:
                                load = bro.find_element(By.XPATH, "//div[@class='mordList']")
                                bro.execute_script('arguments[0].click()', load)
                                sleep(0.2)
                            except:
                                break

                        windows = bro.window_handles
                        bro.switch_to.window(windows[0])
                        sleep(1)

                        itemlist = bro.find_elements(By.XPATH, "//ul[@class='replyList']/li")
                        for content in itemlist:
                            windows = bro.window_handles
                            bro.switch_to.window(windows[0])
                            sleep(1)
                            datalist = []
                            content_link = content.find_element(By.XPATH, './div/h1')
                            bro.execute_script('arguments[0].click()', content_link)
                            windows = bro.window_handles
                            bro.switch_to.window(windows[-1])
                            sleep(2)

                            try:
                                object = bro.find_element(By.XPATH, '//div[@class="replyObject fl"]/span').text
                            except:
                                object = "无"

                            try:
                                title = bro.find_element(By.XPATH, '//h1[@class="fl"]').text
                            except:
                                title = "无"

                            try:
                                typename = bro.find_element(By.XPATH, '//p[@class="typeNameD"]').text
                            except:
                                typename = "无"

                            try:
                                domain = bro.find_element(By.XPATH, '//p[@class="domainName"]').text
                            except:
                                domain = "无"

                            try:
                                state = bro.find_element(By.XPATH, '//p[@class="stateInfo"]').text
                            except:
                                state = "无"

                            try:
                                time = bro.find_element(By.XPATH, '//li[@class="replyMsg"]/span[2]').text
                            except:
                                time = "无"

                            try:
                                main = bro.find_element(By.XPATH, '//p[@id="replyContentMain"]').text
                            except:
                                main = "无"

                            try:
                                reply = bro.find_element(By.XPATH, '//div[@id="mainContainerDetail1"]/h3').text
                            except:
                                reply = "无"

                            try:
                                handle = bro.find_element(By.XPATH, '//div[@class="replyHandleMain fl"]/div/h4').text
                            except:
                                handle = "无"

                            try:
                                replytime = bro.find_element(By.XPATH,
                                                             '//div[@class="replyHandleMain fl"]/div/div[@class="handleTime"]').text
                            except:
                                replytime = "无"

                            try:
                                replycontent = bro.find_element(By.XPATH,
                                                                '//div[@class="replyHandleMain fl"]/div/p[@class="handleContent noWrap sitText"]').text
                            except:
                                replycontent = "无"

                            try:
                                replysatisfy = bro.find_element(By.XPATH, '//h4[@class="satisfied"]').text
                            except:
                                replysatisfy = "无"

                            datalist.append(object)
                            datalist.append(title)
                            datalist.append(typename)
                            datalist.append(domain)
                            datalist.append(state)
                            datalist.append(time)
                            datalist.append(main)
                            datalist.append(reply)
                            datalist.append(handle)
                            datalist.append(replytime)
                            datalist.append(replycontent)
                            datalist.append(replysatisfy)

                            bro.close()

                            datalists.append(datalist)

                        sleep(1)

                        windows = bro.window_handles
                        bro.switch_to.window(windows[0])
                        sleep(1)
                        back = bro.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div[2]/div/div[1]/h2/span[1]')
                        bro.execute_script('arguments[0].click()', back)
                        sleep(1)
                        leader = bro.find_elements(By.XPATH, '//ul[@class="leadersul"]/li')
                        sleep(1)
                        print("已经爬取" + str((item + 1) / len(leader) * 100) + "%")

                    bro.close()
                    bro.quit()

                    def saveToexcel(savepath, datalists):
                        workbook = xlwt.Workbook(encoding="utf-8")
                        worksheet = workbook.add_sheet("sheet1", cell_overwrite_ok=True)
                        name_sheet = (
                            "留言对象", "留言标题", "留言类型", "留言领域", "留言状态", "留言时间", "留言内容", "回复情况", "回复单位", "回复时间", "回复内容", "回复满意度")
                        for i in range(len(name_sheet)):
                            worksheet.write(0, i, name_sheet[i])

                        for i in range(len(datalists)):
                            li = datalists[i]

                            for j in range(len(li)):
                                worksheet.write(i + 1, j, li[j])
                        workbook.save(savepath)

                    def path_file():
                        nowday = str(datetime.datetime.now()).replace(":", "-")[:10]
                        borad_name = input("请输入留言板数据的文件名")
                        file_name = borad_name + nowday + ".xls"
                        saveToexcel(file_name, datalists)
                        filepath = r"城市留言板"
                        if not os.path.exists(filepath):
                            print(filepath + "文件夹不存在，正在创建.....")
                            os.makedirs(filepath)
                            print(filepath + "文件夹创建成功")
                        target_path = filepath
                        aa = os.getcwd()
                        file_path = os.path.join(aa, file_name)
                        try:
                            shutil.move(file_path, target_path)
                        except:
                            print(file_name + "的数据已存在！")
                            print("文件已存在！")
                            ask = input("是否重新出入文件名？请输入'是'或'否'")
                            if ask == "是":
                                path_file()
                            if ask == "否":
                                sys.exit()
                            else:
                                path_file()

                major_leader()

            if rank == "市级":
                def minor_leader():
                    province = input("请输入想要爬取城市所在的省份、直辖市或自治区")
                    bro.find_element(By.XPATH,
                                     '/html/body/div[1]/div[2]/main/div/div/div[2]/div[1]/div[3]/div[2]/div[1]/div/input').click()
                    sleep(1)

                    try:
                        link_province = bro.find_element(By.XPATH, f'//span[text()= "{format(province)}"]')
                        bro.execute_script('arguments[0].click()', link_province)
                        sleep(1)
                    except:
                        print("输入错误，请重新输入")
                        sleep(0.1)
                        minor_leader()
                    bro.find_element(By.XPATH,
                                     '/html/body/div[1]/div[2]/main/div/div/div[2]/div[1]/div[3]/div[2]/div[2]/div/input').click()

                    city = input("请输入想要爬取的城市或辖区")
                    try:
                        link_city = bro.find_element(By.XPATH, f'//span[text()= "{format(city)}"]')
                        bro.execute_script('arguments[0].click()', link_city)
                        sleep(1)
                    except:
                        print("输入错误，请重新输入")
                        sleep(0.1)
                        minor_leader()
                    leader = bro.find_elements(By.XPATH, '//ul[@class="leadersul"]/li')

                    print("正在爬取，请耐心等待......")
                    sleep(1)

                    for item in range(len(leader)):
                        link = leader[item].find_element(By.XPATH, "./div[2]/button[1]")
                        bro.execute_script('arguments[0].click()', link)
                        sleep(1)

                        while True:
                            try:
                                load = bro.find_element(By.XPATH, "//div[@class='mordList']")
                                bro.execute_script('arguments[0].click()', load)
                                sleep(0.2)
                            except:
                                break
                        sleep(1)

                        itemlist = bro.find_elements(By.XPATH, "//ul[@class='replyList']/li")

                        for content in itemlist:
                            windows = bro.window_handles
                            bro.switch_to.window(windows[0])
                            sleep(1)
                            datalist = []
                            content_link = content.find_element(By.XPATH, './div/h1')
                            bro.execute_script('arguments[0].click()', content_link)
                            windows = bro.window_handles
                            bro.switch_to.window(windows[-1])
                            sleep(2)

                            try:
                                object = bro.find_element(By.XPATH, '//div[@class="replyObject fl"]/span').text
                            except:
                                object = "无"

                            try:
                                title = bro.find_element(By.XPATH, '//h1[@class="fl"]').text
                            except:
                                title = "无"

                            try:
                                typename = bro.find_element(By.XPATH, '//p[@class="typeNameD"]').text
                            except:
                                typename = "无"

                            try:
                                domain = bro.find_element(By.XPATH, '//p[@class="domainName"]').text
                            except:
                                domain = "无"

                            try:
                                state = bro.find_element(By.XPATH, '//p[@class="stateInfo"]').text
                            except:
                                state = "无"

                            try:
                                time = bro.find_element(By.XPATH, '//li[@class="replyMsg"]/span[2]').text
                            except:
                                time = "无"

                            try:
                                main = bro.find_element(By.XPATH, '//p[@id="replyContentMain"]').text
                            except:
                                main = "无"

                            try:
                                reply = bro.find_element(By.XPATH, '//div[@id="mainContainerDetail1"]/h3').text
                            except:
                                reply = "无"

                            try:
                                handle = bro.find_element(By.XPATH, '//div[@class="replyHandleMain fl"]/div/h4').text
                            except:
                                handle = "无"

                            try:
                                replytime = bro.find_element(By.XPATH,
                                                             '//div[@class="replyHandleMain fl"]/div/div[@class="handleTime"]').text
                            except:
                                replytime = "无"

                            try:
                                replycontent = bro.find_element(By.XPATH,
                                                                '//div[@class="replyHandleMain fl"]/div/p[@class="handleContent noWrap sitText"]').text
                            except:
                                replycontent = "无"

                            try:
                                replysatisfy = bro.find_element(By.XPATH, '//h4[@class="satisfied"]').text
                            except:
                                replysatisfy = "无"

                            datalist.append(object)
                            datalist.append(title)
                            datalist.append(typename)
                            datalist.append(domain)
                            datalist.append(state)
                            datalist.append(time)
                            datalist.append(main)
                            datalist.append(reply)
                            datalist.append(handle)
                            datalist.append(replytime)
                            datalist.append(replycontent)
                            datalist.append(replysatisfy)

                            bro.close()

                            datalists.append(datalist)

                        windows = bro.window_handles
                        bro.switch_to.window(windows[0])
                        sleep(1)

                        type_button2 = bro.find_element(By.XPATH, '//div[@role="tablist"]/div[3]')
                        bro.execute_script('arguments[0].click()', type_button2)

                        sleep(1)

                        while True:
                            try:
                                load = bro.find_element(By.XPATH, "//div[@class='mordList']")
                                bro.execute_script('arguments[0].click()', load)
                                sleep(0.2)
                            except:
                                break

                        sleep(1)

                        itemlist = bro.find_elements(By.XPATH, "//ul[@class='replyList']/li")
                        for content in itemlist:
                            windows = bro.window_handles
                            bro.switch_to.window(windows[0])
                            sleep(1)
                            datalist = []
                            content_link = content.find_element(By.XPATH, './div/h1')
                            bro.execute_script('arguments[0].click()', content_link)
                            windows = bro.window_handles
                            bro.switch_to.window(windows[-1])
                            sleep(2)

                            try:
                                object = bro.find_element(By.XPATH, '//div[@class="replyObject fl"]/span').text
                            except:
                                object = "无"

                            try:
                                title = bro.find_element(By.XPATH, '//h1[@class="fl"]').text
                            except:
                                title = "无"

                            try:
                                typename = bro.find_element(By.XPATH, '//p[@class="typeNameD"]').text
                            except:
                                typename = "无"

                            try:
                                domain = bro.find_element(By.XPATH, '//p[@class="domainName"]').text
                            except:
                                domain = "无"

                            try:
                                state = bro.find_element(By.XPATH, '//p[@class="stateInfo"]').text
                            except:
                                state = "无"

                            try:
                                time = bro.find_element(By.XPATH, '//li[@class="replyMsg"]/span[2]').text
                            except:
                                time = "无"

                            try:
                                main = bro.find_element(By.XPATH, '//p[@id="replyContentMain"]').text
                            except:
                                main = "无"

                            try:
                                reply = bro.find_element(By.XPATH, '//div[@id="mainContainerDetail1"]/h3').text
                            except:
                                reply = "无"

                            try:
                                handle = bro.find_element(By.XPATH, '//div[@class="replyHandleMain fl"]/div/h4').text
                            except:
                                handle = "无"

                            try:
                                replytime = bro.find_element(By.XPATH,
                                                             '//div[@class="replyHandleMain fl"]/div/div[@class="handleTime"]').text
                            except:
                                replytime = "无"

                            try:
                                replycontent = bro.find_element(By.XPATH,
                                                                '//div[@class="replyHandleMain fl"]/div/p[@class="handleContent noWrap sitText"]').text
                            except:
                                replycontent = "无"

                            try:
                                replysatisfy = bro.find_element(By.XPATH, '//h4[@class="satisfied"]').text
                            except:
                                replysatisfy = "无"

                            datalist.append(object)
                            datalist.append(title)
                            datalist.append(typename)
                            datalist.append(domain)
                            datalist.append(state)
                            datalist.append(time)
                            datalist.append(main)
                            datalist.append(reply)
                            datalist.append(handle)
                            datalist.append(replytime)
                            datalist.append(replycontent)
                            datalist.append(replysatisfy)

                            bro.close()

                            datalists.append(datalist)

                        windows = bro.window_handles
                        bro.switch_to.window(windows[0])
                        sleep(1)

                        type_button3 = bro.find_element(By.XPATH, '//div[@role="tablist"]/div[4]')
                        bro.execute_script('arguments[0].click()', type_button3)

                        sleep(1)

                        while True:
                            try:
                                load = bro.find_element(By.XPATH, "//div[@class='mordList']")
                                bro.execute_script('arguments[0].click()', load)
                                sleep(0.2)
                            except:
                                break

                        sleep(1)

                        itemlist = bro.find_elements(By.XPATH, "//ul[@class='replyList']/li")
                        for content in itemlist:
                            windows = bro.window_handles
                            bro.switch_to.window(windows[0])
                            sleep(1)
                            datalist = []
                            content_link = content.find_element(By.XPATH, './div/h1')
                            bro.execute_script('arguments[0].click()', content_link)
                            windows = bro.window_handles
                            bro.switch_to.window(windows[-1])
                            sleep(2)

                            try:
                                object = bro.find_element(By.XPATH, '//div[@class="replyObject fl"]/span').text
                            except:
                                object = "无"

                            try:
                                title = bro.find_element(By.XPATH, '//h1[@class="fl"]').text
                            except:
                                title = "无"

                            try:
                                typename = bro.find_element(By.XPATH, '//p[@class="typeNameD"]').text
                            except:
                                typename = "无"

                            try:
                                domain = bro.find_element(By.XPATH, '//p[@class="domainName"]').text
                            except:
                                domain = "无"

                            try:
                                state = bro.find_element(By.XPATH, '//p[@class="stateInfo"]').text
                            except:
                                state = "无"

                            try:
                                time = bro.find_element(By.XPATH, '//li[@class="replyMsg"]/span[2]').text
                            except:
                                time = "无"

                            try:
                                main = bro.find_element(By.XPATH, '//p[@id="replyContentMain"]').text
                            except:
                                main = "无"

                            try:
                                reply = bro.find_element(By.XPATH, '//div[@id="mainContainerDetail1"]/h3').text
                            except:
                                reply = "无"

                            try:
                                handle = bro.find_element(By.XPATH, '//div[@class="replyHandleMain fl"]/div/h4').text
                            except:
                                handle = "无"

                            try:
                                replytime = bro.find_element(By.XPATH,
                                                             '//div[@class="replyHandleMain fl"]/div/div[@class="handleTime"]').text
                            except:
                                replytime = "无"

                            try:
                                replycontent = bro.find_element(By.XPATH,
                                                                '//div[@class="replyHandleMain fl"]/div/p[@class="handleContent noWrap sitText"]').text
                            except:
                                replycontent = "无"

                            try:
                                replysatisfy = bro.find_element(By.XPATH, '//h4[@class="satisfied"]').text
                            except:
                                replysatisfy = "无"

                            datalist.append(object)
                            datalist.append(title)
                            datalist.append(typename)
                            datalist.append(domain)
                            datalist.append(state)
                            datalist.append(time)
                            datalist.append(main)
                            datalist.append(reply)
                            datalist.append(handle)
                            datalist.append(replytime)
                            datalist.append(replycontent)
                            datalist.append(replysatisfy)

                            bro.close()

                            datalists.append(datalist)

                        sleep(1)

                        windows = bro.window_handles
                        bro.switch_to.window(windows[0])
                        sleep(1)
                        back = bro.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div[2]/div/div[1]/h2/span[2]')
                        bro.execute_script('arguments[0].click()', back)
                        sleep(1)
                        leader = bro.find_elements(By.XPATH, '//ul[@class="leadersul"]/li')
                        sleep(1)
                        print("已经爬取" + str((item + 1) / len(leader) * 100) + "%")

                    bro.close()
                    bro.quit()

                    def saveToexcel(savepath, datalists):
                        workbook = xlwt.Workbook(encoding="utf-8")
                        worksheet = workbook.add_sheet("sheet1", cell_overwrite_ok=True)
                        name_sheet = (
                        "留言对象", "留言标题", "留言类型", "留言领域", "留言状态", "留言时间", "留言内容", "回复情况", "回复单位", "回复时间", "回复内容", "回复满意度")
                        for i in range(len(name_sheet)):
                            worksheet.write(0, i, name_sheet[i])

                        for i in range(len(datalists)):
                            li = datalists[i]

                            for j in range(len(li)):
                                worksheet.write(i + 1, j, li[j])
                        workbook.save(savepath)

                    def path_file():
                        nowday = str(datetime.datetime.now()).replace(":", "-")[:10]
                        borad_name = input("请输入留言板数据的文件名")
                        file_name = borad_name + nowday + ".xls"
                        saveToexcel(file_name, datalists)
                        filepath = r"城市留言板"
                        if not os.path.exists(filepath):
                            print(filepath + "文件夹不存在，正在创建.....")
                            os.makedirs(filepath)
                            print(filepath + "文件夹创建成功")
                        target_path = filepath
                        aa = os.getcwd()
                        file_path = os.path.join(aa, file_name)
                        try:
                            shutil.move(file_path, target_path)
                        except:
                            print(file_name + "的数据已存在！")
                            print("文件已存在！")
                            ask = input("是否重新出入文件名？请输入'是'或'否'")
                            if ask == "是":
                                path_file()
                            if ask == "否":
                                sys.exit()
                            else:
                                path_file()

                    path_file()

                minor_leader()

            else:
                print("输入错误，请重新输入")
                sleep(0.1)
                local()
        local()

    else:
        print("输入错误，请重新输入")
        sleep(0.1)
        my_fuction()

    def loop_fuction():
        ask = input("是否需要继续爬取留言板数据？请输入'是'或'否'")
        if ask == "是":
            print("程序将在5秒后重启，请耐心等待......")
            sleep(5)
            my_fuction()
        if ask == "否":
            sys.exit()
        else:
            loop_fuction()

    loop_fuction()

my_fuction()