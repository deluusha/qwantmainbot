from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher  # отслеживание сообщений от пользователя
from aiogram.utils import executor
import markups as nav
import information

TOKEN = '5465375647:AAEPTkq8lk1s4GOFwR5fiwBeuXOUBDob644'
PORT = int(os.environ.get('PORT', '8443'))

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

text111 = 'Родителям важно сформировать у ребенка способности самостоятельно принимать информированные решения, ' \
          'связанные с их ребенком, а также навыков развития у ребенка умения слушать, понимать речь и говорить с ' \
          'помощью слуховых аппаратов и кохлеарных имплантов, прежде всего, в повседневных ситуациях и во время ' \
          'совместных игр. Тажк родителям очень важно всегда находиться рядом с ребенком, не оставлять его одного. ' \
          'Нужно показывать свою любовь мимикой и различными действиями, чтобы ребенок это видел и осознал, ' \
          'что он нужен семье\n\nСоветуем заглянуть на наш сайт, там вы найдете больше полезной информации и ресурсов\nhttps://special-c.web.app'
text112 = 'Для детей неспособных слышать и с другими ограничениями мы создали сайт, который поможет Вам в обучении и ' \
          'воспитании ребенка, также там имеется вся необходимая информация о гос. программах для поддержки детей и ' \
          'другая полезная информация\n\nhttps://special-c.web.app/learning'
text121 = '• Учите малыша понимать простые фразы и требования слухозрительно в сопровождении с жестом. Используйте ' \
          'выразительные мимику, голос, жесты,поощряя правильные («Молодец», «Хорошо», «Красиво») и осуждая ' \
          'неправильные действия ребенка («Ай-яяй», «Нельзя»). Чем быстрее малыш начнет понимать мимику, ' \
          'речь слухозрительно и на слух, тем меньше он будет нуждаться в непрерывных действиях, чтобы знакомиться с ' \
          'окружающими предметами и общаться с людьми.\n\n• Регулируйте режим дня и тщательно его придерживайтесь. ' \
          'Распорядок, повторяясь день за днем, помогает ребенку понять, что происходит и что ему нужно делать в ' \
          'определенное время. Это уменьшает его беспокойство.\n\n• Успокаивайте ребенка вечером — успокаивающая ' \
          'теплая ' \
          'ванна, стакан теплого молока с ванилью, успокаивающая музыка, пробежка вокруг дома (для старших ' \
          'детей).\n\n• Подумайте, не предъявляете ли вы к ребенку противоречивые требования? Ссоры между родителями, ' \
          'избалованность, ревность к брату или сестре может быть причиной такого поведения.\n\n• Используйте ' \
          'двигательную активность в «мирных» целях. Например, ребенок не хочет убирать игрушки — сделайте из этого ' \
          'соревнование «Кто быстрее и больше уберет игрушек».\n\n• Играйте с ребенком в подвижные игры. Особенно ' \
          'хорош ' \
          'гимнастический комплекс — шведская стенка, качели и пр. Это позволит малышу использовать энергию для ' \
          'развития крупной моторики, координации движений, что ему так необходимо.\n\nСоветуем заглянуть на наш сайт, там вы найдете больше полезной информации и ресурсов\nhttps://special-c.web.app'
text122 = 'Для плохослышащих детей и детей с другими ограничениями мы создали сайт, который поможет Вам в обучении и ' \
          'воспитании ребенка, также там имеется вся необходимая информация о гос. программах для поддержки детей и ' \
          'другая полезная информация\n\nhttps://special-c.web.app/learning'

text211 = 'Нужно общаться со слепым ребёнком и согласованно взаимодействовать с ним, учитывая особенности его ' \
          'восприятия. Также важно научиться способам сопровождения при перемещениях в пространстве и таким приемам ' \
          'помощи слепому ребенку, чтобы своими действиями не ограничивать его самостоятельности. Общаться со слепым ' \
          'ребенком следует на близком расстоянии лицом к лицу. Начинать беседу следует с обращения к ребенку по ' \
          'имени. Убедитесь, что ребенок понял ваше намерение: он стоит к вам лицом, слушает вас, не отворачивается и ' \
          'не отходит. Разговаривайте с ребёнком не слишком громко, ваша речь должна быть выразительной, чёткой, ' \
          'неторопливой. Необходимо предупреждать ребенка о своих намерениях или своем приближении\n\nСоветуем заглянуть на наш сайт, там вы найдете больше полезной информации и ресурсов\nhttps://special-c.web.app'
