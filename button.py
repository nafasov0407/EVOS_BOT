from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

til = ReplyKeyboardMarkup(
	keyboard = [
		[
				KeyboardButton(text="🇺🇿 O'zbekcha")
		],
	],
	resize_keyboard = True
)

tur = ReplyKeyboardMarkup(
	keyboard = [
		[
				KeyboardButton(text="📖Menyu")
		],
		[
				KeyboardButton(text="📞Telefon raqam"),KeyboardButton(text="📍Joylashuv yuborish")
		],
	],
	resize_keyboard = True
)

xizmatlar = ReplyKeyboardMarkup(
	keyboard = [
		[
				KeyboardButton(text="☎️Biz bilan aloqa")
		],
		[
				KeyboardButton(text="⚙️Sozlamalar")
		],
	],
	resize_keyboard = True
)

buyurtma = InlineKeyboardMarkup(
	inline_keyboard = [

		[
				InlineKeyboardButton(text = "Buyurtma",callback_data = "buy")
		],
	],
)


menyu = InlineKeyboardMarkup(
	inline_keyboard = [
		[
				InlineKeyboardButton(text = "🌯Lavash",callback_data = 'lavash'),InlineKeyboardButton(text = "🌮Shaurma",callback_data = 'shaurma')
		],
		[
				InlineKeyboardButton(text = "🍔Burger",callback_data = 'burger'),InlineKeyboardButton(text = "🌭Xod-dog",callback_data = 'xod-dog')
		],
		[
				InlineKeyboardButton(text = "🍕Pizza",callback_data = 'pizza'),InlineKeyboardButton(text = "☕️Ichimliklar",callback_data = 'ichimliklar')
		],
		[
				InlineKeyboardButton(text = "🥪Sendvich club",callback_data = 'sendvich'),InlineKeyboardButton(text = "🍱Donar",callback_data = 'donar')
		],
		[
				InlineKeyboardButton(text = "🍰Desertlarlar",callback_data = 'desertlar'),InlineKeyboardButton(text = "🔎Boshqa",callback_data = 'boshqa')
		],
	],
)

lavash_menyu2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🍗Tovuqli lavash",callback_data = "tovuqli"),InlineKeyboardButton(text = "🥩Go'shtli lavash",callback_data = "gushtli")
		],
		[
				InlineKeyboardButton(text = "🧀pishloqli lavash",callback_data = "pishloq"),InlineKeyboardButton(text = "🥨Tandir lavash",callback_data = "tandir")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back3')
		],
	],
)
# tovuq uchun
lavash_menyu3 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🫔Mini lavash",callback_data = "mini_tovuq"),InlineKeyboardButton(text = "🍖Big lavash",callback_data = "big_tovuq"),InlineKeyboardButton(text = "🥪Classik lavash",callback_data = "classik_tovuq")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back4')
		],
	],
)
# gush uchun
lavash_menyu4 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🧆Mini lavash",callback_data = "mini_gush"),InlineKeyboardButton(text = "🥩Big lavash",callback_data = "big_gush"),InlineKeyboardButton(text = "🥓Classik lavash",callback_data = "classik_gush")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back5')
		],
	],
)

#pishloqli uchun
lavash_menyu9 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🧆Mini lavash",callback_data = "mini_pish"),InlineKeyboardButton(text = "🥩Big lavash",callback_data = "big_pish"),InlineKeyboardButton(text = "🥓Classik lavash",callback_data = "classik_pish")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back18')
		],
	],
)
# tandir lavash 
lavash_menyu10 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🧆Mini lavash",callback_data = "mini_tan"),InlineKeyboardButton(text = "🥩Big lavash",callback_data = "big_tan"),InlineKeyboardButton(text = "🥓Classik lavash",callback_data = "classik_tan")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back19')
		],
	],
)
#  soni uchun
lavash_menyu5 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back6')
		],
	],
)

lavash_menyu6 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "b1"),InlineKeyboardButton(text = "2",callback_data = "b2"),InlineKeyboardButton(text = "3",callback_data = "b3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "b4"),InlineKeyboardButton(text = "5",callback_data = "b5"),InlineKeyboardButton(text = "6",callback_data = "b6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "b7"),InlineKeyboardButton(text = "8",callback_data = "b8"),InlineKeyboardButton(text = "...",callback_data = "b9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back7')
		],
	],
)

lavash_menyu7 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back16')
		],
	],
)

lavash_menyu8 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "a1"),InlineKeyboardButton(text = "2",callback_data = "a2"),InlineKeyboardButton(text = "3",callback_data = "a3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "a4"),InlineKeyboardButton(text = "5",callback_data = "a5"),InlineKeyboardButton(text = "6",callback_data = "a6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "a7"),InlineKeyboardButton(text = "8",callback_data = "a8"),InlineKeyboardButton(text = "...",callback_data = "a9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back17')
		],
	],
)

