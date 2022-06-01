from config import TOKEN # bu  yerda tokenni (config.py fayilimizdan) chaqirib oldik
import logging
from aiogram import Bot, Dispatcher, executor, types
from button import * # bu yerda kinopkalarimizni chaqirib oldik (button.py dan)
from aiogram.types import Message,CallbackQuery
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("<b>Tilni tanlang</b>",parse_mode = 'HTML',reply_markup = til)

@dp.message_handler(text = "🇺🇿 O'zbekcha")
async def uzb(message: types.Message):
    await message.answer("<b>Iltimos pastdagi knopkalardan tanlang👇👇👇</b>",parse_mode = 'HTML',reply_markup = tur)

#Menyu uchun

@dp.message_handler(text="📖Menyu")
async def men(message: types.Message):
    await message.answer("<b>Kategoryadan tanlang </b>",parse_mode = 'HTML',reply_markup = menyu)

# lavash uchun katta kichikligi
@dp.callback_query_handler(text="lavash")
async def lav_vash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/lavash.jpg','rb'),
        caption = """Lavash turini tanlang""",reply_markup = lavash_menyu2)
    await call.message.delete()

# Tovuqli lavash uchun
@dp.callback_query_handler(text="tovuqli")
async def tovuqli_lav(call:CallbackQuery):
    await call.message.answer("<b> Tovuqli lavash turini tanlang </b>",parse_mode = 'HTML',reply_markup = lavash_menyu3)

@dp.callback_query_handler(text="mini_tovuq")
async def tovuqli_soni(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/lavashtovuqli.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan lavash
    go'shtli mini tovuqli lavash
    Narxi:19000
    Iltimos sonini tanlang""",reply_markup = lavash_menyu5)
    await call.message.delete()

@dp.callback_query_handler(text="big_tovuq")
async def tovuqli_soni(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/lavashtovuqli.jpg','rb'),
        caption = """ Hurmatli mijoz
     siz tanlagan lavash
     go'shtli Big tovuqli lavash
     Narxi:23000
     Iltimos sonini tanlang""",reply_markup = lavash_menyu5)
    await call.message.delete()

@dp.callback_query_handler(text="classik_tovuq")
async def tovuqli_soni(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/lavashtovuqli.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan lavash
    go'shtli Classik tovuqli lavash
    Narxi:21000
    Iltimos sonini tanlang""",parse_mode = 'HTML',reply_markup = lavash_menyu5)
    await call.message.delete()
# Mini tovuqli lavash uchun



#go'shtli lavash uchun
@dp.callback_query_handler(text="gushtli")
async def gushtli_lav(call:CallbackQuery):
    await call.message.answer("<b> Go'shtli lavash turini tanlang </b>",parse_mode = 'HTML',reply_markup = lavash_menyu4)

@dp.callback_query_handler(text="mini_gush")
async def lav_vash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/lavash1.jpg','rb'),
        caption = """ Hurmatli mijoz
    siz tanlagan lavash
    go'shtli mini lavash
    Narxi:19000
    Iltimos sonini tanlang """,reply_markup = lavash_menyu6)
    await call.message.delete()

@dp.callback_query_handler(text="big_gush")
async def lav_vash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/lavash1.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan lavash
    go'shtli Big lavash
    Narxi:23000
    Iltimos sonini tanlang""",reply_markup = lavash_menyu6)
    await call.message.delete()


@dp.callback_query_handler(text="classik_gush")
async def lav_vash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/lavash1.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan lavash
    go'shtli Classik lavash
    Narxi:21000
    Iltimos sonini tanlang""",reply_markup = lavash_menyu6)
    await call.message.delete()



#pishloqli lavash uchun
@dp.callback_query_handler(text="pishloq")
async def gushtli_lav(call:CallbackQuery):
    await call.message.answer("<b> Pishloqli lavash turini tanlang </b>",parse_mode = 'HTML',reply_markup = lavash_menyu9)

