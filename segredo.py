@bot.command(name= "segredo")
async def secret(ctx):
    """Mensagem Direta"""
    await ctx.author.send("Bem-vindo!")
    await ctx.author.send("Obrigado por entrar")
    await ctx.author.send("E se divirta")
