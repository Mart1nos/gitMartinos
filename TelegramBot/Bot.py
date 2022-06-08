import telebot
from telebot import types

bot = telebot.TeleBot('5316261930:AAEiA_HhNoPTNM-XeO07ShiCK6eZQieMQGY')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    mess_one = f'Чтобы получить помощ введите команду /help'
    bot.send_message(message.chat.id, mess_one, parse_mode='html')
    mess_one = f'Давайте начнем? Жми /go'
    bot.send_message(message.chat.id, mess_one, parse_mode='html')

@bot.message_handler(commands=['help'])
def help(message):
    help = f'<b>У данного бота есть несколько команд:</b>'
    bot.send_message(message.chat.id, help, parse_mode='html')
    help1 = f'<b>/start</b>'
    bot.send_message(message.chat.id, help1, parse_mode='html')
    help2 = f'<b>/help</b>'
    bot.send_message(message.chat.id, help2, parse_mode='html')
    help3 = f'<b>/website</b>'
    bot.send_message(message.chat.id, help3, parse_mode='html')
    help4 = f'<b>/go</b>'
    bot.send_message(message.chat.id, help4, parse_mode='html')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Обращаться сюда", url="http://vk.com/first_tut"))
    bot.send_message(message.chat.id, 'По вопросам работы бота', reply_markup=markup)

