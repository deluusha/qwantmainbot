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
