from flask import render_template
from app import app
import spacy
from collections import defaultdict, Counter
from flask import request
from flask import render_template
from spacy.lang.ru.examples import sentences
from flask import jsonify
import array
import pickle
import pandas as pd

def length_component(doc):
    doc_length = len(doc)
    print(f"This document is {doc_length} tokens long.")
    return doc

nlp = spacy.load("ru_core_news_sm")
#nlp = spacy.load("en_core_web_sm")
#nlp.add_pipe(length_component, first=True)

#doc = nlp(sentences[0])
#doc = nlp('Привет, Долли, больше нет боли, ведь есть GENERVIS')
doc = nlp('Друзья и знакомые! Всех искренне приглашаю подписаться на наш с Дашли Рутюб канал https://rutube.ru/channel/25384128/, а также на мой оффициальный канал Meurch на рутюбе! https://rutube.ru/channel/26420086/ Учитывая, что на ютубе какие-то траблы с монетизацией, есть очень важная цель - набрать 5000 просмотров на рутюбе и подключить монетизацию. Это - как заработать 1200 рублей на Арбате, постояв полчаса и попев свои песни... Вроде мало - а приятно. Поэтому просьба всем подписаться на эти 2 канала и смотреть время от времени видосы, которые могут быть для Вас интересны и полезны в чем-то!')
words = [token.text
         for token in doc
         if not token.is_stop and not token.is_punct]

# noun tokens that arent stop words or punctuations
nouns = [token.text
         for token in doc
         if (not token.is_stop and
             not token.is_punct and
             token.pos_ == "NOUN")]

# five most common tokens
word_freq = Counter(words)
common_words = word_freq.most_common(5)

# five most common noun tokens
noun_freq = Counter(nouns)
common_nouns = noun_freq.most_common(5)

@app.route('/')
def home():
    a = 62
    b = 41
    return f'a is {a} and b is {copacopa}'

@app.route('/template', methods=['GET', 'POST'])
def template():
    if request.method == 'GET':
        userText = request.args.get('userText')
        #doc=nlp(userText)
    #return render_template('home.html', result=common_nouns, userText=userText)
    return '\n'.join(str(item) for item in common_nouns)
# allow both GET and POST requests


@app.route('/getanswer', methods=['GET', 'POST'])
def getanswer():
    if request.method == 'POST':
        userText = request.form.get('userText')
        if userText == "Зачем нужны ПТЭ?":
            answer = "Сигнальные приборы железнодорожного транспорта предназначены для обеспечения безопасности движения и эксплуатации железнодорожного транспорта, для четкой организации движения поездов и маневровой работы."
        elif userText == "Кто должен выполнять правила технической эксплуатации?":
            answer = "Эксплуатация верхнего строения пути  осуществляется при соблюдении следующих требований к верхнему строению пути: 1) зазор в стыке, находящемся на противоположном от изолирующего стыка конца рельса, должен быть не менее 3 мм; 2) при величине зазора более 35 мм с диаметром отверстий в рельсах 36 мм и величине зазора более 38 мм с диаметром отверстий в рельсах 40 мм движение закрывается; 3) при величинах зазоров, не соответствующих нормативным параметрам и не требующих закрытия движения до производства работ по их регулировке, допускаемые скорости поездов устанавливаются локальным нормативным актом владельца инфраструктуры (владельца железнодорожных путей необщего пользования) с обеспечением требований безопасности движения и эксплуатации железнодорожного транспорта; 4) при изломе одной стыковой накладки движение поездов прекращается; 5) расстояния между осями шпал должны соответствовать проектной (для вновь строящихся и реконструируемых линий), ремонтной или эксплуатационной документации; 6) отклонения от нормативных значений на главных железнодорожных путях общего и необщего пользования допускаются не более 80 мм при деревянных шпалах и не более 40 мм - при железобетонных шпалах."
        elif userText == "Где найти информацию о требованиях к видимым сигналам?":
            answer = "Видимость сигнальных огней выходных и маршрутных светофоров главных железнодорожных путей составляет не менее 400 м, выходных и маршрутных светофоров главных железнодорожных путей в кривых, боковых железнодорожных путей, горочных светофоров, пригласительных сигналов и маневровых светофоров - не менее 200 м, а показания маршрутных указателей - не менее 100 м"
        elif userText == "Где найти правила приема и отправления поездов?":
            answer = "Железнодорожные станции оборудуются устройствами железнодорожной автоматики и телемеханики, оборудование стрелок, входящих в маршруты приема и отправления поездов, зависимостью с входными, выходными и маршрутными светофорами"
        elif userText == "Какие обязанности у работников ЖД транспорта?":
            answer = "На железнодорожных станциях в зависимости от технологической потребности применяются устройства станционной радиосвязи, устройства двусторонней парковой связи (на основе радиосвязи, или громкоговорящей связи, или их сочетания), ремонтно-оперативная радиосвязь, беспроводная (радиосвязь) передачи данных для информационно-управляющих систем и другие виды технологической электросвязи."
        else:
            answer = 'Вопрос, конечно, интересный, но переформулируйте его понятнее'
        # Загрузка данных из файла output.xlsx
        #data1 = pd.read_excel('output.xlsx')       
        return render_template('getanswer.html', userText=userText, answer=answer)
    return '''
           <form method="POST">
               <div><label>Введите текст: <input type="text" name="userText"></label></div>
               <input type="submit" value="Submit">
           </form>'''


@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        userText = request.form.get('userText')
        framework = request.form.get('framework')
        doc=nlp(userText)
        words = [token.text
         for token in doc
         if not token.is_stop and not token.is_punct]
        # noun tokens that arent stop words or punctuations
        nouns = [token.text
         for token in doc
         if (not token.is_stop and
             not token.is_punct and
             token.pos_ == "NOUN")]
        word_freq = Counter(words)
        common_words = word_freq.most_common(16)
        noun_freq = Counter(nouns)
        common_nouns = noun_freq.most_common(16)
        a = [userText, common_nouns]
        return render_template('template_json.html', result=doc, common_nouns=a)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Введите текст: <input type="text" name="userText"></label></div>
               <div><label>Framework: <input type="text" name="framework"></label></div>
               <input type="submit" value="Submit">
           </form>'''
