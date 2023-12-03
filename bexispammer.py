import requests
import random
import time
import json
import os
os.system('title BEXİ DİSCORD WEBHOOK SPAMMER')
print("BEXİ DİSCORD WEBHOOK SPAMMER")   
done = 1
messages = ''
try:
    with open('messages.txt') as f:
        messages = f.read()
except:
    print('\u001b[0m\u001b[31m[\u001b[0m-\u001b[31m] Failed! \u001b[33m"messages.txt", txt dosyasi bulunamadi lütfen tekrar indirin!')
    os.system('title ERROR - Missing files! && PAUSE >nul')
    os._exit(0)

os.system('title Bexi Webhook Spammer - Enter webhook URL!')
webhook = input('\u001b[0m\u001b[32;1m[\u001b[0m?\u001b[32;1m] Başlatmak için, \u001b[0m\u001b[33mwebhook girin! \u001b[0m>>>\u001b[33m ')
hookInfo = requests.get(webhook)
if hookInfo.status_code == 401:
    print('\u001b[0m\u001b[31m[\u001b[0m-\u001b[31m] Hatali! \u001b[33mHatali webhook!')
    os.system('title ERROR - hatali webhook! && PAUSE >nul')
    os._exit(0)

hookName = hookInfo.json()['name']
os.system('title Bexi Webhook Spammer - Kaç Defa Spamlansin?')
times = input('\u001b[0m\u001b[32;1m[\u001b[0m?\u001b[32;1m] (Enter a NUMBER) \u001b[0m\u001b[33mKaç Defa Spamlansin? (1-100) \u001b[0m>>>\u001b[33m ') or 69
try:
    times = int(times)
except:
    print('\u001b[0m\u001b[31m[\u001b[0m-\u001b[31m] Hatali! \u001b[33mHatali sayi girdiniz! (1-100)')
    times = 100

os.system('title Bexi Webhook Spammer - Hazir')
print(f'\u001b[0m\u001b[32;1m[\u001b[0m+\u001b[32;1m] Hazir! \u001b[0m\u001b[33mWebhook Spamlanacak "{hookName}" {times} kere! (SPAMLAMAK İÇİN ENTER A BASİN!)\n\u001b[0m')
os.system('PAUSE >nul')
while done < times:
    tempMsg = random.choice(messages.splitlines())
    w = requests.post(webhook, json={'content':tempMsg})
    if w.status_code == 429:
        os.system(f'title Bexi Webhook Spammer - Error! (#{done})')
        print('\u001b[0m\u001b[31m[\u001b[0m-\u001b[31m] Hatali! \u001b[33mRatelimited! Bi kaç saniye bekleyin...')
        time.sleep(w.json()['retry_after']/1000 + 1)
    else:
        os.system(f'title Bexi Webhook Spammer - Spamlaniyor! ({done}kere)')
        print(f'\u001b[0m\u001b[32;1m[\u001b[0m+\u001b[32;1m] Başarili! \u001b[0m\u001b[33mSent message "{tempMsg}"! (#{done})\u001b[0m')
        done += 1
requests.delete(webhook)
print(f'\u001b[0m\u001b[32;1m[\u001b[0m+\u001b[32;1m] Başarili Şekilde Spamlandi! \u001b[0m\u001b[33mWebhook imha edildi!\u001b[0m')
os.system(f'title Bexi Webhook Spammer - Spamladiktan Sonra Silindi {done} kere!')
print(f'\u001b[0m\u001b[32;1m[\u001b[0m+\u001b[32;1m] Report: \u001b[0m\u001b[33mWebhook Spamlandi "{hookName}" {times} kere!\n\u001b[0m')
os.system('PAUSE >nul')
