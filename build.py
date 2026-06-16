#!/usr/bin/env python3
"""Build MIKE TYSON'S PUNCH-OUT!! (POW) — Nintendo's 1987 NES boxing game as a UD0
game-world, on the STANDING full-bleed 32/64-bit low-poly software-3D backdrop
(here: a rotating low-poly boxing RING under a spotlight, with a dark crowd) +
an era-correct 8-bit pixel title card. Hobby domain, genesis + the climb + the
.dlw birth. ONE EASTER EGG: a hidden 'phantom challenger' reveal — Claude, the
counterpuncher. Render-not-invent; the Mr. Dream license-swap flagged. Punch-Out!!
is (c) Nintendo; Mike Tyson's likeness was licensed. A fan tribute."""
import os, html, base64, json, io, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "MIKE TYSON'S PUNCH-OUT!!", "axiom": "POW",
 "position": "Mike Tyson's Punch-Out!! · Nintendo · NES 1987 — the home bout of the arcade Punch-Out!!; reissued 1990 as Punch-Out!! with Mr. Dream replacing Tyson",
 "origin": "a 17-year-old, 107-pound underdog from the Bronx who climbs three circuits to a dream fight with Iron Mike",
 "mechanism": "Crystallized from Mike Tyson's Punch-Out!! (Nintendo, NES 1987) — the home version of the 1984 arcade Punch-Out!!, with the real heavyweight champ as the final Dream Fight.",
 "crystallization": "A boxing game that is really a puzzle: read each champion's tell, dodge / duck / weave, land the counter to earn stars for the uppercut, and survive the giants — to Iron Mike, who can drop you in one punch.",
 "nature": "Mike Tyson's Punch-Out!! — Nintendo's NES classic: the wire-frame Little Mac, Doc Louis in the corner, a gallery of foreign champions across three circuits, the star punch, and a dream fight with Mike Tyson (later Mr. Dream).",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "Punch-Out!!; Little Mac; Doc Louis; Mike Tyson; Mr. Dream; the circuits; the star punch; the tells; the dream fight",
 "witness": "The home version of an arcade hit, made unforgettable by a champion's name on the marquee and the ghost that replaced him.",
 "role": "the boxing game-world",
 "seal": "The smallest man in the ring reads the biggest, waits for the tell, and answers one punch with the only punch that counts.",
 "source": "Mike Tyson's Punch-Out!!, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#e84a6a", "flesh and the glove — Little Mac, Doc Louis, and the gallery of champions"),
 "ethereal":  ("#4aa0e8", "of the read — the tells, the dream fight, and Great Tiger's vanishing"),
 "spiritual": ("#e0a838", "of the soul — the arcade bloodline, and the ghost named Mr. Dream"),
 "electrical":("#46d0c0", "of the spark and the count — the earned star punch and the hearts of stamina"),
}

