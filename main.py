import logging
from config import TOKEN
from buttons import* 
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message,CallbackQuery 
import sqlite3

# Configure logging
logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
 
   await message.reply("Tilni tanlang / Choose language",reply_markup=til)
   

@dp.callback_query_handler(text="uz")
async def till_tanlash(call: CallbackQuery):
   await call.message.answer("<b>Assolomu Alaykum!</b>",parse_mode="HTML",reply_markup=test)


@dp.callback_query_handler(text="en")
async def till_tanlash(call: CallbackQuery):
   await call.message.answer("<b>Hi!</b>",parse_mode="HTML",reply_markup=test)


@dp.callback_query_handler(text="bel")
async def Menyu1(call: CallbackQuery):
   await call.message.answer("<b>Nima buyurasiz</b>",parse_mode="HTML",reply_markup=mahsulot) 

###########LAVASH##############

@dp.callback_query_handler(text="lavash")
async def Menyu2(call: CallbackQuery):
   await call.message.answer("<b>Qanday lavash</b>",parse_mode="HTML",reply_markup=lavash1) 


@dp.callback_query_handler(text="lav1")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Kategoriyalardan birini tanlang</b>",parse_mode="HTML",reply_markup=lavash11)




@dp.callback_query_handler(text="klas11")
async def Lavash_menyu(call: CallbackQuery): 
   await call.message.answer_photo(
      photo=open('photo/sirlilavsh.jpg','rb'),
      caption="<b>Tarkibi:Lavash xamir,pishloq,gosht,kartoshka fri,bodring,pomidor,sous,mayonez,ketchup \n Narxi:19.000 so'm</b>",parse_mode="HTML",reply_markup=lavsonlar11)


@dp.callback_query_handler(text="mini11")
async def Lavash_menyu(call: CallbackQuery):      
    await call.message.answer_photo(
      photo=open('photo/lavashrasm.jpg','rb'),
      caption="<b>Tarkib:Lavash xamir,tovuq va mol go'shti,kartoshka fri,pomidor,bodring,mayonez,sous,ketchup \nNarxi:20.000 so'm</b>",parse_mode="HTML",reply_markup=lavsonlar11)


@dp.callback_query_handler(text="back11")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=lavash1)



@dp.callback_query_handler(text="back")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Kategoriyalardan birini tanlang</b>",parse_mode="HTML",reply_markup=lavash11)




@dp.callback_query_handler(text="lavback11")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=lavash11)




@dp.callback_query_handler(text="lav2")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Kategoriyalardan birini tanlang</b>",parse_mode="HTML",reply_markup=lavash22)
   

@dp.callback_query_handler(text="klas22")
async def Lavash_menyu(call: CallbackQuery):      
  await call.message.answer_photo(
      photo=open('photo/lavashrasm.jpg','rb'),
      caption="<b>Tarkibi:Lavash xamir,mol go'shti,kartoshka fri,bodring,pomidor,mayonez,sous,ketchup\n Narxi Katta:18.000 so'm\n Mini:16.000</b>",parse_mode="HTML",reply_markup=lavsonlar22)


@dp.callback_query_handler(text="mini22")
async def Lavash_menyu(call: CallbackQuery):      
   await call.message.answer_photo(
      photo=open('photo/lavashrasm.jpg','rb'),
      caption="<b>Tarkibi:Lavash xamir,mol go'shti,kartoshka fri,bodring,pomidor,mayonez,sous,ketchup\n Narxi Katta:18.000 so'm\n Mini:16.000</b>",parse_mode="HTML",reply_markup=lavsonlar22)

@dp.callback_query_handler(text="back22")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=lavash1)



@dp.callback_query_handler(text="lavback22")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=lavash22)






@dp.callback_query_handler(text="lav3")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Kategoriyalardan biridan tanlang</b>",parse_mode="HTML",reply_markup=lavash33)

@dp.callback_query_handler(text="klas33")
async def Lavash_menyu(call: CallbackQuery):      
  await call.message.answer_photo(
      photo=open('photo/tovuqlilavash.jpg','rb'),
      caption="<b>Tarkibi:Lavash xamir,mol go'shti,kartoshka fri,bodring,pomidor,mayonez,sous,ketchup\n Narxi Katta:18.000 so'm</b>",parse_mode="HTML",reply_markup=lavsonlar33)


