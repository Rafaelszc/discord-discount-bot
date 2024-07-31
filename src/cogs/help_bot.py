import discord
from discord.ext import commands

class HelpBot(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        super().__init__()
    
    @commands.command()
    async def help(self, ctx: commands.Context):
        help_embed = discord.Embed(
            title='Help!!',
            description='Commands:',
            url='https://github.com/Rafaelszc',
            color=discord.Color.from_str("#B04EED")
        )

        help_embed.set_image(url='https://raw.githubusercontent.com/Rafaelszc/discord-discount-bot/main/resources/midia/sad_cat.gif')

        help_embed.add_field(name="$start_loop", value="`$start_loop channel_id` channel_id will be the id of the channel on which the product message loop will run", inline=False)
        help_embed.add_field(name="$add_item", value="`$add_item item` this command will add new types of products to be searched for by the bot.", inline=False)

        help_embed.set_footer(text='Contact to Rafaelszc', icon_url='https://avatars.githubusercontent.com/u/158537746?v=4')

        await ctx.reply(embed=help_embed)
        

async def setup(bot: commands.Bot):
    await bot.add_cog(HelpBot(bot))