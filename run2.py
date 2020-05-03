#@title <center><h1><b>MÁY ẢO</b></h1></center>
import os
import random
import string
import urllib.request
from IPython.display import HTML, clear_output
import time
start = time.time()
#####################################
USE_FREE_TOKEN = False  
CREATE_VNC = True 
TOKEN = "1ZhtP4sxj3UlEpGURFzVPQ1IbN8_4HnyCQB4pH4vuAEY5yWcK" # @param ["1ZhtP4sxj3UlEpGURFzVPQ1IbN8_4HnyCQB4pH4vuAEY5yWcK", "1Zi0Ew278Eflx5NSppqVbmgMsGV_3fWdedaPY1pcRZKnQkf17", "1Zi2uScfkAJXkSe6DbdkdzyIIie_7ysim3A2Dpo9gzuoHua3s", "1Zi31uGY5J1TQU3OHpcFFRlDHgH_6of2bKHuqeq3CbwBeb72K", "1Zi35XM2Ll17gkfyrVMCBZyZtSp_2JuUNUaLQR3rrYBBDGfkj", "1Zi38zk1d08VHRGTbNDfTkEwwOE_GRDCgRGmH6Q9R2WQsERz", "1Zi3CpoqGlZhBksJsQBi5Ow6oPl_46Rax1YQPcQCQWHqY3PvG", "1Zi3HFhCxa3fRktJZHgZt8gxyNK_62zc3D5Ye2T6ff9Pokn3v", "1Zi3KgmdZOJarEqT5u3lx5h1QEp_gJ66Hz1gfFLTHK21o5Gu", "1Zi3Ovjf8d4GZHkQ1y21JNuJ5gZ_7VfLNw8jcvgoCYVXZ1oTD", "1Zi3VuezTeOWKOcwZ7Clmm1EaV6_3iRY8seuSVzgLrXx1LmsR", "1Zi3aFb4OFXxrINVZmmSma8DZ3b_6Ai1Ja7mG5eV29hTb5jDm", "1Zi3huozsbtJWS8CrACvwIOdCS2_5qbnuYR3LW5npbqe22VGS", "1Zi3oHtrE7gq43QmXy2kVncjw3w_3L8uNByyk8CaNFLHWUyZb", "1Zi3t2NnrOHD0SDHXXg2g3qk3DX_gRopZWb3Rw3thLosvYic", "1ZiBYmER8x6Gnsh9vA80lR5L1Nn_b3DExiitAso2gS3E6uGP", "1ZiBdsZNdjMUPcq4IBo6ocd7U6P_2Vgg4K2EdJkz4kJgT4uHX", "1ZiBmJuZc9zRLOv3Mk2gtyufCSV_5tsNuStPATFf4VXuaqE1T", "1ZiBsgnrO7X7Tn8MB7bFVNv2pY5_2yoPmuoYqnf9f69M5hjA4", "1ZiC30h10L1MPsVVBKQkxPJdXE3_3ygCZJpTZahh7PbuaPkAM", "1ZiC9D7GzqW3tqijtNKC7M9wTX9_7EbnUdZRbsXNApDGjfDnt", "1ZiCNJIXMbFwRPWvz2jaZQI8pra_7wKMLyKMwNTBuCRP7JiCH", "1ZiClTLut5EreftSakJJCpnMgtR_2Ses3xSP2Ay1PCNRWkpmJ", "1ZiCzzV7QdR8PNDlPw061SHIlH3_5y1PouFDmL6NpnFpBXywR", "1ZiDEgLRqSIhdAlCSpAFGvXFf64_48Hoze2qA9BpU7vuXbzP7", "1ZiDkIXY3cFZ150235Gj2dW4ONn_48Q8RJA4q7Ny2xvPzAVhu", "1ZiDnGRsUIBs0GTXLBmIVhLa4x5_2tZkDHeYh3DRohrQWyCkq", "1ZiDpt5agobohadElvl9mxDETZC_3rJCxPpKx8ZbthjEbQJre", "1bAPvz17nK3EqD9pcZxjlbBCCAH_65z7Abb736FX6PUVKRXYh", "1ZiDrtSCPf5I4uEklnVVBGxLGWQ_4emH7mdinGtEMSP7Bv4Ek", "1ZiE9sBa1FYLIwDsZNk9YwyJEAL_4RnJg91frtRiiQYMx9HpL", "1ZiEGGfMn8Rj4wEz32KjRfeQju6_3Xy8iMr1euXtK5BNdGAPc", "1ZiEJGkyWVDZ7pkZzx6tcor35U9_4LFJqUzqgLXUHpmNXsZAR", "1ZiEMgjcRDASksJq6WdzZD9oU51_5chQpa4dDcSXmQLVn9vnm", "1ZiEPckIOFa6rQO39M5otDO5wEG_73thNjf3RzKFb16gXn7Rf", "1ZiESVkjlcLiu1COnmGNn0Rd81o_6BB6RwgLBfPfQDaFsauHc", "1ZiEVsK2GQxf2r9PmfcL4Enxrlq_7BCLAewEu5X9ckrmkZHsp", "1ZiEZPSG7kYPftGyzs1u8mtErvm_3AQ4dDJ9UbmkG6yEZqzgv", "1ZiEcOMDij2kvmdosvbqKkeJmex_JrDf2nbpWtUT2FW76xME", "1ZiEff53MvCbPzXPUblHrAYHViS_4ccorbhUwripk1EmCUdH4", "1ZiEiNv3ZsRnb9hVA3uMkwTVuGd_6b8Lhbkaj5KowJgk7oDAh", "1ZiElIaT2Wf3j1QH7NkK1veZein_2okrDKJL8gwmf1RofMTYt", "1ZiEo92uQG6R3Qu0ZfW9x3SrfXt_27ChkeZPniruuXzEFvKRG", "1ZiEqqSmfIeZZPjuqkVPdrAMigO_5x5N7NEbz1ZofNCjciDAc", "1ZiEu27M8iC7ee8l1CfgI5gdwcX_7MeNz73qdgtyGxMqBUC3a", "1ZiEwqco4F0FToMxXOhpSZG4hHs_4o7TKVyAwJaNUkF7xGSk6", "1ZiF0MZbvBqIqV3T1eT8k47ho5t_4xswBhQgYPAjMAftRuMCK", "1ZiF37uqDc2v26RWbqd2ux8Nknc_MyyhNC8g2sbsdWi1wk7s", "1ZiF6Lp82uedbDEneX3s71VFAxr_AvywvdaHQpHBbst8Kse5", "1ZiF8rzxTs8RwP6RhzJfSm27Q6G_7yBGR3XZxBQtkN8g1HvRh"]
May = "May01" # @param ["May01", "May02", "May03", "May04", "May05", "May06", "May07", "May08", "May09", "May10", "May11", "May12", "May13", "May14", "May15", "May16", "May17", "May18", "May19", "May20", "May21", "May22", "May23", "May24", "May25", "May26", "May27", "May28", "May29", "May30", "May31", "May32", "May33", "May34", "May35", "May36", "May37", "May38", "May39", "May40", "May41", "May42", "May43", "May44", "May45", "May46", "May47", "May48", "May49", "May50"]

