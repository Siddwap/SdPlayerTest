# Coded by Noob, so don't laugh.
# Make pull request if you found something wrong
# (c) Jigar Varma (Jigarvarma2005)
# Kangers copy with credits

import os
import requests
import re, requests
import sys
from urllib.parse import unquote_plus
from flask import Flask, jsonify, request
from flask import render_template
from youtube_dl import YoutubeDL
from base64 import standard_b64encode, standard_b64decode

app = Flask(__name__)

__author__ = "Jigarvarma2005"

ACCOUNT_ID = os.environ.get("ACCOUNT_ID", "6206459123001")
BCOV_POLICY = os.environ.get("BCOV_POLICY", "BCpkADawqM1474MvKwYlMRZNBPoqkJY-UWm7zE1U769d5r5kqTjG0v8L-THXuVZtdIQJpfMPB37L_VJQxTKeNeLO2Eac_yMywEgyV9GjFDQ2LTiT4FEiHhKAUvdbx9ku6fGnQKSMB8J5uIDd")

def str_to_b64(__str: str) -> str:
    str_bytes = __str.encode('ascii')
    bytes_b64 = standard_b64encode(str_bytes)
    b64 = bytes_b64.decode('ascii')
    return b64


def b64_to_str(b64: str) -> str:
    bytes_b64 = b64.encode('ascii')
    bytes_str = standard_b64decode(bytes_b64)
    __str = bytes_str.decode('ascii')
    return __str

@app.route("/")
def homepage():
    return render_template("index1.html")
    
@app.route("/checker")
def checker_page():
    try:
        chk_type = request.args['type']
    except:
        return "<font color=red size=15>Wrong Video Type</font> <br> ask at @JV_Community in Telegram"
    if chk_type.lower() == "mpd":
        return mpd()
    if chk_type.lower() == "m3u8":
        return m3u8()
    if chk_type.lower() == "direct":
        return play()
    if chk_type.lower() == "youtube":
        return youtube()
    if chk_type.lower() == "brightcove":
        return brightcove()
    if chk_type.lower() == "jwplayer":
        return jw_payer()
    if chk_type.lower() == "streamtape":
        return streamtape()
    if chk_type.lower() == "vu":
        return vu()
    if chk_type.lower() == "yd":
        return yd()
    if chk_type.lower() == "gdrive":
        return gdrive()
    return 

@app.route("/yt")
def youtube():
    try:
        video_id = request.args['id']
    except Exception as e:
        edata = "Please parse ?id= when calling the api"
        return edata
    try:
        encypted = request.args['en']
    except Exception as e:
        encypted = 1
    if encypted == "0":
        video_id = video_id
    else:
        try:
            video_id = b64_to_str(video_id)
        except:
            return "<font color=red size=15>Wrong Video ID</font> <br> ask at @JV_Community in Telegram"
    if ("youtube.com" in video_id) and ("/" in video_id) and ("=" in video_id):
        url = video_id
    elif ("youtu.be" in video_id) and ("/" in video_id):
        url = video_id
    else:
        vid = video_id
        url = f"https://youtu.be/{vid}"
    with YoutubeDL() as ydl:
      info_dict = ydl.extract_info(url, download=False)
    video_name = info_dict['title']
    videos = [ {"format": format["height"], "url": format["url"]} for format in info_dict["formats"] if format["format_id"] in ["18", "22"] ]
    # captions = info_dict["aut|safeomatic_captions"]
    captions = []
    video_captions = [ {caption: captions[caption][-1]["url"]} for caption in captions]
    return render_template(
        "yt_template.html",
        video_name=video_name,
        videos=videos,
        video_captions=video_captions)
    
        
@app.route("/jw")
def jw_payer():
    try:
        video_id = request.args['id']
    except Exception as e:
        edata = "Please parse ?id= when calling the api"
        return edata
    try:
        encypted = request.args['en']
    except Exception as e:
        encypted = 1
    if encypted == "0":
        video_id = video_id
    else:
        try:
            video_id = b64_to_str(video_id)
        except:
            return "<font color=red size=15>Wrong Video ID</font> <br> ask at @JV_Community in Telegram"
    jw_url = "https://cdn.jwplayer.com/v2/media"
    video_response = requests.get(f"{jw_url}/{video_id}")
    if video_response.status_code != 200:
        return "<font color=red size=20>Wrong Video ID</font>"
    video = video_response.json()
    video_url = video["playlist"][0]["sources"][0]["file"]
    track_url = video["playlist"][0]["tracks"][0]["file"]
    return render_template(
        "m3u8.html",
        video_url=video_url,
        track_url=track_url,
    )

