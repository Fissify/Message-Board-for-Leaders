# Message Board for Leaders

中国领导留言板  
这是基于selenium进行信息抓取的程序，数据来源于中国人民网领导留言板：http://liuyan.people.com.cn/index  
本程序所获取的一切信息均为人民网所有，仅能用于学术交流等非商业活动！

****

｜作者｜于阳｜

****

## 程序使用指南

### 1.使用前的环境配置
  1.1由于本程序是基于python语言中的selenium模块进行编写的，因此在运行时需要借助webdriver。
本程序提供了运用edge、chrome、firefox的三种信息获取方法，可自行根据所用浏览器进行选择。  
具体操作步骤如下：  
第一、下载浏览器对应版本的webdriver。  
第二、建立一个新的文件夹（使用edge的将文件夹命名为edge，使用chrome的将文件夹命名为chrome，使用firefox的将文件命名为firefox），并把下载好的webdriver放入其中（edge浏览器的叫msedgedriver，chrome浏览器的叫chromedriver，firefox浏览器的叫geckodriver）。  
edge浏览器的webdriver下载地址：https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver  
chrome浏览器的webdriver下载地址：http://chromedriver.storage.googleapis.com/index.html  
Firefox浏览器的webdriver下载地址：https://github.com/mozilla/geckodriver/releases  
第三、解压文件后运行dist中的人民网领导留言板  

### 2.数据获取内容与存储
2.1本程序可以爬取中央部委领导的留言板数据与地方领导的留言板数据。中央数据只包括部委数据，地方数据包括省级数据与市区级数据。其中，中央数据只包含:留言对象、留言标题、留言时间、留言内容；省级和市级数据包含:留言对象、留言标题、留言类型、留言领域、留言状态、留言时间、留言内容、回复情况、回复单位、回复时间、回复内容、回复满意度。  
此外，程序在运行时会根据用户回答自动选择模块。


例一、爬取中央数据时:   
-"爬取中央留言板还是地方留言板？请输入'中央'或'地方'"  
-*"中央"*


例二、爬取北京市数据时:  
-"爬取中央留言板还是地方留言板？请输入'中央'或'地方'"  
-*"地方"*  
-"爬取什么层级的留言板？请输入'省级'或'市级'"  
-*"省级"*  
-"请输入想要爬取的省份、直辖市或自治区"  
-*"北京市"*


例三、爬取朝阳区数据时:  
-"爬取中央留言板还是地方留言板？请输入'中央'或'地方'"  
-*"地方"*  
-"爬取什么层级的留言板？请输入'省级'或'市级'"  
-*"市级"*  
-"请输入想要爬取城市所在的省份、直辖市或自治区"  
-*"北京市"*  
-"请输入想要爬取的城市或辖区"  
-*"朝阳区"*


2.2对于抓取下来的数据，程序将会根据用户操作系统进行自动存储。  
对于windows用户，程序将会在D盘自动生成城市留言板文件夹，并把抓取下来的数据以excel格式保存其中。  
对于mac用户，程序将会在用户文件夹中生成城市留言板文件，并把抓取下来的数据以excel格式保存其中。


