import os
from sys import exit as exx
HOME = os.path.expanduser("~")
CWD = os.getcwd()

# All found ngrok authtoken from github
tokens = {
    "lostcatbox": "1X7aYWPuFKYzvewLbnNoMo71kZi_2uzbB966Q4TU5cpgNPKhy",
    "zero-structure": "1UqHsShi6o3ketf426P5UtVdTfs_5XFD6sFRMkryka8fAbLd3",
    "ekkleesia": "7LE18LK8zeaDYeybp5fKP_6GNG1oHEfhTnQE7s9qpw",
    "SEARteam1928": "1Qe1IeySOQWSTnpQ3eFfr8j7Oi5_2zhanqnpZwHBhsfANd6yf",
    "angenalZZZ": "7pWLVhS1gxiMAQdaFeYJy_31krnw9drNLLJftaNSFnm",
    "lukikrk": "1XJNNnG8kZsPjjFmLsYNWCC0gIo_7VpBhwTcvhiuK4o2G2jbt",
    "bhavya7777": "1XzP70k7YVrg7MMaHQWPks0Q8Za_7y6b1mTDJDmJWcuqt5qTp",
    "hector605": "1Y14GB7E4acXxWYnVTiBejgnLuV_853z7mAgaTJxE9KY3HnCW",
    "fouille": "1XkoKNLcyiPECcQfGUjrTVzN64P_7tv2YgC4DSnazyVtpCpHm",
    "rikitz": "1Xc7z0uHxDoI9Ah06EQKgH61zoP_6WTPXDGvjFmcp2o7gNmqa",
    "VictorM369": "3c4WZaxPbjeRwRibY5opU_2N4TTRKaDubtEWMeKkFXn",
    "YHF7": "3fW4eXHdUN3ziCBXcahZ_3tnDdaTyLw8tKzJtKZkLp",
    "cyberkallan": "3CqeFZQht43cG5Z2YKfyv_6aKTrgrbo1HtyRi78hRKK",
    "Toxic-Omega": "1RCQwctVjSz8AIzHO6S55jm8XB8_5N6PqyZVnoN7mUVqF1yvT",
    "DevLuDaley": "1XTxsRKP8XyxvaJigX9XFXU2FvK_4dqzLxNRJHBz8A3aoPC85",
    "randyramig": "3Y8YSw6bvC9CsbYeRczmt_8akMuLYA3bAUshP1NCMnW",
    "sz-xcf": "1XSYq8gmxzNgMlYQzERmC50uBot_6qURZnj43KsYF2GWaUamm",
    "api1": "6qGnEsrCL4GqZ7hMfqpyz_7ejAThUCjVnU9gD5pbP5u",
    "api2": "1Q4i7F6isO7zZRrrjBKZzZhwsMu_74yJqoEs1HrJh1zYyxNo1",
    "api3": "1SCsbuawjv9d79jlhlfNljaFTaB_5heVkcR6C7Sk8UBaQ1U1C",
    "api5": "1Q45NXgsx6oyusN3GiNAYvkNJPS_AveYUDBcPHsvRvf21WZv",
    "api6": "1Q6smHt4Bzz9VEXTwj3a7p5Gdx2_5mp6ivT6N6nB3YmRHUEM3",
    "api7": "7VJwGkCTTUubiGhgz6Gv6_5fMLganRSKj9ntdefnF5o",
    "api9": "5S28rBKgc22ZW7evyedNT_YvEm15RZSHdXgS4QwYbk",
    "api12": "3VnrrXDQVHoNp9HvHFhqX_3X4JExwm6L9n6w4ppL1qy",
    "api13": "1ShshNwfhQcyOqlMjnBDVE5X5jC_3WAmzomMHAgkunka4dSck",
    "api14": "772yFAui6ynH9AYx29HHS_5Xcr88pHtPTQLwewv7Ctk",
    "api16": "5HmAWwzDdkYp8CdzDQMDS_4BGwsK7AdMssLnSttZEeh",
    "api17": "1T750atJi3xccndeUqJ4ewiS62o_2s6f8GUccL1qDUXTGSftN",
    "api18": "1QUysRUo97w5mdB6sCZvTTMM0aK_3unoMs6nYd7grgCkuhbj3",
    "api19": "3CqeFZQht43cG5Z2YKfyv_6aKTrgrbo1HtyRi78hRKK",
    "api20": "5eMywZLisJNdybqpFLVgs_4XQDeF3YCMHu1Ybf7mVE6",
    "api21": "4Cg1cEwCT7Ek89zT4VcdB_4GPAjMFgu6nhwY7SxQm94",
    "api22": "1SGs4s9NrhxP9FRURszjL1nITSv_otcpfpb6aMVEL13u3dv1",
    "api23": "1StL3sIccfR624Uc3BGV36XA0qG_6cAMMYFdKtPjtWax3AHSK",
    "api24": "1SuK2ukM9Z4NohoJbU9224uMzXr_6h1ABdCrJU2EviZv4RN4r",
    "api26": "7ecmt2Kux5uYsTUHrrqGU_3W9CJnaSeSyxiwkjxNhHc",
    "api27": "3CqeFZQht43cG5Z2YKfyv_6aKTrgrbo1HtyRi78hRKK",
    "api28": "2DXURjrUhAZZNMhqN5m1F_6HHzejcfRecP8upwJnNBd"
}


