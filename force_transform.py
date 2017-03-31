#强制图片类型转换
import requests
url="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1488606334478&di=eb69f332ff58c07f8d1377d42533c47f&imgtype=0&src=http%3A%2F%2Fimg3.duitang.com%2Fuploads%2Fitem%2F201503%2F18%2F20150318224439_Qykfu.jpeg"
r=requests.get(url)
r.status_code
