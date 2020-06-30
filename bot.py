import telebot
import random
import sqlite3
from sqlite3 import Error
from time import sleep, ctime

ver = (2.5)
password = 'YOUR_PASSWORD_HERE'

print('started')

"""
    SQLITE
    FUNCTIONS
"""
def post_sql_query(sql_query):
    with sqlite3.connect('my.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(sql_query)
        except Error:
            pass
        result = cursor.fetchall()
        return result
def create_tables():
    users_query = '''CREATE TABLE IF NOT EXISTS USERS 
                        (user_id INTEGER PRIMARY KEY NOT NULL,
                        username TEXT,
                        first_name TEXT,
                        last_name TEXT,
                        reg_date TEXT);'''
    post_sql_query(users_query)
def register_user(user, username, first_name, last_name):
    user_check_query = f'SELECT * FROM USERS WHERE user_id = {user};'
    user_check_data = post_sql_query(user_check_query)
    if not user_check_data:
        insert_to_db_query = f'INSERT INTO USERS (user_id, username, first_name,  last_name, reg_date) VALUES ({user}, "{username}", "{first_name}", "{last_name}", "{ctime()}");'
        post_sql_query(insert_to_db_query )
        print('New user: '+username)

create_tables()

"""
    CARDS GENERATION
    CARDS GENERATION
    CARDS GENERATION
"""

with open('rules.txt','r',encoding="utf-8") as rules:
    rules = rules.read()

def cataclysm():
    with open('cataclysm.txt','r+', encoding="utf-8") as cataclysm_file:
        cataclysm_list = cataclysm_file.read()
        cataclysm_list = cataclysm_list.split('\n')
        cataclysm=((cataclysm_list[random.randint(0,((len(cataclysm_list))-1))])+('\n'*2)+
                   '👥Остаток выжившего населения: '+(str(random.randint(10,50))+'%')+'.'+'\n'+
                   '💥Разрушения на поверхности: '+(str(random.randint(20,80))+'%')+'.'+('\n'*2))
        return(cataclysm)
def shelter():
    with open('shelter1.txt','r', encoding="UTF-8") as shelter_file1:
        shelter_list1 = (shelter_file1.read()).split('\n')
    with open('shelter2.txt','r', encoding="UTF-8") as shelter_file2:
        shelter_list2 = (shelter_file2.read()).split('\n')
    with open('shelter3.txt','r', encoding="UTF-8") as shelter_file3:
        shelter_list3 = (shelter_file3.read()).split('\n')
    with open('shelter4.txt','r', encoding="UTF-8") as shelter_file4:
        shelter_list4 = (shelter_file4.read()).split('\n')
    with open('shelter5.txt','r', encoding="UTF-8") as shelter_file5:
        shelter_list5 = (shelter_file5.read()).split('\n')

    area = (str(random.randint(70,300)))   #Площадь убежища
    
    def shelter_staff(x):
        if x==1:
            shelter_staff1 = []
            for i in range(0,(random.randint(1,3))):
                shelter_staff1.append(shelter_list3[random.randint(0,((len(shelter_list3))-1))])
            shelter_staff1 = list(set(shelter_staff1))
            for i in range(0,(len(shelter_staff1))):
                shelter_staff1[i] = '🔧В убежище оборудовано: ' + shelter_staff1[i]
            shelter_staff1 = ('\n'.join(shelter_staff1))
            return(shelter_staff1)
        elif x==2:
            shelter_staff2 = []
            for i in range(0,(random.randint(1,3))):
                shelter_staff2.append(shelter_list4[random.randint(0,((len(shelter_list3))-1))])
            shelter_staff2 = list(set(shelter_staff2))
            for i in range(0,(len(shelter_staff2))):
                shelter_staff2[i] = '📦В убежище есть: ' + shelter_staff2[i]
            shelter_staff2 = ('\n'.join(shelter_staff2))
            return(shelter_staff2)

    shelter_info1 = ('('+(shelter_list1[random.randint(0,((len(shelter_list1))-1))])+')') #Еда и питье расчитаны на...
    shelter_info2 = (shelter_list2[random.randint(0,((len(shelter_list2))-1))]) #Описание убежища
    shelter_info3 = (shelter_staff(1))  #Оборудование убежища
    shelter_info4 = (shelter_staff(2))  #В убежище есть...
    shelter_info5 = ('♻В убежище живут: '+ shelter_list5[random.randint(0,((len(shelter_list5))-1))])        #В убежище живут...
    time_list = ['month','year']    #Время нахождения в убежище
    time_random = (time_list[random.randint(0,((len(time_list))-1))])
    if time_random == 'month':
        time = (random.randint(3,11))
        if time > 5:
            time = str(time)+' месяцев'
        else:
            time = str(time)+' месяца'
    elif time_random == 'year':
        time = (random.randint(1,10))
        if time == 1:
            time = str(time)+' год'
        elif time > 4:
            time = str(time)+' лет'
        else:
            time = str(time)+' года'
    shelter = ('🏡Площадь убежища: '+area+' квадратных метров'+('\n'*2)+
               '⌛Время нахождения в убежище '+shelter_info1 +':'+time+('\n'*2)+
               '🔓'+shelter_info2+('\n'*2)+
               shelter_info3+('\n'*2)+
               shelter_info4+('\n'*2)+
               shelter_info5)
    return(shelter)


def character():
    gender = ['Мужчина','Женщина']
    child = ['Не childfree','Childfree']
    body = ['Полный','Спортивный','Худощавый','Полноватый','Анорексия']
    height = 'Рост '+str(random.randint(165,195))
    with open('proffesion.txt','r', encoding="UTF-8") as proffesion:
        proffesion_list = (proffesion.read()).split('\n')
    with open('health.txt','r', encoding="UTF-8") as health:
        health_list = (health.read()).split('\n')
    with open('temper.txt','r', encoding="UTF-8") as temper:
        temper_list = (temper.read()).split('\n')
    with open('phobia.txt','r', encoding="UTF-8") as phobia:
        phobia_list = (phobia.read()).split('\n')
    with open('hobby.txt','r', encoding="UTF-8") as hobby:
        hobby_list = (hobby.read()).split('\n')
    with open('inform.txt','r', encoding="UTF-8") as inform:
        inform_list = (inform.read()).split('\n')
    with open('baggage.txt','r', encoding="UTF-8") as baggage:
        baggage_list = (baggage.read()).split('\n')
    with open('cards.txt','r', encoding="UTF-8") as cards:
        cards_list = (cards.read()).split('\n')
    age = str(random.randint(18,90))
    gender = gender[random.randint(0,1)]
    if gender == 'Женщина' and (int(age))>49:
        child = 'Childfree'
    else:
        child = ''.join(random.choices(['Не Childfree', 'Childfree'],[5,1]))
    character = ('💼Професcия: '+ proffesion_list[random.randint(0,(len(proffesion_list)-1))]+'\n'+
                 '👥Пол: '+ gender+'\n'+
                 '🧸Возраст: '+ age +'\n'+
                 '👶Деторождение: '+ child+'\n'+
                 '🧘Телосложение: '+ height+','+body[random.randint(0,(len(body)-1))]+'\n'+
                 '💖Здоровье: '+ health_list[random.randint(0,(len(health_list)-1))]+'\n'+
                 '👺Черта характера: '+ temper_list[random.randint(0,(len(temper_list)-1))]+'\n'+
                 '👻Фобия: '+phobia_list[random.randint(0,(len(phobia_list)-1))]+'\n'+
                 '🎣Хобби: '+hobby_list[random.randint(0,(len(hobby_list)-1))]+'\n'+
                 '📝Доп. информация: '+inform_list[random.randint(0,(len(inform_list)-1))]+'\n'+
                 '📦Багаж: '+baggage_list[random.randint(0,(len(baggage_list)-1))]+'\n'+
                 '🃏Карта 1: '+cards_list[random.randint(0,(len(cards_list)-1))]+'\n'+
                 '🃏Карта 2: '+cards_list[random.randint(0,(len(cards_list)-1))])
    return(character)

def use_prof():
    with open('proffesion.txt','r', encoding="UTF-8") as proffesion:
        proffesion_list = (proffesion.read()).split('\n')
    new_proffesion = ('💼Новая профессия: '+(proffesion_list[random.randint(0,(len(proffesion_list)-1))]))
    return(new_proffesion)
def use_health():
    with open('health.txt','r', encoding="UTF-8") as health:
        health_list = (health.read()).split('\n')
    new_health = ('💖Новое здоровье: '+(health_list[random.randint(0,(len(health_list)-1))]))
    return(new_health)
def use_phobia():
    with open('phobia.txt','r', encoding="UTF-8") as phobia:
        phobia_list = (phobia.read()).split('\n')
    new_phobia = ('👻Новая фобия: '+(phobia_list[random.randint(0,(len(phobia_list)-1))]))
    return(new_phobia)
"""
                Telegram-bot
                Telegram-bot
                Telegram-bot
"""
token = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'
bot = telebot.TeleBot(token)

print('Connected to bot')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Сгенерировать карту')
keyboard1.row('Правила','Помощь')
keyboard1.row('Поддержать')
#####KEYBOARD2#####
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('Сгенерировать катаклизм')
keyboard2.row('Сгенерировать персонажа')
keyboard2.row('Сгенерировать убежище')
keyboard2.row('Использовать карту профессии')
keyboard2.row('Использовать карту здоровья')
keyboard2.row('Использовать карту фобии')
keyboard2.row('Назад')

@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        register_user(message.from_user.id, message.from_user.username,
                      message.from_user.first_name, message.from_user.last_name)
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}. Удачных игр!', reply_markup=keyboard1)
    except:
        print('Error in start_message,chat id: '+message.chat.id)

