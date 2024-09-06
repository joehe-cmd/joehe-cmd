@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Filtro de palavrões
    if "palavrão" in message.content:
        await message.channel.send(f"Por favor, {message.author} não ofenda os demais usuários")
        await message.delete()

    # XP por mensagem
    user_id = message.author.id
    current_time = time.time()

    if user_id in last_message_time and current_time - last_message_time[user_id] < TIME_WINDOW:
        return

    if len(message.content) >= 5:
        xp_db[user_id] = xp_db.get(user_id, 0) + XP_POR_MENSAGEM
        last_message_time[user_id] = current_time

    await bot.process_commands(message)
