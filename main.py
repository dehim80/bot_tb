from config import API_KEY, SECRET_KEY, Token
import ccxt
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from pybit.unified_trading import HTTP

bybit = ccxt.bybit({'apiKey': API_KEY,'secret': SECRET_KEY})

bot = Bot(Token)
dp = Dispatcher(bot)

# кнопки
b1 = KeyboardButton('/balance') # кнопка баланс
b2 = KeyboardButton('/cancell_all')
b3 = KeyboardButton('/Buy')
b4 = KeyboardButton('/Sell')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.add(b1).insert(b2).add(b3).insert(b4)# расположение кнопок


@dp.message_handler(commands=['start','help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Bot running', reply_markup=kb_client)


@dp.message_handler(commands=['balance'])
async def balance(message: types.Message):
    balance = bybit.fetch_balance()
    print(balance['info']['result']['list'][0]['coin'])
    equity = (balance['info']['result']['list'][0]['coin'][0]['equity'])
    unrealisedPnl = (balance['info']['result']['list'][0]['coin'][0]['unrealisedPnl'])
    cumRealisedPnl = (balance['info']['result']['list'][0]['coin'][0]['cumRealisedPnl'])
    balance = (balance['info']['result']['list'][0]['coin'][0]['totalWalletBalance'])    
    await message.answer(f'equity={equity}  balance={balance}  unrealisedPnl={unrealisedPnl}  cumRealisedPnl={cumRealisedPnl}')


@dp.message_handler(commands=['cancell_all'])
async def cancel_all_orders(message: types.Message):
    session = HTTP(
        testnet=False, api_key=API_KEY, api_secret=SECRET_KEY, )
    canc = (session.cancel_all_orders(category="linear", symbol='ETHUSDT'))
    await message.answer(canc)


@dp.message_handler(commands=['Buy'])
async def buy_order(message: types.Message):  # Открываем Новый ордер
    qty = 0.01
    side = 'Buy'
    symbol = 'ETHUSDT'
    print('Функция - new_order')
    session = HTTP(testnet=False, api_key=API_KEY, api_secret=SECRET_KEY)
    print(session.place_order(
        category="linear",
        symbol=symbol,  # "XRPUSDT"
        side=side,  # 'Buy' or 'Sell'
        orderType="Market",
        qty=qty))
    await message.answer(f'symbol={symbol} side={side}')


@dp.message_handler(commands=['Sell'])
async def new_order(message: types.Message):  # Открываем Новый ордер
    qty = 0.01
    side='Sell'
    symbol = 'ETHUSDT'
    print('Функция - new_order')
    session = HTTP(testnet=False, api_key=API_KEY, api_secret=SECRET_KEY)
    print(session.place_order(
        category="linear",
        symbol='ETHUSDT',  # "XRPUSDT"
        side=side,  # 'Buy' or 'Sell'
        orderType="Market",
        qty=qty))
    await message.answer(f'symbol={symbol} side={side}')

executor.start_polling(dp,skip_updates=True)
