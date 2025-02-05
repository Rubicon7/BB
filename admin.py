import discord
from discord.ext import commands

class AdminCog(commands.Cog):
	'''Majora/Server Owner Only stuff'''

	def __init__(self, bot):
		self.bot = bot

	# Self made check since is_owner() doesnt appear to be working and includes server owner
	# For Myself and the Server Owner
	def is_super(ctx):
		return (ctx.message.author.id == 89033229100683264) or (ctx.message.author == ctx.message.server.owner)

	@commands.command(name="echo", hidden=True)
	@commands.check(is_super)
	async def echo(self, ctx, *, message: str):
		await ctx.send(message)

	@commands.command(name="stop", hidden=True)
	@commands.check(is_super)
	async def stop(self, ctx):
		await ctx.send("Shutting down...")
		exit()

	# Cog Management
	@commands.command(name='load', hidden=True)
	@commands.check(is_super)
	async def extension_load(self, ctx, *, cog: str):
		"""Command which Loads a Module. Remember to use dot path. e.g: cogs.owner"""
		try:
			self.bot.load_extension(cog)
		except Exception as e:
			await ctx.send('**`ERROR: %s`**' % e)
		else:
			await ctx.send('**`SUCCESS`**')

	@commands.command(name='unload', hidden=True)
	@commands.check(is_super)
	async def extension_unload(self, ctx, *, cog: str):
		"""Command which Unloads a Module. Remember to use dot path. e.g: cogs.owner"""
		try:
			self.bot.unload_extension(cog)
		except Exception as e:
			await ctx.send('**`ERROR: %s`**' % e)
		else:
			await ctx.send('**`SUCCESS`**')

	@commands.command(name='reload', hidden=True)
	@commands.check(is_super)
	async def extension_reload(self, ctx, *, cog: str):
		"""Command which Reloads a Module. Remember to use dot path. e.g: cogs.owner"""
		try:
			self.bot.unload_extension(cog)
			self.bot.load_extension(cog)
		except Exception as e:
			await ctx.send('**`ERROR: %s`**' % e)
		else:
			await ctx.send('**`SUCCESS`**')

	#Server Channel Specific
	@commands.command(name='yell', hidden=True)
	@commands.check(is_super)
	async def yell(self, ctx, channel_id, *, message: str):
		channel = self.bot.get_channel(int(channel_id))
		await channel.send(message)

	#User Specific
	@commands.command(name='tell', hidden=True)
	@commands.check(is_super)
	async def tell(self, ctx, user_id, *, message: str):
		user = self.bot.get_user(int(user_id))
		if user.dm_channel == None:
			await user.create_dm()
		await user.dm_channel.send(message)

	@commands.command(aliases=['about'])
	async def credits(self, ctx):
		'''Show credits.'''
		await ctx.send("`Nagato created by TheDerpySage.\nHosted on vinny.thederpysage.com.\nQuestions/Concerns? Contact via Discord.\n@TheDerpySage#2049`")

def setup(bot):
	bot.add_cog(AdminCog(bot))