text212 = 'Для слепых детей и детей с другими ограничениями мы создали сайт, который поможет Вам в обучении и ' \
          'воспитании ребенка, также там имеется вся необходимая информация о гос. программах для поддержки детей и ' \
          'другая полезная информация\n\nhttps://special-c.web.app/learning'
text221 = 'Первостепенной задачей родителей является поддержка ребенка, важно вдохновлять его на лечение, ' \
          'чаще разговаривать и проявлять заботу, чтобы ребенок чувствовал себя любимым и нужным. Чаще ' \
          'прислушивайтесь к требованиям ребенка.\n\nСоветуем заглянуть на наш сайт, там вы найдете больше полезной информации и ресурсов\nhttps://special-c.web.app'
text222 = 'Для слабовидящих детей и детей с другими ограничениями мы создали сайт, который поможет Вам в обучении и ' \
          'воспитании ребенка, также там имеется вся необходимая информация о гос. программах для поддержки детей и ' \
          'другая полезная информация\n\nhttps://special-c.web.app/learning'

text311 = 'Детям рекомендована индивидуальная поддержка и подход, поскольку немота в таком возрасте сильно ' \
          'опосредуется окружающим миром. Если ребенок не глухой, то нужно чаще разговаривать с ним. Но нужно ' \
          'учитывать, что не всегда немой ребеок согласен идти на контакт, поэтому нужно узнать, не против ли он.\n\nСоветуем заглянуть на наш сайт, там вы найдете больше полезной информации и ресурсов\nhttps://special-c.web.app'
text312 = 'Для немых детей и детей с другими ограничениями мы создали сайт, который поможет Вам в обучении и ' \
          'воспитании ребенка, также там имеется вся необходимая информация о гос. программах для поддержки детей и ' \
          'другая полезная информация\n\nhttps://special-c.web.app/learning'
text321 = '• Контролируйте собственную речь, обращая внимание на употребляемую лексику и грамматическое оформление. ' \
          'Говорить нужно четко, внятно, проговаривая каждое слово, фразу.\n\n• Озвучивайте любую ситуацию – но ' \
          'только, ' \
          'если Вы видите, что ребенок Вас слышит и видит. Не надо говорить в пустоту, надо смотреть ребенку прямо в ' \
          'глаза. Необходимо, чтобы ребенок видел вашу артикуляцию.\n\n• Употребляйте больше коротких фраз, старайтесь '\
          'четко излагать свои мысли, избегая длинных сложных фраз, которые будут непонятны ребенку.\n\n• Принимайте и '\
          'поддерживайте желание ребенка вступить с Вами в контакт. Если ребенок вообще не говорит – вовлекайте его в '\
          'любые формы диалога, одобряя любой ответ (жест, вырази тельный взгляд).\n\n• Расширяйте словарный запас ' \
          'ребенка ' \
          '(при помощи чтения книг, специальных упражнений).\n\n• Развивайте мелкую моторику рук. Используйте для этой '\
          'цели все многообразие игр и упражнений: игры с мелкими предметами (крупы, пуговицы, прищепки, лепка, ' \
          'рисование (по точкам, штриховка, пальчиковое рисование, лабиринты, пальчиковые игры и пальчиковый театр, ' \
          'шнуровки и т. д. Это поможет развитию речи, а в будущем – письму.\n\n• Читайте как можно больше ребенку ' \
          'коротких стихов и сказок. Перечитывайте их много раз – не бойтесь, что это надоест ребенку, т. к. дети ' \
          'гораздо лучше воспринимают тексты, которые они много раз слышали.\n\n• Ребенка необходимо побуждать к речи. '\
          'Отвечайте на вопросы детей. Поощряйте любопытство, стремление задавать вопросы.\n\nСоветуем заглянуть на наш сайт, там вы найдете больше полезной информации и ресурсов\nhttps://special-c.web.app'
text322 = 'Для плохоговорящих детей и детей с другими ограничениями мы создали сайт, который поможет Вам в обучении и '\
          'воспитании ребенка, также там имеется вся необходимая информация о гос. программах для поддержки детей и ' \
          'другая полезная информация\n\nhttps://special-c.web.app/learning'

text411 = 'Огромный вклад в развитие и оказание полноценной помощи ребенку оказывает окружающая среда, настрой и ' \
          'отношение ближайшего окружения и формирующееся в данных условиях психологическое состояние ребенка. Важна ' \
          'психологическая поддержка ребенка: коррекция и профилактика психических отклонений и нарушений, ' \
          'подготовка к школе, социальная адаптация, работа психолога с членами семьи.\n\nСоветуем заглянуть на наш сайт, там вы найдете больше полезной информации и ресурсов\nhttps://special-c.web.app'
