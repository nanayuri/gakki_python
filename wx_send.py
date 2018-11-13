from wxpy import *

bot = Bot(cache_path=True)


def send_message(mes):
    print()
    my_friend = bot.friends().search(u'gakki-bot')[0]
    my_friend.send(mes)


if __name__ == '__main__':
    send_message('执行成功')