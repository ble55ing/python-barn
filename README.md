# python-barn
[TOC]

### fenjuxxqg.py

实现对中文的分句和去重；

#### 中文分句

使用re库中的split方法，下面的使用方法分出来的是不包含这些符号的，如果将split的第一个参数大括号括起来，则会包含符号。

```
import re
sentences = re.split('（|）|、|。|，|：|！|\:|\,|\(|\.|\!|\"|\.|？|\?',lines)
#sentences = re.split('（（|）|、|。|，|：|！|\:|\,|\(|\.|\!|\"|\.|？|\?）',lines)
```

#### 中文去重

根据分句找到的句频，对中文文件中重复的句子进行去重（句子的格式是不一样的）

### xuexiqiangguo.py

使用selenium实现自动点击、换网页、浏览、删网页等操作。

#### 自动网页操作

```
dr = webdriver.Chrome(executable_path=r"D:\chromedriver.exe")
dr.get("login.html")
link = dr.find_elements_by_xpath("//span[@class='text']")
NowPage = dr.current_window_handle
AllPage = dr.window_handles
dr.switch_to_window(NowPage)
self.dr.execute_script('window.scrollTo(0, document.body.scrollHeight/3)')#下移滑块
dr.close()
```

### barn.py

各种小功能的实现

#### cmpstreq(str1,str2)

比较两个字符串前面相等的长度，返回值是长度i。

#### stringxor(str1,str2)

两字符串异或，返回结果字符串

#### sqrtt(n,e)

开次方根

### misc.py

各种在misc&crypto中出现的需要的功能实现

#### _crc32(v)

输入是字符串，返回值是字符串类型的crc32

####  Toqrcode(str,xlen,ylen)

将01字符串生成二维码，输入是字符串，x轴长度，y轴长度，输出qrcode.png

#### Tobarcode(str,xlen,ylen)

将01字符串生成一维码，输入是字符串，x轴长度，y轴长度，输出barcode.png

#### stringToMorseAlphabet(msg)

字符串转为摩斯码，用空格分离，返回

#### morseAlphabetToStringnonull(morseCode)

将没有空格的摩斯码按长度优先原则翻译，返回

#### morseAlphabetToString(morseCode)

将有空格的摩斯码进行翻译，返回结果字符串

### web1.py

以构造包的形式与网站交互

#### post，get网站交互