@bot.message_handler(commands=['add_card'])
def add_card(message):
    msg = bot.reply_to(message, 'Enter password:')
    bot.register_next_step_handler(msg, auth)

def auth(message):
    answer = message.text
    if answer == password:
        msg = bot.send_message(message.chat.id,'Успешная авторизация!'+'\n'*2+

                                               'Card-list: baggage,cards,cataclysm,health,hobby,inform,phobia,proffession,temper'+'\n'*2+
                                               'Enter: card:text')
        bot.register_next_step_handler(msg, add_card2)
    else:
        bot.send_message(message.chat.id,'Неверный пароль')
def add_card2(message):
    answer = (message.text)
    answer = answer.split(':')
    answer[0] = answer[0]+'.txt'
    try:
        with open(answer[0],'r+',encoding ="UTF-8") as file:
            old_file = file.read()
            new_file = file.write(old_file+'\n'+answer[1])
            print('In '+answer[0]+' was added '+answer[1])
            bot.send_message(message.chat.id,'В файл '+answer[0]+' было добавлено '+answer[1], reply_markup=keyboard1)
    except:
         bot.send_message(message.chat.id,'Ошибка!Вы попытались записать в '+answer[0]+' "'+answer[1]+'"',reply_markup=keyboard1)
    
@bot.message_handler(content_types=['text'])
def send_text(message):
    try:
        if message.text.lower() == 'сгенерировать карту':
            bot.send_message(message.chat.id,'Выберите карту, которую хотите сгенерировать:', reply_markup=keyboard2)
        elif message.text.lower() == 'помощь':
            bot.send_message(message.chat.id,
            'Привет, этот бот предназначен для генерации катастроф, бункеров и ролей для игры с друзьями. Бот обновляется и пополняется новыми характеристиками с каждым днем. Если готов начать — нажимай "Сгенерировать карту".',reply_markup=keyboard1)
        elif message.text.lower() == 'сгенерировать катаклизм':
            bot.send_message(message.chat.id, cataclysm())
        elif message.text.lower() == 'сгенерировать персонажа':
            bot.send_message(message.chat.id, character())
        elif message.text.lower() == 'сгенерировать убежище':
            bot.send_message(message.chat.id, shelter())
        elif message.text.lower() == 'использовать карту профессии':
            bot.send_message(message.chat.id, use_prof())
        elif message.text.lower() == 'использовать карту здоровья':
            bot.send_message(message.chat.id, use_health())
        elif message.text.lower() == 'использовать карту фобии':
            bot.send_message(message.chat.id, use_phobia())
        elif message.text.lower() == 'правила':
            bot.send_message(message.chat.id, rules,reply_markup=keyboard1)
        elif message.text.lower() == 'поддержать':
            bot.send_message(message.chat.id,
                             'К сожалению, бот не может работать вечно и мы нуждаемся в материальной поддержке оплаты хостинга.'+'\n'+'Реквизиты:'+'\n'*2+'🥝Qiwi: qiwilink'+'\n'+' 💳Card: ----',
                             reply_markup=keyboard1)
        elif message.text.lower() == 'назад':
            bot.send_message(message.chat.id,'Выберите опцию:', reply_markup=keyboard1)
        else:
            bot.send_message(message.chat.id, 'Неизвестная команда')
    except:
        print('Error in send_text, chat id: '+message.chat.id)

bot.polling()