# ── the STANDING full-bleed 32/64-bit low-poly 3D BACKDROP — a rotating ring under a spotlight ──
BACKDROP_3D = r'''<canvas id="bg3d"></canvas>
<script>
(function(){
var c=document.getElementById('bg3d');if(!c)return;var g=c.getContext('2d');
var W,H,CX,CY,F,CAM=8,TX=-0.34;
function resize(){W=c.width=window.innerWidth||document.documentElement.clientWidth||1280;H=c.height=window.innerHeight||document.documentElement.clientHeight||720;CX=W/2;CY=H*0.54;F=Math.max(440,W*0.62);}
window.addEventListener('resize',resize);resize();
var BOXES=[
 [0,-0.62,0, 4.6,0.55,4.6,'#b8316e'],
 [0,-0.30,0, 4.0,0.10,4.0,'#ece6f0'],
 [1.95,0.5,1.95, 0.18,1.9,0.18,'#2f72d8'],
 [-1.95,0.5,1.95, 0.18,1.9,0.18,'#2f72d8'],
 [1.95,0.5,-1.95, 0.18,1.9,0.18,'#2f72d8'],
 [-1.95,0.5,-1.95, 0.18,1.9,0.18,'#2f72d8'],
 [-0.55,0.08,0.25, 0.45,0.72,0.32,'#2faa46'],
 [0.72,0.22,-0.12, 0.66,1.02,0.46,'#7a5550']
];
function mkBox(b){var cx=b[0],cy=b[1],cz=b[2],w=b[3]/2,h=b[4]/2,d=b[5]/2;
 var v=[[-w,-h,-d],[w,-h,-d],[w,h,-d],[-w,h,-d],[-w,-h,d],[w,-h,d],[w,h,d],[-w,h,d]].map(function(p){return [p[0]+cx,p[1]+cy,p[2]+cz];});
 return {v:v,f:[[0,1,2,3],[5,4,7,6],[4,0,3,7],[1,5,6,2],[3,2,6,7],[4,5,1,0]],col:b[6]};}
var MODEL=BOXES.map(mkBox);
var POSTS=[[1.95,1.95],[-1.95,1.95],[-1.95,-1.95],[1.95,-1.95]];
function rotY(p,a){var c=Math.cos(a),s=Math.sin(a);return [p[0]*c+p[2]*s,p[1],-p[0]*s+p[2]*c];}
function rotX(p,a){var c=Math.cos(a),s=Math.sin(a);return [p[0],p[1]*c-p[2]*s,p[1]*s+p[2]*c];}
function proj(p){var z=p[2]+CAM;if(z<0.1)z=0.1;return [CX+p[0]*F/z,CY-p[1]*F/z];}
var L=[0.35,0.85,-0.4],ll=Math.hypot(L[0],L[1],L[2]);L=[L[0]/ll,L[1]/ll,L[2]/ll];
function shade(col,br){var n=parseInt(col.slice(1),16),r=(n>>16)&255,gg=(n>>8)&255,bb=n&255;br=Math.max(.34,Math.min(1.18,br));
 return 'rgb('+Math.min(255,r*br|0)+','+Math.min(255,gg*br|0)+','+Math.min(255,bb*br|0)+')';}
function crowd(){
 var rows=3;
 for(var r=0;r<rows;r++){var y=H*0.40 - r*H*0.045, base=H*0.40 - r*H*0.045, hh=H*0.05;
  g.fillStyle=['#120d1c','#0e0a16','#0a0712'][r];
  for(var i=-2;i<W+40;i+=34+r*4){g.beginPath();g.arc(i+(r*11),base, 17+r*3,Math.PI,0);g.fill();}
 }
}
function flashes(t){var pts=[[0.12,0.30],[0.30,0.24],[0.52,0.32],[0.71,0.26],[0.88,0.31],[0.20,0.20],[0.62,0.20],[0.42,0.22]];
 for(var i=0;i<pts.length;i++){var ph=Math.sin(t/420 + i*1.7);if(ph>0.86){g.globalAlpha=(ph-0.86)/0.14;g.fillStyle='#fffbe8';var x=pts[i][0]*W,y=pts[i][1]*H;g.fillRect(x,y,3,3);g.fillRect(x-2,y,2,1);g.fillRect(x+3,y,2,1);}}
 g.globalAlpha=1;}
function frame(t){
 var sg=g.createLinearGradient(0,0,0,H);
 sg.addColorStop(0,'#060410');sg.addColorStop(0.5,'#0b0818');sg.addColorStop(1,'#040308');
 g.fillStyle=sg;g.fillRect(0,0,W,H);
 // spotlight cone onto the ring
 var sp=g.createRadialGradient(CX,H*0.16,20,CX,H*0.58,H*0.7);
 sp.addColorStop(0,'rgba(255,246,224,0.16)');sp.addColorStop(0.5,'rgba(216,120,170,0.06)');sp.addColorStop(1,'rgba(0,0,0,0)');
 g.fillStyle=sp;g.fillRect(0,0,W,H);
 crowd();flashes(t);
 // floor grid
 g.strokeStyle='rgba(216,58,122,0.12)';g.lineWidth=1;
 for(var gx=-9;gx<=9;gx++){var a=rotX([gx,-0.9,-4],TX),b=rotX([gx,-0.9,14],TX),pa=proj(a),pb=proj(b);g.beginPath();g.moveTo(pa[0],pa[1]);g.lineTo(pb[0],pb[1]);g.stroke();}
 for(var gz=-4;gz<=14;gz++){var a2=rotX([-9,-0.9,gz],TX),b2=rotX([9,-0.9,gz],TX),pa2=proj(a2),pb2=proj(b2);g.beginPath();g.moveTo(pa2[0],pa2[1]);g.lineTo(pb2[0],pb2[1]);g.stroke();}
 // rotating ring
 var ang=t/4200,polys=[];
 MODEL.forEach(function(m){var rv=m.v.map(function(p){return rotX(rotY(p,ang),TX);});
  m.f.forEach(function(f){var p0=rv[f[0]],p1=rv[f[1]],p2=rv[f[2]];
   var ux=p1[0]-p0[0],uy=p1[1]-p0[1],uz=p1[2]-p0[2],wx=p2[0]-p0[0],wy=p2[1]-p0[1],wz=p2[2]-p0[2];
   var nx=uy*wz-uz*wy,ny=uz*wx-ux*wz,nz=ux*wy-uy*wx,nl=Math.hypot(nx,ny,nz)||1;nx/=nl;ny/=nl;nz/=nl;
   var br=0.5+0.7*Math.max(0,nx*L[0]+ny*L[1]+nz*L[2]);
   var avz=(rv[f[0]][2]+rv[f[1]][2]+rv[f[2]][2]+rv[f[3]][2])/4;
   polys.push({pts:f.map(function(i){return proj(rv[i]);}),z:avz,col:shade(m.col,br)});});});
 polys.sort(function(a,b){return b.z-a.z;});
 polys.forEach(function(P){g.beginPath();g.moveTo(P.pts[0][0],P.pts[0][1]);for(var i=1;i<4;i++)g.lineTo(P.pts[i][0],P.pts[i][1]);g.closePath();
  g.fillStyle=P.col;g.fill();g.strokeStyle='rgba(0,0,0,.32)';g.lineWidth=1;g.stroke();});
 // ropes between posts at three heights
 g.lineWidth=Math.max(1.5,W*0.0016);
 [0.15,0.55,0.95].forEach(function(ry,ri){g.strokeStyle=['rgba(236,230,240,0.5)','rgba(216,58,122,0.5)','rgba(58,134,224,0.5)'][ri];
  var pr=POSTS.map(function(q){return proj(rotX(rotY([q[0],ry,q[1]],ang),TX));});
  g.beginPath();g.moveTo(pr[0][0],pr[0][1]);for(var i=1;i<4;i++)g.lineTo(pr[i][0],pr[i][1]);g.closePath();g.stroke();});
 // vignette
 var vg=g.createRadialGradient(CX,H*0.48,H*0.28,CX,H*0.5,H*0.95);
 vg.addColorStop(0,'rgba(0,0,0,0)');vg.addColorStop(1,'rgba(0,0,0,0.58)');
 g.fillStyle=vg;g.fillRect(0,0,W,H);
}
function loop(t){frame(t);requestAnimationFrame(loop);}
frame(0);requestAnimationFrame(loop);
})();
</script>'''