class ngrok:

  def __init__(self, TOKEN=None, USE_FREE_TOKEN=True,
               service=[['Service1', 80, 'tcp'], ['Service2', 8080, 'tcp']],
               region='us',
               dBug=[f"{HOME}/.ngrok2/ngrok.yml", 4040]):
    self.region = region
    self.configPath, self.dport = dBug
    self.TOKEN = TOKEN
    self.USE_FREE_TOKEN = USE_FREE_TOKEN
    self.service = service
    if USE_FREE_TOKEN:
      self.sdict = {}
      for i, sn in enumerate(service):
        tempcP = f'{HOME}/.ngrok2/'+sn[0]+'.yml'
        # Port, Protocol, config path
        self.sdict[sn[0]] = [self.dport+i, sn[2], tempcP]

  def nameport(self, TOKEN, AUTO):
    if AUTO:
        try:
            return tokens.popitem()[1]
        except KeyError:
            return "Invalid Token"
    elif not TOKEN:
        if not 'your' in tokens.keys():
            from IPython import get_ipython
            from IPython.display import clear_output
            ipython = get_ipython()

            print(r"Copy authtoken from https://dashboard.ngrok.com/auth")
            __temp = ipython.magic('%sx read -p "Token :"')
            tokens['your'] = __temp[0].split(':')[1]
            USR_Api = "your"
            clear_output()
        else:
            USR_Api = "your"
    else:
        USR_Api = "mind"
        tokens["mind"] = TOKEN
    return tokens[USR_Api]


  def ngrok_config(self, token, Gport, configPath, region, service):
    import os
    data = """
    region: {}
    update: false
    update_channel: stable
    web_addr: localhost:{}
    tunnels:\n""".format(region, Gport)
    if not self.USE_FREE_TOKEN:
      auth ="""
    authtoken: {}""".format(token)
      data = auth+data
    tunnels = ""
    for S in service:
        Sn, Sp, SpC = S
        tunnels += """      {}:
        addr: {}
        proto: {}
        inspect: false\n""".format(Sn, Sp, SpC)
    data = data + tunnels
    os.makedirs(f'{HOME}/.ngrok2/', exist_ok=True)
    with open(configPath, "w+") as configFile:
        configFile.write(data)
    return True


  def startWebUi(self, token, dport, nServer, region, btc, configPath,
               displayB, service, v):
    import os, time, urllib
    from IPython.display import clear_output
    from json import loads

    if token == "Invalid Token":
        print(tokens)
        os.exit()

    installNgrok()
    if v:
      clear_output()
      loadingAn(name="lds")
      textAn("Starting ngrok...", ty='twg')
    if self.USE_FREE_TOKEN:
      for sn in service:
        self.ngrok_config(
          token,
          self.sdict[nServer][0],
          self.sdict[nServer][2],
          region,
          service)
        if sn[0] == nServer:
          runSh(f"ngrok {sn[2]} -config={self.sdict[nServer][2]} {sn[1]} &", shell=True)
    else:
      self.ngrok_config(token, dport, configPath, region, service)
      runSh(f"ngrok start --config {configPath} --all &", shell=True)
    time.sleep(3)
    try:
        if self.USE_FREE_TOKEN:
          dport = self.sdict[nServer][0]
          nServer = 'command_line'
          host = urllib.request.urlopen(f"http://localhost:{dport}/api/tunnels")
        else:
          host = urllib.request.urlopen(f"http://localhost:{dport}/api/tunnels")
        host = loads(host.read())['tunnels']
        for h in host:
          if h['name'] == nServer:
            host = h['public_url'][8:]
            break
    except urllib.error.URLError:
        if v:
          clear_output()
          loadingAn(name="lds")
          textAn("ngrok Token is in used!. Trying another token...", ty='twg')
        time.sleep(2)
        return True

    data = {"url": f"https://{host}"}
    if displayB:
      displayUrl(data, btc)
    return data


  def start(self, nServer, btc='b', displayB=True, v=True):
    import urllib
    from IPython.display import clear_output
    from json import loads

    try:
      nServerbk = nServer
      if self.USE_FREE_TOKEN:
          dport = self.sdict[nServer][0]
          nServer = 'command_line'
      else:
        dport = self.dport
      host = urllib.request.urlopen(f"https://localhost:{dport}/api/tunnels")
      host = loads(host.read())['tunnels']
      for h in host:
        if h['name'] == nServer:
          host = h['public_url'][8:]
          data = {"url": f"https://{host}"}
          if displayB:
            displayUrl(data, btc)
          return data

      raise Exception('Not found tunnels')
    except urllib.error.URLError:
      for run in range(10):
        if v:
          clear_output()
          loadingAn(name='lds')
        dati = self.startWebUi(
            self.nameport(self.TOKEN, self.USE_FREE_TOKEN),
            self.dport,
            nServerbk,
            self.region,
            btc,
            self.configPath,
            displayB,
            self.service,
            v
            )
        if dati == True:
            continue
        return dati