@dp.callback_query_handler(text="mini33")
async def Lavash_menyu(call: CallbackQuery):      
   await call.message.answer_photo(
      photo=open('photo/tovuqlilavash.jpg','rb'),
      caption="<b>Tarkibi:Lavash xamir,mol go'shti,kartoshka fri,bodring,pomidor,mayonez,sous,ketchup\n Narxi:16.000</b>",parse_mode="HTML",reply_markup=lavsonlar33)


@dp.callback_query_handler(text="back33")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=lavash1)



@dp.callback_query_handler(text="lavback33")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=lavash33)




@dp.callback_query_handler(text="lav4")
async def lavash_ortga(call: CallbackQuery):
   await call.message.answer("<b>Kategoriyalardan biridan tanlang</b>",parse_mode="HTML",reply_markup=lavash44)


@dp.callback_query_handler(text="klas44")
async def Lavash_menyu(call: CallbackQuery):      
  await call.message.answer_photo(
      photo=open('photo/lavashrasm.jpg','rb'),
      caption="<b>Tarkibi:Lavash xamir,mol go'shti,kartoshka fri,bodring,pomidor,mayonez,sous,ketchup\n Narxi Katta:18.000 so'm</b>",parse_mode="HTML",reply_markup=lavsonlar44)


@dp.callback_query_handler(text="mini44")
async def Lavash_menyu(call: CallbackQuery):      
   await call.message.answer_photo(
      photo=open('photo/lavashrasm.jpg','rb'),
      caption="<b>Tarkibi:Lavash xamir,mol go'shti,kartoshka fri,bodring,pomidor,mayonez,sous,ketchup\n Narxi:16.000</b>",parse_mode="HTML",reply_markup=lavsonlar44)


@dp.callback_query_handler(text="back44")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=lavash1)




@dp.callback_query_handler(text="lavback44")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=lavash44)




@dp.callback_query_handler(text="ortga")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Orqaga</b>",parse_mode="HTML",reply_markup=mahsulot)






@dp.callback_query_handler(text="klas")
async def Lavash_menyu(call: CallbackQuery):      
   await call.message.answer("<b>Nechta lavash</b>",parse_mode="HTML",reply_markup=sonlar)


@dp.callback_query_handler(text="mini")
async def Lavash_menyu(call: CallbackQuery):      
   await call.message.answer("<b>Nechta lavash</b>",parse_mode="HTML",reply_markup=sonlar)


@dp.callback_query_handler(text="back")
async def Lavash_menyu(call: CallbackQuery):      
   await call.message.answer("<b>Menyu</b>",parse_mode="HTML",reply_markup=lavash1)






######################LAVASH TUGASHI###############################

############################GAMBURGERNI BOSHLANISHI########################

@dp.callback_query_handler(text="gam")
async def Menyu(call: CallbackQuery):
   await call.message.answer("<b>Qanday gamburger</b>",parse_mode="HTML",reply_markup=gamburger1)


@dp.callback_query_handler(text="sir")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer("<b>Kategoriyalardan birini tanlang</b>",parse_mode="HTML",reply_markup=gamburger11)

   

@dp.callback_query_handler(text="gamklas11")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/gamburger1.jpg','rb'),
      caption="<b>Tarkibi:Gamburger noni,mol go'shti,pishloq,pomidor,bodring,sous,mayonez,ketchup,salat bargi \n Narxi katta:25.000</b>",parse_mode="HTML",reply_markup=gamsonlar11)


@dp.callback_query_handler(text="gammini11")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/gamburger1.jpg','rb'),
      caption="<b>Tarkibi:Gamburger noni,mol go'shti,pishloq,pomidor,bodring,sous,mayonez,ketchup,salat bargi \n Narxi:23.000</b>",parse_mode="HTML",reply_markup=gamsonlar11)

@dp.callback_query_handler(text="gambackson11")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=gamburger11)



@dp.callback_query_handler(text="gamback11")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=gamburger1)




@dp.callback_query_handler(text="gosht")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer("<b>Kategoriyalardan birini tanlang</b>",parse_mode="HTML",reply_markup=gamburger22)