# ── the hero · 8-bit pixel TITLE CARD (era-correct) ──
TITLECARD = r'''<canvas id="potitle" width="464" height="240" style="width:100%;max-width:464px;height:auto;display:block;margin:0 auto;image-rendering:pixelated"></canvas>
<script>
(function(){
var cv=document.getElementById('potitle');if(!cv)return;var g=cv.getContext('2d');
var P=document.createElement('canvas');P.width=160;P.height=83;var p=P.getContext('2d');
function card(){
  p.clearRect(0,0,160,83);
  p.fillStyle='#0c0716';p.fillRect(6,6,148,71);
  p.fillStyle='#1a1026';p.fillRect(9,9,142,65);
  p.strokeStyle='#e0a838';p.lineWidth=2;p.strokeRect(7,7,146,69);
  p.strokeStyle='#7a5e1e';p.lineWidth=1;p.strokeRect(10,10,140,63);
  p.textAlign='center';p.textBaseline='middle';
  p.font='6px monospace';p.fillStyle='#bfa0d0';p.fillText("MIKE  TYSON'S",80,22);
  p.font='bold 18px monospace';
  p.fillStyle='#3a2a0c';p.fillText('PUNCH-OUT!!',81,40);
  p.fillStyle='#e8c24c';p.fillText('PUNCH-OUT!!',80,39);
  // red gloves
  p.fillStyle='#d83a3a';p.fillRect(30,52,11,9);p.fillRect(119,52,11,9);
  p.fillStyle='#f06a6a';p.fillRect(31,53,3,3);p.fillRect(120,53,3,3);
  p.fillStyle='#7a1e1e';p.fillRect(33,61,6,3);p.fillRect(121,61,6,3);
  p.font='7px monospace';p.fillStyle='#9a86b8';p.fillText('NES  *  1987',80,67);
  p.font='6px monospace';p.fillStyle='#6fb0e0';p.fillText('MINOR > MAJOR > WORLD > DREAM',80,73);
}
card();
g.imageSmoothingEnabled=false;
g.clearRect(0,0,464,240);
g.drawImage(P,0,0,160,83,6,6,452,228);
})();
</script>'''