def checkAvailable(path_="", userPath=False):
    from os import path as _p

    if path_ == "":
        return False
    else:
        return (
            _p.exists(path_)
            if not userPath
            else _p.exists(f"/usr/local/sessionSettings/{path_}")
        )

def accessSettingFile(file="", setting={}):
    from json import load, dump

    if not isinstance(setting, dict):
        print("Only accept Dictionary object.")
        exx()
    fullPath = f"/usr/local/sessionSettings/{file}"
    try:
        if not len(setting):
            if not checkAvailable(fullPath):
                print(f"File unavailable: {fullPath}.")
                exx()
            with open(fullPath) as jsonObj:
                return load(jsonObj)
        else:
            with open(fullPath, "w+") as outfile:
                dump(setting, outfile)
    except:
        print(f"Error accessing the file: {fullPath}.")


def displayUrl(data, btc='b', EcUrl=None, ExUrl=None):
    from IPython.display import HTML, clear_output


    showTxT = f'{data["url"]}'
    if EcUrl:
      showUrL = data["url"]+EcUrl
    elif ExUrl:
      showUrL = ExUrl
    else:
      showUrL = data["url"]

    return display(HTML('''<center><a href="'''+showUrL+'''" target="_blank"/></center>'''))


def findProcess(process, command="", isPid=False):
    from psutil import pids, Process

    if isinstance(process, int):
        if process in pids():
            return True
    else:
        for pid in pids():
            try:
                p = Process(pid)
                if process in p.name():
                    for arg in p.cmdline():
                        if command in str(arg):
                            return True if not isPid else str(pid)
                        else:
                            pass
                else:
                    pass
            except:
                continue

def installNgrok():
    if checkAvailable("/usr/local/bin/ngrok"):
        return
    else:
        import os
        from zipfile import ZipFile
        from urllib.request import urlretrieve

        ngURL = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip"
        urlretrieve(ngURL, 'ngrok-amd64.zip')
        with ZipFile('ngrok-amd64.zip', 'r') as zip_ref:
            zip_ref.extractall('/usr/local/bin/')
        os.chmod('/usr/local/bin/ngrok', 0o755)
        os.unlink('ngrok-amd64.zip')

def installAutoSSH():
    if checkAvailable("/usr/bin/autossh"):
        return
    else:
        runSh("apt-get install autossh -qq -y")



