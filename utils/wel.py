import os
import io
import discord
from html2image import Html2Image
from PIL import Image

html_str = """

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap" rel="stylesheet" />
</head>
<style>
    body {{ 
        padding: 0;
        margin: 0;
        font-family: 'Poppins', sans-serif;
        width: 1920px;
        height: 1080px;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #313338;
    }}

    #welcomeCard {{
        width: 1800px;
        height: 900px;
        background: linear-gradient(135deg, #23a6d5 0%, #23d5ab 100%);
        position: relative;
        overflow: hidden;
        border-radius: 40px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    }}

    #image {{
        display: flex;
        justify-content: center;
        align-items: flex-start;
        width: 100%;
        height: 100%;
        position: relative;
        padding-top: 100px;
    }}

    #avatar {{
        width: 300px;
        height: 300px;
        border-radius: 50%;
        border: 12px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 16px 50px rgba(0, 0, 0, 0.3);
        position: relative;
    }}

    #memname {{
        font-size: 72px;
        font-weight: 800;
        position: absolute;
        width: 100%;
        text-align: center;
        top: 480px;
        color: white;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);
    }}

    #bottom-text {{
        font-size: 48px;
        font-weight: 600;
        position: absolute;
        width: 100%;
        text-align: center;
        top: 600px;
        color: rgba(255, 255, 255, 0.9);
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);
        padding: 0 40px;
        box-sizing: border-box;
    }}

    .overlay {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle at center, transparent 30%, rgba(0, 0, 0, 0.2));
        pointer-events: none;
    }}

    .decorative-circles {{
        position: absolute;
        width: 100%;
        height: 100%;
        pointer-events: none;
    }}

    .circle{{
        position: absolute;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 50%;
    }}

    .circle-1 {{
        width: 200px;
        height: 200px;
        left: 10%;
        top: 20%;
    }}

    .circle-2 {{
        width: 300px;
        height: 300px;
        right: 15%;
        bottom: 25%;
    }}

    .circle-3 {{
        width: 160px;
        height: 160px;
        right: 25%;
        top: 15%;
    }}
</style>

<body>
    <div id="welcomeCard">
        <div class="decorative-circles">
            <div class="circle circle-1"></div>
            <div class="circle circle-2"></div>
            <div class="circle circle-3"></div>
        </div>
        <div class="overlay"></div>
        <div id="image">
            <img src="{avatar_url}" alt="" id="avatar" />
        </div>
        <div id="memname">{user}</div>
        <div id="bottom-text">Welcome to {guild_name}!</div>
    </div>
</body>

</html>

"""


async def get_welcome_card(member: discord.Member):
    guild_name = member.guild.name
    member_name = str(member)
    avatar_url = str(member.display_avatar.url)

    html = html_str.format(
        guild_name=guild_name, user=member_name, avatar_url=avatar_url
    )
    filename = "wel_{}_{}.png".format(member.guild.id, member.id)

    h2i = Html2Image()
    h2i.screenshot(html_str=html, save_as=filename, size=(1920, 1080))

    pil_image = Image.open(filename)
    img_io = io.BytesIO()
    pil_image.save(img_io, "PNG")
    img_io.seek(0)
    pil_image.close()
    os.remove(filename)

    return img_io
