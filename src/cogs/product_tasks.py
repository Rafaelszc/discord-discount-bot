import discord
from discord.ext import commands, tasks
from model.database import DataBase
from controler.stores.kabum import Kabum
from random import randint

class ProductsEmbed(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.channel_id = 0
        self.index = 0

        super().__init__()

    @commands.command()
    async def start_loop(self, ctx: commands.Context, channel_id: int):
        cog = ProductsEmbed(self.bot)
        cog.channel_id = channel_id

        await ctx.send(f"Start on {channel_id}!")
        await cog.send_product.start()

    @tasks.loop(minutes=10)
    async def send_product(self):
        channel = self.bot.get_channel(self.channel_id)
        try:
            url_list = DataBase().get_values('REQUESTS')
            url = url_list[self.index][1]

            product_response = Kabum(url)

            name = product_response.get_name()
            price = product_response.get_price()
            image_url = product_response.get_image_url()
            store_name = product_response.store_name

        except:
            pass
        else:
            product_embed = discord.Embed(
                title=name,
                color=discord.Color.from_str("#4E54ED"),
                url= url
            )

            product_embed.set_image(url=image_url)
            product_embed.add_field(name=':department_store: Store:', value=store_name, inline=True)
            product_embed.add_field(name=':money_with_wings: Price:', value=f"R$: {price}")

            self.index = randint(0, len(url_list))
            DataBase().remove_value('REQUESTS', 'URL', url)

            await channel.send(embed=product_embed)
    
    @commands.command()
    async def add_item(self, ctx: commands.Context,*args):
        product = ' '.join(args)

        DataBase().insert_values((product,), 'TYPES')

        await ctx.reply(f"{product} was added!")

async def setup(bot: commands.Bot):
    await bot.add_cog(ProductsEmbed(bot))