@dp.callback_query_handler(text="mini_pish")
async def lav_vash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/lavash1.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan lavash
    pishloqli mini lavash
    Narxi:16000
    Iltimos sonini tanlang""",reply_markup = lavash_menyu7)
    await call.message.delete()

@dp.callback_query_handler(text="big_pish")
async def lav_vash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/lavash1.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan lavash
    pishloqli Big lavash
    Narxi:19000
    Iltimos sonini tanlang""",reply_markup = lavash_menyu7)
    await call.message.delete()

@dp.callback_query_handler(text="classik_pish")
async def lav_vash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/lavash1.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan lavash
    pishloqli Classik lavash
    Narxi:17000
    Iltimos sonini tanlang""",reply_markup = lavash_menyu7)
    await call.message.delete()



# Tandir lavash uchun
@dp.callback_query_handler(text="tandir")
async def gushtli_lav(call:CallbackQuery):
    await call.message.answer("<b> Tandir lavash turini tanlang </b>",parse_mode = 'HTML',reply_markup = lavash_menyu10)

@dp.callback_query_handler(text="mini_tan")
async def lav_vash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/qalampirlavash.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan lavash
    tandir mini lavash
    Narxi:20000
    Iltimos sonini tanlang""",reply_markup = lavash_menyu8)
    await call.message.delete()

@dp.callback_query_handler(text="big_tan")
async def lav_vash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/qalampirlavash.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan lavash
    tandir Big lavash
    Narxi:26000
    Iltimos sonini tanlang""",reply_markup = lavash_menyu8)
    await call.message.delete()

@dp.callback_query_handler(text="classik_tan")
async def lav_vash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/qalampirlavash.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan lavash
    tandir Classik lavash
    Narxi:23000
    Iltimos sonini tanlang""",reply_markup = lavash_menyu8)
    await call.message.delete()



# shaurma uchun

@dp.callback_query_handler(text="shaurma")
async def sha_urma(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/shourmamenu.jpg','rb'),
        caption = """Shourma turini tanlang""",reply_markup = shaurma_menyu1)
    await call.message.delete()


@dp.callback_query_handler(text="go'shli")
async def sha_urma(call:CallbackQuery):
    await call.message.answer("<b> Go'shli shourma shaklini tanlang </b>",parse_mode = 'HTML',reply_markup = shaurma_menyu2)

@dp.callback_query_handler(text="katta_gushli")
async def sha_urma(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/molgushli.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan shourma
    go'shtli katta shourma
    Narxi:24000
    Iltimos sonini tanlang""",reply_markup = shaurma_menyu3)
    await call.message.delete()

@dp.callback_query_handler(text="kichig_gushli")
async def sha_urma(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/molgushli.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan shourma
    go'shtli kichik shourma
    Narxi:23000
    Iltimos sonini tanlang""",reply_markup = shaurma_menyu3)
    await call.message.delete()

@dp.callback_query_handler(text="achchiq")
async def sha_urma(call:CallbackQuery):
    await call.message.answer("<b>Achchiq shourma shaklini tanlang </b>",parse_mode = 'HTML',reply_markup = shaurma_menyu5)

@dp.callback_query_handler(text="katta_achchiq")
async def sha_urma(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/molgushli.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan shourma
    achchiq katta shourma
    Narxi:22000
    Iltimos sonini tanlang""",reply_markup = shaurma_menyu4)
    await call.message.delete()

@dp.callback_query_handler(text="kichig_achchiq")
async def sha_urma(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/molgushli.jpg','rb'),
        caption = """Hurmatli mijoz
        siz tanlagan shourma
        achchiq kichik shourma
        Narxi:20000
        Iltimos sonini tanlang""",reply_markup = shaurma_menyu4)
    await call.message.delete()

@dp.callback_query_handler(text="tovuq")
async def sha_urma(call:CallbackQuery):
    await call.message.answer("<b> Tovuqli shourma shaklini tanlang </b>",parse_mode = 'HTML',reply_markup = shaurma_menyu9)

@dp.callback_query_handler(text="katta_tovuq1")
async def sha_urma(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/shourmatovuq.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan shourma
    tovuqli katta shourma
    Narxi:23000
    Iltimos sonini tanlang""",reply_markup = shaurma_menyu7)
    await call.message.delete()