@app.route("/stream")
def streamtape():
    try:
        video_id = request.args['id']
    except Exception as e:
        edata = "Please parse ?id= when calling the api"
        return edata
    try:
        encypted = request.args['en']
    except Exception as e:
        encypted = 1
    if encypted == "0":
        video_id = video_id
    else:
        try:
            video_id = b64_to_str(video_id)
        except:
            return "<font color=red size=15>Wrong Video ID</font> <br>"
    r = requests.get(video_id)
    rstr = str(r.content)
    rstr = rstr[rstr.find("\\'ideoolink\\'"):rstr.find("\\'robotlink\\'")] 
    rstr = rstr[rstr.find('"')+ 1:]
    link = rstr[:rstr.find('"')]
    link = "https:/"+link+rstr[rstr.find("xcdb")+4:rstr.find(".substring")-3]
    video_url = link
    video_name = "SdPyayer"
    track_url = video_url
    return render_template(
        "temp_ads.html",
        type="jw",
        video_name=video_name,
        video_url=video_url,
        track_url=track_url,
    )

@app.route("/vu")
def vu():
    try:
        video_id = request.args['id']
    except Exception as e:
        edata = "Please parse ?id= when calling the api"
        return edata
    try:
        encypted = request.args['en']
    except Exception as e:
        encypted = 1
    if encypted == "0":
        video_id = video_id
    else:
        try:
            video_id = b64_to_str(video_id)
        except:
            return "<font color=red size=15>Wrong Video ID</font> <br>"
    s = requests.Session()
    data = s.get(video_id)
    data = data.text
    vidlinks = re.findall("sources(.*?).m3u8" , data)
    vidlinks = vidlinks[0] + ".m3u8"
    vidlinks = re.sub(r'.', '', vidlinks, count = 9)
    video_url = vidlinks
    video_name = "SdPyayer"
    track_url = video_url
    return render_template(
        "m3u8.html",
        video_name=video_name,
        video_url=video_url,
        track_url=track_url,
    )


@app.route("/yd")
def yd():
    try:
        video_id = request.args['id']
    except Exception as e:
        edata = "Please parse ?id= when calling the api"
        return edata
    try:
        encypted = request.args['en']
    except Exception as e:
        encypted = 1
    if encypted == "0":
        video_id = video_id
    else:
        try:
            video_id = b64_to_str(video_id)
        except:
            return "<font color=red size=15>Wrong Video ID</font> <br>"
    s = requests.Session()
    data = s.get(video_id)
    data = data.text
    vidlinks = re.findall("src(.*?).mp4" , data)
    vidlinks = vidlinks[0] + ".mp4"
    vidlinks = re.sub(r'.', '', vidlinks, count = 2)
    video_url = vidlinks
    video_name = "SdPyayer"
    track_url = video_url
    return render_template(
        "temp.html",
        video_name=video_name,
        video_url=video_url,
        track_url=track_url,
    )


@app.route("/gdrive")
def gdrive():
    try:
        video_id = request.args['id']
    except Exception as e:
        edata = "Please parse ?id= when calling the api"
        return edata
    try:
        encypted = request.args['en']
    except Exception as e:
        encypted = 1
    if encypted == "0":
        video_id = video_id
    else:
        try:
            video_id = b64_to_str(video_id)
        except:
            return "<font color=red size=15>Wrong Video ID</font> <br>"
    url = video_id
    url = re.sub(r'.', '', url, count = 32)
    size = len(url)
    driveid = url[:size - 18]
    apikey = "AIzaSyD739-eb6NzS_KbVJq1K8ZAxnrMfkIqPyw"
    video_url = "https://www.googleapis.com/drive/v3/files/" + driveid + "?alt=media&key=" + apikey
    video_name = "SdPyayer"
    track_url = video_url
    return render_template(
        "temp_ads.html",
        type="jw",
        video_name=video_name,
        video_url=video_url,
        track_url=track_url,
    )