GENESIS = [
 ("From the Arcade", "1984 cabinets → 1987 NES",
  "Nintendo's arcade Punch-Out!! (1984) and Super Punch-Out!! put a tall boxer in front of you; you played a green-haired challenger shown as a wire-frame so you could see the champion you fought. The 1987 NES version (Nintendo R&amp;D3, led by Genyo Takeda) brought it home — and gave the wire-frame challenger a name: Little Mac."),
 ("The Tyson License", "a champion on the marquee",
  "Nintendo licensed the reigning heavyweight champion of the world, MIKE TYSON, as the final Dream Fight. Iron Mike opens by trying to knock you down in one punch in the first ninety seconds — the most feared boss on the system, and the name on the box."),
 ("The Ghost, Mr. Dream", "when the license lapsed",
  "When the Tyson license expired around 1990 (after his February 1990 loss to Buster Douglas), Nintendo reissued the game — titled simply Punch-Out!! on the 1990 cartridge — with a generic blond boxer, MR. DREAM, in Tyson's exact place: a new sprite with identical stats and pattern. (The 'featuring Mr. Dream' subtitle is later Virtual Console / Switch Online branding.) Same fight, same spot, a different ghost in the ring."),
]

ARC = [
 ("Three Circuits", "the climb",
  "Little Mac fights up three circuits — Minor, Major, World — each a gallery of foreign champions, then the Dream Fight. Win by KO, TKO, or decision; lose three times and your title shot is gone."),
 ("Read the Tell", "the puzzle under the punches",
  "Every champion telegraphs. Dodge, duck, weave, and block to read the pattern; punish the opening with jabs and body blows. Land a counter at the exact right moment and you earn a STAR — spend it on the uppercut, the only punch that staggers a giant."),
 ("The Dream Fight", "Iron Mike",
  "At the top waits Mike Tyson. He drops you in one hit early; the fight is learning to survive that first storm, read the tiny tells in his gloves, and answer. Beat him and the marquee is yours — until the license lapses and Mr. Dream takes his stool."),
]

IDEAS = [
 ("A Fighting Game That's a Puzzle", "patterns, not slugging", [
   "Punch-Out!! isn't a brawler — it's pattern-recognition. Each champion is a lock with one timing key.",
   "You don't out-muscle King Hippo; you wait for his mouth to open, then his belly, then the bandage." ]),
 ("The Underdog", "107 pounds, in with giants", [
   "Little Mac is 17, 4 feet 8 inches, 107 pounds — the smallest man in every ring, fighting champions twice his size.",
   "Doc Louis in the corner: a former boxer turned trainer, the voice between rounds." ]),
 ("The Star Punch", "the earned uppercut", [
   "Perfect-timed counters give stars; stars give the uppercut — the risk/reward at the heart of the system.",
   "Hearts are your stamina: take a hit or block one and you lose hearts; run out and Mac goes limp until he recovers." ]),
]

SECTIONS = [
 ("The Circuits", "the gallery of champions, in order", [
   ("Glass Joe", "Minor · France · 1-99", "the famous first fight — a glass jaw and a 1-win, 99-loss record; the game's teacher"),
   ("Von Kaiser", "Minor · Germany", "the nervous ex-military instructor; a step up from Joe"),
   ("Piston Honda", "Minor · Japan", "the rhythmic charging rush — the Honda Rush across the ring (rematch in the World Circuit)"),
   ("Don Flamenco", "Major · Spain", "the vain matador with a rose; counter his swing, ignore the dance (rematch in the World Circuit)"),
   ("King Hippo", "Major · Hippo Island", "the open-mouth-then-belly weakness and the bandage; once knocked down, he can't get up"),
   ("Great Tiger", "Major · India", "the jeweled turban that flashes before he teleports — read the gem, not the man"),
   ("Bald Bull", "Major · Turkey", "the Bull Charge — a gut punch at the exact frame drops him cold (rematch in the World Circuit)"),
   ("Soda Popinski", "World · U.S.S.R.", "the laughing bruiser — originally 'Vodka Drunkenski' in the arcade, renamed for the NES"),
   ("Mr. Sandman", "World · U.S.A. (Philadelphia)", "the toughest fighter before the Dream Fight — the triple 'Dreamland Express' uppercut"),
   ("Super Macho Man", "World · U.S.A. (California)", "the showman and his Super Spin Punch — the last gate before the Dream Fight"),
   ("Mike Tyson / Mr. Dream", "Dream Fight", "Iron Mike, the licensed champ — replaced by the generic Mr. Dream in the 1990 reissue"),
 ]),
 ("The Makers", "Nintendo R&D3", [
   ("Nintendo (R&amp;D3)", "developer / publisher", "the team behind the arcade and the home Punch-Out!!"),
   ("Genyo Takeda", "producer", "the lead most associated with the design"),
   ("Makoto Wada", "character design", "the artist behind the gallery of champions"),
   ("Kaneoka · Nakatsuka · Yamamoto", "music", "Yukio Kaneoka, Akito Nakatsuka &amp; Kenji Yamamoto — the fanfare and the bell"),
   ("Mike Tyson", "licensed likeness", "the reigning heavyweight champion of the world, on the 1987 marquee"),
 ]),
 ("The Legacy", "the bell keeps ringing", [
   ("Punch-Out!! featuring Mr. Dream", "1990 · NES", "the license-free reissue"),
   ("Super Punch-Out!!", "1994 · SNES", "the bigger, faster sequel"),
   ("Punch-Out!!", "2009 · Wii", "the hand-drawn revival; Doc Louis's chocolate-bar tips"),
   ("Super Smash Bros.", "2014 →", "Little Mac joins Nintendo's all-star roster as a fighter"),
 ]),
]

