# -*- coding: utf8 -*-

import requests, time, random
import datetime


url='https://h5.xiaofubao.com/marketing/health/doDetail'

datanow=datetime.datetime.now()


def get_random_temprature():
    random.seed(datetime.time())
    return "{:.1f}".format(random.uniform(36.0, 36.8))
temperature=get_random_temprature()


headers={
    'Connection': '',
    'Accept': '',
    'X-Requested-With': '',
    'User-Agent': ' ',
    #上面的 Agent需要修改
    'Content-Type': '',
    'Referer': 'https://h5.xiaofubao.com/marketing/health/home.shtml?activityCode=health&unionid=########&schoolCode=########',
    #修改Referer
    'Accept-Language': 'zh-CN,en-US;q=0.9',
    'Cookie': '',
    #cookies 需要修改
    }
cookie={"Cookie": "",}

data={ #'id': '',
       'schoolCode': '',
       'schoolName': '',
       'identityType': '1',
       'userId': '',
       'mobilePhone': '',
       'name': '',
       'jobNo': '',
       'departmentCode': '',
       'department': '',
       'specialitiesCode': '',
       'specialities': '',
       'classCode': '',
       'className': '',
       'provinceCode': '',
       'province': '',
       'cityCode': '',
       'city': '',
       'inSchool': '1',
       'contactArea': '1',
       'isPatient': '1',
       'contactPatient': '1',
       'linkPhone': '',
       'parentsPhone': '',
       #'createTime': '2022-08-10 16:28:44',
       #'createDate': '2022-08-10 00:00:00',
       'updateTime':datanow,#别改
       'locationInfo': '',
       'longitudeAndLatitude': '',
       'isSuspected': '1',
       'healthStatusNew': '1',
       'identitySecondType': '',
       'districtCode': '',
       'district': '',
       'isFamiliyPatient': '1',
       'isCommunityPatient': '1',
       'isTodayBack': '1',
       'vaccineStatus': '3',
       'vaccineOneTime': '',
       'vaccineTwoTime': '',
       'vaccineThreeTime': '',
       'loginUserId': '',
       'ymId':'',
       'deviceId': '',
       'temperature': temperature,#别改
       'address': '',
       'sessionId': '',
       'loginUserId': '',
       'loginUserName': '',
       'loginSchoolCode': '',
       'loginSchoolName': '',
       'platform': 'YUNMA_APP'}

def handler(a,b):
    requests.packages.urllib3.disable_warnings()
    r=requests.post(url,headers=headers,data=data,cookies=cookie,verify=False).json()
    print(r)

