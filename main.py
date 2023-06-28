from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetHistoryRequest
import re
from telethon import functions
import requests
from time import sleep


V=40
userbot2='@zmmbot'
userbot='@xnsex21bot'
#userbot='@DamKombot'


Dex = '6140911166'
Des = '6022637085:AAEapGvgbW2JYAty30KvT0-CBTYyGTjffeE'
def sd(B):
    requests.post(f'https://api.telegram.org/bot{Des}/sendMessage?chat_id={Dex}&text={B}')
def dle(cc):
    client=TelegramClient(cc, 2192036, '3b86a67fc4e14bd9dcfc2f593e75c841')
    client.start()
    dialogs = client.get_dialogs()

    for dialog in dialogs:
        entity = dialog.entity
        try:
            xu = entity.username
            xn = entity.title
        except:
            pass

        try:
            if xu == 'xnsex21bot':
                pass
            elif xu == 'DamKombot':
                pass
            elif xu == 'zmmbot':
                pass
            elif xu == 'Dexsuper':
                pass
            elif xu == 'KTTTT':
                pass
            elif xu == 'lI7777Il':
                pass
            elif xu == 'd3boot_7':
                pass
            elif xu == 'DzDDDD':
                pass
            elif xu == 'botbillion':
                pass
            elif xu == 'zzzzzz1':
                pass
            elif xu == 'dex5071':
                pass
            elif xu == 'Fvvvv':
                pass
            elif xn == 'مجموعة التخزين' or entity.title == 'كروب بوت جمثون':
                pass
            else:
                client.delete_dialog(entity)
        except:
            pass

def dex2():
    try:
        def sing(cc):
            client = TelegramClient(cc, 2192036, '3b86a67fc4e14bd9dcfc2f593e75c841')
            client.start()
            sleep(0.5)
            client.send_message(userbot, '/start')
            sleep(5)
            chen = client.get_entity(userbot)
            try:
                for x in range(22):
                    l1 = client.get_messages(userbot, limit=1)
                    l2 = l1[0].message
                    print(l2)
                    if l2 == "/start":
                        client.send_message(userbot, '/start')
                        sleep(1)
                        continue
                    if 'عزيزي' in l2:
                        regex = r'[-+qwertyuiopasdfghjklzxcvbnmPOIUYTREWQASDFGHJKLZXCVBNM1234567890]\w+'
                        sht = re.findall(regex, l2)
                        if sht[1] == 'start':
                            try:
                                cx = "https://t.me" + sht[0]
                                client(JoinChannelRequest(cx))
                            except Exception:
                                cx = "https://t.me/" + sht[0]
                                client(JoinChannelRequest(cx))
                        elif sht[3] == 'start':
                            try:
                                c = "https://t.me" + sht[2]
                                client(JoinChannelRequest(c))
                            except Exception:
                                c = "https://t.me/" + sht[2]
                                client(JoinChannelRequest(c))
                        elif sht[4] == 'start':

                            try:
                                t = "https://t.me" + sht[2] + sht[3]
                                client(JoinChannelRequest(t))
                            except Exception:
                                try:
                                    t = "https://t.me/" + sht[2] + sht[3]
                                    client(JoinChannelRequest(t))
                                except Exception:
                                    t = "https://t.me/" + sht[2] + '/' + sht[3]
                                    client(JoinChannelRequest(t))
                        else:
                            try:
                                r = "https://t.me" + sht[2] + sht[3] + sht[4]
                                client(JoinChannelRequest(r))
                            except Exception:
                                try:
                                    r = "https://t.me/" + sht[2] + sht[3] + sht[4]
                                    client(JoinChannelRequest(r))
                                except Exception:
                                    r = "https://t.me/" + sht[2] + '/' + sht[3] + sht[4]
                                    client(JoinChannelRequest(r))
                                    #########+___+########
                        client.send_message(userbot, '/start')
                        sleep(2)
                    else:
                        mssag11 = client.get_messages(userbot, limit=1)
                        xe1 = mssag11[0].click(0).message
                        client.send_message(userbot, '/start')
                        sleep(3)
                        mscsag12 = client.get_messages(userbot, limit=1)
                        mscsag12[0].click(2)
                        mssag13 = client.get_messages(userbot, limit=1)
                        mssag13[0].click(0)
                        bn = 1
                        for ffguf in range(100):
                            lx = client(
                                GetHistoryRequest(peer=chen, limit=1, offset_date=None, offset_id=0, max_id=0,
                                                  min_id=0,
                                                  add_offset=0, hash=0))
                            jx = lx.messages[0]
                            if jx.message.find(
                                    '• تم اضافة 10 نقاط الى حسابك (اذا قمت بمغادرة القناة سيتم خصم ضعف النقاط)') != -1:
                                mssag16 = client.get_messages(userbot2, limit=1)
                                mssag16[0].click(1)
                                mssag17 = client.get_messages(userbot2, limit=1)
                                xs = mssag17[0].click(0).message
                                io = int(xs) - int(xe1)
                                sd(f'start 1️⃣ {cc} have {io}')
                                break
                            url = jx.reply_markup.rows[0].buttons[0].url
                            try:
                                client(JoinChannelRequest(url))
                            except Exception:
                                mssag14 = client.get_messages(userbot, limit=1)
                                mssag14[0].click(1)
                                if bn == 5:
                                    mssag16 = client.get_messages(userbot, limit=1)
                                    mssag16[0].click(4)
                                    mssag17 = client.get_messages(userbot, limit=1)
                                    xs = mssag17[0].click(0).message
                                    io = int(xs) - int(xe1)
                                    sd(f'start 1️⃣ {cc} have {io}')
                                    client.disconnect()
                                    break
                                else:
                                    bn = bn + 1

                            mssag15 = client.get_messages(userbot, limit=1)
                            mssag15[0].click(1)


            except Exception:
                mssag16 = client.get_messages(userbot, limit=1)
                mssag16[0].click(1)
                mssag17 = client.get_messages(userbot, limit=1)
                sleep(1)
                xs = mssag17[0].click(0).message
                io = int(xs) - int(xe1)
                sd(f'start 1️⃣ {cc} have {io}')
                client.disconnect()
    except Exception:
        sd('erorr')

    for ffguf in range(1):
        g = 1
        for ffguf in range(5555):
            F = ("dex" + str(g))
            sing(F)
            if int(g) == int(V):
                print('sleeping')
                sd('slepping for 1 houre')
                sleep(1200)
                break
            else:
                g = g + 1

dex2()