def runSh(args, *, output=False, shell=False, cd=None):
    import subprocess, shlex

    if not shell:
        if output:
            proc = subprocess.Popen(
                shlex.split(args), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cd
            )
            while True:
                output = proc.stdout.readline()
                if output == b"" and proc.poll() is not None:
                    return
                if output:
                    print(output.decode("utf-8").strip())
        return subprocess.run(shlex.split(args), cwd=cd).returncode
    else:
        if output:
            return (
                subprocess.run(
                    args,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    cwd=cd,
                )
                .stdout.decode("utf-8")
                .strip()
            )
        return subprocess.run(args, shell=True, cwd=cd).returncode

def loadingAn(name="cal"):
      from IPython.display import HTML

      if name == "cal":
          return display(HTML('<style>.lds-ring {   display: inline-block;   position: relative;   width: 34px;   height: 34px; } .lds-ring div {   box-sizing: border-box;   display: block;   position: absolute;   width: 34px;   height: 34px;   margin: 4px;   border: 5px solid #cef;   border-radius: 50%;   animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;   border-color: #cef transparent transparent transparent; } .lds-ring div:nth-child(1) {   animation-delay: -0.45s; } .lds-ring div:nth-child(2) {   animation-delay: -0.3s; } .lds-ring div:nth-child(3) {   animation-delay: -0.15s; } @keyframes lds-ring {   0% {     transform: rotate(0deg);   }   100% {     transform: rotate(360deg);   } }</style><div class="lds-ring"><div></div><div></div><div></div><div></div></div>'))
      elif name == "lds":
          return display(HTML('''<style>.lds-hourglass {  display: inline-block;  position: relative;  width: 34px;  height: 34px;}.lds-hourglass:after {  content: " ";  display: block;  border-radius: 50%;  width: 34px;  height: 34px;  margin: 0px;  box-sizing: border-box;  border: 20px solid #dfc;  border-color: #dfc transparent #dfc transparent;  animation: lds-hourglass 1.2s infinite;}@keyframes lds-hourglass {  0% {    transform: rotate(0);    animation-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19);  }  50% {    transform: rotate(900deg);    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);  }  100% {    transform: rotate(1800deg);  }}</style><div class="lds-hourglass"></div>'''))

def textAn(TEXT, ty='d'):
      from IPython.display import HTML

      if ty == 'd':
            return display(HTML('''<style>@import url(https://fonts.googleapis.com/css?family=Raleway:400,700,900,400italic,700italic,900italic);#wrapper {   font: 17px 'Raleway', sans-serif;animation: text-shadow 1.5s ease-in-out infinite;    margin-left: auto;    margin-right: auto;    }#container {    display: flex;    flex-direction: column;    float: left;     }@keyframes text-shadow { 0% 20% {          transform: translateY(-0.1em);        text-shadow:             0 0.1em 0 #0c2ffb,             0 0.1em 0 #2cfcfd,             0 -0.1em 0 #fb203b,             0 -0.1em 0 #fefc4b;    }    40% {          transform: translateY(0.1em);        text-shadow:             0 -0.1em 0 #0c2ffb,             0 -0.1em 0 #2cfcfd,             0 0.1em 0 #fb203b,             0 0.1em 0 #fefc4b;    }       60% {        transform: translateY(-0.1em);        text-shadow:             0 0.1em 0 #0c2ffb,             0 0.1em 0 #2cfcfd,             0 -0.1em 0 #fb203b,             0 -0.1em 0 #fefc4b;    }   }@media (prefers-reduced-motion: reduce) {    * {      animation: none !important;      transition: none !important;    }}</style><div id="wrapper"><div id="container">'''+TEXT+'''</div></div>'''))
      elif ty == 'twg':
            textcover = str(len(TEXT)*0.55)
            return display(HTML('''<style>@import url(https://fonts.googleapis.com/css?family=Anonymous+Pro);.line-1{font-family: 'Anonymous Pro', monospace;    position: relative;   border-right: 1px solid;    font-size: 15px;   white-space: nowrap;    overflow: hidden;    }.anim-typewriter{  animation: typewriter 0.4s steps(44) 0.2s 1 normal both,             blinkTextCursor 600ms steps(44) infinite normal;}@keyframes typewriter{  from{width: 0;}  to{width: '''+textcover+'''em;}}@keyframes blinkTextCursor{  from{border-right:2px;}  to{border-right-color: transparent;}}</style><div class="line-1 anim-typewriter">'''+TEXT+'''</div>'''))