text412 = 'Для детей с нарушениями опорно-двигательного аппарата и детей с другими ограничениями мы создали сайт, ' \
          'который поможет Вам в обучении и ' \
          'воспитании ребенка, также там имеется вся необходимая информация о гос. программах для поддержки детей и ' \
          'другая полезная информация\n\nhttps://special-c.web.app/learning'
text421 = 'Важнейшим этапом в системе помощи детям с нарушениями опорно-двигательного аппарата и возможныхиных ' \
          'сопутствующих отклонениях является комплексный подход к реабилитации ребенка – а именно, сочетание ' \
          'медикаментозного лечения и создания положительного эмоционального фона. Основной целью работы педагогов (а '\
          'также родителей или опекунов) является формирование осознания ребенком своей полноценности как члена ' \
          'общества. Задачей ближайшего окружения ребенка, таким образом, становится выявление его способностей и ' \
          'талантов, областей, в которых потенциально ребенок может самореализоваться, чувствуя себя при этом ' \
          'самодостаточным и нужным в обществе.\n\nСоветуем заглянуть на наш сайт, там вы найдете больше полезной информации и ресурсов\nhttps://special-c.web.app'
text422 = 'Для детей с нарушениями опорно-двигательного аппарата и детей с другими ограничениями мы создали сайт, ' \
          'который поможет Вам в обучении и ' \
          'воспитании ребенка, также там имеется вся необходимая информация о гос. программах для поддержки детей и ' \
          'другая полезная информация\n\nhttps://special-c.web.app/learning'

text511 = '• Наблюдение за выражением лица проблемного ребенка, развитием его органов чувств не должно оставаться вне ' \
          'поля зрения педагогов и родителей. Различные занятия, упражнения и использование предметов обихода ' \
          'принесут немалую пользу в этом направлении.\n\n• Умственно отсталого ребенка зачастую надо учить всему, ' \
          'даже улыбаться. Известно, что улыбка появляется лишь под воздействием социальных факторов, а не дана нам с ' \
          'рождения.\n\n• С такими детьми нужно постоянно общаться, сопровождая свои действия негромкой, ' \
          'плавной речью со ' \
          'спокойной, приветливой интонацией. С ними надо больше разговаривать, называя действия, ' \
          'которые производятся. Нужно постоянно поддерживать внимание и познавательный интерес к выполняемой ' \
          'деятельности и окружению.\n\nСоветуем заглянуть на наш сайт, там вы найдете больше полезной информации и ресурсов\nhttps://special-c.web.app'
text512 = 'Для детей с умственными отклонениями и детей с другими ограничениями мы создали сайт, который поможет Вам ' \
          'в обучении и ' \
          'воспитании ребенка, также там имеется вся необходимая информация о гос. программах для поддержки детей и ' \
          'другая полезная информация\n\nhttps://special-c.web.app/learning'

text521 = 'Только тесный и доброжелательный контакт ребенка и родителей и при этом помощь специалистов способствуют ' \
          'формированию навыков межличностного общения у умеренно и тяжело умственно отсталых детей и подростков. Для ' \
          'успешной работы с  детьми с проблемами обучения полезно выработать по отношению к нему единые требования, ' \
          'привычки и установки в семье и школе. Надо помнить, что противоречивые требования отрицательно влияют на ' \
          'психику и поведение детей. Познание себя как личности начинается у ребенка с установления физического ' \
          'контакта с окружающим миром через все органы чувств. Развитие личности ребенка — это осознание ' \
          'самоценности человеческой жизни, это развитие его доверия к жизни.\n\nСоветуем заглянуть на наш сайт, там вы найдете больше полезной информации и ресурсов\nhttps://special-c.web.app'
text522 = 'Для детей с умственными отклонениями и детей с другими ограничениями мы создали сайт, который поможет Вам ' \
          'в обучении и ' \
          'воспитании ребенка, также там имеется вся необходимая информация о гос. программах для поддержки детей и ' \
          'другая полезная информация\n\nhttps://special-c.web.app/learning'
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Главное меню')

btnInfo = KeyboardButton('Кто мы?')
btnQuiz = KeyboardButton('Опрос')
btnConsult = KeyboardButton('Консультация с экспертом')
btnOther = KeyboardButton('Обратная связь')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnQuiz, btnConsult, btnOther)  # меню с этими кнопками


