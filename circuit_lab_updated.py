import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="CIRCUIT LAB | Virtual Electronics Lab",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Outfit:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');
:root { color-scheme: dark; }
.stApp {
  background: radial-gradient(ellipse at 15% 0%, #1a3560 0%, #101a32 42%, #090f20 100%);
  color: #eef5ff;
}
html, body, [class*="css"] { font-family: 'Outfit', sans-serif; }
h1,h2,h3 { font-family:'Space Grotesk',sans-serif !important; }
.hero { padding: 10px 2px 16px; }
.hero h1 { font-size: clamp(2rem,4vw,3.4rem); line-height:1.05; margin:0; font-weight:800; }
.hero p { color:#a9bddf; margin:.55rem 0 0; font-size:1rem; }
div[data-testid="stSidebar"] { background:linear-gradient(180deg,#101d39,#0b1429); border-right:1px solid #263b61; }
div[data-testid="stMetric"] { background:#142644; border:1px solid #2d4b76; padding:12px; border-radius:14px; }
div[data-testid="stAlert"] { border-radius:12px; }
.stButton button { border-radius:10px; font-weight:700; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <h1>⚡ CIRCUIT <span style="color:#66e6ff">LAB</span></h1>
  <p>A colourful, realistic 3D electronics laboratory — build circuits, inspect components and experiment with low-voltage DC electronics.</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🧪 Laboratory guide")
    st.markdown("""
**Build**
1. Add parts from the component tray.
2. Drag a component to position it.
3. Click a terminal, then another terminal to draw a wire.
4. Double-click a part to inspect it.

**Experiment**
- Change resistor and battery values in the inspector.
- Press **Simulate** to check circuit continuity and estimate current.
- Use the code panel to explore an Arduino-style example.

**Important:** This is an educational software simulator, not a physical hardware controller or a certified circuit-design tool. Use only safe, low-voltage learning examples. Never connect this learning model to mains electricity or use it as a guide for live electrical work.
""")
    st.markdown("---")
    st.markdown("### 📚 What is included")
    st.write("Battery · Resistor · LED · Switch · Arduino Uno · Breadboard · Potentiometer · LDR · Buzzer · Servo · Ammeter · Voltmeter · Motor · Diode · Transistor · Capacitor · Inductor")
    st.markdown("---")
    st.caption("3D engine: Three.js · App shell: Streamlit")

LAB_HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Outfit:wght@400;500;600;700;800&display=swap');
*{box-sizing:border-box}
body{margin:0;background:#091326;color:#edf4ff;font-family:Outfit,Arial,sans-serif}
button,input,select{font:inherit}
button{cursor:pointer}
#app{height:940px;display:flex;flex-direction:column;background:linear-gradient(135deg,#0b1730,#101d39 55%,#10142d)}
#header{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:11px 15px;background:#101d38;border-bottom:1px solid #2a4169}
.brand{font-weight:800;font-size:17px;letter-spacing:.2px}.brand span{color:#6ce8ff}
.sub{font-size:11px;color:#9fb4d9;margin-top:2px}
.actions{display:flex;gap:7px;flex-wrap:wrap}
.btn{border:1px solid #405a88;background:#1a2d50;color:#eaf3ff;padding:9px 12px;border-radius:9px;font-weight:700;font-size:12px}
.btn.primary{border:0;background:linear-gradient(100deg,#51d9e8,#7f8dff);color:#07142b}
.btn.danger{background:#43253a;border-color:#82415a}
#layout{display:grid;grid-template-columns:190px minmax(0,1fr) 270px;min-height:0;flex:1}
#tray{padding:13px;background:#0e1a33;border-right:1px solid #273d63;overflow:auto}
.section{font-size:10px;text-transform:uppercase;letter-spacing:1.4px;color:#8fa8d3;font-weight:800;margin:5px 0 10px}
.partbtn{width:100%;display:flex;align-items:center;gap:9px;text-align:left;margin:0 0 7px;padding:9px;border-radius:10px;border:1px solid #293f66;background:linear-gradient(135deg,#172b4d,#14213d);color:#eaf2ff;font-size:12px;font-weight:700}
.partbtn:hover{border-color:#65dff4;background:#1b345a}
.particon{width:29px;height:29px;display:grid;place-items:center;border-radius:8px;background:#253d68;font-size:16px}
.partbtn small{display:block;color:#91a8d0;font-weight:400;font-size:10px}
#stage{position:relative;min-width:0;min-height:450px;background:radial-gradient(ellipse at 50% 40%,#1c3156,#0b1429 75%)}
#canvas{width:100%;height:100%;display:block;touch-action:none}
#overlay{position:absolute;left:12px;top:12px;display:flex;gap:7px;flex-wrap:wrap;pointer-events:none}
.chip{background:#101f3bdc;border:1px solid #38537e;color:#c7d9f8;border-radius:8px;padding:6px 9px;font-size:10px;backdrop-filter:blur(8px)}
#help{position:absolute;left:12px;bottom:12px;max-width:calc(100% - 24px);background:#101d38e8;border:1px solid #3a527c;border-radius:10px;padding:8px 10px;color:#b9cbed;font-size:11px;pointer-events:none}
#right{background:#0e1a33;border-left:1px solid #273d63;overflow:auto;padding:13px}
.card{background:linear-gradient(145deg,#17294a,#13213c);border:1px solid #2d4772;border-radius:12px;padding:11px;margin-bottom:11px}
.card h3{font-size:13px;margin:0 0 9px;color:#8deaff}
.muted{font-size:11px;color:#a9bddf;line-height:1.5}
#selectionName{font-size:16px;font-weight:800;margin-bottom:4px}
.field{margin:9px 0}.field label{display:block;color:#a9bddf;font-size:10px;margin-bottom:4px}
.field input,.field select{width:100%;padding:8px;border-radius:8px;background:#0b1730;border:1px solid #38537e;color:#f3f7ff;outline:none}
#explain{font-size:11px;color:#c7d7f1;line-height:1.5}
#readout{font-family:'DM Mono',monospace;font-size:11px;line-height:1.7;color:#b9f6e8;white-space:pre-line}
#meters{display:grid;grid-template-columns:1fr 1fr;gap:7px;margin-top:9px}
.meter{background:#0a1830;border:1px solid #38537e;border-radius:9px;padding:8px}
.meter b{display:block;font:700 10px 'Outfit';color:#9fb4d9}
.meter strong{display:block;font:700 17px 'DM Mono';color:#8ef4dc;margin-top:3px}
#popup{display:none;position:absolute;z-index:20;left:50%;top:50%;transform:translate(-50%,-50%);width:min(390px,calc(100% - 28px));background:#172846;border:1px solid #ffb86b;border-radius:15px;padding:15px;box-shadow:0 18px 60px #000b}
#popup.show{display:block}
#popup h3{margin:0 0 7px;color:#ffd08a;font-size:15px}
#popup p{font-size:12px;line-height:1.5;color:#d7e4fa;margin:6px 0}
#popup button{margin-top:8px}
#footer{padding:9px 13px;border-top:1px solid #293f65;background:#0d1931;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap}
#message{font-size:11px;color:#b9cbed}
#code{width:100%;min-height:100px;resize:vertical;background:#09152a;color:#b9f6e8;border:1px solid #304a75;border-radius:8px;padding:9px;font-family:'DM Mono',monospace;font-size:10px;line-height:1.5}
@media(max-width:900px){
 #app{height:1180px}
 #layout{grid-template-columns:145px minmax(0,1fr);grid-template-rows:minmax(500px,1fr) 310px}
 #tray{grid-column:1;grid-row:1 / 3}
 #stage{grid-column:2;grid-row:1}
 #right{grid-column:2;grid-row:2;border-left:0;border-top:1px solid #273d63;display:grid;grid-template-columns:1fr 1fr;gap:8px;align-content:start}
 .card{margin:0}
}
@media(max-width:560px){
 #app{height:1450px}
 #layout{display:flex;flex-direction:column}
 #tray{display:flex;gap:6px;overflow-x:auto;border-right:0;border-bottom:1px solid #273d63;padding:8px}
 #tray .section{display:none}
 .partbtn{min-width:115px;margin:0}
 #stage{height:520px;flex:none}
 #right{display:block}
}
</style>
</head>
<body>
<div id="app">
 <header id="header">
  <div><div class="brand">⚡ CIRCUIT <span>LAB</span></div><div class="sub">3D electronics workbench · low-voltage learning simulator</div></div>
  <div class="actions">
   <button class="btn" id="reset">↺ Reset</button>
   <button class="btn" id="clear">Clear wires</button>
   <button class="btn primary" id="simulate">▶ Simulate</button>
  </div>
 </header>
 <div id="layout">
  <aside id="tray">
   <div class="section">Component library</div>
   <button class="partbtn" data-add="battery"><span class="particon">🔋</span><span>Battery<small>DC source</small></span></button>
   <button class="partbtn" data-add="resistor"><span class="particon">〰️</span><span>Resistor<small>Current limiting</small></span></button>
   <button class="partbtn" data-add="led"><span class="particon">💡</span><span>LED<small>Light emitting diode</small></span></button>
   <button class="partbtn" data-add="switch"><span class="particon">⏻</span><span>Switch<small>Open / closed</small></span></button>
   <button class="partbtn" data-add="arduino"><span class="particon">🟦</span><span>Arduino Uno<small>Microcontroller</small></span></button>
   <button class="partbtn" data-add="breadboard"><span class="particon">▦</span><span>Breadboard<small>Prototyping board</small></span></button>
   <button class="partbtn" data-add="pot"><span class="particon">🎚️</span><span>Potentiometer<small>Variable resistor</small></span></button>
   <button class="partbtn" data-add="ldr"><span class="particon">☀️</span><span>LDR sensor<small>Light dependent</small></span></button>
   <button class="partbtn" data-add="buzzer"><span class="particon">🔊</span><span>Buzzer<small>Sound output</small></span></button>
   <button class="partbtn" data-add="servo"><span class="particon">⚙️</span><span>Servo motor<small>Position actuator</small></span></button>
   <button class="partbtn" data-add="ammeter"><span class="particon">🅰️</span><span>Ammeter<small>Measures current · series</small></span></button>
   <button class="partbtn" data-add="voltmeter"><span class="particon">Ⓥ</span><span>Voltmeter<small>Measures voltage · parallel</small></span></button>
   <button class="partbtn" data-add="motor"><span class="particon">🌀</span><span>DC motor<small>Electrical to motion</small></span></button>
   <button class="partbtn" data-add="diode"><span class="particon">🔻</span><span>Diode<small>One-way current</small></span></button>
   <button class="partbtn" data-add="transistor"><span class="particon">🔀</span><span>NPN transistor<small>Electronic switch</small></span></button>
   <button class="partbtn" data-add="capacitor"><span class="particon">▤</span><span>Capacitor</span><small>Stores electric charge</small></button>
   <button class="partbtn" data-add="inductor"><span class="particon">〰️</span><span>Inductor</span><small>Magnetic energy storage</small></button>
  </aside>
  <main id="stage">
   <canvas id="canvas"></canvas>
   <div id="overlay"><span class="chip">● 3D WORKSPACE</span><span class="chip">Drag to move · orbit to inspect</span></div>
   <div id="help">Click one terminal, then another to wire · Double-click a component for its explanation · Drag parts to move · Scroll to zoom</div>
   <div id="popup" role="alert"><h3 id="popupTitle">⚠ Circuit coach</h3><p id="popupBody"></p><p id="popupFix"></p><button class="btn primary" id="popupClose">Got it — let's fix it</button></div>
  </main>
  <aside id="right">
   <section class="card">
    <h3>◈ Component inspector</h3>
    <div id="selectionName">No component selected</div>
    <div class="muted" id="selectionHint">Double-click a component in the 3D lab to inspect it.</div>
    <div id="fields"></div>
    <div id="explain" style="margin-top:9px"></div>
   </section>
   <section class="card">
    <h3>⚡ Simulation console</h3>
    <div id="readout">STATUS: READY
SOURCE: —
CURRENT: —
LED: OFF

Connect a circuit and press Simulate.</div>
    <div id="meters">
     <div class="meter"><b>VOLTAGE (V)</b><strong id="vLive">— V</strong></div>
     <div class="meter"><b>CURRENT (I)</b><strong id="iLive">— A</strong></div>
     <div class="meter"><b>RESISTANCE (R)</b><strong id="rLive">— Ω</strong></div>
     <div class="meter"><b>RESISTIVITY (ρ)</b><strong id="rhoLive">— Ω·m</strong></div>
    </div>
   </section>
   <section class="card">
    <h3>⌨ Arduino code sandbox</h3>
    <div class="muted" style="margin-bottom:7px">Example sketch for learning. This editor does not upload code to a physical Arduino.</div>
    <textarea id="code">const int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  digitalWrite(ledPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, LOW);
  delay(1000);
}</textarea>
    <button class="btn" id="checkCode" style="margin-top:7px;width:100%">Check sketch structure</button>
    <div class="muted" id="codeResult" style="margin-top:7px"></div>
   </section>
   <section class="card">
    <h3>🏁 Engineering missions</h3>
    <div class="muted">Mission 1: make a safe LED indicator with a series resistor.<br>Mission 2: measure current by placing the ammeter in series.<br>Mission 3: measure voltage by placing the voltmeter in parallel.<br>Mission 4: build a light-sensing night-lamp concept with an LDR.<br>Mission 5: explore how changing resistance affects current.</div>
   </section>
   <section class="card">
    <h3>🧭 Learning notes</h3>
    <div class="muted">A real circuit needs a complete conductive path. A resistor limits current. An LED is polarised, so its anode and cathode direction matters. This prototype uses a simplified educational circuit check, not a full SPICE-grade solver.</div>
   </section>
  </aside>
 </div>
 <footer id="footer"><span id="message">Ready — add components from the library.</span><span class="muted">Low-voltage learning model · Not a certified engineering solver</span></footer>
</div>
<script type="importmap">
{"imports":{"three":"https://unpkg.com/three@0.160.0/build/three.module.js","three/addons/":"https://unpkg.com/three@0.160.0/examples/jsm/"}}
</script>
<script type="module">
import * as THREE from 'three';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js';

const $=id=>document.getElementById(id);
const canvas=$('canvas'),scene=new THREE.Scene();
scene.background=new THREE.Color(0x0b1429);scene.fog=new THREE.Fog(0x0b1429,17,42);
const camera=new THREE.PerspectiveCamera(46,1,.1,100);camera.position.set(8,8.5,11);
const renderer=new THREE.WebGLRenderer({canvas,antialias:true,alpha:false});
renderer.setPixelRatio(Math.min(devicePixelRatio,2));renderer.shadowMap.enabled=true;renderer.shadowMap.type=THREE.PCFSoftShadowMap;renderer.outputColorSpace=THREE.SRGBColorSpace;
const controls=new OrbitControls(camera,canvas);controls.enableDamping=true;controls.target.set(0,.3,0);controls.maxPolarAngle=Math.PI*.48;
scene.add(new THREE.HemisphereLight(0xc7e6ff,0x18203c,2.1));
const key=new THREE.DirectionalLight(0xffffff,2.5);key.position.set(5,11,7);key.castShadow=true;key.shadow.mapSize.set(2048,2048);scene.add(key);
const fill=new THREE.PointLight(0x46cfff,22,18);fill.position.set(-5,5,-4);scene.add(fill);
const purple=new THREE.PointLight(0x806bff,14,16);purple.position.set(5,4,4);scene.add(purple);
const M=(c,metal=0,rough=.45,em=0)=>new THREE.MeshStandardMaterial({color:c,metalness:metal,roughness:rough,emissive:em});
const floor=new THREE.Mesh(new THREE.PlaneGeometry(200,200),M(0x101a30));floor.rotation.x=-Math.PI/2;floor.position.y=-.3;floor.receiveShadow=true;scene.add(floor);
const table=new THREE.Mesh(new THREE.BoxGeometry(12,.35,8),M(0x26334b,.35,.32));table.position.y=-.13;table.castShadow=true;table.receiveShadow=true;scene.add(table);
const grid=new THREE.GridHelper(20,40,0x41618c,0x253b60);grid.position.y=.05;scene.add(grid);
const parts=new Map(),wires=[],wireGroup=new THREE.Group();scene.add(wireGroup);
let serial=0,selected=null,wireStart=null,drag=null,ledOn=false;

const catalog={
 battery:{title:'9V Battery',emoji:'🔋',desc:'A DC source that converts stored chemical energy into electrical energy. It provides a potential difference between its positive and negative terminals.',use:'Portable projects, toys and small electronic circuits.',how:'When a closed circuit connects its terminals, the battery can drive current through the external components.',term:['+','−'],value:9,unit:'V'},
 resistor:{title:'Resistor',emoji:'〰️',desc:'A passive component that opposes current flow. Resistance is measured in ohms (Ω).',use:'Limiting LED current, setting voltages and controlling signal levels.',how:'For an ideal ohmic resistor, voltage equals current multiplied by resistance: V = I × R.',term:['A','B'],value:220,unit:'Ω'},
 led:{title:'Red LED',emoji:'💡',desc:'A light-emitting diode that produces light when current flows in the forward direction.',use:'Status indicators, displays and lighting.',how:'The anode (+) should be at a higher potential than the cathode (−). A series resistor is normally required to limit current.',term:['Anode +','Cathode −'],value:2,unit:'V forward drop'},
 switch:{title:'SPST Switch',emoji:'⏻',desc:'A switch opens or closes an electrical path.',use:'Power controls and user-operated circuit inputs.',how:'When closed, the contacts are connected. When open, the path is interrupted.',term:['IN','OUT'],value:1,unit:'Closed (1)'},
 arduino:{title:'Arduino Uno',emoji:'🟦',desc:'A microcontroller development board used to read inputs and control outputs with a program.',use:'Robotics, sensors, automation and interactive projects.',how:'The microcontroller executes uploaded code. Digital pins can read HIGH/LOW or drive suitable outputs.',term:['5V','GND','D2','D13'],value:5,unit:'V logic'},
 breadboard:{title:'Breadboard',emoji:'▦',desc:'A solderless prototyping board for assembling temporary circuits.',use:'Testing connections before building a permanent circuit.',how:'Groups of holes are connected internally by metal clips. The centre channel separates the two terminal strips.',term:['+ rail','− rail'],value:0,unit:'Passive'},
 pot:{title:'Potentiometer',emoji:'🎚️',desc:'A three-terminal variable resistor. Its wiper moves along a resistive track.',use:'Adjusting levels, sensor inputs and voltage dividers.',how:'Turning the shaft changes the resistance ratio between the wiper and the two end terminals.',term:['A','Wiper','B'],value:10000,unit:'Ω'},
 ldr:{title:'LDR sensor',emoji:'☀️',desc:'A light-dependent resistor whose resistance changes with illumination.',use:'Automatic night lights and light-sensing circuits.',how:'Its resistance generally decreases as light intensity increases.',term:['A','B'],value:10000,unit:'Ω (illustrative)'},
 buzzer:{title:'Active buzzer',emoji:'🔊',desc:'An output component that produces sound when supplied with suitable electrical power.',use:'Alarms, alerts and simple sound feedback.',how:'An active buzzer contains an oscillator that drives a sound-producing element.',term:['+','−'],value:5,unit:'V nominal'},
 servo:{title:'Servo motor',emoji:'⚙️',desc:'A motor assembly with feedback control for moving to a commanded angular position.',use:'Robot arms, steering mechanisms and small mechanisms.',how:'A control signal communicates a target position; internal electronics drive the motor toward it.',term:['SIG','5V','GND'],value:90,unit:'degrees'},
 ammeter:{title:'Ammeter',emoji:'🅰️',desc:'An instrument that measures electric current in amperes (A).',use:'Measuring current flowing through a branch of a circuit.',how:'An ammeter is connected in series. Its ideal resistance is very low; placing it directly across a battery can cause a short circuit.',term:['A','COM'],value:0,unit:'A'},
 voltmeter:{title:'Voltmeter',emoji:'Ⓥ',desc:'An instrument that measures potential difference between two points.',use:'Checking battery voltage and voltage drops across components.',how:'A voltmeter is connected in parallel across the part being measured. Its ideal resistance is very high.',term:['V','COM'],value:0,unit:'V'},
 motor:{title:'Small DC motor',emoji:'🌀',desc:'A motor converts electrical energy into rotational motion.',use:'Small robots, fans and moving mechanisms.',how:'Current through the motor produces torque. A real motor also has starting current and back EMF.',term:['+','−'],value:6,unit:'V nominal'},
 diode:{title:'Rectifier diode',emoji:'🔻',desc:'A semiconductor component that mainly allows current in one direction.',use:'Reverse-polarity protection and rectification.',how:'The anode must be at a higher potential than the cathode for forward conduction.',term:['Anode','Cathode'],value:0.7,unit:'V drop'},
 transistor:{title:'NPN transistor',emoji:'🔀',desc:'A semiconductor device that can act as an electronic switch or amplifier.',use:'Driving loads from control signals and amplifying signals.',how:'A small base current can control a larger collector current, within device ratings.',term:['Base','Collector','Emitter'],value:0.7,unit:'V base-emitter'},
 capacitor:{title:'Capacitor',emoji:'▤',desc:'A component that stores energy in an electric field.',use:'Smoothing supply voltage, timing and filtering.',how:'It charges and discharges; its behaviour depends on capacitance and circuit frequency.',term:['+','−'],value:100,unit:'µF'},
 inductor:{title:'Inductor',emoji:'〰️',desc:'A coil that stores energy in a magnetic field when current flows.',use:'Filters, converters and electromagnetic circuits.',how:'It resists changes in current. Its behaviour depends on inductance and changing current.',term:['A','B'],value:10,unit:'mH'}
};

function box(g,w,h,d,material,x,y,z){const o=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),material);o.position.set(x,y,z);o.castShadow=true;o.receiveShadow=true;g.add(o);return o;}
function cyl(g,r1,r2,h,material,x,y,z,rot=0){const o=new THREE.Mesh(new THREE.CylinderGeometry(r1,r2,h,24),material);o.position.set(x,y,z);o.rotation.z=rot;o.castShadow=true;g.add(o);return o;}
function textSprite(txt,x,y,z){
 const c=document.createElement('canvas');c.width=512;c.height=128;const ctx=c.getContext('2d');ctx.font='bold 48px Arial';ctx.textAlign='center';ctx.fillStyle='#edf6ff';ctx.shadowColor='#51dfff';ctx.shadowBlur=12;ctx.fillText(txt,256,78);
 const t=new THREE.CanvasTexture(c),s=new THREE.Sprite(new THREE.SpriteMaterial({map:t,transparent:true,depthWrite:false}));s.position.set(x,y,z);s.scale.set(2.15,.54,1);scene.add(s);return s;
}
function terminal(root,name,x,y,z,color){
 const g=new THREE.Group();g.position.set(x,y,z);root.add(g);
 const socket=new THREE.Mesh(new THREE.CylinderGeometry(.085,.085,.045,20),M(0x34435e,.6));socket.rotation.x=Math.PI/2;g.add(socket);
 const ball=new THREE.Mesh(new THREE.SphereGeometry(.09,18,14),M(color,.2,.25,color));ball.position.z=.045;g.add(ball);
 g.userData={terminal:true,name};return g;
}
function createModel(type,x,z){
 const def=catalog[type];if(!def)return;
 const id=type+'_'+(++serial),root=new THREE.Group();root.position.set(x,.12,z);root.userData={partId:id,type};scene.add(root);
 const t={};
 if(type==='battery'){
  box(root,1.25,.58,.76,M(0x222b3e,.6,.3),0,.24,0);box(root,.92,.08,.6,M(0x35445d),0,.57,0);
  cyl(root,.11,.11,.13,M(0xff607b,.55),-.38,.68,0);cyl(root,.11,.11,.13,M(0x64e6ff,.55),.38,.68,0);
  t['+']=terminal(root,'+',-.38,.75,0,0xff5677);t['−']=terminal(root,'−',.38,.75,0,0x5eeaff);
 }else if(type==='resistor'){
  cyl(root,.055,.055,1.12,M(0xc4d0e3,.75),0,.13,0,Math.PI/2);
  const body=cyl(root,.18,.18,.62,M(0xd4a05c,.15),0,.15,0,Math.PI/2);
  [-.17,-.055,.06,.17].forEach((p,i)=>cyl(root,.185,.185,.045,M([0x6d3e27,0x171717,0xc34236,0xd8bd75][i]),p,.15,0,Math.PI/2));
  t.A=terminal(root,'A',-.63,.15,0,0xffd166);t.B=terminal(root,'B',.63,.15,0,0xffd166);
 }else if(type==='led'){
  cyl(root,.035,.035,.42,M(0xcbd7e9,.7),-.14,.2,0);cyl(root,.035,.035,.42,M(0xcbd7e9,.7),.14,.2,0);
  const dome=new THREE.Mesh(new THREE.SphereGeometry(.25,24,18),new THREE.MeshPhysicalMaterial({color:0xff315c,roughness:.18,transparent:true,opacity:.9,emissive:0x160008,transmission:.15}));dome.position.y=.48;root.add(dome);
  const glow=new THREE.PointLight(0xff315c,0,3.5);glow.position.y=.65;root.add(glow);root.userData.glow=glow;
  t['Anode +']=terminal(root,'Anode +',-.14,.03,0,0xff5677);t['Cathode −']=terminal(root,'Cathode −',.14,.03,0,0x5eeaff);
 }else if(type==='switch'){
  box(root,.8,.17,.58,M(0x303d59,.4),0,.1,0);cyl(root,.14,.14,.25,M(0x7c9ac8,.5),0,.31,0);
  const lever=box(root,.08,.07,.55,M(0xf0bd60,.45),0,.49,0);root.userData.lever=lever;
  t.IN=terminal(root,'IN',-.32,.17,0,0xffd166);t.OUT=terminal(root,'OUT',.32,.17,0,0xffd166);
 }else if(type==='arduino'){
  box(root,1.95,.17,1.28,M(0x087b70,.35),0,.12,0);box(root,.65,.2,.55,M(0x202b3d,.65),-.1,.28,0);
  box(root,.42,.2,.3,M(0x28364f,.6),.67,.25,.22);box(root,.35,.2,.28,M(0x27364e,.6),-.7,.25,-.25);
  for(let i=0;i<8;i++){box(root,.08,.1,.08,M(0xd4dce8,.65),-.72+i*.2,.23,-.56);box(root,.08,.1,.08,M(0xd4dce8,.65),-.72+i*.2,.23,.56);}
  t['5V']=terminal(root,'5V',-.78,.24,-.56,0xff5677);t.GND=terminal(root,'GND',.78,.24,-.56,0x5eeaff);t.D2=terminal(root,'D2',-.78,.24,.56,0xffd166);t.D13=terminal(root,'D13',.78,.24,.56,0xffd166);
 }else if(type==='breadboard'){
  box(root,2.55,.2,1.65,M(0xe5eaf1,.05,.65),0,.1,0);
  for(let r=0;r<5;r++)for(let c=0;c<24;c++){const h=cyl(root,.027,.027,.012,M(0x34415a),-1.15+c*.1,.208,-.43+r*.21);h.rotation.x=0;}
  box(root,2.4,.018,.04,M(0xff5c79),0,.22,-.69);box(root,2.4,.018,.04,M(0x4fdff1),0,.22,.69);
  t['+ rail']=terminal(root,'+ rail',-1.18,.24,-.69,0xff5677);t['− rail']=terminal(root,'− rail',1.18,.24,.69,0x5eeaff);
 }else if(type==='pot'){
  cyl(root,.29,.29,.18,M(0x202c42,.45),0,.13,0);cyl(root,.13,.13,.18,M(0x9caec9,.65),0,.3,0);
  t.A=terminal(root,'A',-.38,.15,0,0xffd166);t.Wiper=terminal(root,'Wiper',0,.15,.38,0x5eeaff);t.B=terminal(root,'B',.38,.15,0,0xffd166);
 }else if(type==='ldr'){
  cyl(root,.23,.23,.13,M(0x29334b,.5),0,.13,0);const top=cyl(root,.18,.18,.07,M(0xc6a75c,.25),0,.23,0);top.material=M(0xd2b66e,.25,.35);
  for(let i=-2;i<=2;i++)box(root,.025,.012,.27,M(0x765d35),i*.055,.27,0);
  t.A=terminal(root,'A',-.32,.15,0,0xffd166);t.B=terminal(root,'B',.32,.15,0,0xffd166);
 }else if(type==='buzzer'){
  cyl(root,.34,.34,.3,M(0x222b3d,.6),0,.18,0);cyl(root,.25,.25,.04,M(0x46516b,.5),0,.35,0);
  for(let i=0;i<3;i++)cyl(root,.035,.035,.015,M(0x111827),0,.38,-.13+i*.13);
  t['+']=terminal(root,'+',-.23,.18,0,0xff5677);t['−']=terminal(root,'−',.23,.18,0,0x5eeaff);
 }else if(type==='servo'){
  box(root,.9,.52,.62,M(0x2455a0,.35),0,.25,0);cyl(root,.17,.17,.2,M(0xabb9d1,.65),0,.62,0);
  const arm=box(root,.1,.08,.85,M(0xe9edf7,.55),0,.75,0);root.userData.arm=arm;
  t.SIG=terminal(root,'SIG',-.28,.16,-.33,0xffd166);t['5V']=terminal(root,'5V',0,.16,-.33,0xff5677);t.GND=terminal(root,'GND',.28,.16,-.33,0x5eeaff);
 }else if(type==='ammeter'||type==='voltmeter'){
  const color=type==='ammeter'?0x2a9d8f:0x4169b2;
  box(root,.9,.18,.68,M(color,.25),0,.12,0);
  box(root,.48,.025,.24,M(0x071326),0,.225,0);
  t[type==='ammeter'?'A':'V']=terminal(root,type==='ammeter'?'A':'V',-.32,.14,0,0xff5677);
  t.COM=terminal(root,'COM',.32,.14,0,0x5eeaff);
 }else if(type==='motor'){
  cyl(root,.34,.34,.65,M(0x7b879c,.7),0,.24,0,Math.PI/2);
  cyl(root,.08,.08,.55,M(0xd4dce8,.7),.48,.24,0,Math.PI/2);
  t['+']=terminal(root,'+',-.38,.15,0,0xff5677);t['−']=terminal(root,'−',.38,.15,0,0x5eeaff);
 }else if(type==='diode'){
  cyl(root,.06,.06,.9,M(0xcbd7e9,.6),0,.14,0,Math.PI/2);
  cyl(root,.16,.16,.34,M(0x27364e),0,.14,0,Math.PI/2);
  t.Anode=terminal(root,'Anode',-.48,.14,0,0xffd166);t.Cathode=terminal(root,'Cathode',.48,.14,0,0x5eeaff);
 }else if(type==='transistor'){
  cyl(root,.25,.25,.22,M(0x202b3d),0,.2,0);
  t.Base=terminal(root,'Base',-.3,.14,0,0xffd166);t.Collector=terminal(root,'Collector',0,.14,-.3,0xff5677);t.Emitter=terminal(root,'Emitter',.3,.14,0,0x5eeaff);
 }else if(type==='capacitor'){
  cyl(root,.22,.22,.5,M(0x35445d,.45),0,.25,0);
  t['+']=terminal(root,'+',-.25,.14,0,0xff5677);t['−']=terminal(root,'−',.25,.14,0,0x5eeaff);
 }else if(type==='inductor'){
  for(let i=0;i<5;i++)cyl(root,.13,.13,.12,M(0xc58b42,.6),-.28+i*.14,.2,0,Math.PI/2);
  t.A=terminal(root,'A',-.48,.14,0,0xffd166);t.B=terminal(root,'B',.48,.14,0,0xffd166);
 }
 const label=textSprite(def.title,x,.98,z);
 parts.set(id,{id,type,root,terms:t,label,values:{value:def.value},switchClosed:true});
 root.userData.partId=id;
 $('message').textContent=def.title+' added to the workbench.';
 selectPart(id);
 return id;
}
function getWorld(obj){const v=new THREE.Vector3();obj.getWorldPosition(v);return v;}
function drawWire(a,b){
 const p1=getWorld(a),p2=getWorld(b),mid=p1.clone().lerp(p2,.5);mid.y+=.38;
 const curve=new THREE.QuadraticBezierCurve3(p1,mid,p2);
 const mesh=new THREE.Mesh(new THREE.TubeGeometry(curve,28,.035,8,false),M(0x53d9f4,.35,.25,0x123849));wireGroup.add(mesh);
 wires.push({a,b,mesh});
}
function clearWires(){wires.forEach(w=>wireGroup.remove(w.mesh));wires.length=0;wireStart=null;ledOn=false;updateLeds();$('message').textContent='All wires cleared.';consoleReadout('READY','—','—','OFF');}
function updateLeds(){for(const p of parts.values())if(p.type==='led'&&p.root.userData.glow)p.root.userData.glow.intensity=ledOn?3.2:0;}
function selectPart(id){
 const p=parts.get(id);if(!p)return;selected=id;const d=catalog[p.type];
 $('selectionName').textContent=d.emoji+' '+d.title;$('selectionHint').textContent='Component ID: '+id;
 $('explain').innerHTML='<b>What it is:</b> '+d.desc+'<br><br><b>Where it is used:</b> '+d.use+'<br><br><b>How it works:</b> '+d.how;
 const fields=$('fields');fields.innerHTML='';
 if(['battery','resistor','led','pot','ldr','switch','servo','motor','capacitor','inductor'].includes(p.type)){
  const label=document.createElement('label');label.textContent=p.type==='battery'?'Voltage (V)':p.type==='resistor'?'Resistance (Ω)':p.type==='led'?'Forward drop (V)':p.type==='switch'?'Switch state':p.type==='servo'?'Target angle (degrees)':'Illustrative value';
  const wrap=document.createElement('div');wrap.className='field';wrap.appendChild(label);
  if(p.type==='switch'){
   const s=document.createElement('select');s.innerHTML='<option value="1">Closed</option><option value="0">Open</option>';s.value=p.switchClosed?'1':'0';s.onchange=()=>{p.switchClosed=s.value==='1';$('message').textContent='Switch set to '+(p.switchClosed?'closed':'open')+'.';};wrap.appendChild(s);
  }else{
   const input=document.createElement('input');input.type='number';input.min=p.type==='battery'?'0.1':'0';input.step=p.type==='resistor'?'1':'0.1';input.value=p.values.value;input.onchange=()=>{p.values.value=Math.max(Number(input.min),Number(input.value)||0);};wrap.appendChild(input);
  }
  fields.appendChild(wrap);
  if(p.type==='resistor'){
   const rhoWrap=document.createElement('div');rhoWrap.className='field';
   rhoWrap.innerHTML='<label>Material resistivity ρ (Ω·m) — illustrative</label><input id="rhoInput" type="number" min="0.000000001" step="0.000000001" value="'+(p.values.rho||0.0000017)+'">';
   fields.appendChild(rhoWrap);
   rhoWrap.querySelector('input').onchange=e=>{p.values.rho=Math.max(0,Number(e.target.value)||0);};
   const geometry=document.createElement('div');geometry.className='muted';geometry.textContent='For a uniform wire: R = ρ × L / A. Resistivity belongs to the material; resistance also depends on length and cross-sectional area.';
   fields.appendChild(geometry);
  }
 }else fields.innerHTML='<div class="muted">This component is currently shown as a 3D learning model. Its detailed electrical behaviour is not yet simulated.</div>';
}
function consoleReadout(status,source,current,led){$('readout').textContent=`STATUS: ${status}\nSOURCE: ${source}\nEST. CURRENT: ${current}\nLED: ${led}`;}
function coach(title,body,fix){
 $('popupTitle').textContent=title;$('popupBody').textContent=body;$('popupFix').textContent='HOW TO FIX: '+fix;$('popup').classList.add('show');
}
$('popupClose').onclick=()=>$('popup').classList.remove('show');
function setLive(v,i,r,rho){
 $('vLive').textContent=v;$('iLive').textContent=i;$('rLive').textContent=r;$('rhoLive').textContent=rho;
}
function checkConnection(a,b){
 const pa=partForTerminal(a),pb=partForTerminal(b);
 if(pa&&pb&&pa.id===pb.id){coach('⚠ Same-component connection','You connected two terminals on the same component. That usually does not create the circuit path you intended.','Connect a terminal to a different component, or use a wire to join two separate circuit nodes.');return false;}
 if(hasWire(a,b)){coach('🔁 Duplicate wire','These two terminals are already connected. The wire is already doing its job!','Choose a different terminal pair.');return false;}
 if((pa?.type==='ammeter'&&pb?.type==='battery'&&a===pa.terms.A&&b===pb.terms['−'])||(pb?.type==='ammeter'&&pa?.type==='battery'&&b===pb.terms.A&&a===pa.terms['−'])){
  coach('🚨 Ammeter short-circuit warning','An ammeter has very low resistance. Connecting it directly across a battery can create a short circuit.','Put the ammeter in series with the load, not directly across the battery.');return false;
 }
 return true;
}
function partForTerminal(term){for(const p of parts.values())for(const t of Object.values(p.terms))if(t===term)return p;return null;}
function hasWire(a,b){return wires.some(w=>(w.a===a&&w.b===b)||(w.a===b&&w.b===a));}
function simulate(){
 const batteries=[...parts.values()].filter(p=>p.type==='battery');
 const resistors=[...parts.values()].filter(p=>p.type==='resistor');
 const leds=[...parts.values()].filter(p=>p.type==='led');
 let found=null;
 for(const bat of batteries)for(const res of resistors)for(const led of leds){
  const direct1=hasWire(bat.terms['+'],res.terms.A)||hasWire(bat.terms['+'],res.terms.B);
  const direct2=(hasWire(res.terms.A,led.terms['Anode +'])||hasWire(res.terms.B,led.terms['Anode +']));
  const direct3=hasWire(led.terms['Cathode −'],bat.terms['−']);
  if(direct1&&direct2&&direct3)found={bat,res,led};
 }
 if(!found){
  ledOn=false;updateLeds();consoleReadout('INCOMPLETE','—','—','OFF');setLive('— V','— A','— Ω','— Ω·m');
  const allWires=wires.length;
  if(allWires===0)coach('🧭 No circuit path yet','The simulator cannot find a complete battery–resistor–LED loop. No worries: every engineer starts with a few loose wires.','Connect battery (+) to one resistor terminal, the other resistor terminal to LED anode, and LED cathode to battery (−).');
  else coach('🔎 Circuit not recognised yet','Some wires are present, but the sample LED circuit is incomplete or uses a connection pattern this simplified checker cannot solve.','Build the sample series loop first. A full general-purpose network solver is not included in this prototype.');
  $('message').textContent='Sample check: battery (+) → resistor → LED anode; LED cathode → battery (−).';return;
 }
 const {bat,res,led}=found;
 const direction=hasWire(res.terms.A,led.terms['Anode +'])?['A','B']:['B','A'];
 const first=hasWire(bat.terms['+'],res.terms[direction[0]]);
 const switchParts=[...parts.values()].filter(p=>p.type==='switch');
 const openSwitch=switchParts.some(p=>!p.switchClosed);
 const voltage=Number(bat.values.value)||9,resistance=Math.max(1,Number(res.values.value)||220),vf=Number(led.values.value)||2;
 const amps=Math.max(0,(voltage-vf)/resistance);
 const orientationOk=first&&voltage>vf&&!openSwitch;
 ledOn=orientationOk&&amps>0;updateLeds();
 const ma=(amps*1000).toFixed(2)+' mA';
 const rho=Number(res.values.rho||0.0000017);
 setLive(voltage.toFixed(2)+' V',(ledOn?amps.toFixed(4):'0.0000')+' A',resistance.toFixed(1)+' Ω',rho.toExponential(2)+' Ω·m');
 consoleReadout(ledOn?'PATH DETECTED':'CHECK POLARITY / SWITCH',voltage+' V',ledOn?ma:'0 mA',ledOn?'ON (simplified)':'OFF');
 if(!first)coach('🔄 LED polarity mistake','The LED is connected in reverse in the detected sample path. LEDs are polarised components.','Swap the LED connections so the battery positive side reaches the anode (+), and the cathode (−) returns to battery negative.');
 else if(openSwitch)coach('⏻ Open switch detected','The circuit path contains a switch that is open, so current cannot complete the loop.','Double-click the switch and change its state to Closed.');
 else if(voltage<=vf)coach('🔋 Not enough forward voltage','The source voltage is not greater than the LED forward-voltage drop in this simplified model.','Use a suitable low-voltage source and an LED/resistor combination within component ratings.');
 else if(amps>0.03)coach('⚠ Current may be too high','The estimated LED current is above 30 mA in this simplified model. This may exceed the rating of many indicator LEDs.','Increase the series resistance and check the LED datasheet. Keep experiments low-voltage.');
 $('message').textContent=ledOn?'Circuit detected! Estimated current: '+ma+'. Your LED is glowing — tiny engineering victory!':'The path exists, but polarity, voltage or a switch may prevent LED operation.';
}
function resetLab(){
 [...parts.keys()].forEach(id=>{const p=parts.get(id);scene.remove(p.root);scene.remove(p.label);parts.delete(id);});
 clearWires();serial=0;createModel('battery',-3,-1.4);createModel('resistor',-.8,-1.4);createModel('led',1.35,-1.4);createModel('arduino',-2.5,1.45);createModel('breadboard',.1,1.5);createModel('switch',2.8,1.5);
 camera.position.set(8,8.5,11);controls.target.set(0,.3,0);controls.update();$('message').textContent='Starter workbench restored. Wire the battery, resistor and LED to try the sample circuit.';
}
function setMouse(e){const r=canvas.getBoundingClientRect();mouse.x=(e.clientX-r.left)/r.width*2-1;mouse.y=-(e.clientY-r.top)/r.height*2+1;}
const raycaster=new THREE.Raycaster(),mouse=new THREE.Vector2();
function intersections(e){setMouse(e);raycaster.setFromCamera(mouse,camera);return raycaster.intersectObjects(scene.children,true);}
function findTerm(o){while(o){if(o.userData?.terminal)return o;o=o.parent;}return null;}
function findPart(o){while(o){if(o.userData?.partId)return o;o=o.parent;}return null;}
let down=null;
const dragPlane=new THREE.Plane(new THREE.Vector3(0,1,0),-.12),offset=new THREE.Vector3();
canvas.addEventListener('pointerdown',e=>{
 if(e.button!==0)return;const hits=intersections(e),term=hits.map(h=>findTerm(h.object)).find(Boolean);
 if(term){
  if(!wireStart){wireStart=term;$('message').textContent='Selected terminal '+term.userData.name+'. Select a second terminal.';}
  else if(wireStart!==term){
   if(checkConnection(wireStart,term)){drawWire(wireStart,term);$('message').textContent='Wire connected: '+wireStart.userData.name+' ↔ '+term.userData.name;}
   wireStart=null;
  }else {wireStart=null;$('message').textContent='Wire selection cancelled.';}
  return;
 }
 const part=hits.map(h=>findPart(h.object)).find(Boolean);
 if(part){drag=part;controls.enabled=false;raycaster.setFromCamera(mouse,camera);const point=new THREE.Vector3();if(raycaster.ray.intersectPlane(dragPlane,point))offset.copy(point).sub(part.position);down={x:e.clientX,y:e.clientY};}
});
canvas.addEventListener('pointermove',e=>{
 if(!drag)return;setMouse(e);raycaster.setFromCamera(mouse,camera);const point=new THREE.Vector3();if(raycaster.ray.intersectPlane(dragPlane,point)){drag.position.x=point.x-offset.x;drag.position.z=point.z-offset.z;}
});
canvas.addEventListener('pointerup',()=>{drag=null;controls.enabled=true;});
canvas.addEventListener('dblclick',e=>{const hits=intersections(e),part=hits.map(h=>findPart(h.object)).find(Boolean);if(part)selectPart(part.userData.partId);});
document.querySelectorAll('[data-add]').forEach(b=>b.addEventListener('click',()=>{const n=parts.size;createModel(b.dataset.add,((n%4)-1.5)*1.5,Math.floor(n/4)*1.7+2.8);}));
$('clear').onclick=clearWires;$('simulate').onclick=simulate;$('reset').onclick=resetLab;
$('checkCode').onclick=()=>{
 const code=$('code').value,checks=['setup','loop','pinMode','digitalWrite'];const missing=checks.filter(x=>!code.includes(x));
 $('codeResult').textContent=missing.length?'Review: missing common sketch element(s): '+missing.join(', '):'Basic structure found: setup(), loop(), pinMode() and digitalWrite() are present. This is a text check, not compilation.';
};
function resize(){const w=canvas.clientWidth,h=canvas.clientHeight;if(!w||!h)return;renderer.setSize(w,h,false);camera.aspect=w/h;camera.updateProjectionMatrix();}
new ResizeObserver(resize).observe(canvas);resize();
function animate(){requestAnimationFrame(animate);controls.update();renderer.render(scene,camera);}animate();
resetLab();
</script>
</body>
</html>
"""

components.html(LAB_HTML, height=960, scrolling=False)
st.caption("CIRCUIT LAB is an interactive educational prototype. It uses a simplified continuity check for a sample LED circuit; it is not a full SPICE simulator and does not program or control physical Arduino hardware.")
st.markdown(
    "<div style='text-align:center; color:#9aacc8; padding:8px 0 18px;'>"
    "<strong>Designed &amp; Developed by Shaikh Naushad</strong><br>"
    "<span style='font-size:0.9em;'>Created with coding assistance from ChatGPT</span>"
    "</div>",
    unsafe_allow_html=True
)