@dp.callback_query_handler(text="kichig_tovuq1")
async def sha_urma(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/shourmatovuq.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan shourma
    tovuqli kichik shourma
    Narxi:21000
    Iltimos sonini tanlang""",reply_markup = shaurma_menyu7)
    await call.message.delete()

@dp.callback_query_handler(text="achchig'i")
async def sha_urma(call:CallbackQuery):
    await call.message.answer("<b> Tovuqli achchig' shourma shaklini tanlang </b>",parse_mode = 'HTML',reply_markup = shaurma_menyu6)

@dp.callback_query_handler(text="katta_achchigi1")
async def sha_urma(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/shourmatovuq.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan shourma
    tovuqli katta acchchig' shourma
    Narxi:22000
    Iltimos sonini tanlang""",reply_markup = shaurma_menyu8)
    await call.message.delete()

@dp.callback_query_handler(text="kichig_achchig'i1")
async def sha_urma(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/shourmatovuq.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan shourma
    tovuqli kichik achchig' shourma
    Narxi:19000
    Iltimos sonini tanlang""",reply_markup = shaurma_menyu8)
    await call.message.delete()




#Burger uchun #############################
@dp.callback_query_handler(text="burger")
async def bur_ger(call:CallbackQuery):
    await call.message.answer("<b>Burger turini aniqlang</b>",parse_mode = 'HTML',reply_markup = burger_menyu1)

@dp.callback_query_handler(text="gamburger")
async def bur_ger(call:CallbackQuery):
    await call.message.answer("<b>Gamburger shaklini tanlang</b>",parse_mode = 'HTML',reply_markup = burger_menyu2)

@dp.callback_query_handler(text="kat_bur")
async def bur_ger(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/gamburger.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan burger
    Katta gamburger
    Narxi:21000
    Iltimos sonini tanlang""",reply_markup = burger_menyu3)
    await call.message.delete()

@dp.callback_query_handler(text="kich_bur")
async def bur_ger(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/gamburger.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan burger
    Kichik gamburger
    Narxi:18000
    Iltimos sonini tanlang""",reply_markup = burger_menyu3)
    await call.message.delete()

@dp.callback_query_handler(text="chizburger")
async def bur_ger(call:CallbackQuery):
    await call.message.answer("<b> Chizburger burger turini tanlang</b>",parse_mode = 'HTML',reply_markup = burger_menyu5)

@dp.callback_query_handler(text="kat_chiz")
async def bur_ger(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/chizburger.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan burger
    Katta chizburger
    Narxi:19000
    Iltimos sonini tanlang""",reply_markup = burger_menyu4)
    await call.message.delete()

@dp.callback_query_handler(text="kich_chiz")
async def bur_ger(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/chizburger.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan shourma
    Kichik chizburger
    Narxi:17000
    Iltimos sonini tanlang""",reply_markup = burger_menyu4)
    await call.message.delete() 



#xod dog uchun AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

@dp.callback_query_handler(text="xod-dog")
async def xod_dog(call:CallbackQuery):
    await call.message.answer("<b>xod-dog turini tanlang</b>",parse_mode = 'HTML',reply_markup = xoddog_menyu1)

@dp.callback_query_handler(text="salatli_xoddog")
async def xod_dog(call:CallbackQuery):
    await call.message.answer("<b>Salatli xod-dog shaklini tanlang</b>",parse_mode = 'HTML',reply_markup = xoddog_menyu2)


@dp.callback_query_handler(text="katta_salatli")
async def xod_dog(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/hoddog.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan Xod-dog
    Katta salatli Xod-dog
    Narxi:15000
    Iltimos sonini tanlang""",reply_markup = xoddog_menyu3)
    await call.message.delete() 

@dp.callback_query_handler(text="kichik_salatli")
async def xod_dog(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/hoddog1sasiskali.jpg','rb'),
        caption = """Hurmatli mijoz
        siz tanlagan Xod-dog
        Kichik salatli Xod-dog
        Narxi:12000
        Iltimos sonini tanlang""",reply_markup = xoddog_menyu3)
    await call.message.delete()