@dp.callback_query_handler(text="gamklas22")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/gamburger1.jpg','rb'),
      caption="<b>Tarkibi:Mol go'shti,gamburger noni,bodring,pomidor,mayonez,sous,ketchup,salat bargi\n Narxi:24.000 </b>",parse_mode="HTML",reply_markup=gamsonlar22)


@dp.callback_query_handler(text="gammini22")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/gamburger1.jpg','rb'),
      caption="<b>Tarkibi:Mol go'shti,gamburger noni,bodring,pomidor,mayonez,sous,ketchup,salat bargi\n Narxi 22.000</b>",parse_mode="HTML",reply_markup=gamsonlar22)


@dp.callback_query_handler(text="gambackson22")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=gamburger22)



@dp.callback_query_handler(text="gamback22")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=gamburger1)


@dp.callback_query_handler(text="orqaga")
async def gam_ortga(call: CallbackQuery):
   await call.message.answer("<b>Ortga</b>",parse_mode="HTML",reply_markup=mahsulot)



@dp.callback_query_handler(text="back")
async def gam_menyu(call: CallbackQuery):      
   await call.message.answer("<b>Ortga</b>",parse_mode="HTML",reply_markup=mahsulot) 

##################################GAMBURGER TUGADI@#######################################

 
##################################DONAR BOSHLAMISHI#########################################

@dp.callback_query_handler(text="don")
async def Menyu(call: CallbackQuery):
   await call.message.answer("<b>Nima buyurasiz</b>",parse_mode="HTML",reply_markup=donar1) 



@dp.callback_query_handler(text="donsirli")
async def don_menyu(call: CallbackQuery):
   await call.message.answer("<b>Kategoriyalardan birini tanlang</b>",parse_mode="HTML",reply_markup=donar11)

@dp.callback_query_handler(text="donklas11")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/goshtlidonar.jpg','rb'),
      caption="<b>Tarkibi:Donar noni,mol go'shti,pishloq,kartoshka fri,pomidor,bodring,mayonez,sous,ketchup \n Narxi:20.000so'm</b>",parse_mode="HTML",reply_markup=donsonlar11) 


@dp.callback_query_handler(text="donmini11")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/goshtlidonar.jpg','rb'),
      caption="<b>Tarkibi:Donar noni,mol go'shti,pishloq,kartoshka fri,pomidor,bodring,mayonez,sous,ketchup \n Narxi:17.000so'm</b>",parse_mode="HTML",reply_markup=donsonlar11) 

@dp.callback_query_handler(text="donbackson11")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=donar11)



@dp.callback_query_handler(text="donback11")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=donar1)



@dp.callback_query_handler(text="dongoshtli")
async def don_menyu(call: CallbackQuery):
   await call.message.answer("<b>Kategoriyalardan birini tanlang</b>",parse_mode="HTML",reply_markup=donar22)

@dp.callback_query_handler(text="donklas22")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/goshtlidonar.jpg','rb'),
      caption="<b>Tarkibi:Donar noni,mol go'shti,pishloq,kartoshka fri,pomidor,bodring,mayonez,sous,ketchup \n Narxi:20.000so'm</b>",parse_mode="HTML",reply_markup=donsonlar22) 


@dp.callback_query_handler(text="donmini22")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/goshtlidonar.jpg','rb'),
      caption="<b>Tarkibi:Donar noni,mol go'shti,pishloq,kartoshka fri,pomidor,bodring,mayonez,sous,ketchup \n Narxi:17.000so'm</b>",parse_mode="HTML",reply_markup=donsonlar22) 

@dp.callback_query_handler(text="donbackson22")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=donar22)



@dp.callback_query_handler(text="donback22")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=donar1)



@dp.callback_query_handler(text="menyuga")
async def don_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=mahsulot) 





############################################DONAR TUGADI##############################

###################################################SHAURMA BOSHLANDI#####################

@dp.callback_query_handler(text="shaur")
async def shaurma_menyu(call: CallbackQuery):
   await call.message.answer("<b>Qanday shaurma</b>",parse_mode="HTML",reply_markup=shaurma1) 


