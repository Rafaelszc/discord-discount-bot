from discord.ext import commands, tasks
from model.database import DataBase
from controler.stores.kabum import Kabum

class SearchItens(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        super().__init__()

    @tasks.loop(hours=5)
    async def search_itens(self):
        await DataBase().remove_value('REQUESTS', None, 'all')
        type_products = await DataBase().get_values('TYPES')

        for request_product in type_products:
            kabum_response = Kabum(f'https://www.kabum.com.br/busca/{request_product[1]}')

            url_list = await kabum_response.get_products_url()

            for url in url_list:
                await DataBase().insert_values((url,), "REQUESTS")

async def setup(bot: commands.Bot):
    cog = SearchItens(bot)

    await cog.search_itens.start()
    await bot.add_cog(cog)