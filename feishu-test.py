# -*- coding: utf-8 -*-
import requests


def push_report(web_hook):
    header = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    message_body = {
        "msg_type": "text",
        "content": {
            "text": "\n测试测试测试测试测试测试😀😀😀！！!\n"

        }

    }

    chatrob = requests.post(url=web_hook, json=message_body, headers=header)
    opener = chatrob.json()
    print("opener:{}".format(opener))
    if opener["StatusMessage"] == "success":
        print(u"%s 通知消息发送成功！" % opener)
    else:
        print(u"通知消息发送失败，原因：{}".format(opener))


if __name__ == '__main__':
    # 机器人webhook
    webhook = "https://open.feishu.cn/open-apis/bot/v2/hook/91c46241-a640-4534-9977-5c7f2ebec9a8"
    push_report(webhook)