@dp.callback_query_handler(text="shasirli")
async def shaurma_menyu(call: CallbackQuery):
   await call.message.answer("<b>Kategoriyalardan birini tanlang</b>",parse_mode="HTML",reply_markup=shaurma11)

@dp.callback_query_handler(text="shaklas11")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/goshtlishaurma.jpg','rb'),
      caption="<b>Tarkibi:Shaurma ucuhun maxsus non,mol go'shti,pishloq,pomidor,bodring,mayonez,kartoshka fri,sous,ketchup \n Narxi:18.000so'm</b>",parse_mode="HTML",reply_markup=shasonlar11) 


@dp.callback_query_handler(text="shamini11")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/goshtlishaurma.jpg','rb'),
      caption="<b>Tarkibi:Shaurma ucuhun maxsus non,mol go'shti,pishloq,pomidor,bodring,mayonez,kartoshka fri,sous,ketchup \n Narxi:16.000</b>",parse_mode="HTML",reply_markup=shasonlar11) 

@dp.callback_query_handler(text="shabackson11")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=shaurma11)



@dp.callback_query_handler(text="shaback11")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=shaurma1)



@dp.callback_query_handler(text="shagoshtli")
async def shaurma_menyu(call: CallbackQuery):
   await call.message.answer("<b>Kategoriyalardan birini tanlang</b>",parse_mode="HTML",reply_markup=shaurma22)


@dp.callback_query_handler(text="shaklas22")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/goshtlishaurmaa.jpg','rb'),
      caption="<b>Tarkibi:Shaurma ucuhun maxsus non,mol go'shti,pishloq,pomidor,bodring,mayonez,kartoshka fri,sous,ketchup \n Narxi:18.000so'm</b>",parse_mode="HTML",reply_markup=shasonlar22) 


@dp.callback_query_handler(text="shamini22")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/goshtlishaurmaa.jpg','rb'),
      caption="<b>Tarkibi:Shaurma ucuhun maxsus non,mol go'shti,pishloq,pomidor,bodring,mayonez,kartoshka fri,sous,ketchup \n Narxi:16.000</b>",parse_mode="HTML",reply_markup=shasonlar22) 

@dp.callback_query_handler(text="shabackson22")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=shaurma22)



@dp.callback_query_handler(text="shaback22")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=shaurma1)





@dp.callback_query_handler(text="back")
async def shaurma_menyu(call: CallbackQuery):      
   await call.message.answer("<b>Ortga</b>",parse_mode="HTML",reply_markup=mahsulot)


###############################SHAURMA TUGADI######################################

################################SANDWICH BOSHLANDI#############################


@dp.callback_query_handler(text="sand")
async def Menyu(call: CallbackQuery):
   await call.message.answer("<b>Qanday sandwich</b>",parse_mode="HTML",reply_markup=sandwich1) 


@dp.callback_query_handler(text="sandsirli")
async def Menyu(call: CallbackQuery):
   await call.message.answer("<b>Kategoriyalardan birini tanlang</b>",parse_mode="HTML",reply_markup=sandwich11)



@dp.callback_query_handler(text="sandklas11")
async def gam_menyu(call: CallbackQuery):
    await call.message.answer_photo(
      photo=open('photo/sirlisandwich.jpg','rb'),
      caption="<b>Tarkibi:Sandwich noni,kolbasa,pishloq,bodring,pomidor,sous,mayonez,kartoshka fri,salat bargi \n Narxi:15.000so'm</b>",parse_mode="HTML",reply_markup=sandsonlar11) 



@dp.callback_query_handler(text="sandmini11")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/sirlisandwich.jpg','rb'),
      caption="<b>Tarkibi:Sandwich noni,kolbasa,pishloq,bodring,pomidor,sous,mayonez,kartoshka fri,salat bargi \n Narxi:10.000</b>",parse_mode="HTML",reply_markup=sandsonlar11) 


@dp.callback_query_handler(text="sandbackson11")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=sandwich11)



@dp.callback_query_handler(text="sandback11")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=sandwich1)

@dp.callback_query_handler(text="sandback")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=mahsulot)




@dp.callback_query_handler(text="sandgoshtli")
async def Menyu(call: CallbackQuery):
    await call.message.answer("<b>Kategoriyalardan birini tanlang</b>",parse_mode="HTML",reply_markup=sandwich22)




