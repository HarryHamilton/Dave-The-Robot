import discord
from discord import Embed, Member
from discord.ext.commands import Cog, command, check

from bot.settings import CHANNEL_ID, FIELDS


class Greetings(Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = member.guild.get_channel(CHANNEL_ID)

        welcome_embed = Embed(
            title=f"Welcome, {member.display_name}!",
            color=0x00FF00,
            description=f"{member.mention} To get access to the rest of the server, "
            "assign yourself a role based on your field of study.\n"
            "Type one of the following and hit Enter:\n"
            "```!field ComSci\n"
            "!field SecRes\n"
            "!field SofEng\n"
            "!field GamEng```\n"
            "To set your real name for this server, "
            "use the following format:\n"
            "```!name Myname```\n"
            "To display all the available commands, enter `!help`.",
        )
        if channel is not None:
            await channel.send(embed=welcome_embed)


def setup(bot):
    bot.add_cog(Greetings(bot))
