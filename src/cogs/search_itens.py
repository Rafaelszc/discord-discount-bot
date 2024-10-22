from discord.ext import commands, tasks
from model.database import DataBase
from controler.stores.kabum import Kabum

class SearchItens(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.search_itens.start()
        super().__init__()

    def cog_unload(self):
        self.search_itens.cancel()

    @tasks.loop(hours=5)
    async def search_itens(self):
        DataBase().remove_value('REQUESTS', None, 'all')
        type_products = DataBase().get_values('TYPES')

        for request_product in type_products:
            kabum_response = Kabum(f'https://www.kabum.com.br/busca/{request_product[1]}')

            url_list = kabum_response.get_products_url()

            for url in url_list:
                DataBase().insert_values((url,), "REQUESTS")

async def setup(bot: commands.Bot):
    cog = SearchItens(bot)
    
    await bot.add_cog(cog)