@dp.callback_query_handler(text="sandklas22")
async def gam_menyu(call: CallbackQuery):
    await call.message.answer_photo(
      photo=open('photo/goshtlisandwich.jpg','rb'),
      caption="<b>Tarkibi:Sandwich noni,mol go'shti,pomidor,bodring,sous,mayonez,kartoshka fri,salat bargi \n Narxi:17.000so'm</b>",parse_mode="HTML",reply_markup=sandsonlar22) 



@dp.callback_query_handler(text="sandmini22")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/goshtlisandwich.jpg','rb'),
      caption="<b>Tarkibi:Sandwich noni,mol go'shti,pomidor,bodring,sous,mayonez,kartoshka fri,salat bargi \n Narxi:14.000</b>",parse_mode="HTML",reply_markup=sandsonlar22) 


@dp.callback_query_handler(text="sandbackson22")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=sandwich22)



@dp.callback_query_handler(text="sandback22")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=sandwich1)

@dp.callback_query_handler(text="sandback")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=mahsulot)














@dp.callback_query_handler(text="orqagaa")
async def Menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish </b>",parse_mode="HTML",reply_markup=mahsulot) 


@dp.callback_query_handler(text="klasi")
async def sand_menyu(call: CallbackQuery):
   await call.message.answer("<b>Nechta katta sandwich</b>",parse_mode="HTML",reply_markup=sonlar) 


@dp.callback_query_handler(text="minis")
async def sand_menyu(call: CallbackQuery):
   await call.message.answer("<b>Nechta mini sandwich</b>",parse_mode="HTML",reply_markup=sonlar) 



@dp.callback_query_handler(text="back")
async def sand_menyu(call: CallbackQuery):      
   await call.message.answer("<b>Ortga</b>",parse_mode="HTML",reply_markup=mahsulot)



###############################SANDWICHNI TUGASHI#####################################

################################PITSANI BOSHLANISHI########################################



@dp.callback_query_handler(text="pitsa")
async def Menyu(call: CallbackQuery):
   await call.message.answer("<b>Qanday pitsa</b>",parse_mode="HTML",reply_markup=pitsa1) 



@dp.callback_query_handler(text="pitsirli")
async def Menyu(call: CallbackQuery):
   await call.message.answer("<b>Kategoriyalardan birini tanlang</b>",parse_mode="HTML",reply_markup=pitsa11)



@dp.callback_query_handler(text="pitklas11")
async def gam_menyu(call: CallbackQuery):
    await call.message.answer_photo(
      photo=open('photo/sirlipitsa.jpg','rb'),
      caption="<b>Tarkibi:Pitsa uchun maxsus non,pishloq,pomidor,bodring,ko'katlar,mayonez,sous,kartoshka fri,ketchup \n Narxi:31.000so'm</b>",parse_mode="HTML",reply_markup=pitsonlar11) 



@dp.callback_query_handler(text="pitmini11")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/sirlipitsa.jpg','rb'),
      caption="<b>Tarkibi:Pitsa uchun maxsus non,pishloq,pomidor,bodring,ko'katlar,mayonez,sous,kartoshka fri,ketchup \n Narxi:28.000so'm</b>",parse_mode="HTML",reply_markup=pitsonlar11) 


@dp.callback_query_handler(text="pitbackson11")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=pitsa11)



@dp.callback_query_handler(text="pitback11")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=pitsa1)

@dp.callback_query_handler(text="pitback")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=mahsulot)










@dp.callback_query_handler(text="pitgoshtli")
async def Menyu(call: CallbackQuery):
   await call.message.answer("<b>Kategoriyalardan birini tanlang</b>",parse_mode="HTML",reply_markup=pitsa22)


@dp.callback_query_handler(text="pitklas22")
async def gam_menyu(call: CallbackQuery):
    await call.message.answer_photo(
      photo=open('photo/goshtlipitsa.jpg','rb'),
      caption="<b>Tarkibi:Pitsa uchun maxsus non,pomidor,bodring,mayonez,ko'katlar,kartoshka fri,ketchup,ta'bga ko'ra ziravorlar\n Narxi:33.000so'm</b>",parse_mode="HTML",reply_markup=pitsonlar22) 



