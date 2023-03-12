from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

btnMain = KeyboardButton("Главное меню")

b1 = KeyboardButton('Anime')
b1_1 = KeyboardButton('animeGo')
b1_2 = KeyboardButton('jut')
b1_3 = KeyboardButton('aniu')
b1_4 = KeyboardButton('sovetromantica')

mainAnimeMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(b1_1, b1_2, b1_3, b1_4, btnMain)


b2 = KeyboardButton('Movies')
b2_1 = KeyboardButton('lordfilm')
b2_2 = KeyboardButton('vse-chasti-filmov')
b2_3 = KeyboardButton('zona.plus')
b2_4 = KeyboardButton('lordserial')

mainMoviesMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(b1_1, b2_2, b2_3, b2_4, btnMain)


b3 = KeyboardButton('Series')
b3_1 = KeyboardButton('lordfilm')
b3_2 = KeyboardButton('vse-chasti-filmov')
b3_3 = KeyboardButton('zona.plus')
b3_4 = KeyboardButton('lordserial')
mainSeriesMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(b3_1, b3_2, b3_3, b3_4, btnMain)


b4 = KeyboardButton('Trail')
b4_1 = KeyboardButton('youtube')
mainTrailMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(b4_1, btnMain)


mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(b1, b2, b3, b4)
kb_client.row(b1, b2)
kb_client.row(b3, b4)

