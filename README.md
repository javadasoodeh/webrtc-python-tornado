# webrtc-python-tornado
WebRTC sample with tornado signal server 

**requirement:** <br/>
   <ul>
        <li> tornado 
   </ul>

**RUN :**

`python3 app.py`

see in browser : `localhost:8383/`

   
Note : If you want to use this project on public network you need 
to setup open-source **COTUREN** project on your server and next configure 
TURN server in `index.html`, for testing you can use google STUN server as configured in 
`index.html` .( Also if needed for install and configure COTURN server
, I recommend follow this https://ourcodeworld.com/articles/read/1175/how-to-create-and-configure-your-own-stun-turn-server-with-coturn-in-ubuntu-18-04 )
  