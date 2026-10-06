  !do kick username for being annoying
  !do send "hello" to general
  !do rename the server to something cooler
  !do purge 50 messages from spam

── UTILS ────────────────────────────
!clear                 Reset your conversation
!cmds                  This menu
```""")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("unknown command. `!cmds` for the list.")
    else:
        await ctx.send(f"error: {str(error)}")

bot.run(DISCORD_TOKEN)
