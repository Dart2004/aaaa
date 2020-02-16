import discord
client=discord.Client()

questions=[]
answers=[]
d=0
@client.event
async def on_message(msg):
  global d, questions, answers
  if msg.author==client.user:
    return
  msg.content=msg.content.lower()
  if ">"+msg.content.replace(">","")==msg.content:
    possitive=[]
    for l in range(0,len(questions)):
      possitive.append(0)
    for l in range(0,len(questions)-1):
      msg2=msg.content
      for l2 in msg2:
        if l2 in questions[l]:
          msg2=msg2.replace(l2,"")
          possitive[l]+=1
    g=0
    p=0
    for l in possitive:
      if possitive[l]>g:
        g=possitive[l]
        p=l
    await msg.channel.send(answers[p])
  else:
    if (d==0):
      questions.append(msg.content+" ")
      d=1
    else:
      answers.append(msg.content+" ")
      questions.append(msg.content+" ")
  print(msg)
client.run("NjU5NzYyMTc4OTM2Nzk5MjU4.XklvdQ.fV--GoZSebr55BOAL4B3W9HXez0")