# shourma uchun


shaurma_menyu1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🥩Go'shli shourma",callback_data = "go'shli"),InlineKeyboardButton(text = "🌶Achchig' go'shli shourma",callback_data = "achchiq")
		],
		[
				InlineKeyboardButton(text = "🍗Tovuqli shourma",callback_data = "tovuq"),InlineKeyboardButton(text = "🌶Achchig' tovuqli shourma",callback_data = "achchig'i")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back8')
		],
	],
)

shaurma_menyu2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🌮Katta gushli",callback_data = "katta_gushli"),InlineKeyboardButton(text = "🥓Kichigi gushli",callback_data = "kichig_gushli")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back9')
		],
	],
)

shaurma_menyu6 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🌮Katta achchig'i",callback_data = "katta_achchigi1"),InlineKeyboardButton(text = "🥓Kichig achchig'i",callback_data = "kichig_achchig'i1")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back27')
		],
	],
)

shaurma_menyu5 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🌮Katta achchig'i",callback_data = "katta_achchiq"),InlineKeyboardButton(text = "🥓Kichig achchig'i",callback_data = "kichig_achchiq")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back24')
		],
	],
)

shaurma_menyu9 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🌮Katta tovuqli",callback_data = "katta_tovuq1"),InlineKeyboardButton(text = "🥓Kichig tovuqli",callback_data = "kichig_tovuq1")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back30')
		],
	],
)
shaurma_menyu3 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "c1"),InlineKeyboardButton(text = "2",callback_data = "c2"),InlineKeyboardButton(text = "3",callback_data = "c3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "c4"),InlineKeyboardButton(text = "5",callback_data = "c5"),InlineKeyboardButton(text = "6",callback_data = "c6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "c7"),InlineKeyboardButton(text = "8",callback_data = "c8"),InlineKeyboardButton(text = "...",callback_data = "c9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back10')
		],
	],
)

shaurma_menyu4 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "c1"),InlineKeyboardButton(text = "2",callback_data = "c2"),InlineKeyboardButton(text = "3",callback_data = "c3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "c4"),InlineKeyboardButton(text = "5",callback_data = "c5"),InlineKeyboardButton(text = "6",callback_data = "c6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "c7"),InlineKeyboardButton(text = "8",callback_data = "c8"),InlineKeyboardButton(text = "...",callback_data = "c9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back23')
		],
	],
)

shaurma_menyu7 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "c1"),InlineKeyboardButton(text = "2",callback_data = "c2"),InlineKeyboardButton(text = "3",callback_data = "c3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "c4"),InlineKeyboardButton(text = "5",callback_data = "c5"),InlineKeyboardButton(text = "6",callback_data = "c6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "c7"),InlineKeyboardButton(text = "8",callback_data = "c8"),InlineKeyboardButton(text = "...",callback_data = "c9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back28')
		],
	],
)

shaurma_menyu8 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "c1"),InlineKeyboardButton(text = "2",callback_data = "c2"),InlineKeyboardButton(text = "3",callback_data = "c3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "c4"),InlineKeyboardButton(text = "5",callback_data = "c5"),InlineKeyboardButton(text = "6",callback_data = "c6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "c7"),InlineKeyboardButton(text = "8",callback_data = "c8"),InlineKeyboardButton(text = "...",callback_data = "c9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back29')
		],
	],
)



#Burger uchun ?????????????????????????

burger_menyu1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🍔Gamburger",callback_data = "gamburger"),InlineKeyboardButton(text = "🥪Chizburger",callback_data = "chizburger")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back11')
		],
	],
)

burger_menyu2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🍔Katta Burger",callback_data = "kat_bur"),InlineKeyboardButton(text = "🥮Kichik Burger",callback_data = "kich_bur")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back12')
		],
	],
)


burger_menyu5 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🍔Katta Burger",callback_data = "kat_chiz"),InlineKeyboardButton(text = "🥮Kichik Burger",callback_data = "kich_chiz")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back25')
		],
	],
)

burger_menyu3 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "d1"),InlineKeyboardButton(text = "2",callback_data = "d2"),InlineKeyboardButton(text = "3",callback_data = "d3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "d4"),InlineKeyboardButton(text = "5",callback_data = "d5"),InlineKeyboardButton(text = "6",callback_data = "d6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "d7"),InlineKeyboardButton(text = "8",callback_data = "d8"),InlineKeyboardButton(text = "...",callback_data = "d9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back13')
		],
	],
)

burger_menyu4 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "d1"),InlineKeyboardButton(text = "2",callback_data = "d2"),InlineKeyboardButton(text = "3",callback_data = "d3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "d4"),InlineKeyboardButton(text = "5",callback_data = "d5"),InlineKeyboardButton(text = "6",callback_data = "d6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "d7"),InlineKeyboardButton(text = "8",callback_data = "d8"),InlineKeyboardButton(text = "...",callback_data = "d9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back22')
		],
	],
)


