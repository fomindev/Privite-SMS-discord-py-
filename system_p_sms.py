    @commands.command()
    async def ls(self, ctx, member:discord.Member=None, *,text):
        await ctx.message.add_reaction('📬') # реакция
        await ctx.send("Личное сообщение отправлено!") # содержание сообщения
        await asyncio.sleep(2) # выдержка
        await ctx.message.delete() # Удаляет сообщение автора
        await member.send(f"{ctx.author} отправил вам сообщение:\n{text}") # Вид сообщения в личных сообщениях

    @ls.error
    async def ls_error(self, ctx, error):
        if isinstance ( error, commands.MissingRequiredArgument): 
            emb = discord.Embed(color = 0x37393d, title = f'**Ошибка!**', timestamp=ctx.message.created_at)
            emb.add_field( name = 'Не хватает аргументов', value = "`.ls` <member> <text>", inline=False)
            emb.set_footer(text=f"<...> - Обязательный аргумент\n[...] - Не обязательный аргумент\n{error.param}")
  
            await ctx.message.delete()
            await ctx.send ( embed = emb)