@dp.callback_query_handler(text="pitmini22")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/goshtlipitsa.jpg','rb'),
      caption="<b>Tarkibi:Pitsa uchun maxsus non,pomidor,bodring,mayonez,ko'katlar,kartoshka fri,ketchup,ta'bga ko'ra ziravorlar\n Narxi:31.000so'm</b>",parse_mode="HTML",reply_markup=pitsonlar22) 


@dp.callback_query_handler(text="pitbackson22")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=pitsa22)



@dp.callback_query_handler(text="pitback22")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=pitsa1)

@dp.callback_query_handler(text="pitback")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=mahsulot)







@dp.callback_query_handler(text="ortaga")
async def Menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish </b>",parse_mode="HTML",reply_markup=mahsulot) 

@dp.callback_query_handler(text="klasik")
async def don_menyu(call: CallbackQuery):
   await call.message.answer("<b>Nechta katta pitsa</b>",parse_mode="HTML",reply_markup=sonlar) 


@dp.callback_query_handler(text="minisk")
async def don_menyu(call: CallbackQuery):
   await call.message.answer("<b>Nechta mini pitsa</b>",parse_mode="HTML",reply_markup=sonlar) 



@dp.callback_query_handler(text="back")
async def pitsa_menyu(call: CallbackQuery):      
   await call.message.answer("<b>Ortga</b>",parse_mode="HTML",reply_markup=mahsulot)




############################################PITSA TUGASHI#####################################

################################CHIZBURGER BOSHLANISHI#########################################




@dp.callback_query_handler(text="chiz")
async def Menyu(call: CallbackQuery):
   await call.message.answer("<b>Qanday chizburger</b>",parse_mode="HTML",reply_markup=chiz1)



@dp.callback_query_handler(text="chizsirli")
async def Menyu(call: CallbackQuery):
   await call.message.answer("<b>Kategoriyalardan birini tanlang</b>",parse_mode="HTML",reply_markup=chiz11)


@dp.callback_query_handler(text="chizklas11")
async def gam_menyu(call: CallbackQuery):
    await call.message.answer_photo(
      photo=open('photo/iktalichiz.jpg','rb'),
      caption="<b>Tarkibi: Chizburger noni,pishloq,katlet,pomidor,salat bargi,mayonez,ketchup,bodring,sous,\n Narxi:22.000so'm</b>",parse_mode="HTML",reply_markup=chizsonlar11) 



@dp.callback_query_handler(text="chizmini11")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/iktalichiz.jpg','rb'),
      caption="<b>Tarkibi: Chizburger noni,pishloq,katlet,pomidor,salat bargi,mayonez,ketchup,bodring,sous,\n Narxi:18.000so'm</b>",parse_mode="HTML",reply_markup=chizsonlar11) 


@dp.callback_query_handler(text="chizbackson11")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=chiz11)



@dp.callback_query_handler(text="chizback11")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=chiz1)

@dp.callback_query_handler(text="chizback")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=mahsulot)






@dp.callback_query_handler(text="chizgoshtli")
async def Menyu(call: CallbackQuery):
   await call.message.answer("<b>Kategoriyalardan birini tanlang</b>",parse_mode="HTML",reply_markup=chiz22)

@dp.callback_query_handler(text="chizklas22")
async def gam_menyu(call: CallbackQuery):
    await call.message.answer_photo(
      photo=open('photo/iktalichiz.jpg','rb'),
      caption="<b>Tarkibi:Chizburger uchun maxsus non,katlet,mol go'shti,salat bargi,bodring,sous,ketchup,mayonez Narxi:23.000so'm</b>",parse_mode="HTML",reply_markup=chizsonlar22) 



@dp.callback_query_handler(text="chizmini22")
async def gam_menyu(call: CallbackQuery):
    await call.message.answer_photo(
      photo=open('photo/iktalichiz.jpg','rb'),
      caption="<b>Tarkibi:Chizburger uchun maxsus non,katlet,mol go'shti,salat bargi,bodring,sous,ketchup,mayonez Narxi:19.000so'm</b>",parse_mode="HTML",reply_markup=chizsonlar22) 


@dp.callback_query_handler(text="chizbackson22")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=chiz22)