@app.route("/play")
def play():
    try:
        video_id = request.args['id']
    except Exception as e:
        edata = "Please parse ?id= when calling the api"
        return edata
    try:
        encypted = request.args['en']
    except Exception as e:
        encypted = 1
    if encypted == "0":
        video_id = video_id
    else:
        try:
            video_id = b64_to_str(video_id)
        except:
            return "<font color=red size=15>Wrong Video ID</font> <br> ask at @JV_Community in Telegram"
    video_url = video_id
    track_url = video_id
    video_name = video_id.split("/")[-1]
    return render_template(
        "temp.html",
        type="jw",
        video_name=unquote_plus(video_name),
        video_url=video_url,
        track_url=track_url,
    )

@app.route("/m3u8")
def m3u8():
    try:
        video_url = request.args['id']
    except Exception as e:
        edata = "Please parse ?id= when calling the api"
        return edata
    try:
        encypted = request.args['en']
    except Exception as e:
        encypted = 1
    if encypted == "0":
        video_url = video_url
    else:
        try:
            video_url = b64_to_str(video_url)
        except:
            return "<font color=red size=15>Wrong Video ID</font> <br> ask at @JV_Community in Telegram"
    return render_template(
        "m3u8.html",
        video_url=video_url,
        track_url=video_url
    )

def cw():
    try:
        video_url = request.args['id']
    except Exception as e:
        edata = "Please parse ?id= when calling the api"
        return edata
    try:
        encypted = request.args['en']
    except Exception as e:
        encypted = 1
    if encypted == "0":
        video_url = video_url
    else:
        try:
            video_url = b64_to_str(video_url)
        except:
            return "<font color=red size=15>Wrong Video ID</font> <br> ask at @JV_Community in Telegram"
    return render_template(
        "m3u8.html",
        video_url= (
    f"https://edge.api.brightcove.com/playback/v1/accounts/6206459123001/videos/{video_id}/master.m3u8?bcov_auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3NDQxMzExMjMsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiU2l0c1pFNXFZamhuY1ZKaGNsRklNRmREWlhOUlVUMDkiLCJmaXJzdF9uYW1lIjoiYWtKdU5IZ3pRelpOVml0V04ySnRRVVo0ZG1KVmR6MDkiLCJlbWFpbCI6IlZFRTFlR0pEVGk5UlVqQmtjMEZzYkdOU2IzaEZPSFJPWlRKNk5YSlFWazlHYjNKUk9HTXpPSGxpTUQwPSIsInBob25lIjoiVERGbFIwODNWbU4yV1RoalNtZFlaVWRQTTBWNFVUMDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJRak15WVRsYVdEQlphWEpWYnpoM09GTnpja2xuWnowOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoiUGllKEFuZHJvaWQgOS4wKSIsImRldmljZV9tb2RlbCI6Ik9uZVBsdXMgUEhCMTEwIiwicmVtb3RlX2FkZHIiOiIzNC4yMzEuMTIyLjE1NSJ9fQ.UdZIYfVf7UpyU4zSzGSsjnGPu8PsSSBDMPHeOTmoYdTrsNTTW2anisT5f1nVHxfbhBKEZCuoQ9lf9IZ0CAX3Bry1AHmoLNZN3B1mhgoVIUdkufcD1UNPMd-JLYFHiWpo2gThLUHGyir_1p_IqhWXZca797uXHw5VVjvDThR924cXUMZApR5p2sT3onG_P3hBYjhppouS27E18VSyEJgXg0MZXPmROVhC76rBfjMFdQ0TldT9UBLj9ID7eboowZ7_eJPHsSZw0qzG_E5Q6lGsJX5RZkcePB5Fc52WsC9gZjbgDhS9VMUV1bwizxnDgaNwdmQSPpVtbBbh_9tnCy5FtQ"
    ),
        track_url=(
    f"https://edge.api.brightcove.com/playback/v1/accounts/6206459123001/videos/{video_id}/master.m3u8?bcov_auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3NDQxMzExMjMsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiU2l0c1pFNXFZamhuY1ZKaGNsRklNRmREWlhOUlVUMDkiLCJmaXJzdF9uYW1lIjoiYWtKdU5IZ3pRelpOVml0V04ySnRRVVo0ZG1KVmR6MDkiLCJlbWFpbCI6IlZFRTFlR0pEVGk5UlVqQmtjMEZzYkdOU2IzaEZPSFJPWlRKNk5YSlFWazlHYjNKUk9HTXpPSGxpTUQwPSIsInBob25lIjoiVERGbFIwODNWbU4yV1RoalNtZFlaVWRQTTBWNFVUMDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJRak15WVRsYVdEQlphWEpWYnpoM09GTnpja2xuWnowOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoiUGllKEFuZHJvaWQgOS4wKSIsImRldmljZV9tb2RlbCI6Ik9uZVBsdXMgUEhCMTEwIiwicmVtb3RlX2FkZHIiOiIzNC4yMzEuMTIyLjE1NSJ9fQ.UdZIYfVf7UpyU4zSzGSsjnGPu8PsSSBDMPHeOTmoYdTrsNTTW2anisT5f1nVHxfbhBKEZCuoQ9lf9IZ0CAX3Bry1AHmoLNZN3B1mhgoVIUdkufcD1UNPMd-JLYFHiWpo2gThLUHGyir_1p_IqhWXZca797uXHw5VVjvDThR924cXUMZApR5p2sT3onG_P3hBYjhppouS27E18VSyEJgXg0MZXPmROVhC76rBfjMFdQ0TldT9UBLj9ID7eboowZ7_eJPHsSZw0qzG_E5Q6lGsJX5RZkcePB5Fc52WsC9gZjbgDhS9VMUV1bwizxnDgaNwdmQSPpVtbBbh_9tnCy5FtQ"
    )
    )