2.3输入错误省份或城市将无法进行正常抓取。省份、直辖市、自治区、地级市与市辖区的正确名称如下:  
| 省份、直辖市、自治区 | 地级市、市辖区  |
| :------------: |---------------|
| 北京市  | 东城区、西城区、朝阳区、海淀区、丰台区、石景山区、门头沟区、房山区、通州区、顺义区、昌平区、大兴区、怀柔区、密云区、延庆区、平谷区、北京经济技术开发区 |
| 天津市  | 和平区、河北区、河东区、河西区、南开区、红桥区、滨海新区、东丽区、西青区、北辰区、津南区、武清区、宝坻区、蓟州区、静海区、宁河区     |
| 河北省 | 石家庄市、唐山市、秦皇岛市、邯郸市、邢台市、保定市、张家口市、承德市、沧州市、廊坊市、衡水市、雄安新区、定州市、辛集市      |
| 山西省 | 太原市、大同市、阳泉市、长治市、晋城市、朔州市、晋中市、运城市、忻州市、临汾市、吕梁市       |
| 内蒙古自治区 | 呼和浩特市、包头市、乌海市、赤峰市、通辽市、鄂尔多斯市、呼伦贝尔市、巴彦淖尔市、乌兰察布市、兴安盟、阿拉善盟、锡林郭勒盟      |
| 辽宁省 | 沈阳市、大连市、鞍山市、抚顺市、本溪市、丹东市、锦州市、营口市、阜新市、辽阳市、盘锦市、铁岭市、朝阳市、葫芦岛市        |
| 吉林省 | 长春市、吉林市、四平市、辽源市、通化市、白山市、松原市、白城市、延边朝鲜族自治州       |
| 黑龙江省 | 哈尔滨市、齐齐哈尔市、鸡西市、鹤岗市、双鸭山市、大庆市、伊春市、佳木斯市、七台河市、牡丹江市、黑河市、绥化市、大兴安岭地区   |
| 上海市 | 黄浦区、徐汇区、长宁区、静安区、普陀区、虹口区、杨浦区、宝山区、闵行区、嘉定区、浦东新区、松江区、金山区、青浦区、奉贤区、崇明区   |
| 江苏省 | 南京市、镇江市、常州市、无锡市、苏州市、扬州市、南通市、淮安市、徐州市、盐城市、泰州市、宿迁市、连云港市   |
| 浙江省| 杭州市、宁波市、温州市、嘉兴市、湖州市、绍兴市、金华市、衢州市、舟山市、台州市、丽水市  |
| 安徽省 | 合肥市、芜湖市、蚌埠市、淮南市、马鞍山市、淮北市、铜陵市、安庆市、黄山市、滁州市、阜阳市、宿州市、六安市、亳州市、池州市、宣城市 |
| 福建省 |福州市、厦门市、莆田市、三明市、泉州市、漳州市、南平市、龙岩市、宁德市、平潭综合实验区  |
| 江西省 | 南昌市、景德镇市、萍乡市、九江市、新余市、鹰潭市、赣州市、吉安市、宜春市、抚州市、上饶市 |
| 山东省 | 济南市、青岛市、淄博市、枣庄市、东营市、烟台市、潍坊市、济宁市、泰安市、威海市、日照市、临沂市、德州市、聊城市、滨州市、菏泽市|
| 河南省 | 郑州市、开封市、洛阳市、平顶山市、安阳市、鹤壁市、新乡市、焦作市、濮阳市、许昌市、漯河市、三门峡市、南阳市、商丘市、信阳市、周口市、驻马店市、济源产城融合示范区（济源市）、巩义市、兰考县、汝州市、滑县、长垣市、邓州市、永城市、固始县、鹿邑县、新蔡县 |
| 湖北省| 武汉市、黄石市、十堰市、宜昌市、襄阳市、鄂州市、荆门市、孝感市、荆州市、黄冈市、咸宁市、随州市、恩施土家族苗族自治州、仙桃市、天门市、潜江市、神农架林区 |
| 湖南省 | 长沙市、株洲市、湘潭市、衡阳市、邵阳市、岳阳市、常德市、张家界市、益阳市、郴州市、永州市、怀化市、娄底市、湘西土家族苗族自治州|
| 广东省| 广州市、韶关市、深圳市、珠海市、汕头市、佛山市、江门市、湛江市、茂名市、肇庆市、惠州市、梅州市、汕尾市、河源市、阳江市、清远市、东莞市、中山市、潮州市、揭阳市、云浮市|
| 广西壮族自治区| 南宁市、柳州市、桂林市、梧州市、北海市、防城港市、钦州市、贵港市、玉林市、百色市、贺州市、河池市、来宾市、崇左市 |
| 海南省 |海口市、三亚市、三沙市、儋州市、省辖县(县级市)|
| 重庆市| 两江新区、渝中区、大渡口区、江北区、沙坪坝区、九龙坡区、南岸区、北碚区、万盛经开区管委会、渝北区、万州区、涪陵区、黔江区、长寿区、巴南区、江津区、永川区、合川区、南川区、綦江区、潼南区、铜梁区、大足区、荣昌区、璧山区、梁平区、城口县、丰都县、垫江县、武隆区、忠县、开州区、云阳县、奉节县、巫山县、巫溪县、石柱土家族自治县、秀山土家族苗族自治县、酉阳土家族苗族自治县、彭水苗族土家族自治县、重庆高新区  |
| 四川省 | 成都市、自贡市、攀枝花市、泸州市、德阳市、绵阳市、广元市、遂宁市、内江市、乐山市、南充市、眉山市、宜宾市、广安市、达州市、雅安市、巴中市、资阳市、阿坝藏族羌族自治州、甘孜藏族自治州、凉山彝族自治州  |
| 贵州省 | 贵阳市、六盘水市、遵义市、安顺市、毕节市、铜仁市、黔东南苗族侗族自治州、黔南布依族苗族自治州、黔西南布依族苗族自治州、贵安新区  |
| 云南省 | 昆明市、曲靖市、玉溪市、保山市、昭通市、丽江市、普洱市、临沧市、楚雄彝族自治州、红河哈尼族彝族自治州、文山壮族苗族自治州、西双版纳傣族自治州、大理白族自治州、德宏傣族景颇族自治州、怒江傈僳族自治州、迪庆藏族自治州 |
| 西藏自治区 | 拉萨市、昌都市、山南市、日喀则市、那曲市、阿里地区、林芝市  |
| 陕西省 | 西安市、铜川市、宝鸡市、咸阳市、渭南市、延安市、汉中市、榆林市、安康市、商洛市、杨凌示范区、西咸新区|
| 甘肃省 | 兰州市、嘉峪关市、金昌市、白银市、天水市、武威市、张掖市、平凉市、酒泉市、庆阳市、定西市、陇南市、临夏回族自治州、甘南藏族自治州、兰州新区 |
| 青海省 | 西宁市、海东市、海北藏族自治州、黄南藏族自治州、海南藏族自治州、果洛藏族自治州、玉树藏族自治州、海西蒙古族藏族自治州|
| 宁夏回族自治区 | 银川市、石嘴山市、吴忠市、固原市、中卫市 |
| 新疆维吾尔自治区| 乌鲁木齐市、克拉玛依市、吐鲁番市、哈密市、昌吉回族自治州、博尔塔拉蒙古自治州、巴音郭楞蒙古自治州、阿克苏地区、克孜勒苏柯尔克孜自治州、喀什地区、和田地区、伊犁哈萨克自治州、塔城地区、阿勒泰地区 |


