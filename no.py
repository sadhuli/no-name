import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True  # 啟用訊息相關的 intents

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_message(message):
    if message.author == bot.user or message.guild:  # 排除機器人自身的訊息和伺服器內的訊息
        return

    # 檢查是否包含違禁詞
    forbidden_words = ['@管理', '@here', '@everyone']  # 請替換成實際的違禁詞列表
    contains_forbidden_word = any(word in message.content for word in forbidden_words)

    if contains_forbidden_word:
        # 隱藏資訊，僅顯示訊息內容
        clean_message = f'**私訊收到來自 {message.author} 的訊息：**\n{message.content}'

        # 取得要轉發的文字頻道
        text_channel_id = 1198061788693012520  # 請替換成實際的文字頻道 ID
        text_channel = bot.get_channel(text_channel_id)

        if text_channel:
            # 將訊息轉發到文字頻道
            await text_channel.send(clean_message)
            await message.author.send('已將您的訊息轉發到文字頻道。')
        else:
            print('找不到指定的文字頻道。')
            await message.author.send('無法完成操作，請聯繫伺服器管理員。')

    await bot.process_commands(message)

bot.run('MTE5NzkwMTg2Nzg3NTg0NDE0Nw.GcnrsU.D9zVBvjXewSb_DAhJWY5PJWtmOhFyD5Hw9pjjI')  # 請替換成您的機器人 token