@dp.callback_query_handler(text="chizback22")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=chiz1)

@dp.callback_query_handler(text="chizback")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=mahsulot)






@dp.callback_query_handler(text="ortaga")
async def Menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish </b>",parse_mode="HTML",reply_markup=mahsulot)


@dp.callback_query_handler(text="klasikk")
async def don_menyu(call: CallbackQuery):
   await call.message.answer("<b>Nechta katta chizburger</b>",parse_mode="HTML",reply_markup=sonlar) 


@dp.callback_query_handler(text="minik")
async def don_menyu(call: CallbackQuery):
   await call.message.answer("<b>Nechta mini chizburger</b>",parse_mode="HTML",reply_markup=sonlar) 



@dp.callback_query_handler(text="back")
async def chiz_menyu(call: CallbackQuery):      
   await call.message.answer("<b>Ortga</b>",parse_mode="HTML",reply_markup=mahsulot)


##########################################CHIZBURGER TUGASHI##################################3

#################################HOT DOG BOSHLANISHI##########################################


@dp.callback_query_handler(text="hot")
async def Menyu(call: CallbackQuery):
   await call.message.answer("<b>Qanday hot-dog</b>",parse_mode="HTML",reply_markup=hot1)



@dp.callback_query_handler(text="hotsirli")
async def Menyu(call: CallbackQuery):
   await call.message.answer("<b>Kategoriyalardan birini tanlang</b>",parse_mode="HTML",reply_markup=hot11)


@dp.callback_query_handler(text="hotklas11")
async def gam_menyu(call: CallbackQuery):
    await call.message.answer_photo(
      photo=open('photo/hodog.jpg','rb'),
      caption="<b>Tarkibi: Hot dog noni,sosiska,bodring,pomidor,ketchup,sous,mayonez\nNarxi:12.000so'm</b>",parse_mode="HTML",reply_markup=hotsonlar11) 



@dp.callback_query_handler(text="hotmini11")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/hodog.jpg','rb'),
      caption="<b>Tarkibi: Hot dog noni,sosiska,bodring,pomidor,ketchup,sous,mayonez\nNarxi:10.000so'm</b>",parse_mode="HTML",reply_markup=hotsonlar11) 


@dp.callback_query_handler(text="hotbackson11")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=hot11)



@dp.callback_query_handler(text="hotback11")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=hot1)

@dp.callback_query_handler(text="hotback")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=mahsulot)






@dp.callback_query_handler(text="hotgoshtli")
async def Menyu(call: CallbackQuery):
   await call.message.answer("<b>Kategoriyalardan birini tanlang</b>",parse_mode="HTML",reply_markup=hot22)


@dp.callback_query_handler(text="hotklas22")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/qazilhotdog.jpg','rb'),
      caption="<b>Tarkibi:Hot dog noni,qazi,sosiska,pomidor,bodring,ketchup,sous,mayonez\n Narxi:13.000so'm</b>",parse_mode="HTML",reply_markup=hotsonlar22) 



@dp.callback_query_handler(text="hotmini22")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/qazilhotdog.jpg','rb'),
      caption="<b>Tarkibi:Hot dog noni,qazi,sosiska,pomidor,bodring,ketchup,sous,mayonez\n Narxi:11.000so'm</b>",parse_mode="HTML",reply_markup=hotsonlar22) 

@dp.callback_query_handler(text="hotbackson22")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=hot22)



@dp.callback_query_handler(text="hotback22")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=hot1)

@dp.callback_query_handler(text="hotback")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=mahsulot)




@dp.callback_query_handler(text="orqa")
async def Menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish </b>",parse_mode="HTML",reply_markup=mahsulot) 


@dp.callback_query_handler(text="class")
async def don_menyu(call: CallbackQuery):
   await call.message.answer("<b>Nechta katta hot-dog</b>",parse_mode="HTML",reply_markup=sonlar) 


@dp.callback_query_handler(text="kickina")
async def don_menyu(call: CallbackQuery):
   await call.message.answer("<b>Nechta mini hot-dog</b>",parse_mode="HTML",reply_markup=sonlar) 



@dp.callback_query_handler(text="back")
async def hot_menyu(call: CallbackQuery):      
   await call.message.answer("<b>Ortga</b>",parse_mode="HTML",reply_markup=mahsulot)