btnReview = KeyboardButton('Оставьте нам отзыв')
btnMoney = KeyboardButton('Поддержите нас!')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnReview, btnMoney, btnMain)

#  Опросник
btnQuiz1 = KeyboardButton('Нарушение слуха')
btnQuiz2 = KeyboardButton('Нарушение зрения')
btnQuiz3 = KeyboardButton('Нарушение речи')
btnQuiz4 = KeyboardButton('Нарушение опорно-двигательного аппарата')
btnQuiz5 = KeyboardButton('Умственная отсталость')
Quiz = ReplyKeyboardMarkup(resize_keyboard=True).add(btnQuiz1, btnQuiz2, btnQuiz3, btnQuiz4, btnQuiz5)

#  степень инвалидности




#  Слух
btnQuiz11 = KeyboardButton('Совершенно глухой')
btnQuiz12 = KeyboardButton('Слабослышащий')
Quiz1 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnQuiz11, btnQuiz12)

btnQuiz111 = KeyboardButton('На ментальном здоровье глухого ребенка')
btnQuiz112 = KeyboardButton('На умственном развитии глухого ребенка')
Quiz11 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnQuiz111, btnQuiz112)

btnQuiz121 = KeyboardButton('На ментальном здоровье слабослышащего ребенка')
btnQuiz122 = KeyboardButton('На умственном развитии слабослышащего ребенка')
Quiz12 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnQuiz121, btnQuiz122)
#  Зрение
btnQuiz21 = KeyboardButton('Совершенно слепой')
btnQuiz22 = KeyboardButton('Слабовидящий')
Quiz2 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnQuiz21, btnQuiz22)

btnQuiz211 = KeyboardButton('На ментальном здоровье слепого ребенка')
btnQuiz212 = KeyboardButton('На умственном развитии слепого ребенка')
Quiz21 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnQuiz211, btnQuiz212)

btnQuiz221 = KeyboardButton('На ментальном здоровье слабовидящего ребенка')
btnQuiz222 = KeyboardButton('На умственном развитии слабовидящего ребенка')
Quiz22 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnQuiz221, btnQuiz222)

#  Речь
btnQuiz31 = KeyboardButton('Совершенно немой')
btnQuiz32 = KeyboardButton('Плохо говорит, но может')
Quiz3 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnQuiz31, btnQuiz32)

btnQuiz311 = KeyboardButton('На ментальном здоровье немого ребенка')
btnQuiz312 = KeyboardButton('На умственном развитии немого ребенка')
Quiz31 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnQuiz311, btnQuiz312)

btnQuiz321 = KeyboardButton('На ментальном здоровье плохоговорящего ребенка')
btnQuiz322 = KeyboardButton('На умственном развитии плохоговорящего ребенка')
Quiz32 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnQuiz321, btnQuiz322)

#  Опорно-двигательный аппарат
btnQuiz41 = KeyboardButton('Совершенно не способен ходить')
btnQuiz42 = KeyboardButton('Может, но плохо')
Quiz4 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnQuiz41, btnQuiz42)

btnQuiz411 = KeyboardButton('На ментальном здоровье ребенка с НОДА')
btnQuiz412 = KeyboardButton('На умственном развитии ребенка с НОДА')
Quiz41 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnQuiz411, btnQuiz412)

btnQuiz421 = KeyboardButton('На ментальном здоровье ребенка с слабым НОДА')
btnQuiz422 = KeyboardButton('На умственном развитии ребенка с слабым НОДА')
Quiz42 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnQuiz421, btnQuiz422)

#  Умственная осталость
btnQuiz51 = KeyboardButton('Совершенно умственно отсталый')
btnQuiz52 = KeyboardButton('Отсталый, но не сильно')
Quiz5 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnQuiz51, btnQuiz52)

btnQuiz511 = KeyboardButton('На ментальном здоровье умственно отсталого ребенка')
btnQuiz512 = KeyboardButton('На умственном развитии умственно отсталого ребенка')
Quiz51 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnQuiz511, btnQuiz512)

btnQuiz521 = KeyboardButton('На ментальном здоровье не сильно умственно отсталого ребенка')
btnQuiz522 = KeyboardButton('На умственном развитии не сильно умственно отсталого ребенка')


Quiz52 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnQuiz521, btnQuiz522)

