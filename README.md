# webrtc-python-tornado
WebRTC sample with tornado signal server 

 **W**ebRTC provides web browsers and mobile applications with real-time communication to 
each other,WebRTC used in this project for two client(peer) with tornado signal server .(if you don't know about 
WebRTC visit this address https://www.html5rocks.com/en/tutorials/webrtc/basics/)

**requirement:** <br/>
   <ul>
        <li> tornado 
   </ul>

**RUN :**

`python3 app.py`

See in browser : `localhost:8383/`


**Warning**: It is highly recommended to use headphones when testing these samples, as it will otherwise risk loud audio feedback on your system.
   
**Note** : If you want to use this project on public network you need 
to setup open-source **COTUREN** project on your server and next configure 
TURN server in `index.html`, for testing you can use google STUN server as configured in 
`index.html` .( Also if needed for install and configure COTURN server
, I recommend follow this https://ourcodeworld.com/articles/read/1175/how-to-create-and-configure-your-own-stun-turn-server-with-coturn-in-ubuntu-18-04 )
  