### 3.程序耗时与优化
3.1为了保证运行稳定性与不影响人民网的正常访问，本程序以单线程运行并在编写过程中加入了一定数量的sleep语法，数据爬取速度约为1000条/小时。如有速度要求，可同时运行edge版本、chrome版本、firefox版本的程序，手动进行多线程爬取。


3.2仓库已上传原始代码[原始代码](./message-board.py)，有需求可自行下载并进行优化。类似如留言板的动态网页均可以本代码为模板，进行适当调整。


3.3根据操作系统与所用浏览器类型，本仓库提供了六个程序。  
windows用户请下载:[edge浏览器](./winedge.zip)、[chrome浏览器](./winchrome.zip)、[firefox浏览器](./winfirefox.zip)  
mac用户请下载:[edge浏览器](/.macedge.zip)、[chrome浏览器](./macchrome.zip)、[firefox浏览器](./macfirefox.zip)

****

## 写在最后
当程序运行出现问题，大概率为网页元素无法查找而导致的信息报错，将程序关闭后重新运行即可解决。  
程序开发与代码编写均由本人独立完成，大概用了3天，写了1000行。本程序最主要的目的是方便论文写作和数据分析，减少不必要的复制粘贴的过程，若有帮助到您我将深感荣幸。  
再次声明：本程序仅用于学习和科研等非商业活动，不能用于谋利等非法行为，如有违反后果自负。  
最后，祝您使用愉快:blush:。