@dp.message_handler(commands=['start'])  # обозачает событие в чате, команда через /
async def command_start(message: types.Message):  # асинхронность
    await bot.send_message(message.from_user.id, "Здравствуйте, {0.first_name}!".format(message.from_user),
                           reply_markup=nav.mainMenu)  # на команду появляется меню


@dp.message_handler()
async def bot_message(message: types.Message):
    # await bot.send_message(message.from_user.id, message.text)

    if message.text == 'Кто мы?':
        photo = open('icon.jpeg', 'rb')
        text = '*Special Care* - организация, которая помогает родителям детей с ограниченными ' \
               'возможностями.\n\n\nС нашей помощью родители смогут узнать о _правильном воспитании, ' \
               'поддержке и развитии своего ребёнка._\n\n\nДля нас важно, чтобы каждый особый ребенок ' \
               'получил *должностный уход* и *заслуживаемую любовь.*\n\nИменно поэтому мы *не требуем ' \
               'никакой платы* за наши услуги и наши ресурсы доступны для *каждого!*\n\n\n*Помогаем ' \
               'сделать этот мир лучше! ✨*'
        await bot.send_photo(message.from_user.id, photo, caption=text, parse_mode="Markdown")
    if message.text == 'Консультация с экспертом':
        await bot.send_message(message.from_user.id,
                               'Для связи с экспертом Вам достаточно написать этому боту @QWANT2022bot и ваш запрос '
                               'попадет к профессионалам!')
    if message.text == 'Обратная связь':
        await bot.send_message(message.from_user.id, 'Переходим в меню обратной связи...', reply_markup=nav.otherMenu)
    if message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'Переходим в главное меню...', reply_markup=nav.mainMenu)

    if message.text == 'Оставьте нам отзыв':
        await bot.send_message(message.from_user.id, "Оставьте этому боту @QWANT2022bot свой отзыв")
    elif message.text == 'Поддержите нас!':
        await bot.send_message(message.from_user.id, "Вы можете поддержать нас! \nКаспи: +123456789")

    if message.text == 'Опрос':
        await bot.send_message(message.from_user.id,
                               'Этот опрос поможет лучше понять Ваши предпочтения и дать Вам наилучшие рекомендации. '
                               '\nКакие возможности ограничены у Вашего ребенка?',
                               reply_markup=nav.Quiz)

    if message.text == 'Нарушение слуха':
        await bot.send_message(message.from_user.id, 'Какая у ребенка степень инвалидности?', reply_markup=nav.Quiz1)

    if message.text == 'Совершенно глухой':
        await bot.send_message(message.from_user.id, 'На чем вы бы хотели сосредоточиться?', reply_markup=nav.Quiz11)
    if message.text == 'На ментальном здоровье глухого ребенка':
        await bot.send_message(message.from_user.id, information.text111, reply_markup=nav.mainMenu)
    if message.text == 'На умственном развитии глухого ребенка':
        await bot.send_message(message.from_user.id, information.text112, reply_markup=nav.mainMenu)

    if message.text == 'Слабослышащий':
        await bot.send_message(message.from_user.id, 'На чем вы бы хотели сосредоточиться?', reply_markup=nav.Quiz12)
    if message.text == 'На ментальном здоровье слабослышащего ребенка':
        await bot.send_message(message.from_user.id, information.text121, reply_markup=nav.mainMenu)
    if message.text == 'На умственном развитии слабослышащего ребенка':
        await bot.send_message(message.from_user.id, information.text122, reply_markup=nav.mainMenu)

    if message.text == 'Нарушение зрения':
        await bot.send_message(message.from_user.id, 'Какая у ребенка степень инвалидности?', reply_markup=nav.Quiz2)

    if message.text == 'Совершенно слепой':
        await bot.send_message(message.from_user.id, 'На чем вы бы хотели сосредоточиться?', reply_markup=nav.Quiz21)
    if message.text == 'На ментальном здоровье слепого ребенка':
        await bot.send_message(message.from_user.id, information.text211, reply_markup=nav.mainMenu)
    if message.text == 'На умственном развитии слепого ребенка':
        await bot.send_message(message.from_user.id, information.text212, reply_markup=nav.mainMenu)

    if message.text == 'Слабовидящий':
        await bot.send_message(message.from_user.id, 'На чем вы бы хотели сосредоточиться?',
                               reply_markup=nav.Quiz12)
    if message.text == 'На ментальном здоровье слабовидящего ребенка':
        await bot.send_message(message.from_user.id, information.text221, reply_markup=nav.mainMenu)
    if message.text == 'На умственном развитии слабовидящего ребенка':
        await bot.send_message(message.from_user.id, information.text222, reply_markup=nav.mainMenu)

    if message.text == 'Нарушение речи':
        await bot.send_message(message.from_user.id, 'Какая у ребенка степень инвалидности?',
                               reply_markup=nav.Quiz3)

    if message.text == 'Совершенно немой':
        await bot.send_message(message.from_user.id, 'На чем вы бы хотели сосредоточиться?',
                               reply_markup=nav.Quiz31)
    if message.text == 'На ментальном здоровье немого ребенка':
        await bot.send_message(message.from_user.id, information.text311, reply_markup=nav.mainMenu)
    if message.text == 'На умственном развитии немого ребенка':
        await bot.send_message(message.from_user.id, information.text312, reply_markup=nav.mainMenu)



    if message.text == 'Плохо говорит, но может':
        await bot.send_message(message.from_user.id, 'На чем вы бы хотели сосредоточиться?', reply_markup=nav.Quiz32)
    if message.text == 'На ментальном здоровье плохоговорящего ребенка':
        await bot.send_message(message.from_user.id, information.text321, reply_markup=nav.mainMenu)
    elif message.text == 'На умственном развитии плохоговорящего ребенка':
        await bot.send_message(message.from_user.id, information.text322, reply_markup=nav.mainMenu)

    if message.text == 'Нарушение опорно-двигательного аппарата':
        await bot.send_message(message.from_user.id, 'Какая у ребенка степень инвалидности?',
                               reply_markup=nav.Quiz4)

    if message.text == 'Совершенно не способен ходить':
        await bot.send_message(message.from_user.id, 'На чем вы бы хотели сосредоточиться?',
                               reply_markup=nav.Quiz41)
    if message.text == 'На ментальном здоровье ребенка с НОДА':
        await bot.send_message(message.from_user.id, information.text411, reply_markup=nav.mainMenu)
    if message.text == 'На умственном развитии ребенка с НОДА':
        await bot.send_message(message.from_user.id, information.text412, reply_markup=nav.mainMenu)

    if message.text == 'Может, но плохо':
        await bot.send_message(message.from_user.id, 'На чем вы бы хотели сосредоточиться?',
                               reply_markup=nav.Quiz42)
    if message.text == 'На ментальном здоровье ребенка с слабым НОДА':
        await bot.send_message(message.from_user.id, information.text421, reply_markup=nav.mainMenu)
    if message.text == 'На умственном развитии ребенка с слабым НОДА':
        await bot.send_message(message.from_user.id, information.text422, reply_markup=nav.mainMenu)

    if message.text == 'Умственная отсталость':
        await bot.send_message(message.from_user.id, 'Какая у ребенка степень инвалидности?',
                               reply_markup=nav.Quiz5)

    if message.text == 'Совершенно умственно отсталый':
        await bot.send_message(message.from_user.id, 'На чем вы бы хотели сосредоточиться?',
                               reply_markup=nav.Quiz51)
    if message.text == 'На ментальном здоровье умственно отсталого ребенка':
        await bot.send_message(message.from_user.id, information.text511, reply_markup=nav.mainMenu)
    if message.text == 'На умственном развитии умственно отсталого ребенка':
        await bot.send_message(message.from_user.id, information.text512, reply_markup=nav.mainMenu)

    if message.text == 'Отсталый, но не сильно':
        await bot.send_message(message.from_user.id, 'На чем вы бы хотели сосредоточиться?',
                               reply_markup=nav.Quiz52)
    if message.text == 'На ментальном здоровье не сильно умственно отсталого ребенка':
        await bot.send_message(message.from_user.id, information.text521, reply_markup=nav.mainMenu)
    if message.text == 'На умственном развитии не сильно умственно отсталого ребенка':
        await bot.send_message(message.from_user.id, information.text522, reply_markup=nav.mainMenu)

HEROKU_APP_NAME = "qwantmainbot"

if HEROKU_APP_NAME is None:  # pooling mode
    print("Can't detect 'HEROKU_APP_NAME' env. Running bot in pooling mode.")
    print("Note: this is not a great way to deploy the bot in Heroku.")

    updater.start_polling()
    updater.idle()

else:  # webhook mode
    print(f"Running bot in webhook mode. Make sure that this url is correct: https://{HEROKU_APP_NAME}.herokuapp.com/")
    updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url="https://qwantmainbot.herokuapp.com/5465375647:AAEPTkq8lk1s4GOFwR5fiwBeuXOUBDob644"
    )

    updater.idle()