@dp.callback_query_handler(text="salatsiz_xoddog")
async def xod_dog(call:CallbackQuery):
    await call.message.answer("<b>Salatsiz xod-dog shaklini tanlang</b>",parse_mode = 'HTML',reply_markup = xoddog_menyu5)

@dp.callback_query_handler(text="katta_siz")
async def xod_dog(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/classikhoddog.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan Xod-dog
    Katta salatsiz Xod-dog
    Narxi:14000
    Iltimos sonini tanlang""",reply_markup = xoddog_menyu4)
    await call.message.delete()

@dp.callback_query_handler(text="kichik_siz")
async def xod_dog(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/classikhoddog.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan Xod-dog
    Kichik salatsiz Xod-dog
    Narxi:11000
    Iltimos sonini tanlang""",reply_markup = xoddog_menyu4)
    await call.message.delete()



# Pizza uchun ..................................................................

@dp.callback_query_handler(text="pizza")
async def pitsa(call:CallbackQuery):
    await call.message.answer("<b>Pizza turini tanlang turini tanlang</b>",parse_mode = 'HTML',reply_markup = pizza_menyu1)

@dp.callback_query_handler(text="piperon1")
async def pitsa(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/piperon.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan pizza
    Piperonli pizza
    Narxi:35000
    Iltimos sonini tanlang""",reply_markup = pizza_menyu2)
    await call.message.delete()


@dp.callback_query_handler(text="ananasli1")
async def pitsa(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/ananas.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan pizza
    Ananasli pizza
    Narxi:30000
    Iltimos sonini tanlang""",reply_markup = pizza_menyu2)
    await call.message.delete()    


@dp.callback_query_handler(text="margarinli1")
async def pitsa(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/margaritta.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan pizza
    Margarinli pizza
    Narxi:25000
    Iltimos sonini tanlang""",reply_markup = pizza_menyu2)
    await call.message.delete()  


# ICHIMLIKLAR ?????????????????????????????????????????

@dp.callback_query_handler(text="ichimliklar")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Iltimos ichimlik turini tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu1)

@dp.callback_query_handler(text="choy")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryadan tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu2)

@dp.callback_query_handler(text="kofe")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryadan tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu3)


@dp.callback_query_handler(text="americano")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/americano.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan ichimlik americano
    Narxi:5000
    ltimos sonini tanlang""",reply_markup = ichimlik_menyu5)
    await call.message.delete()

@dp.callback_query_handler(text="capuchino")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/americano.jpg','rb'),
        caption = """Hurmatli mijoz
        siz tanlagan ichimlik capuchino
        Narxi:7000
        ltimos sonini tanlang""",reply_markup = ichimlik_menyu5)
    await call.message.delete()


@dp.callback_query_handler(text="3v1")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/3v1.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan ichimlik 3v1 cofe
    Narxi:4000
    ltimos sonini tanlang""",reply_markup = ichimlik_menyu5)
    await call.message.delete()


@dp.callback_query_handler(text="latte")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/latte.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan ichimlik latte
    Narxi:8000
    ltimos sonini tanlang""",reply_markup = ichimlik_menyu5)
    await call.message.delete()


@dp.callback_query_handler(text="choylar")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryadan tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu10)


@dp.callback_query_handler(text="kuk")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/kukchoy.jpg','rb'),
        caption = """Hurmatli mijoz
        siz tanlagan ichimlik kuk choy
        Narxi:2000
        ltimos sonini tanlang""",reply_markup = ichimlik_menyu6)
    await call.message.delete()

@dp.callback_query_handler(text="qora")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/kukchoy.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan ichimlik qora choy
    Narxi:2000
    ltimos sonini tanlang""",reply_markup = ichimlik_menyu6)
    await call.message.delete()

@dp.callback_query_handler(text="limon")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/choylimon.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan ichimlik limon choy
    Narxi:3000
    ltimos sonini tanlang""",reply_markup = ichimlik_menyu6)
    await call.message.delete()


# yAXAN

@dp.callback_query_handler(text="yaxna")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryadan tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu4)