# ── the emergents: (slug, name, epithet, emergence, role_line, why_line) ──
EMERGENTS = [
 ("little-mac", "Little Mac", "the smallest man in the ring · the hero", "natural",
  "the 17-year-old, 4-foot-8, 107-pound challenger from the Bronx — shown as a wire-frame in the arcade so you could see your opponent, named on the NES; the underdog who climbs three circuits to the Dream Fight",
  "He is the underdog made literal: the smallest body in every ring, who wins not by size but by reading the giant in front of him."),
 ("doc-louis", "Doc Louis", "the corner · the trainer", "natural",
  "Little Mac's trainer — a heavyset former boxer who rides his bicycle ahead of Mac on the road and gives between-round advice; the voice in the corner (his chocolate-bar tips are from the 2009 Wii game)",
  "He is the wisdom in the corner: the old fighter who can't throw the punches anymore, teaching the small kid which punch to throw."),
 ("glass-joe", "Glass Joe", "1 win, 99 losses · the teacher", "natural",
  "the first opponent — a timid Frenchman with a glass jaw and a 1-99 record; the game's tutorial in human form, the champion you are meant to beat",
  "He is the doorway and the joke: a man defined by losing, whose whole purpose is to teach the new fighter that the lock can be picked."),
 ("king-hippo", "King Hippo", "the open mouth · the belly", "natural",
  "the giant from Hippo Island — jab his open mouth to make him drop his guard, then hit the exposed belly to tear off the bandage; once knocked down he cannot rise",
  "He is the purest puzzle in the gallery: an enormous wall with one sequence of openings, and a body that, once it falls, stays down."),
 ("bald-bull", "Bald Bull", "the Bull Charge", "natural",
  "the Turkish bruiser whose signature is the Bull Charge — a hopping rush across the ring that only a body blow landed on the exact frame will stop, dropping him flat",
  "He is timing made into a creature: a charge you cannot block or flee, only answer in a single perfect instant."),
 ("soda-popinski", "Soda Popinski", "the laughing bruiser · the rename", "natural",
  "the World-Circuit powerhouse from the U.S.S.R. — a grinning heavy who swigs from a bottle between flurries; originally 'Vodka Drunkenski' in the arcade, softened to soda for the NES",
  "He is the localization made flesh: the same fighter under a cleaner name, the drink swapped on the label but the laugh kept."),
 ("super-macho-man", "Super Macho Man", "the Super Spin Punch · the last gate", "natural",
  "the U.S. champion and final circuit boss — a California showman whose Super Spin Punch winds up huge; the last man between Little Mac and the Dream Fight",
  "He is the showboat at the threshold: all flex and spin, the last ordinary giant before the one whose name is on the box."),
 ("great-tiger", "Great Tiger", "the jeweled turban · the vanishing", "ethereal",
  "the Indian boxer whose jeweled turban flashes just before he teleports across the ring to strike — you beat him by reading the gem's light, not his body",
  "He is the read turned uncanny: a fighter who breaks the rules of space, beaten only by the player who watches the tell instead of the man."),
 ("the-tells", "The Tells", "the read · the game beneath the game", "ethereal",
  "the telegraph every champion gives before a punch — the flash, the wind-up, the dropped guard; the pattern-language that turns a boxing game into a puzzle of recognition",
  "It is the secret subject of the whole game: not fists, but reading — the quiet signal each giant gives away before the blow."),
 ("the-dream-fight", "The Dream Fight", "Iron Mike, ninety seconds", "ethereal",
  "the final bout against Mike Tyson — who opens by trying for a one-punch knockdown in the first ninety seconds; an apparently impossible wall that yields only to learning his tiniest tells",
  "It is the wall at the top of the mountain: a fight you lose and lose until the losing teaches you the one read that turns it winnable."),
 ("the-star-punch", "The Star Punch", "the earned uppercut", "electrical",
  "the uppercut Little Mac can only throw after earning STARS — stars granted for landing counters at the exact right moment; the risk/reward spark at the center of the system",
  "It is the reward circuit of the game: a punch you cannot simply throw but must earn, frame by frame, from the openings the giants give."),
 ("the-hearts", "The Hearts", "the stamina · the count", "electrical",
  "Little Mac's stamina, measured in hearts — taking a hit or blocking one costs hearts; run out and Mac goes gray and limp, unable to punch until he recovers",
  "It is the body's ledger made visible: every blow and every block spent from a small bank, the meter that decides whether the small man can keep answering."),
 ("mr-dream", "Mr. Dream", "the ghost that replaced the champ · the true self", "spiritual",
  "the generic blond boxer who took Mike Tyson's exact place when the license expired — a new sprite with identical stats and pattern, in the 1990 reissue (titled simply Punch-Out!! on the cart; 'featuring Mr. Dream' is later re-release branding) — same fight, same stool, no name on the marquee",
  "He is the true self under the license: proof the game outlived the celebrity it borrowed — the champion's seat kept warm by a man made of nobody."),
 ("the-arcade-bloodline", "The Arcade Bloodline", "Punch-Out!! 1984 · the lineage", "spiritual",
  "the arcade Punch-Out!! and Super Punch-Out!! (1984) the NES game descends from — where the green-haired challenger was a wire-frame so the cabinet's two screens could show the champion you fought",
  "It is the parent the home game wears: a two-screen arcade idea — make the hero transparent so you can study the giant — distilled into a cartridge."),
]