@bot.message_handler(commands=['go'])
def go(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    go_one = types.KeyboardButton('Супы')
    go_two = types.KeyboardButton('Блюда из мяса')
    go_three = types.KeyboardButton('Блюда из курицы')
    go_four = types.KeyboardButton('Десерт')
    go_five = types.KeyboardButton('Выпечка')
    markup.add(go_one, go_two, go_three, go_four, go_five)
    bot.send_message(message.chat.id, 'Выбери какое блюдо ты хочешь приготовить', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, "И тебе привет, как твои дела?", parse_mode='html')
    elif message.text.lower() == "хорошо":
        bot.send_message(message.chat.id, "Ну и отлично! Давай начнем /go", parse_mode='html')
    elif message.text.lower() == "отлично":
        bot.send_message(message.chat.id, "Ну и хорошо! Давай начнем /go", parse_mode='html')

                                     # СУПЫ

    elif (message.text == "Супы"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Второй рецепт (Супы)")
        btn2 = types.KeyboardButton("Главное меню")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "<b>Суп «Харчо»</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/31/big_30806.jpg')
        bot.send_message(message.chat.id, f"<b>Продукты:</b>\n"
                                          f"Курица бройлерная - 1 шт.\n"
                                          f"Рис - 0,5 стакана\n"
                                          f"Чеснок - 1 головка\n"
                                          f"Масло сливочное - 50 г\n"
                                          f"Лук репчатый - 1 шт.\n"
                                          f"Морковь - 1 шт.\n"
                                          f"Томат-паста - 2 ст. ложки\n"
                                          f"Зелень - 50-60 г\n"
                                          f"Соль - 1 ст. ложка\n"
                                          f"\n"
                                          f"<b>Способ приготовления:</b>\n"
                                          f"Курицу промойте и порежьте на порционные кусочки. Залейте курицу 2,5 л кипящей водой и варите до готовности (30-40 минут) на среднем огне под крышкой. "
                                          f"Промойте рис. Выложите в бульон промытый рис. Когда он начнет набухать (через 10-15 минут), посолите суп. "
                                          f"Очистите, вымойте и мелко порежьте лук и морковь. Чеснок очистите от кожицы, мелко порежьте. "
                                          f"В сковороде разогрейте сливочное масло. Обжарьте овощи на среднем огне, помешивая 2-3 минуты. Перед окончанием жарки добавьте томатную пасту. "
                                          f"И хорошо перемешайте. Чеснок переложите в сковороду к овощам. Тушите овощи вместе около 5–7 минут на самом маленьком огне, помешивая. "
                                          f"Переложите овощи в суп. Отдельно приготовьте заправку для супа харчо. Очистите и порежьте чеснок, затем немного подавите его. Вымойте и нарежьте зелень. "
                                          f"Чеснок смешайте с мелко порубленной зеленью укропа и базилика. Наш суп харчо готов. При подаче посыпать заправкой.\n"
                                          f"Приятного аппетита!", parse_mode='html', reply_markup=markup)
    elif (message.text == "Второй рецепт (Супы)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("Третий рецепт (Супы)")
        btn4 = types.KeyboardButton("Главное меню")
        markup.add(btn3, btn4)
        bot.send_message(message.chat.id, "<b>Тосканский суп с фаршем</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/367/big_366898.jpg')
        bot.send_message(message.chat.id, f"<b>Продукты:</b>\n"
                                          f"Фарш свиной или говяжий - 250 г.\n"
                                          f"Картофель - 300 г (3 шт.)\n"
                                          f"Лук репчатый - 120-150 г (1 шт.)\n"
                                          f"Чеснок - 2 зубчика\n"
                                          f"Сливки жирностью 15% - 200 мл\n"
                                          f"Масло сливочное - 50 г.\n"
                                          f"Сыр твёрдых сортов - 30 г.\n"
                                          f"Паприка молотая - 1 ч. ложка\n"
                                          f"Соль - 1 ч. ложка\n"
                                          f"Перец чёрный молотый - 1/4 ч. ложки\n"
                                          f"Сахар - 1 ч. ложка\n"
                                          f"Петрушка свежая - 2-3 веточки\n"
                                          f"Травы итальянские сухие - 1 ч. ложка\n"
                                          f"Салат латук - 2 небольших листа\n"
                                          f"Вода - 1,5 л.\n"
                                          f"\n"
                                          f"<b>Способ приготовления:</b>\n"
                                          f"Свежую петрушку измельчите острым ножом. В сковороде растопите половину сливочного масла и выложите туда свиной фарш. "
                                          f"Добавьте петрушку, сахар, паприку, итальянские травы, соль и чёрный перец. Перемешайте фарш с зеленью и специями. "
                                          f"Затем туда же на мелкой тёрке натрите очищенный зубчик чеснока (или выдавите через пресс). Обжарьте 5-6 минут, периодически разбивая деревянной лопаткой. "
                                          f"Мясо немного уменьшится в объёме (ужарится) и благодаря паприке, травам и чесноку приобретёт очень красивый цвет и аромат. "
                                          f"В кастрюлю налейте 1,5 л воды и на большом огне доведите до кипения. Картофель очистите, нарежьте крупными кубиками и отправьте в кипящую воду. "
                                          f"Варите картофель до готовности. Очищенный лук нарежьте мелкими кубиками. Оставшийся очищенный зубчик чеснока мелко нарежьте. "
                                          f"В другой сковороде растопите оставшееся сливочное масло и обжарьте лук и чеснок до золотистости. Готовый картофель измельчите в отваре в пюре. "
                                          f"Можно использовать для этого картофелемялку или погружной блендер. Добавьте обжаренные лук и чеснок, доведите до кипения и варите 2-3 минуты. "
                                          f"Далее в кастрюлю влейте сливки, доведите до кипения и варите ещё 5 минут. После этого выложите в кастрюлю фарш, добавьте соль по вкусу и варите ещё 10 минут. "
                                          f"Тосканский сливочный суп с фаршем готов. Выключите плиту. Оставьте суп на тёплой плите настаиваться ещё 5-7 минут. "
                                          f"Сыр натрите на мелкой тёрке. Разлейте суп по порционным тарелкам, выложите в каждую тарелку по половине листа салата латука и по 1/2 ст. ложки натёртого сыра. "
                                          f"Подавайте итальянский суп с фаршем к столу горячим. Ароматная Италия у вас дома - это тосканский суп с фаршем!", parse_mode='html', reply_markup=markup)
    elif (message.text == "Третий рецепт (Супы)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("Четвертый рецепт (Супы)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Томатный суп со свининой и рисом</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/473/big_472428.jpg')
        bot.send_message(message.chat.id, f"<b>Продукты:</b>\n"
                                          f"Свинина (мякоть) - 500 г.\n"
                                          f"Картофель - 500 г (3-4 шт.)\n"
                                          f"Рис - 80 г.\n"
                                          f"Лук репчатый - 0,5 шт. (80 г.)\n"
                                          f"Морковь - 1 шт. (80 г.)\n"
                                          f"Томатный соус (любой, по своему вкусу) - 400 г.\n"
                                          f"Чеснок - 1-2 зубчика\n"
                                          f"Масло растительное - 3 ст. ложки\n"
                                          f"Укроп свежий - 1 веточка\n"
                                          f"Лавровый лист - 1 шт.\n"
                                          f"\n"
                                          f"<b>Способ приготовления:</b>\n"
                                          f"Свинину вымойте, залейте в кастрюлю 2,5 л холодной воды и поставьте на огонь. "
                                          f"Доведите воду до кипения, снимите образовавшуюся пену и варите бульон на среднем огне 1-1,5 часа, до мягкости свинины. "
                                          f"Готовое мясо достаньте из бульона и остудите для нарезания. Картофель очистите и нарежьте кубиками. Переложите картофель в кипящий бульон. "
                                          f"Следом добавьте в кастрюлю рис (при желании можно промыть). Мясо нарежьте кусочками и переложите в кастрюлю к картофелю и рису. "
                                          f"Доведите до кипения и варите 15 минут, до готовности риса и овощей. Очищенный репчатый лук нарежьте мелкими кубиками. "
                                          f"Очищенную морковь натрите на крупной терке. Разогрейте в сковороде растительное масло и выложите в сковороду репчатый лук. Обжарьте лук до прозрачности. "
                                          f"Морковь добавьте к луку и обжарьте 3-4 минуты, до мягкости. К овощам в сковороде добавьте томатный соус. "
                                          f"Обратите внимание - именно соус, а не томатную пасту (её, конечно, нужно меньше)!Добавьте измельчённый чеснок (его можно натереть на мелкой тёрке или выдавить через пресс). "
                                          f"Обжарьте всё 1-2 минуты. Такая предварительная обжарка слегка уберет кислоту томатного соуса и сделает суп ярче по цвету. "
                                          f"Добавьте зажарку в кастрюлю с супом. Варите 3-4 минуты. Добавьте лавровый листик, всыпьте соль и чёрный молотый перец. Перемешайте и выключите огонь под кастрюлей. "
                                          f"Рисовый суп со свининой и томатным соусом готов.", parse_mode='html', reply_markup=markup)
    elif (message.text == "Четвертый рецепт (Супы)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("Пятый рецепт (Супы)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Куриный суп с плавленым сыром</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/173/big_172089.jpg')
        bot.send_message(message.chat.id, f"<b>Продукты:</b>\n"
                                          f"Куриное филе - 500 г.\n"
                                          f"Сыр плавленый - 2 пач. (180-200 г)\n"
                                          f"Вермишель - 0,5 стакана\n"
                                          f"Картофель - 4 шт.\n"
                                          f"Лук репчатый - 1 шт.\n"
                                          f"Морковь - 1 шт.\n"
                                          f"Зелень - 1 пучок\n"
                                          f"Масло сливочное - 2 ст. л.\n"
                                          f"\n"
                                          f"<b>Способ приготовления:</b>\n"
                                          f"Куриное филе моем и нарезаем кусочками. Кладем в кастрюлю, заливаем водой и ставим на плиту."
                                          f"Пока варится мясо, чистим лук и нарезаем мелкими кусочками. Морковь чистим и натираем на крупной терке. "
                                          f"Делаем зажарку из лука и моркови. Пока готовится зажарка, чистим и нарезаем картофель. "
                                          f"Бросаем вариться к мясу готовую зажарку и нарезанный картофель. "
                                          f"Нарезаем сыр кубиками (не покупайте дешевый сыр, он не растворится у вас в супе). Мелко нарезаем помытую зелень. "
                                          f"Через 10 минут после того, как бросили вариться картофель, добавляем в куриный суп вермишель и варим еще 5 мин. "
                                          f"Добавляем в суп с вермишелью соль и специи. Добавляем плавленые сырки и варим сырный суп до полного растворения сыра. "
                                          f"Когда сыр растворится, добавляем зелень и снимаем куриный суп с плавленым сыром с огня.", parse_mode='html', reply_markup=markup)
    elif (message.text == "Пятый рецепт (Супы)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("Шестой рецепт (Супы)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Куриный суп с консервированным горошком и яйцом</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/398/big_397784.jpg')
        bot.send_message(message.chat.id, f"<b>Продукты:</b>\n"
                                          f"Куриные бедрышки - 2 шт. (500 г.)\n"
                                          f"Картофель - 3-4 шт. (400 г.)\n"
                                          f"Морковь - 1 шт. (100 г.)\n"
                                          f"Лук репчатый - 1 шт. (100 г.)\n"
                                          f"Яйца - 2 шт.\n"
                                          f"Горошек зеленый консервированный - 1 банка (380 г.)\n"
                                          f"Укроп свежий - 2-3 веточки\n"
                                          f"Перец черный молотый - 1 щепотка\n"
                                          f"Соль - 1 ч. ложка\n"
                                          f"Масло растительное - 2 ст. ложки\n"
                                          f"\n"
                                          f"<b>Способ приготовления:</b>\n"
                                          f"Подготовьте все ингредиенты. Очистите овощи. "
                                          f"Для этого супа можно взять любые части курицы, я использовала два куриных бедрышка на кастрюлю объемом 3 л. "
                                          f"Яйца залейте водой и варите после закипания 8-10 минут. "
                                          f"Куриное мясо тщательно вымойте, залейте 2 л воды и доведите до кипения. Снимите пену и варите до готовности мяса примерно 40 минут. "
                                          f"Очищенный репчатый лук нарежьте небольшими кубиками, очищенную морковь натрите на крупной терке. "
                                          f"В сковороде разогрейте растительное масло и обжарьте лук до прозрачности, примерно 3-4 минуты на среднем огне. "
                                          f"Добавьте в сковороду морковь и обжарьте 5-7 минут до мягкости моркови. Готовое куриное мясо достаньте из бульона и охладите. "
                                          f"Очищенный картофель нарежьте тонкими брусочками. В кипящий бульон выложите картофель и варите 15 минут. "
                                          f"Когда картофель станет мягким, добавьте в кастрюлю содержимое сковороды. "
                                          f"Куриное мясо отделите от костей, разделите на волокна или нарежьте небольшими кусочками. "
                                          f"Добавьте в кастрюлю банку зеленого горошка вместе с маринадом. Добавьте в кастрюлю соль и черный молотый перец по вкусу. "
                                          f"Отваренные яйца очистите, натрите на крупной терке и добавьте в кастрюлю. Доведите до кипения и варите суп 2-3 минуты. "
                                          f"Свежий укроп мелко нарежьте, добавьте в кастрюлю и выключите огонь. Дайте супу настояться 5-10 минут. ", parse_mode='html', reply_markup=markup)
    elif (message.text == "Шестой рецепт (Супы)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("Седьмой рецепт (Супы)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Солянка сборная с колбасой</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/327/big_326186.jpg')
        bot.send_message(message.chat.id, f"<b>Продукты:</b>\n"
                                          f"Говядина на кости - 800 г.\n"
                                          f"Колбаса копчёная - 150 г.\n"
                                          f"Сосиски - 2-3 шт.\n"
                                          f"Огурцы солёные - 150 г.\n"
                                          f"Лук репчатый - 2 шт.\n"
                                          f"Оливки без косточек - 100 г.\n"
                                          f"Томатная паста -1 ст. ложка\n"
                                          f"Масло растительное - 4 ст. ложки\n"
                                          f"Лавровый лист - 1 шт.\n"
                                          f"Вода - 3 л.\n"
                                          f"\n"
                                          f"<b>Способ приготовления:</b>\n"
                                          f"Подготавливаем необходимые продукты по списку. Говядину кладем в кастрюлю, заливаем холодной водой и доводим до кипения. "
                                          f"Снимаем пену, уменьшаем огонь до минимального. Добавляем в кастрюлю очищенную луковицу и варим бульон на медленном огне 2-2,5 часа (до готовности мяса). "
                                          f"Спустя указанное время добавляем лавровый лист, продолжаем варить бульон еще минут 20. "
                                          f"Достаем из бульона готовое мясо и оставляем остужаться. Луковица и лавровый лист больше не пригодятся. "
                                          f"Бульон процеживаем и снова доводим до кипения. За долгое время варки готового бульона останется около 1,5 л. "
                                          f"Репчатый лук очищаем и мелко нарезаем. Разогреваем на сковороде растительное масло, обжариваем лук пару минут на небольшом огне. "
                                          f"Пока обжаривается лук, натираем на крупной терке соленые огурцы. Выкладываем их к луку, накрываем сковороду крышкой. "
                                          f"Даем огурцам пропариться на сковороде 5 минут. Добавляем томатную пасту и обжариваем 3-4 минуты. "
                                          f"Перекладываем зажарку в бульон. Варим в течение 10 минут. В это время подготавливаем мясные продукты: колбасу и сосиски очищаем от оболочки, сосиски нарезаем кружочками, колбасу соломкой. "
                                          f"Отварное мясо отделяем от костей, нарезаем кубиками. Закладываем колбасные изделия и мясо в кастрюлю. Варим солянку с колбасой и мясом еще 5 минут. "
                                          f"Добавляем в солянку оливки. Солим по вкусу. Варим мясную сборную солянку 5 минут. Даем супу немного настояться. "
                                          f"Мясную сборную солянку с колбасой подаем, добавив в тарелку пару ломтиков лимона и сметану. Можно добавить мелко порезанную зелень.\n"
                                          f"Приятного аппетита!", parse_mode='html', reply_markup=markup)
    elif (message.text == "Седьмой рецепт (Супы)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("Восьмой рецепт (Супы)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Суп Затируха с курицей</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/323/big_322775.jpg')
        bot.send_message(message.chat.id, f"<b>Продукты:</b>\n"
                                          f"Курица (спинка) - 150 г.\n"                                         
                                          f"Яйца - 2 шт.Мука - 6 ст. ложек\n"
                                          f"Картофель - 2 шт.\n"
                                          f"Морковь - 1 шт.\n"
                                          f"Лук репчатый - 1 шт.\n"
                                          f"Лавровый лист - 1 шт.\n"
                                          f"Соль - 0,5 ст. ложки\n"
                                          f"Перец чёрный молотый - 1/3 ч. ложки\n"
                                          f"<b>Способ приготовления:</b>\n"
                                          f"Курицу выложите в кастрюлю, залейте ее водой. Добавьте соль. Отправьте кастрюлю на огонь и варите бульон на слабом огне 40 минут. "
                                          f"Когда бульон закипит, обязательно соберите ложкой пену. В миску вбейте одно яйцо. Яйцо немного взбейте венчиком. "
                                          f"Теперь руки окуните в яйцо. Затем в муку. Потрите ладошки над тарелкой друг о друга. Таким образом проделайте несколько раз, чтобы использовать всю муку. "
                                          f"Лук нарежьте маленькими кубиками. Морковь натрите на мелкой терке. Разогрейте сковороду с растительным маслом. "
                                          f"Обжарьте овощи на среднем огне в течение 3 минут. Картофель нарежьте небольшими кубиками. Достаньте мясо из бульона. Выложите в бульон нарезанный картофель. "
                                          f"Добавьте лавровый лист. Мясо отделите от костей. Нарежьте мясо и выложите назад в бульон. "
                                          f"Отправьте кастрюлю на слабый огонь и варите суп с картофелем и курицей в течение 20 минут. Теперь выложите в суп зажарку. "
                                          f"Затирку просейте через сито. Выложите затирку в суп. Второе яйцо взбейте венчиком и влейте в суп. Варите суп с затиркой еще 10 минут. "
                                          f"В готовый суп добавьте молотый перец. Зеленый лук мелко нарежьте. Разлейте суп по тарелкам, украсьте зеленым луком и подавайте. ", parse_mode='html', reply_markup=markup)
    elif (message.text == "Восьмой рецепт (Супы)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("Девятый рецепт (Супы)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Шурпа из говядины</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/173/big_172088.jpg')
        bot.send_message(message.chat.id, f"<b>Продукты:</b>\n"
                                          f"Говядина с косточкой - 800 г.\n"
                                          f"Картофель - 800 г.\n"
                                          f"Морковь - 200 г.\n"
                                          f"Лук - 150 г.\n"
                                          f"Перец сладкий - 100 г.\n"
                                          f"Лист лавровый - 3 шт.\n"
                                          f"Соль - 1 ст. ложка без горки\n"
                                          f"Куркума - 0,5 ч. ложки\n"
                                          f"Перец - 0,5 ч. ложки\n"
                                          f"Карри - 1 ч. ложка\n"
                                          f"Зелень петрушки - 1 пучок\n"
                                          f"<b>Способ приготовления:</b>\n"
                                          f"Мясо нарезаем порционными кусочками и моем. Заливаем водой и варим до полной готовности в течение 1 часа. "
                                          f"По желанию достаем мясо шумовкой и удаляем все косточки. Добавляем сладкий перец, порезанный на кусочки (я использовала замороженный). "
                                          f"Туда же высыпаем крупно нарезанные лук и морковь. Солим и добавляем лавровый лист. Добавляем картофель, нарезанный кубиками. "
                                          f"Варим до готовности картофеля. Добавляем специи. После высыпаем рубленную зелень. Держим на огне еще 5 минут - и суп готов. "
                                          f"Подаем шурпу из говядины в горячем виде со свежей зеленью.\n"
                                          f"Приятного аппетита!", parse_mode='html', reply_markup=markup)
    elif (message.text == "Девятый рецепт (Супы)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("Десятый рецепт (Супы)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Суп с мясными фрикадельками и вермишелью</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/510/big_509465.jpg')
        bot.send_message(message.chat.id, f"<b>Продукты:</b>\n", parse_mode='html', reply_markup=markup)
    elif (message.text == "Десятый рецепт (Супы)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("Одиннадцатый рецепт (Супы)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Суп картофельный с клецками</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/93/big_92735.jpg')
        bot.send_message(message.chat.id, f"<b>Продукты:</b>\n", parse_mode='html', reply_markup=markup)
    elif (message.text == "Одиннадцатый рецепт (Супы)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("Двенадцатый рецепт (Супы)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Томатный суп с курицей, фасолью и овощами</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/412/big_411724.jpg')
        bot.send_message(message.chat.id, f"<b>Продукты:</b>\n", parse_mode='html', reply_markup=markup)
    elif (message.text == "Двенадцатый рецепт (Супы)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("Тринадцатый рецепт (Супы)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Щи По-русски</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/94/big_93408.jpg')
        bot.send_message(message.chat.id, f"<b>Продукты:</b>\n", parse_mode='html', reply_markup=markup)
    elif (message.text == "Тринадцатый рецепт (Супы)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("Четырнадцатый рецепт (Супы)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Гороховый суп с копчёностями</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/591/big_590270.jpg')
        bot.send_message(message.chat.id, f"<b>Продукты:</b>\n", parse_mode='html', reply_markup=markup)
    elif (message.text == "Четырнадцатый рецепт (Супы)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("Пятнадцатый рецепт (Супы)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Чешский чесночный суп</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/248/big_247500.jpg')
        bot.send_message(message.chat.id, f"<b>Продукты:</b>\n", parse_mode='html', reply_markup=markup)
    elif (message.text == "Пятнадцатый рецепт (Супы)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("Шестнадцатый рецепт (Супы)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Куриный суп со сливками и лапшой</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/480/big_479514.jpg')
        bot.send_message(message.chat.id, f"<b>Продукты:</b>\n", parse_mode='html', reply_markup=markup)
    elif (message.text == "Шестнадцатый рецепт (Супы)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("Семьнадцатый рецепт (Супы)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Суп Рыжик с жареной вермишелью (без зажарки)</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/587/big_586583.jpg')
        bot.send_message(message.chat.id, f"<b>Продукты:</b>\n", parse_mode='html', reply_markup=markup)
    elif (message.text == "Семьнадцатый рецепт (Супы)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("Восемьнадцатый рецепт (Супы)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Фасолевый суп с плавленым сыром и беконом</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/477/big_476614.jpg')
        bot.send_message(message.chat.id, f"<b>Продукты:</b>\n", parse_mode='html', reply_markup=markup)
    elif (message.text == "Восемьнадцатый рецепт (Супы)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("Девятнадцатый рецепт (Супы)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Куриный суп с сырными шариками и картофелем</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/341/big_340209.jpg')
        bot.send_message(message.chat.id, f"<b>Продукты:</b>\n", parse_mode='html', reply_markup=markup)
    elif (message.text == "Девятнадцатый рецепт (Супы)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("Двадцатый рецепт (Супы)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Любимый суп</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/220/big_219213.jpg')
        bot.send_message(message.chat.id, f"<b>Продукты:</b>\n", parse_mode='html', reply_markup=markup)
    elif (message.text == "Двадцатый рецепт (Супы)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn6)
        bot.send_message(message.chat.id, "<b>Гречневый суп со свининой</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/416/big_415166.jpg')
        bot.send_message(message.chat.id, f"<b>Продукты:</b>\n", parse_mode='html', reply_markup=markup)

                              # Блюда из мяса

    elif (message.text == "Блюда из мяса"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Второй рецепт (Блюда из мяса)")
        btn2 = types.KeyboardButton("Главное меню")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "<b>Жаркое по-деревенски</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/465/big_464858.jpg')
        bot.send_message(message.chat.id, "<b>Описание</b>", parse_mode='html', reply_markup=markup)
    elif (message.text == "Второй рецепт (Блюда из мяса)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn3 = types.KeyboardButton("Третий рецепт (Блюда из мяса)")
        btn4 = types.KeyboardButton("Главное меню")
        markup.add(btn3, btn4)
        bot.send_message(message.chat.id, "<b>Тушёная картошка с мясом, грибами и сметаной</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/574/big_573466.jpg')
        bot.send_message(message.chat.id, "<b>Описание</b>", parse_mode='html', reply_markup=markup)
    elif (message.text == "Третий рецепт (Блюда из мяса)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn5 = types.KeyboardButton("Четвертый рецепт (Блюда из мяса)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Макароны с мясом в томатном соусе, на сковороде</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/555/big_554324.jpg')
        bot.send_message(message.chat.id, "<b>Описание</b>", parse_mode='html', reply_markup=markup)

                           # Блюда из курицы

    elif (message.text == "Блюда из курицы"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn5 = types.KeyboardButton("Второй рецепт (Блюда из курицы)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Куриный беф-строганов</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/32/big_31172.jpg')
        bot.send_message(message.chat.id, "<b>Описание</b>", parse_mode='html', reply_markup=markup)
    elif (message.text == "Второй рецепт (Блюда из курицы)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn5 = types.KeyboardButton("Третий рецепт (Блюда из курицы)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Жюльен с курицей и грибами</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/195/big_194679.jpg')
        bot.send_message(message.chat.id, "<b>Описание</b>", parse_mode='html', reply_markup=markup)
    elif (message.text == "Третий рецепт (Блюда из курицы)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn5 = types.KeyboardButton("Четвертый рецепт (Блюда из курицы)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Лагман с курицей</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/130/big_129813.jpg')
        bot.send_message(message.chat.id, "<b>Описание</b>", parse_mode='html', reply_markup=markup)

                         # Десерты

    elif (message.text == "Десерт"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn5 = types.KeyboardButton("Второй рецепт (Десерты)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Торт Медовик за 15 минут</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/174/big_173898.jpg')
        bot.send_message(message.chat.id, "<b>Описание</b>", parse_mode='html', reply_markup=markup)
    elif (message.text == "Второй рецепт (Десерты)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn5 = types.KeyboardButton("Третий рецепт (Десерты)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Шоколадный швейцарский рулет с масляным кремом</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/4/big_3219.jpg')
        bot.send_message(message.chat.id, "<b>Описание</b>", parse_mode='html', reply_markup=markup)
    elif (message.text == "Третий рецепт (Десерты)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn5 = types.KeyboardButton("Четвертый рецепт (Десерты)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Шоколадный кекс в микроволновке</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/323/big_322394.jpg')
        bot.send_message(message.chat.id, "<b>Описание</b>", parse_mode='html', reply_markup=markup)

                       # Выпечки

    elif (message.text == "Выпечка"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn5 = types.KeyboardButton("Второй рецепт (Выпечки)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Булочки Вкусняшки</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/60/big_59497.jpg')
        bot.send_message(message.chat.id, "<b>Описание</b>", parse_mode='html', reply_markup=markup)
    elif (message.text == "Второй рецепт (Выпечки)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn5 = types.KeyboardButton("Третий рецепт (Выпечки)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Пиццы Школьные с варёной колбасой, маринованными огурцами и сыром</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/576/big_575624.jpg')
        bot.send_message(message.chat.id, "<b>Описание</b>", parse_mode='html', reply_markup=markup)
    elif (message.text == "Третий рецепт (Выпечки)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn5 = types.KeyboardButton("Четвертый рецепт (Выпечки)")
        btn6 = types.KeyboardButton("Главное меню")
        markup.add(btn5, btn6)
        bot.send_message(message.chat.id, "<b>Сырные булочки с помидорами и зелёным луком</b>", parse_mode='html')
        bot.send_photo(message.chat.id, photo='https://img1.russianfood.com/dycontent/images_upl/343/big_342294.jpg')
        bot.send_message(message.chat.id, "<b>Описание</b>", parse_mode='html', reply_markup=markup)







    elif (message.text == "Главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        go_one = types.KeyboardButton('Супы')
        go_two = types.KeyboardButton('Блюда из мяса')
        go_three = types.KeyboardButton('Блюда из курицы')
        go_four = types.KeyboardButton('Десерт')
        go_five = types.KeyboardButton('Выпечка')
        markup.add(go_one, go_two, go_three, go_four, go_five)
        bot.send_message(message.chat.id, 'Выбери какое блюдо ты хочешь приготовить', reply_markup=markup)

    else:
        bot.send_message(message.chat.id, "Мои возможности ограничены, напиши команду /help", parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message): # get_user_photo это название, может быть любое
    bot.send_message(message.chat.id, 'Ура, твое фото загружено!')

bot.polling(none_stop=True)