# XOD-dog ???????????????????????
xoddog_menyu1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🥬Salatli xoddog",callback_data = "salatli_xoddog"),InlineKeyboardButton(text = "🌭Bez salat Xod-dog",callback_data = "salatsiz_xoddog")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back14')
		],
	],
)


xoddog_menyu2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🍣katta xoddog",callback_data = "katta_salatli"),InlineKeyboardButton(text = "🌭kichik Xod-dog",callback_data = "kichik_salatli")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back15')
		],
	],
)

xoddog_menyu5 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🍣katta xoddog",callback_data = "katta_siz"),InlineKeyboardButton(text = "🌭kichik Xod-dog",callback_data = "kichik_siz")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'back26')
		],
	],
)
xoddog_menyu3 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga99')
		],
	],
)

xoddog_menyu4 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga100')
		],
	],
)


#  PIZZA uchun >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

pizza_menyu1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🥩Peperonli",callback_data = "piperon1"),InlineKeyboardButton(text = "🍍Ananaslik",callback_data = "ananasli1")
		],
		[
				InlineKeyboardButton(text = "🥛Margaritli",callback_data = 'margarinli1')
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga3')
		],
	],
)

pizza_menyu2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga4')
		],
	],
)



ichimlik_menyu1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🍵Choy/☕️kofe",callback_data = 'choy'),InlineKeyboardButton(text = "🥤Yaxna ichimliklar",callback_data = "yaxna")
		],
		[
				InlineKeyboardButton(text = "🧋Fresh/sok",callback_data = 'sok')
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga5')
		],
	],
)
# kofelar
ichimlik_menyu2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "☕️Kofelar",callback_data = 'kofe'),InlineKeyboardButton(text = "🍵Choylar",callback_data = "choylar")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga6')
		],
	],
)

ichimlik_menyu3 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "😎Americano",callback_data = 'americano'),InlineKeyboardButton(text = "😎Capuchino",callback_data = "capuchino")
		],
		[
				InlineKeyboardButton(text = "😎Kofe 3v1",callback_data = '3v1'),InlineKeyboardButton(text = "😎Latte",callback_data = "latte")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga7')
		],
	],
)

ichimlik_menyu10= InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "😊Ko'k choy",callback_data = 'kuk'),InlineKeyboardButton(text = "😊Qora choy",callback_data = "qora")
		],
		[
				InlineKeyboardButton(text = "😊Limon choy",callback_data = 'limon')
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga13')
		],
	],
)


# yaxna

ichimlik_menyu4 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🍸Fanta",callback_data = 'fanta'),InlineKeyboardButton(text = "🥤Coca cola",callback_data = "cola")
		],
		[
				InlineKeyboardButton(text = "🍷Pepsi",callback_data = 'pepsi'),InlineKeyboardButton(text = "🧉Sprite",callback_data = "sprite")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga8')
		],
	],
)

 # Fresh l;kjhvgcvhjkljkhgcvhbjklknjbhv


ichimlik_menyu9 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🤗Bilis soki",callback_data = 'blis'),InlineKeyboardButton(text = "🤗Mevali fresh",callback_data = "meva")
		],
		
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga9')
		],
	],
)

ichimlik_menyu5 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga10')
		],
	],
)

ichimlik_menyu6 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga11')
		],
	],
)

ichimlik_menyu7 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga12')
		],
	],
)


ichimlik_menyu8 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga14')
		],
	],
)


#  DESERTLAR


desert_menyu1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🍯Assalim",callback_data = 'asal'),InlineKeyboardButton(text = "🍓Qulupnay",callback_data = "qulupnay")
		],
		[
				InlineKeyboardButton(text = "🍫Choko",callback_data = 'choko')
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga15')
		],
	],
)

desert_menyu2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga16')
		],
	],
)


# Sendvich

sendvich_menyu1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "Classik sendvich",callback_data = 'send_classik'),InlineKeyboardButton(text = "Tovuqli sendvich",callback_data = "sendvich_tovuq")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga17')
		],
	],
)


sendvich_menyu2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga18')
		],
	],
)


#  donar 

donar_menyu1 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "🍗Tovuqli",callback_data = 'donar_tovuq'),InlineKeyboardButton(text = "🥩Gushtli",callback_data = "donar_gushli")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga19')
		],
	],
)



donar_menyu2 = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
		],
		[
				InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
		],
		[
				InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
		],
		[
				InlineKeyboardButton(text = "⬅️Orqaga",callback_data = 'orqaga20')
		],
	],
)