##################################HOT DOG TUGASHI########################################

##############################SHIRINLIKLAR BOSHLANISHI####################################


@dp.callback_query_handler(text="shirin")
async def Menyu(call: CallbackQuery):
   await call.message.answer("<b>Qanday shirinlik</b>",parse_mode="HTML",reply_markup=shirin1)



@dp.callback_query_handler(text="med")
async def Menyu(call: CallbackQuery):
   await call.message.answer("<b>Kategoriyalardan birini tanlang</b>",parse_mode="HTML",reply_markup=med1)

@dp.callback_query_handler(text="medklas")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/medovik.jpg','rb'),
      caption="<b>Tarkibi:shakar,slivki,krem,mindal,jelatinNechta medovik\nNarxi:12:000so'm</b>",parse_mode="HTML",reply_markup=medsonlar1)



@dp.callback_query_handler(text="medmini")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/medovik.jpg','rb'),
      caption="<b>Tarkibi:shakar,slivki,krem,mindal,jelatinNechta medovik\nNarxi:10:000so'm</b>",parse_mode="HTML",reply_markup=medsonlar1)

@dp.callback_query_handler(text="medbackson11")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=med1)



@dp.callback_query_handler(text="medback1")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=mahsulot)

@dp.callback_query_handler(text="medback")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=shirin1)





@dp.callback_query_handler(text="chizk")
async def Menyu(call: CallbackQuery):
   await call.message.answer("<b>Kategoriyalardan birini tanlang</b>",parse_mode="HTML",reply_markup=chizk1)

@dp.callback_query_handler(text="chizkklas")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/chizkeyk.jpg','rb'),
      caption="<b>Tarkibi:moloko,jleatin,slivki,shakar,medNechta chizkeyk\nNarxi:15.000so'm</b>",parse_mode="HTML",reply_markup=chizksonlar1)



@dp.callback_query_handler(text="chizkmini")
async def gam_menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open('photo/chizkeyk.jpg','rb'),
      caption="<b>Tarkibi:moloko,jleatin,slivki,shakar,medNechta chizkeyk\nNarxi:12.000so'm</b>",parse_mode="HTML",reply_markup=chizksonlar1)

@dp.callback_query_handler(text="chizkbackson11")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=chizk1)



@dp.callback_query_handler(text="chizkback1")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=shirin1)

@dp.callback_query_handler(text="shirinback")
async def Lavash_menyu(call: CallbackQuery):
   await call.message.answer("<b>Menyuga qaytish</b>",parse_mode="HTML",reply_markup=mahsulot)







####################################SHIRINLIKLAR TUGADI####################################

############################ICHIMLIKLAR BOSHLANDI#################################



@dp.callback_query_handler(text="suv")
async def Menyu(call: CallbackQuery):
   await call.message.answer("<b>Qanday ichimliklar</b>",parse_mode="HTML",reply_markup=suv1) 



@dp.callback_query_handler(text="oddiy")
async def Menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open("photo/oddiysuv.jpg","rb"),
      caption="<b>Nechta oddiy suv 0.5L Narxi:3.000so'm</b>",parse_mode="HTML",reply_markup=suvsonlar) 


@dp.callback_query_handler(text="pepsi")
async def Menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open("photo/pepsi.jpg","rb"),
      caption="<b>Nechta pepsi 1L Narxi:7.000so'm</b>",parse_mode="HTML",reply_markup=suvsonlar) 


@dp.callback_query_handler(text="kofe")
async def Menyu(call: CallbackQuery):
   await call.message.answer_photo(
      photo=open("photo/kofe.jpg","rb"),
      caption="<b>Nechta kofe Narxi:10.000so'm</b>",parse_mode="HTML",reply_markup=suvsonlar) 





@dp.callback_query_handler(text="suvback")
async def suv_menyu(call: CallbackQuery):      
   await call.message.answer("<b>Ortga</b>",parse_mode="HTML",reply_markup=suv1)

@dp.callback_query_handler(text="qayt")
async def suv_menyu(call: CallbackQuery):      
   await call.message.answer("<b>Menyu</b>",parse_mode="HTML",reply_markup=mahsulot)





if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