@dp.callback_query_handler(text="fanta")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/fanta.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan ichimlik Fanta
    Narxi:10000
    ltimos sonini tanlang""",reply_markup = ichimlik_menyu7)
    await call.message.delete()


@dp.callback_query_handler(text="cola")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/cocacola.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan ichimlik Coca-cola
    Narxi:10000
    ltimos sonini tanlang""",reply_markup = ichimlik_menyu7)
    await call.message.delete()

@dp.callback_query_handler(text="pepsi")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/pepsi.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan ichimlik Pepsi
    Narxi:10000
    ltimos sonini tanlang""",reply_markup = ichimlik_menyu7)
    await call.message.delete()

@dp.callback_query_handler(text="sprite")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/sprite.jpg','rb'),
        caption = """>Hurmatli mijoz
    siz tanlagan ichimlik Sprite
    Narxi:9000
    ltimos sonini tanlang""",reply_markup = ichimlik_menyu7)
    await call.message.delete()

# sok """""""""""""""""""""""""""''

@dp.callback_query_handler(text="sok")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryadan tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu9)

@dp.callback_query_handler(text="blis")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/sok.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan ichimlik Bilis soki
    Narxi:8000 I
    ltimos sonini tanlang""",reply_markup = ichimlik_menyu8)
    await call.message.delete()

@dp.callback_query_handler(text="meva")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/meali.lpg.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan ichimlik Mevali sok
    Narxi:8000 
    ltimos sonini tanlang""",reply_markup = ichimlik_menyu8)
    await call.message.delete()


# Desertlar   LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL

@dp.callback_query_handler(text="desertlar")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/desertmenu.jpg','rb'),
        caption = """Desert Kategoryasini tanlang""",reply_markup = desert_menyu1)
    await call.message.delete()


@dp.callback_query_handler(text="asal")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/assalim.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan desert Assalim deserti
    Narxi:14000
    ltimos sonini tanlang""",reply_markup = desert_menyu2)
    await call.message.delete()

@dp.callback_query_handler(text="qulupnay")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/qulupnay.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan desert Qulupnayli desert
    Narxi:13000
    ltimos sonini tanlangg""",reply_markup = desert_menyu2)
    await call.message.delete()

@dp.callback_query_handler(text="choko")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/choko.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan desert Choko desert
    Narxi:15000
    ltimos sonini tanlang""",reply_markup = desert_menyu2)
    await call.message.delete()


#  Boshqa PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP

@dp.callback_query_handler(text="boshqa")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>👇👇👇👇👇👇</b>",parse_mode = 'HTML',reply_markup = xizmatlar)




# sendvich AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA


@dp.callback_query_handler(text="sendvich")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Sendvich turini tanlamg</b>",parse_mode = 'HTML',reply_markup = sendvich_menyu1)

@dp.callback_query_handler(text="send_classik")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/sendvich.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan sendvich classik
    Narxi:15000
    ltimos sonini tanlang""",reply_markup = sendvich_menyu2)
    await call.message.delete()

