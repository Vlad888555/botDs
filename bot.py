import discord
from discord.ext import commands
from discord import utils
from bs4 import BeautifulSoup
import requests
import test


Token = 'ODQ2MjM5MjUzNjgzMjQxMDAw.G8Rjjz.vabIAjhjePi6YDAFW4Ln1I8UbG6n_djPjuzENU'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_raw_reaction_add(self, payload):
        if payload.message_id == test.POST_ID:
            channel = self.get_channel(payload.channel_id)  # получаем объект канала
            message = await channel.fetch_message(payload.message_id)  # получаем объект сообщения
            member = utils.get(message.guild.members,
                               id=payload.user_id)  # получаем объект пользователя который поставил реакцию

            try:
                emoji = str(payload.emoji)  # эмоджик который выбрал юзер
                role = utils.get(message.guild.roles, id=test.ROLES[emoji])  # объект выбранной роли (если есть)

                if (len([i for i in member.roles if i.id not in test.EXCROLES]) <= test.MAX_ROLES_PER_USER):
                    await member.add_roles(role)
                    print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
                else:
                    await message.remove_reaction(payload.emoji, member)
                    print('[ERROR] Too many roles for user {0.display_name}'.format(member))

            except KeyError as e:
                print('[ERROR] KeyError, no role found for ' + emoji)
            except Exception as e:
                print(repr(e))

    async def on_raw_reaction_remove(self, payload):
        channel = self.get_channel(payload.channel_id)  # получаем объект канала
        message = await channel.fetch_message(payload.message_id)  # получаем объект сообщения
        member = utils.get(message.guild.members,
                           id=payload.user_id)  # получаем объект пользователя который поставил реакцию

        try:
            emoji = str(payload.emoji)  # эмоджик который выбрал юзер
            role = utils.get(message.guild.roles, id=test.ROLES[emoji])  # объект выбранной роли (если есть)

            await member.remove_roles(role)
            print('[SUCCESS] Role {1.name} has been remove for user {0.display_name}'.format(member, role))

        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)
        except Exception as e:
            print(repr(e))


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command(name="help_command")
async def hello_command(ctx):
    help_message = ("Запросить ссылку на аккаунт: $p ник регион Примечание если в ники есть пробелы замените на нижние подчеркивание")
    await ctx.send(help_message)


@bot.command(name='p')
async def dynamic_command(ctx, summoner, pegion):
    summoner1 = summoner.strip().lower()
    pegion1 = pegion.strip().lower()
    url = f"https://www.leagueofgraphs.com/ru/summoner/{pegion1}/{summoner1}".replace("_", "+")
    req = requests.get(url, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")

    Noyp = soup.find(class_="solo-text")
    if Noyp:
        await ctx.send("Не найден")
        await ctx.send(url)
    else:
        # уровень
        bannerSubtitle = soup.find(class_="bannerSubtitle")
        level = bannerSubtitle.text.strip() if bannerSubtitle else "Уровень не найден"

        # ранг
        leagueTier = soup.find(class_="leagueTier")
        rank = f"Ранг: {leagueTier.text.strip()}" if leagueTier else "Без ранга"

        # приметы
        tagTitile_list = []
        tagTitle_rank = soup.find_all(class_="tag requireTooltip brown")
        tagTitile_list.extend(item.text.strip() for item in tagTitle_rank)

        tagTitile_green = soup.find_all(class_="tag requireTooltip green withLink")
        tagTitile_list.extend(item.text.strip() for item in tagTitile_green)

        tagTitile_yellow = soup.find_all(class_="tag requireTooltip yellow withLink")
        tagTitile_list.extend(item.text.strip() for item in tagTitile_yellow)

        tagTitile_red = soup.find_all(class_="tag requireTooltip red withLink")
        tagTitile_list.extend(item.text.strip() for item in tagTitile_red)

        tags = ', '.join(tagTitile_list)

        # Всего игр и винрейт
        pie_chart_small = soup.find(id="graphDD2")
        total_games = f"Всего Сыграно: {pie_chart_small.text.strip()} за этот сплит" if pie_chart_small else "Нет данных"
        pie_chart_small1 = soup.find(id="graphDD3")
        win_rate = f"Винрейт {pie_chart_small1.text.strip()} за все игры в этом сплите" if pie_chart_small1 else "Нет данных"

        # Игры в одиночной
        pie_chart_small2 = soup.find(id="graphDD4")
        ranked_games = f"Сыграно {pie_chart_small2.text.strip()} в ранговой" if pie_chart_small2 else "Нет данных"
        pie_chart_small3 = soup.find(id="graphDD5")
        ranked_win_rate = f"Винрайт {pie_chart_small3.text.strip()} в ранговой" if pie_chart_small3 else "Нет данных"

        message = f"{url}\n{level}\n{rank}\nТеги: {tags}\n{total_games}\n{win_rate}\n{ranked_games}\n{ranked_win_rate}"
        await ctx.send(message)


bot.run(test.Token)