HOME = os.path.expanduser("~")
runW = get_ipython()

if not os.path.exists(f"{HOME}/.ipython/ttmg.py"):

    hCode = "https://raw.githubusercontent.com/vlh11098/" \
                "colabx/master/res/ttmg.py"
    urllib.request.urlretrieve(hCode, f"{HOME}/.ipython/ttmg.py")

from ttmg import (
    runSh,
    loadingAn,
    ngrok,
    displayUrl,
    findProcess,
    CWD,
    textAn,
)

loadingAn()

# password ganarate
try:
  print(f"Found old password! : {password}")
except:
  password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(20))



if CREATE_VNC:
  clear_output()
 # textAn("Wait 5 minutes....")
  os.makedirs(f'{HOME}/.vnc', exist_ok=True)
  runW.system_raw('add-apt-repository -y ppa:apt-fast/stable < /dev/null')
  runW.system_raw('echo debconf apt-fast/maxdownloads string 16 | debconf-set-selections')
  runW.system_raw('echo debconf apt-fast/dlflag boolean true | debconf-set-selections')
  runW.system_raw('echo debconf apt-fast/aptmanager string apt-get | debconf-set-selections')
  runW.system_raw('apt install -y apt-fast')
  runW.system_raw('apt-fast install -y lxde caja actiona gdebi autocutsel tightvncserver')
  runW.system_raw('mv /usr/bin/lxpolkit /usr/bin/lxpolkit.bak')
  runW.system_raw('sudo apt-get autoremove --purge clipit')
  runW.system_raw(rf'echo "1971" | vncpasswd -f > ~/.vnc/passwd')
  data = """
#!/bin/bash
/usr/bin/autocutsel -s CLIPBOARD -fork
xrdb $HOME/.Xresources
xsetroot -solid grey -cursor_name left_ptr
/etc/X11/Xsession
autocutsel -fork
/usr/bin/lxsession -s LXDE -e LXDE
"""
  with open(f'{HOME}/.vnc/xstartup', 'w+') as wNow:
    wNow.write(data)
  os.chmod(f'{HOME}/.vnc/xstartup', 0o755)
  os.chmod(f'{HOME}/.vnc/passwd', 0o400)
  runSh('sudo vncserver :1 -geometry 1600x900 -economictranslate -dontdisconnect &', 
        shell=True)
  runSh(f'git clone https://github.com/novnc/noVNC.git {CWD}/noVNC')
  runSh("bash noVNC/utils/launch.sh --listen 6080 --vnc localhost:5901 &",
        shell=True)