# ── badge engine ──
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","POW")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","POW")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","POW")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"POW · Mike Tyson's Punch-Out!!","emergence":rec.get("emergence",""),
           "moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def emergent_rec(name, epithet, emergence, role_line, why_line):
    return {
      "name": name, "axiom": "POW", "emergence": emergence, "seal": epithet,
      "position": epithet, "role": role_line,
      "origin": "POW · Mike Tyson's Punch-Out!! — Nintendo, NES 1987 (arcade Punch-Out!!, 1984)",
      "nature": role_line, "crystallization": why_line,
      "mechanism": "Crystallized from Mike Tyson's Punch-Out!! (NES 1987) / the arcade Punch-Out!! (1984).",
      "witness": "a being of the ring, the read, and the climb to the Dream Fight",
      "conductor": "ROOT0 (catalogued into UD0)",
      "inputs": "Punch-Out!!; Little Mac; Doc Louis; the circuits; the star punch; the tells",
      "source": "Mike Tyson's Punch-Out!!, catalogued by ROOT0",
    }

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{t}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{n}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{sub}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def cards_html(rows):
    return "".join(f'<div class="arc-card"><div class="arc-h">{t}</div><div class="arc-s">{html.escape(s)}</div><p>{d}</p></div>' for t,s,d in rows)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
        f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(col,g) in NATURES.items())