@app.route("/mpd")
def mpd():
    try:
        video_url = request.args['id']
    except Exception as e:
        edata = "Please parse ?id= when calling the api"
        return edata
    try:
        encypted = request.args['en']
    except Exception as e:
        encypted = 1
    if encypted == "0":
        video_url = video_url
    else:
        try:
            video_url = b64_to_str(video_url)
        except:
            return "<font color=red size=15>Wrong Video ID</font> <br> ask at @JV_Community in Telegram"
    return render_template(
        "mpd.html",
        video_url=video_url,
        track_url=video_url
    )

@app.route("/decode")
def decoder_():
    try:
        video_url = request.args['id']
    except Exception as e:
        edata = "Please parse ?id= when calling the api"
        return edata
    try:
        video_url = b64_to_str(video_url)
    except:
        return "<font color=red size=15>Wrong Video ID</font> <br> ask at @JV_Community in Telegram"
    return {"decoded": video_url}

@app.route("/encode")
def encoder_():
    try:
        video_url = request.args['id']
    except Exception as e:
        edata = "Please parse ?id= when calling the api"
        return edata
    video_url = str_to_b64(video_url)
    return {"encoded": video_url}

@app.route("/brightcove")
def brightcove():
    try:
        video_url = request.args['id']
    except Exception as e:
        edata = "Please parse ?id= when calling the api"
        return edata
    try:
        encypted = request.args['en']
    except Exception as e:
        encypted = 1
    if encypted == "0":
        video_url = video_url
    else:
        try:
            video_url = b64_to_str(video_url)
        except:
            return "<font color=red size=15>Wrong Video ID</font> <br> ask at @JV_Community in Telegram"
    bc_url = f"https://edge.api.brightcove.com/playback/v1/accounts/{ACCOUNT_ID}/videos"
    bc_hdr = {"BCOV-POLICY": BCOV_POLICY}
    video_response = requests.get(f"{bc_url}/{video_url}", headers=bc_hdr)
    if video_response.status_code != 200:
        return "<font color=red size=20>Wrong Video ID</font>"
    video = video_response.json()
    video_name = video["name"]
    video_source = video["sources"][3]
    video_url = video_source["src"]
    widevine_url = ""
    microsoft_url = ""
    if "key_systems" in video_source:
        widevine_url = video_source["key_systems"]["com.widevine.alpha"]["license_url"]
        microsoft_url = video_source["key_systems"]["com.microsoft.playready"][
            "license_url"
        ]
    track_url = video["text_tracks"][1]["src"]
    if ".mpd" in video_url and ".m3u8" not in video_url:
        templ = "mpd.html"
    elif ".m3u8" in video_url and ".mpd" not in video_url:
        templ = "m3u8.html"
    else:
        templ = "mpd.html"
    return render_template(
        templ,
        video_url=video_url,
        track_url=track_url,
        widevine_url=widevine_url,
        microsoft_url=microsoft_url
    )
@app.route("/dp")
def dp():
    video_id = request.args['id']
    video_url = video_id
    track_url = video_id
    video_name = video_id.split("/")[-1]
    return render_template(
        "temp.html",
        type="jw",
        video_name=unquote_plus(video_name),
        video_url=video_url,
        track_url=track_url,
    )
    
    


if __name__ == "__main__":
    app.run(debug=True)