# MY_CONFIG
#Start rClone
##################### Share_Drive ######################
rclone_config_name = 'Share_Drive'
local_mount_location = '/content/Share_Drive/' 
runW.system_raw('rm -rf /content/sample_data/')
runW.system_raw('curl -s https://rclone.org/install.sh | sudo bash')
runW.system_raw('wget https://colab.gq/share.conf')
runW.system_raw('mv -f /content/share.conf /root/.rclone.conf')
runW.system_raw('chmod 666 /root/.rclone.conf')
open("nohup.out", 'w').close()
runW.system_raw('fusermount -u $local_mount_location 2>/dev/null')
runW.system_raw('mkdir $local_mount_location 2>/dev/null')
runW.system_raw('nohup rclone mount $rclone_config_name: $local_mount_location --buffer-size 96M &')
runW.system_raw('rm nohup.out')
##################### My_Drive ########################
rclone_config_name = 'My_Drive'
local_mount_location = '/content/My_Drive/' 
runW.system_raw('wget https://colab.gq/my.conf')
runW.system_raw('mv -f /content/my.conf /root/.rclone.conf')
runW.system_raw('chmod 666 /root/.rclone.conf')
open("nohup.out", 'w').close()
runW.system_raw('fusermount -u $local_mount_location 2>/dev/null')
runW.system_raw('mkdir $local_mount_location 2>/dev/null')
runW.system_raw('nohup rclone mount $rclone_config_name: $local_mount_location --buffer-size 96M &')
runW.system_raw('rm nohup.out')
#End rClone
runW.system_raw('sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl')
runW.system_raw('sudo chmod a+rx /usr/local/bin/youtube-dl')
runW.system_raw('cp /usr/share/applications/caja.desktop /root/Desktop/')
runW.system_raw('cp /usr/share/applications/lxterminal.desktop /root/Desktop/')
runW.system_raw('cp /content/Share_Drive/Youtube-DL/00/{May}.sh /root/Desktop/')
runW.system_raw('sudo chmod +x /root/Desktop/{May}sh')
runW.system_raw('cp /content/Share_Drive/Actiona/{May}.ascr /root/Desktop/')

# START_SERVER
# Ngrok region 'us','eu','ap','au','sa','jp','in'
clear_output()
Server = ngrok(TOKEN, USE_FREE_TOKEN, [['ssh', 22, 'tcp'], 
               ['vnc', 6080, 'https']], 'in', 
               [f"{HOME}/.ngrok2/ngrok06.yml", 4045])
data = Server.start('ssh', displayB=False)
# output
Host,port = data['url'][7:].split(':')
data2 = Server.start('vnc', displayB=False)
clear_output()
if CREATE_VNC:
  displayUrl(data2, pNamU='',
            EcUrl=f'/vnc.html?autoconnect=true&password={1971}&reconnect=1&shared=0&autoconnect=1&resize=scale')

end = time.time()
print(May)
print('Thời gian: %s phút' % round(((end - start)/60),1))

#Start ngrok to Google-sheet
time.sleep(30) 
runW.system_raw('rm /content/My_Drive/www.netlify.ml/{May}.html')
runW.system_raw('pip install nbconvert')
runW.system_raw('jupyter nbconvert --to html /content/Share_Drive/50-Colab/{May}.ipynb')
runW.system_raw('mv /content/Share_Drive/50-Colab/{May}.html /content/My_Drive/www.netlify.ml/')
#End ngrok to Google-sheet