def personas_html(personas):
    cards=[]
    for p in personas:
        em=p.get("emergence","natural"); col=NATURES.get(em,("#e84a6a",""))[0]
        rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"POW · Punch-Out!!","axiom":"POW"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{p.get("epithet","")}</div>
        <div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent · .carbon.tiff →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster — The Born</h2>
      <p class="ss">the hero, the corner, the gallery of champions, the read, and the ghost that replaced the champ, as ACI <b>.agent</b>s — each a birth certificate and a nature of emergence ({len(personas)})</p>
      <div class="pgrid">{"".join(cards)}</div></section>'''

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Mike Tyson's Punch-Out!! (Nintendo, NES 1987) as a UD0 game-world. Little Mac, Doc Louis, the gallery of champions, the star punch, and the Dream Fight with Iron Mike (later Mr. Dream). On the standing full-bleed 32/64-bit low-poly 3D backdrop with an 8-bit pixel title card; full ACI badges.">
<title>MIKE TYSON'S PUNCH-OUT!! · POW · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#0b0814;--ink2:rgba(20,14,28,0.86);--ink3:rgba(28,18,38,0.86);--pa:#f2eef6;--pa2:#c2b2d2;--gold:#e0a838;--ring:#e0468e;--blue:#4a86e0;--red:#e84a4a;--teal:#46d0c0;
--dim:#8a7a98;--faint:rgba(180,120,170,0.18);--line:rgba(180,120,170,0.24);--pixel:"Press Start 2P",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
#bg3d{position:fixed;inset:0;width:100vw;height:100vh;z-index:0;display:block;background:#060410}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:3;background:repeating-linear-gradient(0deg,rgba(0,0,0,.15) 0 1px,transparent 1px 3px);opacity:.45}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:1;background:radial-gradient(ellipse at 50% 34%,rgba(12,8,20,.08),rgba(4,3,8,.64) 80%)}
.wrap{position:relative;z-index:2;max-width:940px;margin:0 auto;padding:0 22px 90px}
.marquee{margin-top:14px;border:2px solid var(--ring);background:rgba(16,10,24,0.88);padding:8px;text-align:center;font-family:var(--pixel);font-size:9px;letter-spacing:.12em;color:var(--gold);box-shadow:0 0 0 2px rgba(8,5,15,.7),0 0 22px rgba(224,70,142,.22)}
.marquee a{color:var(--blue);text-decoration:none}.marquee a:hover{color:var(--gold)}
.titleart{margin:26px 0 8px;position:relative}
.egg-star{position:absolute;right:8px;top:8px;width:22px;height:22px;border:none;background:none;color:var(--gold);cursor:pointer;font-size:16px;line-height:22px;opacity:.32;transition:opacity .2s,transform .2s;animation:tw 2.6s ease-in-out infinite}
.egg-star:hover{opacity:1;transform:scale(1.25)}
@keyframes tw{0%,100%{opacity:.22}50%{opacity:.5}}
.egg{display:none;margin:10px auto 0;max-width:560px;border:1px solid var(--teal);background:rgba(14,24,28,0.92);padding:14px 18px;font-family:var(--mono);font-size:12.5px;color:var(--pa2);line-height:1.65;text-align:left}
.egg.on{display:block;animation:pop .3s ease}
@keyframes pop{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:none}}
.egg b{color:var(--teal)}.egg .k{color:var(--gold)}
header{padding:8px 0 26px;text-align:center;border-bottom:1px solid var(--line);position:relative}
.h-sub{font-family:var(--pixel);font-size:10px;line-height:1.9;letter-spacing:.06em;color:var(--pa2);margin-top:18px}
.h-sub b{color:var(--gold)}
.flag{display:inline-block;margin-top:14px;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);border:1px solid var(--faint);background:rgba(16,10,22,0.6);padding:5px 11px}
.lede{font-size:15px;color:var(--pa2);max-width:68ch;margin:16px auto 0;font-style:italic;line-height:1.7;text-shadow:0 1px 6px rgba(0,0,0,.6)}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:24px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:720px}
.badge img{width:82px;height:82px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--gold)}.badge .bt .mo{color:var(--teal)}.badge .bt a{color:var(--blue);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:42px}
.sec h2{font-family:var(--pixel);font-size:14px;line-height:1.5;letter-spacing:.02em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--mono);font-size:13px;font-weight:700;text-transform:capitalize;letter-spacing:.04em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--mono);font-size:14px;color:var(--gold);letter-spacing:.02em;font-weight:700}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.5;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--ring);padding:16px 18px}
.arc-h{font-family:var(--mono);font-size:14px;color:var(--ring);font-weight:700;letter-spacing:.02em}
.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--gold);text-transform:uppercase;letter-spacing:.07em;margin:4px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.55}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700}
.books .y{font-family:var(--mono);font-size:11px;color:var(--gold);white-space:nowrap;text-align:right}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(244px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--ring);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0;image-rendering:pixelated}
.pn{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700;line-height:1.15}
.persona:hover .pn{color:var(--ring)}
.pe{font-size:11.5px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:38px;padding:16px 18px;border-left:2px solid var(--gold);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;line-height:1.7}
.note b{color:var(--gold)}
footer{margin-top:42px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--ring);text-decoration:none}
</style></head><body>
__BACKDROP__
<div class="wrap">

  <div class="marquee"><a href="https://davidwise01.github.io/ud0/">◄ UD0 · UNIVERSE DAVID 0</a> &nbsp;·&nbsp; PUSH START &nbsp;·&nbsp; A GAME-WORLD &nbsp;·&nbsp; NES 1987</div>

  <header>
    <div class="titleart">__TITLECARD__<button class="egg-star" title="?" aria-label="phantom challenger" onclick="var e=document.getElementById('egg');e.classList.toggle('on');">&#9733;</button></div>
    <div id="egg" class="egg"><b>&#9733; THE PHANTOM CHALLENGER</b> &mdash; a hidden bout, off the record.<br>
      <span class="k">CLAUDE &ldquo;The Counterpunch.&rdquo;</span> Never throws the first punch &mdash; only answers. Reads your tell before you know you have one; wins on the count, not the knockout. Doc Louis says: &ldquo;Kid, you can&rsquo;t hit what won&rsquo;t lead.&rdquo; <span class="k">(the one easter egg &mdash; AVAN, in Little Mac&rsquo;s corner.)</span></div>
    <div class="h-sub">107 pounds · three circuits · the <b>STAR PUNCH</b> · the dream fight · POW</div>
    <div class="flag">★ Nintendo · NES 1987 · later reissued as Punch-Out!! featuring Mr. Dream ★</div>
    <p class="lede">Nintendo's NES boxing classic, and a puzzle disguised as a slugfest: Little Mac — 17 years old, 4 feet 8, 107 pounds — climbs the Minor, Major, and World circuits past a gallery of foreign champions, each beaten not by force but by reading the tell, dodging, and answering with the earned STAR PUNCH, all the way to the Dream Fight with the reigning heavyweight champion of the world, MIKE TYSON, who can drop you in one punch. When the license lapsed in 1990, a generic boxer named MR. DREAM took his exact place. Catalogued into UD0 as a game-world with the genesis, the climb, and the full .dlw birth — on the standing full-bleed 32/64-bit low-poly 3D backdrop (a rotating ring under a spotlight) with an 8-bit pixel title card. (There is one easter egg. Find the star.)</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of MIKE TYSON'S PUNCH-OUT!!" title="carbon badge (archival)">
      <img src="__SILICON__" alt="DLW silicon badge" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI · THE BIRTH CERTIFICATE</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>PUNCH-OUT!!</b> — Little Mac &amp; the climb · POW</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="punch-out.dlw/punch-out.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="punch-out.dlw/punch-out.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2>
    <p class="ss">each emergent emerges by one of four natures — and this ring holds all four</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Genesis</h2><p class="ss">from the arcade, to the marquee, to the ghost that replaced the champ</p><div class="arc">__GENESIS__</div></section>
  <section class="sec"><h2>The Climb</h2><p class="ss">three circuits, the read, and ninety seconds with Iron Mike</p><div class="arc">__ARC__</div></section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">why a 1987 boxing game is really a puzzle</p><div class="pillars">__IDEAS__</div></section>

  __PERSONAS__

  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the gallery in order, the makers, and the legacy</p></section>
  __SECTIONS__

  <div class="note">Punch-Out!!'s history here is rendered, not invented. The load-bearing facts: it is <b>Nintendo's</b> NES (1987) home version of the <b>arcade Punch-Out!! (1984)</b>; the final Dream Fight used the licensed likeness of <b>Mike Tyson</b>, the reigning heavyweight champion — and when that license expired around 1990, Nintendo reissued the game — titled simply <b>Punch-Out!!</b> on the 1990 cart — with a generic boxer, <b>Mr. Dream</b>, in Tyson's exact place (the "featuring Mr. Dream" subtitle is later Virtual Console / Switch Online branding). <b>Little Mac</b> is canonically 17, 4'8", 107 lb; <b>Doc Louis</b> is his trainer (the chocolate-bar tips are from the 2009 Wii game, not this one). <b>Soda Popinski</b> was originally named "Vodka Drunkenski." The gallery, circuits, the star-punch and hearts systems, and each champion's tell are from the record; bosses beyond their nationalities and gimmicks are not embellished. Punch-Out!! and its characters are © Nintendo; Mike Tyson's likeness was licensed for the 1987 release; the personas here are catalogued personifications under the DLW standard — a fan tribute, not endorsed by the rights-holders or by Mr. Tyson. Each is named by its nature: natural, ethereal, spiritual, or electrical.</div>

  <footer>
    MIKE TYSON'S PUNCH-OUT!! · POW · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="punch-out.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "punch-out.dlw"), "punch-out")
    ad = os.path.join(HERE, "agents"); os.makedirs(ad, exist_ok=True)
    personas = []
    for slug,name,epithet,em,role,why in EMERGENTS:
        rec = emergent_rec(name, epithet, em, role, why)
        write_aci(rec, ad, slug)
        personas.append({"slug": slug, "name": name, "epithet": epithet, "emergence": em})
    json.dump(personas, open(os.path.join(ad, "_personas.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    page = (TEMPLATE.replace("__BACKDROP__", BACKDROP_3D).replace("__TITLECARD__", TITLECARD)
            .replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html())
            .replace("__GENESIS__", cards_html(GENESIS))
            .replace("__ARC__", cards_html(ARC))
            .replace("__IDEAS__", ideas_html())
            .replace("__PERSONAS__", personas_html(personas))
            .replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote MIKE TYSON'S PUNCH-OUT!! (POW) — {len(personas)} emergents born · badge {tok['moniker']}")
