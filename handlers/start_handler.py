from aiogram import F,Router
from aiogram.types import Message,CallbackQuery,ReplyKeyboardRemove
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext


from states import Register
from texts import START_TEXT,REGISTER_SUCCESS_TEXT
from buttons import START_BUTTONS,PHONE_BUTTON,LOCATION_BUTTON,GENDER_BUTTON
from filters import is_valid_fullname,is_valid_phone

start_router=Router()


@start_router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(text=START_TEXT, reply_markup=START_BUTTONS)
    
    
@start_router.message(F.text == "📝 Register")
async def register_handler(message: Message, state: FSMContext):
    text = (
        "🖋 Ro'yxatdan o'tish jarayoniga xush kelibsiz!\n\n"
        "Iltimos, ismingizni kiriting.\n"
        "Masalan: <b>Ali</b> yoki <b>Ali Valiyev</b>"
    )
    await state.set_state(Register.name)
    await message.answer(text,reply_markup=ReplyKeyboardRemove(),parse_mode="HTML" )
    
    
@start_router.message(Register.name)
async def get_name(message: Message, state: FSMContext):
    full_name = message.text.strip()

    if is_valid_fullname(full_name):
        await state.update_data(name=full_name)
        await state.set_state(Register.phone)

        text = (
            "✅ <b>Ismingiz qabul qilindi!</b>\n\n"
            "Endi iltimos, telefon raqamingizni yuboring 📞"
        )
        await message.answer(text,reply_markup=PHONE_BUTTON, parse_mode="HTML")

    else:
        text = (
            "❌ <b>Noto‘g‘ri format!</b>\n\n"
            "Iltimos, ismingizni to‘g‘ri kiriting.\n"
            "Masalan: <b>Ali Valiyev</b>"
        )
        await message.answer(text, parse_mode="HTML")
        

@start_router.message(Register.phone)
async def get_phone(message: Message, state: FSMContext):
    if message.contact:
        phone = message.contact.phone_number
    else:
        phone = message.text.strip()

   
    if not is_valid_phone(phone):
        text = (
            "❌ <b>Telefon raqam noto‘g‘ri formatda!</b>\n\n"
            "Iltimos, to‘g‘ri kiriting:\n"
            "Masalan: <code>+998901234567</code>"
        )
        await message.answer(text,parse_mode="HTML"
        )
        return

    await state.update_data(phone=phone)
    await state.set_state(Register.gender)

    text1 = (
        "📱 <b>Telefon raqam saqlandi!</b>\n\n"
        f"Raqamingiz: <code>{phone}</code>"
    )
    await message.answer(text1,reply_markup=ReplyKeyboardRemove(),parse_mode="HTML")

    text2 = (
        "👫 <b>Iltimos, jinsingizni tanlang:</b>"
    )
    await message.answer(text2,reply_markup=GENDER_BUTTON,parse_mode="HTML")
    
    

    
    