@dp.callback_query_handler(text="sendvich_tovuq")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/sendvich.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan sendvich Tovuqli
    Narxi:18000
    ltimos sonini tanlang""",reply_markup = sendvich_menyu2)
    await call.message.delete()

# Donar

@dp.callback_query_handler(text="donar")
async def donar1(call:CallbackQuery):
    await call.message.answer("<b>Donar turini tanlamg</b>",parse_mode = 'HTML',reply_markup = donar_menyu1)



@dp.callback_query_handler(text="donar_tovuq")
async def donar1(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/donartovuqli.jpg','rb'),
        caption ="""Hurmatli mijoz
    siz tanlagan Donar Tovuqli
    Narxi:23000
    ltimos sonini tanlang""",reply_markup = donar_menyu2)
    await call.message.delete()


@dp.callback_query_handler(text="donar_gushli")
async def donar1(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/donargushli.jpg','rb'),
        caption = """Hurmatli mijoz
    siz tanlagan Donar Gushli
    Narxi:25000
    ltimos sonini tanlang""",reply_markup = donar_menyu2)
    await call.message.delete()



# orqaga ###########################################################################################################3

@dp.callback_query_handler(text="back3")
async def nazad5(call:CallbackQuery):
    await call.message.answer("<b>Kategoryadan tanlang</b>",parse_mode = 'HTML',reply_markup = menyu)

@dp.callback_query_handler(text="back4")
async def nazad5(call:CallbackQuery):
    await call.message.answer("<b>Lavash turini tanlang </b>",parse_mode = 'HTML',reply_markup = lavash_menyu2)

@dp.callback_query_handler(text="back5")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b>Lavash turini tanlang </b>",parse_mode = 'HTML',reply_markup = lavash_menyu2)

@dp.callback_query_handler(text="back6")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b>Tovuqli lavash turini tanlang </b>",parse_mode = 'HTML',reply_markup = lavash_menyu3)

@dp.callback_query_handler(text="back7")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b>Go'shtli lavash turini tanlang </b>",parse_mode = 'HTML',reply_markup = lavash_menyu4)

@dp.callback_query_handler(text="back16")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b>Pishkoqli lavash turini tanlang </b>",parse_mode = 'HTML',reply_markup = lavash_menyu9)

@dp.callback_query_handler(text="back17")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b>Tandirli lavash turini tanlang </b>",parse_mode = 'HTML',reply_markup = lavash_menyu10)

@dp.callback_query_handler(text="back18")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b>Lavash turini tanlang </b>",parse_mode = 'HTML',reply_markup = lavash_menyu2)

@dp.callback_query_handler(text="back19")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b>Lavash turini tanlang </b>",parse_mode = 'HTML',reply_markup = lavash_menyu2)

#shaurma orqaga @@@@@@@@@@@@@@@@@

@dp.callback_query_handler(text="back8")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b>Kategoryadan tanlang</b>",parse_mode = 'HTML',reply_markup = menyu)

@dp.callback_query_handler(text="back9")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b>Shourma turini tanlang </b>",parse_mode = 'HTML',reply_markup = shaurma_menyu1)

@dp.callback_query_handler(text="back24")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b>Shourma turini tanlang </b>",parse_mode = 'HTML',reply_markup = shaurma_menyu1)


@dp.callback_query_handler(text="back10")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b>Go'shli shourma shaklini tanlang</b>",parse_mode = 'HTML',reply_markup = shaurma_menyu2)

@dp.callback_query_handler(text="back23")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b> Go'shli achchiq shourma shaklini tanlang</b>",parse_mode = 'HTML',reply_markup = shaurma_menyu5)

@dp.callback_query_handler(text="back28")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b>Tovuqli  shourma shaklini tanlang</b>",parse_mode = 'HTML',reply_markup = shaurma_menyu6)

@dp.callback_query_handler(text="back29")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b>Tovuqli achchiq shourma shaklini tanlang</b>",parse_mode = 'HTML',reply_markup = shaurma_menyu6)

@dp.callback_query_handler(text="back27")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b>Shourma turini tanlang </b>",parse_mode = 'HTML',reply_markup = shaurma_menyu1)

@dp.callback_query_handler(text="back30")
async def nazad1(call:CallbackQuery):
    await call.message.answer("<b>Shourma turini tanlang </b>",parse_mode = 'HTML',reply_markup = shaurma_menyu1)



# Burger orqaga????????????????????
@dp.callback_query_handler(text="back11")
async def nazad2(call:CallbackQuery):
    await call.message.answer("<b>Kategoryadan tanlang</b>",parse_mode = 'HTML',reply_markup = menyu)

@dp.callback_query_handler(text="back12")
async def nazad2(call:CallbackQuery):
    await call.message.answer("<b>Burger turini aniqlang</b>",parse_mode = 'HTML',reply_markup = burger_menyu1)

@dp.callback_query_handler(text="back25")
async def nazad2(call:CallbackQuery):
    await call.message.answer("<b>Burger turini aniqlang</b>",parse_mode = 'HTML',reply_markup = burger_menyu1)

@dp.callback_query_handler(text="back13")
async def nazad2(call:CallbackQuery):
    await call.message.answer("<b>Gamburger burger shaklini aniqlang</b>",parse_mode = 'HTML',reply_markup = burger_menyu2)

@dp.callback_query_handler(text="back22")
async def nazad2(call:CallbackQuery):
    await call.message.answer("<b>Chizburger burger shaklini aniqlang</b>",parse_mode = 'HTML',reply_markup = burger_menyu5)



# xod-dog orqagaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA yiban chiqmagan
@dp.callback_query_handler(text="back14")
async def nazad3(call:CallbackQuery):
    await call.message.answer("<b>Kategoryadan tanlang</b>",parse_mode = 'HTML',reply_markup = menyu)

@dp.callback_query_handler(text="back15")
async def nazad3(call:CallbackQuery):
    await call.message.answer("<b>Xod-dog turini aniqlang</b>",parse_mode = 'HTML',reply_markup = xoddog_menyu1)

@dp.callback_query_handler(text="back26")
async def nazad3(call:CallbackQuery):
    await call.message.answer("<b>Xod-dog turini aniqlang</b>",parse_mode = 'HTML',reply_markup = xoddog_menyu1)


@dp.callback_query_handler(text="orqaga99")
async def nazad4(call:CallbackQuery):
    await call.message.answer("<b>Salatli xod-dog shaklini tanlang</b>",parse_mode = 'HTML',reply_markup = xoddog_menyu2)

@dp.callback_query_handler(text="orqaga100")
async def nazad4(call:CallbackQuery):
    await call.message.answer("<b>Salatsiz xod-dog shaklini tanlang</b>",parse_mode = 'HTML',reply_markup = xoddog_menyu5)


# pizza orqaga>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.


@dp.callback_query_handler(text="orqaga3")
async def xod_dog(call:CallbackQuery):
    await call.message.answer("<b>Kategoryadan tanlang</b>",parse_mode = 'HTML',reply_markup = menyu)

@dp.callback_query_handler(text="orqaga4")
async def xod_dog(call:CallbackQuery):
    await call.message.answer("<b>Pizza turini tanlang turini tanlang</b>",parse_mode = 'HTML',reply_markup = pizza_menyu1)



#  ichimlik orqaga |||||||||||||||||||||||||||||||||||||||||||||


@dp.callback_query_handler(text="orqaga5")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = menyu)

@dp.callback_query_handler(text="orqaga6")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu1)

@dp.callback_query_handler(text="orqaga7")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu2)

@dp.callback_query_handler(text="orqaga10")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu3)

@dp.callback_query_handler(text="orqaga13")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu2)

@dp.callback_query_handler(text="orqaga11")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu10)


@dp.callback_query_handler(text="orqaga8")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu1)


@dp.callback_query_handler(text="orqaga12")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu4)


@dp.callback_query_handler(text="orqaga9")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu1)

@dp.callback_query_handler(text="orqaga14")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu9)


# Desert orqaga  """"""""""""""""""""""""""""""""""""""


@dp.callback_query_handler(text="orqaga15")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = menyu)


@dp.callback_query_handler(text="orqaga16")
async def suv(call:CallbackQuery):
    await call.message.answer("<b> Desert Kategoryasini tanlang</b>",parse_mode = 'HTML',reply_markup = desert_menyu1)


# ########################## sendvich

@dp.callback_query_handler(text="orqaga17")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = menyu)

@dp.callback_query_handler(text="orqaga18")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Sendvich turini tanlamg</b>",parse_mode = 'HTML',reply_markup = sendvich_menyu1)

#  donar aaaaaaaaaaaaa

@dp.callback_query_handler(text="orqaga19")
async def donar1(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = menyu)


@dp.callback_query_handler(text="orqaga20")
async def donar1(call:CallbackQuery):
    await call.message.answer("<b>Donar turini tanlamg</b>",parse_mode = 'HTML',reply_markup = donar_menyu1)


@dp.callback_query_handler(text="orqaga20")
async def donar1(call:CallbackQuery):
    await call.message.answer("<b>Donar turini tanlag</b>",parse_mode = 'HTML',reply_markup = donar_menyu1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)